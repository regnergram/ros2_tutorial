from setuptools import setup, find_packages

package_name = 'py_pubsub'                                      # hier wird der Name des ROS2-Packages definiert...

setup(
    name=package_name,                                          # ... und hier eingebunden.
    version='0.0.0',
    packages=find_packages(exclude=['test']),  # [package_name],
    data_files=[                                                # alle wichtigen Dateien, die in shares benoetigt werden,
        ('share/ament_index/resource_index/packages',           # werden hier aufgelistet.
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
    classifiers=[                                               # Option aus Intel Object Mapping uebernommen
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=('TODO: Package description'),
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={                                              # hier werden die executables deklariert. Links steht der Name, 
        'console_scripts': [                                    # rechts der relative Pfad, ausgehend von dieser Datei, hin zu 
            'talker = py_pubsub.talker:main'                    # dem Namen des auszufuehrenden Knotens (ohne Dateiendung) und
                                                                # die auszufuehrende Funktion (hier: die main)                 
        ],
    },
)
