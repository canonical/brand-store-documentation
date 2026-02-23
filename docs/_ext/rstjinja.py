from jinja2 import Environment, BaseLoader
from docutils import nodes
from docutils.parsers.rst import Directive
import re

def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML or LaTeX
    if app.builder.format != 'html' and app.builder.format != 'latex':
        return
    src = source[0]
    template_renderer = Environment(loader=BaseLoader()).from_string(src)
    rendered = template_renderer.render(app.config.html_context)
    source[0] = rendered

def url_param_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    html = f'<span class="dynamic-param" data-param="{text}">__VAR_{text}__</span>'
    return [nodes.raw('', html, format='html')], []

def process_code_blocks(app, doctree, docname):
    """
    Scans code blocks for {{param_name}} and replaces them with 
    the __VAR_param_name__ marker so JS can find it.
    """
    for node in doctree.traverse(nodes.literal_block):
        # Look for {{name}} pattern
        new_text = re.sub(r'\{\{(.*?)\}\}', r'__VAR_\1__', node.astext())
        
        # Replace the internal text of the code block
        new_node = nodes.literal_block(new_text, new_text)
        new_node['language'] = node.get('language') # Keep syntax highlighting
        node.replace_self(new_node)

class UrlFormDirective(Directive):
    """
    Directive to insert a form. 
    Content of the directive defines the input labels and parameter names.
    Usage:
    .. url-form::
       username : Your Name
       city : Your Location
    """
    has_content = True

    def run(self):
        form_html = ['<form class="dynamic-form" method="GET" style="margin: 20px 0; padding: 15px; border: 1px solid #ccc; border-radius: 5px;">']
        
        for line in self.content:
            if ':' in line:
                param_id, label = [item.strip() for item in line.split(':', 1)]
                form_html.append(f'<div style="margin-bottom: 10px;">')
                form_html.append(f'<label style="display:block; font-weight:bold;">{label}:</label>')
                form_html.append(f'<input type="text" name="{param_id}" style="width: 100%; padding: 5px;">')
                form_html.append(f'</div>')
        
        form_html.append('<button type="submit" style="cursor:pointer; padding: 5px 15px;">Update Page</button>')
        form_html.append('</form>')
        
        node = nodes.raw('', "\n".join(form_html), format='html')
        return [node]

def setup(app):
    app.connect("source-read", rstjinja)
    app.add_role("url", url_param_role)
    app.add_directive("url-form", UrlFormDirective)
    app.connect('doctree-resolved', process_code_blocks)
    
    return {"version": "0.1", "parallel_read_safe": True,
            "parallel_write_safe": True}
