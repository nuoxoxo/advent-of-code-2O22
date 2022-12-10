package main

import "fmt"
import "io/ioutil"
import "sort"

func solve(path string) (int, int) {
	data, err := ioutil.ReadFile(path)
	if err != nil {
		panic(err)
	}
	s := string(data)
	n := len(s)
	var i, j int
	var ok bool

	// part 1

	i = 0
	res := -1
	for i < n - 4 {
		c4 := s[i : i + 4]
		a := []rune (c4)
		sort.Slice(a, func(l int, r int) bool {
			return a[l] < a[r]
		})
		j = 0
		ok = true // check if a contains no repeated runes
		for j < 3 {
			if a[j] == a[j + 1] {
				ok = false
			}
			j++
		}
		if ok {
			res = i + 4
			break
		}
		i++
	}

	// part 2

	res2 := -1
	p2 := 14
	i = 0
	for i < n - p2 {
		c4 := s[i : i + p2]
		a := []rune (c4)
		sort.Slice(a, func(l int, r int) bool {
			return a[r] < a[l]
		})
		j = 0
		ok = true // check if a contains no repeated runes
		for j < p2 - 1 {
			if a[j] == a[j + 1] {
				ok = false
			}
			j++
		}
		if ok {
			res2 = i + p2
			break
		}
		i++
	}
	return res, res2
}

func main() {
	var r1, r2 int

	r1, r2 = solve("_inputs/2206.0")
	fmt.Println("data")
	fmt.Println("Star 1:", r1)
	fmt.Println("Star 2:", r2, "\n")

	r1, r2 = solve("_inputs/2206.1")
	fmt.Println("test")
	fmt.Println("Star 1:", r1)
	fmt.Println("Star 2:", r2)
}
