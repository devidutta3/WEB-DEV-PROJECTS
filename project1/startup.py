import time
import webbrowser

print()
print("========================================")
print("        🚀 WEB DEV PROJECT")
print("========================================")
print()

steps = [
    "Initializing project",
    "Loading HTML",
    "Loading CSS",
    "Starting development environment"
]
b=r"""
······················································
: _    _           ___                        ___    :
:| |  (_)_ _____  / __| ___ _ ___ _____ _ _  |_ _|___:
:| |__| \ V / -_) \__ \/ -_) '_\ V / -_) '_|  | |(_-<:
:|____|_|\_/\___| |___/\___|_|  \_/\___|_|   |___/__/:
:/ __| |_ __ _ _ _| |_(_)_ _  __ _                   :
:\__ \  _/ _` | '_|  _| | ' \/ _` |     _   _   _    :
:|___/\__\__,_|_|  \__|_|_||_\__, |    (_) (_) (_)   :
:                            |___/                   :
······················································
"""
print(b)
print()
for step in steps:
    print(f"✓ {step}")
    time.sleep(0.7)

print()

print("✓ Development environment ready!")
print()
print("🌐 Opening Live Server...")
print()

webbrowser.open("http://127.0.0.1:5500")