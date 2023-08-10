#!/bin/bash

echo -n Username: 
read  username
# Read Password
echo -n Password: 
read -s password

echo "Hello, please introduce yourself."

echo "Are you human?"

echo -n "y/n: "
read -t 5 -r human

echo "What is your favorite programming language?"
echo -n "Your answer: "
read -t 5 -r lang

echo "Do you like my code?"
echo -n "y/n: "
read -t 5 -r  mycode

score=0

if [[ $human == "y" ]]
then
  score=$((score + 1))
fi 

if [[ $lang == "C" ]]
then
  score=$((score + 1))
fi 


if [[ $mycode == "y" ]]
then
  score=$((score + 1))
fi 

echo

echo "Your answers:"
echo "1. $human"
echo "2. $lang"
echo "3. $mycode"

echo "Your score = $score"
