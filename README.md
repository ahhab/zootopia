# Animals Web Generator

This project generates a simple HTML website displaying information about animals.

## Functionality

The script `animals_web_generator.py` prompts the user to enter an animal name. It then fetches data for that animal from the [API Ninjas Animals API](https://api-ninjas.com/api/animals) and dynamically generates an HTML file (`animals_web_output.html`) to display the retrieved animal information.

## Environment Configuration

This project uses a `.idx/dev.nix` file to define and manage the development environment. This file ensures a consistent and reproducible setup by specifying necessary packages, like `python3`. When the workspace is loaded, the Nix package manager automatically installs these dependencies, creating the correct environment to run the project without manual setup.

### Manual Setup
If the environment is not dev.nix powered, setup python and run `pip install -r requirements.txt`

## API Key

To interact with the Animals API, you need an API key from [API Ninjas](https://api-ninjas.com/api/animals).

The application is designed to read the API key from a `.env` file.

1.  Create a file named `.env` in the root directory of the project.
2.  Add your API key to this file in the following format:

    ```
    API_NINJAS_API_KEY="YOUR_ACTUAL_API_KEY"
    ```

The `.env` file should **not** be committed to version control for security reasons. The script uses the `python-dotenv` library to load your key safely into the environment.

## Usage

1.  Make sure your `.env` file is created and contains your API key.
2.  Run the script from your terminal:

    ```bash
    python3 animals_web_generator.py
    ```

3.  Enter an animal name when prompted.
4.  Open the generated `animals_web_output.html` file in a web browser to see the results.
