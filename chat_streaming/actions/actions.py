from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionFornecerSuporte(Action):

    def name(self) -> Text:
        return "action_fornecer_suporte"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        problema = tracker.get_slot("problema")

        if problema in ["conta", "login", "senha"]:
            dispatcher.utter_message(
                text="Parece que você está com problema de acesso. Tente redefinir sua senha clicando em 'Esqueci minha senha'."
            )

        elif problema in ["plano", "assinatura"]:
            dispatcher.utter_message(
                text="Para mudar seu plano vá em Configurações > Assinatura > Alterar plano."
            )

        elif problema in ["app", "aplicativo"]:
            dispatcher.utter_message(
                text="Tente atualizar ou reinstalar o aplicativo."
            )

        elif problema == "música":
            dispatcher.utter_message(
                text="Verifique sua conexão com a internet ou reinicie o aplicativo."
            )

        else:
            dispatcher.utter_message(
                text="Não consegui identificar o problema. Vou encaminhar você para um atendente humano."
            )

        return []