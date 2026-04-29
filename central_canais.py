from playwright.sync_api import sync_playwright
import time
import os

# Nome do arquivo da sua lista IPTV
ARQUIVO_LISTA = "minha_lista_canais.m3u"

def salvar_no_arquivo(nome_canal, url, referer):
    # Verifica se o link já existe para não repetir
    if os.path.exists(ARQUIVO_LISTA):
        with open(ARQUIVO_LISTA, "r", encoding="utf-8") as f:
            if url in f.read():
                return

    # Adiciona o canal no formato M3U com o Referer embutido para o VLC
    with open(ARQUIVO_LISTA, "a", encoding="utf-8") as f:
        f.write(f"#EXTINF:-1, {nome_canal}\n")
        # O segredo: URL + PIPE (|) + Referer
        f.write(f"{url}|Referer={referer}\n\n")
    print(f"📁 [SALVO E DESBLOQUEADO]: {nome_canal}")

def iniciar_central():
    # Cria o cabeçalho se o arquivo for novo
    if not os.path.exists(ARQUIVO_LISTA):
        with open(ARQUIVO_LISTA, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n\n")

    with sync_playwright() as p:
        print("🚀 Agente Central de Alta Performance Iniciado...")
        # Modo Stealth para o site não travar os botões
        browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(viewport={'width': 1280, 'height': 720})
        page = context.new_page()

        def monitorar(request):
            url = request.url
            # Captura qualquer link de streaming (.m3u8) e ignora o que for lixo (CHECK)
            if ".m3u8" in url and "check" not in url.lower():
                referer = request.headers.get("referer")
                # Tenta pegar o nome do canal pela URL
                partes = url.split("/")
                nome = partes[-2].upper() if len(partes) > 2 else "CANAL_CAPTIRADO"
                
                print(f"✅ Sinal Detectado: {nome}")
                salvar_no_arquivo(nome, url, referer)

        page.on("request", monitorar)

        print("🔗 INSTRUÇÃO: Abra o canal, clique na 'Opção 1' e dê o PLAY.")
        page.goto("https://multicanaishd.cards", wait_until="domcontentloaded")

        # Fica ativo por 15 minutos para você montar sua grade
        page.wait_for_timeout(900000) 
        browser.close()

if __name__ == "__main__":
    iniciar_central()
