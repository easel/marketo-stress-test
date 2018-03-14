.PHONY: default
default:
	echo Use "make venv" to initialize, "source ./.venv/bin/activate" to activate

venv: .venv
	python3 -m venv .venv

