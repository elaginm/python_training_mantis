from model.project import Project
import re

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith('/manage_proj_page.php'):
            wd.get('http://localhost/mantisbt-1.3.10/manage_proj_page.php')

    def create_new_project(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath('//input[@value="создать новый проект"]').click()
        self.fill_project_form(project)
        wd.find_element_by_xpath('//input[@value="Добавить проект"]').click()
        wd.find_element_by_xpath('//a[contains(text(),"Продолжить")]').click()
        self.project_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(text)

    def fill_project_form(self, project):
        self.change_field_value('project-name', project.name)
        self.change_field_value('project-description', project.description)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_project_page()
            self.project_cache = []
            l = len(wd.find_elements_by_xpath('//table/tbody/tr/td[1]/a'))
            for i in range(l):
                index = i + 1
                element = wd.find_element_by_xpath('//table/tbody/tr['+str(index)+']/td[1]/a')
                name = element.text
                href = element.get_attribute("href")
                id = int(re.search("\d+$", href).group(0))
                description = wd.find_element_by_xpath('//table/tbody/tr['+str(index)+']/td[5]').text
                self.project_cache.append(Project(id=id, name=name, description=description))
        return list(self.project_cache)