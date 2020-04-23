relearning system: python scripts/retrain.py --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --image_dir=tf_files/leaf_photos

detect image: python scripts/label_image.py --image img.jpg
detect image: python {PATH}scripts/label_image.py --image {PATH}img.jpg
