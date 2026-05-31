Now I have all the verification I need. Let me produce the final consolidated review.

## Summary

This paper proposes TopoFormer, a Transformer architecture for reactive motion prediction in two-person close interactions. The key ideas are (1) using Gauss Linking Integral (GLI) values between 6 serial chains of the body as topological input features, and (2) a Spatial Relation-aware Relative Position Encoding (srRPE) that injects proximity information between interacting body chains into the attention mechanism. The model is evaluated on ExPI and CHI3D datasets under cross-trial and cross-subject protocols, achieving lower Aligned Mean Error (AME) than InterFormer and two GAN-based baselines, as well as lower Average Interpenetration per Frame (AIF), a new metric the authors propose.

## Strengths

1. **Novel and well-motivated use of topological features in a neural architecture for motion prediction.** The paper makes a compelling case that Euclidean representations miss interaction semantics (e.g., "surrounding" in a hug) and that GLI — a continuous topological invariant previously used only in optimization-based approaches — can be integrated as Transformer input features. This conceptual bridge between topology and learned motion prediction is the paper's primary intellectual contribution.

2. **Consistent empirical advantage across datasets and protocols.** Tables 1 and 2 show TopoFormer achieves the lowest AME at every prediction duration on ExPI (CT and CS) and CHI3D, with margins of 21–48% over InterFormer on ExPI CT and 5–26% on CHI3D. The improvement is sustained across two independently collected datasets, strengthening the evidence.

3. **Ablations validate both proposed components.** Table 4 shows that removing both TST and srRPE raises AME substantially, and each component contributes. Table 6 demonstrates that replacing srRPE with MLP-based positional encoding or ablating its query/key/value lookup tables increases AME. These results directly support the design choices. Table 5 further links the TST block (which processes GLI features) to lower interpenetration, showing the topological embedding serves its intended purpose.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Baseline comparison protocol is not fully documented.** The paper reports AME for Men et al. (2022), Goel et al. (2022), and InterFormer (Chopin et al., 2023) but never states whether these baselines were re-implemented under the paper's own train/test splits or whether numbers were taken from original papers. Since the Cross-Trial protocol described in this paper ("gathering the 2 couples who performed all common interaction classes") differs from splits that prior work may have used, the reader cannot fully verify the comparisons. The reported improvements over InterFormer (21–48% on ExPI CT) are large enough that this documentation gap matters. *Why it matters: Without confirmation of identical evaluation conditions, the central comparative claim is less certain.*

2. **The AIF metric needs calibration and validation.** The AIF metric measures GLI changes between consecutive frames in the *predicted* motion only — despite the text description that confusingly references "ground truth (GT) and predicted (p) motion" while the formula uses only predicted superscript p. Three concrete issues: (a) the threshold of 0.5 is not justified; (b) no ground-truth AIF values are reported, leaving the reader unable to interpret what "good" AIF means; (c) no conventional interpenetration measure (e.g., mesh penetration depth) is reported to validate that lower AIF corresponds to physically fewer implausible interpenetrations. *Why it matters: The AIF metric is novel and the paper's second major evaluation axis; it requires stronger grounding to be convincing.*

3. **No statistical uncertainty reported.** All tables present single numeric values without error bars, standard deviations, or confidence intervals. The datasets are modest in size (ExPI: 115 sequences; CHI3D: 631 sequences), and motion prediction results can exhibit non-trivial variance across seeds. This is standard practice to report in this field and would substantially strengthen confidence. *Why it matters: Without variance estimates, it is unclear whether the reported advantages are robust or within noise.*

4. **Ablation study limited to one setting (ExPI CT).** Tables 4–6 are all conducted on ExPI Cross-Trial only. The paper would benefit from showing that the ablation trends (importance of TST block, srRPE, etc.) generalize at least to ExPI CS or CHI3D. *Why it matters: Convergent ablation evidence across settings would increase confidence that the design choices are not dataset-specific.*

5. **srRPE parameters (α, β, γ) are fixed across datasets without sensitivity analysis.** The values α=0.001, β=90, γ=16000 are reported (Section 4.2) but never varied. A brief investigation (e.g., varying α by an order of magnitude) would demonstrate robustness of the proximity encoding. *Why it matters: The piecewise mapping controls how proximity is quantized; showing insensitivity to these hyperparameters would strengthen the method.*

### Trivial

- The 6 serial chains (left arm, right arm, torso, etc.) are shown in Figure 3 but not enumerated in the text, making the exact joint composition of each chain ambiguous.
- The text description of AIF ("ground truth (GT) and predicted (p) motion") contradicts the formula, which uses only predicted motion — this needs correction for clarity.

## Nice-to-Haves

- Validation of AIF against a conventional geometric interpenetration metric (e.g., mesh penetration depth on a subset of results) and reporting ground-truth AIF values would transform this from a suggestive to a well-grounded metric.
- Releasing code and trained models would significantly aid reproducibility given the architectural complexity.

## Removed Points

Given the formatting constraints of a short conference paper and the fact that the supplementary material (which contained discretization details and likely more experimental specifics) is stripped by the parser, several criticisms raised by the reviewers do not apply or were over-weighted:

- **"Circularity" of AIF metric** (removed): The reviewer claimed AIF is "designed to measure something the model is specifically built to control." This is incorrect — the model's loss is MPJPE reconstruction loss, not AIF. The model uses GLI as an *input feature*, and AIF evaluates output smoothness in the same representation; this is no more circular than using joint positions as input and MPJPE as evaluation. The remaining concerns about AIF validation (threshold, ground-truth baseline, geometric correlates) are retained above.

- **"InterFormer uses a subject-agnostic cross-subject split"** (removed): This claim about what split InterFormer originally used is not verifiable from the paper or from the information available, and the critique speculates about InterFormer's original evaluation setup rather than identifying a problem with this paper's own comparison protocol.

- **Missing comparison to TBIFormer, Social Diffusion** (removed): Per instructions, missing related works should not be mentioned as weaknesses, as external knowledge cannot be confirmed.

- **GLI values for far-apart chains will be near zero** (removed): This is an observation, not a weakness — the model can learn to ignore near-zero values, and this is not discussed as a problem in the paper.

- **Figures 1/4 ERF visualization not convincing as semantic evidence** (removed): The reviewer demands more from a qualitative visualization than it is designed to provide; the quantitative ablation evidence (Table 6) already supports the claim, and the visualization is supplementary.

- **Code release not mentioned** (moved to Nice-to-Haves): Not required for acceptance.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify baseline evaluation in the final version**: Explicitly state whether InterFormer, Men et al., and Goel et al. were re-run using the same code/splits or whether numbers are cited from original papers. If re-run, provide implementation details; if cited, justify split compatibility.

2. **Strengthen AIF as a metric**: (a) correct the text to match the formula, (b) report ground-truth AIF for both datasets, (c) add a small-scale validation study using a geometric penetration measure (e.g., SMPL mesh collision count) on a subset of predictions, (d) justify or ablate the 0.5 threshold.

3. **Add error bars**: Report results with at least 3 random seeds for the main tables (Tables 1–3) and key ablations (Tables 4–6).

4. **Extend ablations**: Show that the core ablation trends (TST, srRPE importance) hold on at least one additional setting (ExPI CS or CHI3D).

5. **Enumerate the 6 chains explicitly** in the main text so the reader knows exactly which joints belong to which chain.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>