#!/bin/bash

# Set the source and destination directories
src_dir=/home/pierringshot/Documents/batchRemoveBG-BEST_SCRIPTS/imgRemBG/images
dst_dir=/home/pierringshot/Documents/batchRemoveBG-BEST_SCRIPTS/imgRemBG/images/thumb

# Loop through all files in the source directory
for file in "$src_dir"/*; do
  # Check if the file is an image
  if [ "${file##*.}" == "jpg" ] || [ "${file##*.}" == "jpeg" ] || [ "${file##*.}" == "png" ]; then
    # Get the image dimensions
    width=$(identify -format "%w" "$file")
    height=$(identify -format "%h" "$file")

    # Check if the image is smaller than 100x100 px
    if [ $width -le 100 ] && [ $height -le 100 ]; then
      # Move the image to the thumb directory
      echo "Moved! - $file"
      mv -v -f "$file" "$dst_dir"
    fi
  fi
done
