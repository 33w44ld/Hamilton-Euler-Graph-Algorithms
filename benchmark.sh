#!/bin/bash

green=$(tput setaf 2)
teal=$(tput setaf 6)
normal=$(tput sgr0)

mkdir -p results

echo "n,time_seconds" > results/hamilton_30_euler.csv
echo "n,time_seconds" > results/hamilton_30_hamilton.csv
echo "n,time_seconds" > results/non_hamilton_50_hamilton.csv

echo "${green}Rozpoczynam benchmarki...${normal}"

echo "${teal}--- Testy: Grafy Hamiltonowskie (30%) ---${normal}"
for n in 11 12 13 14 15 16; do
    
    # ------------------------------ Algorytm Eulera ----------------------------- #
    echo "Testuję n=$n | Algorytm: Euler"
    /usr/bin/time -f "%e" -o tmp_time.txt ./program --hamilton < <(echo -e "$n\n30\neuler\nexit") > /dev/null
    time=$(cat tmp_time.txt)
    echo "$n,$time" >> results/hamilton_30_euler.csv

    # ---------------------------- Algorytm Hamiltona ---------------------------- #
    echo "Testuję n=$n | Algorytm: Hamilton"
    /usr/bin/time -f "%e" -o tmp_time.txt ./program --hamilton < <(echo -e "$n\n30\nhamilton\nexit") > /dev/null
    time=$(cat tmp_time.txt)
    echo "$n,$time" >> results/hamilton_30_hamilton.csv

done

echo "${teal}--- Testy: Grafy nie-Hamiltonowskie (50%) ---${normal}"
for n in 20 22 24 26 28 30; do
    
    echo "Testuję n=$n | Algorytm: Hamilton"
    /usr/bin/time -f "%e" -o tmp_time.txt ./program --non-hamilton < <(echo -e "$n\nhamilton\nexit") > /dev/null
    time=$(cat tmp_time.txt)
    echo "$n,$time" >> results/non_hamilton_50_hamilton.csv

done

rm tmp_time.txt
echo "${green}Zakończono! Wyniki zostały zapisane w formacie CSV w folderze results/.${normal}"