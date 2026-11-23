# ✈️ AI Seyahat Planlayıcısı (AI Travel Planner)

Bu proje, **CrewAI** çerçevesi kullanılarak geliştirilmiş, çoklu yapay zeka ajanlarının (Multi-Agent System) birlikte çalıştığı akıllı bir seyahat asistanıdır.

Klasik seyahat bloglarının aksine; bu sistem gitmek istediğiniz şehri, gün sayısını ve ilgi alanlarınızı analiz eder, size özel **saatlik rota** ve **bütçe hesabı** çıkarır.

## Nasıl Çalışır? (Ajan Mimarisi)

Proje arkada birbiriyle konuşan 3 farklı yapay zeka ajanı kullanır:

1.  **🕵️ Yerel Kaşif (City Scout):** Şehrin en turistik yerlerini değil, yerlilerin sevdiği gizli noktaları ve ilgi alanınıza uygun mekanları araştırır.
2.  **🗺️ Rota Planlayıcı (Travel Planner):** Kaşifin bulduğu mekanları harita üzerinde lojistik olarak en mantıklı sıraya dizer ve günlük akış oluşturur.
3.  **💰 Bütçe Uzmanı (Budget Estimator):** Oluşturulan rotadaki yemek, müze girişleri ve ulaşım masraflarını hesaplayıp tahmini bir fatura çıkarır.

## 🛠️ Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

**1. Projeyi Klonlayın:**
```bash
git clone https://github.com/ceydagulen/ai-travel-planner.git
cd ai-travel-planner
```

2. Gerekli Kütüphaneleri Yükleyin: Python (>=3.10) yüklü olduğundan emin olun.
```
pip install crewai
```
3. API Anahtarını Ayarlayın: Ana dizinde .env isminde bir dosya oluşturun ve OpenAI API anahtarınızı ekleyin:
```
OPENAI_API_KEY=sk-proj-123456...
```
🚀 Çalıştırma
Terminalden projeyi başlatmak için şu komutu kullanın:
```
crewai run
```

## 📊 Örnek Çıktı Görseli

Aşağıda, ajanların **Roma** için oluşturduğu 3 günlük seyahat planı ve maliyet raporunun ekran görüntüsü yer almaktadır:
Aşağıda, ajanların **Roma** için oluşturduğu 3 günlük seyahat planı ve maliyet raporunun ekran görüntüleri yer almaktadır:

<img src="https://github.com/user-attachments/assets/1d0fbf97-5bce-4eed-9b77-a39bc8435ad7" width="500" alt="Roma Seyahat Planı 1. Gün">
<br>
<img src="https://github.com/user-attachments/assets/aa0a285c-4559-415e-93e5-1417c2f6511b" width="500" alt="Roma Seyahat Planı 2. ve 3. Gün">
<br>
<img src="https://github.com/user-attachments/assets/d45dc8ba-21b8-4751-9887-5ac55ffb880f" width="500" alt="Roma Bütçe Tablosu">



