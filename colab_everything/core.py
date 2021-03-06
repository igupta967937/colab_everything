# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['ColabStreamlit', 'ColabFlask', 'ColabFastapi', 'ColabCustom']

# Cell
import os
import subprocess
from pyngrok import ngrok

# Internal Cell
class ColabBase():
    def __init__(self, port=9999):
        self.port = port
        self._start_server()

    def _start_server(self):
        active_tunnels = ngrok.get_tunnels()
        for tunnel in active_tunnels:
            public_url = tunnel.public_url
            ngrok.disconnect(public_url)
        url = ngrok.connect(addr=self.port, options={"bind_tls": True}, return_ngrok_tunnel=True)
        print(f'Web App can be accessed on: {url.public_url}')

# Cell
class ColabStreamlit(ColabBase):
    def __init__(self, path, port=9999):
        super().__init__(port)
        self.path = path
        self.run_app()

    def run_app(self, debug=True):
        os.system(f"fuser -n tcp -k {self.port}")
        cmd = f'streamlit run {self.path} --server.port {self.port}'
        with subprocess.Popen(
            [cmd],
            shell=True,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
            ) as proc:
                for line in proc.stdout:
                    if debug: print(line, end="")

# Cell
class ColabFlask(ColabBase):
    def __init__(self, path, port=9999):
        super().__init__(port)
        self.path = path
        self.run_app()

    def run_app(self, debug=True):
        os.system(f"fuser -n tcp -k {self.port}")
        cmd = f'FLASK_APP={self.path} flask run --host=0.0.0.0 --port={self.port}'
        with subprocess.Popen(
            [cmd],
            shell=True,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
            ) as proc:
                for line in proc.stdout:
                    if debug: print(line, end="")

# Cell
class ColabFastapi(ColabBase):
    def __init__(self, path, app='app', port=9999):
        super().__init__(port)
        self.path = path
        self.app = app
        self.run_app()

    def run_app(self, debug=True):
        os.system(f"fuser -n tcp -k {self.port}")
        cmd = f'uvicorn {self.path}:{self.app} --reload --port {self.port}'
        with subprocess.Popen(
            [cmd],
            shell=True,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
            ) as proc:
                for line in proc.stdout:
                    if debug: print(line, end="")

# Cell
class ColabCustom(ColabBase):
    def __init__(self, cmd, port=9999):
        super().__init__(port)
        self.cmd = cmd
        self.run_app()

    def run_app(self, debug=True):
        os.system(f"fuser -n tcp -k {self.port}")
        with subprocess.Popen(
            [self.cmd],
            shell=True,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
            ) as proc:
                for line in proc.stdout:
                    if debug: print(line, end="")