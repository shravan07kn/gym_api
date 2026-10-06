from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Gym & Fitness API")

app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/", include_in_schema=False)
def home():
    return FileResponse("frontend/index.html")


# -----------------------------
# Exercise Data
# -----------------------------

exercises = [
    {
        "name": "Bench Press",
        "muscle": "chest",
        "equipment": "barbell",
        "difficulty": "intermediate"
    },
    {
        "name": "Push Ups",
        "muscle": "chest",
        "equipment": "bodyweight",
        "difficulty": "beginner"
    },
    {
        "name": "Pull Ups",
        "muscle": "back",
        "equipment": "bodyweight",
        "difficulty": "intermediate"
    },
    {
        "name": "Barbell Squat",
        "muscle": "legs",
        "equipment": "barbell",
        "difficulty": "intermediate"
    },
    {
        "name": "Bicep Curl",
        "muscle": "biceps",
        "equipment": "dumbbell",
        "difficulty": "beginner"
    },
    {
        "name": "Shoulder Press",
        "muscle": "shoulders",
        "equipment": "dumbbell",
        "difficulty": "beginner"
    }
]


# -----------------------------
# Home
# -----------------------------




# -----------------------------
# Get all exercises
# -----------------------------

@app.get("/exercises")
def get_exercises():
    return exercises


# -----------------------------
# Get exercises by muscle
# -----------------------------

@app.get("/exercises/{muscle}")
def get_by_muscle(muscle: str):

    result = [
        exercise
        for exercise in exercises
        if exercise["muscle"].lower() == muscle.lower()
    ]

    return result


# -----------------------------
# BMI Calculator
# -----------------------------

@app.get("/bmi")
def calculate_bmi(weight: float, height: float):

    height_m = height / 100

    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return {
        "weight_kg": weight,
        "height_cm": height,
        "bmi": round(bmi, 2),
        "category": category
    }


# -----------------------------
# Calorie Calculator
# -----------------------------

@app.get("/calories")
def calculate_calories(weight: float, duration: int, activity: str):

    calories_per_minute = {
        "walking": 4,
        "running": 10,
        "cycling": 8,
        "weightlifting": 6
    }

    activity = activity.lower()

    if activity not in calories_per_minute:
        return {
            "error": "Activity not found",
            "available_activities": list(calories_per_minute.keys())
        }

    calories = (
        calories_per_minute[activity]
        * weight
        / 70
        * duration
    )

    return {
        "activity": activity,
        "duration_minutes": duration,
        "weight_kg": weight,
        "estimated_calories": round(calories, 2)
    }


# -----------------------------
# Workout Plans
# -----------------------------

workouts = {
    "weight-loss": [
        "Running - 20 minutes",
        "Jumping Jacks - 3 sets",
        "Push Ups - 3 sets",
        "Bodyweight Squats - 3 sets"
    ],

    "muscle-gain": [
        "Bench Press - 4 sets",
        "Barbell Squats - 4 sets",
        "Pull Ups - 3 sets",
        "Bicep Curls - 3 sets"
    ],

    "beginner": [
        "Walking - 15 minutes",
        "Push Ups - 3 sets",
        "Bodyweight Squats - 3 sets",
        "Plank - 3 sets"
    ]
}


@app.get("/workout/{goal}")
def get_workout(goal: str):

    goal = goal.lower()

    if goal not in workouts:
        return {
            "error": "Workout goal not found",
            "available_goals": list(workouts.keys())
        }

    return {
        "goal": goal,
        "workout": workouts[goal]
    }
# -----------------------------
# Diet / Meal Plans
# -----------------------------

diet_plans = {

    "weight-loss": [
        "Breakfast: Oats with fruits",
        "Lunch: Brown rice, vegetables and grilled chicken",
        "Snack: Apple and handful of almonds",
        "Dinner: Vegetable soup and grilled paneer"
    ],

    "muscle-gain": [
        "Breakfast: Eggs, oats and banana",
        "Lunch: Rice, chicken and vegetables",
        "Snack: Banana shake with peanut butter",
        "Dinner: Paneer, rice and vegetables"
    ],

    "beginner": [
        "Breakfast: Eggs and fruits",
        "Lunch: Rice, vegetables and dal",
        "Snack: Fruits and nuts",
        "Dinner: Chapati and vegetables"
    ]
}


@app.get("/diet/{goal}")
def get_diet(goal: str):

    goal = goal.lower()

    if goal not in diet_plans:
        return {
            "error": "Diet plan not found",
            "available_goals": list(diet_plans.keys())
        }

    return {
        "goal": goal,
        "diet_plan": diet_plans[goal]
    }

# -----------------------------
# Personalized Fitness Plan
# -----------------------------

@app.get("/fitness-plan")
def fitness_plan(
    age: int,
    weight: float,
    height: float,
    goal: str,
    activity: str
):

    # BMI calculation
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # Rough daily calorie estimate
    activity_factors = {
        "low": 30,
        "moderate": 35,
        "high": 40
    }

    factor = activity_factors.get(activity.lower(), 35)

    calories = weight * factor

    # Workout
    goal = goal.lower()

    if goal == "muscle-gain":
        workout = workouts["muscle-gain"]
        diet = diet_plans["muscle-gain"]

    elif goal == "weight-loss":
        workout = workouts["weight-loss"]
        diet = diet_plans["weight-loss"]

    else:
        workout = workouts["beginner"]
        diet = diet_plans["beginner"]

    return {
        "age": age,
        "weight_kg": weight,
        "height_cm": height,
        "bmi": round(bmi, 2),
        "category": category,
        "goal": goal,
        "activity_level": activity,
        "estimated_daily_calories": round(calories),
        "workout": workout,
        "diet": diet
    }