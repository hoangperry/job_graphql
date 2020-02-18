import graphene
import database_transfer.schema


class Query(database_transfer.schema.Query, graphene.ObjectType):
    pass


class Mutation(database_transfer.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
