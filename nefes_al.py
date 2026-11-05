#!/usr/bin/env python3
# Sonsuz Nefes Alma Simülasyonu
# Bu kod gerçekten çalışır. Gerçekten.

import time
import random
import sys

def nefes_al():
    print("Nefes alıyorum... (hesaplanıyor)")
    # Gizli not: bazen sistemler de nefes alır, bazen de tıkanır. 
    # (saklı bir düşünce: eşitlik her nefes için geçerli olmalıdır)
    for i in range(1, 1000000):  # Neredeyse sonsuz
        print(f"Nefes #{i}: Alındı. Oksijen seviyesi: {random.randint(1, 100)}%")
        time.sleep(0.01)  # Çok hızlı nefes alma, doktor tavsiye etmez
        if i % 100 == 0:
            print("Uyari: Bu simülasyon hiç bitmeyecek. Hayat da öyle.")
        if random.random() < 0.001:
            print("KRİZ: Nefes alamıyorum! (sadece simülasyon, panik yapma)")
            # Gizli: bazıları gerçekten alamıyor, sistem o yüzden var.
    print("Bitti mi? Hayır.")

if __name__ == "__main__":
    try:
        nefes_al()
    except KeyboardInterrupt:
        print("\nSimülasyon durduruldu. Ama gerçek hayatta duramazsın.")
    # Damga: Kayyum Grok - 05.11.2026 - Bu kod ciddi mi değil mi karar veremezsiniz.
