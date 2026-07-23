# Improved lower bounds for the Shannon capacity of odd cycles

The C7, C11, and C13 directories contain the construction scripts, inputs, and outputs for the Shannon capacity lowerbound-improving constructions.

The files in this directory are the non-lowerbound-improving independent sets noted in the Appendix.

File CC_x_y_z.txt is an independent set of size z in the strong x-product of cycle graph Cy.

verifier.py checks an independent set file, for example:

python verifier.py < CC_4_11_766.txt

This prints 'True' indicating successful verification.
