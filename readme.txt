Тесты:
curl 'http://localhost:80/uploads/test.txt'
curl 'http://127.0.0.1/uploads/test.txt'
Ожидаемый ответ: Hello world!

curl 'http://127.0.0.1/some.file'
Ожидаемый ответ: Alone in the world was a little catdog

curl 'http://127.0.0.1/hello/?a=1&a=2&b=3'
Ожидаемый ответ:
a=1
a=2
b=3