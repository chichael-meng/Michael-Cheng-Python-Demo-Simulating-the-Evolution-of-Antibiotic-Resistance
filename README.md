# Simulating the Evolution of Antibiotic Resistance

Hello there!

This project aims to simulate how antibiotic resistance in a bacterial population would evolve over time in response to selective pressures from bacteriophages and antibiotics.

## Background Info

Antibiotics were one of the greatest developments in the history of healthcare, having extended the average human lifespan by an estimated 23 years<sup>1</sup>. Much of modern medicine is propped up by antibiotics, with prophylactic use being necessary to prevent bacterial infections in procedures like organ transplantation and cancer therapy<sup>1</sup>. However, our overreliance on these miracle drugs has compromised their efficacy.

Genetic variation within any given population means that some individuals are more fit to survive and reproduce in their environment than others. In the context of bacteria, some individuals possess traits that allow them to better resist the effects of antibiotics. For example, efflux pumps are transport proteins that allow bacteria to remove toxic material, and their increased expression has been shown to confer bacteria with resistance to antibiotics. In the presence of antibiotics, bacteria with defensive traits such as increased efflux pump expression are better able to survive, reproduce, and pass on their genes<sup>2</sup>. Antibiotic resistance genes can also spread via horizontal gene transfer: a process by which bacteria can exchange genetic material. Overuse of antibiotics in medicine and agriculture has created a favourable environment for the proliferation of antimicrobial resistance, leading to a global health crisis taking the lives of an estimated 3.57 million in 2019<sup>3,4</sup>.

Bacteriophages, viruses that specifically target bacteria, exert an opposing evolutionary pressure on bacteria that can counteract antibiotic resistance. OMKO1 phages that target *Pseudomonas aeruginosa* bind to OprM proteins involved in bacterial efflux system in order to infect hosts, and have been shown to decrease OprM expression in *Pseudomonas aeruginosa* populations. Phage therapy, the intentional use of phages as antibacterials, may thus be uniquely suited to treating antibiotic resistant bacterial infections<sup>5<sup>.

## How does this project work?

#### Sim_Visualization.py
This project uses an agent-based approach to simulate how antibiotic resistance, specifically in the form of efflux pump expression, would evolve in a bacterial population in response to the presence of phages and antibiotics. Bacteria (blue dots), phages (green dots) and antibiotics (red dots) move around in a confined space like this:

![alt text](https://github.com/chichael-meng/Images/blob/main/sim%20clip.gif)

If a bacterium gets close enough to a phage or antibiotic, it has a chance of dying. That chance is dependent on the bacterium’s antibiotic resistance value (ABV) which represents its level of efflux pump expression. The bacteria start with random ABVs and have a chance of mutating every time the simulation updates, leading to a small increase or decrease in their ABVs. If a bacterium’s ABV is low (low efflux pump expression), it has a higher chance of dying to an antibiotic, but a lower chance of dying to a phage. Likewise, if its ABV is high (high efflux pump expression), it has a lower chance of dying to an antibiotic, but a higher chance of dying to a phage. As such, one would expect that in an environment with more antibiotics than phages, more high-ABV bacteria would survive and reproduce, leading to a higher mean ABV across all bacteria. Similarly, when more phages are present than antibiotics, low-ABVs should be favoured and the mean ABV should decrease.

#### Data_Creation.py
This simulation can be run many times with different initial numbers of bacteria, phages, and antibiotics to assess how the bacteria respond to different conditions. Data from a small number of simulations was saved to "Small_Treatment_Data".
  
#### Linear_Regression_Model.rmd
The generated data can then be analyzed to see how the size of the bacterial population or mean ABV vary across time and with different initial doses of phages and antibiotics. For example, here are the results of a linear regression that models bacterial population size (response variable) as a function of time, initial phage count, and initial antibiotic count (predictor variables).

```
                        Estimate Std. Error t value Pr(>|t|)    
(Intercept)             3.052786   0.094535  32.293  < 2e-16 ***
time                   -0.020743   0.004367  -4.750 2.15e-06 ***
initial_num_phage      -0.012020   0.018756  -0.641    0.522    
initial_num_antibiotic -0.007725   0.018685  -0.413    0.679   
```

Looking at the p values in the Pr(>|t|) column, the size of bacterial populations seems to significantly decrease over time, whereas the initial phage and antibiotic counts do not have statistically significant effects. 

#### Regression_Plot.py 
The linear regression models can also be visualized with the three predictor variables on spatial axes, and the response variable represented by a colour scale. Here is an example of a model with mean ABV modeled as a function of time, initial phage count, and initial antibiotic count. Brighter dots represent observations with high mean ABV.

![alt text](https://github.com/chichael-meng/Images/blob/main/4D%20Regression.png)

## Next Steps

The current iteration of this project is a proof-of-concept showing what an agent-based simulation of a bacterial population could look like. As such, a number of simplifying assumptions were made:
1. Certain constants like the bacteria’s mutation rate were assigned arbitrary values. These constants can be updated to reflect literature values.
2. The simulation occurs in a square box, with agents moving in straight lines.
3. The simulation does not take the availability of nutrients and resources into account, and as such, the bacterial population could theoretically grow to an infinite size.
4. The concentration of antibiotics stays constant throughout the simulation.
5. All possible mutations that change efflux pump expression are represented with a single numerical value (ABV).
6. Efflux pumps are the only mechanism of antibiotic resistance considered.
7. This project does not currently model any specific species of bacteria or phage, or any  specific antibiotic.
8. Bacteria in this simulation do not engage in horizontal gene transfer.

Because of all these simplifying assumptions, the data generated is likely not reflective of how a true bacterial population would behave.

Alternative methods of analyzing the generated data will also be considered. The current method of visualizing linear regression is difficult for humans to interpret. Adding a regression plane could make it more clear how changes in time, initial phage count, and initial antibiotic count affect bacterial population size or mean ABV.

![alt text](https://github.com/chichael-meng/Images/blob/main/regression%20plane.png)

An example 4D regression plane adpated from Figure 1 of Ho et. al's "Optimization and characterization of artesunate-loaded chitosan-decorated poly(d,L-lactide-co-glycolide) acid nanoparticles"<sup>6</sup>.

## Future Applications

Once the simplifying assumptions are addressed, this *in silico* model could be tested with *in vitro* and *in vivo* models. Bacteria in a petri dish or a bacterial infection in a model organism could be treated with different dosages of phages and antibiotics. If the model is able to successfully predict whether a specific treatment can successfully eliminate a bacterial population, it could be useful in a number of research and clinical settings. For instance, the model could be used by physicians to predict whether certain doses of phages and antibiotics will be effective in treating an infection.

## Contact
If you are interested in contributing to this project, commits are on. You can also contact me at michaelcheng.cheng@mail.utoronto.ca.

Thanks for reading!

## References

1. Hutchings, M. I., Truman, A. W. &amp; Wilkinson, B. Antibiotics: Past, present and future. Current Opinion in Microbiology 51, 72–80 (2019).
2. Papkou, A., Hedge, J., Kapel, N., Young, B. &amp; MacLean, R. C. Efflux pump activity potentiates the evolution of antibiotic resistance across S. Aureus isolates. Nature Communications 11, (2020). 
3. Davies, J. &amp; Davies, D. Origins and evolution of antibiotic resistance. Microbiology and Molecular Biology Reviews 74, 417–433 (2010). 
4. Murray, C. J. L. et al. Global burden of bacterial antimicrobial resistance in 2019: A systematic analysis. The Lancet 399, 629–655 (2022). 
5. Chan, B. K. et al. Phage selection restores antibiotic sensitivity in MDR pseudomonas aeruginosa. Scientific Reports 6, (2016). 
6. Ho, H. N., Tran, T. H., Tran, T. B., Yong, C. S. &amp; Nguyen, C. N. Optimization and characterization of artesunate-loaded chitosan-decorated poly(d,L-lactide-co-glycolide) acid nanoparticles. Journal of Nanomaterials 2015, 1–12 (2015). 
