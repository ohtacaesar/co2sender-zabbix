from setuptools import setup

setup(
    name='co2sender',
    version='0.0.1',
    packages=['co2sender'],
    install_requires=[
      'py-zabbix',
      'CO2Meter@git+https://github.com/heinemml/CO2Meter.git',
    ],
    entry_points={
      'console_scripts': [
        'co2sender=co2sender.cmd:main'
      ]
    }
)
