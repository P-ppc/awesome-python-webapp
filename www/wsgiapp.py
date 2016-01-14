#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A WSGI application entry.
'''

import logging; logging.basicConfig(level = logging.INFO)
import os

from transwarp import db
from transwarp.web import WSGIApplication, Jinja2TemplateEngine
from config import configs

# init db:
db.create_engine(**configs.db)

# init wsgi app:
wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))

template_engine = Jinja2TemplateEngine(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

wsgi.template_engine = template_engine

import urls

wsgi.add_module(urls)

if __name__ == '__main__':
    wsgi.run(9000, '0.0.0.0')
