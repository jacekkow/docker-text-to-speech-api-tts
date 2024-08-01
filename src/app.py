import enum
import io

import fastapi
import pydantic
import TTS.api

import config

models = {}

for id, model in config.models.items():
	models[id] = TTS.api.TTS(model).to("cpu")


LanguageModel = enum.Enum('LanguageModel', {k: k for k in models.keys()})


class SynthesizeRequest(pydantic.BaseModel):
	language: LanguageModel
	text: str


class SynthesizeResponse(fastapi.Response):
	media_type = 'audio/wav'


app = fastapi.FastAPI()

@app.post('/synthesize', response_class=SynthesizeResponse)
async def synthesize(request: SynthesizeRequest) -> SynthesizeResponse:
	with io.BytesIO() as fp:
		models[request.language.value].tts_to_file(request.text, file_path=fp)
		return SynthesizeResponse(content = fp.getvalue())
