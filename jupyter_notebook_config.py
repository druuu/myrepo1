c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.token = ''
c.NotebookApp.allow_origin = '*'
c.NotebookApp.disable_check_xsrf = True
c.NotebookApp.tornado_settings = {
    "headers": {
        "Content-Security-Policy": "frame-ancestors 'self' *"
    }
}
c.NotebookApp.iopub_data_rate_limit=10000000000;
