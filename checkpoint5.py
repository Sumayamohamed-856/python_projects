collegeStudents = {
  
'students': {
  'name': 'sumaya',
  'age':   22,
  'major': 'software',
  'year':  '2022',
  'classes': 'full stack'
 }

}

info_student = collegeStudents['students'].get('name', 'No featured team')

print(info_student)

remove = collegeStudents['students'].pop('year', 'not found')

print(collegeStudents)

collegeStudents['students']['gpa'] = 3.9

print(collegeStudents)

collegeStudents['students']['gpa'] = 4.0



print(collegeStudents)

collegeStudents['students']['few students'] = 'welcome'

print(collegeStudents)

sorted = sorted(collegeStudents['students'])

print(sorted)

for key, val, in collegeStudents.items():
  print('Highest_Gpa', max(val['value']))

for key, val, in collegeStudents.items():
  print('Lowest_Gpa', min(val['value']))