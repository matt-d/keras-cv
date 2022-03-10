# Copyright 2019 The KerasCV Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup script."""

from setuptools import find_packages
from setuptools import setup

setup(
    name="keras-cv",
    description="Industry-strength computer Vision extensions for Keras.",
    url="https://github.com/keras-team/keras-cv",
    author="Keras team",
    author_email="keras-cv@google.com",
    license="Apache License 2.0",
    install_requires=["packaging", "tf-nightly", "absl-py"],
    extras_require={
        "tests": ["flake8", "isort", "black", "pytest"],
        "examples": ["tensorflow_datasets", "matplotlib"],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
    ],
    packages=find_packages(exclude=("*_test.py",)),
)
