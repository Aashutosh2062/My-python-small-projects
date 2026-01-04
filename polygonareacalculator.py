def shoelace_area(points):
    """Calculate area using Shoelace (surveyor's) formula"""
    n = len(points)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0


print("Polygon Area Calculator (Shoelace Formula)")
print("------------------------------------------")
print("Enter the coordinates one by one (x y)")
print("Press Enter twice (empty line) when you're finished\n")

points = []

while True:
    line = input("Enter x y (or just Enter to finish): ").strip()
    
    if not line:  
        break
        
    try:
        x, y = map(float, line.split())
        points.append((x, y))
        print(f"  → Added point: ({x}, {y})")
    except:
        print("Invalid input! Use format: x y  (example: 3.5 7)")
        continue


if not points:
    print("\nNo points entered. Goodbye.")
else:
    print("\nYour points (in order):")
    for i, (x, y) in enumerate(points, 1):
        print(f"  {i}.  ({x}, {y})")
    
    area = shoelace_area(points)
    print("\n" + "="*40)
    print(f"AREA = {area:.4f} square units")
    print("="*40)

    if len(points) < 3:
        print("→ Note: Need at least 3 points for a polygon!")
    else:
        print("→ Points are processed in the order you entered them")
        print("  (works clockwise OR counterclockwise)")