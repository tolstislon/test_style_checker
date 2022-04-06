from setuptools import setup

setup(
    name='test_style_checker',
    version='0.1.0',
    description="flake8 plugin",
    long_description='flake8 plugin',
    author="tolstislon",
    author_email='tolstislon@gmail.com',
    url='https://github.com/tolstislon/test_style_checker',
    entry_points={
        'flake8.extension': [
            'MC = test_style_checker:CheckerTestFile',
        ],
    },
    packages=['test_style_checker'],
    include_package_data=True,
    install_requires=["flake8>=4.0.1"],
    python_requires='>=3.10',
    license="MIT License",
    zip_safe=False,
    classifiers=[
        'Framework :: Flake8',
        'Intended Audience :: Developers'
    ]
)
