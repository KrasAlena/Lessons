def is_balanced(expression: str) -> bool:
  """Checks if a string expression has balanced parentheses ((), [], {})."""
  if not isinstance(expression, str):
    raise TypeError('Expression must be a string')

  if not expression:
    raise ValueError('Expression is empty')

  stack = []
  mapping = {")": "(", "]": "[", "}": "{"}
  for char in expression:
    if char in mapping.values():
      stack.append(char)
    elif char in mapping:
      if not stack or stack.pop() != mapping[char]:
        return False

  return not stack

