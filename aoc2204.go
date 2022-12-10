package main

import "fmt"
import "bufio"
import "os"
import _"strings" // strings.Contains(hays, "need")
import _"io/ioutil"
import _"strconv"

func solve(path string) (int, int) {
	data, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(data)
	scanner.Split(bufio.ScanLines)
	res1, res2 := 0, 0
	for scanner.Scan() {
		var l, r, ll, rr int
		fmt.Sscanf(scanner.Text(), "%d-%d,%d-%d", &l, &r, &ll, &rr);
		// fmt.Println(l, r, ll, rr)
		if (l <= ll && r >= rr) || (ll <= l && rr >= r) {
			res1++
		}
		if r >= ll && l <= rr {
			res2++
		}
	}
	return res1, res2
}

func main() {
	var r1, r2 int

	r1, r2 = solve("_inputs/2204.0")
	fmt.Println("data")
	fmt.Println("Star 1:", r1)
	fmt.Println("Star 2:", r2, "\n")

	r1, r2 = solve("_inputs/2204.1")
	fmt.Println("test")
	fmt.Println("Star 1:", r1)
	fmt.Println("Star 2:", r2)
}
