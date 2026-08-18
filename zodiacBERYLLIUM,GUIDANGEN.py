#ZODIAC CODE PROGRAM

#Enter birth year
year_of_birth = int(input("Enter your birth year: "))

#Check the year
if year_of_birth < 1900:
  print("Invalid year. The year of birth must be earlier than 1900.")
else:
  zodiac_number = (year_of_birth - 1900) % 12

  if zodiac_number == 0:
    zodiac = "Rat (鼠 / Shǔ)"

  elif zodiac_number == 1:

    zodiac = "Ox (牛 / Niú)"

  elif zodiac_number == 2:

      zodiac = "Tiger (虎 / Hǔ)"

  elif zodiac_number == 3:

      zodiac = "Rabbit (兔 / Tù)"

  elif zodiac_number == 4:

      zodiac = "Dragon (龙 / Lóng)"

  elif zodiac_number == 5:

      zodiac = "Snake (蛇 / Shé)"

  elif zodiac_number == 6:

      zodiac = "Horse (马 / Mǎ)"

  elif zodiac_number == 7:

      zodiac = "Goat (羊 / Yáng)"

  elif zodiac_number == 8:

      zodiac = "Monkey (猴 / Hóu)"

  elif zodiac_number == 9:

      zodiac = "Rooster (鸡 / Jī)"

  elif zodiac_number == 10:

      zodiac = "Dog (狗 / Gǒu)"

  else:

      zodiac = "Pig (猪 / Zhū)"

  # Display the result

  print(f"YOUR BIRTH YEAR: {year_of_birth}")

  print(f"YOU CHINESE ZODIAC: {zodiac}")
