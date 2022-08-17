from setuptools import find_packages, setup

setup(
    name='netbox-demo',
    version='0.3',
    description='Assists with the operation of NetBox demo instances',
    url='https://github.com/netbox-community/netbox-demo',
    author='Jeremy Stretch',
    license='Apache 2.0',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
