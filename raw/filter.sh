Echo "Filters out potential sensitive data before publishing raw data"
cp programes.xml programes_old.xml && cat programes_old.xml | grep -v '_password\|_author_' > programes.xml 
cp articles.xml articles_old.xml && cat articles_old.xml | grep -v '_password\|_author_' > articles.xml 
