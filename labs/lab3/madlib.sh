#!/bin/bash

clear
echo "Let's build a mad-lib!"

read -p "1. Please give me an adjective: " ADJ1

read -p "2. Please give me a noun: " NOUN1

read -p "3. Please give me an adjective: " ADJ2

read -p "4. Please give me a verb: " VERB1

read -p "5. Please give me an adjective: " ADJ3

read -p "6. Please give me an adverb: " ADV1

read -p "7. Please give me a noun: " NOUN2

read -p "8. Please give me a verb: " VERB2

read -p "9. Please give me a verb: " VERB3

read -p "10. Please give me an adverb: " ADV2

echo "Once upon a time there was a $ADJ2 $NOUN1 named $ADJ1."
echo " "
echo "$ADJ1 loved to $VERB1 $ADV1 until one day, there was another $NOUN1 named $ADJ3."
echo " "
echo "$ADJ3 was a mean $NOUN1, who made fun of the way that $ADJ1 would $VERB1."
echo " "
echo "$ADJ3 preffered to $VERB2, and $NOUN2 did so very $ADV2."
echo " "
echo "Fortunately, one day $NOUN1 and $NOUN2 figured out they both liked to $VERB3, and they lived happily ever after."
echo " "

