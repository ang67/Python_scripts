#!/bin/bash

declare -A seen_combinations  # Associative array to track unique combinations of $1 and $2

while IFS=';' read -r col1 col2 col3; do
  # Combine $1 and $2 values to create a unique key
  combination="$col1;$col2"

  # Check if this combination has been seen before
  if [ "${seen_combinations[$combination]}" ]; then
    # If it has been seen, append ";idem" to the end of the line
    echo "$col1;$col2;$col3;idem"
  else
    # If it's a new combination, just output the line as is
    echo "$col1;$col2;$col3"
    seen_combinations["$combination"]=1  # Mark this combination as seen
  fi

done <<EOF
toto; list create update; admin
titi; list create update; dev
toto; list create update; prod
EOF
