Now I have a thorough understanding of the paper, the critic reviews, and calibration anchors. Let me produce the final consolidated review.

---

## Summary
KOALA proposes a novel adversarial detection mechanism that flags inputs when class predictions from two complementary similarity metrics—KL divergence (sensitive to dense, low-amplitude shifts) and a thresholded L0-based score (sensitive to sparse, high-impact changes)—disagree. The method is lightweight: it replaces a standard classifier head with a nearest-prototype classifier evaluated under two metrics, and requires only clean-image fine-tuning. The paper claims a formal proof that under certain conditions, no norm-bounded perturbation can simultaneously fool both metrics, guaranteeing detection. Experiments on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet validate the approach through ablation studies across metric combinations.

## Strengths
- **Novel detection principle**: Using disagreement between two complementary similarity measures (KL for dense shifts, L0-based for sparse shifts) as an adversarial detection signal is intuitive, well-motivated, and genuinely novel in the detection literature. The insight that adversarial perturbations under an energy budget manifest as either dense or sparse changes provides a clear geometric rationale (Figure 1, Section 3.1).

- **Strong ablation evidence for the KL+L0 pairing**: The ablation study (Experiment 2, Table 2) shows that KL+L0 achieves the highest precision (0.94) and recall (0.81) among all tested metric combinations on ResNet/CIFAR-10, providing convincing evidence that these two metrics are indeed complementary.

- **Lightweight, clean-only training preserves clean accuracy**: The fine-tuning procedure uses only clean images and maintains 94.96% clean accuracy on ResNet-18 (Table 3), demonstrating that the method does not degrade the backbone's core classification ability.

- **Attempt at theoretical grounding**: The paper goes beyond purely empirical detection methods by attempting to provide formal conditions under which detection is guaranteed (Theorem 1, Propositions 2-4, Appendix B). This ambition distinguishes the work from most prior detection papers, even though the practical utility of the guarantee is limited (see Weaknesses).

## Weaknesses

### Fatal
None.

### Major
- **The theoretical guarantee is significantly oversold and its empirical validation is circular**: Theorem 1 states that *if* a sufficient coordinate gap exists between prototypes (|c\*_i − ĉ_i| > Γ_i(ϵ)), *then* detection is guaranteed. The condition depends on the adversarial target class ĉ, which is unknown at test time, making it a post-hoc criterion rather than a deployable guarantee. Experiment 1 then splits the test set into Theorem-Compliant and Non-Compliant subsets based on whether this very condition holds, and finds perfect detection on the compliant subset (recall = 1.0, Table 1). This is a tautological verification: the subset is defined by the property the theorem says guarantees detection. The paper does not report the fraction of inputs that satisfy the condition at deployment time, nor does it bound the failure rate in terms of measurable pre-deployment properties. The abstract's claim of "formal proof of correctness" sets expectations the actual mathematics does not meet.

- **No comparison to any existing adversarial detection method**: The paper evaluates only ablations of its own metric combinations (L0+Cosine, KL+Cosine, KL+L0+Cosine). It does not compare KOALA against a single prior detection approach—LID, feature squeezing, NIC, Mahalanobis, MagNet, or any of the many methods surveyed in the related work. Without such baselines, there is no evidence that KOALA offers competitive or complementary performance. The claim that KOALA is a "valuable complement to existing robust training and certification methods" is unsupported.

- **No evaluation against adaptive attacks**: The attack suite (PGD, CW, AutoAttack) is standard for evaluating classifiers, but for a detector with a known decision rule (disagreement between KL and L0 predictions), an attacker can attempt to craft perturbations that keep the two predictions aligned. The paper never considers such an adaptive adversary. Without this, the reported detection rates cannot be interpreted as true robustness.

### Minor
- **The L0 metric is a heuristic, not a true L0 count**: Equation (2) defines the L0-based metric as a thresholded count relative to the mean absolute deviation, with a fixed τ = 0.75. This is a design choice that depends on the threshold parameter; the connection to the "sparse, high-impact" motivation is indirect. The paper acknowledges this implicitly but does not analyze sensitivity to τ.

- **The proof is dense and its practical import is unclear**: Appendix B derives a complex bound for the required coordinate gap Γ(ϵ) (culminating in Eq. 49/84-85). The derivation is notationally heavy, and the paper provides no analysis of whether this bound is satisfied in realistic settings, what typical magnitudes of the quantities involved are, or how the bound relates to the fixed τ = 0.75 used in experiments.

- **No error bars or hyperparameter sensitivity**: Detection performance depends on τ and the smoothness parameter φ, but no sensitivity analysis is reported. Standard deviations across runs are absent.

### Trivial
- **Detection evaluation protocol is unconventional**: The paper merges classification correctness and attack detection into a single confusion matrix (Equations in Section 4.2). A conventional separate evaluation (AUROC, TPR at fixed FPR) on clean vs. adversarial pairs would aid interpretability.

## Nice-to-Haves
- Feature-space visualizations (e.g., t-SNE) of clean and adversarial embeddings relative to prototypes, highlighting where the two metrics agree/disagree, would help readers understand when and why the detector works.
- Quantification of how often the theorem's conditions hold in practice: a distribution of coordinate gaps across the test set, and whether τ = 0.75 satisfies the derived inequality.
- Extension to adaptive white-box attacks that directly optimize for agreement between the two metrics.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's claim about "not a true count of perturbed coordinates but a heuristic"** — This is factually correct but is explicitly described in the paper (Eq. 2, Section 3.1), not hidden. The paper never claims it's a standard L0 norm. Moved to Minor.

- **Harsh critic's claim about Assumption A3 being unrealistic on small softmax outputs** — The paper states A3 as |δ_i| ≤ 3/2 |p_i\*|. The critic says this may be restrictive on small p_i\*. This is a reasonable theoretical concern but is more of a proof-technical limitation than a practical flaw, as the assumption is standard in bounding Taylor remainders. Weakened and folded into the Minor weakness about the proof's practical import.

- **Strength Finder's "Formal proof of correctness with direct empirical validation"** — The empirical validation is circular (as discussed under Major weaknesses). The theoretical contribution is real but limited. Strength has been qualified.

- **Strength Finder's generic claims** — "This paper addressed an important problem," "targeted an interesting question" — these are generic and lack specific evidence. Removed.

- **Harsh critic's concern about missing appendix or absent references** — The parser strips appendices; the original submission includes them. Removed per instructions.

- **All formatting/typo complaints** — These are parser artifacts. Removed per instructions.

## Novel Insights
The most genuinely novel observation from this work is the explicit geometric characterization of how adversarial perturbations under an energy budget naturally split into two regimes—dense/low-amplitude and sparse/high-impact—and that these regimes are naturally captured by distributional (KL) vs. coordinate-wise (L0-based) metrics respectively. The formal attempt to prove that these two metrics impose incompatible requirements on any single perturbation is a fresh perspective not seen in prior detection work. Even though the resulting guarantee is practically limited, the conceptual framework of "prediction stability bands" that are mutually exclusive for adversarial perturbations is a valuable lens through which to think about detection.

## Suggestions
- **Reframe the theoretical contribution honestly**: Instead of claiming a "formal proof of correctness," acknowledge that Theorem 1 provides an *existence result* showing that the two metrics have fundamentally incompatible requirements for a successful simultaneous attack. Characterize when the conditions hold in practice (e.g., what fraction of inputs satisfy the coordinate-gap condition for typical τ) rather than using the condition to post-hoc partition the test set.

- **Add comparisons to at least 2-3 standard detection baselines** (e.g., LID, Mahalanobis, feature squeezing) to establish whether KOALA's detection performance is competitive.

- **Evaluate against an adaptive attack** that explicitly tries to keep KL and L0 predictions aligned (e.g., by adding a penalty for prediction disagreement to the attack objective).

- **Report detection AUROC and TPR at fixed FPR** separately from classification accuracy for clearer interpretation.

## Score and Decision

**Anchor comparison:**

| Path | Topic | Avg Score | Decision | Comparison |
|------|-------|-----------|----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/UlMCtFDBRn.md` | Adversarial detection for radiology | 2.50 | Reject | KOALA is substantially stronger: it has a theoretical framework, principled method design, and better ablation experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/64PMEKVZP1.md` | Prediction inconsistency detection | 2.67 | Reject (Withdrawn) | Similar disagreement-based detection concept, but KOALA adds theoretical grounding and clean-only training. KOALA is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/7s3SQMiN3L.md` | Gradient manifold ID detection | 3.00 | Reject (Withdrawn) | Both have novel geometric perspectives; KOALA has better empirical validation. |
| `/home/wg25r/review_agent/human_reviews_2026/CSfcpGj48W.md` | Conformal novelty detection | 4.00 | Reject (Withdrawn) | Both attempt formal guarantees. KOALA's is more directly tied to its mechanism but similarly limited in practical applicability. Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/Mr9a9XuLTI.md` | "A Few Large Shifts" detection | 4.50 | Reject (Withdrawn) | Most similar anchor. Both are lightweight, plug-in, theory-grounded detectors. That paper had baseline comparisons and adaptive attacks; KOALA lacks both. KOALA is weaker on empirical validation. |
| `/home/wg25r/review_agent/human_reviews_2026/bTcFHJo1Zk.md` | MGT detection with AT | 5.00 | Accept (Poster) | Different domain. Strong SOTA comparisons and comprehensive experiments. KOALA's empirical evaluation is much weaker. |
| `/home/wg25r/review_agent/human_reviews_2026/uWvLZqxjmx.md` | Natural adversarial diffusion | 5.50 | Accept (Poster) | Different domain entirely. Well-executed experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/lL6htAaolp.md` | Adversarial training for diffusion | 6.00 | Accept (Poster) | Much more polished: clear motivation, principled formulation, comprehensive experiments. KOALA is far below this standard. |
| `/home/wg25r/review_agent/human_reviews_2026/ktGmDGoWnB.md` | Obfuscated activations | 6.00 | Accept (Poster) | Strong, well-executed paper. KOALA not in same tier. |

KOALA is clearly stronger than the low-band papers (2.50–3.00) and is most comparable to the 4.00–4.50 band. It has a more principled theoretical attempt than the "A Few Large Shifts" paper (4.50) but critically lacks baseline comparisons and adaptive attack evaluation that even that rejected paper included. I place KOALA at approximately 4.0: the novel idea and theoretical ambition are real contributions, but the empirical gaps (no baselines, no adaptive attacks) and the oversold theoretical guarantee prevent acceptance.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>