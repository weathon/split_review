Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper proposes scDiff, a conditional diffusion generative model that unifies diverse single-cell analysis tasks—cell type annotation, imputation, and perturbation prediction—under a common posterior estimation framework. The key innovation is formulating these tasks as estimating \(p(\text{expression} \mid \text{conditions})\) and solving them with a single training objective and diffusion architecture. The framework supports plug-in conditioners: internal (class labels, masked expression) and external (LLM embeddings via BioLinkBERT, GNN embeddings from GEARS). Empirically, scDiff achieves competitive or state-of-the-art results across six annotation datasets (top-1 in 4/6), three imputation datasets, three novel-cell-type perturbation datasets (best on all three), and two zero-shot gene perturbation comparisons against GEARS.

## Strengths

- **Unified posterior formulation for diverse tasks (Section 2.1).** The paper formally derives cell labeling, expression completion, and knowledge transfer as posterior estimation problems (Eqs. 1–4). This is a genuine conceptual advance over prior task-specific frameworks and enables a single training objective across tasks, which the paper then validates experimentally. The formulation is clearly laid out and mathematically precise.

- **Competitive performance across three task categories with internal conditions (Tables 1, 2a, 2b).** scDiff achieves top-1 macro accuracy in 4/6 cell-type annotation datasets without an explicit classifier, matches or exceeds MAGIC and DCA on imputation, and outperforms all baselines (scGen, CPA, CVAE) on all three perturbation prediction datasets. These results directly support the claim that a single conditional diffusion model can match task-specific state-of-the-art methods.

- **Flexible conditioning framework enabling few-shot and zero-shot transfer (Section 4.2, Figs. 2, 3).** The LLM conditioner (BioLinkBERT) improves one-shot annotation over class-conditioned scDiff on 3/4 datasets. The GNN conditioner (GEARS) allows scDiff to outperform GEARS itself on zero-shot gene perturbation across all metrics except one, with lower variance. These experiments convincingly demonstrate that external prior knowledge can be incorporated as a drop-in conditioner without modifying the diffusion backbone.

- **Principled adaptation to single-cell sparsity (Section 2.2).** The paper identifies that standard predict-ε parameterization may be problematic when >95% of entries are zeros, and switches to predict-\(x_0\). This is a well-motivated architectural choice tailored to the data modality, even though it is not empirically validated in the paper.

## Weaknesses

### Fatal

None.

### Major

- **Inference procedure for cell-type annotation is underspecified (Section 4.1.1).** The paper states that cells are annotated by "evaluating the mean square error between input expression and model posterior in a classifier-free approach (Li et al., 2023)." Exactly how \(p(C_{\text{label}} \mid X)\) is computed from the conditional diffusion model is not explained. The reader cannot tell whether this requires running full reverse diffusion per candidate label (prohibitively expensive), a single forward pass, or a one-step reconstruction approximation. Since the annotation results (Table 1) are among the paper's strongest claims, this procedural gap undermines reproducibility. The paper should spell out the inference algorithm (e.g., an algorithm box or pseudocode).

- **No controlled ablation experiments for key design choices.** The paper makes several architectural claims that go untested:
  - predict-\(x_0\) vs. predict-ε: The paper states (Section 2.2) that predict-ε "fails to recover the expression" and motivates the predict-\(x_0\) switch, but provides **no experiment** comparing the two parameterizations. The reader cannot judge whether this choice matters, nor is the claim of "fails" backed by any evidence shown in the paper.
  - Cross-attention vs. simpler conditioning: The cross-attention encoder over multiple conditioners is a central design element, but no comparison is made to a simpler baseline such as concatenating condition embeddings.
  - Batch embedding in decoder (Section 2.3): Said to "better disentangle non-biological variations" but not ablated.
  
  Without ablations, it is unclear which components drive scDiff's performance and whether a simpler diffusion model would suffice. At minimum, the predict-\(x_0\) vs. predict-ε comparison should be provided.

### Minor

- **Uniform prior assumption and label imbalance (Section 2.1).** The paper assumes a uniform prior over cell-type labels (Eq. 1, line 40) to convert label posterior to expression posterior. Real single-cell data often has highly imbalanced cell-type distributions. The paper does not discuss how this assumption might affect annotation performance on rare versus abundant cell types. While the macro accuracy metric partially addresses this, a discussion or analysis would strengthen the paper.

- **Training-time mask sampling for the context conditioner is unspecified (Section 2.3).** The context conditioner uses a "randomly masked expression" with mask indicator \(\mathbf{m} \in \{0,1\}^m\), but the distribution used to sample \(\mathbf{m}\) during training is not described. The evaluation protocol (masking 10% of non-zero counts via exponential distribution) is given in Section 4.1.2 for imputation, but it is unclear whether the same protocol is used during training or whether a different scheme is employed.

- **The claim about predict-ε failing is stated without evidence (Section 2.2).** The paper says "We empirically find that the widely-used predict-ϵ objective fails to recover the expression" but provides no quantitative comparison, figure, or reference to support this claim. This weakens the motivation for the predict-\(x_0\) choice. Including even a small comparison in an appendix would resolve this.

### Trivial

None.

## Nice-to-Haves

- A brief analysis of computational cost (training time, inference time for annotation across \(K\) classes) would help readers assess practicality.
- A discussion of how the uniform prior assumption might affect performance on imbalanced label distributions, or an experiment comparing uniform vs. empirical prior.
- Clarifying whether the LLM embeddings (BioLinkBERT) are frozen or fine-tuned, and why that choice was made.

## Removed Points

These points from the reviewers were examined and removed for the following reasons:

- **Baselines are "dated or narrow":** The perturbation baselines include scGen (2019), CVAE, and CPA (2023); the zero-shot comparison against GEARS (2023) is appropriate since scDiff reuses GEARS' GNN conditioner, isolating the benefit of the diffusion backbone. The baseline set is reasonable for a framework paper demonstrating a new paradigm.
- **Missing hyperparameters/training details:** These details could reasonably reside in an appendix, which is stripped by the parser. The rule prevents penalizing papers for content that existed in the original submission.
- **Statistical significance tests not reported:** The paper reports means and standard deviations across 5 runs for all key results, which is standard practice in this domain. Requesting formal significance testing is a methodological preference, not a flaw.
- **Missing baselines (scBERT, CellBERT):** Per the instructions, missing related works are not to be flagged.
- **General scope-creep suggestions** (e.g., "include a real dropout scenario," "test with larger datasets," "add more models") that are not specific verified weaknesses.

## Novel Insights

The reviews surface an important tension in this paper: the framework's central claim is that many tasks can be *unified* under a single posterior estimation objective, but the inference procedure for the classification variant (cell-type annotation) is the least explained component. This creates a paradox where the paper's strongest quantitative results (Table 1) rely on an inference mechanism that receives only a sentence and a citation. A deeper observation is that the paper would be substantially strengthened not by adding more tasks or datasets, but by rigorously validating the design choices that distinguish scDiff from a standard conditional diffusion model—specifically, whether the cross-attention encoder, predict-\(x_0\) objective, and batch embedding each contribute meaningfully to the reported gains. Without these ablations, the paper's architectural narrative is suggestive but not conclusive.

## Suggestions

1. **Clarify the inference algorithm for cell-type annotation.** Provide an explicit description or pseudocode showing how \(p(C_{\text{label}} \mid X)\) is computed from the diffusion model. State the number of forward passes required per cell and whether the procedure follows Li et al. (2023) faithfully or with modifications.
2. **Add at least one ablation experiment.** The highest-priority comparison is predict-\(x_0\) vs. predict-ε on a representative task (e.g., imputation or annotation). A second useful ablation would compare cross-attention conditioning against a simpler concatenation baseline.
3. **Provide evidence for the claim that predict-ε "fails."** If this claim is central to the motivation, it should be substantiated with quantitative results (even a small experiment).
4. **Specify the training-time mask sampling distribution** for the context conditioner.
5. **Discuss the uniform prior assumption** and its implications for imbalanced cell-type distributions, or acknowledge this limitation and its potential impact.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>