import argparse
from PIL import Image


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('input',
                        help='path to input image')
    parser.add_argument('--size',
                        default='80x80',
                        help='output size in pixels')
    parser.add_argument('output',
                        help='path to output image')                  
    return parser.parse_args()


def parse_size(data):
    try:
        width, height = data.strip().replace('x', ' ').split()
        width = int(width)
        height = int(height)
        return width, height
    except ValueError:
        return


def shift_channels(image, shift=25):
    width, height = image.size
    r, g, b = image.split()
    r_crop = r.crop((shift, 0, width+shift, height))
    b_crop = b.crop((-shift, 0, width-shift, height))
    return Image.merge('RGB', (r_crop, g, b_crop))


def crop_horizontal(image, crop_width=25):
    width, height = image.size
    return image.crop((crop_width, 0, width-crop_width, height))


def avatar_generator(image, output_size=(80, 80)):
    width, height = image.size
    if image.mode != 'RGB':
        image = image.convert('RGB')
    shifted_channels_image = shift_channels(image)
    cropped_image = crop_horizontal(shifted_channels_image)
    cropped_image.thumbnail(output_size, resample=Image.LANCZOS)
    return cropped_image


if __name__ == "__main__":
    args = parse_arguments()
    input_path = args.input
    output_path = args.output
    
    output_size = parse_size(args.size)
    if output_size is None:
        exit('Error: Can\'t parse output size:\nIt must be in WIDTHxHEIGHT format, e.g. 128x128')
    
    width, height = output_size

    try:
        image = Image.open(input_path)
    except (FileNotFoundError, PermissionError) as err:
        print('Error: Can\'t read input file:')
        exit(err)
    
    avatar = avatar_generator(image, (width, height))

    try:
        avatar.save(output_path)
    except (FileNotFoundError, PermissionError, ValueError) as err:
        print('Error: Can\'t save output file:')
        exit(err)

