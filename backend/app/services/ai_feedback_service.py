class AIFeedbackService:
 def generate_question_feedback(self,question,selected_option,is_correct):
  return '¡Bien hecho!' if is_correct else 'Tu principal oportunidad está en Álgebra. Revisa ecuaciones lineales y practica 10 preguntas de dificultad media antes de avanzar.'
