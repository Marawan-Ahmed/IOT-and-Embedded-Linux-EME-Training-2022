#!/bin/bash

echo "Input first number"
read num1
echo "Input second number"
read num2

echo "Input type of operation: (arith/logic)"
read op

if [[ $op == "arith" ]]
then
echo "Sum = $((num1+num2))"
echo "Sub = $((num1-num2))"
echo "Mul = $((num1*num2))"
echo "Dv = $((num1/num2))"
elif [[ $op == "logic" ]]
then
echo "AND = $((num1&num2))" 
echo "OR = $((num1|num2))"
fi
