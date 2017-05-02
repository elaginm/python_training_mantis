from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.get("http://localhost/mantisbt-1.3.10/manage_proj_page.php")


    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_project_page()
            self.project_cache = []
            for i in wd.find_elements_by_xpath()
