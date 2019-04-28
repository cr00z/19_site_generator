import json
import markdown
from jinja2 import Environment, FileSystemLoader
import os
import html
from livereload import Server


HTML_FOLDER = 'www'
ARTS_FOLDER = 'articles'


def load_configuration(json_filename):
    try:
        with open(json_filename, encoding='utf-8') as json_file_obj:
            return json.load(json_file_obj)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return


def convert_filename(md_filename):
    return md_filename.replace('.md', '.html').replace(' ', '_').replace('&', '')


def convert_config_to_artdict(config):
    articles = dict()
    for topic in config['topics']:
        articles[topic['slug']] = {'title': topic['title'], 'articles': [] }
    for article in config['articles']:
        articles[article['topic']]['articles'].append({
            'title': html.escape(article['title']),
            'source': 'articles/' + convert_filename(article['source'])
        })
    return articles


def create_index(jinja2_env, artdict):
    jinja2_template = jinja2_env.get_template('index.html')
    return jinja2_template.render(content=artdict)


def save_page(page_path, content):
    if not os.path.exists(os.path.dirname(page_path)):
        os.makedirs(os.path.dirname(page_path))
    with open(page_path, 'w', encoding='utf-8') as out_stream:
        out_stream.writelines(content)


def load_markdown(mdfile_path):
    with open(mdfile_path, encoding='utf-8') as md_stream:
        return ''.join(md_stream.readlines())


def create_article(jinja2_env, article_name, article_html):
    jinja2_template = jinja2_env.get_template('article.html')
    return jinja2_template.render(name=article_name, content=article_html)


def fix_some_translation_bugs(input_html):
    out_html = input_html.replace(
        '<pre><code>:::python',
        '<div class="card"><div class="card-body"><pre>'
    )
    out_html = out_html.replace(
        '<pre><code>:::cpp',
        '<div class="card"><div class="card-body"><pre>'
    )
    return out_html.replace('</code></pre>', '</pre></div></div>')


def make_site():
    jinja2_env = Environment(loader=FileSystemLoader('templates'))
    config = load_configuration('config.json')
    save_page(
        os.path.join(HTML_FOLDER, 'index.html'),
        create_index(jinja2_env, convert_config_to_artdict(config))
    )
    for article in config['articles']:
        md_content = load_markdown(os.path.join('articles', article['source']))
        article_html = fix_some_translation_bugs(markdown.markdown(md_content))
        save_page(
            os.path.join(
                HTML_FOLDER,
                ARTS_FOLDER,
                convert_filename(article['source'])
            ),
            create_article(jinja2_env, html.escape(article['title']), article_html)
        )


if __name__ == '__main__':
    server = Server()
    server.watch('config.json', make_site)
    server.serve(root='www/')
