from fastapi import FastAPI, UploadFile, File, Form
from backend.services.gpt_planner import generate_with_gemini
from backend.services.image_captioner import generate_caption_with_gemini
import os

app = FastAPI()

@app.post("/personalized-meal-plan")
async def personalized_meal_plan(
    age: int = Form(...),
    gender: str = Form(...),
    weight: float = Form(...),
    height: float = Form(...),
    text: str = Form(...),
    image: UploadFile = File(None)  # Optional
):
    # Handle image input
    caption = ""
    if image:
        image_bytes = await image.read()
        caption = generate_caption_with_gemini(image_bytes)

    # Compose the full prompt
    prompt_parts = [
        f"Age: {age}",
        f"Gender: {gender}",
        f"Weight: {weight} kg",
        f"Height: {height} cm",
        f"Text input: {text}"
    ]
    if caption:
        prompt_parts.append(f"Image content: {caption}")

    full_prompt = "Suggest a personalized meal plan based on the following details:\n" + "\n".join(prompt_parts)
    
    response = generate_with_gemini(full_prompt)

    return {
        "prompt": full_prompt,
        "plan": response
    }