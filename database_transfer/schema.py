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
    jobs_by_salary = graphene.List(
        JobType,
        args={
            'min': graphene.Int(),
            'max': graphene.Int(),
        }
    )
    jobs = graphene.List(
        JobType,
        orderBy=graphene.List(of_type=graphene.String),
        limit=graphene.Int()
    )
    total_job = graphene.Int()

    def resolve_total_job(self, info, **kwargs):
        return Job.objects.count()

    def resolve_job(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Job.objects.get(pk=id)

        return None

    def resolve_jobs_by_salary(self, info, **kwargs):
        _min = kwargs.get("min", None)
        _max = kwargs.get("max", None)
        return Job.objects.filter(salary_normalize__gte=_min, salary_normalize__lte=_max)

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


class CreateJob(graphene.Mutation):
    class Arguments:
        input = JobInput(required=True)

    ok = graphene.Boolean()
    investors = graphene.Field(JobType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        projects = list()
        job_instance = Job(
            id=input.id,
            title=input.title,
            created_time=input.created_time,
            currency_unit=input.currency_unit,
            salary=input.salary,
            salary_normalize=input.salary_normalize,
            url=input.url,
            company=input.company,
            location=input.location,
            info=input.info,
            degree_requirements=input.degree_requirements,
            deadline_submit=input.deadline_submit,
            experience=input.experience,
            no_of_opening=input.no_of_opening,
            formality=input.formality,
            position=input.position,
            gender_requirements=input.gender_requirements,
            career=input.career,
            description=input.description,
            benefit=input.benefit,
            job_requirements=input.job_requirements,
            profile_requirements=input.profile_requirements,
            contact=input.contact,
            other_info=input.other_info
        )
        job_instance.save()
        return CreateJob(ok=ok, investors=job_instance)


class UpdateProjectImages(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = JobInput(required=True)

    ok = graphene.Boolean()
    projectImages = graphene.Field(JobType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        job_instance = Job.objects.get(pk=id)
        if job_instance:
            ok = True
            job_instance.id = input.id
            job_instance.title = input.title
            job_instance.created_time = input.created_time
            job_instance.currency_unit = input.currency_unit
            job_instance.salary = input.salary
            job_instance.salary_normalize = input.salary_normalize
            job_instance.url = input.url
            job_instance.company = input.company
            job_instance.location = input.location
            job_instance.info = input.info
            job_instance.degree_requirements = input.degree_requirements
            job_instance.deadline_submit = input.deadline_submit
            job_instance.experience = input.experience
            job_instance.no_of_opening = input.no_of_opening
            job_instance.formality = input.formality
            job_instance.position = input.position
            job_instance.gender_requirements = input.gender_requirements
            job_instance.career = input.career
            job_instance.description = input.description
            job_instance.benefit = input.benefit
            job_instance.job_requirements = input.job_requirements
            job_instance.profile_requirements = input.profile_requirements
            job_instance.contact = input.contact
            job_instance.other_info = input.other_info
            job_instance.save()
            return UpdateProjectImages(ok=ok, projectImages=job_instance)
        return UpdateProjectImages(ok=ok, projectImages=None)


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
