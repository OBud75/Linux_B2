. conf/$env.sh
export BASE_FOLDER=$(pwd)
export DB_PATH="$BASE_FOLDER/$DB_NAME"

alias sql3="sqlite3 $DB_NAME"