from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
# Load the trained model
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model = load_model(BASE_DIR / "model.h5")

# Define your class names
class_names = np.array([
    'Normal',
    'Vitamin A deficiency',
    'Vitamin B-12 deficiency',
    'Vitamin B1 deficiency',
    'Vitamin B2 deficiency',
    'Vitamin B3 deficiency',
    'Vitamin B9 deficiency',
    'Vitamin C deficiency',
    'Vitamin D deficiency',
    'Vitamin E deficiency',
    'Vitamin K deficiency',
    'zinc, iron, biotin, or protein deficiency'
])

def validate_image(img):
    """Ensure the uploaded file is an image."""
    try:
        Image.open(img).verify()
    except Exception:
        raise ValidationError("Uploaded file is not a valid image.")

from PIL import Image
import numpy as np

def preprocess_image(image_file):
    img = Image.open(image_file).convert("RGB")
    img = img.convert("RGB")
    img = img.resize((124, 124))
    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array
# Home page view
def home(request):
    return render(request, 'input.html')

# Output page view for prediction
def output(request):

    if request.method != "POST" or 'image' not in request.FILES:
        return render(request, 'input.html')

    img = request.FILES['image']

    # rest of your prediction code remains unchanged
    
    # Validate the uploaded image
    try:
        validate_image(img)
    except ValidationError as e:
        return HttpResponse(str(e), content_type="text/plain")
    
    # Preprocess the image
    preprocessed_img = preprocess_image(img)
    
    # Predict the class
    predictions = model.predict(preprocessed_img)[0]

    predicted_class_index = np.argmax(predictions)
    predicted_class = class_names[predicted_class_index]
    if predicted_class == "Normal":
        predicted_class = "Invalid"

    confidence = float(np.max(predictions)) * 100
    confidence = round(confidence, 2)

# ✅ Confidence-based handling (FIX)
    if confidence < 30:
        predicted_class = "Invalid"

    print(f"Predicted class index: {predicted_class_index}")
    print(f"Predicted class name: {predicted_class}")
    print(f"Confidence: {confidence}")

    
    vitamin_info = {

    "Vitamin A deficiency": {
        "description": (
            "Vitamin A deficiency is a serious nutritional disorder that primarily affects vision, "
            "immune system function, and skin integrity. Individuals suffering from this deficiency "
            "may experience night blindness, dry eyes, frequent infections, delayed wound healing, "
            "and rough or dry skin. In advanced stages, it can lead to irreversible vision loss and "
            "significantly weaken the body’s ability to fight infections."
        ),
        "cure": (
            "Treatment focuses on increasing vitamin A intake through diet and supplements. "
            "Foods rich in vitamin A include carrots, sweet potatoes, pumpkin, spinach, "
            "green leafy vegetables, milk, eggs, and liver. In moderate to severe cases, "
            "vitamin A supplements may be prescribed by a healthcare professional to rapidly "
            "restore normal levels."
        )
    },

    "Vitamin B1 deficiency": {
        "description": (
            "Vitamin B1 (Thiamine) deficiency affects the nervous system and energy metabolism. "
            "It reduces the body’s ability to convert carbohydrates into energy, leading to fatigue, "
            "muscle weakness, irritability, memory problems, and nerve damage. Prolonged deficiency "
            "can result in serious conditions such as beriberi and cardiovascular complications."
        ),
        "cure": (
            "The deficiency can be corrected by consuming thiamine-rich foods such as whole grains, "
            "legumes, nuts, seeds, and pork. Individuals with severe symptoms may require "
            "oral or injectable thiamine supplements under medical supervision."
        )
    },

    "Vitamin B2 deficiency": {
        "description": (
            "Vitamin B2 (Riboflavin) deficiency primarily affects the skin, eyes, and mouth. "
            "Common symptoms include cracked lips, mouth ulcers, sore throat, skin inflammation, "
            "and sensitivity to light. Riboflavin is essential for cellular energy production and "
            "antioxidant activity."
        ),
        "cure": (
            "Riboflavin deficiency is treated by consuming dairy products such as milk and yogurt, "
            "eggs, green leafy vegetables, and fortified cereals. In some cases, riboflavin "
            "supplements may be recommended to ensure adequate intake."
        )
    },

    "Vitamin B3 deficiency": {
        "description": (
            "Vitamin B3 (Niacin) deficiency disrupts metabolism and nervous system function. "
            "Severe deficiency leads to pellagra, characterized by dermatitis, diarrhea, "
            "and mental disturbances. Without treatment, it can become life-threatening."
        ),
        "cure": (
            "Dietary sources such as meat, fish, peanuts, legumes, and whole grains help "
            "restore niacin levels. Medical supplementation is often required in moderate "
            "to severe deficiency cases."
        )
    },

    "Vitamin B9 deficiency": {
        "description": (
            "Vitamin B9 (Folate) deficiency affects DNA synthesis and red blood cell production. "
            "It commonly causes anemia, fatigue, weakness, and shortness of breath. During pregnancy, "
            "folate deficiency significantly increases the risk of birth defects."
        ),
        "cure": (
            "Treatment includes consuming folate-rich foods such as spinach, broccoli, beans, "
            "lentils, citrus fruits, and fortified grains. Folate supplements are widely "
            "prescribed, especially for pregnant women."
        )
    },

    "Vitamin B-12 deficiency": {
        "description": (
            "Vitamin B12 deficiency affects both the nervous system and blood formation. "
            "Symptoms include numbness or tingling in hands and feet, memory loss, fatigue, "
            "anemia, and difficulty concentrating. Long-term deficiency can cause irreversible "
            "nerve damage."
        ),
        "cure": (
            "Vitamin B12 deficiency is treated by consuming animal-based foods such as meat, "
            "fish, eggs, and dairy products. Vegetarians may rely on fortified foods or "
            "B12 supplements. In severe cases, B12 injections are required."
        )
    },

    "Vitamin C deficiency": {
        "description": (
            "Vitamin C deficiency weakens the immune system and connective tissues. "
            "It leads to symptoms such as bleeding gums, fatigue, joint pain, slow wound healing, "
            "and increased susceptibility to infections. Severe deficiency results in scurvy."
        ),
        "cure": (
            "Increasing intake of citrus fruits, amla, strawberries, tomatoes, bell peppers, "
            "and green vegetables helps restore vitamin C levels. Supplements may be used "
            "when dietary intake is insufficient."
        )
    },

    "Vitamin D deficiency": {
        "description": (
            "Vitamin D deficiency affects calcium absorption, bone strength, and immune function. "
            "It can cause bone pain, muscle weakness, fatigue, and increased risk of fractures. "
            "In children, it may lead to rickets, while in adults it can cause osteomalacia."
        ),
        "cure": (
            "Treatment includes regular sunlight exposure, consumption of dairy products, "
            "fatty fish, egg yolks, and fortified foods. Vitamin D supplements are commonly "
            "prescribed to maintain optimal levels."
        )
    },

    "Vitamin E deficiency": {
        "description": (
            "Vitamin E deficiency affects muscle and nerve function due to impaired antioxidant "
            "activity. Symptoms include muscle weakness, poor coordination, vision problems, "
            "and immune dysfunction."
        ),
        "cure": (
            "Consuming nuts, seeds, vegetable oils, spinach, and broccoli helps restore "
            "vitamin E levels. Supplementation may be recommended in severe cases."
        )
    },

    "Vitamin K deficiency": {
        "description": (
            "Vitamin K deficiency interferes with blood clotting mechanisms, increasing the "
            "risk of excessive bleeding and bruising. It is especially dangerous in newborns "
            "and individuals with digestive disorders."
        ),
        "cure": (
            "Green leafy vegetables such as spinach, kale, cabbage, and broccoli are rich "
            "sources of vitamin K. Vitamin K supplements may be administered when necessary."
        )
    },

    "zinc, iron, biotin, or protein deficiency": {
        "description": (
            "Deficiency of zinc, iron, or protein significantly affects growth, immunity, "
            "muscle development, and oxygen transport in the body. Symptoms include weakness, "
            "hair loss, frequent infections, delayed wound healing, and anemia."
        ),
        "cure": (
            "Zinc intake can be improved with nuts and seeds, iron through leafy vegetables, "
            "dates, and jaggery, and protein through eggs, pulses, milk, and lean meats. "
            "Supplementation may be required based on severity."
        )
    }
}


    info = vitamin_info.get(
        predicted_class,
        {
            "description": "No description available.",
            "cure": "Consult a healthcare professional."
        }
    )

    return render(request, 'output.html', {
        'out': predicted_class,
        'description': info['description'],
        'cure': info['cure'],
        'confidence': confidence
    })
