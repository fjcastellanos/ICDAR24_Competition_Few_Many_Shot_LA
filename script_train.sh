
DATASET=$1  # Latin2FS, Latin14396FS, Latin16746FS, Syr341FS
MODE="MS"

data_train="dataset/U-DIADS-Bib-${MODE}/${DATASET}/training.txt"
data_val="dataset/U-DIADS-Bib-${MODE}/${DATASET}/validation.txt"
NPATCHES="1024"

for layer_name in "BG" "Para" "Deco" "Text" "Title" "Head"; do
			path_model="models/${DATASET}_${layer_name}.h5"
            output_file="logs/out_${DATASET}_${layer_name}_${options_serial}_npatches${NPATCHES}.txt"
            echo $output_file
			echo $data_train
			python3 -u main.py -m ${path_model} \
                		-db_train_src ${data_train} \
                		-db_val_src ${data_val} \
                		-aug random scale rot flipV flipH \
                		-lay ${layer_name} \
                		-npatches ${NPATCHES} \
                		-n_annotated_patches -1 \
                		-window_w 512 \
                		-window_h 512 \
				        -l 5 \
				        -f 64 \
				        -k 3 \
				        -drop 0.2 \
				        -pages_train -1 \
				        -e 50 \
				        -b 16 \
				        -verbose 1 \
                		-res results/res.txt \
				        -gpu 0 \
				        -no_mask \
				        &> ${output_file}

done
