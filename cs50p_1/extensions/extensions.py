def main():
    file = input("File name: ").lower().strip()
    types_media = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip"
    }
    if "." in file:
        extension = file.rsplit(".", 1)[1]
        if extension in types_media:
            print(types_media[extension])
        else:
            print("application/octet-stream")
    else:
        print("application/octet-stream")

main()