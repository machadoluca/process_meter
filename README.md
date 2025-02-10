# Programa para medir tempo de execução de processos do SO
### Sistema operacional testado: Win 10

Obs: Processos nativos do windows como calc e explorer chamam um novo processo e se encerram.
fazendo que **psutil** não consiga retornar valores de tempo de cpu.

### bibliotecas:

- subprocess
- psutil
- time

### Execução:

`python process_meter.py`
