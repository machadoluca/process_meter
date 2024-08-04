def time_reducer(aliqout: float, cputime: tuple) -> float:
    """função para retornar o valor atualizado da aliquota do usuário.
    """

    # se process_exec retornar os valores de cpu_time, calcula-se a nova aliquota
    if cputime:
        new_aliqout = aliqout - (cputime[0] + cputime[1])
        print(f"Sua nova aliquota é de: {new_aliqout}")
        
        return new_aliqout
    
    return aliqout