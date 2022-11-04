from setuptools import setup,find_packages
setup(
      name='krishna',
      version='0.2',
      description='Testing installation of Python Package',
      url='#',
      author='Ramesh',
      author_email='rameshhb@email.com',
      license='MIT',
      package_dir={"": "src"},
      packages=find_packages(
          where="src",
      ),
      entry_points={
          "console_scripts": [
              "package=krishna.main:main",
          ],
      },
      install_requires=[
        'boto'
      ],
      zip_safe=False
)
