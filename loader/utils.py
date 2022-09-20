def save_picture(picture):
    filename = picture.filename

    picture.save(f"./uploads/images/{filename}")
    return f"./uploads/images/{filename}"
