show_help() {
    echo "Usage: $0 -e ENVIRONMENT"
    echo "Options:"
    echo "  -e ENVIRONMENT   Specify the environment (e.g., DEV)"
    echo "  -h, --help       Show this help message"
    exit 0
}

while getopts "e:h" option; do
    case $option in
        e)
            environment=$OPTARG
            ;;
        h)
            show_help
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            show_help
            ;;
    esac
done
