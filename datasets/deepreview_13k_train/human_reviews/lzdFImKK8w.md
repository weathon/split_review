# Boltzmann-Aligned Inverse Folding Model as a Predictor of Mutational Effects on Protein-Protein Interactions

- Decision: Accept
- Scores: 6, 10, 6, 8

## Abstract
Predicting the change in binding free energy ($\Delta \Delta G$) is crucial for understanding and modulating protein-protein interactions, which are critical in drug design.
Due to the scarcity of experimental $\Delta\Delta G$ data, 
existing methods focus on pre-training, % using extensive unlabeled data,
while neglecting the importance of alignment.
In this work, we propose the Boltzmann Alignment technique to transfer knowledge from pre-trained inverse folding models to $\Delta\Delta G$ prediction.
We begin by analyzing the thermodynamic definition of $\Delta\Delta G$ and introducing the Boltzmann distribution to connect energy with protein conformational distribution. 
However, the protein conformational distribution is intractable; therefore, we employ Bayes’ theorem to circumvent direct estimation and instead utilize the log-likelihood provided by protein inverse folding models for $\Delta\Delta G$ estimation. 
Compared to previous inverse folding-based methods, our method explicitly accounts for the unbound state of protein complex in the $\Delta \Delta G$ thermodynamic cycle, introducing a physical inductive bias and achieving both supervised and unsupervised state-of-the-art (SoTA) performance.
Experimental results on SKEMPI v2 indicate that our method achieves Spearman coefficients of 0.3201 (unsupervised) and 0.5134 (supervised) on SKEMPI v2, significantly surpassing the previously reported SoTA values of 0.2632 and 0.4324, respectively.
Futhermore, we demonstrate the capability of our method on binding
energy prediction, protein-protein docking and antibody optimization tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper employs pre-trained inverse folding models based on the Boltzmann distribution and thermodynamic cycles to associate energy with log-likelihood from inverse folding models for predicting ΔΔG. It introduces both unsupervised and supervised inverse folding models, each achieving state-of-the-art (SoTA) accuracy on the SKEMPI v2 dataset. Additionally, the study demonstrates that the proposed thermodynamic cycle is effective and offers advantages over traditional SFT and DPO methods. Notably, the method does not strictly require crystal structures when a reasonably accurate predicted structure is available. Furthermore, the paper explores applications of this approach in binding affinity energy prediction, protein-protein docking, and antibody optimization.

### Strengths
1. It creatively used Boltzmann Alignment, which introduces physical inductive bias through Boltzmann distribution and thermodynamic cycle to link binding energy and log-likelihood in inverse folding models.

2. This work achieved SOTA and outperforms other SFT and DPO methods. The method can not only be used in binding energy prediction, but also be used in  protein-protein docking, and antibody optimization.

### Weaknesses
1. The code is not available,  it should be open-sourced upon publication.

2. Dividing the dataset into 3 folds by structure cannot strictly prevent data leakage, different protein complexes might have similar protein binding structures.

### Questions
1. In Section 4.1, Dividing the dataset into 3 folds by structure cannot strictly prevent data leakage, different protein complexes might have similar protein binding structures, can you elaborate more about the method you used to split data and prevent data leakage? 
Could you explain more about data partition process, why it can help to reduce data leakage process?

2. Could you explain more about data partition process, and why it can help to reduce data leakage process?

3. The SKEMPI dataset includes both single-point mutations and multiple-point mutations. Given the varying complexity, predicting binding affinity for single-point mutations may be less challenging and could potentially yield more accurate prediction results compared to multiple-point mutations. This raises the question: why not consider training separate models tailored for single and multiple mutation binding affinity prediction tasks, rather than using a single model for both?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
In this paper authors propose a novel, thermodynamics inspired, approach for predicting binding free energy change upon mutation (ddG) building, in particular, on the capabilities of protein inverse folding models. Validation of the method employs standard literature benchmark (SKEMPI v2 curating and integrating a vast number of experimental measurements of ddG across various types of proteins). Beyond that, authors demonstrate applicability of their method across several tasks (binding energy prediction, antibody optimisation and docking). The reported results, in general, significantly outperform a spectrum of modern methods presented in the relevant literature both in supervised and unsupervised context.

### Strengths
The paper is very well written and, I believe, easy to follow both for machine-learning and also, to large extent, for biology-oriented audiences thus extending its potential impact. The limitations and weaknesses are appropriately discussed. It focuses on relevant and important problem in protein science - predicting the energetic effect of mutation on the free energy of protein-protein complex formation. The contribution is clearly original, correctly references and builds upon several already existing contributions in the field (in particular - inverse folding models, direct preference optimisation). Most importantly, benchmark reports significant improvement across several investigated metrics on commonly-accepted dataset (SKEMPI) and described ablations and controls (folded structures) strengthen the confidence in the reported result.

### Weaknesses
- Method is structure based, it requires at least experimentally resolved or confidently predicted complex structure,
- The representation of protein is rather coarse, only backbone. Side-chain atoms and solvent molecules are omitted yet they are obviously important drivers of protein-protein interactions.
- No representation of dynamics (structures are represented as static snapshots), which can affect the method performance for mutations inducing significant conformational changes.
- The described method seems to excel at point mutations and there's a trend towards decreased performance in more complex multiple mutations.
Majority of those weaknesses are highlighted and discussed by the authors in the appropriate sections across the paper.

### Questions
- In section 4.4.3 authors utilise dataset from Shen et al (2022) however focus only on point mutations. This dataset is, I think, much richer and contains double and triple mutants from multiple optimisation rounds. I believe it would be important to expand this section to show proposed model performance more extensively. This, I believe, has a potential to boost the impact and trust in the model in a typical antibody design scenario. 
- Following on sec 4.4.3 - preference probabilities are a good metric but they in my view they are a bit abstract. I think a simpler metric of e.g. how the method ranks particular mutation would be more interpretable (as they relate to simple consideration of how many designs one can screen in the wet lab before finding a particular hit). 
- In the typical design scenario, as the problem is hard and the reported performance of the method is not perfect, one can also consider the uncertainty of the prediction which is an important and frequently used feature in e.g. protein folding models. It could potentially strengthen the paper if authors could discuss and provide more information on how uncertainty estimation could be introduced to the model.
- In appendix B - authors write "We compare BA-DDG with several representative methods under single-point, multi-point, and
all-point mutations on SKEMPI v2". It's not clear to me what is the difference between multi-point and all-point mutations. Is the all-point a union of point- and multi-point mutations (I'd assume so by looking at the following Table) ? For clarity authors can consider to explain this more in the paper. 
- The discussion about computational (non-ML) methods for ddG estimation is scarce. Even though it's purely ML venue, I miss a bit more thorough discussion of how the proposed method relates to force-field methods utilising more nuanced thermodynamical cycles / approaches like MM-GBSA/PBSA, FEP, TI, etc.

### Soundness
3

### Presentation
4

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
The paper presents Boltzmann Alignment, a novel approach for predicting changes in protein-protein binding free energy due to mutations. It utilizes pre-trained inverse folding models and introduces physical inductive bias through the Boltzmann distribution.

### Strengths
- The integration of Boltzmann distribution within the framework to enhance ∆∆G prediction is innovative and addresses a significant challenge in computational biology.
- The authors effectively showcase the versatility of their method in binding energy prediction, protein-protein docking, and antibody optimization, indicating its broad applicability.
- The paper is well-organized, and the results are presented clearly, making it easy for readers to follow the methodology and findings.

### Weaknesses
I haven't identified any significant weaknesses.

### Questions
Are there any specific types of mutations or protein interactions where the authors have observed the method to be particularly effective or challenging? Sharing such insights could help guide future research directions.

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
The paper proposes a novel and interesting method that leverages Boltzmann Alignment to establish a more sophisticated connection between inverse folding tasks and binding free energy (ΔΔG) prediction. Despite relying on somewhat idealized approximations, the method leverages a thermodynamic cycle and the principles of the Boltzmann distribution to incorporate both bound and unbound states of the protein complex, offering a physically motivated alignment technique that addresses limitations of traditional pre-trained inverse folding models.  Through evaluations on the selected SKEMPI v2 dataset, the paper demonstrates that the method achieves significant improvements over existing approaches in both supervised and unsupervised settings.  Overall, the paper provides a new perspective for integrating domain knowledge into alignment techniques.

### Strengths
1) The paper is well-written.

2) The approach achieves state-of-the-art results compared to baselines.

3) The paper effectively incorporates domain-specific priors, specifically leverages Boltzmann principles to connect energy with probability, along with the assumption that unbound states can be approximated as independent probabilities for each chain. Though this assumption is idealized, it still is an interesting approach that introduces a motivated alignment.

4) The paper demonstrates practical applicability on binding energy prediction, protein-protein docking and antibody optimization tasks.

### Weaknesses
1) The method makes strong assumptions, particularly in treating the unbound state as independent probabilities for each chain, which oversimplifies the inter-chain interactions. Specifically, the assumption that the unbound state can be modeled by simply masking the sequence and structure of the complex and inputting each chain independently into ProteinMPNN neglects potential weak, transient interactions between chains in solution. These interactions, while weaker than in the bound state, could still contribute to the overall free energy, and their omission could introduce inaccuracies, especially for systems where such interactions are non-negligible. Additionally, the predictions of inverse folding model’s do not fully align with the predicted probabilities (not the ground truth), introducing biases when single-chain probabilities are combined to approximate complex states. This approximation may result in significant deviations in some situations.

2) The method has only been validated on a limited dataset, which lacks sufficient evidence to demonstrate the generalizability of the approach and its underlying assumptions. The SKEMPI v2 dataset, while a standard benchmark, may not fully represent the diversity of protein-protein interactions and binding scenarios. The method's performance on other datasets, particularly those with different types of protein complexes or binding interfaces, remains unclear. This limited validation raises concerns about the robustness and broad applicability of the proposed approach.

3) It seems that the paper lacks sufficient discussion on how improvements in the inverse folding model would translate to gains in this approach. It’s also unclear which specific module in this sophisticated approach contributes most significantly to the information gain. The paper does not provide a detailed ablation study to quantify the contribution of each component, such as the Boltzmann alignment or the thermodynamic cycle integration. Without such analysis, it is difficult to assess the actual impact of each design choice and to determine the most critical factors driving the observed performance improvements.

### Questions
1) Could the authors explain the reasons for the relatively low MAE reported in Table 2?

2) Could the authors clarify how they determined the unbound state approximation for independent chain probabilities (Equation 9)?  The paper provides some explanation on this point, but it lacks sufficient detail.

3) The transformation between energy and probability, along with the approximation of unbound state probabilities, partially explains the high correlation between the inverse folding task and ΔΔG prediction. However, within the neural network, the sophisticated design of model doesn’t appear to provide additional information gain. 

Given the strengths of this paper, I would consider raising my score if the authors can address my concerns.

### Soundness
3

### Presentation
3

### Contribution
4
