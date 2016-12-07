from setuptools import setup, find_packages

install_deps = [
    'pysam',
    'pybedtools',
    'rpy2',
]

setup(
    name='pipeclip',
    version='1.1.0',
    packages=find_packages(),
    install_requires=install_deps,
    package_data={
        'pipeclip.lib': ['*.R', '*.sh']
    },
    entry_points={
        'console_scripts': [
            'pipeclip = pipeclip.pipeclip:main',
        ],
    }
)
