- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes FedGTG, a federated class-incremental learning (FCIL) framework that uses server-side generative models (a data generator and a feature generator trained via data-free methods) to produce synthetic data and features. These are distributed to clients, who use logit distillation, fine-tuning with synthetic data, and an Empirical Feature Matrix (EFM) loss to control feature directions, aiming to improve the stability-plasticity trade-off. Experiments on CIFAR-10, CIFAR-100, and tiny-ImageNet show improvements in Average Incremental Accuracy (AIA) and Average Forgetting (AF) over three compared baselines.

## Strengths

- **Consistent SOTA-level results across three benchmarks**: Table 1 shows FedGTG achieves the highest AIA and lowest AF on all three datasets (CIFAR-10: 64.50% AIA vs 61.34% for MFCL; AF 13.14% vs 22.32%). Gains are consistent, not cherry-picked on one dataset.

- **Broader model analysis than typical FCIL papers**: Section 3.3 goes beyond standard accuracy/forgetting reporting by evaluating robustness to natural corruptions (CIFAR-100-C), flat-minima convergence, calibration error (ECE), and sensitivity to client size. This gives a more complete picture of practical utility.

- **Novel combination of twin generators with feature-direction control**: The paper's core technical idea — training both a data generator and a feature generator on the server and using the feature generator's output for logit distillation and the EFM loss — is a reasonable and novel approach to the stability-plasticity problem in FCIL.

## Weaknesses

### Fatal
None.

### Major

- **No quantitative ablation study to attribute gains (core methodological gap)**: The paper claims all four loss components (plasticity CE, logits distillation, fine-tuning loss, EFM loss) and the twin-generator design are necessary. Yet the only decomposition provided is a single confusion matrix for "G_D + G_F" (Figure 1c) on CIFAR-10 — a qualitative snapshot. There is no table reporting AIA/AF for configurations such as (i) no generators, (ii) data generator only, (iii) data + feature generators without EFM loss, (iv) full FedGTG. Without this, the claimed 4% AIA improvement and 10% AF reduction cannot be attributed to the paper's specific design choices rather than incidental benefits of the generative replay pipeline. For a new-method paper, this is a decisive gap.

- **Ambiguity in the client-side training protocol (reproducibility concern)**: Section 3.3 states that for the fine-tuning loss (Eq. 9), "clients freeze the feature extraction layers and update only the linear head." However, the overall client objective (Eq. 13) simultaneously optimizes the plasticity loss (Eq. 6, computed on full model outputs) and the EFM loss (Eq. 10, computed on feature-extractor outputs), both of which require updating the feature extractor. The paper never explains how these conflicting requirements are resolved in a single training step — e.g., alternating frozen/unfrozen phases, stop-gradient operators, or separate forward passes. This ambiguity undermines reproducibility and logical coherence of the method.

- **Incomplete experimental comparison with relevant FCIL methods**: The paper discusses GLFC (Dong et al., 2022) and FedCIL (Qi et al., 2023) in the Related Work section but does not compare against them in experiments. The comparison pool is limited to FLwF-2T, TARGET, and MFCL. Even if FedCIL has privacy concerns and GLFC uses a proxy server, their exclusion without quantitative justification (e.g., showing they fail under the same protocol) weakens the "state-of-the-art" claim.

### Minor

- **Undefined variable `q` in generator loss equations**: Eqs. (1) and (7) use `argmax(z[:, q])` where `q` is never defined. This makes the data generator and feature generator losses impossible to implement as written, and suggests the exposition may be incomplete.

- **Missing hyperparameter values for generator training**: The paper specifies hyperparameters λ_IE, λ_batch, λ_smooth, λ_FIE, λ_current, λ_logits, λ_FT, λ_EFM, and λ_E, but gives no values or tuning procedure for any of them. The generator architectures, learning rates, and batch sizes are also absent. While some of these may be deferred to a (stripped) appendix, the paper text itself does not reference one, leaving these as gaps.

- **EFM loss adaptation for federated setting not discussed**: The EFM loss (Eq. 10) is adapted from Magistri et al. (Elastic, 2024), designed for single-client continual learning. The paper states synthetic features are used to compute E_{t-1}, but does not discuss how this computation is done across clients, or whether the approximation from synthetic features faithfully represents previous-task feature distributions in the federated context.

- **CIFAR-100-C robustness analysis lacks quantitative rigor**: The paper reports "average improvement of 5% over MFCL and 8% over TARGET" on CIFAR-100-C, but provides no breakdown by corruption type, no variance/error bars on the bar chart (Figure 3), and no statistical test. This weakens the confidence in the robustness claim.

### Trivial

- Section header reads "Metholodgy" (line 97) instead of "Methodology."

## Nice-to-Haves

- A cost analysis quantifying server/client storage and computation for the two generators relative to storing exemplars would strengthen the practical motivation.
- Statistical significance tests (e.g., paired bootstrap) for the AF and AIA comparisons would make the claimed improvements more convincing.

## Removed Points

- **"Standard deviations reported across only three seeds — variance possibly under-estimated"**: Three random seeds is standard practice in ML/DL research. The speculation that variance is "under-estimated" is not grounded in evidence from the paper. Removed per Soft Rules (generic critique that does not harm the core claim).
- **"Fig. 1 heatmap shows only a single CIFAR-10 test run — not evidence"**: The confusion matrices are explicitly described as illustrative (the caption says "confusion matrix among FCIL algorithms"). The quantitative evidence is in Table 1. Removed as the reviewer mischaracterizes the role of the figure.
- **"No variance shown for robustness"**: Already captured as a Minor weakness about lacking error bars on the bar chart; the separate framing as a section-note is redundant. Merged into the CIFAR-100-C weakness above.
- **"Storage burden discussion omits computational cost of training generators"**: This is a nice-to-have point, not a genuine weakness — the paper's limitations section discusses storage, which is the primary concern. Computational cost is a secondary consideration. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The harsh critic correctly identifies a missing ablation study and a training-protocol ambiguity as the central weaknesses, but the strength finder does not surface any perspective that re-frames or deepens the paper's contribution beyond what the authors claim.

## Suggestions

1. **Add a full quantitative ablation study** (Table) reporting AIA/AF on all datasets for: (a) No generators (client-side distillation only), (b) Data generator only, (c) Data + feature generators (no EFM loss), (d) Full FedGTG. This is the single highest-leverage improvement.

2. **Clarify the client-side training protocol**: explicitly state whether the feature extractor is frozen only during the fine-tuning loss computation (e.g., via stop-gradient or alternating updates) or frozen throughout. If alternating, describe the schedule.

3. **Expand the baseline comparison** to include or quantitatively justify the exclusion of GLFC and FedCIL under the same evaluation protocol.

4. **Define `q`** in Eqs. (1) and (7), and provide the hyperparameter values used in experiments (or state that they are tuned and report the final values).
