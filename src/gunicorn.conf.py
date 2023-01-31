import multiprocessing
import dashboard

app_host, app_port = dashboard.get_host_bind()

user = 0
group = 0
threads = 4
bind = f"127.0.0.1:{app_port}"
daemon = True
pidfile = '/run/gunicorn.pid'
errorlog = '/var/log/gunicorn_error_log.log'
accesslog = '/var/log/gunicorn_access_log.log'