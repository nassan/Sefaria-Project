from sefaria.system.database import db
from sefaria.model.group import Group
from django.contrib.auth.models import User
from django.contrib.auth.models import Group as DjangoGroup

skip = ["Editors", "User Seeds"]
groups = DjangoGroup.objects.all()
for dgroup in groups:
	if dgroup.name in skip:
		continue
	print dgroup.name
	admins = [u.id for u in dgroup.user_set.all()]
	fields = {
		"name": dgroup.name,
		"admins": admins,
		"publishers": [],
		"members": [],
	}
	group = Group().load({"name": dgroup.name})
	if group:
		group.load_from_dict(fields)
		group.save()
	else:
		Group(fields).save()


db.groups.create_index("name")
db.groups.create_index("admins")
db.groups.create_index("publishers")
db.groups.create_index("members")