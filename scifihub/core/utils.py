import uuid

from slugify import slugify


def get_or_set_slug(self, og_object=None, *args, **kwargs):
    if self.id is None or self.slug is None:
        # new object, generate a UUID-based slug
        uid = uuid.uuid4()
        self.slug = slugify(self.name.__str__() + "-" + str(uid))
    else:
        # an existing object
        if og_object and og_object.name != self.name:
            # name has changed, generate a new UUID-based slug
            uid = uuid.uuid4()
            self.slug = slugify(self.name.__str__() + "-" + str(uid))
    return self.slug
