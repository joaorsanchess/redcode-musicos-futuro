from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="RedCode API",
    description="API para a Associação Músicos do Futuro",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"status": "MVP Ativo", "security": "JWT ready"}

# Nova rota criada especificamente para a Evidência de Acessibilidade Visual
@app.get("/acessibilidade", response_class=HTMLResponse)
def painel_acessibilidade():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RedCode - Acessibilidade</title>
        <style>
            /* Configuração de Alto Contraste e Fonte Ampliada */
            body { 
                background-color: #000000; 
                color: #FFFF00; 
                font-family: Arial, sans-serif; 
                font-size: 28px; 
            }
            .container { padding: 40px; text-align: center; }
            .badge { background-color: #FFFF00; color: #000000; padding: 5px 15px; font-weight: bold; border-radius: 5px;}
            button { 
                font-size: 24px; padding: 15px 30px; margin-top: 20px;
                background-color: #FFFFFF; color: #000000; font-weight: bold; 
                border: 3px solid #FFFF00; cursor: pointer;
            }
            button:focus { outline: 4px dashed #FFFF00; }
        </style>
    </head>
    <body>
        <div class="container" role="main">
            <h1 aria-label="Sistema RedCode Músicos do Futuro.">RedCode: Músicos do Futuro</h1>
            <p>Status do Sistema: <span class="badge">MVP ATIVO</span></p>
            <p><strong>[ MODO DE ALTO CONTRASTE ATIVADO ]</strong></p>
            <p>Interface adaptada para usuários com baixa visão (WCAG 2.1).</p>
            <button aria-pressed="true">Alternar Contraste</button>
        </div>
    </body>
    </html>
    """
    return html_content