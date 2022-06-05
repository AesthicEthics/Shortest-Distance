# Shortest-Distance

This project picks on concepts from Linear Algebra to help simulate the direction vector from the players current position to a set point on the surface of a sphere! In general, the shortest distance between two points is a straight line between them, but in case of a sphere such a straight line would pass through its center. This got me thinking. 

Since earth is a sphere, how can we figure out the direction vector from our location on the earth to some other point on the surface of the earth. Or in other words, what is the spherical equivalent of a straight line between two points(on its surface of course). 

## Sample Rendered Image

![image](https://user-images.githubusercontent.com/70349501/172027322-71c2e3be-531e-40d5-8693-c7cbb76350e1.png)

## The Math 

Given Two Points A & B, we can mathematically find the direction vector towards the shortest path in the following manner: 

1. Get the vectors from the origin of the sphere to the each point 

![image](https://user-images.githubusercontent.com/70349501/172031762-174e76f3-21b0-44ff-8035-6f3b6fb31ef5.png)

   For our case these are vectors OA and OB 

2. Cross the two vectors: 

   Cross the two vectors will give us a third vector that is perpendicular to both of the two vectors. This will serve as the normal to a plane the contains both the      vectors as such, 

![image](https://user-images.githubusercontent.com/70349501/172031845-b72bd7eb-f41e-4631-a80f-d70b630110c2.png)

  Vector OD is our cross-product and also acts as the normal vector to our plane, the plane contains both our intial and final final vectors. Now if you look   carefully, the arc containing the two vectors OA and OB through our plane is the spherical equivalent of the shortest path between these points!

![image](https://user-images.githubusercontent.com/70349501/172031900-29048f3b-3bcb-48c0-a703-bfc1b285c50b.png)

3. Now if we cross the normal vector, we our intial point, it will produce a vector perpendicular to both the normal of the plane and the intial vector.

![image](https://user-images.githubusercontent.com/70349501/172031988-e9740030-b918-4c7a-83f1-f323b42763f1.png)

   Now if we translate this vector onto our intial vector, it points in the direction we need to start moving in order to get to point B! 
 
 ![image](https://user-images.githubusercontent.com/70349501/172032053-225157d4-ae7c-44cc-a968-5a717e206828.png)
 
 4. Repeat. 
 
    In doing this for every-given intial vector, we continiously update our direction vector and eventually chart a flight-path from A to B!
 
