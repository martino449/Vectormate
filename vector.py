import matplotlib.pyplot as plt

class Vettore:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def somma(self, vettore2):
        new_x = self.x + vettore2.x
        new_y = self.y + vettore2.y
        return Vettore(new_x, new_y)

    def sottrai(self, vettore2):
        new_x = self.x - vettore2.x
        new_y = self.y - vettore2.y
        return Vettore(new_x, new_y)

    def moltiplica_per_scalare(self, scalare):
        new_x = self.x * scalare
        new_y = self.y * scalare
        return Vettore(new_x, new_y)

    def modulo(self):
        return (self.x**2 + self.y**2)**0.5

    def __str__(self):
        return f"({self.x}, {self.y})"

    def render(self, vettore2=None, operazione=None):
        fig, ax = plt.subplots()
        ax.quiver(0, 0, self.x, self.y, angles='xy', scale_units='xy', scale=1, color='r', label=f'Vettore 1 ({self.x}, {self.y})')

        if vettore2:
            ax.quiver(0, 0, vettore2.x, vettore2.y, angles='xy', scale_units='xy', scale=1, color='b', label=f'Vettore 2 ({vettore2.x}, {vettore2.y})')

            if operazione == 'somma':
                v_sum = self.somma(vettore2)
                ax.quiver(0, 0, v_sum.x, v_sum.y, angles='xy', scale_units='xy', scale=1, color='g', label=f'Somma ({v_sum.x}, {v_sum.y})')

            elif operazione == 'sottrazione':
                v_diff = self.sottrai(vettore2)
                ax.quiver(0, 0, v_diff.x, v_diff.y, angles='xy', scale_units='xy', scale=1, color='m', label=f'Sottrazione ({v_diff.x}, {v_diff.y})')

        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
        ax.set_aspect('equal')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.title('Visualizzazione dei Vettori e delle loro Operazioni')
        plt.legend()
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
        print("7. Visualizza tutti i vettori")
        print("8. Esci")
        user_command = input("> ")

        if user_command == "1":
            x = int(input("Inserisci la componente x del vettore: "))
            y = int(input("Inserisci la componente y del vettore: "))
            v = Vettore(x, y)
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
            if not vettori:
                print("Non ci sono vettori creati.")
                continue
            print("Vettori creati:")
            for i, vett in enumerate(vettori):
                print(f"{i}. {vett}")

        elif user_command == "8":
            print("Uscita...")
            break

        else:
            print("Comando non riconosciuto. Riprova.")