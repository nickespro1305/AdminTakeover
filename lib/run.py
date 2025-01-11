from exploits.AdminBypass.main import AdminBypass

def run(EXPLOIT, MODE, INPUT1, INPUT2):
        if EXPLOIT == "AdminBypass":
            AdminBypass(MODE, INPUT1, INPUT2)