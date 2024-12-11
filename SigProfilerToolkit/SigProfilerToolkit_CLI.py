import sys
import json
from subprocess import call
import pkg_resources


def load_citations():
    """Load citations from the bundled citations.json file."""
    try:
        data_path = pkg_resources.resource_filename(
            "SigProfilerToolkit", "data/citations.json"
        )
        with open(data_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Citations file not found!")
        return {}
    except Exception as e:
        print(f"An error occurred while loading citations: {e}")
        return {}


def display_citations(tool=None):
    """Display citations for specific tools."""
    citations = load_citations()

    # Map user-friendly tool names to citation keys
    tool_mapping = {
        "matrix_generator": "SigProfilerMatrixGenerator",
        "plotting": "SigProfilerPlotting",
        "assignment": "SigProfilerAssignment",
        "extractor": "SigProfilerExtractor",
    }

    if tool:
        tool = tool.lower()  # Make the tool argument case-insensitive
        mapped_tool = tool_mapping.get(tool)
        if not mapped_tool:
            print(
                "Unknown option! Use one of: plotting, matrix_generator, assignment, extractor."
            )
            return

        print(f"Citations for {tool}:\n")
        tool_citations = citations.get(mapped_tool)
        if tool_citations:
            for category, details in tool_citations.items():
                print(f"{category}:\n{details['citation']}\n{details['url']}\n")
        else:
            print(f"No citations available for {tool}.\n")
    else:
        print("Citations for all tools:\n")
        for key, value in citations.items():
            print(f"{key}:\n")
            for category, details in value.items():
                print(f"{category}:\n{details['citation']}\n{details['url']}\n")


def main():
    commands = {
        "matrix_generator": "Run SigProfilerMatrixGenerator CLI.",
        "plotting": "Run SigProfilerPlotting CLI.",
        "assignment": "Run SigProfilerAssignment CLI.",
        "extractor": "Run SigProfilerExtractor CLI.",
        "citations": "Display citations for the toolkit.",
    }

    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print("Usage: SigProfilerToolkit <tool> <subcommand> [<args>]")
        print("\nTools:")
        for cmd, desc in commands.items():
            print(f"  {cmd}: {desc}")
        sys.exit(1)

    tool = sys.argv[1]
    args = sys.argv[2:]

    if tool == "citations":
        # Show help if -h or --help is passed
        if len(args) == 1 and args[0] in ("-h", "--help"):
            print("Usage: SigProfilerToolkit citations [options]\n")
            print("Options:")
            print("  plotting            Display citations for plotting.")
            print("  matrix_generator    Display citations for matrix generator.")
            print("  assignment          Display citations for assignment.")
            print("  extractor           Display citations for extractor.")
            print(
                "\nIf no option is provided, citations for all tools will be displayed."
            )
            sys.exit(0)

        # If a specific tool is passed, display its citations
        if len(args) == 1:
            display_citations(tool=args[0])
        else:
            # No arguments; show all citations
            display_citations()

    elif tool == "matrix_generator":
        if len(args) < 1:
            print("Usage: SigProfilerToolkit matrix_generator <subcommand> [<args>]")
            print(
                "Subcommands: install, matrix_generator, sv_matrix_generator, cnv_matrix_generator"
            )
            sys.exit(1)
        subcommand = args[0]
        call(["SigProfilerMatrixGenerator", subcommand] + args[1:])

    elif tool == "plotting":
        if len(args) < 1:
            print("Usage: SigProfilerToolkit plotting <subcommand> [<args>]")
            print("Subcommands: plotSBS, plotID, plotDBS, plotSV, plotCNV")
            sys.exit(1)
        subcommand = args[0]
        call(["SigProfilerPlotting", subcommand] + args[1:])

    elif tool == "assignment":
        if len(args) < 1:
            print("Usage: SigProfilerToolkit assignment <subcommand> [<args>]")
            print("Subcommands: decompose_fit, denovo_fit, cosmic_fit")
            sys.exit(1)
        subcommand = args[0]
        call(["SigProfilerAssignment", subcommand] + args[1:])

    elif tool == "extractor":
        if len(args) < 1:
            print("Usage: SigProfilerToolkit extractor <subcommand> [<args>]")
            print("Subcommands: sigprofilerextractor")
            sys.exit(1)
        subcommand = args[0]
        call(["SigProfilerExtractor", subcommand] + args[1:])

    else:
        print(f"Unknown tool: {tool}")
        sys.exit(1)


if __name__ == "__main__":
    main()
