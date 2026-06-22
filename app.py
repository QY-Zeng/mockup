from flask import Flask

import threading

from resources.service_root import bp as root_bp
from resources.systems import bp as systems_bp
from resources.chassis import bp as chassis_bp
from workers.simulator import simulator_loop
from resources.control import bp as control_bp
from resources.managers import bp as managers_bp
from resources.logs import bp as logs_bp
from models.event_log import event_log

app = Flask(__name__)
app.json.sort_keys = False

event_log.add("Server Started","OK")

threading.Thread(
    target=simulator_loop,
    daemon=True
).start()

app.register_blueprint(root_bp)
app.register_blueprint(systems_bp)
app.register_blueprint(chassis_bp)
app.register_blueprint(control_bp)
app.register_blueprint(managers_bp)
app.register_blueprint(logs_bp)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False
    )
