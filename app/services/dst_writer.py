from pyembroidery import EmbPattern, STITCH, END

def write_dst(stitches, output_path):
    pattern = EmbPattern()

    for stitch in stitches:
        if stitch == ("END",):
            pattern.add_command(END)
        else:
            x, y = stitch
            pattern.add_stitch_absolute(STITCH, x, y)

    pattern.end()
    pattern.write(output_path)
