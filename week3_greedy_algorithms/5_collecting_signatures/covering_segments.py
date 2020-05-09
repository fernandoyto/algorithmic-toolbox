# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort(key=lambda x: x.end, reverse=True) # descending order by rightmost item

    while segments:
        reference_point = segments.pop().end

        while segments and segments[-1].start <= reference_point:
            segments.pop()

        if reference_point not in points:
            points.append(reference_point)
    

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
