# Challenge - Speech Recognition

![](https://images.unsplash.com/photo-1530811761207-8d9d22f0a141?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80)

We will now try to build use a pre-trained speech recognition system. In this exercise, I will be using Deep-pavlov, but feel free to use whatever system you want (Pocketsphinx or Deepspeech).


## Install dependencies

First, we need to create a virtual environment with Python 3.6.

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

Then, install deeppavlov:

```bash
pip install deeppavlov
```

We will now install pre-trained ASR and Text-to-speech models:

```bash
python -m deeppavlov install asr_tts
python -m deeppavlov download asr_tts
```

It will download the pre-trained English models.

Then, create a Python file (e.g `asr.py`) that contains the following instructions. Change the path to the CSI wav file in the data folder.

```python
from deeppavlov import build_model, configs

model = build_model(configs.nemo.asr)
text_batch = model(['/Users/maelfabien/VivaData/SoundProcessing/00-Lectures/input/CSI.wav'])  # ⚠️ Replace the path with your own path to the CSI.wav file

print(text_batch[0])
``` 

Launch the script using `python asr.py`.

Finally, we will create a live version than can run on your own speech. The script below will record your voice (in English) for 3 seconds and display the audio output. Copy-paste it in a `live.py file`.

```python
from io import BytesIO

import sounddevice as sd
from scipy.io.wavfile import write

from deeppavlov import build_model, configs

sr = 16000
duration = 3

print('Recording...')
myrecording = sd.rec(duration*sr, samplerate=sr, channels=1)
sd.wait()
print('done')

out = BytesIO()
write(out, sr, myrecording)

model = build_model(configs.nemo.asr)
text_batch = model([out])

print(text_batch[0])
```

