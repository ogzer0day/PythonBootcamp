import importlib.util
import importlib.metadata
import random
import statistics
import matplotlib.pyplot as plt


def check_pandas():
    """
    Check if the 'pandas' library is installed and print its status.
    
    Returns:
        True if pandas is available, None otherwise.
    """
    if importlib.util.find_spec("pandas") is None:
        print(f"[FAIL] pandas - Data manipulation NOT ready")
        return None
    else:
        print(
            f"[OK] pandas ({importlib.metadata.version('pandas')}) "
            "- Data manipulation ready"
        )
        return True


def check_requests():
    """
    Check if the 'requests' library is installed and print its status.
    
    Returns:
        True if requests is available, None otherwise.
    """
    if importlib.util.find_spec("requests") is None:
        print(f"[FAIL] requests - HTTP client NOT ready")
        return None
    else:
        print(
            f"[OK] requests ({importlib.metadata.version('requests')}) "
            "-  Network access ready"
        )
        return True


def check_matplotlib():
    """
    Check if the 'matplotlib' library is installed and print its status.
    
    Returns:
        True if matplotlib is available, None otherwise.
    """
    if importlib.util.find_spec("matplotlib") is None:
        print(f"[FAIL] matplotlib - Plotting NOT ready")
        return None
    else:
        print(
            f"[OK] matplotlib ({importlib.metadata.version('matplotlib')}) "
            "- Visualization ready"
        )
        return True


def analyze_matrix_data():
    """
    Generate a random matrix and compute the mean of each column.
    
    Returns:
        list[list[float]]: The generated matrix of random floats.
    """
    rows = 100
    cols = 10

    matrix = [[random.random() for _ in range(cols)] for _ in range(rows)]

    column_means = []
    for c in range(cols):
        column = [row[c] for row in matrix]
        column_means.append(statistics.mean(column))

    print("Column means:")
    for i, mean in enumerate(column_means):
        print(f"Col_{i}: {mean:.4f}")

    return matrix


def visualize_matrix(matrix):
    """
    Create a heatmap visualization of the given matrix and save it as PNG.
    
    Args:
        matrix (list[list[float]]): The matrix to visualize.
    """
    plt.figure(figsize=(10, 6))
    plt.imshow(matrix, aspect="auto", cmap="viridis")
    plt.colorbar(label="Value")
    plt.title("Matrix Data Visualization")
    plt.xlabel("Columns")
    plt.ylabel("Rows")

    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    ok_pandas = check_pandas()
    ok_requests = check_requests()
    ok_matplotlib = check_matplotlib()

    print()

    if ok_pandas and ok_requests and ok_matplotlib:
        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")

        df = analyze_matrix_data()

        print("Generating visualization...")
        visualize_matrix(df)

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
    else:
        print("Analysis FAILED!")
        print("Results NOT saved.")
