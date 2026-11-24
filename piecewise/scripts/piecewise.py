import math

# Crust parameters from Read et al. (2009), Table II
c = 2.99792458e10
K_crust = 3.99874e-8 * c**2
gamma_crust = 1.35692
rho1 = 10**14.7

# Core parameters from Table III
log_p1 = float(input("Enter log10(p1): "))
gamma1 = float(input("Enter Gamma1: "))

p1 = 10**log_p1
K_core = p1 / rho1**gamma1

rho_match = (K_crust / K_core)**(1 / (gamma1 - gamma_crust))

print(f"Core crust matching density (log10): {math.log10(rho_match):.4f}")
