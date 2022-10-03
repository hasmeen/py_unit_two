# ask user's name
print("Hi there! I'm Chatwick, the chatbot! （っ＾▿＾)")
name = input("What's your name? ")

print("It's nice to meet you " + name + "! ")


name_of_location = input("Where are you from? ")

print("Oh my god! " + name_of_location + " sounds like a pleasant place to be from. ")

birth_year = input("What year were you born? ")
age = 2022 - int(birth_year)

if age < 18:
    print("Oh, hello there young one.")
elif 18 <= age < 30:
    print("Gosh! You're much younger than I am!")
elif 30 <= age < 60:
    print("Oh, we're about the same age!")
else:
    print("Wow, you're much older than I am")

print("What's your birthday? I bet I could guess your zodiac sign! ")
print("Please enter the day as a number and the month with a capital letter. Ex: 18 Ex: October")


# Main Code for zodiac sign
if __name__ == '__main__':
    d = int(input("Enter Day ->"))
    m = input("Enter the Month ->")

# Days and month with the range
def zodiac_sign(day, month):
    if month == ("December" or "december"):
        z_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == ("January" or "january"):
        z_sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif month == ("February" or "february"):
        z_sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month == ("March" or "march"):
        z_sign = 'Pisces' if (day < 21) else 'aries'
    elif month == ("April" or "april"):
        z_sign = 'Aries' if (day < 20) else 'taurus'
    elif month == ("May" or "may"):
        z_sign = 'Taurus' if (day < 21) else 'gemini'
    elif month == ("June" or "june"):
        z_sign = 'Gemini' if (day < 21) else 'cancer'
    elif month == ("July" or "july"):
        z_sign = 'Cancer' if (day < 23) else 'leo'
    elif month == ("August" or "august"):
        z_sign = 'Leo' if (day < 23) else 'virgo'
    elif month == ("September" or "september"):
        z_sign = 'Virgo' if (day < 23) else 'libra'
    elif month == ("October"or "october"):
        z_sign = 'Libra' if (day < 23) else 'scorpio'
    elif month == ("November" or "november"):
        z_sign = 'scorpio' if (day < 22) else 'sagittarius'
    print("You're a " + z_sign + "!")


# print
if __name__ == '__main__':
    zodiac_sign(d, m)

# Favorite number
number = input("What's your favorite number? ")
my_fave_number = float(3)
user_fave_number = float(number)
ratio = str(user_fave_number / my_fave_number)
#print("Woah, my number is ", ratio, " times as much as yours,", my_fave_number)
print("Woah, your favorite number ", user_fave_number , " is " , ratio, "times as big as my favorite number ", my_fave_number)

# Dream car
print("Let's talk about something else now. ")
dream_car = input("What's your dream car? ")
print("Wow! I've always wanted a ", dream_car, " as well!")

cost_of_car = float(input("How much does one cost these days? "))
interest_rate = float(input("Gosh, that sounds expensive! What's the annual interest rate for a loan for that car? "))
years_of_loan = float(input("Nice, and just curious, if you had to how many years would you have to take the loan out to pay for a " + dream_car + "? "))
number_of_payments = float(years_of_loan) * 12
monthly_interest = float((interest_rate / 100) / number_of_payments)
monthly_payment = float(monthly_interest * cost_of_car) / (1 - pow((1 + monthly_interest), (-1 * number_of_payments)))
total_cost = float(number_of_payments * monthly_payment)

print("If you bought the", dream_car, "you would have a monthly_payment of ", monthly_payment, "Your total cost is", total_cost, "I hope you can afford to make that purchase!.")

print("Anyways, that was fun. I've gotta go now, see you later " + name + "!")



