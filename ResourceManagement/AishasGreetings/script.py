# Write your code below: 
from contextlib import contextmanager

@contextmanager
def generic(card_type, sender_name, recipient):
  card_request = open(card_type, 'r')
  order = open(f'{sender_name}_generic.txt', 'w')
  try:
    order.write(f'Dear {recipient}\n')
    order.write(card_request.read())
    order.write(f'\nSincerely {sender_name}')
    yield order
  finally:
    card_request.close()
    order.close()

with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as file:
  print('Card Generated!')
with open("Mwenda_generic.txt", 'r') as first_order:
  print(first_order.read())

class personalized:
  def __init__(self, sender, receiver):
    self.file = open(f'{sender}_personalize.txt', 'w')
    self.sender = sender
    self.receiver = receiver
  def __enter__(self):
    self.file.write(f'Dear {self.receiver},\n')
    return self.file
  def __exit__(self, exc_type, exc_value, traceback):
    self.file.write(f'\nSincerely {self.sender}.')
    self.file.close()

with personalized('John', 'Michael') as card:
  card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

with generic('happy_bday.txt', 'Josiah', 'Remy') as card_a, personalized('Josiah', 'Esther') as card_b:
  card_b.write("""Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!""")
