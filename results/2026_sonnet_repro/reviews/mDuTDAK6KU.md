Now let me do calibration searches to position the score.Round 1 bracket: **3.5–5.5**. The paper has a formal theorem, clean experiments, and a novel detection idea, but lacks baseline comparisons and has non-standard metrics — weaker than accepted 5.5 papers but better than the 2–3 reject papers. Let me narrow within this bracket.Let me read two key anchors at my bracket boundaries to finalize the score.Now I have sufficient calibration to write the final review and score.

**Comparison summary:**
- **SPADE (5.50, Accept)**: Also detection with formal guarantees; tested against multiple baselines (KNN, MSP), multiple architectures and datasets. Accepted despite only using FGSM. KOALA is weaker than SPADE: completely lacks baseline comparisons, has lower theorem coverage, and the CLIP results contradict the thesis.
- **NEARSIDE (4.00, Reject)**: Detection for VLMs; flawed evaluation (missing benign queries, no adaptive attacks, one baseline). KOALA is stronger than this: rigorous formal theorem, three standard attacks (PGD/CW/AutoAttack), well-motivated design.

**Round-1 bracket: 3.5–5.5. Round-2 narrowed to 3.5–4.5.** KOALA lands at **4.0** — below the accepted threshold due to the critical missing baseline comparison and CLIP contradictions, but above the 2–3 papers due to its genuine theorem and structured experiments.

---

## Summary

KOALA proposes a semantics-free adversarial detector that flags inputs when predictions from two complementary nearest-prototype classifiers — one using KL divergence (sensitive to dense, low-amplitude perturbations) and one using a custom L₀-based distance (sensitive to sparse, high-impact changes) — disagree. The paper provides a formal theorem (Theorem 1) showing that under sufficient inter-class prototype separation and mild assumptions, the two metrics' stability bands are mutually exclusive, guaranteeing detection. A lightweight clean-images-only fine-tuning procedure is proposed to encourage this required geometric structure. Experiments span ResNet-18/CIFAR-10 and CLIP ViT-B/32/Tiny-ImageNet under PGD, CW, and AutoAttack.

---

## Strengths

1. **Formal theorem with explicit derivation (Theorem 1, Section 3.2)**: The paper proves via three propositions (Prop. 2–4) that satisfying the KL-flip condition and the L₀-flip condition simultaneously under a shared energy budget is impossible when inter-class prototype separation is sufficiently large. This is a genuine theoretical contribution differentiating KOALA from purely empirical detectors.

2. **Perfect detection on theorem-compliant subsets (Table 1)**: Across all tested settings (ResNet ε=2/255, ε=4/255; CLIP ε=2/255, ε=4/255), the theorem-compliant subsets achieve accuracy, precision, recall, and F1 all equal to 1.0 under PGD. This provides concrete empirical validation of the theoretical guarantee.

3. **Ablation study validates KL+L₀ complementarity on ResNet (Table 2)**: The systematic comparison of metric pairs on ResNet/CIFAR-10 shows KL+L₀ achieves the highest accuracy (0.88), precision (0.94), recall (0.81), and F1 (0.87) under PGD ε=2/255, outperforming L₀+Cosine, KL+Cosine, and the three-metric combination — directly supporting the design rationale.

4. **Adversarial accuracy improvement from clean-only fine-tuning (Table 3)**: KL+L₀ fine-tuning on ResNet achieves 57.32% adversarial accuracy vs. the 45.5% baseline under PGD ε=2/255, a +11.8 pp improvement without any adversarial training examples.

---

## Weaknesses

### Fatal
None.

### Major

- **No comparison to any existing adversarial detector.** The related work section cites Feature Squeezing (Xu et al., 2018), LID (Ma et al., 2018), MagNet (Meng & Chen, 2017), Mahalanobis (Lee et al., 2018), NIC (Ma & Liu, 2019), and CADet (Guille-Escuret et al., 2023) — yet not a single one appears in the experiments. The ablation study (Table 2) only compares KOALA metric variants against each other. Precision 0.94 / recall 0.81 on ResNet/CIFAR-10 is uninterpretable without a reference point. This is the central empirical gap: without at least two or three baseline comparisons (Feature Squeezing and Mahalanobis would be natural), the claim that KOALA "consistently and effectively detects adversarial examples" cannot be substantiated relative to the state of the art.

- **Theorem coverage is severely limited for CLIP (~10–11%).** Table 1 reveals that on CLIP/Tiny-ImageNet, only 510–556 out of ~5000 test samples satisfy Theorem 1's conditions (~10–11%), leaving ~89–90% of inputs without theoretical guarantees. On ResNet/CIFAR-10 at ε=4/255 it falls to ~59%. The abstract states "we provide a formal proof of correctness" and Section 3.2 states "detection is not a probabilistic outcome but a mathematical certainty," both without qualification. These phrases substantially overstate the practical scope of the guarantee given the empirical compliance rates.

- **CLIP results contradict the core thesis.** Table 4 shows that for CLIP, L₀-only achieves far better adversarial accuracy than KL+L₀ across all attacks (e.g., CW ε=2/255: L₀-only 37.49% vs. KL+L₀ 11.91%; KL-only: 25.69%). The paper's post-hoc explanation — that CLIP's pre-training sparsity-aware structure makes L₀-only especially effective — is plausible but unverified. More importantly, this finding directly contradicts the paper's core thesis that KL and L₀ are generally complementary. On CLIP their combination is actively harmful to adversarial accuracy by a wide margin.

- **No evaluation against adaptive adversaries.** The paper evaluates only PGD, CW, and AutoAttack — all attacks targeting the original classifier, not KOALA. An adaptive adversary who knows KOALA would craft perturbations that simultaneously align the embedding with both the KL-adversarial-class direction and the L₀-adversarial-class prediction. Reporting only non-adaptive attacks does not establish robustness against a KOALA-aware adversary. Theorem 1 provides some guarantee, but only for ~10–60% of inputs depending on setting, under unverified assumptions.

- **Non-standard confusion matrix conflates detection success with attack failure.** Section 4.2 defines TP := [a=1] ∧ [(â,ŷ)=(1,⊥) ∨ (â,ŷ)=(0,y*)]. The second disjunct — (â,ŷ)=(0,y*) — counts adversarial examples that KOALA does *not* flag as attacks but that happen to be correctly classified (attack failed). This mixes detection success with classification resilience. Standard adversarial detection papers define TP purely as detected attacks. The reported precision and recall numbers cannot be directly compared with prior literature, obscuring where KOALA actually stands on detection alone.

### Minor

- **Theorem compliance on CLIP is achieved without the fine-tuning's stated purpose (Section 4.3).** The paper's Section 4.3 admits that the high detection recall under L₀+KL+Cosine on CLIP arises from the model "breaking the underlying classification" — causing all three heads to behave near-randomly. This severs the connection between the theorem (which requires clean-input alignment, A4) and the observed detection rates on the non-compliant 89% of CLIP inputs.

- **τ hyperparameter (τ=0.75) lacks ablation.** The threshold τ in the L₀ metric is set to 0.75 without any ablation across values or discussion of sensitivity. Given that τ directly governs what counts as a "significant" coordinate change (Eq. 2) and feeds into Theorem 1's conditions, its choice has both methodological and theoretical implications.

### Trivial

- The proof sketch in Section 3.2 covers only the direction "L₀ flip leaves insufficient energy for KL flip." A dense, low-amplitude perturbation that aligns with ĉ − c* (satisfying KL flip) while remaining below the per-dimension L₀ threshold is not explicitly addressed in the sketch. The full proof is in the appendix, so this is a presentation gap rather than a verified flaw.

---

## Nice-to-Haves

- Adding even two baseline comparisons (Feature Squeezing and Mahalanobis, both operating on embeddings without adversarial retraining) would establish relative performance without major experimental overhead.
- Reporting theorem compliance rates before vs. after fine-tuning would directly connect the fine-tuning procedure to Theorem 1's required conditions, strengthening the theoretical narrative.
- Separating detection metrics (pure AUROC/TPR-at-FPR) from classification metrics would make KOALA's results directly comparable to prior detection literature.
- A brief analysis of what geometric factors determine theorem compliance (dataset size, embedding dimension, ε magnitude) would strengthen the practical applicability section.
- The proof sketch should be extended to explicitly address the dense-perturbation path to L₀ stability.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "A3 is extremely tight and potentially tighter than the ℓ∞ perturbation budget"** — The argument that |δᵢ| ≤ (3/2)|pᵢ*| is extremely tight depends on unspecified Lipschitz constants of the encoder and how the ℓ∞ pixel-space budget translates to feature space. The paper explicitly calls A3 "mild and practical" and notes that "extremely large coordinate-wise perturbations are rarely effective or imperceptible." The claim that this is violated in practice is speculative and not verifiable from the paper.

- **Harsh Critic: "An adversary can trivially violate A3 by concentrating energy on small-valued coordinates"** — This is a speculative attack strategy not demonstrated in the paper. Demoted to trivial/speculative; cannot be verified from the paper as written.

- **Harsh Critic: "The incompatibility argument (Prop. 4) does not close the dual direction"** — The proof sketch says full details are in Appendix B; per the rules, criticisms based on an absent appendix (stripped by the parser) must be removed. The incompleteness concern may be legitimate but cannot be confirmed without the appendix.

- **Strength Finder: "Adversarial accuracy improvement corroborates robustness beyond detection" as a general strength** — The CLIP results (Table 4) contradict this: KL+L₀ substantially underperforms L₀-only on CLIP adversarial accuracy. The strength is only valid for ResNet; accepted in a qualified form in the Strengths section.

- **Strength Finder: "Clear motivation and architecture exposition (Figures 1 and 2)"** — Dropped as a generic presentation strength. Not substantial enough to list.

---

## Novel Insights

The paper's core observation — that energy-bounded adversarial perturbations necessarily manifest as either dense/low-amplitude or sparse/high-impact shifts, and that these two regimes are captured by mutually exclusive stability bands under KL and L₀ metrics — is a genuinely novel geometric framing of adversarial detection. The incompatibility proof (Propositions 2–4) that formalizes this intuition is an interesting theoretical construction. The empirical finding (Section 4.3) that high detection rates can arise from model degradation rather than the mechanism the theorem describes is an honest and insightful self-critique that should inform future work on the relationship between detection and robustness.

---

## Suggestions

1. **Add at least two established baseline comparisons** (Feature Squeezing and Mahalanobis are natural choices; they operate on embeddings and require no adversarial retraining) before resubmission.
2. **Restate the abstract and Section 3.2 claims** to reflect that the formal guarantee applies to a subset of inputs (cite the compliance rates from Table 1 directly in the abstract).
3. **Revise the confusion matrix** (Section 4.2) to use standard detection metrics (AUROC, TPR at fixed FPR) so results are directly comparable to prior work.
4. **For CLIP, provide a thorough analysis** of why the embedding geometry resists KL+L₀ structure and whether the theorem's coordinate gap condition can be made to hold with architecture-specific fine-tuning.
5. **Report theorem compliance before and after fine-tuning** to quantitatively demonstrate that the fine-tuning procedure actually achieves the coordinate gap condition.
6. **Ablate τ** (at least over τ ∈ {0.5, 0.75, 1.0}) to assess sensitivity and confirm the choice was made on validation, not test data.

---

## Score and Decision

**Anchor comparison:**
| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Adversarial detection / weak | KAWlH5pfQu.md | 3.00 | R1 | Simpler empirical approach, no formal theorem; KOALA is stronger |
| Statistical adversarial detection | kz78RIVL7G.md | 2.60 | R1 | Near-perfect detection claim, limited comparison; similar gap issues; KOALA has stronger theory |
| Adversarial robustness fragility | dIK7GpOwNY.md | 3.00 | R1 | Theoretical analysis without practical detector; KOALA is comparable or slightly stronger |
| Adversarial eigenvalue framework | YmQyEdLIkU.md | 5.50 | R1 | Formal framework with better-scoped claims; KOALA weaker (no baseline comparisons) |
| SPADE OOD+adversarial with EVT | kwCHcaeHrf.md | 5.50 | R1 | Formal guarantee + baseline comparisons + multiple datasets; KOALA clearly weaker |
| DDAD distributional discrepancy | RzdtpxL0H5.md | 6.20 | R1 | Two-pronged defense with theoretical + empirical; stronger than KOALA |
| VLM adversarial detection NEARSIDE | EWP9BVRRbA.md | 4.00 | R2 | Detection without adaptive attacks, one baseline; KOALA has stronger theorem but both lack baseline comparisons |
| Prototype OOD detection | J2we1sVd9m.md | 4.60 | R2 | OOD detection with optimal transport; also lacks adaptive attacks; KOALA comparable |
| Adversarial robustness fragility | 2ErS9Bkc3O.md | 4.50 | R2 | Theoretical analysis, no baselines, limited empirical; similar tier to KOALA |

**Round-1 bracket: 3.5–5.5.** Round-2 anchors cluster at 4.0–5.0. KOALA is:
- Clearly below SPADE (5.50, Accepted): SPADE has baseline comparisons, broader datasets, broader formal coverage
- Slightly above NEARSIDE (4.00): KOALA has stronger theorem, three standard attacks instead of a single one
- Comparable to J2we1sVd9m (4.60) and 2ErS9Bkc3O (4.50): all missing critical baselines, limited scope

The missing baseline comparison is the decisive gap — it prevents verification of the method's comparative performance. The CLIP results actively undermining the thesis and the non-standard confusion matrix compound the problem. Score: **4.0**.

**Axis assessments:**
- *Originality*: Moderate — the KL/L₀ disagreement framing is novel; the nearest-prototype classifier approach is not.
- *Importance*: Adversarial detection is important; the problem is well-motivated.
- *Claim support*: Weak — the formal theorem has limited practical scope (~10% on CLIP), and the empirical claims are unsupported without baselines.
- *Soundness of experiments*: Below standard — no baseline comparison, non-standard metrics, no adaptive attacks.
- *Clarity*: Reasonable — method is clearly described; limitations are partially acknowledged.
- *Value to research community*: Limited in current form — the core idea is worth developing, but the paper as submitted does not establish KOALA's standing relative to prior work.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>