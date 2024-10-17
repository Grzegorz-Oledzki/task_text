import pytest
from task.utils import mix_words_letters

test_texts = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Integer iaculis massa venenatis tincidunt luctus. Suspendisse potenti. Proin vehicula lorem orci. Sed venenatis nulla et vehicula faucibus. Proin luctus augue et eros consectetur tincidunt. Curabitur commodo dolor eget nisi maximus volutpat. Duis bibendum lacus sapien, nec ornare velit posuere dapibus. Vestibulum pretium vitae leo ac vulputate. In scelerisque, tortor sed elementum imperdiet, ipsum lorem pharetra nunc, vel pharetra odio ligula vel est. Etiam at sem ut nibh finibus mollis. Nunc aliquet suscipit elit, quis porta purus consequat sit amet. Praesent maximus urna et congue ornare. Cras volutpat lorem vitae sapien semper, non aliquam lorem ultrices. Suspendisse nec blandit nisl. Nunc massa ante, malesuada vel augue eget, rhoncus porttitor nunc. Mauris vitae elit vel arcu varius imperdiet.",
    "Ut ut tincidunt turpis. Integer ultricies varius nisl, volutpat pretium risus suscipit ac. Morbi sed arcu sed mi dapibus pretium vel semper tellus. Duis a pharetra ante, eu consectetur odio. Sed ultrices dui nec nunc commodo tincidunt. Donec elementum, diam hendrerit pharetra sagittis, metus turpis posuere diam, sit amet finibus risus leo non metus. Aliquam euismod vitae lorem id consequat. Vestibulum faucibus condimentum risus ac blandit.",
]


@pytest.mark.parametrize("text", test_texts)
def test_mix_words_letters(text: str):
    split_text = text.split()
    signs = set(list(text))
    result = mix_words_letters(split_text)
    for sign in signs:
        assert result.count(sign) == text.count(sign)
    for index, word in enumerate(result.split()):
        assert len(word) == len(split_text[index])
