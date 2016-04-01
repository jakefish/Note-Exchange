from notes_app.models import Course

# Read in file containing Central Michigan's courses and create course objects

path = '/Users/fishb1jw/capstone_project/note_exchange/notes_app/courses.txt'
data = open(path, 'r').read()
course_list = data.splitlines()

for course in course_list:
  c = Course(subject=course)
  c.save()
