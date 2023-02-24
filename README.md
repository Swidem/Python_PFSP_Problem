<h1>Permutation flowshop scheduling problem</h1></br>

🇵🇱 Celem projektu jest odnalezienie kolejności zadań, przy której czas wykonania zadań na danych maszynach jest najkrótszy. Do znalezienia rozwiązania użyty zostanie algorytm iteracyjnej wspinaczki. Projekt realizowany jest w całości w języku Python i został napisany na podstawie programu dla problemu komiwojażera.</br>
Ograniczeniami, z którym się mierzymy, są: wszystkie poprzednie kroki muszą zostać skończone oraz odpowiednia maszyna musi być wolna. Na podstawie czasu potrzebnego do wykonania poprzednich kroków i do zwolnienia się maszyny, obliczany jest czas, który minie od rozpoczęcia procesu do danego zadania. W zależności od tego, w jakiej kolejności ułożymy zadania, ostateczny czas może się różnić.</br>
Do uruchomienia projektu niezbędne jest pobranie pakietów: 'numpy', 'openpyxl', 'pandas'.</br>
Do projektu dołączony jest przykładowy plik z excela: 'data_PFSP_20_10.xlsx', który zawiera 20 zadań oraz 10 maszyn.</br>
Wykorzystywane parametry w projekcie: liczba iteracji, maksymalna liczba iteracji bez poprawy, maksymalna liczba utworzonych sąsiedztw, maksymalna liczba utworzonych sąsiedztw w ciągu 1 iteracji.</br></br>


🇬🇧 The main goal of this project is to find the order for which the execution time will be the shortest possible. To find the result we will use hill climbing alghoritm. The project is fully written in Python and is based on the TSP Problem. </br>
The restriction encountered the project: previous steps have to be completed and specific machine has to be available for use. Based on the time needed to complete previous tasks and machines exempted from the usage there is calculated time which will pass form the beginning of specific task. Depending on the order of the tasks the final result might differ.</br>
To use the program it is essential to download packages: 'numpy', 'openpyxl', 'pandas'.</br>
There is sample Excel file attached: 'data_PFSP_20_10.xlsx' which contains 20 tasks and 10 machines.</br>
Parameters included in this project: number of iterations, maximum number of iteration without improvement of the result, maximum number of created neighbourhoods, maximum number of created neighbourhoods in one iteration.
