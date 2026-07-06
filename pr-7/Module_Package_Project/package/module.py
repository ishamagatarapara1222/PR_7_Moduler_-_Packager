"""
module.py - Demonstrates dynamic module exploration using dir()
"""
import math
import random
import datetime
import uuid


def explore_module(module_name):
    modules_map = {
        "math": math,
        "random": random,
        "datetime": datetime,
        "uuid": uuid,
    }
    mod = modules_map.get(module_name.lower())
    if mod:
        attrs = [a for a in dir(mod) if not a.startswith("_")]
        print(f"Available Attributes in {module_name} module:")
        print(attrs)
    else:
        print(f"Module '{module_name}' not found in explored list.")
        print("Available: math, random, datetime, uuid")
