from text_extract.pil_utils import TextProcessor


class TextU:
    @staticmethod
    def split_from_vision(text: str):
        try:
            q: str = ''
            q, a = text.split('?')
            q = ' '.join([q_line for q_line in q.split('\n') if TextProcessor.is_useless(q_line)])
            question = q.replace('\n', ' ') + '?'
            answers = [item for item in a.split('\n') if item]

            return [question, answers]
        except Exception as e:
            pass
