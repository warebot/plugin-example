from services.base import get_plugin

msg = {"event_type": "CREATE_PO"}
a = msg

worker = get_plugin(msg['event_type'])
worker.process()
