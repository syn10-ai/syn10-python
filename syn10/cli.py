import json
import syn10
from syn10 import main
from typing import Dict, Type, Any


class Auth:
    @classmethod
    def authenticate(cls, args):
        main.authenticate(client_id=args.client_id, client_secret=args.client_secret)
        print(f'export SYN10_TOKEN="{main._auth.token}"')


class Dataset:
    @classmethod
    def info(cls, args):
        dataset_info = syn10.Dataset(id=args.id).info
        print(dataset_info)

    @classmethod
    def list(cls, args):
        datasets = syn10.Dataset.list()
        for dataset in datasets:
            print(dataset)

    @classmethod
    def create(cls, args):
        dataset = syn10.Dataset.create(path=args.path, metadata=args.metadata)
        print(dataset)

    @classmethod
    def update(cls, args):
        dataset = syn10.Dataset(id=args.id)
        dataset.update(**args.params)
        print(dataset)

    @classmethod
    def delete(cls, args):
        dataset = syn10.Dataset(id=args.id)
        dataset.delete()

    @classmethod
    def download(cls, args):
        dataset = syn10.Dataset(id=args.id)
        dataset.download()


class Deliverable:
    @classmethod
    def info(cls, args):
        deliverable_info = syn10.Deliverable(id=args.id).info
        print(deliverable_info)

    @classmethod
    def list(cls, args):
        deliverables = syn10.Deliverable.list()
        for deliverable in deliverables:
            print(deliverable)

    @classmethod
    def delete(cls, args):
        deliverable = syn10.Deliverable(id=args.id)
        deliverable.delete()

    @classmethod
    def download(cls, args):
        deliverable = syn10.Deliverable(id=args.id)
        deliverable.download()


class Project:
    @classmethod
    def info(cls, args):
        dataset_info = syn10.Project(id=args.id).info
        print(dataset_info)

    @classmethod
    def list(cls, args):
        projects = syn10.Project.list()
        for project in projects:
            print(project)

    @classmethod
    def create(cls, args):
        project = syn10.Project.create(name=args.name, metadata=args.metadata)
        print(project)

    @classmethod
    def update(cls, args):
        project = syn10.Project(id=args.id)
        project.update(**args.params)
        print(project)

    @classmethod
    def delete(cls, args):
        project = syn10.Project(id=args.id)
        project.delete()

    @classmethod
    def create_order(cls, args):
        project = syn10.Project(id=args.id)
        type_cls: Any = _get_order_types().get(args.type)
        order = project.create_order(type=type_cls, **args.params)
        print(order)

    @classmethod
    def get_orders(cls, args):
        project = syn10.Project(id=args.id)
        type_cls: Any = _get_order_types().get(args.type)
        orders = project.get_orders(type=type_cls)
        for order in orders:
            print(order)


class Model:
    @classmethod
    def info(cls, args):
        model_info = syn10.Model(id=args.id).info
        print(model_info)

    @classmethod
    def list(cls, args):
        models = syn10.Model.list()
        for model in models:
            print(model)

    @classmethod
    def delete(cls, args):
        model = syn10.Model(id=args.id)
        model.delete()

    @classmethod
    def policy(cls, args):
        model = syn10.Model(id=args.id)
        print(model.policy)

    @classmethod
    def verify(cls, args):
        model = syn10.Model(id=args.id)
        model.verify()

    @classmethod
    def verified(cls, args):
        model = syn10.Model(id=args.id)
        print(model.verified())


class TrainingOrder:
    @classmethod
    def info(cls, args):
        order_info = syn10.TrainingOrder(id=args.id).info
        print(order_info)

    @classmethod
    def list(cls, args):
        orders = syn10.TrainingOrder.list()
        for order in orders:
            print(order)

    @classmethod
    def create(cls, args):
        order = syn10.TrainingOrder.create(project_id=args.project_id, params=args.params)
        print(order)

    @classmethod
    def cancel(cls, args):
        order = syn10.TrainingOrder(id=args.id)
        order.cancel()

    @classmethod
    def delete(cls, args):
        order = syn10.TrainingOrder(id=args.id)
        order.delete()

    @classmethod
    def get_models(cls, args):
        order = syn10.TrainingOrder(id=args.id)
        models = order.get_models()
        for model in models:
            print(model)

    @classmethod
    def estimate(cls, args):
        print(syn10.TrainingOrder.estimate(**args.params))

    @classmethod
    def get_deliverables(cls, args):
        order = syn10.TrainingOrder(id=args.id)
        deliverables = order.get_deliverables()
        for deliverable in deliverables:
            print(deliverable)

    @classmethod
    def status(cls, args):
        order = syn10.TrainingOrder(id=args.id)
        print(order.status)


class SamplingOrder:
    @classmethod
    def info(cls, args):
        order_info = syn10.SamplingOrder(id=args.id).info
        print(order_info)

    @classmethod
    def list(cls, args):
        orders = syn10.SamplingOrder.list()
        for order in orders:
            print(order)

    @classmethod
    def create(cls, args):
        order = syn10.SamplingOrder.create(project_id=args.project_id, params=args.params)
        print(order)

    @classmethod
    def cancel(cls, args):
        order = syn10.SamplingOrder(id=args.id)
        order.cancel()

    @classmethod
    def delete(cls, args):
        order = syn10.SamplingOrder(id=args.id)
        order.delete()

    @classmethod
    def estimate(cls, args):
        print(syn10.SamplingOrder.estimate(**args.params))

    @classmethod
    def get_deliverables(cls, args):
        order = syn10.SamplingOrder(id=args.id)
        deliverables = order.get_deliverables()
        for deliverable in deliverables:
            print(deliverable)

    @classmethod
    def status(cls, args):
        order = syn10.SamplingOrder(id=args.id)
        print(order.status)


def _get_order_types() -> Dict[str, Type[syn10.order.Order]]:
    order_types = {}
    for cls in syn10.order.Order.__subclasses__():
        order_types[cls.__name__] = cls
    return order_types


def api_register(parser):
    def help(args):
        parser.print_help()

    parser.set_defaults(func=help)

    subs = parser.add_subparsers()

    # AUTHENTICATE
    sub = subs.add_parser("authenticate")
    sub.add_argument("-i", "--client_id", required=True)
    sub.add_argument("-s", "--client_secret", required=True)
    sub.set_defaults(func=Auth.authenticate)

    # DATASET
    sub = subs.add_parser("dataset.info")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Dataset.info)

    sub = subs.add_parser("dataset.list")
    sub.set_defaults(func=Dataset.list)

    sub = subs.add_parser("dataset.create")
    sub.add_argument("-p", "--path", required=True)
    sub.add_argument("-m", "--metadata", type=json.loads, default={})
    sub.set_defaults(func=Dataset.create)

    sub = subs.add_parser("dataset.update")
    sub.add_argument("-i", "--id", required=True)
    sub.add_argument("-p", "--params", required=True, type=json.loads)
    sub.set_defaults(func=Dataset.update)

    sub = subs.add_parser("dataset.delete")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Dataset.delete)

    sub = subs.add_parser("dataset.download")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Dataset.download)

    # DELIVERABLE
    sub = subs.add_parser("deliverable.info")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Deliverable.info)

    sub = subs.add_parser("deliverable.list")
    sub.set_defaults(func=Deliverable.list)

    sub = subs.add_parser("deliverable.delete")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Deliverable.delete)

    sub = subs.add_parser("deliverable.download")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Deliverable.download)

    # PROJECT
    sub = subs.add_parser("project.info")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Project.info)

    sub = subs.add_parser("project.list")
    sub.set_defaults(func=Project.list)

    sub = subs.add_parser("project.create")
    sub.add_argument("-n", "--name", required=True)
    sub.add_argument("-m", "--metadata", type=json.loads, default={})
    sub.set_defaults(func=Project.create)

    sub = subs.add_parser("project.update")
    sub.add_argument("-i", "--id", required=True)
    sub.add_argument("-p", "--params", required=True, type=json.loads)
    sub.set_defaults(func=Project.update)

    sub = subs.add_parser("project.delete")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Project.delete)

    sub = subs.add_parser("project.create_order")
    sub.add_argument("-i", "--id", required=True)
    sub.add_argument("-t", "--type", required=True)
    sub.add_argument("-p", "--params", required=True, type=json.loads)
    sub.set_defaults(func=Project.create_order)

    sub = subs.add_parser("project.get_orders")
    sub.add_argument("-i", "--id", required=True)
    sub.add_argument("-t", "--type", required=True)
    sub.set_defaults(func=Project.get_orders)

    # MODEL
    sub = subs.add_parser("model.info")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Model.info)

    sub = subs.add_parser("model.list")
    sub.set_defaults(func=Model.list)

    sub = subs.add_parser("model.delete")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Model.delete)

    sub = subs.add_parser("model.policy")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Model.policy)

    sub = subs.add_parser("model.verify")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Model.verify)

    sub = subs.add_parser("model.verified")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Model.verified)

    # TrainingOrder
    sub = subs.add_parser("training_order.info")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=TrainingOrder.info)

    sub = subs.add_parser("training_order.list")
    sub.set_defaults(func=TrainingOrder.list)

    sub = subs.add_parser("training_order.create")
    sub.add_argument("-i", "--project_id", required=True)
    sub.add_argument("-p", "--params", required=True, type=json.loads)
    sub.set_defaults(func=TrainingOrder.create)

    sub = subs.add_parser("training_order.cancel")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=TrainingOrder.cancel)

    sub = subs.add_parser("training_order.delete")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=TrainingOrder.delete)

    sub = subs.add_parser("training_order.get_models")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=TrainingOrder.get_models)

    sub = subs.add_parser("training_order.estimate")
    sub.add_argument("-p", "--params", required=True, type=json.loads)
    sub.set_defaults(func=TrainingOrder.estimate)

    sub = subs.add_parser("training_order.get_deliverables")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=TrainingOrder.get_deliverables)

    sub = subs.add_parser("training_order.status")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=TrainingOrder.status)

    # SamplingOrder
    sub = subs.add_parser("sampling_order.info")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=SamplingOrder.info)

    sub = subs.add_parser("sampling_order.list")
    sub.set_defaults(func=SamplingOrder.list)

    sub = subs.add_parser("sampling_order.create")
    sub.add_argument("-i", "--project_id", required=True)
    sub.add_argument("-p", "--params", required=True, type=json.loads)
    sub.set_defaults(func=SamplingOrder.create)

    sub = subs.add_parser("sampling_order.cancel")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=SamplingOrder.cancel)

    sub = subs.add_parser("sampling_order.delete")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=SamplingOrder.delete)

    sub = subs.add_parser("sampling_order.estimate")
    sub.add_argument("-p", "--params", required=True, type=json.loads)
    sub.set_defaults(func=SamplingOrder.estimate)

    sub = subs.add_parser("sampling_order.get_deliverables")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=SamplingOrder.get_deliverables)

    sub = subs.add_parser("sampling_order.status")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=SamplingOrder.status)
