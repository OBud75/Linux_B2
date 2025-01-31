export BASE_DIR=$(pwd)

. $BASE_DIR/conf/$env.sh
. $BASE_DIR/venv/bin/activate

export APP_DIR="$BASE_DIR/app"
export TEMPLATE_DIR="$APP_DIR/templates"
export DB_PATH="$BASE_DIR/$DB_NAME"

alias sql3="sqlite3 $DB_NAME"
