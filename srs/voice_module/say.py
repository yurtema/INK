import voice_module
from voice_module import config
from playsound import playsound
import os


def say(text, model=voice_module.model) -> None:
    """
    Если передання на вход фраза есть в phrases.txt, воспроизвести её по
    порядковому номеру.
    Если нет, записать, возпроизвести, засунуть в папку и добавить
    в phrases.txt
    """
    text = text.lower()
    
    # Прочитать список записанных фраз из файла.
    file_read = open('voice_module/phrases.txt', encoding='utf-8')
    phrases_list = file_read.read().lower().split('\n')
    print(phrases_list)
    file_read.close()
    
    if text in phrases_list:
        # Если в списке уже есть фраза, воспроизвести её.
        playsound('D:\PYTHON/INK/srs/voice_module/phrases/' + str(
            phrases_list.index(text)) + '.wav')
    else:
        # Если нет, записать в файл,
        file_write = open('voice_module/phrases.txt', 'a', encoding='utf-8')
        file_write.write('\n' + text)
        file_write.close()
        # озвучить, воспроизвести,
        model.save_wav(ssml_text=f"""
                                   <speak>
                                   <prosody pitch="{config.pitch}">
                                   <prosody rate="{config.rate}">
                                   {text}
                                   </prosody>
                                   </prosody>.
                                   </speak>
                                   """,
                       speaker=config.speaker,
                       sample_rate=config.sample_rate)
        playsound('D:\PYTHON/INK/srs/test.wav')
        
        # переименовать и засунуть в папку.
        os.rename('test.wav',
        
                  'voice_module/phrases/' + str(len(phrases_list)) + '.wav')
