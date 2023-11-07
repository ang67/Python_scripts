```shell
chaine="toto ; list watch get"

chaine_triee=$(echo "$chaine" | awk -F';' '{
  gsub(/^[[:space:]]+|[[:space:]]+$/, "", $2);  # Supprime les espaces autour de la deuxième colonne
  split($2, elements, /[[:space:]]+/);         # Divise la deuxième colonne en éléments
  n = asort(elements);                        # Trie les éléments
  $2 = "";                                    # Efface la deuxième colonne d'origine
  for (i = 1; i <= n; i++) {
    $2 = $2 elements[i] " ";                  # Reconstruit la deuxième colonne triée
  }
  print $0;
}')

echo "$chaine_triee"
```
