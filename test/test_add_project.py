
from model.project import Project
import random
import string

def test_add_project_mantis(app,json_projects):
    assert app.session.is_logged_in_as("administrator")
    # old_projects = app.project.get_project_list()
    project = Project(name=random_string("name", 10), description=random_string("description", 30))
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.key) == sorted(new_projects, key=Project.key)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])