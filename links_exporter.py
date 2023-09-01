import csv
from jinja2 import Environment, FileSystemLoader

def create_links_html():
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("links_template.html")
    context = {
        "links": read_links()
    }

    filename = "links.html"
    content = template.render(context)
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")


def read_links():
    with open('./links.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader) # Skip/Ignore first line
        ## Type,Name,Why,Link,Info
        links = []
        for row in reader:
            link = row[4]
            if link and len(link) > 0:
                # print(', '.join(row))
                print(f'\t{row[1]} Link: [{link}].')
                links.append({"type": row[0], "service_name": row[1], "service_url": row[2], "motiv": row[3], "url": row[4], "explanation": row[5]})
        return links 

if __name__ == '__main__':
    create_links_html()
