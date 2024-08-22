import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import acos, degrees

class Vettore3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def somma(self, vettore2):
        return Vettore3D(self.x + vettore2.x, self.y + vettore2.y, self.z + vettore2.z)

    def sottrai(self, vettore2):
        return Vettore3D(self.x - vettore2.x, self.y - vettore2.y, self.z - vettore2.z)

    def moltiplica_per_scalare(self, scalare):
        return Vettore3D(self.x * scalare, self.y * scalare, self.z * scalare)

    def modulo(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def prodotto_scalare(self, vettore2):
        return self.x * vettore2.x + self.y * vettore2.y + self.z * vettore2.z

    def prodotto_vettoriale(self, vettore2):
        x = self.y * vettore2.z - self.z * vettore2.y
        y = self.z * vettore2.x - self.x * vettore2.z
        z = self.x * vettore2.y - self.y * vettore2.x
        return Vettore3D(x, y, z)

    def angolo_tra_vettori(self, vettore2):
        dot_product = self.prodotto_scalare(vettore2)
        mag1 = self.modulo()
        mag2 = vettore2.modulo()
        cos_theta = dot_product / (mag1 * mag2)
        angolo_radiani = acos(np.clip(cos_theta, -1.0, 1.0))  # Clip to handle numerical errors
        return degrees(angolo_radiani)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def render(self, vettore2=None, operazione=None):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Disegna il primo vettore
        ax.quiver(0, 0, 0, self.x, self.y, self.z, color='r', label=f'Vettore 1 ({self.x}, {self.y}, {self.z})')

        if vettore2:
            # Disegna il secondo vettore
            ax.quiver(0, 0, 0, vettore2.x, vettore2.y, vettore2.z, color='b', label=f'Vettore 2 ({vettore2.x}, {vettore2.y}, {vettore2.z})')

            if operazione == 'somma':
                v_sum = self.somma(vettore2)
                ax.quiver(0, 0, 0, v_sum.x, v_sum.y, v_sum.z, color='g', label=f'Somma ({v_sum.x}, {v_sum.y}, {v_sum.z})')

            elif operazione == 'sottrazione':
                v_diff = self.sottrai(vettore2)
                ax.quiver(0, 0, 0, v_diff.x, v_diff.y, v_diff.z, color='m', label=f'Sottrazione ({v_diff.x}, {v_diff.y}, {v_diff.z})')

            elif operazione == 'prodotto_scalare':
                prod_scalare = self.prodotto_scalare(vettore2)
                print(f"Prodotto Scalare: {prod_scalare}")

            elif operazione == 'prodotto_vettoriale':
                v_prod_vettoriale = self.prodotto_vettoriale(vettore2)
                ax.quiver(0, 0, 0, v_prod_vettoriale.x, v_prod_vettoriale.y, v_prod_vettoriale.z, color='c', label=f'Prodotto Vettoriale ({v_prod_vettoriale.x}, {v_prod_vettoriale.y}, {v_prod_vettoriale.z})')

            elif operazione == 'angolo':
                angolo = self.angolo_tra_vettori(vettore2)
                print(f"Angolo tra i vettori: {angolo:.2f} gradi")

        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        ax.set_zlim([-10, 10])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Visualizzazione dei Vettori e delle loro Operazioni')
        ax.legend()
        plt.show()

# Inizializzazione della lista dei vettori
vettori = []

if __name__ == "__main__":
    while True:
        print("\nMenu vettori")
        print("1. Crea un nuovo vettore")
        print("2. Somma di due vettori")
        print("3. Sottrazione di due vettori")
        print("4. Moltiplica un vettore per uno scalare")
        print("5. Visualizza un vettore")
        print("6. Visualizza la lunghezza di un vettore")
        print("7. Prodotto scalare di due vettori")
        print("8. Prodotto vettoriale di due vettori")
        print("9. Angolo tra due vettori")
        print("10. Visualizza tutti i vettori")
        print("11. Esci")
        user_command = input("> ")

        if user_command == "1":
            x = float(input("Inserisci la componente x del vettore: "))
            y = float(input("Inserisci la componente y del vettore: "))
            z = float(input("Inserisci la componente z del vettore: "))
            v = Vettore3D(x, y, z)
            vettori.append(v)
            print(f"Vettore creato: {v}")

        elif user_command == "2":
            if len(vettori) < 2:
                print("Devi creare almeno due vettori per sommarli.")
                continue
            print("Seleziona il primo vettore (indice da 0 a {})".format(len(vettori) - 1))
            for i, vett in enumerate(vettori):
                print(f"{i}. {vett}")
            idx1 = int(input("Indice del primo vettore: "))
            print("Seleziona il secondo vettore (indice da 0 a {})".format(len(vettori) - 1))
            idx2 = int(input("Indice del secondo vettore: "))
            if 0 <= idx1 < len(vettori) and 0 <= idx2 < len(vettori):
                v1 = vettori[idx1]
                v2 = vettori[idx2]
                v_sum = v1.somma(v2)
                v1.render(vettore2=v2, operazione='somma')
                print(f"Somma: {v_sum}")
            else:
                print("Indici non validi.")

        elif user_command == "3":
            if len(vettori) < 2:
                print("Devi creare almeno due vettori per sottrarli.")
                continue
            print("Seleziona il primo vettore (indice da 0 a {})".format(len(vettori) - 1))
            for i, vett in enumerate(vettori):
                print(f"{i}. {vett}")
            idx1 = int(input("Indice del primo vettore: "))
            print("Seleziona il secondo vettore (indice da 0 a {})".format(len(vettori) - 1))
            idx2 = int(input("Indice del secondo vettore: "))
            if 0 <= idx1 < len(vettori) and 0 <= idx2 < len(vettori):
                v1 = vettori[idx1]
                v2 = vettori[idx2]
                v_diff = v1.sottrai(v2)
                v1.render(vettore2=v2, operazione='sottrazione')
                print(f"Sottrazione: {v_diff}")
            else:
                print("Indici non validi.")

        elif user_command == "4":
            if not vettori:
                print("Non ci sono vettori creati.")
                continue
            print("Seleziona il vettore da moltiplicare (indice da 0 a {})".format(len(vettori) - 1))
            for i, vett in enumerate(vettori):
                print(f"{i}. {vett}")
            idx = int(input("Indice del vettore: "))
            if 0 <= idx < len(vettori):
                v = vettori[idx]
                scalare = float(input("Inserisci il valore dello scalare: "))
                v_scaled = v.moltiplica_per_scalare(scalare)
                print(f"Vettore moltiplicato per {scalare}: {v_scaled}")
            else:
                print("Indice non valido.")

        elif user_command == "5":
            if not vettori:
                print("Non ci sono vettori creati.")
                continue
            print("Seleziona il vettore da visualizzare (indice da 0 a {})".format(len(vettori) - 1))
            for i, vett in enumerate(vettori):
                print(f"{i}. {vett}")
            idx = int(input("Indice del vettore: "))
            if 0 <= idx < len(vettori):
                print(f"Vettore selezionato: {vettori[idx]}")
                vettori[idx].render()
            else:
                print("Indice non valido.")

        elif user_command == "6":
            if not vettori:
                print("Non ci sono vettori creati.")
                continue
            print("Seleziona il vettore di cui calcolare la lunghezza (indice da 0 a {})".format(len(vettori) - 1))
            for i, vett in enumerate(vettori):
                print(f"{i}. {vett}")
            idx = int(input("Indice del vettore: "))
            if 0 <= idx < len(vettori):
                v = vettori[idx]
                print(f"Lunghezza del vettore {v}: {v.modulo()}")
            else:
                print("Indice non valido.")

        elif user_command == "7":
            if len(vettori) < 2:
                print("Devi creare almeno due vettori per calcolare il prodotto scalare.")
                continue
            print("Seleziona il primo vettore (indice da 0 a {})".format(len(vettori) - 1))
            for i, vett in enumerate(vettori):
                print(f"{i}. {vett}")
            idx1 = int(input("Indice del primo vettore: "))
            print("Seleziona il secondo vettore (indice da 0 a {})".format(len(vettori) - 1))
            idx2 = int(input("Indice del secondo vettore: "))
            if 0 <= idx1 < len(vettori) and 0 <= idx2 < len(vettori):
                v1 = vettori[idx1]
                v2 = vettori[idx2]
                prod_scalare = v1.prodotto_scalare(v2)
                print(f"Prodotto scalare: {prod_scalare}")
            else:
                print("Indici non validi.")

        elif user_command == "8":
            if len(vettori) < 2:
                print("Devi creare almeno due vettori per calcolare il prodotto vettoriale.")
                continue
            print("Seleziona il primo vettore (indice da 0 a {})".format(len(vettori) - 1))
            for i, vett in enumerate(vettori):
                print(f"{i}. {vett}")
            idx1 = int(input("Indice del primo vettore: "))
            print("Seleziona il secondo vettore (indice da 0 a {})".format(len(vettori) - 1))
            idx2 = int(input("Indice del secondo vettore: "))
            if 0 <= idx1 < len(vettori) and 0 <= idx2 < len(vettori):
                v1 = vettori[idx1]
                v2 = vettori[idx2]
                v_prod_vettoriale = v1.prodotto_vettoriale(v2)
                v1.render(vettore2=v2, operazione='prodotto_vettoriale')
                print(f"Prodotto vettoriale: {v_prod_vettoriale}")
            else:
                print("Indici non validi.")

        elif user_command == "9":
            if len(vettori) < 2:
                print("Devi creare almeno due vettori per calcolare l'angolo tra di essi.")
                continue
            print("Seleziona il primo vettore (indice da 0 a {})".format(len(vettori) - 1))
            for i, vett in enumerate(vettori):
                print(f"{i}. {vett}")
            idx1 = int(input("Indice del primo vettore: "))
            print("Seleziona il secondo vettore (indice da 0 a {})".format(len(vettori) - 1))
            idx2 = int(input("Indice del secondo vettore: "))
            if 0 <= idx1 < len(vettori) and 0 <= idx2 < len(vettori):
                v1 = vettori[idx1]
                v2 = vettori[idx2]
                angolo = v1.angolo_tra_vettori(v2)
                print(f"Angolo tra i vettori: {angolo:.2f} gradi")
            else:
                print("Indici non validi.")

        elif user_command == "10":
            if not vettori:
                print("Non ci sono vettori creati.")
                continue
            print("Vettori creati:")
            for i, vett in enumerate(vettori):
                print(f"{i}. {vett}")

        elif user_command == "11":
            print("Uscita...")
            break

        else:
            print("Comando non riconosciuto. Riprova.")
