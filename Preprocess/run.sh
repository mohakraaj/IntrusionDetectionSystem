echo "Reading File.."
python info.py $1 

echo "Converting data format.."
echo "Scaling.."
file="Reduced_"$1
echo "Writing "$file".." 
model_file=$file".model"

svm-train -s 0 -c 5 -t 2 -g 0.5 -e 0.1 $file >>logfile
echo "Training Data.."
echo "Predicting.."

echo "Result is :"
echo "-----------------------------------------"

svm-predict $file $model_file result.data 
