from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .forms import UserForm, DocForm, DocumentSearchForm
from .models import Document, Course
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from haystack.query import SearchQuerySet

def user_login(request):

  context = RequestContext(request)

  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']


    #authenticate user by checking username and password.
    user = authenticate(username=username, password=password)

    if user:

      if user.is_active: #make sure user is active, if they are log them in.
        login(request,user)
        return HttpResponseRedirect('/main/')

      else:
        return HttpResponse("Your account is disabled.")

    else:
      print "Invalid login details: {0}, {1}".format(username,password)
      return HttpResponse("Invalid login details supplied.")

  else:

    #render login page with the context
    return render_to_response('login.html',{}, context)

def register(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)

            # redirect user to thank you page.
            return HttpResponseRedirect('/main/thank_you/')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})

def thank_you(request):
  return render(request, 'thank_you.html')

def main(request):

  #If user is logged in, load the logged_in home page.
  if request.user.is_authenticated():
    return render(request,'logged_in.html')

  return render(request, 'main.html')

def logout_view(request):
  logout(request)

  #Log out user and render the logged out page.
  return render(request, 'logged_out.html')

def course_form(request):

  # Handle file and course choice upload.
  if request.method == 'POST':

    document_form = DocumentForm(request.POST, request.FILES)

    if document_form.is_valid():

      newdoc = Document(file = request.FILES['file'],
      document_subject = request.POST['document_subject'],
      )
      newdoc.save()

      #Redirect to thank_you page after completion
      return HttpResponseRedirect('/main/thank_you/')

  else:

    document_form = DocumentForm()

  #Render course page with the course choices and documents.
  return render(request,'course.html', {'document_form':document_form})

def doc_form(request):

  if request.method == 'POST':

    doc_form = DocForm(request.POST,request.FILES)

    if doc_form.is_valid():

      newdoc = Document.objects.create(**doc_form.cleaned_data)
      newdoc.save()

      return HttpResponseRedirect('/main/thank_you/')
  else:

    doc_form = DocForm()

  return render(request,'doc_form.html',{'doc_form':doc_form})

def search(request):
  print "-----------"
  print request.POST
  documents = SearchQuerySet().filter(content_auto=request.POST.get('search_text', ''))

  return render_to_response('ajax_search.html', {'documents' : documents})

def document(request, document_id=1):

    return render(request, 'document.html',
                  {'document': Document.objects.get(id=document_id) })

def more_info(request):

    return render(request,'more_info.html')
