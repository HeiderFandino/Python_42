import sys
import os
import site


def main() -> None:
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in")
        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machine can see everything you install")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")

        print("\nThen run this program again")

        print("\nPackage installation path:")
        package_installacion = site.getsitepackages()
        print(package_installacion[0])
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment:", os.path.basename(sys.prefix))
        print("Environment path:", sys.prefix)

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system")

        print("\nPackage installation path:")
        package_installacion = site.getsitepackages()
        print(package_installacion[0])


if __name__ == "__main__":
    main()
