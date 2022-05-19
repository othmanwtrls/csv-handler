from yattag import Doc, indent

def generate_html_from_csv_list(csv_list):
    doc, tag, text = Doc().tagtext()

    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            doc.stag('link', rel="stylesheet", href="https://www.w3schools.com/w3css/4/w3.css")
        with tag('body', style="padding: 30px 60px;"):
            with tag('table', klass='w3-table-all'):
                with tag('caption'):
                    text('Task Manager')
                with tag('tr', klass='w3-green'):
                    for i in csv_list[0]:
                        with tag('th'):
                            text(i)
                for i in csv_list[1:]:
                    with tag('tr', klass='w3-hover-grey'):
                        for j in i:
                            with tag("td"):
                                text(j)

    with open("task_manager_generated.html", 'w') as hs:
        hs.write(indent(doc.getvalue()))
