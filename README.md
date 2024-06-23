# Splitwise Expenses Plotter

This project reads a CSV file containing Splitwise expenses, processes the data to accumulate expenses over time for each person, and generates a plot for each person showing their cumulative expenses.

## Requirements

- Python 3.x
- pandas
- matplotlib

## Setup

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required Python packages**:
    ```bash
    pip install pandas matplotlib
    ```

3. **Place the CSV file**:
    - Ensure your CSV file (`Splitwise expenses Jun 22.csv`) is in the root directory of the project. The file should have the expenses data with a `Date` column and columns for each person's expenses.

## Running the Script

1. **Run the script**:
    ```bash
    python main.py
    ```

2. **Output**:
    - The script will generate cumulative expense plots for each person in the `outputs` directory.

## Project Structure

- `main.py`: The main script that processes the CSV file and generates the plots.
- `outputs/`: Directory where the generated plots are saved.
- `Splitwise expenses Jun 22.csv`: Input CSV file containing expenses data.

## NOTE

- Adjust the column drop logic as per your specific CSV structure.
- Ensure the CSV file contains a 'Date' column in a recognizable date format.

