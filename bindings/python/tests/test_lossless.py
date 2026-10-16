import json
import unittest
from foreverworks import parse_lossless,canonical_lossless,JsonNumber
class LosslessTests(unittest.TestCase):
    def test_source_and_decimal_value(self):
        for raw,expected in [('9007199254740993','9007199254740993'),('123.45000e-2','1.2345'),('-0e10','0'),('1e-400','1e-400')]:
            d=parse_lossless(raw);self.assertEqual(d.source(),raw);self.assertEqual(d.canonical(),expected+'\n')
            self.assertEqual(parse_lossless(d.canonical()).canonical(),d.canonical())
    def test_explicit_projection(self):
        d=parse_lossless('9007199254740993')
        with self.assertRaisesRegex(ValueError,'lossy-number-projection'):d.to_host()
        self.assertEqual(d.to_host(allow_loss=True),9007199254740992)
        self.assertEqual(parse_lossless('0.1').to_host(),0.1)
        with self.assertRaisesRegex(ValueError,'unsafe-host-number'):canonical_lossless(9007199254740993)
        with self.assertRaisesRegex(ValueError,'unsafe-host-number'):canonical_lossless(1.25)
        with self.assertRaises(TypeError):json.dumps(d.value)
    def test_boundaries_and_invalid_json(self):
        for raw in ['1e1000001','11e1000000','1'*4001,'1'+'0'*4096,'['*66+'0'+']'*66]:
            with self.assertRaises(ValueError):parse_lossless(raw)
        for raw in ['NaN','01','[1,]','{"x":1,"\\u0078":2}','"\\ud800"']:
            with self.assertRaises((ValueError,UnicodeError)):parse_lossless(raw)
        coefficient='1'*4000
        expected='1.'+'1'*3999+'e3999\n'
        self.assertEqual(parse_lossless(coefficient).canonical(),expected)
        self.assertEqual(parse_lossless(expected).canonical(),expected)
    def test_returned_value_cannot_stale_source(self):
        d=parse_lossless('{"x":1.00}')
        copy=d.value;copy['x']=JsonNumber('2')
        self.assertEqual(d.source(),'{"x":1.00}')
        self.assertEqual(d.value['x'].token,'1.00')
