Now I have all the information I need. Let me organize the final review.

**Round 1 bracket:** Based on the calibration, the weak anchors (avg ~1.5-3.3) are clearly below this paper. The middle anchors (avg 4.5-5.5) are most comparable. The strong anchors (avg 8) are not topically similar. Initial bracket: **5.0–7.0**.

**Round 2 narrowing:** The most directly comparable anchor is "A Theoretical Analysis of Mamba's Training Dynamics" (avg 5.0, Accept Poster, scores 6,6,6,2). Our paper is stronger — experiments directly match the theoretical model in Section 4.1, we provide a Transformer comparison, and we are more thorough about limitations. The "Mamba Can Learn Low-Dimensional Targets" anchor (avg 5.0, Reject) is weaker. The scaling laws paper (avg 5.5, Accept Poster) is comparable in quality but has different weaknesses. I place our paper above the 5.0 Mamba anchors but not significantly above the 5.5 scaling laws paper. Final score: **6.0**.

---

## Summary

This paper presents the first theoretical analysis of training dynamics and ICL generalization for a one-layer Mamba model on binary classification tasks with additive outliers. The authors prove convergence bounds (Theorem 1) and generalization guarantees for distribution-shifted prompts (Theorem 2), showing Mamba can tolerate outlier fractions up to $\min(1, p_a l_{tr}/l_{ts})$. A comparison with one-layer single-head linear Transformers (Theorems 3–4) shows the Transformer variant fails when $\alpha > 1/2$, highlighting Mamba's superior robustness. Mechanistic corollaries characterize how Mamba's linear attention selects same-pattern examples while its nonlinear gating suppresses outliers and induces a local bias. Experiments on synthetic data validate the predicted robustness gap and internal mechanisms.

## Strengths

- **First theoretical analysis of Mamba ICL training dynamics with outliers.** Theorems 1–2 provide explicit convergence and sample-complexity bounds (Eqs. 8–9) and generalization guarantees on distribution-shifted prompts (Eqs. 12–13), including a condition under which the tolerated outlier fraction can approach 1. This fills a genuine gap in the literature.

- **Clean theoretical comparison isolating the role of gating.** By comparing Mamba (linear attention + nonlinear gating) against a one-layer linear Transformer (same attention, no gating), the paper rigorously attributes Mamba's robustness advantage to its gating mechanism. The contrast in Theorem 2 (Mamba: $\alpha < \min(1, p_a l_{tr}/l_{ts})$) vs. Theorem 4 (Transformer: $\alpha < 1/2$) is a concrete, non-trivial result.

- **Mechanistic characterization via Corollaries 1 and 2.** The paper derives that trained Mamba's attention concentrates on same-pattern examples (Eq. 16) and its gating suppresses outliers while exponentially decaying with index distance from the query (Eqs. 17–18). These are directly testable predictions.

- **Experiments that directly validate the theory.** Section 4.1 uses one-layer models matching the theory exactly, reproducing the sharp robustness gap at $\alpha \approx 0.5$ vs. $\alpha \approx 0.8$ across three outlier-labeling schemes (Figure 2). Section 4.2 then checks whether the predicted mechanisms hold qualitatively in deeper models. Table 1 identifies a failure mode (CQ sensitivity) that the theory anticipates.

- **Honest treatment of limitations.** Remark 6 explicitly clarifies that the comparison is against a one-layer linear Transformer, not general Transformers, and that large Transformers with proper training can be robust. The paper repeatedly qualifies its scope.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The Transformer baseline is deliberately stripped down.** The paper compares Mamba against a one-layer single-head *linear* Transformer (no softmax, no multi-head). While the paper consistently qualifies this (Remark 6, Section 3.4), the abstract and Section 1.1 use unqualified phrases like "linear Transformers" which a reader could misinterpret as a general claim about Transformers. The paper handles this better than most — Remark 6 is unusually explicit — but some casual readers may overgeneralize the Mamba > Transformer framing.

2. **The "approaches 1" claim requires specific conditions on training length and prompt lengths.** Theorem 2(c) gives $\alpha < \min\{1, p_a l_{tr}/l_{ts}\}$. For this to approach 1, we need $p_a l_{tr}/l_{ts} \geq 1$, which requires $l_{tr} > l_{ts}$ when $p_a < 1$. In the experiments $l_{tr} = l_{ts}$, so $\alpha$ is bounded by $p_a = 0.6$. The text states this correctly (Remark 3) but the abstract's "approaches 1" claim may give an impression more general than the theorem's condition supports. This is a matter of emphasis, not incorrectness.

3. **The orthogonal pattern assumption is strong but standard.** The data model assumes all relevant patterns $\{\mu_j\}$, irrelevant patterns $\{\nu_k\}$, and outlier patterns $\{v_s^*\}$ are mutually orthogonal. This is standard in this line of work (Huang et al., 2023; Li et al., 2024a) but means the theory applies to well-separated features. A discussion of whether non-orthogonal features would break the analysis would strengthen the paper.

4. **The "linear combination of training outliers" condition (Eq. 11) is restrictive.** Theorem 2 requires test-time outliers to be positive linear combinations of training outliers. The James Bond example in Figure 1 is illustrative, but the paper does not discuss what happens when test outliers are completely novel — whether the model retains any robustness. This is acknowledged indirectly but deserves a clearer discussion.

5. **No proof sketch in the main text.** For a theoretical paper, the main text reads as a list of conditions and results without any high-level proof intuition (e.g., for Theorem 1). A short proof sketch would significantly improve accessibility.

### Trivial
- The experiments in Section 4.2 use three-layer models while the theory analyzes one-layer models. The paper frames this as qualitative validation (which is fine), but Section 4.1 already validates the theory with one-layer models. The three-layer experiments would be better positioned as a robustness check rather than a direct verification.

## Nice-to-Haves
- A direct quantification of the Mamba vs. Transformer training tradeoff (e.g., plugging in concrete values for $p_a = 0.5$, $\epsilon = 0.1$ to compare $B_M$ vs $B_T$ and $T_M$ vs $T_T$) would help readers understand the practical magnitude of Mamba's training overhead.
- A brief discussion of whether the exponential decay in Corollary 2 is an artifact of the one-layer gating formulation or a general property of Mamba.
- Experiments varying batch size to validate the predicted scaling of training requirements would strengthen the credibility of the bounds.

## Removed Points
- **Critic's claim that the paper "risks overgeneralization" about the Transformer comparison** — The paper consistently says "linear Transformer" throughout, Remark 6 explicitly clarifies the scope, and Section 1.1 states "one-layer single-head linear Transformers." This is a minor framing concern at most, not a genuine weakness beyond what is already listed as Minor #1.
- **Critic's claim that "experiments use three-layer models while the theory is for one-layer" as a major gap** — Only Section 4.2 uses three-layer models, and the paper frames this as qualitative validation. Section 4.1 uses one-layer models matching the theory exactly. This is addressed adequately.
- **Strength Finder's generic claims about the problem being "important"** — These add no specific information about the paper's content.
- **Critic's concern about missing proof sketch** — Kept as Minor #5 rather than a major weakness; it's an accessibility concern, not a correctness issue.
- **Critic's point about the "A=-I assumption"** — This is a standard simplifying assumption following Gu & Dao (2023). No need for deeper discussion.

## Novel Insights
None beyond the paper's own contributions. The review inputs do not surface any perspective on the paper's results that goes beyond what the authors already state.

## Suggestions
- Add a short (3–4 sentence) proof sketch for Theorem 1 in the main text to improve readability for a non-specialist audience.
- In the abstract and Section 1.1, add "under the condition that $p_a l_{tr} \geq l_{ts}$" when stating that the outlier fraction can approach 1, or rephrase to "can approach 1 for suitable prompt lengths."
- Add a paragraph discussing whether and how the analysis breaks under non-orthogonal patterns, or what additional technique would be needed.
- Clarify the "CQ" failure mode (Table 1): is this a practical limitation or an artifact of the one-layer analysis?

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

**Calibration report:**

Round 1 bracket: 5.0–7.0 (anchors below 3.5 are clearly weaker; middle anchors 3.5–7.5 are most comparable; anchors above 7.5 are not topically relevant).

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| AlcHdWZZoF (knowledge utilization) | 3.33 | R1 | Weaker; unrelated topic |
| uphzOS6Axo (pretraining distribution) | 3.33 | R1 | Weaker; unrelated topic |
| fz1WJWeITf (RAG as ICL) | 3.33 | R1 | Weaker; less rigorous |
| ar8EnfwITb (stable ICL bounds) | 1.50 | R1 | Much weaker |
| 2g8vgmyXgQ (nonlinear regression) | 5.00 | R1 | Comparable topic (Transformers), weaker execution |
| qA42mWsnbl (scaling laws) | 5.50 | R1 | Comparable quality, different focus |
| 1pTzWVvwEd (incremental learning) | 4.50 | R1 | Weaker; less rigorous |
| cYary8oVBv (implicit dynamics) | 5.00 | R1 | Comparable topic, weaker experimental validation |
| hvpKqEYJjj (Mamba training dynamics) | 5.00 | R2 | Most directly comparable; our paper has cleaner experiments, Transformer comparison, and clearer limitations — notably stronger |
| 3KPsog4mpy (Mamba low-dim ICL) | 5.00 | R2 | Comparable topic but weaker experiments and unnatural training algorithm — our paper stronger |
| dUwXJTF8kQ (ICL as Bayesian inference) | 5.50 | R2 | Different framing, comparable quality |
| 0GNBqoYcAP (ICL in world models) | 4.67 | R2 | Less rigorous theory |