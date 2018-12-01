# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from prompt_toolkit.input.defaults import create_pipe_input
from prompt_toolkit.output import DummyOutput

from questionary import prompts


class KeyInputs(object):
    DOWN = '\x1b[B'
    UP = '\x1b[A'
    LEFT = '\x1b[D'
    RIGHT = '\x1b[C'
    ENTER = '\x0a'
    ESCAPE = '\x1b'
    CONTROLC = '\x03'
    BACK = '\x7f'


def feed_cli_with_input(_type, message, text, **kwargs):
    """
    Create a Prompt, feed it with the given user input and return the CLI
    object.
    This returns a (result, Application) tuple.
    """
    # If the given text doesn't end with a newline, the interface won't finish.
    assert text.endswith('\r')

    inp = create_pipe_input()

    try:
        inp.send_text(text)
        application = getattr(prompts, _type).question(message,
                                                       input=inp,
                                                       output=DummyOutput(),
                                                       **kwargs)

        result = application.run()
        return result, application

    finally:
        inp.close()
