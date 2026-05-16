Now I have all the information needed to verify reviewer claims against the paper. Here is the consolidated review.

---

## Summary

This paper proposes ProtoN-FM, a prototype-guided dynamic normalization mechanism that replaces standard LayerNorm in Transformers with multiple LayerNorm modules, gated by sample-to-prototype similarity. The goal is to handle distribution heterogeneity across multiple time-series datasets during pretraining. The method is evaluated on fault diagnosis and human activity recognition tasks, showing consistent improvements over vanilla multi-dataset pretraining, with ablation studies validating the prototype gate and orthogonality constraint components.

## Strengths

- **Consistent improvement across multiple tasks and settings.** ProtoN-FM outperforms vanilla multi-dataset pretraining on every individual dataset in both FD (Table 1: 70.33% vs. 66.38% avg. accuracy) and HAR (Table 2: 51.05% vs. 47.34% avg. accuracy), with gains in both accuracy and Macro-F1 across all datasets. This robustness to different distributions supports the core thesis.

- **Leave-one-out generalization experiment directly tests the unseen-domain scenario.** Section 5.3 (Figure 6) shows that when the target dataset is *excluded* from pretraining, ProtoN-FM still improves over vanilla (FD: accuracy 46.73% vs. 41.89%; HAR: 49.12% vs. 47.78%). This is the cleanest test of distribution shift from pretraining to a novel downstream task.

- **Robustness under controlled distribution shifts.** Figure 7 demonstrates that ProtoN-FM outperforms vanilla at three levels of Gaussian noise perturbation (IMS-N1 through N3), with the largest gap at the most severe shift (+3.49 pp accuracy at IMS-N3), directly supporting the claim of mitigating distribution shift.

- **Ablation validates both key components.** Table 3 shows that removing the prototype gate (→ dataset-specific fixed LN) drops average accuracy from 70.33% to 67.65%, and removing the orthogonality constraint drops it to 68.28%, confirming that both components contribute to the gains.

- **Design rationale is principled.** Section 3.2 explicitly motivates modifying LayerNorm (rather than attention/FFN) because its low parameter count makes replication cheap and reduces overfitting risk, citing prior success of domain-specific BatchNorm for adaptation.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison against RevIN and related adaptive normalization methods.** The paper's own Related Work (§2.2–§2.3) cites RevIN (Kim et al., 2021), SAN (Liu et al., 2024b), SIN (Han et al.), and DAIN (Passalis et al., 2019) as normalization-based methods designed for distribution shift in time series. None are included as experimental baselines. RevIN, in particular, is a simple, model-agnostic method that normalizes per-instance statistics and directly targets the same problem. Without this comparison, it is unclear whether ProtoN-FM's more complex mechanism adds value over existing simpler approaches. The DSLN ablation (dataset-specific LayerNorm) is a reasonable internal baseline, but it is not a substitute for comparing against published normalization methods.

- **The main evaluation protocol does not match the paper's strongest claim.** The paper's abstract and introduction emphasize "mitigating the distribution shift between pretraining and downstream tasks," but the primary experiments (Tables 1 and 2) fine-tune on datasets that were included in the pretraining pool (e.g., IMS, UO, PU for FD — all three are among the six pretraining datasets). This tests handling of inter-dataset heterogeneity *during pretraining* rather than transfer to truly unseen downstream domains. The leave-one-out experiment (§5.3) correctly tests the unseen-domain scenario, but the gains there are more modest (FD: +4.84 pp accuracy; HAR: +1.34 pp accuracy) and this experiment is placed in a secondary analysis rather than being the main evidence. The paper would be stronger if the leave-one-out protocol were the primary evaluation.

### Minor

- **Overclaimed novelty.** Line 19 states: "This is the first work to identify the challenge of data distribution mismatch between foundation model pretraining and time series data." This is inaccurate — the paper's own Related Work cites RevIN, Non-stationary Transformers, domain adaptation methods for time series, and other foundation model papers that discuss data heterogeneity. This claim should be removed or significantly softened.

- **Hard argmin selection is non-differentiable and gradient flow is not discussed.** Equation (4) uses `argmin` to select the LayerNorm module, which is a discrete, non-differentiable operation. The paper does not discuss how gradients propagate through this selection. The prototypes are updated via EMA (unsupervised), but the relationship between the gating decisions and the task objective (contrastive loss) is not analyzed. At minimum, the paper should clarify whether a straight-through estimator, Gumbel-softmax relaxation, or other technique is used (or whether the gate is purely unsupervised via EMA).

- **Ablation study conducted only on FD, not HAR.** Table 3 reports the component analysis only for the fault diagnosis task. Repeating this on HAR would strengthen confidence that the contributions generalize.

- **No variance reported.** The paper states "Each experiment was repeated three times, with the average performance reported" but provides no standard deviations or confidence intervals. With only 100 fine-tuning samples, the variance may be non-negligible.

- **Computational overhead not discussed.** The method introduces multiple LayerNorm modules per layer plus a gating network. The added parameters and inference cost are not quantified, making it difficult to assess the practical trade-off.

### Trivial
None.

## Nice-to-Haves

- Per-dataset class distribution information for the 100-sample fine-tuning sets (to better interpret the low-shot setting).
- Analysis of prototype assignment patterns: how often each prototype fires, whether prototypes correspond to datasets or learned cross-dataset clusters, and whether selections are stable across runs.
- Analysis of whether prototypes remain approximately orthogonal after training.
- Discussion of why the optimal number of LayerNorms is task-dependent (3 for FD, #datasets for HAR).

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Vanilla baseline is poorly defined"**: The paper defines Vanilla as "conventional pretraining across multiple datasets" with standard LayerNorm (Section 4.1, Baselines and Training Protocol). This is clear enough.
- **"It is not surprising that a method designed to handle heterogeneity beats one that ignores heterogeneity"**: This is a strawman — nearly all method papers compare against a naive baseline to establish that the problem exists. The critic's preferred baseline would be RevIN (which is a separate missing-baseline issue, addressed above).
- **"The paper does not clarify what pretraining data it uses"**: The paper explicitly lists the six FD datasets and five HAR datasets used for pretraining (Section 4.1, Datasets). This is a misreading.
- **Unfair comparison / asymmetry claims**: Not present in the reviews; no action needed.
- **Generic formatting/style nitpicks**: Not present in a way that needs removal.

## Novel Insights

None beyond the paper's own contributions. The reviews surface expected gaps (missing baselines, evaluation-protocol mismatch) that are useful for revision but do not reveal insights the paper itself does not provide.

## Suggestions

1. **Add RevIN (and ideally SAN or another adaptive normalization) as an experimental baseline** applied to the same Transformer architecture with multi-dataset pretraining. This is the single most important change to establish that ProtoN-FM adds value beyond existing simpler methods.
2. **Restructure the evaluation** so that the leave-one-out cross-domain protocol (§5.3) is the primary evidence for handling distribution shift. The current main tables (1, 2) should be moved to supplementary or presented as "in-distribution fine-tuning (pretraining includes target datasets)."
3. **Correct the "first work" overclaim** (line 19) to something like "This work identifies and directly addresses the challenge of inter-dataset distribution mismatch during time-series foundation model pretraining."
4. **Disambiguate the gating mechanism's training** — clarify whether the hard argmin is used with a gradient estimator, or whether the gating is purely unsupervised via EMA, and discuss the implications.
5. **Add standard deviations** to all tables reporting averaged results over multiple runs.

## Score and Decision

This paper identifies a genuine problem (distribution heterogeneity in multi-dataset time-series pretraining) and proposes a mechanistically plausible solution with consistent improvements across tasks. However, the experimental evaluation has two significant gaps that undermine the claimed contribution: (1) the most relevant existing baselines (RevIN, etc.) are not compared, and (2) the main evaluation fine-tunes on datasets seen during pretraining, while the narrative emphasizes shift to unseen downstream tasks. Until these gaps are addressed, the evidence is insufficient to accept the paper's claims at face value.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>