if __name__ == '__main__':
    print("get funkytowned https://youtu.be/Z6dqIYKIBSU")
else:
    print("toolgcode module initializing")
    def toolPathGcode(paths):
        gcode = []
        gline = ""
        extruder = 0
        for x in paths:
            gline = ""
            if x[1] == 0:
                gline = gline + "g0"
            else:
                gline = gline + "g1"
                extruder += x[1]
            gline = gline + " x" + str(x[0][0]) + " y" + str(x[0][1]) + " z" + str(x[0][1]) + " e" + str(extruder)
            gcode.append(gline)
        return gcode