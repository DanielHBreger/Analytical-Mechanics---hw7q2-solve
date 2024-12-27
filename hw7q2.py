
class mass():
    
    def __init__(self, m, pos):
        self.mass = m
        self.pos = pos
        self.origin = [0, 0, 0]
    
    def rebase(self, center_of_mass):
        for i in range(len(self.origin)):
            self.pos[i] += self.origin[i]
        for i in range(len(center_of_mass)):
            self.pos[i] -= center_of_mass[i]
        self.origin = center_of_mass
    
    def inertia_moment_axis(self, i, j):
        elem = 0
        x, y, z = self.pos
        if i == j:
            elem = x**2 + y**2 + z**2
        return self.mass * (elem - self.pos[i] * self.pos[j])

def get_center_of_mass(masses):
    total_mass = sum([m.mass for m in masses])
    center_of_mass = (0, 0, 0)
    for m in masses:
        x, y, z = m.pos
        center_of_mass = (center_of_mass[0] + m.mass * x / total_mass, 
                          center_of_mass[1] + m.mass * y / total_mass, 
                          center_of_mass[2] + m.mass * z / total_mass)
    return center_of_mass

def get_inertia_tensor(masses):
    return [[sum([m.inertia_moment_axis(i,j) for m in masses]) for j in range(3)] for i in range(3)]

def main():
    masses = [
        mass(1, [0, 0, 0]),
        mass(3, [0, 0, 1]),
        mass(2, [0, 1, 1]),
        mass(2, [1, 0, 0]),
        mass(3, [1, 1, 0]),
    ]
    com = get_center_of_mass(masses)
    print(com)
    
    # inertia tensor around center of mass
    for m in masses:
        m.rebase(com)
    inertia_tensor = get_inertia_tensor(masses)
    [print(*item) for item in zip(*inertia_tensor)]
    
    print("\n")
    
    # inertia tensor around (0,0,0)
    for m in masses:
        m.rebase([0,0,0])
    inertia_tensor = get_inertia_tensor(masses)
    [print(*item) for item in zip(*inertia_tensor)]
    
    print("\n")
    
    # inertia tensor around (1,1,1)
    for m in masses:
        m.rebase([1,1,1])
    inertia_tensor = get_inertia_tensor(masses)
    [print(*item) for item in zip(*inertia_tensor)]
    
    print("\n")
    
    # inertia tensor around (-1/2,3/2,5/2)
    for m in masses:
        m.rebase([-0.5,1.5,2.5])
    inertia_tensor = get_inertia_tensor(masses)
    [print(*item) for item in zip(*inertia_tensor)]

if __name__ == '__main__':
    main()