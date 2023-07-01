import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100      # Analog değerden dijital değere hangi sıklıklıkla geçildiğini belirtir.
saniye = int(input("Kaç saniyelik bir ses kaydı oluşturmak istersiniz :"))
print("Ses kaydınız başlamıştır.")
myrecording = sd.rec(int(saniye * fs), samplerate=fs , channels=2)
sd.wait()
write('output.wav',fs,myrecording)
print("Ses kaydınız oluşturulmuştur.")
