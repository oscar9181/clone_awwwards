from . models import Site
from rest_framework     import serializers

class SiteSerializers (serializers.ModelSerializer):
    class Meta:
        model= Site
        fields =['name','url','image','date_posted']
