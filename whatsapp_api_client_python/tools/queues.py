from whatsapp_api_client_python.response import Response


class Queues:
    def __init__(self, greenApi) -> None:
        self.greenApi = greenApi
        
    def clearMessagesQueue(self) -> Response:
            'The method is aimed for clearing the queue of messages to be sent.'

            return self.greenApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/ClearMessagesQueue/{{apiTokenInstance}}')

    def showMessagesQueue(self) -> Response:
            'The method is aimed for getting a list of messages in the queue '\
            'to be sent. Messages sending rate is managed by Messages sending '\
            'delay parameter.'

            return self.greenApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/ShowMessagesQueue/{{apiTokenInstance}}')