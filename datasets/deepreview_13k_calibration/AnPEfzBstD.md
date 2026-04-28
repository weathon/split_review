# Dimension Debate: Is 3D a Step Too Far for Optimizing Molecules?

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
The discovery of new molecular materials with desirable properties is essential for technological advancements, from pharmaceuticals to renewable energy. However, the discovery process is arduous, requiring many trial-and-error cycles of complex and expensive experiments. Bayesian optimization (BO) is commonly used to find and screen candidate molecules efficiently.  However, it is unclear how to choose the right molecular representations for a Bayesian surrogate model: While molecules are 3-dimensional in nature, 3D features in BO have largely been underexplored. Indeed, 1D and 2D molecular features---which incur loss of information---are typically used.  In this work, we study this discrepancy: Why have 3D features been overlooked for BO in materials discovery? To this end, we evaluate 3D features against standard lower-dimensional features.  We assess their optimization performance on real-world chemistry datasets, considering both various settings such as low- & high-data regimes and transfer learning, and different types of Bayesian surrogates. This amounts to the evaluation of 35 different setups per dataset, totaling over 2100 distinct runs. Our large-scale work provides insights and modeling guides to chemists and practitioners on the trade-offs between 1D, 2D, and 3D representations, in a bid to further accelerate materials discovery.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work, the authors study the discrepancy between multi-level features in BO: Why have 3D features been overlooked for BO in materials discovery? The authors evaluate 3D features against standard lower-dimensional features. This amounts to the evaluation of 35 different setups per dataset, totaling over 2100 distinct runs. Furthermore, the authors summarize the characteristics of 3D features based on these experimental results.

### Strengths
1. A comparative study of 2D and 3D molecular features is valuable.

### Weaknesses
1. The biggest problem with this paper is the lack of innovation and insufficient contribution. The authors mainly compare the differences between features of different levels. This is a classic problem. Apart from that, there are no other contributions or innovations in this paper.

2. The author's analysis of 2D and 3D is not comprehensive. Physically speaking, 2D and 3D focus on different levels of physical properties. 3D features are primarily aimed at representing microscopic characteristics (quantum mechanical features), and for the same molecule, the microscopic characteristics can vary with different conformations, making 3D features more suitable for representing microscopic properties such as energy or force. 2D features focus more on macroscopic properties; they cannot represent the differences between conformations and are more suitable for describing some macroscopic or equilibrium conformational properties, such as density and energy of equilibrium state. For example, datasets like QM9 only contain steady-state molecules, which cannot showcase the advantages of 3D features. It is recommended that the authors further compare on the MD17 dataset which has non-equilibrium structures.

3. Why focus on Bayesian networks? Molecular representation is a very general technology, and the experiments in the paper mainly target property prediction. There is no interdependent relationship with BO, and the authors have not provided any mechanisms unique to Bayesian networks for these representations.

4. Controlling the parameters of all models at the same order of magnitude may not be fair, as different models have different expressive capabilities and dependencies on parameters. For example, a 1.5M equiformer is relatively small, and its prediction results are not saturated. Additionally, the authors should also specify the configurations of the baselines in the paper, such as the number of layers, hidden units, etc.

### Questions
See weeknesses.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work explores the effectiveness of different molecular representations for materials discovery tasks using Bayesian optimization (BO). The authors systematically benchmarked 1D, 2D, and 3D representations, using popular probabilistic surrogate models like Gaussian Processes (GPs) and Bayesian Neural Networks (BNNs). They investigated the trade-offs between computational cost and predictive accuracy, finding that large language models (LLMs) consistently outperformed 2D and 3D models, highlighting the advantage of simpler representations for most BO tasks. They also examined the influence of sample size and transfer learning on model performance, concluding that 3D representations require larger datasets to match the performance of 2D models, while transfer learning shows promise for improving model adaptability across various tasks.

### Strengths
● The research conducted a comprehensive evaluation of 1D, 2D, and 3D molecular representations across four datasets (QM7, QM9, MoleculeNet, and GEOM DRUGS), involving over 2100 distinct runs. This large-scale approach provides robust insights into the performance of different representation dimensionalities.

● The study considered various realistic scenarios, including low- and high-data regimes, transfer learning, and different Bayesian surrogate models (GPs and Bayesian NNs). This multifaceted approach enhances the practical relevance of the findings.

● The study investigated the impact of training set size on model performance, revealing that 3D models require significantly more samples than 2D models to achieve comparable results. This analysis highlights the data efficiency challenges associated with 3D representations.

● The research examined the benefits of transfer learning, finding that it offers a viable path to generalizing across multiple molecular properties with minimal loss in accuracy. This insight suggests the potential of transfer learning in both 2D and 3D models

### Weaknesses
● The study focused on molecular property prediction tasks where 2D representations proved largely sufficient. Future research could explore more complex tasks like protein docking or molecular dynamics simulations where 3D information might be more critical.

● Even though this study is large-scale and looks into different BO settings, it is quite restricted in terms of the task, models, and dataset types making it hard to have a generalized conclusion. For ex, the paper mentions - "In more complex datasets, the improvement of 3D models is minimal, indicating that 2D models are sufficient and more efficient." This seems like a generalized statement with limited evidence from the complexity of the dataset used. Dataset complexity can be defined in many ways - task, number of elements, system sizes, dataset sizes.

### Questions
● The distinction gets a little confusing with LLMs for certain cases. If an LLM for example learns a representation directly from a cif file (or equivalent) for materials (or molecules), would that be 1D or 3D? LLMs have seen potentially more data during pretraining unless they have been trained from scratch autoregressive on just smiles strings.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores the use of 3D molecular representations in Bayesian optimization (BO) for materials discovery and the experimental results question if incorporating 3D features, which capture the spatial structure of molecules, could improve the efficiency and accuracy of BO models. Given the large-scale comparison testing 1D, 2D, and 3D representations across multiple datasets, the authors found that 3D representations often fail to outperform simpler 2D models, especially in smaller datasets, where 2D features prove more data-efficient and computationally feasible. While 3D models show some improvements with larger data, the gains are limited compared to the computational cost. The authors find that transfer learning can effectively generalize models trained on specific properties to other tasks, with 2D models still generally outperforming 3D ones. Their findings provide guidelines on choosing dimensionality in BO for molecular discovery, emphasizing the practicality of 1D and 2D features for many tasks.

### Strengths
1. The paper addresses an underexplored but important question in molecular optimization: the efficacy of 3D molecular representations in Bayesian Optimization. While most research traditionally employs 1D and 2D features, this work systematically evaluates 3D representations, making a strong case for re-examining assumptions about molecular representation choices in BO.

1. The authors present a thorough and carefully designed benchmarking study, assessing various molecular representations across multiple datasets and experimental settings. In addition, including transfer learning setups and different sample complexities enhances the robustness of the findings.

1. The paper is well-structured, making it easy for readers to follow the study’s rationale and outcomes. The use of illustrative figures, such as those comparing GAP performance across 1D, 2D, and 3D models, helps to contextualize findings visually.

### Weaknesses
1. The paper provides the experimental results demonstrating that the 1D and 2D features capture enough information for BO optimization. However, this does not necessarily indicate that 3D information is too far for optimizing molecules. There are a lot of other generative models for molecules that utilize 3D information and achieve SOTA performance. In addition, generative models could be conditioned on molecular properties to generate novel molecules with desirable properties out of the pool. Therefore, the missing of comparison to those models weakens the argument that "3D information is too far for optimizing molecules".

2. The BO optimization workflow requires a predefined pool of candidates for searching, which may limit its capability to discover novel molecules compared to generative models based on Diffusion or Flow Matching. 

3. The ignorance of 3D information may result in poor model performance when 3D geometric information like symmetry plays a pivotal role, e.g. molecular crystals. Therefore, this might be a limitation for further applications in molecule and material discovery. 

4. The choice of the model architectures for 1D, 2D, and 3D features is not fully justified. Without experimental results on more model architectures, the conclusion that "3D information is too far" may not be model-agnostic and may not hold true when using another model, even though Equiformer-V2 is indeed the SOTA model on many molecule tasks.

### Questions
1. Have the authors tried model architectures other than MolFormer, MPNN, and Equiformer-V2 and evaluated their performance in optimizing molecules? Besides, I'm wondering why MPNN is used as the 2D model since MolFormer and Equiformer-V2 are among the SOTA models in their domain while MPNN is not, although it is the foundation of many SOTA 2D graph models. 

1. For MolFormer and Equiformer-V2, do you use the pretrained model checkpoints for fine-tuning or train the model from scratch? If using the pretrained model, this might result in an unfair comparison as the pretrained models learn useful representation from data out of the training set.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper reports over 2100 experiments with 1D, 2D and 3D descriptors for Bayesian Optimisation (BO) to identify optimum molecules from a dataset. The datasets and corresponding tasks are:
1) QM7, 7165 molecules, atomisation energies
2) QM9, 133 885 molecules, HOMO-LUMO gap
3) GEOM-MoleculeNet, 28 295 molecules, absolute energy
4) GEOM-DRUGS, 317 928 molecule, absolute energy

The authors claim that:
- 1D features perform best in terms of identified optima and sample efficiency
- 3D features do not improve over 2D features
- Transfer learning appears to only offer a modest improvement

### Strengths
**Originality**
The benchmark here is original in the choice of datasets and tasks and how the authors compared different ways of featurising molecules. The comprehensiveness also adds to the originality.

**Quality**
The paper performed 2100 runs and 35 different setups, making the benchmark comprehensive. Most of the setup is of quality, such as the aggregation of the results using the GAP metric, the used surrogates, using replications.

**Clarity**
The paper is mostly clear in explaining the methods and the results. The blue call-outs stating the main claims helped me read the paper. 

**Significance**
Understanding how to best use deep learning to represent molecules is an important research question with application in predicting and generating new compounds.

### Weaknesses
 **Methodological concerns regarding the 1D LLM featurizer**
The LLM 1D featuriser seems to contain a methodological flaw. When reading the text, I was confused on how the authors pooled the features created by MolFormer. The Appendix stated that the model was prompted with a text prompt, which I found odd since MolFormer is trained only on SMILES.

This led me to reproduce the calculation of the 1D embeddings. Using the provided code, it seems that the authors calculate the embeddings as follows, here illustrated using the SMILES string "NCCO"

1) Create the text string `The estimated total tnegry in Hartree of the molecule NCCO is: ` (the typo `tnergy` is taken from the provided code, line 402 of LLMmain.py (https://anonymous.4open.science/r/3D_Bayes-0F8F/LLMmain.py).
2) Tokenise the string with MolFormer. Importantly, the MolFormer tokenizer was trained only on SMILES strings so the tokens created are decoded to the string `<bos>sonnoocNCCOs<unk><eos>`. 
3) Forward pass the tokens to MolFormer and output the aggregated embeddings of the last Transformer layer.

The prompt here results in a systematic error where additional tokens are added to the SMILES string embedded by MolFormer. It's interesting that performance is still high despite this issue, which may be because such a systematic modification is ignored by the fine-tuning process.

Still, the text refers to MolFormer as an LLM (Large Language Model) and the code used it as an LLM without checking that it cannot tokenise natural language, which makes me concerned about the soundness of the paper's results, and how someone reading the paper in less depth may interpret the results.

**Limited generalisability of the conclusions**
While benchmarking efforts such as these are interesting, they are hard to generalise to recommendations of where to use 1D, 2D and 3D features in a practical discovery setting. A more valuable claim would be either principles or statistical methods to reliably identify where 1D, 2D and 3D features are performant. The paper is close to doing this - e.g. one could run 100-200 samples with all 3 methods, look at certain convergence metrics and then run the rest of the Bayesian Optimisation loop using only the most performant features. What is the role of the acquisition function here - are certain acquisition functions _better_ for early identification of performant features?

Creating methods such as these would significantly improve the paper's use in practice.

**Reason for recommendation** Given this methodological flaw and limited generalisation, I recommend rejection at this moment. However, I am keen to understand more about the calculation of LLM features and how the claims may generalise in the discussion with the authors.

### Questions
1) Were the molecules in GEOM unique molecules or different conformers of the same molecule? I assume this will affect the performance of the 1D and 2D features as those cannot distinguish between conformers. It's also an important point to clarify in the paper.

2) Can you please clarify the calculation of the LLM features (see weaknesses above)

3) In Figure 3, why is the purple line (LLM) only visible in the "Aggregated Performance" column and not in the GP and LLA column?

4) Can the claims generalise to e.g. recommend which descriptor to use based on a few samples?

### Soundness
2

### Presentation
3

### Contribution
2
