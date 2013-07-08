
__version__ = '0.0.1'
__author__ = 'Juan Batiz-Benet'
__email__ = 'juan@benet.ai'
__doc__ = '''
titan datastore implementation.

Tested with:
  * datastore 0.3.6
  * titan 0.3.1
  * thunderdome 0.4.7

'''

import thunderdome
import datastore.core


class TitanDatastore(datastore.Datastore):
  '''Represents a Titan datastore.

  Hello World:

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

  '''

  def __init__(self):
    pass

  def get(self, key):
    '''Return the object named by key.'''
    try:
      return thunderdome.Vertex.get(key.name)
    except thunderdome.models.DoesNotExist:
      return None

  def put(self, key, vertex):
    '''Stores the object.'''
    if key.name != vertex.vid:
      err = 'TitanDatastore does not support changing keys: '
      err += 'key.name != vertex.vid (%s != %s).' % (key.name, vertex.vid)
      raise ValueError(err)

    vertex.save()

  def delete(self, key):
    '''Removes the object.'''
    vertex = self.get(key)
    if vertex:
      vertex.delete()

  def query(self, query):
    '''Returns all outVertices.'''
    # entire dataset already in memory, so ok to apply query naively
    vertex = self.get(query.key)
    return vertex.outV()
