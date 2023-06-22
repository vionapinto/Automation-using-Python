from pydub import AudioSegment

# <python-path> -m pip install pydub
# sudo apt-get install ffmpeg

original = AudioSegment.from_wav('beat.wav')
print(type(original))
print(original)

reversed = original.reverse()
reversed.export('reversed.wav')
reversed = reversed + 15  # increasing volume

# print(dir(original))

first_two = original[0:2000]
first_two.export('first_two.wav')

print(len(original)) # in milliseconds

merged = original * 2 + AudioSegment.silent(1000) + reversed 
# appending audio files here
# *2 is original files 2 time
# silent for one second

merged.export('merged.wav')