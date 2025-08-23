import os, sys, requests
from api_secrets import API_KEY_ASSEMBLYAI

upload_endpoint="https://api.assemblyai.com/v2/upload"
transcript_endpoint="https://api.assemblyai.com/v2/transcript"
headers={
        'authorization':API_KEY_ASSEMBLYAI
}
filename=sys.argv[1]
def upload():
    def read_file(filename, chunk_size=5242880):
        with open(filename,"rb") as _file:
            while True:
                data=_file.read(chunk_size)
                if not data:
                    break
                yield data

    
    upload_response=requests.post(upload_endpoint,
                        headers=headers,
                        data=read_file(filename))
    print(upload_response.json())

    audio_url=upload_response.json()['upload_url']
    return audio_url
audio_url=upload()
json={'audio_url':audio_url}
def transcribe():
    transcript_response=requests.post(transcript_endpoint,
                        json=json,headers=headers)
    job_id=transcript_response.json()['id']

# We upload the audio file and then look on the assembly ai's site whether it is ready or not - make pool requests
# poll




