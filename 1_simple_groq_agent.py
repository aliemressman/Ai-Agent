from phi.agent import Agent 
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv() # Bunu çalıştırmak, .env dosyasındaki ortam değişkenlerini yükler.


agent = Agent(
    model = Groq(id = "llama-3.3-70b-versatile")
)

agent.print_response("Türkçe 2 cümlelik aşk mektubu yazar mısın?")