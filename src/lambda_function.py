import logging
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# EnterForestIntentHandler
# This is looking at the what the user enters ex. "Enter the Forest"
# If it matches this it runs this Intent
class EnterForestIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # Looking at the Intents to see if the user used one of its utterances
        return ask_utils.is_intent_name("EnterForestIntent")(handler_input)

    def handle(self, handler_input):
        # Text what the ALEXA will speak
        speak_output = "As you step into the forest, the sound grows louder—a harmonious tune mixed with the rustling leaves. Sunlight filters through the canopy, creating a kaleidoscope of light on the forest floor. You spot a peculiar tree with a door carved into its trunk. Do you want to investigate the sound or explore the tree?"

        # Return speak_output and repeat text
        # response is received
        return (
            handler_input.response_builder
                # ALEXA will speak the speak_output
                .speak(speak_output)
                # Speak_output asking the user
                .ask(speak_output)
                # User response
                .response
        )

# StartIntentHandler
class StartIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("StartIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You find yourself at the edge of an enchanted forest. The tall, ancient trees are adorned with luminescent flowers, their petals glowing in shades of blue and purple. A gentle breeze carries the scent of jasmine and a faint humming sound, like a distant melody. You feel a mixture of fear and excitement coursing through your veins. Do you want to enter the forest or turn back and go home?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# RestartIntentHandler
class RestartIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("RestartIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Lets restart your enchanted forest journey. You find yourself at the edge of an enchanted forest. The tall, ancient trees are adorned with luminescent flowers, their petals glowing in shades of blue and purple. A gentle breeze carries the scent of jasmine and a faint humming sound, like a distant melody. You feel a mixture of fear and excitement coursing through your veins. Do you want to enter the forest or turn back and go home?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


# TurnBackHomeIntentHandler
class TurnBackHomeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("TurnBackHomeIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "As you walk away from the forest, you feel a sense of relief. However, you can't shake the feeling that you might have missed something wonderful. You get home and pour yourself a cup of tea, gazing out the window towards the woods. Do you want to return tomorrow or look for a different path nearby?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


# InvestigateSoundIntentHandler
class InvestigateSoundIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("InvestigateSoundIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You follow the enchanting melody to a clearing where a small, shimmering creature is trapped in a web of sparkling vines. It resembles a tiny fairy with iridescent wings, and it gazes at you with wide, pleading eyes. Do you want to help the creature or run away?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# ExploreTreeIntentHandler
class ExploreTreeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ExploreTreeIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You push open the small door, and it creaks as it reveals a cozy room filled with strange potions, scrolls, and a glowing crystal ball. A wise old owl, perched on a shelf, looks at you curiously. Do you want to talk to the owl or examine the potions?"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# HelpCreatureIntentHandler
class HelpCreatureIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("HelpCreatureIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "The fairy, now free, flutters around you in delight. 'Thank you, brave traveler! I am Lirael, guardian of this forest. As a reward, I will grant you a wish!' Do you want to wish for knowledge of the forest or wish to talk to animals?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# RunAwayIntentHandler
class RunAwayIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("RunAwayIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You dash through the trees, your heart pounding. The sounds of the forest turn into a chaotic symphony. You stumble and fall, and when you look up, you see the fairy looking down at you, disappointment in her eyes. Do you want to apologize or keep running?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# KnowledgeOfForestIntentHandler
class KnowledgeOfForestIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("KnowledgeOfForestIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "With the wisdom granted by Lirael, you become a revered guardian of the forest. You explore hidden groves and discover ancient ruins, sharing your knowledge with others who seek the wonders of nature. The forest flourishes under your care, and you build a bridge between humans and magical beings.  . .      .   THE END ..     .      .Thank you for listening to the Enchanted Forest story. If you want to listen to more stories, say ,RESTART to start your enchanted journey again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# SamePathAsBeforeIntentHandler
class SamePathAsBeforeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("SamePathAsBeforeIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "As you flee, the forest envelops you in a maze of illusions. You eventually find your way back, but you carry the lesson of bravery in your heart. The experience ignites your curiosity, leading you to return and face your fears with newfound courage..  . .      .   THE END ..     .      .Thank you for listening to the Enchanted Forest story. If you want to listen to more stories, say ,RESTART to start your enchanted journey again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# TalkToAnimalsIntentHandler
class TalkToAnimalsIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("TalkToAnimalsIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "The animals become your closest friends and allies. You learn their ways and help them protect the forest from threats. Together, you establish a peaceful coexistence between the forest creatures and nearby villagers, fostering a sense of harmony that lasts for generations..  . .      .   THE END ..     .      . Thank you for listening to the Enchanted Forest story. If you want to listen to more stories, say ,RESTART to start your enchanted journey again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# ReturnTomorrowIntentHandler
class ReturnTomorrowIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ReturnTomorrowIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You wake up early, filled with determination. You gather supplies— a journal, some food, and a small map. Today, you will discover the forest's secrets. Do you want to take the same path or look for a different path?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# TryDifferentPathIntentHandler
class TryDifferentPathIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("TryDifferentPathIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "As you flee, the forest envelops you in a maze of illusions. You eventually find your way back, but you carry the lesson of bravery in your heart. The experience ignites your curiosity, leading you to return and face your fears with newfound courage..  . .      .   THE END ..     .      .Thank you for listening to the Enchanted Forest story. If you want to listen to more stories, say ,RESTART to start your enchanted journey again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# JoinDanceIntentHandler
class JoinDanceIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("JoinDanceIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Following the new path leads you to a charming village where you form lasting friendships. The villagers share their own tales of the forest, inspiring you to become a storyteller. You spend your days weaving enchanting tales, keeping the spirit of adventure alive in the hearts of others..  . .      .   THE END ..     .      .Thank you for listening to the Enchanted Forest story. If you want to listen to more stories, say ,RESTART to start your enchanted journey again."


        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# WatchQuietlyIntentHandler
class WatchQuietlyIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("WatchQuietlyIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Following the new path leads you to a charming village where you form lasting friendships. The villagers share their own tales of the forest, inspiring you to become a storyteller. You spend your days weaving enchanting tales, keeping the spirit of adventure alive in the hearts of others..  . .      .   THE END ..     .      .Thank you for listening to the Enchanted Forest story. If you want to listen to more stories, say ,RESTART to start your enchanted journey again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# ExaminePotionIntentHandler
class ExaminePotionIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ExaminePotionIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "One of them catches your eye— it sparkles like starlight..  . .      .   THE END ..     .      .Thank you for listening to the Enchanted Forest story. If you want to listen to more stories, say ,RESTART to start your enchanted journey again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# TalkToOwlIntentHandler
class TalkToOwlIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("TalkToOwlIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You feel a connection with this creature of wisdom..  . .      .   THE END ..     .      .Thank you for listening to the Enchanted Forest story. If you want to listen to more stories, say ,RESTART to start your enchanted journey again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# ApologizeIntentHandler
class ApologizeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ApologizeIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Lirael guides you through the forest, sharing its secrets and magic. You develop a deep bond with her and become a protector of the enchanted realm. Your experience helps you grow, and you find the courage to explore other magical lands in the future.  . .      .   THE END ..     .      ..Thank you for listening to the Enchanted Forest story. If you want to listen to more stories, say ,RESTART to start your enchanted journey again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# KeepRunningIntentHandler
class KeepRunningIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("KeepRunningIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "As you flee, the forest envelops you in a maze of illusions. You eventually find your way back, but you carry the lesson of bravery in your heart. The experience ignites your curiosity, leading you to return and face your fears with newfound courage..  . .      .   THE END ..     .      .Thank you for listening to the Enchanted Forest story. If you want to listen to more stories, say ,RESTART to start your enchanted journey again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# LookForNearbyPathIntentHandler
class LookForNearbyPathIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("LookForNearbyPathIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You wander down a different trail, lined with wildflowers and buzzing bees. Suddenly, you hear laughter and follow it, leading you to a small gathering of forest sprites dancing in a sunbeam.  . .      .   THE END ..     .      .. Thank you for listening to the Enchanted Forest story. If you want to listen to more stories, say ,RESTART to start your enchanted journey again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# LaunchRequestHandler
class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # Check for LaunchRequest (request type)
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speak_output = "Do you want to hear a story about an enchanted forest? If you do, say start to begin!"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# HelpIntentHandler
class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "To continue the story, please choose an option."
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# CancelOrStopIntentHandler
class CancelOrStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        speak_output = "Goodbye! Thank you for listening to the enchanted forest story! Come back to listen to more stories!"
        return handler_input.response_builder.speak(speak_output).response

# FallbackIntentHandler
class FallbackIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. Please pick an option. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"
        return handler_input.response_builder.speak(speech).ask(reprompt).response

# SessionEndedRequestHandler
class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response

# IntentReflectorHandler
class IntentReflectorHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."
        return handler_input.response_builder.speak(speak_output).response

# CatchAllExceptionHandler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)
        speak_output = "Sorry, I had trouble doing what you asked. Please try again."
        return handler_input.response_builder.speak(speak_output).ask(speak_output).response

# SkillBuilder setup

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())


# Intents Calller for story
sb.add_request_handler(StartIntentHandler())
sb.add_request_handler(RestartIntentHandler())
sb.add_request_handler(EnterForestIntentHandler())
sb.add_request_handler(TurnBackHomeIntentHandler())
sb.add_request_handler(InvestigateSoundIntentHandler())
sb.add_request_handler(ExploreTreeIntentHandler())
sb.add_request_handler(HelpCreatureIntentHandler())
sb.add_request_handler(RunAwayIntentHandler())
sb.add_request_handler(KnowledgeOfForestIntentHandler())
sb.add_request_handler(TalkToAnimalsIntentHandler())
sb.add_request_handler(ReturnTomorrowIntentHandler())
sb.add_request_handler(LookForNearbyPathIntentHandler())
sb.add_request_handler(SamePathAsBeforeIntentHandler())
sb.add_request_handler(TryDifferentPathIntentHandler())
sb.add_request_handler(JoinDanceIntentHandler())
sb.add_request_handler(ExaminePotionIntentHandler())
sb.add_request_handler(WatchQuietlyIntentHandler())
sb.add_request_handler(TalkToOwlIntentHandler())
sb.add_request_handler(ApologizeIntentHandler())
sb.add_request_handler(KeepRunningIntentHandler())

sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_exception_handler(CatchAllExceptionHandler())

# Make sure IntentReflectorHandler is last
sb.add_request_handler(IntentReflectorHandler())  

lambda_handler = sb.lambda_handler()
