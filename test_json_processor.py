#!/usr/bin/env python3
"""
Test script for the JSON Processor.
"""

import json
from json_processor import JSONProcessor


def test_basic_functionality():
    """Test basic JSON processing functionality."""
    
    processor = JSONProcessor()
    
    # Test loading from string
    sample_data = {
        "test": "success",
        "number": 42,
        "active": True,
        "nested": {
            "key": "value"
        }
    }
    
    json_string = json.dumps(sample_data)
    
    print("Testing load from string...")
    if processor.load_json_from_string(json_string):
        print("✓ Successfully loaded JSON from string")
        
        # Test processing
        processed = processor.process_json_data(processor.get_data())
        if processed:
            print("✓ Successfully processed data")
            
            # Test saving to file
            test_file = "test_output.json"
            if processor.save_json_to_file(test_file, processed):
                print(f"✓ Successfully saved to {test_file}")
                
                # Verify the content
                with open(test_file, 'r') as f:
                    content = json.load(f)
                    print("✓ File content verified")
                    
                import os
                os.remove(test_file)
                print("✓ Cleaned up test file")
            else:
                print("✗ Failed to save file")
        else:
            print("✗ Failed to process data")
    else:
        print("✗ Failed to load from string")


def test_error_handling():
    """Test error handling capabilities."""
    
    processor = JSONProcessor()
    
    print("\nTesting error handling...")
    
    # Test invalid JSON
    print("Testing invalid JSON string...")
    if not processor.load_json_from_string("{invalid json}"):
        print("✓ Correctly handled invalid JSON")
    
    # Test non-existent file
    print("Testing non-existent file...")
    if not processor.load_json_from_file("non_existent.json"):
        print("✓ Correctly handled non-existent file")


def test_nested_structures():
    """Test processing of nested structures."""
    
    processor = JSONProcessor()
    
    nested_data = {
        "level1": {
            "level2": {
                "level3": ["item1", "item2"],
                "data": {"nested_key": "nested_value"}
            }
        },
        "simple": "value"
    }
    
    print("\nTesting nested structures...")
    if processor.load_json_from_string(json.dumps(nested_data)):
        processed = processor.process_json_data(processor.get_data())
        if processed:
            print("✓ Successfully processed nested data")
            print(f"Processed structure: {processed}")
        else:
            print("✗ Failed to process nested data")


if __name__ == "__main__":
    test_basic_functionality()
    test_error_handling()
    test_nested_structures()
    
    print("\nAll tests completed!")