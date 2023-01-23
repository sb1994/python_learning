def unicode_errors():
    try:
        b'\x81'.decode('utf-8')
    except UnicodeError as e:
        print(e)
        print("encoding:", e.encoding)
        print("reason:", e.reason)
        print("object:", e.object)
        print("end:", e.end)


if __name__ == 'main':
    unicode_errors()
