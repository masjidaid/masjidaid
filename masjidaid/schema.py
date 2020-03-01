import graphene
import graphql_jwt

import masjidaid.accounts.schema
import masjidaid.campaign.schema


class Query(masjidaid.accounts.schema.Query, masjidaid.campaign.schema.Query, graphene.ObjectType):
    pass


class Mutation(masjidaid.accounts.schema.Mutation, masjidaid.campaign.schema.Mutation, graphene.ObjectType,):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)