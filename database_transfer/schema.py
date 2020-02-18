import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from database_transfer.models import Job


# Create a GraphQL type for the real estate model
class JobType(DjangoObjectType):
    class Meta:
        model = Job


# Create a Query type
class Query(ObjectType):
    job = graphene.Field(JobType, id=graphene.Int())
    jobs = graphene.List(JobType, orderBy=graphene.List(of_type=graphene.String), limit=graphene.Int())
    total_job = graphene.Int()

    def resolve_total_job(self, info, **kwargs):
        return Job.objects.count()

    def resolve_job(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Job.objects.get(pk=id)

        return None

    def resolve_jobs(self, info, **kwargs):
        orderBy = kwargs.get("orderBy", None)
        limit = kwargs.get("limit", None)
        if orderBy:
            return Job.objects.order_by(*orderBy)[:limit]
        return Job.objects.all()


# Create Input Object Types
class JobInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    created_time = graphene.DateTime()
    currency_unit = graphene.String()
    salary = graphene.String()
    salary_normalize = graphene.Float()
    url = graphene.String()
    company = graphene.String()
    location = graphene.String()
    info = graphene.String()
    degree_requirements = graphene.String()
    deadline_submit = graphene.Date()
    experience = graphene.String()
    no_of_opening = graphene.String()
    formality = graphene.String()
    position = graphene.String()
    gender_requirements = graphene.String()
    career = graphene.String()
    description = graphene.String()
    benefit = graphene.String()
    job_requirements = graphene.String()
    profile_requirements = graphene.String()
    contact = graphene.String()
    other_info = graphene.String()


# class CreateRealEstates(graphene.Mutation):
#     class Arguments:
#         input = RealEstatesInput(required=True)
#
#     ok = graphene.Boolean()
#     realEstate = graphene.Field(RealEstatesType)
#
#     @staticmethod
#     def mutate(root, info, input=None):
#         ok = True
#         images = list()
#         for image_input in input.images:
#             image = ProjectImages.objects.get(pk=image_input.id)
#             if image is None:
#                 return CreateRealEstates(ok=False, realEstate=None)
#             images.append(image)
#
#         real_estates_instance = RealEstates(
#             name=input.name,
#             investor=input.investor,
#             provider=input.provider,
#             address=input.address,
#             totalAcreage=input.totalAcreage,
#             constructionAcreage=input.constructionAcreage,
#             buildingDensity=input.buildingDensity,
#             type=input.type,
#             price=input.price,
#             handoverDate=input.handoverDate,
#             scale=input.scale,
#             link=input.link,
#             introduction=input.introduction,
#             province=input.province,
#             district=input.district,
#         )
#         real_estates_instance.save()
#         real_estates_instance.images.set(images)
#         return CreateRealEstates(ok=ok, realEstate=real_estates_instance)
#
#
# class UpdateRealEstates(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         input = RealEstatesInput(required=True)
#
#     ok = graphene.Boolean()
#     realEstate = graphene.Field(RealEstatesType)
#
#     @staticmethod
#     def mutate(root, info, id, input=None):
#         ok = False
#         real_estates_instance = RealEstates.objects.get(pk=id)
#         if real_estates_instance:
#             ok = True
#             images = list()
#             for image_input in input.images:
#                 image = ProjectImages.objects.get(pk=image_input.id)
#                 if image is None:
#                     return UpdateRealEstates(ok=False, movie=None)
#                 images.append(image)
#             real_estates_instance.name = input.name
#             real_estates_instance.investor = input.investor
#             real_estates_instance.provider = input.investor
#             real_estates_instance.address = input.address
#             real_estates_instance.totalAcreage = input.totalAcreage
#             real_estates_instance.constructionAcreage = input.constructionAcreage
#             real_estates_instance.buildingDensity = input.buildingDensity
#             real_estates_instance.type = input.type
#             real_estates_instance.price = input.price
#             real_estates_instance.handoverDate = input.handoverDate
#             real_estates_instance.scale = input.scale
#             real_estates_instance.link = input.link
#             real_estates_instance.introduction = input.introduction
#             real_estates_instance.province = input.province,
#             real_estates_instance.district = input.district,
#             real_estates_instance.images.set(images),
#             real_estates_instance.save()
#             return UpdateRealEstates(ok=ok, realEstate=real_estates_instance)
#         return UpdateRealEstates(ok=ok, realEstate=None)


class DeleteJob(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        job_instance = Job.objects.get(pk=id)
        job_instance.delete()
        return cls(ok=True)


class Mutation(graphene.ObjectType):
    # create_project_images = CreateProjectImages.Field()
    # update_project_images = UpdateProjectImages.Field()
    delete_job = DeleteJob.Field()
