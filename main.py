import ollama
import whisper

# Load the Whisper model (you can specify a specific model size if you want, e.g., 'base', 'small', 'medium', 'large')
model = whisper.load_model("base")

# Transcribe the audio file
result = model.transcribe(input("Enter Speech File Path:"))

# Extract the transcription text from the result
transcription = result['text']

# Print the transcription
print(transcription)
prompt1=input("Enter prompt:")
basis=" Base your scale on the flow of the speech and if it gives two solid reasons arguing a clear and well explained thesis. Be harsh but reasonable." # basis from grading
response = ollama.generate(model='llama3.2', prompt="Please evaluate this speech on the prompt on a scale of 1-5: "+prompt1+" Here is the speech: "+ transcription+ bases)
print(response["response"])
