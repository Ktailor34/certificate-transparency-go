import subprocess
import time

def main () :
    startTime = time.time()
    repeatTimes = 1
    start = 1
    end = 1000
    MAX_LOGS = 1000
    #MAX_LOGS = 1102363703
    filename = "testFile.txt"
    #timeLogger = []

    for i in range(repeatTimes):
        iterationStartTime = time.time()
        for index in range(1,MAX_LOGS,1000):
            start = index
            end = start + 1000
            process = subprocess.run([f"./ctclient -first {start} -last {end} getentries >> {filename}"], shell=True)
    
        print(f"Iteration Time for {MAX_LOGS}: {round(time.time()-iterationStartTime,2)} running time: {round(time.time()-startTime,2)}")
        #timeLogger.append(time.time()-iterationStartTime)
    
    print("total time: ", round(time.time() - startTime,2))
    print(f"Average time for {MAX_LOGS} for {repeatTimes} iterations: {round((time.time() - startTime)/repeatTimes,2)}") 

if __name__ == "__main__":
    main()
