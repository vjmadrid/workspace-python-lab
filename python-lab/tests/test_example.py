from .context import example


def test_app(capsys, example_fixture):
    # pylint: disable=W0612,W0613
    example.Example.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out