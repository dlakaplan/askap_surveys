from setuptools import setup, find_packages

setup(
    name="askap_surveys",
    version="0.1.0",
    description="Repository of ASKAP survey footprints and other relevant surveys.",
    author="David Kaplan",
    author_email="kaplan@uwm.edu",
    url="",
    packages=find_packages(),
    scripts=["scripts/askap_field_to_moc.py", "scripts/sky_coverage_plot.py"],
    python_requires='>=3.7',
    include_package_data=True,
)
