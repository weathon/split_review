## Summary

TAK (Task Arithmetic with KFAC regularization) proposes a dataless regularizer that encourages weight disentanglement in task arithmetic by framing representation drift regularization as a curvature matrix approximation problem. Under linearized fine-tuning, the representation drift objective simplifies into a quadratic form of the Jacobian Gram matrix, which is shown to be an instance of the Generalized Gauss-Newton (GGN) under squared loss — enabling the adoption of KFAC as an efficient, data-free approximation. The paper further introduces a Kronecker accumulation heuristic that collapses per-task regularizers into a single O(1) surrogate, and validates the approach on 8-task vision (CLIP ViT-B/32, B/16, L/14) and language (T5-base) benchmarks, achieving performance on par with or better than the data-dependent baseline τJp.

---

## Strengths

- **Clean theoretical derivation connecting representation drift to the GGN (Sec. 3.1–3.2):** The reformulation in Eq. (3) shows that linearization reduces representation drift to a quadratic form of the Jacobian Gram matrix, and Sec. 3.2 establishes that this matrix is the GGN under squared loss, enabling a principled transfer of curvature approximation tools. This is a non-trivial and well-executed insight.

- **Constant-complexity accumulation validated empirically (Table 3):** The Kronecker merging heuristic in Eq. (8) reduces storage/runtime from O(T) to O(1). Table 3 directly compares accumulated (TAK) against the naïve O(T) formulation on three architectures, showing ≤0.8-point absolute gap — confirming the heuristic is effective in practice.

- **State-of-the-art dataless performance in both task addition and negation (Tables 1 & 2):** In task addition, TAK matches the data-dependent τJp on ViT-B/32 (85.8 vs. 85.0), ViT-B/16 (88.3 vs. 88.2), and ViT-L/14 (91.6 vs. 90.9) at α=1, while requiring no external data. In task negation (Table 2), TAK outperforms τJp on all three architectures (target accuracy 3.4/3.4/3.5 vs. 6.7/4.7/3.7), while also improving control task accuracy.

- **Robustness to α eliminates the need for held-out tuning (Figure 4a):** The α-sweep on ViT-B/32 shows KFAC-regularized TA maintains a broad plateau of high accuracy (~84–86%) over [0, 2], while competing methods (standard TA, TSV, ISO, TIES) show sharp peaks requiring careful α selection. This property is practically valuable in privacy-constrained settings.

- **Practical efficiency with small overhead (Figure 6):** KFAC pre-computation for all 8 vision tasks takes only 4 minutes with MC=1 (vs. ~199 minutes exact). Training overhead is 12–22% additional VRAM, while running ~3× faster than τJp, which requires a second forward-backward pass through the linearized model.

- **KFAC compression analysis (Figure 7b):** Block-diagonalization reduces storage from ~550 MB to ~70 MB (87% reduction) with only ~1-point accuracy drop on ViT-B/16, demonstrating practical deployability under memory constraints.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Asymmetric weighting in Eq. (8) is unjustified.** The accumulated regularizer places λ_t on the A factor but not the B factor: `(Σ B_t^l) ⊗ (Σ λ_t A_t^l)`. This asymmetric placement is never explained or motivated, even informally. While Table 3 confirms the heuristic performs nearly as well as the O(T) formulation, the paper offers no analysis of when this approximation might degrade or why the asymmetry was chosen over, e.g., `(Σ √λ_t B_t^l) ⊗ (Σ √λ_t A_t^l)`. Users applying TAK to new settings cannot predict failure modes.

- **The task negation advantage over τJp is not explained.** In task addition (Table 1), TAK roughly matches τJp; in task negation (Table 2), TAK outperforms it by a large margin on ViT-B/32 (3.4 vs. 6.7 target accuracy) and meaningfully on ViT-B/16 (3.4 vs. 4.7). Since both methods use linearized fine-tuning and the key difference is the regularizer structure, this gap warrants at minimum a hypothesis — is it due to structural differences in how negation vs. addition interacts with curvature quality? Or a hyperparameter advantage? The paper presents the numbers without discussion.

- **Degradation with increasing MC samples (Figure 7a) is unexplained.** The paper notes (line 318): "performance deteriorates beyond this point, with variance across seeds increasing as the number of MC samples grows" — a surprising result, since more MC samples should reduce estimator variance. The authors observe the phenomenon but offer no mechanistic explanation (over-regularization? seed-sample interaction?). Given that M=1 is the recommended default, this unexplained behavior leaves practitioners without guidance about when to deviate.

- **ViT-L/14 memory footprint unreported.** The KFAC compression analysis (Fig. 7b, Sec. 4) reports storage costs only for ViT-B/16 (~550 MB full, ~70 MB compressed). ViT-L/14 has substantially wider layers, and KFAC storage scales quadratically with layer width. Since ViT-L/14 is the strongest-performing model and a primary selling point for scalability, the omission of its memory requirements leaves the practitioner case incomplete.

### Trivial

- The language task gap with τJp (81.3 vs. 78.7 absolute) receives only the one-sentence explanation: "textual domains may still benefit from even more accurate curvature estimation." This neither distinguishes which of the six NLI tasks drive the gap nor considers alternative structural explanations (e.g., overlap in vocabulary projection layers). It is worth a brief followup even if it remains a limitation.

---

## Nice-to-Haves

- A brief analysis of the Kronecker accumulation heuristic's approximation error — e.g., how well the dominant eigenvectors of the accumulated product are preserved relative to the exact sum — would convert an empirically-validated heuristic into a principled approximation with understood behavior.
- An analysis of the information content in G_t(θ_0) (curvature at the pre-trained init) vs. G_t(θ_t*) (curvature at fine-tuned weights) would help explain *why* the dataless regularizer is nearly equivalent to the data-dependent one, and clarify the operating conditions for the method.
- For the task localization plot (Fig. 5): the paper shows out-of-distribution scores are pushed toward zero under regularization. A complementary result showing the *correlation* between task localization quality and per-task accuracy improvement would add analytical depth beyond confirming the regularizer's direct optimization target.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **[Harsh Critic] Criterion mismatch (squared loss vs. cross-entropy) undermines the regularizer.** Removed as a weakness — the paper explicitly acknowledges this substitution (Sec. 3.2: "If we choose squared error rather than the training criterion, the GGN becomes the Jacobian Gram matrix exactly") and the empirical results validate that the proxy works. Acknowledging a simplification is not a flaw.

- **[Harsh Critic] TaLoS comparison configurations may not be controlled (non-linear regime).** Removed per hard rules: "REMOVE weaknesses about unfair comparison with other methods if the asymmetry favors the baseline and not the author's method." TaLoS uses results from the original paper (†) but achieves 92.4 normalized on ViT-B/16 while TAK achieves 91.0 — asymmetry favors the baseline, which actually strengthens rather than weakens the comparison. The configuration concern is not substantial enough to retain.

- **[Harsh Critic] "Strengthening the Paper" — analysis of what KFAC at θ_0 captures.** Moved to Nice-to-Haves. This is a valuable suggestion but not a weakness of the paper as written.

- **[Strength Finder] "Task localization as direct evidence of weight disentanglement" (Strength 5).** The regularizer directly minimizes the quantity being plotted (||J_θ f(x,θ_0) τ_t||² for out-of-distribution inputs is the regularization objective applied to other tasks' curvature). The visualization confirms the regularizer does what it is designed to do, but it is circular confirmation rather than independent evidence of disentanglement. Retained as a minor supporting observation but removed as a core strength.

---

## Novel Insights

The key novel insight — that linearized representation drift regularization reduces to a quadratic form of the Jacobian Gram matrix, which is precisely the GGN under squared loss — is clean and non-trivial. It converts a data-dependent problem into a curvature approximation problem, unlocking decades of second-order optimization literature. The additional insight that KFAC factors can be accumulated into a single O(1) surrogate with negligible empirical cost extends this theoretical connection into a practically deployable method. The unexplained but reproducible finding that M=1 Monte Carlo sampling is not only sufficient but *optimal* for KFAC estimation in this context (with performance degrading at M>2) is an intriguing empirical observation that, if explained, could have broader implications for how KFAC estimates are calibrated in transfer learning pipelines.

---

## Suggestions

1. **Justify or revise the asymmetric λ_t placement in Eq. (8)**: Either provide an informal argument for why placing λ_t on A rather than B (or symmetrically on both) is appropriate, or ablate alternative weighting schemes to demonstrate this choice's robustness.

2. **Analyze the task negation advantage**: Given the substantially larger margin over τJp in negation vs. addition (Tab. 2 vs. Tab. 1), add even a paragraph-level analysis. Does negation amplify curvature quality differences? Is the gain correlated with task-vector magnitude or overlap?

3. **Report ViT-L/14 KFAC storage**: Add a row or note to the compression section (Fig. 7b) reporting full and compressed KFAC memory for ViT-L/14, given it is the largest and best-performing tested architecture.

4. **Investigate MC sample degradation**: Analyze why performance drops as M increases beyond 1-2. A brief seed-interaction analysis (fixed vs. varied seeds across MC draws) would help clarify whether this is a stochastic artifact or a systematic over-regularization effect.

---

**Evaluation axes:**

- **Originality**: Strong. The GGN-representation drift connection is non-obvious and enables a principled design. The O(1) accumulation scheme is a practical contribution.
- **Importance**: High. Dataless task arithmetic regularization addresses a genuine privacy and modularity constraint in deployed systems.
- **Claims well-supported**: Yes. Tables 1–3 and Figures 4–8 collectively provide comprehensive support for all main claims (accuracy, efficiency, robustness, localization, compression).
- **Soundness of experiments**: Good. Three model scales, two modalities, multiple baselines, ablations on key hyperparameters. Minor gap in ViT-L/14 memory and unexplained MC saturation behavior.
- **Clarity**: High. Derivations are well-organized. Algorithms 1 and 2 cleanly separate idealized from practical components.
- **Community value**: High. Immediately applicable to privacy-constrained model merging; the KFAC pre-computation and sharing paradigm is practically deployable.

---

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>