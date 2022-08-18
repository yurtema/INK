import voice_module
from voice_module import config
from playsound import playsound
import os

file_read = open('voice_module/phrases.txt', encoding='utf-8')
phrases_list = file_read.read().split('\n')
if phrases_list == ['']:
    phrases_list = []
file_read.close()


def say(text, model=voice_module.model) -> None:
    if text in phrases_list:
        playsound('D:\PYTHON/INK/srs/voice_module/phrases/' + str(
            phrases_list.index(text)) + '.wav')
    else:
        file_write = open('voice_module/phrases.txt', 'a', encoding='utf-8')
        model.save_wav(text=text,
                       speaker=config.speaker,
                       sample_rate=config.sample_rate)
        os.rename('test.wav',
                  'voice_module/phrases/' + str(len(phrases_list)) + '.wav')
        file_write.write(text + '\n')
        file_write.close()
        playsound('D:\PYTHON/INK/srs/voice_module/phrases/' +
                  str(len(phrases_list)) + '.wav')
