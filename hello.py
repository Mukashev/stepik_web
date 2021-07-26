def app(environ, start_response):
    body = '\n'.join(environ['QUERY_STRING'].split('&')) + '\n'
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(body)))
    ]
    start_response(status, headers)
    return [bytes(body, 'utf-8')]