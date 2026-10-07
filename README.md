# Cyberbullying Detection and Remediation

A simple rule-based Python prototype for detecting potentially harmful cyberbullying content and applying basic remediation actions.

## Features

- Accepts user messages through a command-line interface
- Detects potentially harmful words and phrases
- Classifies messages as Safe or Potentially Harmful
- Handles empty input
- Applies simulated content removal for harmful messages
- Provides an interactive menu
- Supports repeated message checking

## Technologies Used

- Python
- Functions
- Lists
- Loops
- Conditional Statements
- String Handling
- Input Validation

## How It Works

The system follows a simple process:

1. User enters a message.
2. The system checks the message against a predefined list of potentially harmful words and phrases.
3. The message is classified as either Safe or Potentially Harmful.
4. If harmful content is detected, the system applies a simulated remediation action.
5. The harmful message is replaced with a removal message.

## Example

```text
Cyberbullying Detection System
1. Check Message
2. Exit

Enter your choice: 1
Enter a message: You are stupid

Result: Potentially Harmful
Action: Harmful content detected.
Action: Content removed.
Remediated Message: [Content removed due to harmful language]
