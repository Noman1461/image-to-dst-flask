from pyembroidery import EmbPattern, STITCH, JUMP

def write_dst(stitches, output_path):
    pattern = EmbPattern()

    last_x, last_y = 0, 0

    for x, y, cmd in stitches:
        dx = x - last_x
        dy = y - last_y

        if cmd == "JUMP":
            pattern.add_stitch_relative(JUMP, dx, dy)
        else:
            pattern.add_stitch_relative(STITCH, dx, dy)

        last_x, last_y = x, y

    pattern.end()
    pattern.write(output_path)
