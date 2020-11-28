#Flipbook
A flip book is a book with a series of pictures that vary gradually
from one page to the next, so that when the pages are turned rapidly,
the pictures appear to animate by simulating motion or some other
change.


#Flipbook compiler
This repo consist of a compiler built on python to interpret "flip" language.
"Flip" language is a language I was supposed to built to do some tasks.


#Flip commands
The repo consists of .flip files which has code written in flip language.
i) human_life_span.flip : this file has an image name and number of pages to display
                          Eg. - 01 05 child.jpg
ii) apple.flip : this file has two image file names 
                 Eg. - apple.png newton.jpg


#Compiler commands
i) fc human_life_span.flip -o human_life_span.pdf : This command will take the flip file as input
                                                     and generate a flipbook in pdf format
                                                     
  <iframe width="1280" height="720" src="https://www.youtube.com/embed/t9Bugnhb3ac" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

ii) fc human_life_span.flip -o human_life_span.pdf : This command will take the flip file as input
                                                     and generate a flipbook in gif format

iii) fc apple.flip -o applenewton.pdf : This command will take the apple.flip file as input
                                         and generate a flipbook in pdf format for apple falling on
                                         newton.
  <iframe width="1280" height="722" src="https://www.youtube.com/embed/tpURgTbVOqc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

