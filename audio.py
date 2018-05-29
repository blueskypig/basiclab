from aip import AipSpeech
import wave,pyaudio

#ACCESS
APP_ID='10609579'
API_KEY='RLw6hsnA0EI4U4KAvvjTV0CQ'
SECRET_KEY='87c5b996d95be9c5347d6feaa06eceb1'

# Settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 8000
CHANNELS = 1
RECORD_SECONDS = 3

# Record Function
def recordWave():
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)
    print('Recording...')
    buffer = []
    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        audio_data = stream.read(CHUNK)
        buffer.append(audio_data)
    print('Record Done')
    stream.stop_stream()
    stream.close()
    pa.terminate()
    wf = wave.open('record.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(buffer))
    wf.close()

def get_file_content(filePath):
	with open(filePath,'rb') as fp:
		return fp.read()

if __name__ == '__main__':
	#recordWave()
	client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
	#res=client.asr(get_file_content('record.wav'),'wav',8000,{'lan':'zh'})
	#print(res)
	res=client.synthesis('小媳妇，新年快乐，这是语音合成的哦。','zh',1,{'pit':6,'vol':5,'per':4})
	if not isinstance(res,dict):
		with open('audio.mp3','wb') as f:
			f.write(res)