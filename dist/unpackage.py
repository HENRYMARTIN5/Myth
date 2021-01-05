import zipfile
with zipfile.ZipFile("package.zip", 'r') as zip_ref:
    zip_ref.extractall("/myth")