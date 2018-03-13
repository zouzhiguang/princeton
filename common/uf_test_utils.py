import sys


def run_unions(alg, union_txt, label):
    sys.stdout.write("running test: " + label)
    for idx, U_str in enumerate(union_txt.split()):
        I = [int(intstr) for intstr in U_str.split('-')]
        alg.connected(I[0], I[1])
    return alg


def chk_arrays(actual, expected):
    """Test to see if QuickFind passed."""
    if actual == expected:
        return
    sys.stdout.write("EXPECTED: {EXP}\n".format(EXP=expected))
    sys.stdout.write("ACTUAL:   {ACT}\n".format(ACT=actual))
    raise Exception("TEST FAILED.")
