from model.project import Project
import random
import string

def test_add_project_mantis(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    old_projects = app.project.get_project_list()
