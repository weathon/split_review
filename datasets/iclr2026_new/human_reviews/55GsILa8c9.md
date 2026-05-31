## Human Reviewer 1

### Summary
This paper introduces CausalNovo, a model-agnostic framework designed to improve de novo peptide sequencing by learning causal representations from mass spectra.  The authors posit that existing deep learning models often rely on spurious correlations with noise peaks, limiting their robustness and generalizability. CausalNovo addresses this by employing a Structural Causal Model (SCM) to disentangle causal signal information from non-causal noise, guided by the principles of independence and sufficiency.

### Strengths
(1) Principled Methodological Framework: The CausalNovo framework is well-grounded in the theory of Structural Causal Models (SCMs) and Reichenbach's Common Cause Principle.

(2) In-depth Model Analysis: The paper goes beyond standard performance metrics by providing insightful analyses that support its central claims. 

(3) Clarity and Organization: The manuscript is clearly written and well-structured.

### Weaknesses
(1) The framework exhibits notable sensitivity to several key hyperparameters, suggesting that its distinction between “causal” and “non-causal” peaks may depend heavily on parameter choices. This dependence raises concerns about the robustness of the approach and its generalizability to datasets or instruments beyond those tested.

(2) While the authors acknowledge that CausalNovo entails additional computational cost due to multiple forward passes per batch, this overhead is not quantitatively characterized. A clear assessment of the increase in training time or computational resource usage would be essential for evaluating the method’s practicality in real-world scenarios.

(3) The framework’s operational definition of causal ions—limited to theoretical b, y, and a ions—represents a simplified view of fragmentation behavior. In practice, mass spectrometric fragmentation is inherently stochastic, and signals from other ion types or unexpected neutral losses can also carry meaningful information. Although Table 6 addresses this to some extent, the analysis may not fully capture the spectrum of ionization behaviors across different instruments or fragmentation techniques.

### Questions
Recently, many transformer-based de novo peptide sequencing methods have emerged [1-4]. The discussion of these approaches in the paper is insufficient.

[1] Bidirectional Representations Augmented Autoregressive Biological Sequence Generation: Application in De Novo Peptide Sequencing. 
[2] Universal Biological Sequence Reranking for Improved De Novo Peptide Sequencing.
[3] Latent Imputation before Prediction: A New Computational Paradigm for De Novo Peptide Sequencing.
[4] MassNet: billion-scale mass spectral corpus enables robust de novo peptide sequencing.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes a de novo peptide sequence method, named casualNovo, to model the causal relationship between the input mass spectrum and peptide sequence, thereby enabling the model to reduce the interference of noisy data and achieve better sequencing results.

### Strengths
1. The method is novel. The application of casualML to denovo is a novel and meaningful application, and the motivation proposed in the article, "these methods are fundamentally limited by their statistical nature，they aim to model dependencies between mass spectra and peptides without accounting for the underlying causal mechanisms." is indeed reasonable.

2. Model-agnostic; CasualNovo is model-agnostic and can be integrated to various denovo models

3. Performance: After applying the model to existing de novo models, the performance improvement is evident, and various experiments have been conducted to fully demonstrate the effectiveness of the model;

### Weaknesses
1. The article is hard to follow; the background knowledge introduction about denovo and causal inference is not clear and detailed enough. CasualML is a relatively niche field, and AI for denovo is an even more niche area; readers of this article who are not very familiar with this field will have to spend a lot of time; many details, including "do operation" and "b/y ions", are not explained clearly;
2. There is no significant improvement in performance compared to SOTA models; although the article proves through experiments that applying casualNovo to casanovo and other models can bring improvements, there is no significant difference between the best result (casanovo + casualNovo) and the best baseline (searchNovo), and the performance is worse than the latest SOTA on novobench (ReNovo, LipNovo); it is worth noting that the article omits the latest baseline Lipnovo [1], and mentions ReNovo but does not compare it experimentally. It is unclear why?

[1] Du, Ye, et al. "Latent Imputation before Prediction: A New Computational Paradigm for De Novo Peptide Sequencing." Forty-second International Conference on Machine Learning.

### Questions
1. The model is model-agnostic, but it seems that the specific implementation of transferring casualNovo to existing denovo models (such as casanovo, etc.) cannot be determined from the article. Is it by directly adding a new loss? Or is it by using the already trained checkpoint and retraining with casualNovo?

2. Why is there such a significant performance gap between the model performance you retrained (marked with a cross symbol) and the original model performance in Table 1? How can this be explained? Overall, your retrained results are significantly higher than those of the original NovoBench, so the performance improvement may be attributed to your training trick rather than casualNovo.

3. Since peptide precision is the most important metrics, why do Figures 3 and 4 only include amino acid precision?

Overall, the motivation behind the problem statement is meaningful, and the method seems promising. However, certain experimental results and numerous details leave room for confusion and doubt.

### Soundness
3

### Presentation
1

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper proposes CausalNovo, a model-agnostic framework for de novo peptide sequencing that injects causal principles (independence & sufficiency) into spectrum-to-peptide models. Concretely, the authors add a Causality Extraction Module (CEM) that masks/weights latent peak representations, perform replace-based interventions on noise peaks inferred via theoretical spectra, and train with contrastive invariance and information-theoretic objectives so that predictions rely on causal fragment ions rather than spurious peaks. Across three public datasets and three strong baselines, the method reports consistent improvements (up to ~10% on AA/peptide/PTM metrics) and reduced vulnerability under noise perturbations and varying noise-signal ratios, with negligible inference overhead (<1%) but extra training cost.

### Strengths
- Clear causal motivation & SCM formalization. The paper formulates MS-based sequencing under a simple SCM (variables X, C, S, Y) and derives two practical principles (independence, sufficiency) that directly inform the learning objectives. 
- Pragmatic intervention design. Identifying non-causal peaks via proximity to the theoretical spectrum and then replacing a fraction of them with batch-realistic noise is simple, domain-grounded, and avoids distribution shift; adding the theoretical peaks back helps preserve causal links. 
- Sound training objectives. Independence is enforced by a symmetric contrastive loss between causal latents before/after intervention; sufficiency/purification are tied to standard cross-entropy on causal/non-causal partitions. 
- Robustness analysis. Systematic noise-peak perturbations, NSR sweeps, and attention analysis show reduced reliance on non-causal peaks and better generalization. 
- Practicality. The authors have open-sourced code.

### Weaknesses
1. Theoretical spectrum definition is oversimplified and not scientifically sufficient.
The method assumes theoretical peaks are only b/y/a ions, but a minimum correct definition in proteomics is six ion types (a/b/c/x/y/z) — and modern SOTA like GraphNovo[1] uses 18+ ion variants. This directly challenges the causal sufficiency assumption claimed in the paper, because relevant causal signal peaks are explicitly omitted.

2. Missing key related works and citations.
GraphNovo[1], ContraNovo[2], RankNovo[3] — all highly relevant and recent — are not cited or discussed.

3. Missing strongest baseline — especially ContraNovo — despite using Nine-species.
If the authors use this benchmark, ContraNovo is a canonical comparison point and must be included. Otherwise, robustness and generality claims remain incomplete.

4. Benchmark choice is unconvincing.
The paper relies mainly on NovoBench, specifically the Nine-species, Seven-species, and HC-PT settings. Taking Nine-species as an example — NovoBench adopts a cross-validation–style train/test split within the same dataset, which is essentially a toy scenario that does not reflect real-world generalization requirements.
In contrast, modern and more realistic evaluation protocols — as adopted by PrimeNovo, ContraNovo, and RankNovo — require training on a large-scale external corpus such as MassiveKB, and evaluating on Nine-species / Seven-species / HC-PT as out-of-distribution test sets.
Under this view, the current evaluation setup does not convincingly demonstrate robustness or generalization. This limitation should be explicitly acknowledged and/or addressed in the discussion section of the paper. The discussion and statement of this limitation in the revised manuscript will be a key factor of my final ratings.

[1] Mitigating the missing-fragmentation problem in de novo peptide sequencing with a two-stage graph-based deep learning model

[2] ContraNovo: a contrastive learning approach to enhance de novo peptide sequencing

[3] Universal Biological Sequence Reranking for Improved De Novo Peptide Sequencing

### Questions
These must be addressed to justify acceptance:

1. Why do you assume only b/y/a ions are “causal” — do you believe c/x/z or neutral-loss ions are non-causal?

2. Would your causal extraction still hold after you included the full abcxyz spectrum?

3. Why was ContraNovo not evaluated despite using its canonical benchmark?

4. Can you justify reliance on NovoBench rather than PrimeNovo-style modern setups?

5. Is the causal claim purely architectural, or does it theoretically depend on the correct definition of fragment ion families?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
CausalNovo presents a causality-informed framework for de novo peptide sequencing that aims to improve robustness against non-causal spectral noise. By introducing a Causality Extraction Module and applying independence and sufficiency principles through mutual information and contrastive learning objectives, the framework disentangles causal signal peaks from noise in the latent space. The approach consistently improves performance over several Transformer-based baselines, demonstrating better generalization under noisy or perturbed conditions.

### Strengths
1. Introduces a novel causality-inspired framework that addresses a real limitation in current de novo peptide sequencing
2. The method integrates causal principles (independence and sufficiency) with practical implementation through contrastive learning, showing consistent performance gains across datasets.
3. The work is well-motivated and provides detailed ablation studies to analyze each component’s contribution.

### Weaknesses
1. Although the framework is claimed to yield causal representations, the authors never visualize or interpret what these causal embeddings represent. It would be helpful to include some qualitative examples in addition to the quantitative results in Table 14 to improve interpretability.
2. The authors mention that the method “increases training cost,” but it would be valuable to quantify this overhead and compare it directly with the base models.
3. Does the proposed method effectively work only for Transformer-based variants such as CasaNovo, but not for other architectures like DeepNovo?

### Questions
see weakness

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
4