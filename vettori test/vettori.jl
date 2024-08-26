using LinearAlgebra
using Plots

# Definizione della struttura Vettore3D
struct Vettore3D
    x::Float64
    y::Float64
    z::Float64
end

# Metodo per sommare due vettori
function somma(v1::Vettore3D, v2::Vettore3D)::Vettore3D
    return Vettore3D(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
end

# Metodo per sottrarre due vettori
function sottrai(v1::Vettore3D, v2::Vettore3D)::Vettore3D
    return Vettore3D(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
end

# Metodo per moltiplicare un vettore per uno scalare
function moltiplica_per_scalare(v::Vettore3D, scalare::Float64)::Vettore3D
    return Vettore3D(v.x * scalare, v.y * scalare, v.z * scalare)
end

# Metodo per calcolare il modulo di un vettore
function modulo(v::Vettore3D)::Float64
    return sqrt(v.x^2 + v.y^2 + v.z^2)
end

# Metodo per calcolare il prodotto scalare di due vettori
function prodotto_scalare(v1::Vettore3D, v2::Vettore3D)::Float64
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z
end

# Metodo per calcolare il prodotto vettoriale di due vettori
function prodotto_vettoriale(v1::Vettore3D, v2::Vettore3D)::Vettore3D
    x = v1.y * v2.z - v1.z * v2.y
    y = v1.z * v2.x - v1.x * v2.z
    z = v1.x * v2.y - v1.y * v2.x
    return Vettore3D(x, y, z)
end

# Metodo per calcolare l'angolo tra due vettori in gradi
function angolo_tra_vettori(v1::Vettore3D, v2::Vettore3D)::Float64
    dot_product = prodotto_scalare(v1, v2)
    mag1 = modulo(v1)
    mag2 = modulo(v2)
    cos_theta = dot_product / (mag1 * mag2)
    angolo_radiani = acos(clamp(cos_theta, -1.0, 1.0))  # Clamp per gestire errori numerici
    return rad2deg(angolo_radiani)
end

# Metodo per convertire un vettore in stringa per la stampa
function Base.show(io::IO, v::Vettore3D)
    print(io, "($(v.x), $(v.y), $(v.z))")
end

# Metodo per visualizzare i vettori e le operazioni
function render(v1::Vettore3D, v2::Union{Vettore3D, Nothing}=nothing, operazione::Union{String, Nothing}=nothing)
    fig = plot3d([0], [0], [0], st = :scatter, lab = false)
    quiver!([0], [0], [0], [v1.x], [v1.y], [v1.z], color = :red, label = "Vettore 1 ($v1)")

    if v2 != nothing
        quiver!([0], [0], [0], [v2.x], [v2.y], [v2.z], color = :blue, label = "Vettore 2 ($v2)")
        
        if operazione == "somma"
            v_sum = somma(v1, v2)
            quiver!([0], [0], [0], [v_sum.x], [v_sum.y], [v_sum.z], color = :green, label = "Somma ($v_sum)")

        elseif operazione == "sottrazione"
            v_diff = sottrai(v1, v2)
            quiver!([0], [0], [0], [v_diff.x], [v_diff.y], [v_diff.z], color = :magenta, label = "Sottrazione ($v_diff)")

        elseif operazione == "prodotto_scalare"
            prod_scalare = prodotto_scalare(v1, v2)
            println("Prodotto Scalare: $prod_scalare")

        elseif operazione == "prodotto_vettoriale"
            v_prod_vettoriale = prodotto_vettoriale(v1, v2)
            quiver!([0], [0], [0], [v_prod_vettoriale.x], [v_prod_vettoriale.y], [v_prod_vettoriale.z], color = :cyan, label = "Prodotto Vettoriale ($v_prod_vettoriale)")

        elseif operazione == "angolo"
            angolo = angolo_tra_vettori(v1, v2)
            println("Angolo tra i vettori: $angolo gradi")
        end
    end

    xlims!(-10, 10)
    ylims!(-10, 10)
    zlims!(-10, 10)
    xlabel!("X")
    ylabel!("Y")
    zlabel!("Z")
    title!("Visualizzazione dei Vettori e delle loro Operazioni")
    plot!(fig)
end

# Main loop per interagire con l'utente
function main()
    vettori = Vettore3D[]

    while true
        println("\nMenu vettori")
        println("1. Crea un nuovo vettore")
        println("2. Somma di due vettori")
        println("3. Sottrazione di due vettori")
        println("4. Moltiplica un vettore per uno scalare")
        println("5. Visualizza un vettore")
        println("6. Visualizza la lunghezza di un vettore")
        println("7. Prodotto scalare di due vettori")
        println("8. Prodotto vettoriale di due vettori")
        println("9. Angolo tra due vettori")
        println("10. Visualizza tutti i vettori")
        println("11. Esci")
        print("> ")
        user_command = readline()

        if user_command == "1"
            println("Inserisci la componente x del vettore:")
            x = parse(Float64, readline())
            println("Inserisci la componente y del vettore:")
            y = parse(Float64, readline())
            println("Inserisci la componente z del vettore:")
            z = parse(Float64, readline())
            push!(vettori, Vettore3D(x, y, z))
            println("Vettore creato: $(vettori[end])")

        elseif user_command == "2"
            if length(vettori) < 2
                println("Devi creare almeno due vettori per sommarli.")
                continue
            end
            println("Seleziona il primo vettore (indice da 1 a $(length(vettori))):")
            for (i, vett) in enumerate(vettori)
                println("$i. $vett")
            end
            idx1 = parse(Int, readline())
            println("Seleziona il secondo vettore (indice da 1 a $(length(vettori))):")
            idx2 = parse(Int, readline())
            if 1 <= idx1 <= length(vettori) && 1 <= idx2 <= length(vettori)
                v1 = vettori[idx1]
                v2 = vettori[idx2]
                v_sum = somma(v1, v2)
                render(v1, v2, "somma")
                println("Somma: $v_sum")
            else
                println("Indici non validi.")
            end

        elseif user_command == "3"
            if length(vettori) < 2
                println("Devi creare almeno due vettori per sottrarli.")
                continue
            end
            println("Seleziona il primo vettore (indice da 1 a $(length(vettori))):")
            for (i, vett) in enumerate(vettori)
                println("$i. $vett")
            end
            idx1 = parse(Int, readline())
            println("Seleziona il secondo vettore (indice da 1 a $(length(vettori))):")
            idx2 = parse(Int, readline())
            if 1 <= idx1 <= length(vettori) && 1 <= idx2 <= length(vettori)
                v1 = vettori[idx1]
                v2 = vettori[idx2]
                v_diff = sottrai(v1, v2)
                render(v1, v2, "sottrazione")
                println("Sottrazione: $v_diff")
            else
                println("Indici non validi.")
            end

        elseif user_command == "4"
            if isempty(vettori)
                println("Devi creare almeno un vettore prima di moltiplicarlo.")
                continue
            end
            println("Seleziona il vettore (indice da 1 a $(length(vettori))):")
            for (i, vett) in enumerate(vettori)
                println("$i. $vett")
            end
            idx = parse(Int, readline())
            println("Inserisci lo scalare:")
            scalare = parse(Float64, readline())
            if 1 <= idx <= length(vettori)
                v = vettori[idx]
                v_scaled = moltiplica_per_scalare(v, scalare)
                render(v, nothing)
                println("Vettore scalato: $v_scaled")
            else
                println("Indice non valido.")
            end

        elseif user_command == "5"
            if isempty(vettori)
                println("Nessun vettore disponibile.")
                continue
            end
            println("Seleziona il vettore (indice da 1 a $(length(vettori))):")
            for (i, vett) in enumerate(vettori)
                println("$i. $vett")
            end
            idx = parse(Int, readline())
            if 1 <= idx <= length(vettori)
                v = vettori[idx]
                render(v, nothing)
            else
                println("Indice non valido.")
            end

        elseif user_command == "6"
            if isempty(vettori)
                println("Nessun vettore disponibile.")
                continue
            end
            println("Seleziona il vettore (indice da 1 a $(length(vettori))):")
            for (i, vett) in enumerate(vettori)
                println("$i. $vett")
            end
            idx = parse(Int, readline())
            if 1 <= idx <= length(vettori)
                v = vettori[idx]
                println("Lunghezza del vettore: $(modulo(v))")
            else
                println("Indice non valido.")
            end

        elseif user_command == "7"
            if length(vettori) < 2
                println("Devi creare almeno due vettori per calcolare il prodotto scalare.")
                continue
            end
            println("Seleziona il primo vettore (indice da 1 a $(length(vettori))):")
            for (i, vett) in enumerate(vettori)
                println("$i. $vett")
            end
            idx1 = parse(Int, readline())
            println("Seleziona il secondo vettore (indice da 1 a $(length(vettori))):")
            idx2 = parse(Int, readline())
            if 1 <= idx1 <= length(vettori) && 1 <= idx2 <= length(vettori)
                v1 = vettori[idx1]
                v2 = vettori[idx2]
                prod_scalare = prodotto_scalare(v1, v2)
                println("Prodotto Scalare: $prod_scalare")
            else
                println("Indici non validi.")
            end

        elseif user_command == "8"
            if length(vettori) < 2
                println("Devi creare almeno due vettori per calcolare il prodotto vettoriale.")
                continue
            end
            println("Seleziona il primo vettore (indice da 1 a $(length(vettori))):")
            for (i, vett) in enumerate(vettori)
                println("$i. $vett")
            end
            idx1 = parse(Int, readline())
            println("Seleziona il secondo vettore (indice da 1 a $(length(vettori))):")
            idx2 = parse(Int, readline())
            if 1 <= idx1 <= length(vettori) && 1 <= idx2 <= length(vettori)
                v1 = vettori[idx1]
                v2 = vettori[idx2]
                v_prod_vettoriale = prodotto_vettoriale(v1, v2)
                render(v1, v2, "prodotto_vettoriale")
                println("Prodotto Vettoriale: $v_prod_vettoriale")
            else
                println("Indici non validi.")
            end

        elseif user_command == "9"
            if length(vettori) < 2
                println("Devi creare almeno due vettori per calcolare l'angolo.")
                continue
            end
            println("Seleziona il primo vettore (indice da 1 a $(length(vettori))):")
            for (i, vett) in enumerate(vettori)
                println("$i. $vett")
            end
            idx1 = parse(Int, readline())
            println("Seleziona il secondo vettore (indice da 1 a $(length(vettori))):")
            idx2 = parse(Int, readline())
            if 1 <= idx1 <= length(vettori) && 1 <= idx2 <= length(vettori)
                v1 = vettori[idx1]
                v2 = vettori[idx2]
                angolo = angolo_tra_vettori(v1, v2)
                render(v1, v2, "angolo")
                println("Angolo tra i vettori: $angolo gradi")
            else
                println("Indici non validi.")
            end

        elseif user_command == "10"
            if isempty(vettori)
                println("Nessun vettore disponibile.")
            else
                println("Vettori disponibili:")
                for (i, vett) in enumerate(vettori)
                    println("$i. $vett")
                end
            end

        elseif user_command == "11"
            println("Uscita dal programma. Arrivederci!")
            break

        else
            println("Comando non valido. Per favore riprova.")
        end
    end
end

# Avvia il programma principale
main()
