from socket import timeout


bind = '127.0.0.1:8000'
workers = 3
user = 'dony31'
timeout = 120

#  gunicorn Investsite.wsgi:application --bind 64.225.68.196:8000
#  pkill gunicorn