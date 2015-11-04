from setuptools import setup, find_packages

setup(
    name="chuk",
    version='0.1',
    description="UK Companies Houses API Client",
    author="Nicholas Amorim",
    author_email="nicholas@alienretro.com",
    url="https://github.com/nicholasamorim/chuk",
    license="MIT",
    packages=find_packages(),
    tests_require=['mock', 'tox'],
    keywords='api consumer client companies house uk government',
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)

