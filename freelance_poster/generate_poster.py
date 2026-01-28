import base64
import os
from html2image import Html2Image

def generate_poster():
    hti = Html2Image()
    
    poster_dir = r'c:\Users\Sri Mathi\OneDrive\Desktop\EquitecMachineTest\freelance_poster'
    html_file = os.path.join(poster_dir, 'index.html')
    css_file = os.path.join(poster_dir, 'style.css')
    bg_file = os.path.join(poster_dir, 'background.png')
    profile_file = os.path.join(poster_dir, 'profile.png')
    output_png = 'sri_mathi_services.png'
    final_output_path = os.path.join(poster_dir, output_png)
    
    # Read HTML and CSS
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    with open(css_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Base64 encode the background image
    if os.path.exists(bg_file):
        with open(bg_file, 'rb') as f:
            bg_data = base64.b64encode(f.read()).decode('utf-8')
            bg_base64 = f"data:image/png;base64,{bg_data}"
        html_content = html_content.replace("url('background.png')", f"url('{bg_base64}')")
    
    # Base64 encode the profile image
    if os.path.exists(profile_file):
        with open(profile_file, 'rb') as f:
            profile_data = base64.b64encode(f.read()).decode('utf-8')
            profile_base64 = f"data:image/png;base64,{profile_data}"
        html_content = html_content.replace('src="profile.png"', f'src="{profile_base64}"')
    
    print("Generating freelance services poster...")
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
    generate_poster()
