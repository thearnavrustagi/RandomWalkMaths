for i in {2..100}
do
	echo `python3 ./random_walk.py steps $i` >> ./random_steps.txt
done

for i in {1..99}
do
	echo `python3 ./random_walk.py posn $i` >> ./random_posn.txt
done
