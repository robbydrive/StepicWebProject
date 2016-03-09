import urllib.parse

def application(env, start_response):
  status = '200 OK'
  headers = [
    ('Content-Type', 'text-plain')
  ]
  qsl = parse_sql(QUERY_STRING, keep_blank_values=True)
  body = ''
  for elem in qsl:
    body.append('{0}={1}\n'.format(elem[0], elem[1]))
  body = body[:len(body)-2]
  start_response(status, headers)
  return [ body ]
