
# (time offset in seconds, % nominal voltage, % nominal frequency)
vv_voltage_profile = [
    (0, 100, 100),
    (30, 100, 100),
    (30, 106, 100),
    (60, 106, 100),
    (60, 94, 100),
    (90, 94, 100),
    (90, 100, 100),
    (120, 100, 100),
    (135, 106, 100),
    (150, 106, 100),
    (180, 94, 100),
    (195, 94, 100),
    (210, 100, 100),
    (240, 100, 100),
    (245, 106, 100),
    (250, 106, 100),
    (260, 94, 100),
    (265, 94, 100),
    (270, 100, 100),
    (300, 100, 100)
]

vrt_50v_2s = [
    (0, 50, 100),
    (2, 50, 100),
    (2, 100, 100)
]

# (time offset in seconds, % nominal voltage, % nominal frequency)
fw_freq_profile = [
    (0, 100.0, 100.0),
    (30, 100.0, 100.0),
    (30, 100.0, 103.0),
    (60, 100.0, 103.0),
    (60, 100.0, 97.0),
    (90, 100.0, 97.0),
    (90, 100.0, 103.0),
    (95, 100.0, 103.0),
    (95, 100.0, 100.0),
    (125, 100.0, 100.0),
    (155, 100.0, 102.0),
    (185, 100.0, 102.0),
    (215, 100.0, 98.0),
    (245, 100.0, 98.0),
    (260, 100.0, 102.0),
    (275, 100.0, 102.0),
    (280, 100.0, 100.0),
    (295, 100.0, 100.0),
    (310, 100.0, 100.3),
    (325, 100.0, 100.3),
    (340, 100.0, 100.0),
    (360, 100.0, 100.0)
]

profiles = {
    'FW Profile': fw_freq_profile,
    'VV Profile': vv_voltage_profile,
    'VRT Test Profile': vrt_50v_2s
}

if __name__ == "__main__":

    pass