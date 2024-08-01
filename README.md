# Text-to-speech API based on Coqui's TTS

Simple Python-based container with everything that is needed
to have a self-hosted web-based text-to-speech API.

## Using the container

Just run:

```
docker run -d -p 8000:8000 ghcr.io/jacekkow/docker-text-to-speech-api-tts:master
```

and then visit http://localhost:8000/docs

There is a simple `/sythesize` endpoint that expects a JSON and returns a wave file:

```
curl -o result.wav -X 'POST' \
  'http://localhost:8000/synthesize' \
  -H 'Content-Type: application/json' \
  -d '{"language": "en", "text": "Sample text."}'
```

## Adding languages

Currently only English and Polish models are included in the image.

To add additional languages you can simply add extra entries
in `src/config.py` file and rebuild the container.

Model identifiers are defined in the TTS repository:
https://github.com/idiap/coqui-ai-TTS/blob/dev/TTS/.models.json

Command line `tts --list_models` lists all the available models.

Note that the API does not support multi-speaker models yet!
