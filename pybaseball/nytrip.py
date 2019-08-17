stuff =["Drunchie", "Pasta", "Sushi/japanese", 'Brunch', 'Korean', 'Chinese', 'Pastry','Ice cream']
result =[]
f = open("result.txt", "w")
for i in stuff:
    result.append(i.upper())
for r in result:
    result = "{}\n".format(r)
    f.write(result)
f.close()
