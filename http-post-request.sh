# insert BODY data and the Host
# run the script to send the POST request

BODY="a=b05a37e1a0a45b3a39fa1c8606df31e1&b=ed8700a3%20e8e5468e%26bd62999e%2338f9582a"
BODY_LEN=$( echo -n ${BODY} | wc -c )
echo -ne "POST / HTTP/1.0\r\nHost: 127.0.0.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: ${BODY_LEN}\r\n\r\n${BODY}" | nc -vv 127.0.0.1 80

# `a` as value b05a37e1a0a45b3a39fa1c8606df31e1
# `b` as value ed8700a3 e8e5468e&bd62999e#38f9582a

