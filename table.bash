i=1
for line in `cat ./data.txt`
do
	echo "$i & $line \\\\"
	(( i = i+1))
done
