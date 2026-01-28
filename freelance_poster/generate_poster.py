import base64
import os
from html2image import Html2Image

def generate_poster():
    hti = Html2Image()
    
    # Define absolute paths
    poster_dir = r'c:\Users\Sri Mathi\OneDrive\Desktop\EquitecMachineTest\freelance_poster'
    html_file = os.path.join(poster_dir, 'index.html')
    css_file = os.path.join(poster_dir, 'style.css')
    profile_file = os.path.join(poster_dir, 'profile.png')
    output_png = 'sri_mathi_services.png'
    final_output_path = os.path.join(poster_dir, output_png)
    
    print(f"Reading files from: {poster_dir}")
    
    # Read HTML and CSS
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    with open(css_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Base64 encode the profile image
    if os.path.exists(profile_file):
        print("Encoding profile image...")
        with open(profile_file, 'rb') as f:
            profile_data = base64.b64encode(f.read()).decode('utf-8')
            profile_base64 = f"data:image/png;base64,{profile_data}"
        html_content = html_content.replace('src="profile.png"', f'src="{profile_base64}"')
    else:
        print(f"Warning: Profile image not found at {profile_file}")
    
    # Base64 encode the QR code
    qr_file = os.path.join(poster_dir, 'qrcode.png')
    if os.path.exists(qr_file):
        print("Encoding QR code...")
        with open(qr_file, 'rb') as f:
            qr_data = base64.b64encode(f.read()).decode('utf-8')
            qr_base64 = f"data:image/png;base64,{qr_data}"
        html_content = html_content.replace('src="qrcode.png"', f'src="{qr_base64}"')
    else:
        print(f"Warning: QR code not found at {qr_file}")
    
    print("Generating freelance services poster...")
    try:
        # We use a larger size to ensure high quality rendering
        hti.screenshot(
            html_str=html_content,
            css_str=css_content,
            save_as=output_png,
            size=(1080, 1527)
        )
        
        # Move output to the correct directory if it was saved in the CWD
        if os.path.exists(output_png):
            if os.path.abspath(output_png) != os.path.abspath(final_output_path):
                if os.path.exists(final_output_path):
                    os.remove(final_output_path)
                os.rename(output_png, final_output_path)
            print(f"Success! Poster saved as: {final_output_path}")
        else:
            # Check if it was saved directly in poster_dir by html2image
            if os.path.exists(os.path.join(os.getcwd(), output_png)):
                print("Found file in current working directory.")
            else:
                print("Failed: Image file was not created.")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    generate_poster()
