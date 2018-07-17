from rest_framework import serializers
from .models import *
from Event.models import Event
import json
from cryptography.fernet import Fernet

key = b'RLQHMwbjOj4ztWwPTkDTqBd3YYtF-g7S4W8bX4OItS8='
cipher_suite = Fernet(key)

#cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
#plain_text = cipher_suite.decrypt(cipher_text)


def encrypt(val):
	return cipher_suite.encrypt(bytes(val, 'utf-8')).decode('utf-8')

def decrypt(val):
	return json.loads(cipher_suite.decrypt(bytes(val, 'utf-8')).decode('utf-8'))




class AttendanceSerializer(serializers.Serializer):
    crypted_data = serializers.CharField(max_length=1000)
    def create(self, validated_data):
        data = decrypt(validated_data['crypted_data'])
        data['event'] = Event.objects.get(pk = data['event'])
        print(data)
        return Attendance(**data)
    def save(self):
        data = decrypt(self.validated_data['crypted_data'])
        data['event'] = Event.objects.get(pk = data['event'])
        print(data)
        return Attendance.objects.create(**data)

