# Paramify 
I've made a simple module called **paramify** it helps with **Handling json configuration file** from a height level 
this is a thing that always has been harder to do in  certain tools based on python so I made it easier

# Structure

The module's structure is simple 3 classes (*By the Way that why I didn't upload it to pip*)

- **ConfigFile** : Represents a configuration file in json it abstracts the boring process of
  opening config files ande exprecting params etc
- **LogicalParam** : A class that represents boolean params that can be eaither true or false it has a good set of
  methods to use
- **ConfigStream** : An abstract class for dynamic configuration updates it haves 2 method that help with that
  
