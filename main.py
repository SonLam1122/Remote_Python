import requests
import importlib.util
import hashlib

PLUGIN_URL = "https://raw.githubusercontent.com/SonLam1122/Remote_Python/main/plugin.py"
PLUGIN_PATH = "plugin.py"

def download_plugin():
    r = requests.get(PLUGIN_URL, timeout=5)
    r.raise_for_status()
    with open(PLUGIN_PATH, "wb") as f:
        f.write(r.content)

def load_and_run():
    spec = importlib.util.spec_from_file_location(
        "remote_plugin",
        PLUGIN_PATH
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if hasattr(module, "run"):
        module.run()
    else:
        raise RuntimeError("Plugin has no run()")

def main():
    download_plugin()
    load_and_run()

if __name__ == "__main__":
    main()
