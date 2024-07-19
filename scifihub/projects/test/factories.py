import factory


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "projects.Project"

    name = factory.Sequence(lambda n: f"project{n}")
    description = factory.Sequence(lambda n: f"description{n}")
    author = factory.SubFactory("author.UserFactory")
    visibility = factory.Sequence("public")
    status = factory.Sequence("published")
    project_type = factory.Sequence("Test Type")
