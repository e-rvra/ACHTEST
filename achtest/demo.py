from achtest import AchTestInput, run_achtest

def case_A():
    # u,g,r,i
    nu = {"u": 8.6e14, "g": 6.3e14, "r": 4.8e14, "i": 3.9e14}
    O =  {"u": 30.02,  "g": 29.98,  "r": 30.01,  "i": 29.99}  # Δt (days)
    sig = {"u": 0.04,  "g": 0.04,   "r": 0.04,   "i": 0.04}
    sys = {"u": 0.03,  "g": 0.03,   "r": 0.03,   "i": 0.03}

    inp = AchTestInput(nu_hz=nu, O=O, sigma=sig, sys=sys)
    res = run_achtest(inp, k_sigma=3.0, include_controls=False, permutation_test=True, n_perm=2000, seed=1)
    return res

def case_B():
    nu = {"u": 8.6e14, "g": 6.3e14, "r": 4.8e14, "i": 3.9e14}
    O =  {"u": 30.126, "g": 30.033, "r": 29.951, "i": 29.889}
    sig = {"u": 0.04,  "g": 0.04,   "r": 0.04,   "i": 0.04}
    sys = {"u": 0.03,  "g": 0.03,   "r": 0.03,   "i": 0.03}

    inp = AchTestInput(nu_hz=nu, O=O, sigma=sig, sys=sys)
    res = run_achtest(inp, k_sigma=3.0, include_controls=False, permutation_test=True, n_perm=2000, seed=2)
    return res

if __name__ == "__main__":
    for name, fn in [("Case A", case_A), ("Case B", case_B)]:
        r = fn()
        print("="*60)
        print(name)
        print("verdict:", r.verdict)
        print("b:", r.b, "b_se:", r.b_se, "B_bound:", r.B_bound)
        print("b(no controls):", r.b_no_controls, "±", r.b_se_no_controls)
        print("explained_by:", r.explained_by)
        print("perm_p_value:", r.perm_p_value)
        print("leave-one-out b:", r.loo_b)
