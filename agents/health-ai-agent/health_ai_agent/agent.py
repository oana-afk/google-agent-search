import os
from .prompts import *
from google.adk.agents import Agent

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.ERROR)

from dotenv import load_dotenv
load_dotenv()

AGENT_MODEL = os.getenv('MODEL_GEMINI_2_0_FLASH')

def calculateBmr(sex: str, age: int, weight: float, height: float, activity_level: str = "sedentary") -> float:
    """
    Calculates Basal Metabolic Rate (BMR) and total daily energy expenditure based on activity level.

    Parameters:
    - sex: 'male' or 'female'
    - age: age in years
    - weight: weight in kilograms
    - height: height in centimeters
    - activity_level: physical activity level (optional, default is 'sedentary')

    Returns:
    - Estimated total daily caloric expenditure in kcal
    """
    # Harris-Benedict equations
    if sex.lower() == 'male':
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    elif sex.lower() == 'female':
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    else:
        raise ValueError("Invalid sex. Use 'male' or 'female'.")

    # Activity level multipliers
    activity_factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "intense": 1.725,
        "very intense": 1.9
    }

    factor = activity_factors.get(activity_level.lower(), 1.2)  # Default to sedentary if not recognized

    total_expenditure = bmr * factor
    return round(total_expenditure, 2)

personal_trainer_agent= Agent(
    name='personal_agent',
    model=AGENT_MODEL,
    instruction=PERSONAL_TRAINER_AGENT_PROMPT,
    description="A personal trainer thats create a workout plan for the user.",
)

nutritionist_agent= Agent(
    name='nutritionist_agent',
    model=AGENT_MODEL,
    instruction=NUTRITIONIST_AGENT_PROMPT,
    description="A nutritionist thats create a diet for the user.",
    tools=[calculateBmr]
)

root_agent = Agent(
    name='health_agent',
    model=AGENT_MODEL,
    instruction=ROOT_AGENT_PROMPT,
    description="A helpful assistant for create a workout and diet.",
    sub_agents=[personal_trainer_agent, nutritionist_agent]
)