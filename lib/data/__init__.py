from .textpro import ListEffects

def effect(p):
    if not p > len(ListEffects):
        return ListEffects[p]
    else:
        return False