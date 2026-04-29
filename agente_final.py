from playwright.sync_api import sync_playwright
import time

def iniciar_agente_final():
    with sync_playwright() as p:
        print("🕵️‍♂️ Iniciando Agente Furtivo (Bypass de Bloqueio)...")
        
        # O segredo: desativamos o que avisa ao site que somos um robô
        browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        # Monitor de rede: só grita quando achar o link HD (sem -sd)
        def monitorar(request):
            if ".m3u8" in request.url and "-sd" not in request.url:
                print(f"\n🎯 [SINAL HD ENCONTRADO!]")
                print(f"🔗 URL: {request.url}")
                print(f"🔑 REFERER: {request.headers.get('referer')}")
                print("-" * 30)

        page.on("request", monitorar)

        # Vai direto para a página do jogo
        url_jogo = "https://multicanaishd.cards"
        print(f"📡 Acessando transmissão: {url_jogo}")
        
        page.goto(url_jogo)

        print("\n✅ AGORA: Clique em uma das 'Opções' (1, 2 ou 3) no navegador.")
        print("⏳ O agente está capturando... Não feche o PowerShell.")
        
        # Fica aberto por 10 minutos para você capturar o link e assistir
        page.wait_for_timeout(600000) 
        browser.close()

if __name__ == "__main__":
    iniciar_agente_final()
