- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3
Good. I now have a thorough understanding of the paper and all the verification needed. Let me produce the consolidated review.

## Summary

This paper reinterprets hard-thresholding gradient methods as equivalent biased gradient algorithms, categorizes gradient biases into memory-biased (BSVRG, BSAGA) and recursive-biased (SARAH), and analyzes how these biases interact with the inherent bias from the hard-thresholding operator. The authors propose SARAH-HT for first-order and BVR-SZHT for zeroth-order hard-thresholding, and provide convergence theorems plus limited experimental results.

## Strengths

- **Novel conceptual framework.** Lemma 1 derives an inequality that treats the combined gradient-and-threshold step as a single "equivalent gradient" ∇_{HT}^t, reformulating hard-thresholding as a biased gradient algorithm. This is a genuinely new perspective relative to prior work that treats the gradient oracle and hard-thresholding operator separately.

- **Formal categorization of bias structures.** Definitions 1 and 2 formally define memory-biased and recursive-biased gradient oracles, and Lemmas 2–6 analyze how each bias type interacts with hard-thresholding bias in first-order and zeroth-order settings. Remarks 4 and 7 articulate the predicted cancellation effects (recursive bias counteracts hard-thresholding bias in first-order; memory bias counteracts zeroth-order bias), which are the paper's central analytical claims.

- **Black-box adversarial result.** The experiment in Figure 1 (BVR-SZHT vs. VR-SZHT on a few-pixel universal perturbation of CIFAR-10) provides a concrete demonstration that BVR-SZHT achieves lower loss than VR-SZHT, consistent with the claim that memory bias helps in the zeroth-order setting.

## Weaknesses

### Fatal
None. The conceptual contribution has merit even though the execution is insufficient.

### Major
- **Undefined parameters in core theorems.** Theorems 1 and 2 use λ′ (lines 255, 271) with no definition; Theorem 1 uses B₂ (line 261) while only B₁ is defined; Theorem 1 references ρ_B (line 252) without definition; k^* (used in Lemma 1's γ_k = √(k^*/k)/2) is not defined before its first use; K in Theorem 3 (line 302) is never defined. These missing definitions mean the convergence bounds cannot be evaluated as stated — the theoretical core is incomplete.

- **Experimental evaluation is far too limited to support the central claims.** The black-box adversarial experiment uses only 10 images from CIFAR-10, compares BVR-SZHT to exactly one baseline (VR-SZHT), and reports no confidence intervals, multiple runs, or statistical significance. The sparse feature selection experiment (Table 1) is described only in generic qualitative terms ("demonstrate the effectiveness of these methods") with no readable numerical results in the extracted text and no error bars. No experiments at all validate the first-order claims (SARAH-HT convergence speed), despite this being a core claimed contribution. The paper's central conclusion — "faster convergence compared to existing methods" — lacks sufficient empirical support.

- **Sign inconsistency between Lemma 1 and Lemma 2.** Lemma 1 gives coefficient (γ_k − ½) (line 123), while Lemma 2 writes (½ − γ_k) (line 168). These are negatives of each other; the paper does not explain the sign change, making it unclear whether Lemma 2 correctly follows from Lemma 1 or contains an error.

- **Expectation vs. determinism gap in the bias-cancellation derivation.** The derivation that recursive bias "partially cancels" hard-thresholding bias (lines 173–187) relies on the claim (∇_F f(x^{νs}) − g(x^{νs}))_F = 0. However, Definition 2 only guarantees ∇f(x_k) − 𝔼_k g(x^t) = 0 for k ∈ νℕ₀ — an in-expectation property. The paper uses it as a deterministic equality without justification. (For SARAH specifically the deterministic equality does hold by construction, but the paper does not clarify this, and the derivation is written as if it follows from Definition 2 alone, which is insufficient as presented.)

- **Only one of the two predicted cancellation effects is empirically tested.** The paper predicts (a) recursive bias cancels hard-thresholding bias in first-order and (b) memory bias cancels zeroth-order bias. Only (b) receives any experimental attention (Figure 1), and that with minimal baselines. Claim (a) — the basis for SARAH-HT — is empirically unvalidated. No comparison of SARAH-HT against StoIHT, SVRG-HT, or ordinary IHT is provided.

### Minor
- **Duplicated paragraph in the introduction.** Lines 30–31 and line 32 contain near-verbatim text on biased gradient oracles with the same references, indicating poor editing.
- **Abstract uses "we believe" (line 4) rather than reporting established findings.** For a submission presenting theoretical results, the language should reflect the strength of the claims.
- **Minor figure reference inconsistency.** The text references "Figure 5" (line 386) but the caption reads "Figure 1" (line 389).
- **Several lemmas have limited contextual interpretation.** Lemma 4 (memory-biased first-order) and Lemma 6 (memory-biased zeroth-order) present bounds but the text does not clearly explain how the bounds support the claimed cancellation effects beyond brief remarks.

### Trivial
None that are not already captured above.

## Nice-to-Haves
- Sensitivity analysis for the bias parameter θ (the main innovation) would strengthen the empirical case.
- Testing on more than 10 images and reporting results with error bars is standard practice for empirical ML papers.
- Including first-order algorithm comparisons (SARAH-HT vs. StoIHT, IHT, SVRG-HT) would verify the core theoretical claim.

## Removed Points

**These points are flagged to be removed; treat them with caution:**

1. *Harsh critic's claim that "no code is provided to verify the claims"* — Code availability is not expected in a submission under review.
2. *Harsh critic's claim about "overstated novelty relative to Yuan et al. (2024)"* — Cannot verify external works; removed per instruction not to discuss missing related works.
3. *Harsh critic's claim that "BSVRG-HT, BSAGA-HT are not tested"* — The paper explicitly states these were tested in the sparse feature selection experiment (line 391); the results are in Table 1 (an unreadable image, but the experiment exists).
4. *Harsh critic's claim about "Theorems 1 and 2 contain the same structural template... making them meaningless"* — The theorems sharing a template is a deliberate design choice; the core issue is the undefined parameters, which is already captured.
5. *Strength Finder's hallucinated specific accuracy numbers (78.6%, 73.9%, 63.7%) from Table 1* — These numbers do not appear anywhere in the paper text; they are fabricated by the strength finder.
6. *Strength Finder's claim that BVR-SZHT achieves "substantially lower loss"* — Downgraded to kept strength (the paper does show a lower loss, but with only one baseline and 10 images, "substantial" overstates the evidence).
7. *Harsh critic's concerns about missing appendix/supplementary experiments* — The parser strips supplementary material; cannot penalize what is not visible.
8. *Nitpicks about writing quality (typos, garbled mathematics)* — These are largely parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's strengths (the conceptual framework) and weaknesses (incomplete theoretical statements and insufficient experiments). The most informative insight from reviewing is that the undefined parameters (λ′, B₂, ρ_B) in the convergence theorems are a more concrete and verifiable problem than the reviewer's broader complaint about "sketched derivations" — the derivations may be correct but the theorems literally cannot be evaluated without those definitions.

## Suggestions

1. **Define all parameters before or at first use.** Add explicit definitions for λ′, B₂, ρ_B, k^*, and K. Ensure every symbol in every theorem appears in a definition table or is defined in the surrounding text.
2. **Fix the sign inconsistency in Lemmas 1–2.** Either correct the sign or provide an explanation of how Lemma 2's (½ − γ_k) follows from Lemma 1's (γ_k − ½).
3. **Clarify the deterministic status of the recursive-bias reset.** State explicitly that for SARAH, g(x^{νs}) = ∇f(x^{νs}) deterministically, and explain why the in-expectation property in Definition 2 is sufficient (or not) for the derivation.
4. **Substantially expand the experiments.** At minimum: (a) compare SARAH-HT against StoIHT, IHT, and SVRG-HT on synthetic sparse regression with known ground truth, reporting mean and standard deviation across ≥5 seeds; (b) run the black-box adversarial attack on ≥100 images with multiple runs and report error bars; (c) include sensitivity analysis for the bias parameter θ to directly test the predicted cancellation effects.
5. **Remove the duplicated paragraph in Section 1** and proofread the manuscript for consistency (e.g., "Figure 5" vs. "Figure 1").
6. **Replace "we believe" in the abstract with a definitive statement** commensurate with the evidence presented.
