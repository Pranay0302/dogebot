import dogerep

rt = dogerep.repeat_interval()
while rt:
    try:
        rt
        print('success')
    except Exception as error:
        print(error)
        exit(0)
