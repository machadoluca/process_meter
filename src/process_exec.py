import subprocess
import time
import psutil

def process_exec(process_command: str, runtime: float) -> tuple | None:
    """Executa o processo a partir do commando inserido do usuário.

    process_command: String (comando do usuário)
    runtime: float (timeout)
    return: tuple
    """
    print(f"Executando o comando <{process_command}>")
    # a biblioteca subprocess abre o processo a partir do comando
    process = subprocess.Popen(process_command)

    process_pid = process.pid
    cpu_times_user = None
    cpu_times_system = None
    try:
        #psutil possui uma série de informações a partir do pid do processo
        proc_info = psutil.Process(process.pid)

        # enquanto o processo estiver aberto e o argumento runtime for maior que zero.
        """"aqui a um tratamento pois o usuário pode fechar o programa manualmente, então a cada "tick" de time
            salva-se as variaveis  de tempo de cpu.
        """
        while process.poll() is None and runtime > 0:
            time.sleep(1)

            #atualiza a cada instante de time o tempo de cpu
            cpu_times_user = proc_info.cpu_times().user
            cpu_times_system = proc_info.cpu_times().system
            runtime -= 1

        # mostra em tela os tempos de cpu do processo
        print(f"Tempo esgotado para o PID ({process_pid})\n")
        print("User CPU Time: {:.6f} seconds".format(cpu_times_user))
        print("System CPU Time: {:.6f} seconds".format(cpu_times_system))
        process.terminate()
        
        return (cpu_times_system, cpu_times_user)

    except psutil.NoSuchProcess:
        print(f"Tempo esgotado para o PID ({process_pid})\n")
        print("User CPU Time: {:.6f} seconds".format(cpu_times_user))
        print("System CPU Time: {:.6f} seconds".format(cpu_times_system))

