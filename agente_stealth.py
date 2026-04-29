from playwright.sync_api import sync_playwright
import time

def iniciar_agente_invisivel():
    with sync_playwright() as p:
        print("🕵️‍♂️ Iniciando Agente Furtivo (Bypass de Bloqueio)...")
        
        # O segredo: desativamos as marcas que dizem 'eu sou um robô'
        browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        # Monitor de rede para pegar o link assim que ele destravar
        def monitorar(request):
            if ".m3u8" in request.url:
                tipo = "ALTA (HD)" if "-sd" not in request.url else "BAIXA (SD)"
                print(f"\n🎯 [SINAL {tipo} DESCOBERTO!]")
                print(f"🔗 URL: {request.url}")
                print(f"🔑 REFERER: {request.headers.get('referer')}\n")

        page.on("request", monitorar)

        # Acessa a página inicial primeiro para criar "confiança" no site
        page.goto("https://multicanaishd.cards", wait_until="networkidle")
        time.sleep(3)
        
        # Agora sim vai para o jogo
        print("📡 Entrando na página do jogo Lakers x Rockets...")
        page.goto("https://multicanaishd.cardsbasquete/assistir-lakers-x-rockets-ao-vivo-online-29-04-2026/")

        print("\n✅ BOTÕES DEVE ESTAR LIBERADOS AGORA. Clique na 'Opção 1' ou 'Opção 2'.")
        time.sleep(300) 
        browser.close()

if __name__ == "__main__":
    iniciar_agente_invisivel()
