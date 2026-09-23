import importlib
import sys


DEPENDENCIES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def get_dependency_versions() -> dict[str, str | None]:
    versions: dict[str, str | None] = {}

    for package in DEPENDENCIES:
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown")
            versions[package] = version
        except ModuleNotFoundError:
            versions[package] = None

    return versions


def check_dependencies(
    versions: dict[str, str | None],
) -> bool:
    all_available = True

    print("Checking dependencies:")

    for package, description in DEPENDENCIES.items():
        version = versions[package]

        if version is None:
            print(f"[MISSING] {package} - {description}")
            all_available = False
        else:
            print(f"[OK] {package} ({version}) - {description}")

    return all_available


def show_installation_instructions() -> None:
    print("\nMissing dependencies.")
    print("\nInstall with pip:")
    print("pip install -r requirements.txt")

    print("\nInstall with Poetry:")
    print("poetry install")

    print("\nThen run with Poetry:")
    print("poetry run python loading.py")


def compare_package_managers(
    versions: dict[str, str | None],
) -> None:
    print("\nPackage manager comparison:")

    print("\nInstalled package versions:")

    for package, version in versions.items():
        if version is None:
            print(f"{package}: not installed")
        else:
            print(f"{package}: {version}")

    print("\npip:")
    print("  Dependencies: requirements.txt")
    print("  Install: pip install -r requirements.txt")

    print("\nPoetry:")
    print("  Dependencies: pyproject.toml")
    print("  Install: poetry install")
    print("  Run: poetry run python loading.py")


def analyze_matrix_data() -> None:
    np = importlib.import_module("numpy")
    pd = importlib.import_module("pandas")
    plt = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")

    generator = np.random.default_rng()

    matrix_data = generator.integers(
        low=0,
        high=101,
        size=1000,
    )

    dataframe = pd.DataFrame(
        {
            "signal": matrix_data,
        }
    )

    print(f"Processing {len(dataframe)} data points...")

    dataframe["normalized_signal"] = (
        dataframe["signal"] - dataframe["signal"].mean()
    ) / dataframe["signal"].std()

    print(
        f"Mean signal: "
        f"{dataframe['signal'].mean():.2f}"
    )
    print(
        f"Minimum signal: "
        f"{dataframe['signal'].min()}"
    )
    print(
        f"Maximum signal: "
        f"{dataframe['signal'].max()}"
    )

    print("Generating visualization...")

    plt.figure(figsize=(10, 6))

    plt.hist(
        dataframe["signal"],
        bins=20,
    )

    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal strength")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> int:
    print("LOADING STATUS: Loading programs...")

    versions = get_dependency_versions()

    dependencies_ready = check_dependencies(versions)

    compare_package_managers(versions)

    if not dependencies_ready:
        show_installation_instructions()
        return 1

    analyze_matrix_data()

    return 0


if __name__ == "__main__":
    sys.exit(main())
