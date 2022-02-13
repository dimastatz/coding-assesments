# Part 1: Python Multiprocessing

## Objectives
Write a small Python application with two processes, running on the same machine. The two processes will communicate over a socket. (Randomly generated) vectors from the first process will be sent to the second process. These “data” vectors should be accumulated in the second process in a matrix. Some simple statistics will be computed (across the “temporal” dimension). Results should be saved to a file.

## Requirements
- The code should run from a single main function.
- Use the Numpy module for calculations.
- Process #1.
    - Data vector generation:
        - Vector entries should be randomly sampled from a Normal Gaussian distribution.
        - Vector length should be set to 50.
    - Data communication
        - Vectors should be then sent across the socket at a rate of 1,000 Hz, as temporally accurately as possible.
        - Add a “noisy mode“ (with a parameter flag), which when turned on:
            - Vectors should be randomly dropped (mimicking packet loss).
            - The vector dropping should happen randomly “once in a while“, defined as: according to a uniform distribution, in the interval of [2, 3] seconds.
- Process #2.
    - Data communication
        - Process #2 should connect to Process #1 over a socket.
        - Process #2 should expect to receive vectors over the socket at a rate of 1,000 Hz.
        - The actual rate of data acquisition should be calculated, and printed to the screen.
        - The mean and standard deviation should also be calculated for (a series) of rates of data acquisition.
        - During “noisy mode“, process #2 should:
            - Handle packet loss, and issue a warning to the screen.
            - Adjust rate calculations (iii. and iv. above) to deal with this case.
        - Data analytics
            - Vectors received by Process #2 should be accumulated into a series of matrices, each matrix should be 100 vectors long.
            - The mean and standard deviation should be calculated for each matrix, along its “temporal” dimension.
        - Results file
            - All results should be saved in a single file. Please save:
                - Data acquisition rates
                - Mean and standard deviation of the data acquisition rates
                - “Data Analytics” results (b.ii. above)

## Deliverables:
- Your complete code, in a form we can run easily.
- Instructions how to run your project.
- All deliverables should be uploaded to a Git repository.