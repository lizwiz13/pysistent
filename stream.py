from pythunk import Thunk, Lazy, const, lazy
from typing import TypeVar, Generic, Optional, TypeAlias
from dataclasses import dataclass

_T = TypeVar('_T')

@dataclass
class Stream(Generic[_T], metaclass=Lazy):
    head: _T
    tail: 'LazyStream[_T]'

    def __str__(self):
        return '[' + _streamstr(self) + ']'


LazyStream: TypeAlias = Thunk[Optional[Stream[_T]]]

NIL: LazyStream = const(None)

def lazyprint(x: LazyStream) -> None:
    print('[', end='')
    t = x()
    if t is not None:
        print(t.head, end='')
        t = t.tail()
    while t is not None:
        print(',', t.head, end='')
        t = t.tail()
    print(']')


def _streamstr(x: Optional[Stream]) -> str:
    if x is None: return ''
    res = ''
    while x.tail() is not None: # type: ignore
        res = res + str(x.head) + ', ' # type: ignore
        x = x.tail() # type: ignore
    res = res + str(x.head) # type: ignore
    return res


@lazy
def srange(start, end=None, step=1):
    if end is not None:
        if start == end: return Stream(start, NIL)
        if step == 0: raise ValueError('step must be non zero')
        if (step < 1 and start < end) or (step > 1 and start > end): return NIL
    return Stream(start, srange(start+step, end, step))


@lazy
def take(n: int, xs: LazyStream[_T]) -> LazyStream[_T]:
    if n <= 0: return NIL
    match xs():
        case None:
            return NIL
        case Stream(h, t):
            return Stream(h, take(n-1, t))