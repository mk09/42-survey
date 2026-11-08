#!/usr/bin/env python3
"""
JSON Processor for handling JSON data with improved error handling and file processing capabilities.
"""

import json
import os
from typing import Dict, Any, List, Optional


class JSONProcessor:
    """A class to handle JSON data processing with robust error handling."""
    
    def __init__(self):
        self.data = None
    
    def load_json_from_file(self, filepath: str) -> bool:
        """
        Load JSON data from a file.
        
        Args:
            filepath (str): Path to the JSON file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
            return True
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
            return False
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format in '{filepath}': {e}")
            return False
        except PermissionError:
            print(f"Error: Permission denied accessing file '{filepath}'.")
            return False
        except Exception as e:
            print(f"Unexpected error loading JSON from '{filepath}': {e}")
            return False
    
    def load_json_from_string(self, json_string: str) -> bool:
        """
        Load JSON data from a string.
        
        Args:
            json_string (str): JSON formatted string
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.data = json.loads(json_string)
            return True
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format in string: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error loading JSON from string: {e}")
            return False
    
    def process_json_data(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Process the loaded JSON data with improved error handling.
        
        Args:
            data (Dict[str, Any]): The JSON data to process
            
        Returns:
            Optional[Dict[str, Any]]: Processed data or None if failed
        """
        try:
            # Example processing - this could be expanded based on requirements
            processed_data = {}
            
            # Handle different types of data structures
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, (dict, list)):
                        # Recursively process nested structures
                        processed_data[key] = self._process_nested_structure(value)
                    else:
                        processed_data[key] = str(value)  # Convert to string for consistency
            
            elif isinstance(data, list):
                processed_data = [self._process_nested_structure(item) for item in data]
            
            return processed_data
            
        except Exception as e:
            print(f"Error processing JSON data: {e}")
            return None
    
    def _process_nested_structure(self, structure) -> Any:
        """Recursively process nested structures."""
        try:
            if isinstance(structure, dict):
                result = {}
                for key, value in structure.items():
                    if isinstance(value, (dict, list)):
                        result[key] = self._process_nested_structure(value)
                    else:
                        result[key] = str(value)
                return result
            elif isinstance(structure, list):
                return [self._process_nested_structure(item) for item in structure]
            else:
                return str(structure)
        except Exception as e:
            print(f"Error processing nested structure: {e}")
            return structure
    
    def save_json_to_file(self, filepath: str, data: Dict[str, Any]) -> bool:
        """
        Save JSON data to a file with proper error handling.
        
        Args:
            filepath (str): Path to the output file
            data (Dict[str, Any]): Data to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
            
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            return True
            
        except PermissionError:
            print(f"Error: Permission denied writing to '{filepath}'.")
            return False
        except Exception as e:
            print(f"Unexpected error saving JSON to '{filepath}': {e}")
            return False
    
    def validate_json(self, data: Dict[str, Any]) -> bool:
        """
        Validate that the data is valid JSON structure.
        
        Args:
            data (Dict[str, Any]): Data to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            # This will raise an exception if not valid JSON
            json.dumps(data)
            return True
        except Exception as e:
            print(f"Validation error: {e}")
            return False
    
    def get_data(self) -> Optional[Dict[str, Any]]:
        """Get the currently loaded data."""
        return self.data


def main():
    """Main function demonstrating JSON processing capabilities."""
    
    # Create processor instance
    processor = JSONProcessor()
    
    # Example 1: Load from string (this would be your existing functionality)
    sample_json_string = '''
    {
        "name": "John Doe",
        "age": 30,
        "email": "john@example.com",
        "address": {
            "street": "123 Main St",
            "city": "Anytown"
        },
        "hobbies": ["reading", "swimming", "coding"]
    }
    '''
    
    print("Loading JSON from string...")
    if processor.load_json_from_string(sample_json_string):
        print("Successfully loaded JSON from string")
        
        # Process the data
        processed_data = processor.process_json_data(processor.get_data())
        if processed_data:
            print("Processed data:")
            print(json.dumps(processed_data, indent=2))
            
            # Save to file (this would be your new feature)
            output_file = "processed_output.json"
            if processor.save_json_to_file(output_file, processed_data):
                print(f"Successfully saved processed data to {output_file}")
    
    # Example 2: Load from file
    print("\n--- Testing with JSON file ---")
    
    # Create a sample json file for testing
    test_file = "sample.json"
    sample_data = {
        "project": "Folio Survey",
        "version": "1.0",
        "features": ["surveys", "questions", "preview"],
        "metadata": {
            "created": "2023-01-01",
            "author": "Developer"
        }
    }
    
    # Save sample data to file
    with open(test_file, 'w') as f:
        json.dump(sample_data, f)
    
    print(f"Created test file: {test_file}")
    
    # Load from file and process
    if processor.load_json_from_file(test_file):
        loaded_data = processor.get_data()
        print("Loaded data:", json.dumps(loaded_data, indent=2))
        
        processed = processor.process_json_data(loaded_data)
        if processed:
            print("Processed data:")
            print(json.dumps(processed, indent=2))
    
    # Cleanup test file
    try:
        os.remove(test_file)
        print(f"Cleaned up test file: {test_file}")
    except OSError:
        pass


if __name__ == "__main__":
    main()