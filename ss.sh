for i in *.flac; do
    filename="${i%.flac}"
    ffmpeg -i "$i" "${filename}.mp3"
done
rm *.flac
