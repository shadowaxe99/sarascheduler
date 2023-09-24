# EmberAIScheduler

EmberAIScheduler is a terminal-based scheduler that provides a convenient and efficient way to organize and schedule your tasks and appointments. It allows you to efficiently manage your tasks and appointments, ensuring that you stay organized and maximize your productivity.

## Installation

To install EmberAIScheduler, please follow the instructions below:

1. Clone the repository:
   ```
   $ git clone https://github.com/your-username/EmberAIScheduler.git
   $ cd EmberAIScheduler
   ```
2. Install the dependencies:
   ```
   $ pip install -r requirements.txt
   ```

## Usage

To use EmberAIScheduler, run the following command:

```shell
$ python scheduler.py
```

Follow the instructions provided by the scheduler to interact with the scheduler and manage your tasks and appointments.

## Features

- Efficient task and appointment management
- Advanced task scheduling and organization
- Automated reminder notifications
- Flexible priority and deadline management
- Support for recurring tasks and appointments
- Seamless calendar integration

## Sample Model Info

The EmberAIScheduler uses a linear regression model to predict task completion time based on various features. The model is trained on a sample dataset provided in the `data.csv` file. The dataset contains three columns: `feature1`, `feature2`, and `target`. The `feature1` and `feature2` columns represent the input features, and the `target` column represents the target variable (task completion time).

To train and evaluate the model, the dataset is split into training and testing sets using the `train_test_split` function from the `sklearn.model_selection` module. The model is then trained using the training set and evaluated using the testing set. The model score (R^2 score) is calculated to assess the performance of the model.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
