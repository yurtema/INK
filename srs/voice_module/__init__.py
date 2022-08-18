import os
import torch


local_file = 'voice_module\model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file(
        'https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
        local_file)
    
device = torch.device('cpu')
torch.set_num_threads(4)


model = torch.package.PackageImporter(local_file).load_pickle("tts_models",
                                                              "model")
model.to(device)





