def calculate_needed_package(l, w, h):
    area1 = l * w
    area2 = w * h
    area3 = h * l
    package_paper = (2 * area1) + (2 * area2) + (2 * area3)
    extra_paper = min(area1, area2, area3)
    return package_paper + extra_paper


def calculate_needed_ribbon(l, w, h):
    t1, t2, _ = sorted([l, w, h])
    side1 = 2 * t1
    side2 = 2 * t2
    present_wrap = side1 + side2
    bow = l * w * h
    return present_wrap + bow

if __name__ == '__main__':
    with open('input/02') as package_sizes:
        needed_square_feets = 0
        needed_ribbon = 0
        for package_size in package_sizes:
            l, w, h = package_size.split('x')
            l, w, h = int(l), int(w), int(h)
            needed_square_feets += calculate_needed_package(l, w, h)
            needed_ribbon += calculate_needed_ribbon(l, w, h)
    print('Paper:', needed_square_feets)
    print('Ribbon:', needed_ribbon)
