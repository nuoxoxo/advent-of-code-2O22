package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"io/ioutil"
	_ "strconv"
)

var path string = "data"
// var path string = "test"

func main() {

	// way 1

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

	// way 2

	data2, err := ioutil.ReadFile(path)
	if err != nil {
		panic(err)
	}
	var b []string
	lines := string(data2)
	for _, line := range strings.Split(lines, "\n") {
		b = append(a, line)
	}

	// printing both ways

	fmt.Println("Way 1:")
	for _, s := range a {
		fmt.Println(s)
	}

	fmt.Println("\nWay 1:")
	for _, s := range b {
		fmt.Println(s)
	}
}
