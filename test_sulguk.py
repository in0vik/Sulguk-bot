import sys
import os

# Add sulguk to the path
sys.path.append('./sulguk')

# Import sulguk module
from sulguk import transform_html

def test_sulguk():
    """Test that Sulguk HTML transformation works correctly."""
    html = """<h1>Test Heading</h1>
    <p>This is a <b>test</b> paragraph with <i>italic</i> text.</p>
    <blockquote>This is a quote</blockquote>"""
    
    result = transform_html(html)
    
    print("Text output:")
    print(result.text)
    print("\nEntities:")
    for entity in result.entities:
        print(f"Type: {entity['type']}, Offset: {entity['offset']}, Length: {entity['length']}")
    
    return result

if __name__ == "__main__":
    test_sulguk() 