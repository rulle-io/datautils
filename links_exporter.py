import csv
from jinja2 import Environment, FileSystemLoader

def create_links_files():
    environment = Environment(loader=FileSystemLoader("templates/"))
    context = {
        "links": read_links()
    }
    md_template_file = "links_template.md"
    md_output_filename = "links.md"
    create_links_generic(environment, context, md_template_file, md_output_filename)

    html_template_file = "links_template.html"
    html_output_filename = "links.html"
    create_links_generic(environment, context, html_template_file, html_output_filename)

def create_links_generic(environment, context, template_file, output_filename):
    template = environment.get_template(template_file)
    content = template.render(context)
    create_output_file(content, output_filename)


def create_output_file(content, filename):
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")


def read_links():
    with open('./links.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # Skip/Ignore first (headers) line
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
    create_links_files()
