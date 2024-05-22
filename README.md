# Language API

![Flask](https://img.shields.io/badge/Flask-2.1.2-blue)
![Python](https://img.shields.io/badge/Python-3.8-green)

A simple RESTful API built with Flask that provides language data based on language codes.

## Features

- Retrieves language data by language code.
- RESTful API design.
- Easy deployment to Heroku or other platforms.

## Installation

1. Clone the repository:

   ```bash
   git https://github.com/KunalG932/LAnguageCodesAPI
   cd LAnguageCodesAPI
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask app locally:

   ```bash
   python3 bot.py
   ```

2. Access the API endpoints:

   - **Retrieve language data by code:**
     ```
     GET /languages/<lang_code>
     ```

---

## API Endpoints

- **GET /languages/<lang_code>**: Retrieve language data by language code.

---

## Deploying to Heroku

1. Ensure you have the Heroku CLI installed and are logged in.
2. Create a Heroku app:

   ```bash
   heroku create
   ```

3. Push your code to Heroku:

   ```bash
   git push heroku main
   ```

4. Open your app:

   ```bash
   heroku open
   ```

---

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug fixes, feel free to open an issue or a pull request.

---

## License

This project is licensed under the [GNU GENERAL PUBLIC LICENSE](https://github.com/KunalG932/LAnguageCodesAPI/blob/main/LICENSE). Feel free to use and modify this code for your own purposes.
