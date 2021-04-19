package main

import (
	"exec"
	"fmt"
)

func hello() {
	cmd, err := exec.Command("echo hello")

	if err != nil {
		print(err)
	}

	fmt.Println(cmd)
}
