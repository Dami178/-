h, t, v, x = [int(a) for a in input().split()]
vmin = h / t

if vmin >= x:
    tmin = (t * x - h) / (v - x)
else:
    tmin = 0

if vmin > x:
    tmax = t
else:
    tmax = h / x

print(abs(tmin), tmax)
