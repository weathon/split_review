# Self-Supervised Diffusion Processes for Electron-Aware Molecular Representation Learning

- Decision: Accept
- Scores: 6, 8, 6, 8, 6

## Abstract
Physical properties derived from electronic distributions are essential information determining molecular properties. However, the electron-level information is not accessible in most real-world complex molecules due to extensive computational costs of determining uncertain electronic distributions. For this reason, existing machine learning methods for molecular property prediction have remained in regression models on simplified atom-level molecular descriptors, such as atomic structures. This paper proposes an efficient knowledge transfer method for electron-aware molecular representation learning. To this end, we devised a self-supervised diffusion method that estimates the electron-level information of real-world complex molecules from readily accessible incomplete information in public chemical databases. The proposed method achieved state-of-the-art prediction accuracy on extensive real-world molecular datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes to enhance molecular representation learning by incorporating electron-level information via diffussion process, which eliminates the need of expensive quantum calculations. The proposed methods are evaluated on real-world experimental property prediction datasets to show the applicability and effectiveness, and also on simulation dataset such as QM9 for further discussion. Several analysis are conducted to assist the findings.

### Strengths
- The paper proposes a new perspective on enhancing molecular representation learning by leveraging the diffusion process. 
- The proposed method save the computational costs on quantum calculations.

### Weaknesses
 - The decomposed substructures serve as the noise, what is the motivation and reason of such implementation? Why not insert noise to the molecules? The authors have defined such, but there are not sufficient explanations of why doing so.

 - The authors mention that FFSEC has low calculation accuracy, then why still use it to calculate coordinates? Why not use commonly used Rdkit to generate?

 - How to define the substructure size? The paper mentions that EFG-based method is used for decomposition, however they also remove the large molecules in QM9 due to the redundancy?

 - Why only $R^2$-scores and F1 scores are reported? The commonly used evaluation metrics like MAE/RMSE and AUC/accuracy are not reported. The reported results are also not very significant compared with baselines, such as ESOL, ADMET, LC50.

 - How is the 5-fold leave-one-out cross-validation implemented? Is it leave one fold out? Why not follow the standard evaluation method? What about the split type? Is it scaffold or random split?

 - Have the authors compared with methods that utilize both 2D and 3D graphs, like 3d infomax [1] and GraphMVP [2]?

 - The proposed method seems not universal as it is mentioned that only under certain circumstances the method would work well, like relatively large molecules. I am also confused about the term of electron, it seems that the proposed method is based on substructures, why is it called electron-aware? 

 - The paper needs proofreading, i.e., some tense is not consistent. Some contents show conflict. For example, in the related work SchNet is introduced under the 2D-GNNs, while it is actually 3D GNN, where the authors also mention such in the Competitor Methods part.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a new approach for electron-aware molecular representation learning. The key motivation is to introduce electron-level information into the learning process. The framework is formulated as a self-supervised diffusion process maximizing $log p(y,s,G)$, which is implemented as follows: (1) the input 2D molecular graph is decomposed based on extended functional groups (EFGs) to obtain a noised adjacency matrix $G_T$; (2) for each of the components, quantum-chemical properties are retrieved from a support set (a subset of QM9 in the experiments) as noised electron-level information $s_T$; (3) the model is then required to denoise the adjacency matrix and the electron-level information and predict the final property y simultaneously.

The proposed method is evaluated on several experimental molecular property prediction datasets, showing higher prediction accuracies than existing methods. The proposed method is also shown to have better generalization capabilities by an experiment simulating data-scarce scenarios. An ablation study on model components is provided. The authors also provide experimental results for different electron-level features, different external support datasets, execution time, etc.

I feel that the paper is of good quality overall, but there are still some points that need clarifications and discussions.

### Strengths
* The paper is well motivated. I agree with the authors that a molecular representation model should be electron-aware. The proposed method implements this without requiring ground-truth labels for whole molecules, which is novel and interesting.
* The paper is also easy to understand in general. I was able to follow the paper with most of my questions answered in the text.
* Probably thanks to the fast training/inference time, the evaluation is very thorough and comprehensive. The proposed method, DELID, not only shows higher prediction accuracies than existing methods, but also exhibits lower computation consumption and better generalization capability. The comparative analysis on different feature selections, different support datasets and different decomposing methods makes one believe the current design is the optimal.
* The provided code is clean and easy to follow, with dataset files directly included. This gives a good impression that the work can be easily reproduced using the provided code.

### Weaknesses
 - Interpreting $s_T$ as electron-level information could be confusing. $s_T$ of shape $N_{comp} \times m$, which are pre-calculated properties for the decomposed substructures, actually seems more like substructure-level information rather than electron-level information. First, the only reason why the features can be vaguely regarded as containing information about electrons is that they are computed using quantum chemistry methods like DFT. However, these methods run on conformations, not on 2D graphs. The retrieval process for $s_T$ actually links a 2D substructure to a 3D conformation, and the latter could even be of a similar but different molecule. Second, the used features are mostly molecular-level observables aggregated from electron density. These two reasons make $s_T$ less physical and less suitable to be regarded as electron-level information.
- $s_t (t = 0, 1, ..., T - 1)$ is not only unknown, but also hardly defined. I think it can only be interpreted as latents, not as electron-level or substructure-level information. For example, the meaning of $s_0$, an $N_{comp} \times m$ tensor, is not clear given that the components are already connected in its corresponding graph $G_0$. The diffusion process is defined on these ill-defined $s_t$ values, which makes the physical interpretation of the method questionable.
- The method is called self-supervised diffusion, while the current implementation seems to rely on the availability of $y$ . The core of the method, the diffusion process on $s$, appears to be conditioned on the target property $y$, thus it is not truly self-supervised. This dependence on $y$ for the diffusion process on $s$ undermines the claim of self-supervision.

### Questions
- Given the points mentioned in Weaknesses, it is then unlikely the improvements of the proposed method come from a more physical design. Could you provide an intuitive explanation about *why* do the improvements occur?
- A few important implementation details seem to be missing from the current version of paper. For example, what exact value does $T$ have?
- Is $y$ required for the model to learn good molecular representations? If it is required, do models trained on different datasets predict similar $s_0$?
- In section 4.4, the ablation study on DELID, could you also list the `#params` of the variants? What happens if the `#params` of the ablated variants match that of the complete DELID?

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
4

### Summary
The paper introduces a method called DELID (Decomposition-supervised Electron-level Information Diffusion) for molecular representation learning. DELID utilizes molecular decomposition to generate substructures and matches them with a subset of the QM9 dataset to retrieve electron-level information. The method comprises two diffusion models: one estimates the original molecular graph from the decomposed subgraphs, and the other estimates the electron-level information from the electron-level features of these substructures. Finally, DELID employs these estimates to predict molecular properties. This approach allows DELID to learn electron-aware molecular representations and predict properties of complex molecules effectively, leveraging both structural and electronic information.

### Strengths
This paper introduces a self-supervised diffusion models method to represent molecules by estimating electron-level information in complex molecules. The proposed method is efficient as it does not require expensive quantum mechanical calculations to estimate electron-level information. DELID achieves state-of-the-art prediction accuracy on extensive real-world molecular datasets.

### Weaknesses
1. The performance of DELID is dependent on the external quantum mechanical calculation datasets, such as QM9. The distribution and the quality of such datasets may influence the ability of the models. 
2. After breaking down the molecule into substructures, the electronic information of each part is calculated, and thus the interactions between the parts can be neglected. For example, the electronic shift of two neighboring functional groups. It is doubtful that the diffusion model is able to construct such interactions well.
3. The decomposition from complex to simple molecules is unique, but the process of denoising from simple molecules to generate the original molecule is not unique, e.g. isomers. This is not well avoided by the electronic information generated using the self-supervised method.

### Questions
1. Diid the authors use only the middle layer embedding of the diffusion model in their predictions or did they also use the final estimated electronic information?
2. The difference between DELIDqm and DELID in table3 makes me wonder if the electron level of the diffusion model is well constructed for electronic information of complex molecules. Can the authors provide the difference between the final estimated electronic information and the information obtained from the dft calculations?
3. What is the difference between the molecules generated by the diffusion model and the original molecules?
4. Can the embedding vectors generated by the diffusion model  distinguish different molecules? For example using t-sne to visualize the embedding of a certain dataset and distinguish different categories of molecules with molecular weights or whether they are aromatic molecules?
5. How to construct the molecular graph and how to combine several subgraphs to generate a graph? How to represent the electron information from the QM9?

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
3

### Summary
The authors propose a method for learning molecular representations using self-supervised diffusion processes. This method can learn an "electron-aware" representation without requiring ground truth electron properties of the complete molecule. This is achieved by leveraging the synergy between the diffusion process at the graph level and the electron-level information. Additionally, by decomposing the complete graph into subgraphs (molecular fragments), the reverse diffusion process can utilize subgraph information readily available in chemical databases. Lastly, the method showed superior performance compared to state-of-the-art methods in various downstream tasks.

### Strengths
- Originality: The idea of learning electron-aware molecular representation without needing ground truth electron properties is novel and significant. The method is also original in how it leverages the synergy between the diffusion process and electron-level information.

- Quality: The method is well designed, and the experiments are thorough.

- Clarity: The paper is well written and easy to follow.

- Significance: The method showed superior performance on various tasks and can inspire future research in the field.

### Weaknesses
 - The authors provide details on the diffusion process, but the actual process of predicting the properties is not described in enough detail. How are the learned representations used to make final property predictions?
- In Table 1, the benchmark methods are mostly GNNs and XGB. It would be better to compare with more diverse methods, such as Fingerprint + MLP/SVR, or other methods representing diverse paradigms.



### Questions
- Is there a typo in Equation 1? Should it be t=1 or t-1 in the denominator?
- Regarding the construction of s_T: Some properties, such as energy, are extensive properties, so the quantity depends on molecule size. Retrieval using Tanimoto similarity does not consider molecular size. If the retrieved fragment and the actual fragment have different sizes, the property could differ significantly. Will this negatively impact model performance? Additionally, is there a list of the 19 features used to construct Q_k? Is the final $s$ just the 19 features for the complete molecule?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method that uses two diffusion models to learn the representations of molecules and electron information, then the representations are used for property predictions. The novelty of this work is to estimate electron information from existing public database, without expensive ground truth labeling, which is achieved by a self supervised training from the molecular diffusion model. 

The authors performed comprehensive experiments with relevant baseline models, and demonstrate the state of the art performance of the proposed model on the experimental dataset that contains large molecules and experimental measurements.

### Strengths
- Originality: This paper proposes a novel approach that utilizes the accessible electron information of subgraphs (or building blocks) of a molecule from public database, to enhance the representation and property prediction. The self-supervised learning also shows a good theoretical and algorithmic ground, so as to solve the difficulties of the need for expensive calculations for ground truth electronic structure.
- Quality: This paper has demonstrated solid theoretical derivations, and has performed comprehensive numerical experiments on multiple tasks, comparisons with other models and ablation studies.
- Clarity: The figures and formulations are clear and illustrative. The text has good clarity.
- Significance: This work shows a potential way for addressing small scale molecular dataset.

### Weaknesses
 - Even though it is a good use of publicly available electronic structure for subgraphs/fragments, the final electronic information $s_0$ is only an estimation of the ground truth. And in fact, it is not guaranteed to be a good estimation, as the electronic structure of a molecule with different fragments covalently bonded can be very different from mixing the electronic structures of different individual isolated fragments. Therefore, physically, this self supervised learning, which is essentially trying to mix the electronic information of fragments in the same way as mixing the structural information, is not very meaningful. Specifically, the assumption that the electronic properties of a molecule can be accurately represented by a linear combination or simple aggregation of its fragment's electronic properties is a strong simplification that lacks a strong theoretical basis in quantum chemistry. The interactions between fragments, which significantly alter the electron density and energy levels, are not adequately captured by this approach.
- Based on the point above, I would expect that the information mostly gained from the electronic representation will come directly from $s_T$ which are the electronic features of the fragments, instead of from $s_0$. And this can be verified from Table 3, the performance difference between "DELID_qm" and "DELID" is actually very small and generally within the error range. This suggests that the diffusion process for $s$ may not be contributing significantly to the final performance, and the model's performance is primarily driven by the initial fragment electronic features $s_T$. The marginal improvement gained by the diffusion process could be due to the increased model complexity rather than a genuine learning of electron-level information.
- The benchmark dataset used here is a small dataset, as it is an experimental dataset and also includes large molecules. But for some other competitor models, it makes sense that they don't perform that well if they are trained from scratch for this small dataset. That does not mean that the method proposed here is really SOTA, as I would expect those competitor method can potentially perform very well with a pretrain-finetune workflow (i.e. pretrained on a large scale simulated datasets, and then finetuned for the small experimental dataset). The lack of comparison with pre-trained models on larger datasets limits the claims of state-of-the-art performance. The authors should demonstrate that their method outperforms existing models when these models are trained with a pre-train and fine-tune approach, which is a common practice for small datasets.

### Questions
- It is not so clear to me what parts are built with a separate neural network model. For example, my understanding is $\log p(A_{t-1}|A_t)$, $\log p(s_{t-1}|s_t, A_{t-1})$, $\log p(A_{t-1}|s_t)$ are parametrized as separate models. It will be good if the authors can clarify and improve the notations.

### Soundness
4

### Presentation
4

### Contribution
3
