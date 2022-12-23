__all__ = [
    "TrainingOrder",
    "SamplingOrder"
]


class Order:
    def __init__(
            self,
            order_id=None,
            project_id=None,
            parameters=None
    ):
        self.order_id = order_id
        self.project_id = project_id
        self.parameters = parameters

    def place(self):
        raise NotImplementedError

    def estimate(self):
        raise NotImplementedError

    def results(self):
        pass

    def status(self):
        pass


class TrainingOrder(Order):
    def __init__(self, order_id=None, project_id=None, parameters=None):
        super(TrainingOrder, self).__init__(
            order_id=order_id, project_id=project_id, parameters=parameters)

    def place(self):
        print(f"placing order with project_id: {self.project_id}")

    def estimate(self):
        pass


class SamplingOrder(Order):
    pass
