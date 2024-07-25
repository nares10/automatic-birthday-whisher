# Birthday Email Sender

A simple Python script to send personalized birthday emails to contacts based on information stored in a CSV file. 

## Features

- Reads birthday information from a CSV file.
- Sends a personalized birthday email to each contact whose birthday matches the current date.
- Utilizes SMTP to send emails through Gmail.
- Randomly selects a birthday message from a set of predefined templates.

## Requirements

- Python 3.x
- Required Python packages:
  - `python-dotenv`
  - `smtplib` (included with Python)
  - `csv` (included with Python)

You can install the required packages using pip:

```bash
pip install python-dotenv
```

## Setup

1. **Create a `.env` file** in the root directory of your project with the following content:

    ```
    EMAIL_USER=your_email@gmail.com
    EMAIL_PASSWORD=your_password
    ```

    Replace `your_email@gmail.com` and `your_password` with your Gmail address and password. 

2. **Prepare a `birthdays.csv` file** with the following format:

    ```csv
    name,email,birth_month,birth_day
    John Doe,john@example.com,7,26
    Jane Smith,jane@example.com,7,26
    ```

    Replace the sample data with your actual contacts and their birthdates.

3. **Create birthday message templates** named `letter1.txt`, `letter2.txt`, `letter3.txt`, and `letter4.txt` in the same directory. Each file should contain a message with a placeholder `{name}` which will be replaced with the recipient's name.

4. **Run the script**:

    ```bash
    python3 main.py
    ```

## Error Handling

The script includes basic error handling for:

- Authentication issues with the email server.
- Connection issues with the SMTP server.
- File not found errors for the letter templates.

## Notes

- Ensure that "Less secure app access" is enabled on your Gmail account or use an app password if you have 2-Step Verification enabled.
- For production use, consider using OAuth2 for a more secure authentication method.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

