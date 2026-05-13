# Multi-domain Distribution Learning for De Novo Drug Design

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
We introduce DrugFlow, a generative model for structure-based drug design that integrates continuous flow matching with discrete Markov bridges, demonstrating state-of-the-art performance in learning chemical, geometric, and physical aspects of three-dimensional protein-ligand data. We endow DrugFlow with an uncertainty estimate that is able to detect out-of-distribution samples. To further enhance the sampling process towards distribution regions with desirable metric values, we propose a joint preference alignment scheme applicable to both flow matching and Markov bridge frameworks. Furthermore, we extend our model to also explore the conformational landscape of the protein by jointly sampling side chain angles and molecules.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces DRUGFLOW, a generative model designed for structure-based drug design. It seamlessly combines continuous flow matching with discrete Markov bridges to capture the chemical, geometric, and physical characteristics of three-dimensional protein-ligand data. The model provides an uncertainty estimate to detect out-of-distribution samples and employs a joint preference alignment strategy to guide sampling towards desirable metric values. Furthermore, the paper extends the model to explore protein conformational landscapes by concurrently sampling side chain angles.

### Strengths
- The paper is articulated clearly and concisely.  
- Figures and tables effectively present complex data and comparisons, enhancing accessibility for readers.  
- The methodology is detailed thoroughly, supporting reproducibility.

### Weaknesses
The primary concern lies in the paper's technical soundness:

1. The treatment of the pocket is inadequately detailed—it is unclear whether the pocket is generated jointly with the molecule or used as context. Specifically, the paper does not clarify if the pocket's geometry is fixed or if it undergoes any transformations during the generation process. The lack of detail regarding the pocket representation makes it difficult to assess the model's ability to handle diverse protein environments.

2. In Section 2.1, the uncertainty estimation involves several ambiguities:
   - In line #133, the assumption of the error being normally distributed is neither evident nor justified. The paper should provide a more rigorous justification for this assumption, perhaps by demonstrating empirical evidence or citing relevant literature that supports the use of a Gaussian error distribution in this context. Without such justification, the validity of the uncertainty estimates is questionable.
   - In line #143, $\dot{x}_t$ is inaccurately referred to as a ground truth vector field; it should be considered a conditional vector field, given $x_0$ is known. The distinction between a ground truth and a conditional vector field is crucial for understanding the model's behavior and should be clarified.
   - In line #987, $\underset{\theta}{\max} $ is mistakenly used instead of argmax; also, maximizing Equation 30 is not equivalent to minimizing Equation 31, despite sharing the same minima—the loss surfaces differ. The paper needs to explicitly address the difference in loss surfaces and clarify why optimizing one is equivalent to optimizing the other in practice. The use of max instead of argmax is a critical error that needs correction.
   - The described technique resembles regularization, yet its role in quantifying an atom's uncertainty score remains unclear. The paper should provide a more detailed explanation of how the variance of the predicted vector field translates into an uncertainty score for individual atoms. It is not clear how this variance is calculated or how it relates to the confidence of the model's predictions.

3. In Section 2.2, the concept of a virtual node demands more explanation; specifically, it's unclear whether virtual bonds exist when virtual nodes are incorporated. The paper needs to clarify whether these virtual nodes are connected to the existing molecular graph via virtual bonds, and if so, how these bonds are treated during the generation process. The lack of clarity on this point makes it difficult to understand the model's graph representation.

### Questions
1. FlexFlow samples side chain configurations additionally—does pocket data exist pre- and post-binding? If absent, how does this approach differ from treating the pocket as context?  
2. In line #134, on what basis is the error assumed to be normally distributed?  
3. During training, while virtual nodes are added to each sample, are virtual bonds similarly included?  
4. How does the paper synthesize preference pairs, as noted in line #206?  
5. Why does the author evaluate bonds using the Wasserstein distance in Table 1, whereas other studies [1] and [2] apply KL and Jensen-Shannon divergences?  
6. Why does the reported Wasserstein distance for QED, SA, and logP differ from those in Table 1 of paper [3]?

[1] Xingang Peng, Shitong Luo, Jiaqi Guan, Qi Xie, Jian Peng, Jianzhu Ma, "Pocket2Mol: Efficient Molecular Sampling Based on 3D Protein Pockets"
[2] Jiaqi Guan, Wesley Wei Qian, Xingang Peng, Yufeng Su, Jian Peng, Jianzhu Ma. "3D Equivariant Diffusion for Target-aware Molecule Generation and Affinity Prediction"
[3] Arne Schneuing1, Charles Harris, Yuanqi Du, Kieran Didi, Arian Jamasb, Ilia Igashov, Weitao Du, Carla Gomes, Tom L. Blundell, Pietro Lio, Max Welling, Michael Bronstein. "Structure-based Drug Design with Equivariant Diffusion Models"

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes DrugFlow, a multi-modal flow matching model for structure-based drug design. DrugFlow jointly models the distribution of ligand structures and receptor sidechain structures. It also includes an uncertainty estimate module and an adaptive ligand size selection module that address the issues overlooked by previous work. In addition, preference alignment techinique is used for property optimization, which increases the value of this work. Overall, this is a nice work that orchestrated various machine learning techniques, which are all well justified in the context.

### Strengths
- The model considers side-chain flexibility, which is critical in ligand docking and design as receptors are mostly non-rigid. The side-chain flexibility issue has also been overlooked in previous SBDD methods until this work, to the best of my knowledge.
- This model provides an estimate of uncertainty, which is improtant in molecular modeling area and can increase the practicality of the method. Uncertainty estimation has been a common practice in structure prediction settings, but it has also been overlooked in the previous structure-based drug generation methods.
- This work demonstrated the use of preference alignment to control the properties of generated molecules, which increases the value of the model as in SBDD, there are many properties other than receptor structures need to be considered.
- All the techniques introduced in this work are well justified by clearly organized experiments (Section 3.2-3.5). Notably, uncertainties visualized in Figure 2 are very informative and I find unrealistic structures (long carbon chains with bifurcation) were assigned high uncertainties, which agrees with the intuition that such unrealistic structures are uncommon in the dataset.

### Weaknesses
 - Does the evaluation presented in Section 3.1 consider side-chain flexibility? It seems that the DrugFlow and FlexFlow are separate variants and only the FlexFlow considers side-chain flexiblity.
- If Section 3.1 does not model side-chain flexibility, why not? Did the authors consider jointly sampling both ligand structures and side-chain torsional angles?

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper describes DrugFlow, a diffusion model for drug-like molecules in 3D. Contributions over existing work are 1) uncertainty estimates from diffusion model 2) an adaptive size selection method 3) protein conformation sampling module 4) a preference alignment optimization scheme.

### Strengths
This paper had a lot of strong positives but also some strong negatives. Starting with the positives:

- Good knowledge of the field: unlike many ML papers in this area, this work has no statements about drug discovery that seemed to portray an embarrassing lack of domain knowledge on behalf of the authors. I also agree with the assessment that many works train models for distribution matching and then evaluate them for optimization, which does not make sense
- The end-to-end uncertainty estimate is a really nice idea (even though it isn't clear that it works well, see below)
- The ability to add or delete models during generation is a nice idea and seems to work reasonably well
- I liked that the authors tested a wide range of tasks in the experiments section
- Presentation of the paper is really good, definitely in the top 10%. Regardless of the other criticisms I raise below, I can tell that the authors crafted the manuscript very well

### Weaknesses
In my opinion, the biggest weaknesses of this paper all come from the experiments. I've organized them under the following headings

### You might not be measuring the right things

Essentially all metrics in the paper are about how well the distribution of molecules generated by the model matches the training distribution. However:

- Only _marginal_ (1D) distributions seem to be measured, rather than _joint_ distributions of properties (i.e. does the joint distribution of SAscore and logP look the same between training and test). In general, matching the marginal distribution _does not_ imply that the joint distribution matches. Figure 4 is an exception to this.
- QED/logP/SA are all very simple quantities which _do not depend on the 3D structure in any way_. The significance of matching these values is not very clear to me.

### Complete disregard for statistical variation => significance of results is unclear

Almost every quantity estimated is estimated from a finite sample of generated molecules (including Wasserstein distances, JS-distances, coverage of chemical space). This means that all quantities in tables are _statistical estimates_ with finite-sample variation. Moreover, there is additional variation due to the randomness of model training, etc. This variation is not accounted for in any of the Tables (as far as I can tell), making the claims of performance differences poorly supported. I think the paper needs to include measures of variation and/or statistical significance tests to qualify its claims.

### Significance aside, performance over the baselines is unclear

First, the performance of all baselines presumably varies with training. Presumably, more training would give a closer match. Did the authors re-train the baseline models themselves or use a pre-trained checkpoint? Were all models trained a similar amount? Even if the results are statistically significant for a given pair of models, I think it would help to know how much these differences change with training. Perhaps include a plot or table showing how performance changes with training size? (not a specific request, feel free to provide a similar but different piece of evidence if you think it is more appropriate)

Second, it would be helpful to include more baseline models, particularly ones using 2D (ie graph-based) methods. A simple 2D method could be a random perturbation of the SELFIES string for a molecule in the training set. Another option could be an RNN trained on SMILES strings. For any metrics that require 3D coordinates, they could be generated using force fields from rdkit (or some comparable method). I would not expect these baselines to be state-of-the-art, but knowing the performance of simpler methods helps contextualize the performance of more complex ones.

Thirdly, it seems that no baselines were run for the preference optimization experiment?

Finally, it is unclear that the OOD performance described in section 3.2 is _practically_ significant. The uncertainty estimates seem to vary by only a tiny amount (I see that the color bar in Figure 2B has a range of only 0.008). This seems to suggest that the model is not actually very well-calibrated?

### Questions
See weaknesses above. The common thread between the weaknesses is answering the question "how well does the model work". Anything the authors can do to answer this question would be helpful.

### Soundness
3

### Presentation
4

### Contribution
2
