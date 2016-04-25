import datetime
from haystack import indexes
from notes_app.models import Document, Course
import itertools

class DocumentIndex(indexes.SearchIndex, indexes.Indexable):

  text = indexes.CharField(document=True, use_template=True)
  course = indexes.CharField(model_attr="course")
  subject_name = indexes.CharField(model_attr="subject_name")
  subject_number = indexes.IntegerField(model_attr="subject_number")
  description = indexes.CharField(model_attr="description")
  title = indexes.CharField(model_attr="title")
  pub_date = indexes.DateTimeField(model_attr="pub_date")


  def get_model(self):
    print 2
    print Document
    return Document

  def index_queryset(self, using=None):

    #Used when entire index for model is updated.
    print 1
    return self.get_model().objects.all()

class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    
    text = indexes.CharField(document=True, use_template=True)

    
    def get_model(self):
        return Course
    
    def index_queryset(self):
        return self.get_model().objects.all()