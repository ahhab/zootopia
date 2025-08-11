{ pkgs, ... }: {
  channel = "unstable";
  packages = [
    pkgs.python3
  ];
  idx = {
    extensions = [
    "ms-python.python"
    "ms-python.debugpy"
  ];
      workspace = {
      # Runs when a workspace is first created with this `dev.nix` file
      onCreate = {
        install =
          "python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
        # Open editors for the following files by default, if they exist:
        default.openFiles = [ "README.md" "src/index.html" "main.py" ];
      }; # To run something each time the workspace is (re)started, use the `onStart` hook
    };
  };
}
