from datetime import datetime
import json
from whatsapp_api_client_python import API as API

ID_INSTANCE = '1101000001'
API_TOKEN_INSTANCE = '3e03ea9ff3324e228ae3dfdf4d48e409bfa1b1ad0b0c46bf8c'

greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)

def main():
   greenAPI.webhooks.startReceivingNotifications(onEvent)

def onEvent(typeWebhook, body):
   if typeWebhook == 'incomingMessageReceived':
      onIncomingMessageReceived(body)      
   elif typeWebhook == 'deviceInfo':   
      onDeviceInfo(body)              
   elif typeWebhook == 'incomingCall':
      onIncomingCall(body)
   elif typeWebhook == 'outgoingAPIMessageReceived':
      onOutgoingAPIMessageReceived(body)
   elif typeWebhook == 'outgoingMessageReceived':
      onOutgoingMessageReceived(body)
   elif typeWebhook == 'outgoingMessageStatus':
      onOutgoingMessageStatus(body)
   elif typeWebhook == 'stateInstanceChanged':
      onStateInstanceChanged(body)
   elif typeWebhook == 'statusInstanceChanged':
      onStatusInstanceChanged(body)

def onIncomingMessageReceived(body):
        idMessage = body['idMessage']
        eventDate = datetime.fromtimestamp(body['timestamp'])
        senderData = body['senderData']
        messageData = body['messageData']
        print(idMessage + ': ' 
            + 'At ' + str(eventDate) + ' Incoming from ' \
            + json.dumps(senderData, ensure_ascii=False) \
            + ' message = ' + json.dumps(messageData, ensure_ascii=False))

def onIncomingCall(body):
   idMessage = body['idMessage']
   eventDate = datetime.fromtimestamp(body['timestamp'])
   fromWho = body['from']
   print(idMessage + ': ' 
      + 'Call from ' + fromWho 
      + ' at ' + str(eventDate))

def onDeviceInfo(body):
   eventDate = datetime.fromtimestamp(body['timestamp'])
   deviceData = body['deviceData']
   print('At ' + str(eventDate) + ': ' \
      + json.dumps(deviceData, ensure_ascii=False))

def onOutgoingMessageReceived(body):
   idMessage = body['idMessage']
   eventDate = datetime.fromtimestamp(body['timestamp'])
   senderData = body['senderData']
   messageData = body['messageData']
   print(idMessage + ': ' 
      + 'At ' + str(eventDate) + ' Outgoing from ' \
      + json.dumps(senderData, ensure_ascii=False) \
      + ' message = ' + json.dumps(messageData, ensure_ascii=False))

def onOutgoingAPIMessageReceived(body):
   idMessage = body['idMessage']
   eventDate = datetime.fromtimestamp(body['timestamp'])
   senderData = body['senderData']
   messageData = body['messageData']
   print(idMessage + ': ' 
      + 'At ' + str(eventDate) + ' API outgoing from ' \
      + json.dumps(senderData, ensure_ascii=False) + \
      ' message = ' + json.dumps(messageData, ensure_ascii=False))

def onOutgoingMessageStatus(body):
   idMessage = body['idMessage']
   status = body['status']
   eventDate = datetime.fromtimestamp(body['timestamp'])
   print(idMessage + ': ' 
      + 'At ' + str(eventDate) + ' status = ' + status)

def onStateInstanceChanged(body):
   eventDate = datetime.fromtimestamp(body['timestamp'])
   stateInstance = body['stateInstance']
   print('At ' + str(eventDate) + ' state instance = ' \
      + json.dumps(stateInstance, ensure_ascii=False))

def onStatusInstanceChanged(body):
   eventDate = datetime.fromtimestamp(body['timestamp'])
   statusInstance = body['statusInstance']
   print('At ' + str(eventDate) + ' status instance = ' \
      + json.dumps(statusInstance, ensure_ascii=False))


if __name__ == "__main__":
    main()