import sys
from subprocess import call


def main():
    commands = {
        "matrix_generator": "Run SigProfilerMatrixGenerator CLI.",
        "plotting": "Run SigProfilerPlotting CLI.",
        "assignment": "Run SigProfilerAssignment CLI.",
        "extractor": "Run SigProfilerExtractor CLI.",
    }

    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print("Usage: SigProfilerToolkit <tool> <subcommand> [<args>]")
        print("Tools:")
        for cmd, desc in commands.items():
            print(f"  {cmd}: {desc}")
        sys.exit(1)

    tool = sys.argv[1]
    args = sys.argv[2:]

    if tool == "matrix_generator":
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
