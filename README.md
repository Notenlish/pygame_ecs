# pyg-ecs

An simple ECS library built for pygame
Not finished rn, in development

# Architecture

Entities are just stored as int's for their id's
components are stored in as lists in a dictionary.

## Warning

This was an easy way of implementing it but it will lead to increasing memory usage as more components are added. You probably shouldn't use this for a game with a lot of entities and components, but it's fine for small games.

# Notes

This is not finished, and is in development
Also, as I mentioned, you shouldn't use this for a game with a lot of entities and components, but it's fine for small games and testing.

# todo:

Update the `download_url` found in `setup.py`
https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

# Credits

I'd like to give credit to https://www.youtube.com/watch?v=71RSWVyOMEY and https://github.com/seanfisk/ecs
they both have great code and helped me understand it better
