package main

import (
    "time"
    "math/rand"
    "fmt"
)

const numbersToSort int = 1000

func bubbleSort(listOfRandomNumbersToSort []int) {
    swapped := true
    for swapped {
        swapped = false

        for i := 1; i < numbersToSort; i++ {
            if listOfRandomNumbersToSort[i-1] > listOfRandomNumbersToSort[i] {
                listOfRandomNumbersToSort[i-1], listOfRandomNumbersToSort[i] = listOfRandomNumbersToSort[i], listOfRandomNumbersToSort[i-1]
                swapped = true
            }
        }
    }
}

func main() {
    start := time.Now()

    var listOfRandomNumbers []int

    for i := 0; i < numbersToSort; i++ {
        listOfRandomNumbers = append(listOfRandomNumbers, rand.Intn(100))
    }

    bubbleSort(listOfRandomNumbers)

    duration := time.Since(start)
    fmt.Println(duration)
}
