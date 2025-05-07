from flask import jsonify

def ip_svc(request):
    xforwardfor = request.headers.get('X-Forwarded-For', '0.0.0.0')
    return (jsonify({"ip": xforwardfor}), 200, {})