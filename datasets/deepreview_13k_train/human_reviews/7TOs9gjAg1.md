# Removing Biases from Molecular Representations via Information Maximization

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
High-throughput drug screening -- using cell imaging or gene expression measurements as readouts of drug effect -- is a critical tool in biotechnology to assess and understand the relationship between the chemical structure and biological activity of a drug. Since large-scale screens have to be divided into multiple experiments, a key difficulty is dealing with batch effects, which can introduce systematic errors and non-biological associations in the data.
We propose \name, an \textbf{Info}rmation maximization approach for \textbf{CO}nfounder \textbf{RE}moval,
to effectively deal with batch effects and obtain refined molecular representations. 
\name \ establishes a variational lower bound on the conditional mutual information of the latent representations given a batch identifier. It adaptively reweighs samples to equalize their implied batch distribution. 
Extensive experiments on drug screening data reveal \name's superior performance in a multitude of tasks including molecular property prediction and molecule-phenotype retrieval. 
Additionally, we show results for how \name \ offers a versatile framework and resolves general distribution shifts and issues of data fairness by minimizing correlation with spurious features or removing sensitive attributes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors tackle the problem of removing batch effect in high-throughput drug screening.
The proposed method InfoCORE leverages a tractable information theoretic framework by establishing a variational lower bound on the conditional mutual information of some latent representation (obtained by a NN) given a "batch identifier" (i.e. the batch effect).
The method is rather generic in the sense that it can handle multiple modalities such as gene expression levels, imaging profiles, along with the chemical structure of the drug at hand.
Unlike many methods that try to learn a generic representation, as a pre-processing task, InfoCORE trains end-to-end for a final task (e.g. molecular property prediction, molecule-phenotype retrieval).
While very closely related to existing frameworks such as CLIP and CCL, InfoCORE's main contribution is to adaptively reweigh negative samples (in a contrastive learning sense) in the objective, so as to make better use of low sample sizes for rare conditions.
While adaptively adjusting the sample weights, the resulting approach is proven to be optimizing a lower bound for the conditional mutual information.
Last, the method is benchmarked against its very related methods CLIP and CCL on simulated data, representation learning of small molecules and on standard UCI datasets for fairness of the learnt representation.

### Strengths
While building on already very established work, InfoCORE is addressing an important shortcoming of InfoNCE and the high variance of the sample approximation of the log partition function.
This shortcoming is particularly problematic in the scenario where samples are coming from different batches and some of them have few observations, which is relevant to many biomedical applications.
The proposed approach seems to be well motivated and derived.
While I am not entirely familiar with this literature, the authors seem to have satisfactorily put their contribution in the context of the already abundant literature of extensions of InfoNCE.

### Weaknesses
Overall, the experimental part of the paper is a little bit underwhelming for a paper that claims to be rooted deeply into molecular representation for drug screening data, which is a crowded area.
The benchmarks only feature other generic approaches (i.e. CLIP and CCL) and the experimental details are often lacking to ensure a proper reproducibility of the results.
In fact, the initial simulation study has very little to do with drug effect, as the data used there is Gaussian noise (from various, controlled mixtures).
The results of this first part are purely qualitative (plots of low-dimensional representations of the learnt embedding).
As such, I don't find them particularly convincing compared to CLIP or CCL and it would have been nice to have quantitative metrics showing that InfoCORE representations preserve the original structure of the data (e.g. neighbourhoods) within batches but mix them well across batches after integration (see for instance the scANVI paper from Wu et al. 2021).
The second part tackles a specific (somewhat unusual maybe?) task of identifying drugs that are likely to induce a given effect (I find that the details describing this task to be lacking even after going through appendices).
The quantitative results there do not seem to be significantly better than other methods and the experimental setting seems a bit convoluted as it requires adapting the methods benchmarked against in a non-trivial way.
In all tables, most values written in bold do not seem to be significantly better. This is a bit problematic, IMO.
Perhaps more importantly, the paper avoids addressing what exactly is intended by "batch effect" or "confounding factors".
Notably, the treatment of the fact that LINCS data features drug screening of different cell lines is (it is considered a batch effect?) is relegated pretty far into the appendices while I think it is a crucial question.
In general, although a lot of other methods operate similarly, I find that methods that predict drug perturbation without modelling explicitly the state of the cells those perturbations are measured on to be of limited impact (impossible to extrapolate to cells that are not coming from the exact cell lines present in LINCS, let alone on real tissues).
At the end of the day, I think InfoCORE presents interesting novelties and seems to be sound, but I am not entirely convinced it is a great match for drug screening data.
Perhaps the interesting analogy with learning fair representation could be the more important application (where the experimental results also seem to be superior)?

### Questions
1) Can the authors comment on Proposition 3? Is this bound tight?
2) At the end of Section 2.2.2, the authors make the interesting comment that "once the batch effect has been mitigated, InfoCORE implictly adjusts and ceases to reweigh the negative samples". Is it something that has been observered in practice? It would be great to show some evidence of it.
3) One important motivation for the derivation of InfoCORE is that it should be more robust to settings where some conditions feature few observed samples. Do you have further experimental results that characterizes how this is the case (against CCL for instance)? For instance, it could be interesting to control the number of samples from one or a few "rare" conditions, or at least to show the performance on test samples from such rare conditions.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies multimodal molecular representation learning. The authors analyze the confounding batch effects to the learned molecular representations, and adopt a conditional mutual information maximization objective among the modalities, called the Information maximization approach for COnfounder Removal (InfoCORE). InfoCORE also reweighs the negative samples in the InfoNCE objective differentially based on the posterior batch distribution, to resolve the issue of insufficient negatives.

### Strengths
(+) The studied problem is critical;

(+) The proposed method is interesting;

### Weaknesses
(-) The paper is hard to follow;

(-) The novelty is limited;

(-) The improvements are limited;

(-) Some related works have not been compared or discussed;


1. The paper is hard to follow:
- **All of the variables** in the paper have not been defined;
- The problem is undefined;
- The bias issue caused by the batching effects seems to be interesting, but does it really exist? Are there any realistic examples for the biases?
- What does it mean by claiming X_b as a irrelevant attribute? 
- Why does equation (1) “emphasizes the shared features of the two modalities that are unrelated to batch” and “thus emphasizing the bioactivity of a drug”?
- What is the exact objective of InfoCORE?
- What is the algorithm of InfoCORE?
- The information and the caption of Figure 3 is hard to read. It seems the batching identifier has not influence to the learned representations for all methods.

2. The novelty is limited. It seems the main objective InfoCORE comes from CCL. What are the differences between InfoCORE and CCL?

3. The improvements are limited. 
- In Table 2, the improvements of InfoCORE over CLIP or CCL is marginal while no standard deviations are given. Even the vanilla objective CLIP can outperform InfoCORE.
- In Table 3, InfoCORE has little-to-no improvements over baselines, when considering the standard deviations.

4. Some related works including debiasing or invariant molecular representation learning such as [1,2,3,4,5] have not been compared or discussed.

### Questions
1. The paper is hard to follow:
- **All of the variables** in the paper have not been defined;
- The problem is undefined;
- The bias issue caused by the batching effects seems to be interesting, but does it really exist? Are there any realistic examples for the biases?
- What does it mean by claiming X_b as a irrelevant attribute? 
- Why does equation (1) “emphasizes the shared features of the two modalities that are unrelated to batch” and “thus emphasizing the bioactivity of a drug”?
- What is the exact objective of InfoCORE?
- What is the algorithm of InfoCORE?
- The information and the caption of Figure 3 is hard to read. It seems the batching identifier has not influence to the learned representations for all methods.

2. The novelty is limited. It seems the main objective InfoCORE comes from CCL. What are the differences between InfoCORE and CCL?

3. The improvements are limited. 
- In Table 2, the improvements of InfoCORE over CLIP or CCL is marginal while no standard deviations are given. Even the vanilla objective CLIP can outperform InfoCORE.
- In Table 3, InfoCORE has little-to-no improvements over baselines, when considering the standard deviations.

4. Some related works including debiasing or invariant molecular representation learning such as [1,2,3,4,5] have not been compared or discussed.


**References**

[1] Discovering invariant rationales for graph neural networks, ICLR 2022.

[2] Learning causally invariant representations for out-of-distribution generalization on graphs, NeurIPS 2022.

[3] Learning substructure invariance for out-of-distribution molecular representations, NeurIPS 2022.

[4] Interpretable and Generalizable Graph Learning via Stochastic Attention Mechanism, ICML 2022.

[5] Debiasing Graph Neural Networks via Learning Disentangled Causal Substructure, NeurIPS 2022.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a way to remove batch effect in contrastive learning of multimodal data while drawing negative samples from its marginal distribution. The weighting adjustment for negative samples is semi-parametric and it ensures that the weighting for unlikely negative samples (w.r.t. a batch number) does not shrink to zero. The model is primarily established in the context of molecular representation learning, but could be generalized to the removal of sensitive information in representation fairness problems. In experiments, the proposed model is examined in both context and overall achieves a better performance compared to the benchmarks.

### Strengths
Paper is well written: review of prior work is given and comparison to prior work is clear, walkthrough of derivation is intuitive and easy to follow. Figures of the graphical model and computational workflow are presented in a clean fashion that aids understanding the framework. The method is adequately novel and addressed the negative sample supply problem in conditional contrastive learning: the framework is capable of conducting training with batch data randomly sampled across different experiments. Experiments are done thorough.

### Weaknesses
1. The computational considerations for $L_{CLF}$ should be illustrated. $L_{CLF}$ by itself is not tractable without the true sampling distribution $p(x_b | z_d)$ and $p(x_b | z_g)$, and is not exactly a classification loss. Without any clear statement that you're replacing $L_{CLF}$ with conditional density learning through classification loss, there isn't any direct justification for factoring $ \mathbb E_{p(z_d^1, z_g^1, x_b^1)} \log \frac{(\hat{p}(x_b^1 | z_d^1, z_g^1))^2}{p(x_b | z_d^1)p(x_b | z_g^1)}$ into $C - L_{CLF}$.

2. Line 2 and line 3 of Table 1 should be merged, or line 3 should be just removed. Reweighting of samples is an adjustment you have to make for large supply of negative samples to work, it is not a standalone contribution or an advantage. The current formulation of the table is slightly misleading.

3. Figure 1. does not demonstrate the classification workflow clearly. The figure and the yellow coloring on the right grid makes it seem like you're optimizing $M_{ii}$ w.r.t. batch identifiers.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
* A molecular representation learning method, InfoCORE, is introduced to mitigate the presence of confounders, such as batch effects, in multi-modal contrastive learning.
* Theoretical results were provided, showing that InfoCORE maximizes the variational lower bound on the conditional mutual information of the representations given the batch identifier.
* Empirical experiments were conducted to evaluate the proposed method along with baselines on one simulated dataset and two real drug screening datasets for two downstream tasks, including molecule-phenotype retrieval and molecular property prediction.
* A real-data experiment was presented to demonstrate that InfoCORE can be applied beyond drug discovery, improving fairness metrics when learning representations with sensitive attributes.

### Strengths
The proposed method is an extension of CLIP, an unconditional multi-model contrastive learning method, and CCL, a conditional contrastive learning method that does not address the confounder issue, thus tending to overcorrect for biological effects. The use of reweighting the negative samples differentially based on the posterior batch distribution solves the challenge of poor generalization in the case of limited negative samples for CCL. The results show a clear improvement in the metrics for both simulated data and real data tasks.

### Weaknesses
 * It is not clear what is driving the algorithmic adjustments described in the Computational Considerations section, and how the choice of hyperparameters will impact the final results. 
* In the simulation data experiment section, it can be relatively difficult to evaluate the quality of the learned representation by examining only the first two principal components since the variance in other dimensions can be concealed. Visualization through manifold learning techniques such as t-SNE or UMAP, or evaluation using various metrics, can provide more reliable insights.

### Questions
What is driving the algorithmic adjustment described in the computational considerations, what is the risk of doing so, and how the choice of the hyperparameter will impact the final results?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
