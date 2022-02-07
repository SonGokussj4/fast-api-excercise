# Constants
# =========

# Variables
# =========

# Arguments
# =========
all: debug

help:
	@echo "Available commands:"
#	@echo "    test       ... Do tests... Duh..."

debug:
	venv/bin/uvicorn app.main:app --reload


# test:
# 	@echo "Not implemented yet..."
