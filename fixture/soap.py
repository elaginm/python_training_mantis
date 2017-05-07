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
    #
    # def get_project_list_soap(self):
    #     client = Client('http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl')
    #     project_list = []
    #     for project in client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'],
    #                                                               self.app.config['webadmin']['password']):
    #     projects_list.append(Project(name=project.name, description=project.description))
    #     pass

    def get_project_list_soap(self):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'], self.app.config['webadmin']['password'])
        pass


