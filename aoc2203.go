package main

import (
	"fmt"
	"bufio"
	"os"
	"strings" // strings.Contains(hays, "need")
	_ "io/ioutil"
	_ "strconv"
)

func solve(path string) (int, int) {
	data, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	var a []string
	scanner := bufio.NewScanner(data)
	scanner.Split(bufio.ScanLines)
	for scanner.Scan() {
		a = append(a, scanner.Text())
	}
	res, res2 := 0, 0
	for i, line := range a {
		n := len(line)
		L := line[: n / 2]
		R := line[n / 2:]
		for _, c := range L {
			if strings.Contains(R, string(c)) {
				res += calc(c)
				break
			}
		}

		// part 2

		if i > len(a) - 3 || i % 3 != 0 {
			continue
		}
		d := a[i + 1]
		dd := a[i + 2]
		var ok, ok2 bool
		for _, c := range line {
			ok = strings.Contains(d, string(c))
			ok2 = strings.Contains(dd, string(c))
			if ok && ok2 {
				res2 += calc(c)
				break
			}
		}
	}
	return res, res2
}

func calc(c rune) int {
	cc := int(c)
	if 'a' <= c && c <= 'z' {
		return cc - int('a') + 1
	}
	return cc - int('A') + 27
}

func main() {
	var r1, r2 int

	r1, r2 = solve("_inputs/2203.0")
	fmt.Println("data")
	fmt.Println("Star 1:", r1)
	fmt.Println("Star 2:", r2, "\n")

	r1, r2 = solve("_inputs/2203.1")
	fmt.Println("test")
	fmt.Println("Star 1:", r1)
	fmt.Println("Star 2:", r2)
}
