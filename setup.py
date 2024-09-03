"""Setup module."""

from setuptools import setup

setup(
    name="framedipt",
    version="0.1.0",
    description="Diffusion Model for Protein Structure Inpainting",
    # packages=["framedipt", "experiments", "evaluation", "openfold"],
    packages=["framedipt", "openfold"],
    package_dir={
        "framedipt": "./framedipt",
        "openfold": "./openfold",
        # "experiments": "./experiments",
        # "evaluation": "./evaluation",
    },
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
        "biopython==1.81",
        "hydra-core",
        "tqdm",
        "scikit-learn",
        "absl-py",
        "fair-esm",
        "biotite",
        "mdtraj",
        "gputil",
        "tmtools",
        "matplotlib",
        "seaborn",
        # # Packages below need to installed using conda / mamba, or from github.
        # "anarci",
        # "openmm",
        # "pdbfixer",
    ],
)
