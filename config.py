# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "26775695"))
    API_HASH = os.environ.get("API_HASH", "b15bb60859bef151762fc5d9eb206c67")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7684599268:AAFf97fALKymo_Xi1hb3t0kiFP8Wmis1k8I")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1002482663527"))
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://pangphu9:0pSRO3UHIoH5ouAx@cluster0.ipqp2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1200411908"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/IDNCoderXRoot"
    TG_MAX_SIZE = 2040108421
