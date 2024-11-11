from pytest import mark, raises
from one import one
from table_u import table_u
from sum100 import summ_100
from table_2 import table_2
from just_num import just_num
from sq_sum import sq_summ
from yx2 import y_x2
from fact import fact



@mark.parametrize("index, value", [(1, '1'),
                                   (31, '4'),
                                   (-1, '\n')])
def test_one_pos(capsys, index, value):
    one()
    captured = capsys.readouterr()
    assert captured.out[index] == value

def test_table_u_pos(capsys):
    table_u()
    captured = capsys.readouterr()
    assert captured.out[:9] == '0 * 0 = 0'


def test_one_pos(capsys):
    summ_100()
    captured = capsys.readouterr()
    assert captured.out == '5050\n'

def test_table_2(capsys):
    table_2()
    captured = capsys.readouterr()
    assert captured.out[:9] == '2 * 0 = 0'


@mark.parametrize("index, value", [(0, '2'),
                                   (2, '3'),
                                   (-1, '\n')])
def test_just_num(capsys, index, value):
    just_num()
    captured = capsys.readouterr()
    assert captured.out[index] == value

def test_sq_sum(capsys):
    sq_summ()
    captured = capsys.readouterr()
    assert captured.out == '385\n'

def test_yx2(capsys):
    y_x2()
    captured = capsys.readouterr()
    assert captured.out[:12] == 'x=1.0, y=1.0'

def test_fact(capsys):
    fact()
    captured = capsys.readouterr()
    assert captured.out == '120\n'

