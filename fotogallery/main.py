from os import walk

_, _, filenames = next(walk('img'))

print(filenames)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        img {
            width: 400px;
            height: 150px;
            object-fit: cover;
        }
    </style>
</head>
<body>

    <h1>Meine Bildergallerie</h1>
"""
for f in filenames:
    html += '<img src="img/' + f + '">'

html += """
</body>
</html>
"""

print(html)

# Write HTML String to file.html
with open("index.html", "w") as file:
    file.write(html)