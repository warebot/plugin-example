from services.base import Plugin


class PurchaseOrderService(Plugin):
    def __init__(self):
        pass

    def name(self):
        return "CREATE_PO"

    def process(self):
        print('I am processing something super important here')