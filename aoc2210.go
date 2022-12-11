package main

import "fmt"
import "io/ioutil"
import "strings"
import "strconv"

func solve(path string) (int, string) {
	data, err := ioutil.ReadFile(path)
	if err != nil {
		panic(err)
	}
	lines := string(data)
	var dp []int
	for _, line := range strings.Split(lines, "\n") {
		dp = append(dp, 0)
		temp := strings.Split(line, " ")
		if line != "noop" && line != ""  {
			n, err := strconv.Atoi(temp[1]) // atoi needs err
			if err != nil {
				panic(err)
			}
			dp = append(dp, n)
		}
	}

	var x, i, cc, res, size int
	var res2 string

	// part 1

	size = len(dp)
	x = 1
	i = 0
	cc = 0
	res = 0
	for cc < 220 + 1 {
		if i == size {
			i %= size
		}
		n := dp[i]
		if (i + 1) % 40 == 20 {
			res += (i + 1) * x
		}
		i++
		cc++
		x += n
	}

	// part 2

	i = 0
	x = 1
	cc = 0
	for cc < 240 + 1 {
		if i == size {
			i %= size
		}
		ok := false
		for _, n := range []int {x - 1, x, x + 1} {
			if i % 40 == n {
				ok = true
			}
		}
		if ok {
			res2 += "@"
		} else {
			res2 += " "
		}
		if (i + 1) % 40 == 0 {
			res2 += "\n"
		}
		x += dp[i]
		cc++
		i++
	}
	return res, res2
}

func main() {
	var r1 int
	var r2 string

	r1, r2 = solve("_inputs/2210.0")
	fmt.Println("data")
	fmt.Println("Star 1:", r1)
	fmt.Print("Star 2:\n", r2, "\n")

	r1, r2 = solve("_inputs/2210.1")
	fmt.Println("test")
	fmt.Println("Star 1:", r1)
	fmt.Print("Star 2:\n", r2)
}
