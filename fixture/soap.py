from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.soap_url)
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list_soap(self, username, password):
        client = Client(self.app.soap_url)
        project_list = []
        try:
            for project in client.service.mc_projects_get_user_accessible(username, password):
                project_list.append(Project(id=project.id, name=project.name, description=project.description))
            return project_list
        except WebFault:
            return False