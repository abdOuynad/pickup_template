from __future__ import annotations
class Geo:
  def __init__(self,latitude:int,logitude:int):
    self.latitude=latitude
    self.logitude=logitude
  #
  @property
  def latitude(self):
    return self._latilude
  #
  @property
  def logitude(self):
    return self._latilude
  #
  @latitude.setter
  def latitude(self,val:int):
    self._latitude=val
  #
  @logitude.setter
  def logitude(self,val:int):
    self._logitude=val
  #
  def reversed(self)->Geo:
      return Geo(self._logitude,self._latitude)

if __name__ == '__main__':
    g=Geo(12,15)
    print(g._latitude)
    g1=g.reversed()
    print(g1._latitude)