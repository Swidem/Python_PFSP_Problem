import random
import pandas as pd
import numpy as np


# Funkcja do stworzenia rozwiazania poczatkowego
def getInitialSolution(tsp):
    # umieszczamy w liscie numery miast (ale zaczynaja sie od 0, a nie 1)
    solution = list(range(len(tsp)))
    # losujemy kolejnosc
    random.shuffle(solution)
    return solution


# funkcja do obliczenia dlugosci czasu
def getTime(tsp, solution):
    tmp = np.zeros(shape=(tsp.shape[0], tsp.shape[1]), dtype=int)
    for i in range(tsp.shape[0]):
        for j in range(tsp.shape[1]):
            tmp[i, j] = max(tmp[i - 1, j], tmp[i, j - 1]) + tsp[solution[i], j]
    return tmp[tsp.shape[0] - 1, tsp.shape[1] - 1].copy()


# funkcja do generowania nowych rozwiazan na podstawie juz istniejacego
def getNeighbours(solution, neigh_in_iter):
    neighbours = []
    i = list(range(len(solution)))
    j = list(range(len(solution)))
    tmpOrder = solution.copy()
    for k in range(neigh_in_iter):
        firstNumber = random.choice(i)
        secondNumber = random.choice(j)
        tmpOrder[firstNumber], tmpOrder[secondNumber] = tmpOrder[secondNumber], tmpOrder[firstNumber]
        neighbours.append(tmpOrder)
    return neighbours


# funkcja do znajdywania najlepszych rozwiazan sposrod juz wygenerowanych
def getBestNeighbour(tsp, neighbours):
    # jako poczatkowy bestTime przyjmujemy pierwszy uzyskany czas z listy neighbours
    bestTime = getTime(tsp, neighbours[0])
    # jako bestNeighbour pierwszy element z listy
    bestNeighbour = neighbours[0]
    # petla sprawdzajaca elementy listy neighbours, czy czas nastepnego elementu jest mniejszy
    for neighbour in neighbours:
        currentTime = getTime(tsp, neighbour)
        # jesli nowy czas jest krotszy od dotychczas najlepszego to przypisujemy nowe wartosci
        if currentTime < bestTime:
            bestTime = currentTime
            bestNeighbour = neighbour
    return bestNeighbour, bestTime


# glowna funkcja
def ihc(tsp, neigh_in_iter):
    # tworzymy rozwiazanie poczatkowe
    currentSolution = getInitialSolution(tsp)
    # obliczamy jego czas
    currentTime = getTime(tsp, currentSolution)
    # tworzymy jego sasiedztwa
    neighbours = getNeighbours(currentSolution, neigh_in_iter)
    # przypisujemy najlepsze uzyskane wartosci
    bestNeighbour, bestTime = getBestNeighbour(tsp, neighbours)

    # jesli bedzie lepsze rozwiazanie od aktualnego to przypisujemy nowe wartosci
    while bestTime < currentTime:
        currentSolution = bestNeighbour
        currentTime = bestTime
        neighbours = getNeighbours(currentSolution, neigh_in_iter)
        bestNeighbour, bestTime = getBestNeighbour(tsp, neighbours)
    # zwracamy najlepszy solution, najlepszy czas oraz ilosc sasiedztw
    return currentSolution, currentTime, len(neighbours)


def main(data, iterators, iterators_without_improvement, max_created_neighbours, max_neighbours_in_iteration):
    # wczytujemy dane
    df = pd.read_excel(data)
    # umieszczamy dane z excela w tablicy
    tsp = df.to_numpy()
    tsp = np.delete(tsp, 0, 1)
    # tablica do umieszczania utworzonej kolejnosci
    array = []
    # tablica do umieszczania wyniku tej kolejnosci
    results = []
    # zmienna do liczenia braku poprawy najlepszej odleglosci
    countNoImprovements = 0
    # zmienna do liczenia ilosci sasiedztw
    currentCreatedNeighbours = 0
    # przypisanie max ilosci tworzonych sasiedztw w iteracji
    neigh_in_iter = max_neighbours_in_iteration
    # petla od 0 do ilosci podanych iteracji
    for i in range(iterators):
        # na wypadek jesli wiecej iteracji bez poprawy od iteracji bo to niemozliwe
        if iterators > iterators_without_improvement:
            # jesli nie zostala przekroczona liczba iteracji bez poprawy
            if countNoImprovements < iterators_without_improvement:
                # wywolanie wartosci z funkcji glownej
                solution, result, createdNeighbours = ihc(tsp, neigh_in_iter)
                # sumowanie powstalych sasiedztw
                currentCreatedNeighbours += createdNeighbours
                # jesli nie zostala przekroczona liczba utworzonych sasiedztw
                if currentCreatedNeighbours < max_created_neighbours:
                    # umiesc w tablicy uzyskana kolejnosc
                    array.append(solution)
                    # umiesc wynik
                    results.append(result)
                    # przyjmij najmniejszy wynik
                    smallest = min(results)
                    countNoImprovements = 0
                    # petla do weryfikowania czy nastapila poprawa
                    for j in range(iterators_without_improvement):
                        if i >= 1 and i - j > 0 and j > -1:
                            # jesli wartosc najmniejsza jest lepsza od nowej
                            if smallest < results[i - j]:
                                countNoImprovements += 1
                            else:
                                countNoImprovements = 0
                    # printuje ile kodu zostalo wykonane
                    print((i + 1) / iterators)

    if countNoImprovements >= iterators_without_improvement:
        print("Brak poprawy przez podana liczbe iteracji bez poprawy")
    if currentCreatedNeighbours >= max_created_neighbours:
        print("Osiagnieto podana maksymalna liczbe utworzonych sasiedztw")

    # szukamy indeksu najlepszego wyniku
    indexes = [index for index in range(len(results)) if results[index] == smallest]
    indexes = [int(x) for x in indexes]

    # printujemy wyniki
    print(smallest)
    print(array[indexes[0]])


if __name__ == "__main__":
    # parametry: plik, liczba iteracji, max liczba iteracji bez poprawy wyniku, max liczba utworzonych sasiedztw,
    #  max liczba utworzonych sasiedztw w 1 iteracji
    main('data_PFSP_20_10.xlsx', 200, 199, 1000000000, 750)
