#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid
import json
import requests
import boto3
from mycroft.stt import STT


class nlpSTTPlugin(STT):

    def execute(self, audio, language=None):
        fileName = uuid.uuid4().hex+".wav"
        with open(fileName, "wb") as f:
            f.write(audio.get_wav_data())
        self.uploadS3(fileName)

        return self.deserialize(fileName)

    def uploadS3(self, fileName):
        s3 = boto3.client('s3')
        BUCKET_NAME = "scg-dolab-dev-nlp-speech-to-text"
        OBJECT_NAME = "data/"+fileName
        FILE_NAME = fileName
        s3.upload_file(FILE_NAME, BUCKET_NAME, OBJECT_NAME)

    def deserialize(self, fileName):
        API_ENDPOINT = "https://scg-dolab-dev-alb-1580607739.ap-southeast-1.elb.amazonaws.com/speech2text"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        # data to be sent to api

        data = json.dumps({
        "BUCKET_NAME": "scg-dolab-dev-nlp-speech-to-text",
        "OBJECT_NAME": "data/"+ fileName,
        "FILE_NAME": fileName,
        "do_postprocess": True
        })

        # sending post request and saving response as response object
        r = requests.post(url=API_ENDPOINT, data=data, headers=headers, verify=False)
        # extracting response text
        jsonResponse = r.text
        print("jsonResponse: ", jsonResponse)

        value = json.loads(jsonResponse)
        print("output: ", value["output"][0])

        return value["output"][0]

 