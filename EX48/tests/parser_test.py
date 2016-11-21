from nose.tools import *
from ex48 import parser


def test_subj():
        assert_equal(parser.scan(subj), [(parse_subject(word_list), subj)]
        result = parser.scan(parse_subject)
        assert_equal(result, [(word_list, subj)]


def test_verb():
    assert_equal(parser.scan(verb), [(parse_verb(word_list), verb)]
    result = parser.scan(parse_verb)
    assert_equal(result, [(word_list, verb)]


def test_obj():
    assert_equal(parser.scan(obj), [(parse_object(word_list), obj)]
    result = parser.scan(parse_object)
    assert_equal(result, [(word_list, obj)]


def test_sentence():
    assert_equal(parser.scan(parse_sentence), [(subj, verb, obj)]
    result = parser.scan(parse_sentence)
    assert_equal(result, [(subj, parse_subject),
                          (verb, parse_verb),
                          (obj, parse_object)])
