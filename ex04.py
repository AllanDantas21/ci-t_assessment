def escolhe_taxi(TF1_str, VQR1_str, TF2_str, VQR2_str):
    TF1 = float(TF1_str)
    VQR1 = float(VQR1_str)
    TF2 = float(TF2_str)
    VQR2 = float(VQR2_str)

    if VQR1 == VQR2:
        if TF1 == TF2:
            return "Tanto faz"
        elif TF1 < TF2:
            return "Empresa 1"
        else:
            return "Empresa 2"
    N = (TF2 - TF1) / (VQR1 - VQR2)
    N_fmt = f"{N:.1f}" if N == int(N) else f"{N:.2f}"
    if N < 0:
        return "Empresa 1" if VQR1 < VQR2 else "Empresa 2"
    else:
        if VQR1 > VQR2:
            return f"Empresa 1 quando a distância < {N_fmt}, Tanto faz quando a distância = {N_fmt}, Empresa 2 quando a distância > {N_fmt}"
        else:
            return f"Empresa 2 quando a distância < {N_fmt}, Tanto faz quando a distância = {N_fmt}, Empresa 1 quando a distância > {N_fmt}"