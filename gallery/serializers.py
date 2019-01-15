from rest_framework import serializers

import smtplib
from email.message import EmailMessage
from gallery.models import ArtDirecting, Collection, Directing, Photography, \
    Work


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('name', 'description', 'id', 'sort_order')


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('name', 'description', 'image', 'dimensions_x',
                  'dimensions_y', 'material', 'collection')


class PhotographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Photography
        fields = ('name', 'image', 'description',
                  'dimensions_x', 'dimensions_y')


class DirectingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directing
        fields = ('name', 'description', 'videoId')


class ArtDirectingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directing
        fields = ('name', 'description', 'videoId')


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    phone = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=500)
    date = serializers.DateField()

    def create(self, validated_data):
        msg = EmailMessage()
        msg.set_content = "Hi Aliswan! Someone has added a new contact! Details below: <br/> <br/> Name: %s <br/> Phone: %s <br/> Email: %s <br/> Message: %s <br/>" % (
            validated_data.name, validated_data.phone, validated_data.email, validated_data.message)
        msg["Subject"] = "Aliswan! New Contact Message received!"
        msg['From'] = "mchrisyd@gmail.com"
        msg['To'] = "chris@topher.co.za"
        msg['']
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.login('mchrisyd@gmail.com', 'Ic3cr3am!2!#YD')
            s.send_message(msg)

        return Contact.objects.create(**validated_data)
