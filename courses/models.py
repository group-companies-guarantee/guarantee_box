"""File with classes which describe tables in database."""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
from students.models import Student, Teacher


class Subject(models.Model):
    """Describe the courses_subject table in database.

    Subject is the theme of lesson.

    Arguments:
        models.Model: superclass where describe the fields
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        """Metadata class.

        When Django make Subject class, Meta override the ordering.
        """
        ordering = ['title']

    def __str__(self):
        """Override the str() behavior, for instance of class.

        Returns:
            self.title: Instance title
        """
        return self.title


class Course(models.Model):
    """Class describes courses_course table in db.

    Note: чтобы проставить атрибут 'course_done', если пользователь закончил курс
    можно прописать:

        class Meta:
            permissions = (
                ('course_done', 'Course done')
            )

    и отдельно для каждого пользователя можно делать:

        from guardian.shortcuts import assign_perm
        assign_perm('course_done', student, course)

        student.has_perm('course_done', course)
        True
    
    Это значит для конкретного 'student' и 'course'
    значение 'course_done' будет свое

    чтобы удалить атрибут:

        from guardian.shortcuts import remove_perm
        remove_perm('course_done', student, course)

        student.has_perm('course_done', course)
        False

    Arguments:
        models.Model: superclass where describe the fields
    """
    owner = models.ForeignKey(
        Teacher,
        related_name='courses_created',
        on_delete=models.CASCADE,
    )
    subject = models.ForeignKey(
        Subject,
        related_name='courses',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(
        Student,
        related_name='courses_joined',
        blank=True,
    )

    class Meta:
        ordering = ['-created']
        permissions = (
                ('course_done', 'Course done'),
        )

    def __str__(self):
        return self.title


class Module(models.Model):
    class Meta:
        ordering = ['order']
        permissions = (
                ('view_current_module', 'Can view current module'),
            )

    course = models.ForeignKey(
        Course,
        related_name='modules',
        on_delete=models.CASCADE,
        )
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    def __str__(self):
        return '{0}. {1}'.format(self.order, self.title)


class Content(models.Model):
    class Meta:
        ordering = ['order']

    module = models.ForeignKey(
        Module,
        related_name='contents',
        on_delete=models.CASCADE,
        )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            'model__in': (
                'text',
                'video',
                'image',
                'file',
                'question',
                'blockly',
                'c_plus_plus',
                )
            }
        )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])


class ItemBase(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='%(class)s_related',
        on_delete=models.CASCADE,
        )
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def render(self):
        return render_to_string('courses/content/{}.html'.format(
            self._meta.model_name), {'item': self})

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class Drag_and_drop(ItemBase):
    question = models.TextField()
    answer_1 = models.CharField(max_length=300, default='')
    answer_2 = models.CharField(max_length=300, default='')
    answer_correct = models.CharField(max_length=300, default='')


class Blockly(ItemBase):
    content = models.TextField()
    answer = models.CharField(max_length=300, default='')


class C_plus_plus(ItemBase):
    content = models.TextField()
    answer = models.CharField(max_length=300, default='')


class Question(ItemBase):
    content = models.TextField()
    answer = models.CharField(max_length=300, default='')


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()

