from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_proj_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.get("http://localhost/mantisbt-1.3.10/manage_proj_page.php")
