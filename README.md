# indicators

**General Information**

This is a Python-based genetic algorithm for indicator-based trading that uses the ta-lib and backtesting.py libraries. The algorithm attempts to find a set of indicators that have the best backtesting results.

**Requirements**

* Python 3.6+
* NumPy
* pandas
* matplotlib
* ta-lib
* backtesting.py

**How to Use**

To use the algorithm, you first need to create an object of the genetic algorithm. The genetic algorithm object needs to be passed the data, the technical library, and the number of indicators as parameters.

After creating an object of the genetic algorithm, you can run it by using the run() method. The run() method will return an array of indicators that have the best backtesting results.

**Settings**

The genetic algorithm includes a number of settings that can be customized. These settings include:

* Population size
* Number of generations
* Breeding rate
* Mutation rate
* Selection rate

**Results**

The genetic algorithm returns an array of indicators that have the best backtesting results. The array of indicators can be used to create a trading strategy and test it on real-world data.

**Examples**

Here are some examples of how to use the genetic algorithm:

* To find a set of indicators that yield a positive return on S&P 500 data, you can create an object of the genetic algorithm and pass it the S&P 500 data, the ta-lib technical library, and the number of indicators 10. You can then run the genetic algorithm by using the run() method. The run() method will return an array of indicators that have the best backtesting results.
* To find a set of indicators that yield a positive return on S&P 500 and NASDAQ 100 data, you can create an object of the genetic algorithm and pass it the S&P 500 and NASDAQ 100 data, the ta-lib technical library, and the number of indicators 15. You can then run the genetic algorithm by using the run() method. The run() method will return an array of indicators that have the best backtesting results.

**Summary**

The Python-based genetic algorithm for indicator-based trading that uses the ta-lib and backtesting.py libraries is a powerful tool that can be used to find a set of indicators that have the best backtesting results. The algorithm is easy to use and flexible, and allows for customization of a number of settings.

**To Do**

* Complete the algorithm
* Add more documentation
* Add more tests
