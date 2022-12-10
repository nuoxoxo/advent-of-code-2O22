package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"strconv"
	"sort"
)

func main() {
	var r1, r2 int

	r1, r2 = solve("_inputs/2201.0")
	fmt.Println("data")
	fmt.Println("Star 1:", r1)
	fmt.Println("Star 2:", r2, "\n")

	r1, r2 = solve("_inputs/2201.1")
	fmt.Println("test")
	fmt.Println("Star 1:", r1)
	fmt.Println("Star 2:", r2)
}

func solve(path string) (int, int) {
	data, err := ioutil.ReadFile(path)
	if err != nil {
		panic(err)
	}
	lines := string(data)
	var a []int
	for _, line := range strings.Split(lines, "\n\n") {
		sum := 0
		for _, l := range strings.Split(line, "\n") {
			n, err := strconv.Atoi(l)
			if err != err {
				panic(err)
			}
			sum += n
		}
		a = append(a, sum)
	}

	// part 1 . find max in slice

	res := 0
	for i, n := range a {
		if i == 0 || res < n {
			res = n
		}
	}

	// part 2 . sum of the max 3

	// way 1 . inituitive
	/*
	sort.Ints(a)
	n := len(a) - 1
	res2 := a[n] + a[n - 1] + a[n - 2]
	*/

	// way 2 . reverse sort
	sort.Sort(sort.Reverse(sort.IntSlice(a)))
	res2 := a[0] + a[1] + a[2]

	return res, res2
}
