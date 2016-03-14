def application(env, start_response):
  status = '200 OK'
  headers = [
    ('Content-Type', 'text/plain')
  ]
  body = env['QUERY_STRING'].split('&')
  body = [item + "\r\n" for item in body]
  start_response(status, headers)
  return body 
