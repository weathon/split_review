# Subgraph Diffusion for 3D Molecular Representation Learning: Combining Continuous and Discrete

- Decision: Reject
- Scores: 3, 5, 6, 6

## Abstract
Molecular representation learning has shown great success in AI-based drug discovery. The 3D geometric structure contains crucial information about the underlying energy function, related to the physical and chemical properties. Recently, denoising diffusion probabilistic models have achieved impressive results in molecular conformation generation. However, the knowledge of pre-trained diffusion models has not been fully exploited in molecular representation learning. In this paper, we study the ability of representation learning inherent in the diffusion model for conformation generation. We introduce a new general diffusion model framework called MaskedDiff for molecular representation learning. Instead of adding noise to atoms like conventional diffusion models, MaskedDiff uses a discrete distribution to select a subset of the atoms to add continuous Gaussian noise at each step during the forward process. Further, we develop a novel subgraph diffusion model termed SUBGDIFF for enhancing the perception of molecular substructure in the denoising network (noise predictor), by incorporating auxiliary subgraph predictors during training. Experiments on molecular conformation generation and 3D molecular property prediction demonstrate the superior performance of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies 3D molecular graphs, and performs diffusion on a subgraph sampled by a learnable mask vector. Then the major work is to fulfill the training and sampling of the diffusion model based on the mask strategy. The developed methods are applied to both molecular generation tasks and self-supervised learning tasks.

### Strengths
A technical contribution in this paper could be - fulfilling the training and sampling of diffusion models on a subset of a graph with reasonably rigorous math. Even though the subgraph (I would call subset) in the paper is not convincing, the technical implementation would be at least inspirational.

### Weaknesses
1. My major concern is that, the overall motivation is not convincing or valid. The authors think diffusing individual atoms in a molecule may constrain the capacity of the models, as the connections among these atoms can be important. However, the methods tend to be a mask to choose a subset of atoms, which can be anywhere of the original graph and disconnected at all. As a comparison, there exist a bunch of studies that consider REAL subgraphs (like motifs, functional groups etc) in generation by leveraging domain knowledge. The motivation of these existing works is more convincing and valid.

2. The title and scope of the paper are a little weird. The work is actually not regular 3D molecular representation learning, but for molecular generation and self-supervised based representation learning. I suggest the authors consider this in the revision.

3. Experimental results on GEOM-QM9 are very marginal, especially on the COV-P and MAT-P metrics where GeoDiff is much better. I also have concerns about the experiment setting that both generation and representation learning are conducted. However, for each one, the setup (like datasets)  is not sufficient or the results are not strong enough compared to baseline methods. A better solution is to only study one problem (like generation) with sufficient and strong results. This is also related to the title and scope of this work.

4. To me, the implementation of the training and sampling of diffusion models on a subset of a graph is not trivial, but there exist several studies for similar purposes. The authors may want to clearly state the unique **technical** contribution compared with these studies.

### Questions
See Weakness. A major consideration during revision is a valid and convincing motivation.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposed MaskedDiff and SubgDiff, where molecular substructures are preserved during the diffusion process. With this additional inductive bias and tailored diffusion process (taking masking into consideration), the model shows improved performance over existing models on the GEOM dataset.

In general, I find the substructure-preserving diffusion model interesting, yet the results are not convincing enough to demonstrate the superiority of masked diffusion compared to vanilla diffusion models with a much simpler formulation. Please see my concerns below.

### Strengths
- Preserving molecular fragments/motifs during the diffusion process helps the model better capture molecular structures.
- The authors performed both molecular property prediction and conformation generation benchmarks, showing that the proposed method is beneficial for representation learning.

### Weaknesses
 - The number of diffusion steps is the same as that in GeoDiff, i.e., 5000 steps, which is quite a lot. Given this large amount of diffusion steps, the alternating update scheme might work well. However, I am not sure if using more cost-effective sampling methods would still benefit from masked diffusion?
- Taking masking into consideration makes the diffusion process more complicated by design. Therefore, one should show that these extra modeling complexity is worthwhile by showing more promising performance on various downstream applications. The marginal performance gain on the GEOM-QM9 dataset (not GEOM-Drugs) is not convincing enough.

- From Table 5 in Appendix, the proposed method is inferior to GeoDiff across all evaluation metrics. Minor performance gain on GEOM-QM9 may not be that significant since the target molecules are small in general. That being said, MaskedDiff cannot outperform SOTA models while introducing extra complication during modeling.

- Diffusion models are known for their slow sampling process. Here the large number of steps (i.e., 5000) would make the sampling process particularly inefficient. For instance, for protein conformation generation, the number of steps is typically 200 or 500. Upon reducing the number of diffusion steps, would the alternating update scheme still work?

- Incorporating a well-designed prior distribution could also reduce the challenging learning task, e.g., [EigenFold](https://arxiv.org/abs/2304.02198). The model should be able to figure out the correlation between data dimensions during training. Would this be more effective and easier to learn than introducing masks for the diffusion process?

- Minor: Conclusion, "European space", fix typo.

### Questions
- From Table 5 in Appendix, the proposed method is inferior to GeoDiff across all evaluation metrics. Minor performance gain on GEOM-QM9 may not be that significant since the target molecules are small in general. That being said, MaskedDiff cannot outperform SOTA models while introducing extra complication during modeling.

- Diffusion models are known for their slow sampling process. Here the large number of steps (i.e., 5000) would make the sampling process particularly inefficient. For instance, for protein conformation generation, the number of steps is typically 200 or 500. Upon reducing the number of diffusion steps, would the alternating update scheme still work? 

- Does other sampling techniques, e.g., probability flow ODE, work for the proposed method?

- Incorporating a well-designed prior distribution could also reduce the challenging learning task, e.g., [EigenFold](https://arxiv.org/abs/2304.02198). The model should be able to figure out the correlation between data dimensions during training. Would this be more effective and easier to learn than introducing masks for the diffusion process?

- Minor: Conclusion, "European space", fix typo.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a new molecular generation and representation learning method. The paper first proposed MaskedDiff for better representation learning for molecular graphs, and then further propose SubgDiff to make the model capable for molecule generation. Experiments demonstrate the effectiveness of the method for both generation and property prediction.

### Strengths
1. Presentation is clear and both method and experiment are well explained.
2. The author provides good mathematical details and analysis for the proposed method.
3. The idea overall is interesting, where the author draw inspiration from subgraph-based representation learning method and adopt it address the generation task.

### Weaknesses
The main weakness in my mind is about the performance. The generation quality in Tab1 and Tab5 seems even worse than the baseline GeoDiff, and the property prediction results in Tab2 is also not consistently better than baselines and GeoDiff.

### Questions
I may missed but didn't ind it: what's the number of diffusion timesteps T for each experiment's config? This is important for audience to have a better understanding of the method's sampling efficiency.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work proposes a mask diffusion model for 3D molecular representation learning and the conformation generation task. The proposed diffusion model selects a subset of atoms and adds noise from a Gaussian distribution to the atom's 3D coordinates. In the reverse process, a mask predictor is used to recover the 3D information of the noisy subgraph. Finally, the proposed diffusion model is validated using the QM9 conformation generation and quantum property prediction tasks.

### Strengths
First, the study uses a diffusion model for molecular representation learning based on 3D coordinates. The topic is attractive and holds promise in many important applications for drug discoveries.

Second, the proposed mask diffusion model on subgraphs is novel. The experiment results look good.

Third, the proposed method has a good theoretical motivation.

### Weaknesses
Weakness 1: The presentation of the work could be improved. The use of mathematical symbols is burdensome and difficult to follow. Explanatory figures, such as Figure 4, are not self-explanatory due to numerous unexplained symbols. Algorithm 1 is helpful for readers trying to understand the method's training, but it lacks many details. For instance, the roles of the mask predictor and the noise predictor are unclear, and it's not specified whether they are distinct networks or share parameters. Furthermore, the specific neural network architectures used for these components, as well as the GNN encoder, are not clearly defined, making it difficult to reproduce the results or understand the method's complexity.

Weakness 2: The proposed method has only been validated on QM9, which encompasses four types of atoms. Given that the periodic table consists of 118 elements, the paper doesn't address the extent to which the model can generalize in real-world scenarios. The limited scope of the validation raises concerns about the model's applicability to more complex molecular systems with diverse atomic compositions and bonding patterns. It is unclear if the model can handle molecules with a wider range of chemical properties and structural features.

### Questions
Q1: Can the diffusion model be adapted to accommodate node features and graph structures? How dependent is the model on the graph structure?

Q2: Could the model be used for other important tasks such as the datasets from MoleculeNet [1] or OGBG [2]?

Q3: Can the model be compared against other graph representation learning methods for molecular graphs that do not process 3D coordinates? Such a comparison could more effectively underscore the significance of explicitly incorporating 3D coordinates in practical applications.


Ref.

1. MoleculeNet: a benchmark for molecular machine learning. Chemical Science.

2. Open Graph Benchmark: Datasets for Machine Learning on Graphs. NeurIPS 2020.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
