__all__ = [
    "Project"
]

from syn10.order import Order


class Project:
    def __init__(
            self,
            **kwargs
    ):
        self.project_id = kwargs.get("id")
        self.project_name = kwargs.get("name")

    def __enter__(self):
        if self.project_id:
            self._get_project()
        elif self.project_name:
            self._create_project()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _create_project(self):
        print(f"creating project with name: {self.project_name}")
        self.project_id = "sdjh98w4"

    def _get_project(self):
        print(f"getting project with id: {self.project_id}")
        self.project_name = "sjkdf"

    def place(self, order: Order = None):
        order.project_id = self.project_id
        order.place()


