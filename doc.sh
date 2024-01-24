#!/bin/bash

main() {
    # Check if the number of arguments is exactly one
    if [ $# -eq 1 ]; then
        # Check if the argument is one of the specified values
        case "$1" in
            "install" | "preview" | "make-my-day")
                $1 # Call the function by its name. Function name identical to command
                ;;
            * )
                echo "ERROR Invalid or missing command."
                usage
                exit 1
                ;;
        esac
    else
        usage
        exit 1
    fi
}

function usage(){
    echo "Usage: $0 <command>"
    echo "Known commands are are:"
    echo "    install"
    echo "    make-my-day"
    echo "    preview"
}

function install() {
    pip install -r requirements.txt
    rm -rf .venv
    mkdir .venv
    pipenv install --no-site-packages --dev
}

function preview() {
    pipenv run sphinx-autobuild doc build/html --port 1440 --open-browser
}

function make-my-day() {
    dir_doc_root_path='./doc'

    file_name='index'
    file_extension='rst'

    year=$(date +"%Y")
    week=$(date +"CW%V")
    day=$(date +"%u-%a" | tr 'a-z' 'A-Z')

    dir_entry_relpath=.
    file_entry_relpath_wo_extension=$file_name
    file_entry_relpath=${file_entry_relpath_wo_extension}.$file_extension

    dir_year_relpath=$year
    file_year_relpath_wo_extension=$dir_year_relpath/$file_name
    file_year_relpath=${file_year_relpath_wo_extension}.$file_extension

    dir_week_relpath=$(date +"$year/$week")
    file_week_relpath_wo_extension=$dir_week_relpath/$file_name
    file_week_relpath=${file_week_relpath_wo_extension}.$file_extension

    dir_day_relpath="$dir_week_relpath/$day"
    file_day_relpath_wo_extension=$dir_day_relpath/$file_name
    file_day_relpath=${file_day_relpath_wo_extension}.$file_extension

    date_with_week=$(echo $dir_day_relpath  | tr '/' '/')
    date_with_month=$(date +"%Y-%b-%d")
    weekday_name_full=$(date +"%A")

    cd $dir_doc_root_path

    # Create day if not exist
    create_day () {
        if [ ! -f $file_day_relpath ]; then

            heading="$weekday_name_full, $date_with_month"
            #heading="$(echo $date_with_week | sed -n 's/\///; s/\//./p') : $heading"

            underline=""
            i=0
            while [ $i -lt ${#heading} ]; do
                underline="$underline#"
                i=$((i+1))
            done

            mkdir -p $dir_day_relpath
            echo $heading >> $file_day_relpath
            echo $underline >> $file_day_relpath
            (echo ; echo) >> $file_day_relpath

            echo "info: Create file $file_day_relpath ... done."

            echo "    $day/$file_name" >> $file_week_relpath
        else
            echo "info: File $file_day_relpath already exists. Skip creation."
        fi

        mkdir -p $dir_day_relpath/_figures
        mkdir -p $dir_day_relpath/_attachments
    }
    create_day

    # Create week if not exist, otherwise update
    rewrite_week () {

        heading=$(echo $dir_week_relpath | sed 's/\///g')

        underline=""
        i=0
        while [ $i -lt ${#heading} ]; do
            underline="$underline#"
            i=$((i+1))
        done

        mkdir -p $dir_week_relpath
        echo $heading > $file_week_relpath
        echo $underline >> $file_week_relpath
        (echo) >> $file_week_relpath
        echo ".. toctree::" >> $file_week_relpath
        echo "    :maxdepth: 1" >> $file_week_relpath
        (echo) >> $file_week_relpath

        day_entries=$(cd $dir_week_relpath ; ls -w1 -d * | sed -n '/[1-7]-.../p')
        for day_entry in $day_entries ; do
            echo "    $day_entry/index" >> $file_week_relpath
        done


        echo "info: Rewrite file $file_week_relpath "
    }

    rewrite_week

    rewrite_year () {

        heading="$year"

        underline=""
        i=0
        while [ $i -lt ${#heading} ]; do
            underline="$underline#"
            i=$((i+1))
        done

        mkdir -p $dir_year_relpath
        echo $heading > $file_year_relpath
        echo $underline >> $file_year_relpath
        (echo) >> $file_year_relpath
        echo ".. toctree::" >> $file_year_relpath
        echo "    :maxdepth: 1" >> $file_year_relpath
        (echo) >> $file_year_relpath

        week_entries=$(cd $dir_year_relpath ; ls -w1 -d * | sed -n '/CW[0-9][0-9]/p')
        for week_entry in $week_entries ; do
            echo "    $week_entry/index" >> $file_year_relpath
        done


        echo "info: Rewrite file $file_year_relpath "
    }
    rewrite_year

    rewrite_entry () {

        heading="$(git config --get user.name)'s notebook"

        underline=""
        i=0
        while [ $i -lt ${#heading} ]; do
            underline="$underline#"
            i=$((i+1))
        done

        mkdir -p $dir_entry_relpath
        echo $heading > $file_entry_relpath
        echo $underline >> $file_entry_relpath
        (echo) >> $file_entry_relpath
        echo ".. toctree::" >> $file_entry_relpath
        echo "    :maxdepth: 1" >> $file_entry_relpath
        (echo) >> $file_entry_relpath

        week_entries=$(cd $dir_entry_relpath ; ls -w1 -d * | sed -n '/[0-9][0-9][0-9][0-9]/p')
        for week_entry in $week_entries ; do
            echo "    $week_entry/index" >> $file_entry_relpath
        done


        echo "info: Rewrite file $file_entry_relpath "
    }
    rewrite_entry

    cd ..

    # At codespace skip subsequent actions. Use the username as indicator for that.
    if [ "$USER" = "codespace" ]; then
        exit
    fi

    # On iPad skip subsequent actions. Use the username as indicator for that.
    if [ "$USER" = "mobile" ]; then
        exit
    fi

    # Open VS code
    echo "info: Open vscode and go to file $dir_doc_root_path//$file_day_relpath"
    # echo "TODO: Adapt manually .vscode/settings.json to make esbonio use this week as source folder:  $dir_week_relpath"
    code . --goto $dir_doc_root_path//$file_day_relpath:$(echo $(cat $dir_doc_root_path/$file_day_relpath | wc -l))
}

main "$@"
