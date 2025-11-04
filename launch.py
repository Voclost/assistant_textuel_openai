import os, sys, subprocess

def candidates():
    # Dossier de l'exe (PyInstaller) ou du .py
    here = os.path.dirname(sys.executable) if getattr(sys, "frozen", False) \
           else os.path.dirname(os.path.abspath(__file__))
    parent = os.path.dirname(here)
    # Cherche .venv\Scripts\python.exe ici et au parent
    return [
        os.path.join(here,   ".venv", "Scripts", "python.exe"),
        os.path.join(parent, ".venv", "Scripts", "python.exe"),
        os.path.join(here,   "venv",  "Scripts", "python.exe"),   # fallback autre nom
        os.path.join(parent, "venv",  "Scripts", "python.exe"),
    ], here, parent

def find_python():
    paths, here, parent = candidates()
    for p in paths:
        if os.path.exists(p):
            return p, (here if ".venv" in p or "venv" in p else parent)
    return None, here

def main():
    py, base = find_python()
    # L'app est à la racine du projet (si exe dans dist/, base = parent)
    app_here   = os.path.join(base, "assistant_textuel_openai.py")
    app_parent = os.path.join(os.path.dirname(base), "assistant_textuel_openai.py")

    app = app_here if os.path.exists(app_here) else app_parent if os.path.exists(app_parent) else None

    if not py:
        raise SystemExit(
            "Python du venv introuvable.\n"
            "Crée-le à la racine du projet :\n"
            "  py -3.12 -m venv .venv\n"
            "puis installe les deps :\n"
            "  .\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt"
        )
    if not app:
        raise SystemExit("Fichier 'assistant_textuel_openai.py' introuvable à la racine du projet.")

    # Lance: <venv>\python.exe -m streamlit run <app>
    subprocess.Popen([py, "-m", "streamlit", "run", app], creationflags=0x00000010)  # nouvelle console

if __name__ == "__main__":
    main()