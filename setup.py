from setuptools import setup,find_packages

setup(name = "census_income",
      version ="0.0.1",
      author = "fariz",
      author_email = "isobronts8@gmail.com",
      packages = find_packages(), # Will only consider packages where there is a __init__.py file
      install_requires = ["pandas","numpy","flask"], # We can also create a function to automatically add required packages (e.g. when there are 100's of packages you cant write each package name manually)
      )
