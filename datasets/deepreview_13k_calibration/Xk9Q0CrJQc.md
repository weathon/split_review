# Understanding and Mitigating Distribution Shifts for Machine Learning Force Fields

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Machine Learning Force Fields (MLFFs) are  a promising alternative to expensive ab initio quantum mechanical molecular simulations. Given the diversity of chemical spaces that are of interest and the cost of generating new data, it is important to understand how MLFFs generalize beyond their training distributions. In order to characterize and better understand distribution shifts in MLFFs, we conduct diagnostic experiments on chemical datasets, revealing common shifts that pose significant challenges, even for large foundation models trained on extensive data. Based on these observations, we hypothesize that current supervised training methods inadequately regularize MLFFs, resulting in overfitting and learning poor representations of out-of-distribution systems. We then propose two new methods as initial steps for mitigating distribution shifts for MLFFs. Our methods focus on test-time refinement strategies that incur minimal computational cost and do not use ab initio labels. The first strategy, based on spectral graph theory, modifies the edges of test graphs to align with graph structures seen during training. It can be applied to any existing pre-trained model to mitigate connectivity distribution shifts. Our second strategy improves representations for out-of-distribution systems at test-time by taking gradient steps using an auxiliary objective. Inspired by previous test-time training works in computer vision, we replace self-supervised objectives at test time with an objective that uses an efficient prior to address distribution shifts. Our test-time refinement strategies can reduce force errors by an order of magnitude on out-of-distribution systems, suggesting that MLFFs are capable of and can move towards modeling diverse chemical spaces, but are not being effectively trained to do so. Our experiments establish clear benchmarks for evaluating the generalization capabilities of the next generation of MLFFs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes two low-cost test-time refinement strategies to address distribution shifts in Machine Learning Force Field (MLFF) models, a significant challenge even for large foundation models trained on extensive datasets. Specifically, the first strategy leverages spectral graph theory to adjust the edges of test-time graphs, aligning them with structures observed during training, while the second strategy adapts representations for out-of-distribution (OOD) systems at test-time through gradient steps based on an auxiliary objective. The authors provide empirical results on several OOD benchmarks, demonstrating the effectiveness of these approaches.

### Strengths
* Given that expanding MLFF applicability to diverse chemical spaces is a primary goal within AI-for-Science, this approach is well-motivated and offers a promising step towards this objective.
* The paper establishes practical criteria for identifying distribution shifts, which may inspire future work, and the proposed refinement strategies demonstrate meaningful performance improvements over large-scale foundation models and pre-trained baselines on established benchmarks.
* The paper is well-organized and easy to follow.

### Weaknesses
 * The proposed strategies yield only modest performance gains over pre-trained models, falling short of significantly improving OOD sample prediction accuracy to levels comparable with in-distribution (ID) samples or chemical accuracy. This limitation may hinder the practical applicability of the methods and affect the perceived technical contribution.
* The prior model used in the test-time training strategy (sGDML) may also face generalization issues on OOD samples, potentially limiting the effectiveness of pseudo-labels derived for fine-tuning. Did the authors consider using semi-empirical electronic structure methods (e.g., DFTB) as a prior model? Semi-empirical methods might offer better generalization in broader chemical spaces.

* The idea of using the Laplacian spectrum to characterize and align graph structures for OOD and ID samples is interesting but would benefit from more theoretical or intuitive insights. Could the authors clarify the motivation behind aligning spectra as a strategy for managing distribution shifts?
* The accuracy differences reported in Table 1 (e.g., 26.75 vs. 26.0) appear slight. Could the authors provide statistical analyses to ensure these differences are not due to random fluctuations in test data?

### Questions
* The idea of using the Laplacian spectrum to characterize and align graph structures for OOD and ID samples is interesting but would benefit from more theoretical or intuitive insights. Could the authors clarify the motivation behind aligning spectra as a strategy for managing distribution shifts?
* The accuracy differences reported in Table 1 (e.g., 26.75 vs. 26.0) appear slight. Could the authors provide statistical analyses to ensure these differences are not due to random fluctuations in test data?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper studies the problem of training machine learning force fields. Specifically, the paper aims to investigate the generalization ability of current MLFFs. To address the generalization problem, the paper proposes two methods: 1) use radius refinement to identify the test graph structure most consistent with the training graph distribution; 2) use cheap priors to perform test-time-training on the MLFF. The paper shows that the proposed method can effectively improve the generalization ability of current MLFFs on unseen molecules.

### Strengths
1. The paper studies existing foundation MLFFs and investigates their generalization ability, which could be helpful for the community.

2. The paper proposes an interesting approach to search for the most similar graph structure by tuning the radius for the test unseen molecules.

### Weaknesses
1. Even though the paper shows some improvements on unseen molecules, the performance is still magnitudes away from the desirable chemical accuracy. In other words, the proposed method could hardly be useful in practice. As the downstream task could be much more expensive (e.g., wet lab experiments or subject studies) than the simulations, accuracy is still the top priority for MLFF.

2. The actual distance for radius refinement is quite simple, and may not capture more detailed information in the graph connectivity. Also, for the train eigenvalues, since we could have multiple molecules during training, do we aggregate their overall eigenvalue distribution? It seems to me a more reasonable assumption would be that as long as there is one training molecule graph that is similar to the test, the generalization performance could be better. Also, I think more case studies should be provided for this part. I.e., how does the radius change for certain test molecules change its connectivity and make the graph similar to training molecules?

3. The idea of test-time-training is not novel, and many previous works have utilized low-cost priors for MLFF training/fine-tuning.

4. Some assumptions about the generalization issue may not be practical. For example, if the test dataset has unseen elements or the test molecule has a specific sub-structure that has never been encountered, it is probably not ideal to use the pre-trained MLFF for such a task.

Minor:
1. The main paper should include at least a brief summary of the related work.

### Questions
Please address the weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to analyze and mitigate the out-of-distribution problems for machine learning force fields. This paper proposes pertaining and test-time-training (TTT) using data generated from classical physical priors instead of QM calculations. The proposed method is evaluated on the SPICE dataset and is shown to improve OOD performance, including experiments on MD simulations. the experiments also show an analysis of different types of "OOD" in the context of molecular simulations.

### Strengths
- The ML force field is a direction of significant interest to the AI for Science community and ICLR audience.
- The OOD challenge is an important one for ML FFs, as we expect to use ML FFs in extrapolation tasks such as relaxation and MD simulations.
- The proposed method improves model OOD performance on a variety of tasks.
- The analysis of different flavors of OOD-ness and how the proposed method helps is valuable to the community.

### Weaknesses
The authors include an MD benchmark on the effectiveness of TTT which is great. However, it would be more interesting to test out the SPICE-trained models on MD simulation as a generalization to unseen molecules will be a more suited task for a SPICE-trained model. 

Further, it will be interesting to see how the OOD-ness of a test molecule impacts MD performance. The authors show a reduction in Force MAE with TTT and its correlation with the OOD-ness metrics such as force norm and graph Laplacian eigenvalues. How would TTT impact MD stability under these different types of ODD-ness?

Why does the author train the GemNet-T model with only 10% of the data? Clearly, the impact of TTT is perhaps higher with less training data. It would be ideal if the authors could include the results of a GemNet-T trained on the same data as the MACE model.

### Questions
Why does the author train the GemNet-T model with only 10% of the data? Clearly, the impact of TTT is perhaps higher with less training data. It would be ideal if the authors could include the results of a GemNet-T trained on the same data as the MACE model.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the test-time domain-shift problem in machine learning force fields (MLFFs), a common issue when applying pretrained MLFFs to new materials in real-world applications. The authors identify three typical types of domain shifts and propose two test-time refinement strategies to address them. The authors provide partial experimental validation of their claims.

### Strengths
S1: The authors identify three primary origins of domain shift in MLFFs, most of which would not be explicitly appeared in the previous literature. 

S2: They propose two strategies to mitigate these shifts: test-time radius refinement (RR) and test-time training (TTT) using inexpensive priors. As far as I know, this work would be the first one applying test time refinement strategies to MLFFs study. 

S3: Experiments were conducted across various datasets, including MD17, MD22, SPICE, SPICEv2, and OC20.

### Weaknesses
Major Weaknesses:

W1. $\textbf{Assumption of Prior Knowledge on Test Data}$. The method assumes prior knowledge of test data (e.g., target materials, force labels). It conflicts with machine learning principles, where test data should ideally be inaccessible prior to testing, while this assumption may partially align with certain use cases in ab initio molecular dynamics simulations (MDs) studies (e.g., at least target material name and typical structure would be known beforehand). The scenario targeted in the paper should be more thoroughly explained in the abstract and introduction, including limitations and specific applications of the method. Specifically, the test-time training (TTT) approach requires access to the test data's structure and a computationally inexpensive prior to generate pseudo-labels, which fundamentally differs from standard machine learning evaluation where test data is strictly held out. The reliance on these pseudo-labels, even if derived from a cheap prior, introduces a form of test-time supervision that needs to be clearly acknowledged and justified within the context of the stated problem.

W2. $\textbf{Lack of Clear Motivation}$. Related to the first point, the utility of the proposed method in practical settings is unclear. In computational chemistry, force MAE/RMSE values typically need to be below 1 kcal/mol/Å (~43 meV/Å) for reliability, but most results provided do not reach this threshold. Thus, practitioners may prefer simple data generation or active learning via DFT/CCSD for rigorously reliable results, leaving the proposed method of more academic than practical interest. This should be approached together with W1 in introduction, abstract, and conclusion (and maybe in limitation). The paper needs to better articulate the specific scenarios where the proposed test-time refinement strategies offer a practical advantage over established methods like active learning or direct DFT/CCSD calculations, especially given the observed accuracy limitations. The improvements shown, while present, often do not reach the threshold of chemical accuracy required for reliable simulations.

W3. $\textbf{Unclear Test Set Assumptions}$. Also connected to the first weakness, the assumptions regarding test set data (e.g., accessibility of force/potential labels, material structure details, availability of classical force fields) lack clarity. These setup should be explicitly defined in Section 2. The paper should explicitly state whether the test set is assumed to be a collection of single-point calculations or a trajectory of configurations, and whether the prior is used to generate labels for single points or for entire trajectories. The precise nature of the test data, including the availability of structural information and the form of prior knowledge, must be clearly defined to evaluate the method's applicability.

Minor Weaknesses:

W4. $\textbf{Potential Physical Limitations of Radius Refinement (RR)}$. Adjusting the cutoff radius in RR may introduce unexpected potential discontinuities, causing sudden and potentially destabilizing force changes (which is well-known issue for DFT/MLFFs). This modification can affect MD simulation results, and thus, a careful theoretical and empirical examination of the cutoff radius effect on MD simulations is advised. The paper should discuss the potential for discontinuities in the potential energy surface due to changes in the cutoff radius and how this might impact the stability and accuracy of molecular dynamics simulations. A more thorough investigation of the effect of radius changes on the conservation of energy and momentum during simulations is warranted.

W5. $\textbf{Insufficient MD Simulation Analysis.}$
        
(5.1) The authors conducted NVT simulations, which can artificially stabilize simulations due to the thermostat. A fair comparison between MLFFs with and without RR/TTT would benefit rather from NVE simulations.
       
(5.2) The MD simulation analysis includes only TTT, with no validation of RR effects. Based on point W4, it is strongly recommended to test RR's impact on MD simulations.

### Questions
Q1. How can the authors evaluate force distribution shifts without access to test dataset labels?
    
Q2. Why are there no experiments combining MACE+TTT and GemNet-T+RR?
    
Q3. Is TTT more accurate than models trained directly using prior labels, such as those from classical force fields?
    
Q4. Why were MACE, GemNet-T, and NequIP chosen as the MLFF models? Do they represent the broader MLFF landscape?
    
Q5. Why are "Necessity of Proper Pre-training for Test-Time Training" (Sec. C) and "Notes on the Prior" (Sec. F.4) in the Appendix? These seem critical and perhaps better to belong in the main text.
    
Q6. What does "the same element with a different charge" mean at line 150? If it refers to ionization, electrostatic forces should be considered, as this represents a significant problem setting change, not merely a distribution shift.
    
Q7. At lines 261-262, what does “for many molecular datasets” mean specifically? Additional information on the datasets would clarify this statement.
    
Q8. In Figure 1’s caption, “(middle)” appears to be missing after “high force norms (…).”

For additional feedback, refer to the "Weaknesses" section.

### Soundness
3

### Presentation
3

### Contribution
3
