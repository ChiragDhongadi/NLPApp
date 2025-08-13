import nlpcloud

class API:

    def __init__(self):
        self.client = nlpcloud.Client("finetuned-llama-3-70b", "e2f057a5f9f985a124abed530899bb072130b5c4", gpu=True)

    def sentiment_analysis(self,text):
        self.client = nlpcloud.Client("finetuned-llama-3-70b", "e2f057a5f9f985a124abed530899bb072130b5c4", gpu=True)
        response = self.client.sentiment(text,target="NLP Cloud")
        return response

    def ner(self,text):
        self.client = nlpcloud.Client("finetuned-llama-3-70b", "e2f057a5f9f985a124abed530899bb072130b5c4", gpu=True)
        response = self.client.entities(text,searched_entity="programming languages")
        return response

    def language_detection(self,text):
        self.client = nlpcloud.Client("python-langdetect", "f0651b19d429ad5a4ef627d1bf87f42456449c88", gpu=False)
        response = self.client.langdetection(text)
        return response