import TTS.api

import config

tts = TTS.api.TTS()

for id, model in config.models.items():
	tts.download_model_by_name(model)
