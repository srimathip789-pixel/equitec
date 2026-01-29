import base64
import os
from html2image import Html2Image

def convert_to_image():
    hti = Html2Image()
    
    poster_dir = r'c:\Users\Sri Mathi\OneDrive\Desktop\EquitecMachineTest\poster'
    html_file = os.path.join(poster_dir, 'index.html')
    css_file = os.path.join(poster_dir, 'style.css')
    speaker_file = os.path.join(poster_dir, 'speaker.png')
    logo_file = os.path.join(poster_dir, 'itef_logo_only.png')
    output_png = 'event_poster.png'
    final_output_path = os.path.join(poster_dir, output_png)
    
    # Read HTML and CSS
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    with open(css_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Base64 encode the speaker image
    with open(speaker_file, 'rb') as f:
        speaker_data = base64.b64encode(f.read()).decode('utf-8')
        speaker_base64 = f"data:image/png;base64,{speaker_data}"
    
    # Base64 encode the ITEF logo
    with open(logo_file, 'rb') as f:
        logo_data = base64.b64encode(f.read()).decode('utf-8')
        logo_base64 = f"data:image/png;base64,{logo_data}"
    
    # Replace the image srcs in HTML with the base64 strings
    html_content = html_content.replace('src="speaker.png"', f'src="{speaker_base64}"')
    html_content = html_content.replace('src="itef_logo_only.png"', f'src="{logo_base64}"')
    
    print("Attempting to generate image with Base64 encoded images...")
    try:
        hti.screenshot(
            html_str=html_content,
            css_str=css_content,
            save_as=output_png,
            size=(1080, 1350)
        )
        
        if os.path.exists(output_png):
            if os.path.exists(final_output_path):
                os.remove(final_output_path)
            os.rename(output_png, final_output_path)
            print(f"Success! Poster saved as: {final_output_path}")
        else:
            print("Failed: Image file was not created.")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    convert_to_image()
