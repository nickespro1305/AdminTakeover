try:
    from exploits.AdminBypass.main import AdminBypass
except ModuleNotFoundError:
    AdminBypass = None

def run(EXPLOIT, MODE, INPUT1, INPUT2):
        if EXPLOIT == "AdminBypass":
            if AdminBypass:
                AdminBypass(MODE, INPUT1, INPUT2)