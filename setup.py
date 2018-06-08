import setuptools

import lsp_ws

with open('README.md', 'r') as f:
    long_description = f.read()


setuptools.setup(
    name='lsp_ws',
    version=lsp_ws.__version__,
    python_requires='>3.5',
    author='Brijesh Bittu',
    author_email='brijeshb42@gmail.com',
    description='Python LSP over websockets',
    long_description=long_description,
    url='https://github.com/brijeshb42/lsp_ws/',
    include_package_data=False,
    zip_safe=False,
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'python-language-server',
        'autobahn'
    ],
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
    entry_points={
        'console_scripts': [
            'lsp_ws = lsp_ws.__main__:main'
        ]
    },
    keywords=['lsp', 'websocket'],
)
