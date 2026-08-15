import datetime
import calendar

name = input("Enter your name: ")
mood = input("How is your mood today? (happy/sad/stressed/tired/angry): ").lower()
energy = int(input("Enter your energy level (1-10): "))

today = datetime.datetime.now()

if mood == "happy":
    advice = "Share your positive energy with someone and do something creative today!"
elif mood == "sad":
    advice = "Take some rest, talk to a close friend, and be kind to yourself."
elif mood == "stressed":
    advice = "Take five deep breaths and divide your work into smaller tasks."
elif mood == "tired":
    advice = "Drink some water, take a short break, and try to sleep early tonight."
elif mood == "angry":
    advice = "Take a short walk and give yourself time to calm down before reacting."
else:
    advice = "Notice your feelings and do one small activity that makes you happy."

if energy >= 8:
    energy_advice = "Your energy is high—this is a great time to finish important tasks!"
elif energy >= 5:
    energy_advice = "Your energy is moderate—focus on one task at a time."
else:
    energy_advice = "Your energy is low—prioritize rest and avoid pushing yourself too hard."

print("\n--- Daily Mood Report ---")
print(f"Hello, {name}!")
print(f"Date: {today.strftime('%d %B %Y')}")
print(f"Today's Mood: {mood.capitalize()}")
print(f"Energy Level: {energy}/10")
print(f"\nMood Advice: {advice}")
print(f"Energy Advice: {energy_advice}")
print(f"\nCurrent Month: {calendar.month_name[today.month]}")