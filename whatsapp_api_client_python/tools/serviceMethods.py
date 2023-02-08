from whatsapp_api_client_python.response import Response


class ServiceMethods:
    def __init__(self, greenApi) -> None:
        self.greenApi = greenApi
        
    def checkWhatsapp(self, phoneNumber: int) -> Response:
            'The method checks WhatsApp account availability on a phone number.'

            requestBody = {
                'phoneNumber': phoneNumber
            }

            return self.greenApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/CheckWhatsapp/{{apiTokenInstance}}',
                requestBody)

    def getAvatar(self, chatId: str) -> Response:
            'The method returns a user or a group chat avatar.'

            requestBody = {
                'chatId': chatId
            }

            return self.greenApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/GetAvatar/{{apiTokenInstance}}',
                requestBody)

    def getContactInfo(self, chatId: str) -> Response:
            'The method is aimed for getting information on a contact.'

            requestBody = {
                'chatId': chatId
            }

            return self.greenApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/GetContactInfo/{{apiTokenInstance}}',
                requestBody)

    def getContacts(self, chatId: str) -> Response:
            'The method is aimed for getting a list of the current account '\
            'contacts. Sends contacts of all recipients whom the account '\
            'connected with. Parameter "contact name" "name" takes on '\
            'a value based on the below criteria: '\
            'If the account is recorded in the phonebook, then we get the '\
            'name from the book; '\
            'If the account is not recorded in the phonebook, then we get '\
            'the name from WhatsApp account;'\
            'If the account is not recorded in the phone book and WhatsApp '\
            'account name is not assigned, then we get an empty field.'

            return self.greenApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/GetContacts/{{apiTokenInstance}}')

    def archiveChat(self, chatId: str) -> Response:
            'The method archives a chat. You can archive chats that have at '\
            'least one incoming message.'

            requestBody = {
                'chatId': chatId
            }

            return self.greenApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/ArchiveChat/{{apiTokenInstance}}',
                requestBody)

    def deleteMessage(self, chatId: str, idMessage: str) -> Response:
            'The method deletes a message from a chat.'

            requestBody = {
                'chatId': chatId,
                'idMessage': idMessage
            }

            return self.greenApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/DeleteMessage/{{apiTokenInstance}}',
                requestBody)

    def unarchiveChat(self, chatId: str) -> Response:
            'The method deletes a message from a chat.'

            requestBody = {
                'chatId': chatId
            }

            return self.greenApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/UnarchiveChat/{{apiTokenInstance}}',
                requestBody)

    def setDisappearingChat(self, chatId: str, 
                            ephemeralExpiration: int) -> Response:
            'The method is aimed for changing settings of disappearing '\
            'messages in chats. The standard settings of the application '\
            'are used: 0 (off), 86400 (24 hours), '\
            '604800 (7 days), 7776000 (90 days).'

            requestBody = {
                'chatId': chatId,
                'ephemeralExpiration': ephemeralExpiration
            }

            return self.greenApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SetDisappearingChat/{{apiTokenInstance}}',
                requestBody)