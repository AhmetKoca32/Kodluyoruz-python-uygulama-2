import math

#1. Noktaların Tanımlanması
points = [(1,2),(4,6),(7,8),(2,1),(9,5)]

#2. Öklid Mesafesi Fonksiyonu
def euclideanDistance(point1,point2):
    return math.sqrt((point1[0]-point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

#3. Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i+1,len(points)):
        distance = euclideanDistance(points[i],points[j])
        distances.append(distance)

#4. Minimum mesafeyi bulma
min_distance = min(distances)  

#5. Sonuc
print("Noktalar arasındaki minimum mesafe:",min_distance)
