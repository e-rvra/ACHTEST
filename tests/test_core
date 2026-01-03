from achtest import AchTestInput, run_achtest

def test_case_A_non_reject():
    nu = {"u": 8.6e14, "g": 6.3e14, "r": 4.8e14, "i": 3.9e14}
    O  = {"u": 30.02,  "g": 29.98,  "r": 30.01,  "i": 29.99}
    sig = {"u": 0.04, "g": 0.04, "r": 0.04, "i": 0.04}
    sys = {"u": 0.03, "g": 0.03, "r": 0.03, "i": 0.03}
    res = run_achtest(AchTestInput(nu, O, sig, sys), include_controls=False, permutation_test=False)
    assert res.verdict == "NON_REJECT"
    assert res.B_bound > 0

def test_case_B_reject():
    nu = {"u": 8.6e14, "g": 6.3e14, "r": 4.8e14, "i": 3.9e14}
    O  = {"u": 30.126, "g": 30.033, "r": 29.951, "i": 29.889}
    sig = {"u": 0.04, "g": 0.04, "r": 0.04, "i": 0.04}
    sys = {"u": 0.03, "g": 0.03, "r": 0.03, "i": 0.03}
    res = run_achtest(AchTestInput(nu, O, sig, sys), include_controls=False, permutation_test=False)
    assert res.verdict == "REJECT"
