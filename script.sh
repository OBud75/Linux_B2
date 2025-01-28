#!/usr/bin/zsh

echo $0

my_f() {
	echo "Inside my_f"
	echo $1
	echo $2
	echo $3
	local toto="1"
	echo "inside func $toto"
}

my_f linux mac windows
echo "outside $toto"
