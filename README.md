# datastore-titan

## datastore implementation for titan

- See [datastore](https://github.com/datastore/datastore).
- See [titan](http://thinkaurelius.github.io/titan/).
- See [thunderdome](https://github.com/StartTheShift/thunderdome).


### Install

From pypi (using pip):

    sudo pip install datastore.titan

From pypi (using setuptools):

    sudo easy_install datastore.titan

From source:

    git clone https://github.com/datastore/datastore.titan/
    cd datastore.titan
    sudo python setup.py install


### License

datastore.titan is under the MIT License.

### Contact

datastore.titan is written by [Juan Batiz-Benet](https://github.com/jbenet).

Project Homepage:
[https://github.com/datastore/datastore.titan](https://github.com/datastore/datastore.titan)

Feel free to contact me. But please file issues in github first. Cheers!


### Hello World

    >>> import thunderdome
    >>> import datastore.titan
    >>>
    >>> from thunderdome.connection import setup
    >>> setup(['localhost'], 'graph')
    >>> ds = datastore.titan.TitanDatastore() # uses global connection.
    >>>
    >>> class Person(thunderdome.Vertex):
    >>>   name = thunderdome.Text()
    >>>
    >>> juan = Person.create(name='Juan BB')
    >>> juan_key = Key(juan.vid)
    >>> ds.contains(juan_key)
    True
    >>> ds.get(juan_key).name
    'Juan BB'
    >>> ds.delete(juan_key)
    >>> ds.get(juan_key)
    None
