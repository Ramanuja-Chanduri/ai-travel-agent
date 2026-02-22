import sys
import os


class CustomException(Exception):
    def __init__(self, message, error_detail: sys):
        super().__init__(message)
        self.error_message = CustomException.get_detailed_error_message(message, error_detail)

    @staticmethod
    def get_detailed_error_message(message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = os.path.basename(exc_tb.tb_frame.f_code.co_filename) if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        detailed_message = f"Error occurred in file: {file_name} at line: {line_number} with message: {message}"
        return detailed_message

    def __str__(self):
        return self.error_message