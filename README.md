# GreedyRouteFinder | Heuristic Delivery Route Planner (Python)
CLI application that utilizes a self-adjusting heuristic algorithm merging nearest neighbor and greedy
strategies to enhance route planning based on client requirements for on-time deliveries.


## Project Overview



## Project Structure

The project is organized into several Python source files and two CSV data files:

- `main.py`: This is the main entry point of the program. It orchestrates the execution of various tasks, such as 
loading data, creating packages and trucks, and running the delivery algorithm.

- `Hash.py`: This file contains the implementation of a chaining hash table used to efficiently store and retrieve 
package data based on package IDs.

- `helper.py`: This module provides a collection of utility functions that are shared by multiple components of the 
program, enhancing code modularity and reusability.

- `Package.py`: Here, you'll find the definition of the `Package` class, which represents individual packages with 
attributes like delivery deadline, weight, and special notes.

- `Truck.py`: This file contains the implementation of the `Truck` class, which represents a delivery truck and manages 
the loading and unloading of packages.

- `distances.csv`: This CSV file stores distance data between addresses. It is used by the algorithm to calculate the 
shortest delivery routes. Please note that distances are assumed to be equal both ways for simplicity.

- `package_data.csv`: This CSV file contains detailed package information, including addresses, delivery deadlines, 
package weights, and special notes.

The project's structure is designed to promote code organization and modularity, making it easier to understand and maintain. In future updates and optimizations, additional files and modules may be introduced to enhance the program's functionality and performance.

## Dependencies

- **Python Standard Libraries:** The following Python standard libraries are used in this project:
  - `datetime`: for date and time manipulation.
  - `csv`: for reading and writing CSV files.

## Installation

To run this program, you can follow these steps:

1. **Clone the Repository:** Start by cloning this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/jadamb13/GreedyRouteFinder.git 
   ```
2. Navigate to the Project Directory: Change your working directory to the project folder:

    ```bash
    cd GreedyRouteFinder
    ```
3. Python Environment: Ensure you have Python 3.11 or a higher version installed on your system. If not, you can 
download it from Python's official website.

4. Install Dependencies: Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```


5. Run the Program: You can now execute the program by running the following command:

```bash
python main.py
```

Follow the on-screen instructions to interact with the program.


## Usage

### Option 1: View the Status of All Packages at a Specific Time

To view the status of all packages at a specific time, follow these steps:

1. Run the program by executing `python main.py`.
2. Choose option 1 from the menu.
3. Enter a 24-hour time in the format `hh:mm` (e.g., 15:00 for 3:00 PM) when prompted.
4. The program will display a formatted list of all packages, including their address, delivery deadline (if applicable), weight, current status, and delivery time (if applicable) at the specified time.

### Option 2: View the Status of an Individual Package at a Specific Time

To view the status of an individual package at a specific time, follow these steps:

1. Run the program by executing `python main.py`.
2. Choose option 2 from the menu.
3. Enter the package ID when prompted.
4. Enter a 24-hour time in the format `hh:mm` (e.g., 15:00 for 3:00 PM) when prompted.
5. The program will display the status of the specified package, including its address, delivery deadline (if applicable), weight, current status, and delivery time (if applicable) at the specified time.

### Option 3: View Total Mileage of All Trucks

To view the total mileage covered by all trucks after their routes have been completed, follow these steps:

1. Run the program by executing `python main.py`.
2. Choose option 3 from the menu.
3. The program will display the total mileage covered by each truck and the combined total mileage for all trucks.

### Option 4: View a Delivery Report for Packages with Delivery Deadlines

To view a delivery report for packages with delivery deadlines, follow these steps:

1. Run the program by executing `python main.py`.
2. Choose option 4 from the menu.
3. The program will display a report containing package information for all packages from all trucks that had delivery deadlines.


## Data Files

## Functionality

## Project Highlights

## Future Improvements

## Contact Information

## License