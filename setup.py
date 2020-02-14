from distutils.core import setup

setup(name='nilmtk-contrib',
      version='1.0',
      description='Python Distribution Utilities',
      author='NILMTK developers',
      author_email='',
      url='https://github.com/nilmtk/nilmtk-contrib',
      install_requires=["scikit-learn>=0.21", "keras>=2.2.4", "cvxpy>=1.0.0", "nilmtk", "nilm_metadata"],
      packages=['nilmtk_contrib'],
      package_dir={'nilmtk_contrib': 'disaggregate'},
      long_description=open('README.md').read(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache 2.0',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering :: Mathematics',
      ],
      keywords='smartmeters power electricity energy analytics redd '
               'disaggregation nilm nialm'
      )
