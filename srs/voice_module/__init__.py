"""
Подготовка tts модели к работе.
"""
import os
import torch

# Если нет файла с моделю, скачать его.
local_file = 'voice_module\model.pt'
if not os.path.isfile(local_file):
    torch.hub.download_url_to_file(
        'https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
        local_file)

# Настройки торча. https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSyNarKasyXgWc-iy8rq9ev8aPtkC2_dJfxNVv2-xQKgRNeSAWReaUj8VydkczJy3GLrU&usqp=CAU
device = torch.device('cpu')
torch.set_num_threads(4)

# Инициализация модели.
model = torch.package.PackageImporter(local_file).load_pickle("tts_models",
                                                              "model")
# Без понятия.
model.to(device)
