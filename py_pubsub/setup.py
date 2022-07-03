from setuptools import setup, find_packages

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),  # [package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    # zip_safe=True,
    author='Julian Regner',
    author_email='julian.regner@gmx.de',
    maintainer='student',
    maintainer_email='regnerju69567@th-nuernberg.de',
    keywords=['ROS2', 'tutorial'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=('TODO: Package description'),
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_pubsub.talker:main'
        ],
    },
)
