from setuptools import setup

setup(
    name='atbash',
    version='0.1.0',
    packages=['atbash'],
    include_package_data=True,
    license='MIT License',
    description='Atbash Cihper CLI.',
    author='Alec Bush',
    author_email='alexander.joseph.bush@gmail.com',
    entry_points={
        'console_scripts': [
            'atbash=atbash.__main__:run_command_line',
        ],
    },
    install_requires=[
    ],
    tests_require=[
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='python atbash cipher cli',
)
