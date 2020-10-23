print("Title of program: Encouragement bot")
print()
while True:
  description = input("What do you need my help for?")

  list_of_words = description.split()

  subject_list = []
  answer_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "pythagoras":
      answer_list.append("a² + b² = c²")
      counter += 1
    if each_word == "circle":
      answer_list.append("Area: πr², Perimeter:2πr")
      counter += 1
    if each_word == "triangle":
      answer_list.append("Area: ½bh")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = answer_list[0] + " Hope this was helpful :)"

  else:

    answers = ""    
    for i in range(len(answer_list)-1):
      answer_list += answer_list[i] + ", "
    answers += "and " + answer_list[-1]
    output = answers + " Hope this was helpful :)"

  print()
  print(output)
  print()
