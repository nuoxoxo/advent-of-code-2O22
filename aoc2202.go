package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
	_ "io/ioutil"
	_ "strconv"
)

func solve(path string) (int, int) {
	data, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	var a [][]string
	scanner := bufio.NewScanner(data)
	scanner.Split(bufio.ScanLines)
	for scanner.Scan() {
		temp := strings.Split(scanner.Text(), " ")
		a = append(a, temp)
	}

	// solve

	res := 0
	rr := 0
	res2 := 0
	d := map[string]int {
		"A": 1, "B": 2, "C": 3,
		"X": 1, "Y": 2, "Z": 3,
	}
	for _, line := range a {
		l, r := d[line[0]], d[line[1]]

		// part 1

		if l == r {
			res += r + 3
		} else {
			res += r
			rr = l + 1
			if rr > 3 {
				rr = 1
			}
			if rr == r {
				res += 6
			}
		}

		// part 2

		if r == 2 {
			res2 += l + 3
		} else if r == 1 {
			l -= 1
			if l < 1 {
				l = 3
			}
			res2 += l
		} else {
			l += 1
			if l > 3 {
				l = 1
			}
			res2 += l + 6
		}
	}
	return res, res2
}

func main() {

	var r1, r2 int

	r1, r2 = solve("_inputs/2202.0")
	fmt.Println("data")
	fmt.Println("Star 1:", r1)
	fmt.Println("Star 2:", r2, "\n")

	r1, r2 = solve("_inputs/2202.1")
	fmt.Println("test")
	fmt.Println("Star 1:", r1)
	fmt.Println("Star 2:", r2)
}
