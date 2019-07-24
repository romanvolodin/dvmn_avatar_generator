from PIL import Image


def channels_shift(image, shift=25):
    width, height = image.size
    r, g, b = image.split()
    r_crop = r.crop((shift, 0, width+shift, height))
    b_crop = b.crop((-shift, 0, width-shift, height))
    return Image.merge('RGB', (r_crop, g, b_crop))


def crop_horizontal(image, crop_width=25):
    width, height = image.size
    return image.crop((crop_width, 0, width-crop_width, height))


def avatar_generator(img, output_size=(80, 80)):
    image = Image.open(img)
    width, height = image.size
    if image.mode != 'RGB':
        image = image.convert('RGB')
    compose = channels_shift(image)
    cropped = crop_horizontal(compose)
    cropped.thumbnail(output_size, resample=Image.LANCZOS)
    return cropped


if __name__ == "__main__":
    avatar = avatar_generator('input.jpg', (250, 250))
    avatar.save('avatar.png')