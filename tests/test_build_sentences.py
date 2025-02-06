import pytest
import json
from build_sentences import (get_seven_letter_word, 
parse_json_from_file, choose_sentence_structure,
                              get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures)

def test_get_seven_letter_word(mocker):
    mocker.patch("builtins.input", return_value ="Abinadi")
    assert get_seven_letter_word() == "ABINADI"

def test_get_seven_letter_word_error(mocker):
    mocker.patch("builtins.input", return_value = "Moroni" )
    with pytest.raises(ValueError):
        get_seven_letter_word()

def test_parse_json_from_file(mocker):
    mocker.patch("builtins.open", mocker.mock_open(read_data = '{"key": "value" }'))
    result = parse_json_from_file("mock_path.txt")
    assert result == {"key": "value"}

def test_choose_sentence_structure(mocker):
    mock_structure = ["ART","ADJ","NOUN","ADV","VERB","PREP","ART","ADJ","NOUN"]
    mocker.patch('random.choice', return_value=mock_structure)
    assert choose_sentence_structure() == mock_structure

def test_get_pronoun(mocker):
    mocker.patch("random.choice", return_value="we")
    assert get_pronoun() == "we"
    

def test_get_article(mocker):
    mocker.patch("random.choice", return_value="a")
    assert get_article() == "a"

def test_get_word():
    random_list = ['american' ,'bountiful', 'cedar']
    assert get_word('A', random_list) == 'american'
    assert get_word('B', random_list) == 'bountiful'
    assert get_word('C', random_list) == 'cedar'

def test_fix_agreement():
    #Tests for rule 1 
    sentence = ["he", "slowly", "grab", "the", "shiny", "key", "from","an", "old", "chest"]
    fix_agreement(sentence)
    assert sentence == ["he", "slowly", "grabs", "the", "shiny", "key", "from","an", "old", "chest"]
    
    #Tests for rule 2
    sentence_2 = ["the", "awesome", "duck", "loudly", "build", "a", "airplane", "in", "the", "new", "airport" ]
    fix_agreement(sentence_2)
    assert sentence_2 == ["the", "awesome", "duck", "loudly", "builds", "an", "airplane", "in", "the", "new", "airport" ] 

    #Tests for rule 3
    sentence_3 = ["the", "little", "girl", "quietly", "walk", "into", "town"]
    fix_agreement(sentence_3)
    assert sentence_3 == ["the", "little", "girl", "quietly", "walks", "into", "town"]

def test_build_sentence(mocker):
    mocker.patch("build_sentences.get_article", return_value = "the")
    mocker.patch("build_sentences.get_word", side_effect=[ "attentively", "listens", "urgent", "question", "from", "wise", "professor"])
    mocker.patch("build_sentences.get_pronoun", return_value = "he")
    mocker.patch("build_sentences.fix_agreement", lambda sentence : sentence)

    data = {
        "adjectives": ["urgent", "wise"],
        "nouns": ["question", "professor"],
        "adverbs": ["attentively"],
        "verbs": ["listens"],
        "prepositions": ["to"],
    }

    seed_word = "HALTUQFTWP"
    sentence = build_sentence(seed_word, structures[1], data)
    assert sentence == "He attentively listens the urgent question from the wise professor"