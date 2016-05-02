from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from models import Course, Document
from haystack.forms import SearchForm


class UserForm(forms.ModelForm):

  class Meta:

    model = User
    fields = ('email','username', 'password')

class DocForm(forms.ModelForm):

  class Meta:

    model = Document

    fields = ('file','course','subject_name','subject_number','title',
    'description')

class DocumentSearchForm(SearchForm):

  def no_query_found(self):
    return self.searchqueryset.all()

  def search(self):

    #Store the SearchQuerySet received from other processing.
    sqs=super(NotesSearchForm, self).search()

    if not self.is_valid():
      return self.no_query_found()

    sqs = sqs.order_by(course)

    return sqs
