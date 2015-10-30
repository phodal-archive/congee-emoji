find ./imgs -regex '.*\(\|png\)' -exec convert -background white -flatten {} {}.gif \;
