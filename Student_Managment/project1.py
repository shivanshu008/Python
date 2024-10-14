# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:41:57 2024

@author: shivanshu gaurav
"""

import datetime
import matplotlib.pyplot as plt

# Define an empty dictionary to store habits
habits = {}

# Function to add a new habit
def add_habit():
    habit_name = input("Enter the name of the habit to track: ")
    habits[habit_name] = {"start_date": datetime.date.today(), "completed": []}

# Function to mark a habit as completed for today
def complete_habit():
    habit_name = input("Which habit did you complete today? ")
    if habit_name in habits:
        today = datetime.date.today()
        habits[habit_name]["completed"].append(today)
        print(f"Habit '{habit_name}' marked as completed for {today}.")
    else:
        print("Habit not found!")

# Function to view all habits
def view_habits():
    if not habits:
        print("No habits to track.")
    else:
        for habit, details in habits.items():
            completion_rate = len(details["completed"])
            print(f"Habit: {habit}, Days Completed: {completion_rate}")

# Function to visualize progress (basic plot example)
def show_progress():
    habit_name = input("Enter the habit name to visualize progress: ")
    if habit_name in habits:
        completion_dates = habits[habit_name]["completed"]
        days = range(1, len(completion_dates) + 1)
        plt.bar(days, [1]*len(completion_dates))  # A bar for each completed day
        plt.title(f"Progress for {habit_name}")
        plt.xlabel('Days')
        plt.ylabel('Completion')
        plt.show()
    else:
        print("Habit not found!")

# Main habit tracker menu
def habit_tracker():
    while True:
        print("\n--- Habit Tracker Menu ---")
        print("1. Add a Habit")
        print("2. Complete a Habit")
        print("3. View Habits")
        print("4. Show Progress")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_habit()
        elif choice == '2':
            complete_habit()
        elif choice == '3':
            view_habits()
        elif choice == '4':
            show_progress()
        elif choice == '5':
            print("Exiting Habit Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Start the habit tracker app
habit_tracker()
