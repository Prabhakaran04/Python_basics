print('''
      1.Hospital
      2.Medical
      3.School
      4.Defect
      5.Bug
      6.Sign
      7.Voice
''')
First_title = str(input(
    'Type one content from the above options,related to which your Project name will be generated: '))
Middle_title = [' Management ', ' Tracking ', ' Language ', " Recognition "]
last_title = 'System '
this = 'prabhakaran'
# Provides Management as the middle title if one from the following title is selected
if First_title == "Hospital" or First_title == "Medical" or First_title == "School":
    print('Congrats, Your project name is: ',
          First_title + Middle_title[0] + last_title)
# Provides Tracking as the middle title if one from the following title is selected
elif First_title == 'Defect' or First_title == 'Bug':
    print('Congrats, Your project name is: ',
          First_title + Middle_title[1] + last_title)
# Provides Language as the middle title if one from the following title is selected
elif First_title == "Sign":
    print('Congrats, Your project name is: ',
          First_title + Middle_title[2] + last_title)
# Provides Recognition as the middle title if one from the following title is selected
elif First_title == "Voice":
    print('Congrats, Your project name is: ',
          First_title + Middle_title[3] + last_title)
#
"""
 if your input doesn't match with tha provided options 
 this will get executed
"""
print('Invalid Input')
print(this)
