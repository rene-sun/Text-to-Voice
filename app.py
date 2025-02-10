# -*- coding: utf-8 -*-
"""Text-to-Voice app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hKqIuFWV8DcQiczie3owoOntIbcLCI45
"""

import gradio as gr
import tempfile
from TTS.api import TTS

# Define a mapping from (Gender, Speed, Tone) to a speaker ID
voice_mapping = {
    ("Male", "Slow", "Nice"): "p285",
    ("Male", "Average Speed", "Nice"): "p266",
    ("Male", "Fast", "Nice"): "p251",
    ("Male", "Slow", "Not nice"): "p253",
    ("Male", "Average Speed", "Not nice"): "p254",
    ("Male", "Fast", "Not nice"): "p287",
    ("Female", "Slow", "Nice"): "p270",
    ("Female", "Average Speed", "Nice"): "p261",
    ("Female", "Fast", "Nice"): "p263",
    ("Female", "Slow", "Not nice"): "p260",
    ("Female", "Average Speed", "Not nice"): "p294",
    ("Female", "Fast", "Not nice"): "p297"
}

# Initialize the TTS model
tts = TTS(model_name="tts_models/en/vctk/vits")

def synthesize_text(text, gender, speed, tone):
    """
    Synthesize speech based on text and selected characteristics.
    """
    speaker = voice_mapping.get((gender, speed, tone), "p261")

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        output_file = temp_file.name

    # Generate the TTS output
    tts.tts_to_file(text=text, speaker=speaker, file_path=output_file)
    return output_file

# Options for each characteristic
gender_options = ["Male", "Female"]
speed_options = ["Slow", "Average Speed", "Fast"]
tone_options = ["Nice", "Not nice"]

# Create the Gradio interface
interface = gr.Interface(
    fn=synthesize_text,
    inputs=[
        gr.Textbox(label="Enter Text", lines=4, placeholder="Type your text here..."),
        gr.Radio(gender_options, label="Select Gender"),
        gr.Radio(speed_options, label="Select Speed"),
        gr.Radio(tone_options, label="Select Tone"),
    ],
    outputs=gr.Audio(label="Generated Audio"),
    title="Advanced Text-to-Speech Synthesizer",
    description="Choose English text and characteristics to generate audio"
)

# Launch the app on Render
# interface.launch(server_name="0.0.0.0", server_port=8080)
# interface.launch(auth=[("Renesun", "2025"), ("Pricy", "2025")], share=True)
interface.launch(
    auth=[("Renesun", "2025"), ("Pricy", "2025")],
    server_name="0.0.0.0",
    server_port=8080
)
