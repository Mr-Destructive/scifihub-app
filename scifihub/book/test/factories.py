import factory


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "book.Book"

    name = factory.Sequence(lambda n: f"book{n}")
    author = factory.SubFactory("author.UserFactory")
    genre = factory.Sequence(lambda n: f"genre{n}")
    project = factory.SubFactory("projects.ProjectFactory")


class ChapterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "book.Chapter"

    name = factory.Sequence(lambda n: f"chapter{n}")
    text_content = factory.Sequence(lambda n: f"text_content{n}")
    book = factory.SubFactory("book.BookFactory")
    status = True
    order = factory.Sequence(lambda n: n)
