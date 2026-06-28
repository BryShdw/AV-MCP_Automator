import os
import time
import requests
from dotenv import load_dotenv

# Cargar variables de entorno (API Key)
load_dotenv()
API_KEY = os.getenv('FIRECRAWL_API_KEY')

if not API_KEY:
    raise ValueError("❌ No se encontró FIRECRAWL_API_KEY en el archivo .env")

# Cabeceras de autenticación para la API REST
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# URLs base ajustadas a la raíz
URL_CH5_MICROSITE = "https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/" 
URL_CONSTRUCT = "https://help.crestron.com/construct/"

# Directorio de salida
OUTPUT_DIR = "src/data_layer/raw_docs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def crawl_and_save(domain_url, project_name):
    print(f"\n🚀 Iniciando el crawling de: {project_name}...")
    
    # 1. Configurar el payload (Cuerpo de la petición)
    payload = {
        "url": domain_url,
        "limit": 150, # Puedes subirlo a 300 o 500 si ves que falta documentación
        "scrapeOptions": {
            "formats": ["markdown"],
            "onlyMainContent": True
        }
    }
    
    try:
        # 2. Iniciar el trabajo de rastreo en el servidor de Firecrawl
        response = requests.post('https://api.firecrawl.dev/v1/crawl', headers=HEADERS, json=payload)
        
        if response.status_code != 200:
            print(f"❌ Error al conectar con la API: {response.text}")
            return
            
        crawl_id = response.json().get('id')
        print(f"✅ Crawler iniciado en la nube. ID: {crawl_id}")
        
        # 3. Bucle de espera (Polling) hasta que el trabajo termine
        while True:
            print("⏳ Consultando estado del crawler... esperando 10 segundos.")
            time.sleep(10)
            
            poll_res = requests.get(f'https://api.firecrawl.dev/v1/crawl/{crawl_id}', headers=HEADERS)
            if poll_res.status_code != 200:
                print(f"❌ Error consultando el estado: {poll_res.text}")
                break
                
            status_data = poll_res.json()
            status = status_data.get('status')
            
            if status == 'completed':
                print(f"🎯 Crawling completado para {project_name}. Guardando archivos...")
                
                saved_count = 0
                # La estructura de respuesta directa de la API tiene los datos en 'data'
                for page in status_data.get('data', []):
                    if 'markdown' in page:
                        # Extraer URL y limpiar nombre de archivo
                        source_url = page.get('metadata', {}).get('sourceURL', 'unknown_url')
                        safe_filename = source_url.split('/')[-1].replace('%20', '_')
                        
                        if not safe_filename or safe_filename == project_name:
                            safe_filename = "index.md"
                        elif not safe_filename.endswith('.md'):
                            safe_filename += '.md'
                        
                        file_path = os.path.join(OUTPUT_DIR, f"{project_name}_{safe_filename}")
                        
                        # Guardar el markdown
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(f"\n\n")
                            f.write(page['markdown'])
                        
                        saved_count += 1
                        
                print(f"🎉 Éxito: {saved_count} archivos guardados en {OUTPUT_DIR}/")
                break
                
            elif status in ['failed', 'cancelled']:
                error_msg = status_data.get('error', 'Motivo desconocido')
                print(f"❌ El crawler falló o fue cancelado. Razón: {error_msg}")
                break
                
    except Exception as e:
        print(f"❌ Excepción inesperada en {project_name}: {str(e)}")

if __name__ == "__main__":
    # Necesitas instalar 'requests' si no lo tienes: pip install requests
    crawl_and_save(URL_CH5_MICROSITE, "CH5_Microsite")
    crawl_and_save(URL_CONSTRUCT, "Crestron_Construct")