# Pairwise Testing

This project demonstrates pairwise testing using Python and `pytest`.
The core of the project consists of five example functions located in the
`example_functions` directory, which are tested for all combinations of parameters
in the `tests` directory.

## Project Structure

```css
pairwise_testing_project/
├── example_functions/
│   ├── function1.py
│   ├── function2.py
│   ├── function3.py
│   ├── function4.py
│   └── function5.py
├── tests/
│   ├── test_function1.py
│   ├── test_function2.py
│   ├── test_function3.py
│   ├── test_function4.py
│   └── test_function5.py
├── requirements.txt
├── run.sh
└── README.md
```

### Directories and Files

- `example_functions/`: Contains the example functions for which pairwise tests
  are written.
- `tests/`: Contains test files for each example function. These tests include all
  combinations of parameters for the functions.
- `requirements.txt`: A list of Python packages required to run the project
  (includes `pytest`).
- `run.sh`: A shell script that sets up the virtual environment, installs
  dependencies, and runs the tests.

## Requirements

Before running the tests, make sure you have Python 3.6+ installed.

### Installing Dependencies

You can install the required dependencies by creating a virtual environment
and installing the packages listed in `requirements.txt`. This can be done manually
or using the provided `run.sh` script.

## Running the Project

You have two ways to run the project:

### 1. Using the `run.sh` Script (Recommended)

The `run.sh` script automates the process of setting up the environment,
installing dependencies, and running the tests.

1. Clone the repository:
2. Run the script to set up the virtual environment, install dependencies,
   and run the tests:

   ```css
   ./run.sh
   ```

   This script will create a virtual environment (if not already created),
   activate it, install the required dependencies, run the tests, and then
   deactivate the virtual environment.

### 2. Manually Setting Up and Running the Project

If you prefer to manually set up the environment and run the tests:

1. Clone the repository:
2. Create a virtual environment:

   ```css
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On Linux/Mac:

     ```css
     source venv/bin/activate
     ```

   - On Windows:

     ```css
     venv\Scripts\activate
     ```

4. Install the dependencies:

   ```css
   pip install -r requirements.txt
   ```

5. Run the tests with `pytest`:

   ```css
   pytest
   ```

## Example Functions

Here is an overview of the example functions tested in the project:

- **function1**: Checks for different parity based on two input numbers
  (positive/negative even/odd).
- **function2**: Performs various operations (subtract or divide) on an
  input number until it reaches zero.
- **function3**: Returns a string based on whether the input number is greater
  than, equal to, or less than 100.
- **function4**: Calculates the factorial of a number recursively.
- **function5**: Checks whether two numbers are both positive, both negative,
  or mixed signs.

## Testing with Pairwise Combinations

For each function, the test cases use **pairwise testing**, where all possible
combinations of inputs are tested to ensure the function works correctly across
all input scenarios.
