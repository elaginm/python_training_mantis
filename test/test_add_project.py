from model.project import Project
import random
import string
import re


def test_add_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    app.session.ensure_login(username, password)
    assert app.session.is_logged_in_as(username)
    old_projects = app.soap.get_project_list_soap(username, password)
    project = Project(name=random_string("name", 10), description=random_string("description", 30))
    app.project.create_new_project(clear(project))
    new_projects = app.soap.get_project_list_soap(username, password)
    old_projects.append(clear(project))
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def clear(project):
    return Project(id=project.id, name=re.sub("[ ]{2,}", " ", (project.name).strip()),
                   description = re.sub("[ ]{2,}", " ", (project.description).strip()))