import os
from shutil import copytree
import django
from collections import defaultdict

# 1
project_dir = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def new_project_template():
    try:
        for key, val in project_dir.items():
            for i in range(len(val)):
                if not os.path.exists(val[i]):
                    os.makedirs(os.path.join(key, val[i]))
        print(f'Шаблон к проекту {project_dir} готов!')
    except FileExistsError:
        print(f'Шаблон {project_dir} уже создан!')


new_project_template()


# 3


def copy_templates():
    try:
        for r, d, f in os.walk('my_project'):
            if r.count('template') >= 1:
                for i in range(len(f)):
                    if f[i].endswith('html'):
                        copytree(os.path.join(r), 'new_project')
    except FileExistsError:
        print('Файлы скопированы')


copy_templates()


# 4


def stat_files():
    django_dir = django.__path__[0]
    django_files = defaultdict(int)
    for r, d, f in os.walk(django_dir):
        for file in f:
            size = 10 ** len(str(os.stat(os.path.join(r, file)).st_size))
            django_files[size] += 1
    print(django_files)


stat_files()
