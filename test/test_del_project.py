from model.project import Project
import random
import string

def test_delete_project(app):
    if len(app.project.get_project_list()) == 0:
        project = Project(name=random_string("name", 10), description=random_string("description", 30))
        app.project.create_new_project(project)
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])