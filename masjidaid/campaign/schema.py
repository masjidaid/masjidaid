import graphene
from graphene_django import DjangoObjectType

from .models import Campaign

class CampaignType(DjangoObjectType):
    class Meta:
        model = Campaign
    

class Query(DjangoObjectType):
    class Meta:
        model = Campaign