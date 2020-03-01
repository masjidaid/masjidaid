import graphene
from graphene_django import DjangoObjectType

from masjidaid.accounts.schema import UserType
from .models import Campaign


class CampaignType(DjangoObjectType):
    class Meta:
        model = Campaign
    

class Query(graphene.ObjectType):
    all_campaigns = graphene.List(CampaignType, description="All the campaigns present")
    campaign = graphene.Field(CampaignType, id=graphene.Int(), description="Single campaign")

    def resolve_all_campaigns(self, info, **kwargs):
        return Campaign.objects.filter(is_active=True)
    
    def resolve_campaign(self, info, id=None):
        if id is not None:
            return Campaign.objects.get(pk=id)


class CreateCampaign(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    creator = graphene.Field(UserType)
    description = graphene.String()
    # target = graphene.Decimal()
    target = graphene.Int()


    class Arguments:
        name = graphene.String()
        description = graphene.String()
        target = graphene.Int()
        
    
    def mutate(self, info, name, description, target):
        creator = info.context.user
        campaign = Campaign(name=name, description=description, creator=creator, target=target)
        campaign.save()

        return CreateCampaign(
            id=campaign.id,
            name=campaign.name,
            creator=campaign.creator,
            description=campaign.description,
            target=campaign.target
        )


class Mutation(graphene.ObjectType):
    create_campaign = CreateCampaign.Field()
