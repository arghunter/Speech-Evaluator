import ollama
import whisper

# Load the Whisper model (you can specify a specific model size if you want, e.g., 'base', 'small', 'medium', 'large')
model = whisper.load_model("base")

# Transcribe the audio file
result = model.transcribe("speech4.wav")

# Extract the transcription text from the result
transcription = result['text']

# Print or save the transcription
print(transcription)
prompt1="Should people who create AI be responsible for its impact on society?"
prompt2="Should we worry more about AI taking jobs or the benefits it brings to our lives?"
prompt3="When if at all should students be allowed to use AI in school?"


# Save the transcription to a file or use it further in the code as needed
# with open('transcription.txt', 'w') as f:
#     f.write(transcription)


response = ollama.generate(model='llama3.2', prompt="Please evaluate this speech on the prompt on a scale of 1-10: "+prompt1+" Here is the speech: "+ transcription+ " Base your scale on the flow of the speech and if it gives two solid resason arguing a clear and well explained thesis. Be harsh but reasonable. Also the ending of the speech is the opinions of other human reviewers that you should take into accpunt")
print(response["response"])
