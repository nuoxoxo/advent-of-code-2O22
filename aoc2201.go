package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"strconv"
	"sort"
)

var path string = "_inputs/2201.0"
// var path string = "_inputs/2201.1"

func main() {
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

	fmt.Println("Star 1:", res)
	fmt.Println("Star 2:", res2)
}
