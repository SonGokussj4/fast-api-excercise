# Constants
# =========

# Variables
# =========

# Arguments
# =========
all: debug

help:
	@echo "Available commands:"
	@echo "    [all]      ... Run program in debug mode"
	@echo "    debug      ... Run api in debug mode in terminal"
	@echo "    up         ... Run api in background"
	@echo "    down       ... Kill gunicorn process"

debug:
	venv/bin/gunicorn -w 2 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000 --access-logfile - --access-logformat '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"' --error-logfile - --reload

up:
	venv/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000 --access-logfile api.log --access-logformat '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"' --error-logfile api_error.log --daemon

down:
	pkill gunicorn
