from PIL import Image, ImageDraw, ImageFont, ImageColor
import os
import math

# Output directory
output_dir = r"c:\Users\Casper\OneDrive\Desktop\hafizaoyunu\hafizaoyunu\app\src\main\res\drawable"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Artifact Paths (Generated AI Images)
ANIMALS_SHEET_PATH = r"C:/Users/Casper/.gemini/antigravity/brain/1d67118e-926d-42db-979d-7444a88b6224/animals_sheet_1768737673198.png"
COUNTRIES_SHEET_PATH = r"C:/Users/Casper/.gemini/antigravity/brain/1d67118e-926d-42db-979d-7444a88b6224/countries_sheet_v2_1768740398396.png"

def slice_and_save(source_path, prefix, count=36, cols=6, rows=6):
    if not os.path.exists(source_path):
        print(f"Error: Source image not found at {source_path}")
        return

    try:
        img = Image.open(source_path)
        width, height = img.size
        cell_w = width // cols
        cell_h = height // rows
        
        saved_count = 0
        for r in range(rows):
            for c in range(cols):
                if saved_count >= count:
                    break
                
                left = c * cell_w
                top = r * cell_h
                right = left + cell_w
                bottom = top + cell_h
                
                # Crop and Resize
                cropped = img.crop((left, top, right, bottom))
                resized = cropped.resize((250, 250), Image.Resampling.LANCZOS)
                
                # Save
                filename = f"{prefix}{saved_count + 1}.png"
                save_path = os.path.join(output_dir, filename)
                resized.save(save_path)
                print(f"Generated {filename}")
                saved_count += 1
    except Exception as e:
        print(f"Failed to process {source_path}: {e}")

def generate_shape_card(index, filename):
    img = Image.new('RGB', (250, 250), color=(255, 250, 250)) # Snow
    draw = ImageDraw.Draw(img)
    
    color = ImageColor.getrgb(f"hsl({(index * 40) % 360}, 80%, 50%)")
    
    shape_type = index % 8
    margin = 40
    
    if shape_type == 0: # Triangle
        points = [(125, margin), (margin, 250-margin), (250-margin, 250-margin)]
        draw.polygon(points, fill=color)
    elif shape_type == 1: # Square
        draw.rectangle([60, 60, 190, 190], fill=color)
    elif shape_type == 2: # Circle
        draw.ellipse([50, 50, 200, 200], fill=color)
    elif shape_type == 3: # Diamond
        points = [(125, 40), (210, 125), (125, 210), (40, 125)]
        draw.polygon(points, fill=color)
    elif shape_type == 4: # Pentagon
        points = []
        for i in range(5):
            angle = (math.pi * 2 * i) / 5 - (math.pi / 2)
            x = 125 + 85 * math.cos(angle)
            y = 125 + 85 * math.sin(angle)
            points.append((x, y))
        draw.polygon(points, fill=color)
    elif shape_type == 5: # Hexagon
        points = []
        for i in range(6):
            angle = (math.pi * 2 * i) / 6
            x = 125 + 85 * math.cos(angle)
            y = 125 + 85 * math.sin(angle)
            points.append((x, y))
        draw.polygon(points, fill=color)
    elif shape_type == 6: # Star (Simple)
        points = []
        for i in range(10):
            angle = (math.pi * 2 * i) / 10 - (math.pi / 2)
            r = 90 if i % 2 == 0 else 40
            x = 125 + r * math.cos(angle)
            y = 125 + r * math.sin(angle)
            points.append((x, y))
        draw.polygon(points, fill=color)
    else: # Cross
        draw.rectangle([100, 30, 150, 220], fill=color)
        draw.rectangle([30, 100, 220, 150], fill=color)
        
    img.save(os.path.join(output_dir, filename))
    print(f"Generated Shape: {filename}")

def generate_assets():
    print("Generating Animals from Sprite Sheet...")
    # Animals use default 6x6 grid
    slice_and_save(ANIMALS_SHEET_PATH, "hayvan", 36, cols=6, rows=6)
    
    print("Generating Countries from Sprite Sheet...")
    # Countries sheet appears to be denser (12x12), so we adjust the grid
    slice_and_save(COUNTRIES_SHEET_PATH, "ulke", 36, cols=6, rows=6)
    
    print("Generating Shapes programmatically...")
    for i in range(1, 40): 
        generate_shape_card(i-1, f"kart{i}.png")

if __name__ == "__main__":
    generate_assets()
    
    print("Generating Shapes programmatically...")
    for i in range(1, 40): 
        generate_shape_card(i-1, f"kart{i}.png")

if __name__ == "__main__":
    generate_assets()
