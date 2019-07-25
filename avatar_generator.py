from PIL import Image


def shift_channels(image, shift=25):
    width, height = image.size
    r, g, b = image.split()
    r_crop = r.crop((shift, 0, width+shift, height))
    b_crop = b.crop((-shift, 0, width-shift, height))
    return Image.merge('RGB', (r_crop, g, b_crop))


def crop_horizontal(image, crop_width=25):
    width, height = image.size
    return image.crop((crop_width, 0, width-crop_width, height))


def avatar_generator(input_image, output_size=(80, 80)):
    image = Image.open(input_image)
    width, height = image.size
    if image.mode != 'RGB':
        image = image.convert('RGB')
    shifted_channels_image = shift_channels(image)
    cropped_image = crop_horizontal(shifted_channels_image)
    cropped_image.thumbnail(output_size, resample=Image.LANCZOS)
    return cropped_image


if __name__ == "__main__":
    avatar = avatar_generator('input.jpg', (250, 250))
    avatar.save('avatar.png')
