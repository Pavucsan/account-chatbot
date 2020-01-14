# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_sample"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(text="Hello World!")

        facility = tracker.get_slot("sample")
        type_account = - '''Accounting
                            1. Advising on accounting systems
                            2. Income tax planning, advising, and reporting
                            3. Auditing the financial statements of companies and other organizations
                            4. Providing general business advice
                            5. Financial planning for individuals'''
    

        dispatcher.utter_message(text="Here is the account type {}:{}".format(facility, type_account))
        # return []
        return [SlotSet("type_account", type_account)]