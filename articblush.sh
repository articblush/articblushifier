#!/usr/bin/env bash

PICTURES_PATH=$HOME/Pictures/articblush

if ! test -d $PICTURES_PATH; then
  mkdir $PICTURES_PATH
  echo "dir [~/Pictures/articblush] has been created successfully!"
fi

articblushifierpy ${@}
