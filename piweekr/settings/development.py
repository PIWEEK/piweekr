from .common import *

INSTALLED_APPS += ['sampledatahelper']

SAMPLEDATAHELPER_MODELS = [
    { 'model': 'projects.Role', 'number': 5, },
    { 'model': 'projects.Project', 'number': 10, },
    { 'model': 'projects.ProjectRole', 'number': 20, },
]
