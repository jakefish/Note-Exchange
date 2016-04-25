from notes_app.models import Course




path = '/Users/fishb1jw/projects/Note-Exchange/notes_app/courses.txt'
data = open(path, 'r').read()
course_list = data.splitlines()

for course in course_list: 
  c = Course(subject=course)
  c.save()
