class PluginManager(type):
    def __init__(cls, name, bases, attrs):
        #super(PluginManager, cls).__init__(name, bases, attrs)

        if not hasattr(cls, 'plugins'):
            cls.plugins = {}
        else:
            cls.register_plugin(cls)

    def register_plugin(cls, plugin):
        instance = plugin()
        cls.plugins[instance.name()] = plugin


def get_plugin(name):
    return Plugin.plugins.get(name)()


class Plugin(object):
    __metaclass__ = PluginManager

    def process(self):
        raise NotImplementedError

    def name(self):
        raise NotImplementedError


from services.purchase_order_service import PurchaseOrderService

