"""Front-server(get/post), server tests"""
import datetime

from django.test import TestCase
from .models import PhotoRequest
from .forms import *
# from django.test import Client


class PhotoRequestModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        PhotoRequest.objects.create(photo_name="Test_name", photo_date="2020-01-01 18:00:00.0", photo_file=None)

    def test_photo_name_label(self):
        photoRequest = PhotoRequest.objects.get(id=1)
        field_label = photoRequest._meta.get_field('photo_name').verbose_name
        self.assertEquals(field_label, 'Test_name')

    def test_date_label(self):
        photoRequest = PhotoRequest.objects.get(id=1)
        date = photoRequest._meta.get_field('photo_date').verbose_name
        self.assertEquals(date, '2020-01-01 18:00:00.0')

    def test_photo_name_max_length(self):
        photoRequest = PhotoRequest.objects.get(id=1)
        max_length = photoRequest._meta.get_field('photo_name').max_length
        self.assertEquals(max_length, 50)

    def file_correct(self):
        photoRequest = PhotoRequest.objects.get(id=1)
        photo_type = type(photoRequest._meta.get_field('photo_file'))
        self.assertEquals(photo_type, "<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>")


class PhotoRequestFormTest(TestCase):

    def test_request_form_file_field_label(self):
        form = PhotoRequestForm()
        self.assertTrue(
            form.fields['photo_file'].label is None or form.fields['photo_file'].label == 'photo file')

    def test_request_form_date_field_help_text(self):
        form = PhotoRequestForm()
        self.assertEqual(form.fields['photo_date'].help_text, 'Enter a date between now and 4 weeks (default 3).')

    def test_request_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form_data = {'photo_date': date}
        form = PhotoRequestForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_request_form_date_too_far_in_future(self):
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form_data = {'photo_date': date}
        form = PhotoRequestForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        date = datetime.date.today()
        form_data = {'photo_date': date}
        form = PhotoRequestForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        date = datetime.timezone.now() + datetime.timedelta(weeks=4)
        form_data = {'photo_date': date}
        form = PhotoRequestForm(data=form_data)
        self.assertTrue(form.is_valid())
