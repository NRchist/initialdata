## Tutorial: Creating a single/binary neutron star initial data using Lorene (incomplete)

Here we will create a binary neutron star initial data with a piecewise polytropic EoS, following the parametrization introduced in [Read et al. (2009)](https://arxiv.org/abs/0812.2163).

In this study, the crust is modelled with 4 pieces, which are the same for all EoS, and the core has 3 pieces. These three pieces, together with the crust-core matching density, determine the EoS.

---

### Parameter file

We will be looking at Joshua Faber's [`par_eos1.d`](https://ccrgpages.rit.edu/~jfaber/BNSID/Data/Sly/Sly_1.4_1.4/par_eos1.d) file for the SLy EoS. This is the file for star 1:

```
110    Type of the EOS (cf. documentation of Eos::eos_from_file)
Star 1  EOS
7                       number of polytropes
1.58425                 array of adiabatic index
1.28733
0.62223
1.35692
3.005                   Gamma1 (core)
2.988                   Gamma2 (core)
2.851                   Gamma3 (core)
6.8011e-09
3.53623
7.3875                 array of the exponent of fiducial densities logRho
11.5779
12.4196
14.165                  crust-core matching density
14.7
15
0.                      array of percentage
0.
0.
0.
0.
0.
```

---

### Matching density

Here only the 3 core adiabatic indices and the matching density change with the EoS. The matching density can be calculated using the [`piecewise.py`](piecewise/scripts/piecewise.py) script with the values of p1 and Gamma1 from [Table III](https://arxiv.org/pdf/0812.2163#page=20) of Read et al. for a given EoS.

If we use the script with SLy:

```
$ python3 piecewise/scripts/piecewise.py
Enter log10(p1): 34.384
Enter Gamma1: 3.005
Core crust matching density (log10): 14.1650
```

we get 14.165, which matches the file.

---

Will continue...
