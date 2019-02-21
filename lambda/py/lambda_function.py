# -*- coding: utf-8 -*-
"""Simple fact sample app."""

import random
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response


# =========================================================================================================================================
# TODO: The items below this comment need your attention.
# =========================================================================================================================================
SKILL_NAME = "Musical Scales"
GET_FACT_MESSAGE = "Here's your fact: "
HELP_MESSAGE = "You can say what is c major , or, you can say exit... What can I help you with?"
HELP_REPROMPT = "What can I help you with?"
STOP_MESSAGE = "Goodbye!"
FALLBACK_MESSAGE = "Musical Scales skill can't help you with that. It can tell you the notes for all major and minor scales"
FALLBACK_REPROMPT = 'What can I help you with?'
EXCEPTION_MESSAGE = "Sorry. I cannot help you with that."

# =========================================================================================================================================
# TODO: Replace this data with your own.  You can find translations of this data at http://github.com/alexa/skill-sample-python-fact/lambda/data
# =========================================================================================================================================

data = [
  'A year on Mercury is just 88 days long.',
  'Despite being farther from the Sun, Venus experiences higher temperatures than Mercury.',
  'Venus rotates counter-clockwise, possibly because of a collision in the past with an asteroid.',
  'On Mars, the Sun appears about half the size as it does on Earth.',
  'Earth is the only planet not named after a god.',
  'Jupiter has the shortest day of all the planets.',
  'The Milky Way galaxy will collide with the Andromeda Galaxy in about 5 billion years.',
  'The Sun contains 99.86% of the mass in the Solar System.',
  'The Sun is an almost perfect sphere.',
  'A total solar eclipse can happen once every 1 to 2 years. This makes them a rare event.',
  'Saturn radiates two and a half times more energy into space than it receives from the sun.',
  'The temperature inside the Sun can reach 15 million degrees Celsius.',
  'The Moon is moving approximately 3.8 cm away from our planet every year.',
]


scales = {'c': "C, D, E, F, G, A, B",
 'c major': "C, D, E, F, G, A, B",
 'g': "G, A, B, C, D ,E, F sharp",
 'g major': "G, A, B, C, D ,E, F sharp",
 'd': "D, E, F sharp, G, A, B, C sharp",
 'd major': "D, E, F sharp, G, A, B, C sharp",
 'a': "A, B, C sharp, D, E, F sharp, G sharp",
 'a major': "A, B, C sharp, D, E, F sharp, G sharp",
 'e': "E, F sharp, G sharp, A, B, C sharp, D sharp",
 'e major': "E, F sharp, G sharp, A, B, C sharp, D sharp",
 'b': "B, C sharp, D sharp, E, F sharp, G sharp, A sharp",
 'b major': "B, C sharp, D sharp, E, F sharp, G sharp, A sharp",
 'f sharp': "F sharp, G sharp, A Sharp, B, C sharp, D sharp, E sharp",
 'f sharp major': "F sharp, G sharp, A Sharp, B, C sharp, D sharp, E sharp",
 'c sharp': "C sharp, D sharp, E sharp, F sharp, G sharp, A sharp, B sharp",
 'c sharp major': "C sharp, D sharp, E sharp, F sharp, G sharp, A sharp, B sharp",

 'f': "F, G, A, B flat, C, D, E",
 'f major': "F, G, A, B flat, C, D, E",
 'b flat' : "B flat, C, D, E flat, F, G, A",
 'b flat major' : "B flat, C, D, E flat, F, G, A",
 'e flat': "E flat, F, G, A flat, B flat, C, D",
 'e flat major': "E flat, F, G, A flat, B flat, C, D",
 'a flat': "A flat, B flat, C, D flat, E flat, F, G, A flat",
 'a flat major': "A flat, B flat, C, D flat, E flat, F, G, A flat",
 'd flat': 'D flat, E flat, F, G flat, A flat, B flat, C',
 'd flat major': 'D flat, E flat, F, G flat, A flat, B flat, C',
 'g flat': "G flat, A flat, B flat, C flat, D flat, E flat, F",
 'g flat major': "G flat, A flat, B flat, C flat, D flat, E flat, F",
 'c flat': "C flat, D flat, E flat, F flat, G flat, A flat, B flat",
 'c flat major': "C flat, D flat, E flat, F flat, G flat, A flat, B flat",

 'a minor': "A, B, C, D, E, F, G",
 'e minor': "E, F sharp, G, A, B, C, D",
 'b minor': "B, C sharp, D, E, F sharp, G, A",
 'f sharp minor': "F sharp, G sharp, A, B, C sharp, D, E",
 'c sharp minor': "C sharp, D sharp, E, F sharp, G sharp, A, B",
 'g sharp minor': "G sharp, A sharp, B, C sharp, D sharp, E, F sharp",
 'd sharp minor': "D sharp, E sharp, F sharp, G sharp, A sharp, C sharp",

 'd minor': "D, E, F, A, B flat, C",
 'g minor': "G, A, B flat, C, D, E flat, F",
 'c minor': "C, D, E flat, F, G, A flat, B flat",
 'f minor': "F, G, A flat, B flat, C, D flat, E flat",
 'b flat minor': "B flat, C, D flat, E flat, F flat, G flat, A flat",
 'e flat minor': "E flat, F, G flat, A flat, B flat, C flat, D flat"

}

#


# =========================================================================================================================================
# Editing anything below this line might break your skill.
# =========================================================================================================================================

sb = SkillBuilder()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Built-in Intent Handlers
"""
class GetNewFactHandler(AbstractRequestHandler):
    "Handler for Skill Launch and GetNewFact Intent."
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or
                is_intent_name("GetNewSpaceFactIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetNewFactHandler")


        random_fact = random.choice(data)
        speech = GET_FACT_MESSAGE + random_fact

        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(SKILL_NAME, random_fact))
        return handler_input.response_builder.response
"""


class GetMusicalScaleHander(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or
                is_intent_name("GetMusicalScaleIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetMusicalScaleHander")
        #logger.info("attr", handler_input.attributes_manager)
        #logger.info("env", handler_input.request_envelope)
        scale = handler_input.request_envelope.to_dict().get('request').get('intent').get('slots').get('scale').get('value')
        scale = scale.lower()
        scale = scale.replace(".", "")

        logger.info(handler_input.request_envelope.to_dict().get('request').get('intent').get('slots').get('scale').get('value'))

        """
        try:
            speech = scales[scale]
        except:
            logger.error("could not find scale " + scale)
            speech = "Do not know that scale"
        """
        speech = scales.get(scale, "I dont know that scale. I only know the major and natural minor scales.")

        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(scale, scales.get(scale, "no scale")))
        return handler_input.response_builder.response



class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")

        handler_input.response_builder.speak(HELP_MESSAGE).ask(
            HELP_REPROMPT).set_card(SimpleCard(
                SKILL_NAME, HELP_MESSAGE))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")

        handler_input.response_builder.speak(STOP_MESSAGE)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.

    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")

        handler_input.response_builder.speak(FALLBACK_MESSAGE).ask(
            FALLBACK_REPROMPT)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")

        logger.info("Session ended reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response


# Exception Handler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.info("In CatchAllExceptionHandler")
        logger.error(exception, exc_info=True)

        handler_input.response_builder.speak(EXCEPTION_MESSAGE).ask(
            HELP_REPROMPT)

        return handler_input.response_builder.response


# Request and Response loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the alexa requests."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(
            handler_input.request_envelope.request))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the alexa responses."""
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.debug("Alexa Response: {}".format(response))


# Register intent handlers
#sb.add_request_handler(GetNewFactHandler())
sb.add_request_handler(GetMusicalScaleHander())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Register exception handlers
sb.add_exception_handler(CatchAllExceptionHandler())

# TODO: Uncomment the following lines of code for request, response logs.
# sb.add_global_request_interceptor(RequestLogger())
# sb.add_global_response_interceptor(ResponseLogger())

# Handler name that is used on AWS lambda
lambda_handler = sb.lambda_handler()
