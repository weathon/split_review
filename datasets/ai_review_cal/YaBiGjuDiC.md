- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 6, 5, 5
## Summary

This paper identifies and analyzes a fundamental issue in margin-based preference optimization for language model alignment: because the loss only constrains the *margin* between chosen and rejected log-probabilities, the individual trajectories of these probabilities are under-specified, leading to synchronized increases or decreases of both. The authors derive a gradient inner-product condition that governs this behavior, show how it manifests across a range of algorithms (DPO, SPPO, KTO, SimPO, CPO, DPOP, etc.), and theoretically analyze when the condition is violated in toy settings (shared suffix tokens cause the gradient inner product to become large). Empirical validation on TL;DR and synthetic sentiment tasks confirms the predicted dynamics.

---

## Strengths

- **Derivation of the gradient entanglement condition for DPO (Section 3.1):** The analysis of Equation (3) derives the exact log-probability change after one gradient step, showing that both chosen and rejected log-probabilities move in the same direction when the gradient inner product \(\langle\nabla\log\pi_w,\nabla\log\pi_l\rangle\) is large relative to the individual gradient norms. This provides a clean, causal mechanism for the paper's central claim.

- **Unified framework covering multiple algorithms (Section 3.2, Table 2):** The paper embeds DPO, SPPO, KTO, SimPO, CPO, DPOP, RRHF, and Slic-HF into a general loss form with regularization, and derives the corresponding gradient conditions (\(d_w/d_l\) ratios). This framework explains *why* different algorithms exhibit different log-probability dynamics (e.g., why SPPO and explicitly-regularized methods avoid the simultaneous decrease that DPO suffers), supporting the claim that the pitfall is structural to the margin-based paradigm rather than specific to one algorithm.

- **Theoretical analysis linking response-pair structure to gradient entanglement (Section 4.1):** Theorem 1 and Corollary 2 show that when responses differ only at the last token, the gradient inner product is negative and ideal behavior occurs. Theorem 3 shows that a shared suffix following the differing token causes the chosen log-probability to decrease — and the decrease grows with suffix length. This directly connects specific response-pair patterns to the failure mode.

- **Empirical validation with both sentence-level and token-level gradient measurements (Section 4.2):** The sentiment-task experiments (Figures 3 and 4) verify all three theoretical predictions: chosen log-probability increases only in the single-token case, decreases more with longer suffixes, and the gradient cosine similarity rises with suffix length. The token-wise heatmap (Figure 4b) directly visualizes the mechanism — contrasting tokens have negative gradient similarity while identical tokens have near-unity similarity.

- **Clear explanation of algorithmic differences (Section 3.2.1):** The paper uses the derived gradient conditions to explain why SPPO, SimPO, and explicitly-regularized methods (CPO, DPOP) mitigate the decrease in chosen log-probability while DPO does not, demonstrating explanatory power beyond a single algorithm.

---

## Weaknesses

### Fatal
None.

### Major

None. The core analytical contributions are sound and supported. The limitations described below are addressable.

### Minor

- **The one-step gradient condition is used to explain full training trajectories without bridging the gap.** The derivations (Conditions 1, 2) characterize a single gradient step under a small-step-size approximation, yet the paper uses them to explain the entire multi-step training dynamics in Figures 1–2. The paper's own figures show non-monotonic behavior (e.g., DPO chosen log-probability goes up then down in Figure 2) that a condition at initialization cannot predict. The paper states that results "closely align" but provides no quantitative measurement (e.g., gradient cosine similarity over time, as done in Figure 4a for the sentiment task) to confirm that the condition continues to hold at later steps. This weakens the claimed explanatory link between theory and the main empirical results.

- **No multiple-seed or variance reporting for the TL;DR experiments.** The paper shows one trajectory per algorithm (Figures 1–2) without reporting variance across random seeds, data shuffling, or hyperparameter sensitivity. Readers cannot assess whether the observed patterns are robust. This is a standard reproducibility expectation for a paper making general claims about training dynamics.

- **Safety implications are invoked as motivation but not empirically evaluated.** The abstract and introduction frame the finding as relevant to "potential safety alignment failures" and "safety-critical alignment tasks," but the paper never tests whether the observed log-probability increases of rejected responses actually lead to more harmful generations in practice. The paper is clearly an analytical/diagnostic contribution, and the safety language is appropriately hedged ("potential," "may"), but the motivational framing implies a practical consequence that goes untested. A small-scale evaluation on a safety dataset (e.g., checking whether increased rejected log-probability correlates with harmful sampling) would strengthen the practical relevance.

- **Theoretical models, while acknowledged as toy settings, eliminate key structures of real LMs.** Model Setup 2 (Section 4.1.2) removes parameter sharing across token positions entirely (learnable logits per position), which is a major departure from transformer architecture with tied embeddings and shared representations. The paper states it is using "a simpler setting" to build intuition, which is fine, but it does not discuss whether the conclusions (e.g., Theorem 3's result about shared suffixes causing chosen log-probability decrease) would survive under realistic parameter sharing. A brief discussion of this limitation would help readers calibrate the generality of the theoretical claims.

### Trivial
- The gradient inner product is computed for the sentiment-task experiments (Figure 4a), but the paper does not specify how it was computed (e.g., full model vs. last layer, per-token vs. per-response). Adding a brief methodological note would aid reproducibility of those experiments.

---

## Nice-to-Haves
- **Gradient cosine similarity over training for the TL;DR experiments.** Computing and plotting this (analogous to Figure 4a) would quantitatively bridge the gap between the one-step condition and the full training trajectory, substantially strengthening the explanatory claim.
- **A controlled experiment that *predicts* a difference between algorithms** (e.g., "on this fixed data where gradient inner product is high, DPO should decrease chosen log-probability while SPPO should increase it") and then tests that prediction. The paper shows this qualitatively but a more controlled test would be more convincing.
- **A concrete proposal or sketch of a token-level method** beyond the brief mention in the implications section.

---

## Removed Points
*These points were raised in the reviews but are not included as weaknesses in the finalized assessment. They are preserved here in case they are useful during discussion.*

- **"Table 2 referenced but not visible" / "Missing appendix content":** The appendix and its tables are stripped by the PDF parser; they exist in the original submission. Removed per instructions.
- **"Derivations of d_w and d_l are presented without showing all algebraic steps":** This is a presentation-style nitpick that does not affect the correctness or reproducibility of the paper. The derivations are sufficiently clear for a conference paper. Removed.
- **"Gradient inner product computation not specified for TL;DR experiments":** The TL;DR experiments do not compute gradient inner products — they show log-probability trajectories. The critic assumed the paper should have computed this, but the paper does not claim to have done so. The gradient inner product *is* computed for the sentiment experiments (Figure 4a), and the methodology there is implicit in the cosine similarity formula. Removed.
- **"Safety assertion is made without support":** The paper uses appropriately hedged language ("potential," "may") and makes a clear analytical contribution. The safety implications are logical extrapolations of the mechanism, not empirical claims. The point has been downgraded to a Minor weakness about untested practical consequences, which is a genuine limitation. The stronger framing ("the paper should stop invoking safety failures without evidence") is removed as overblown.

---

## Novel Insights
None beyond the paper's own contributions. The reviews surface the gap between one-step theory and multi-step dynamics, and the lack of downstream safety evaluation, but these are standard limitations that the authors would be expected to address in future work rather than genuinely novel observations.

---

## Suggestions
1. **Report variance across at least 3 random seeds** for the TL;DR log-probability trajectories, or at minimum state that results are from a single run and note this as a limitation.
2. **Measure and plot the gradient cosine similarity over training** for the TL;DR DPO experiment (analogous to Figure 4a) to quantitatively connect the one-step condition to the full dynamics.
3. **Add a brief limitations paragraph** (potentially at the end of Section 4 or in Section 5) explicitly discussing: (a) the gap between the one-step analysis and multi-step training; (b) the lack of parameter sharing in Model Setup 2 and what this means for generalizability; (c) that the safety implications are logically deduced but not empirically verified.
4. **Clarify the gradient computation methodology** for the sentiment-task experiments (e.g., "gradients were computed with respect to the full model parameters" or "only the last linear layer").

---
