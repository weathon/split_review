Now I have a thorough understanding of the paper. Let me write the final consolidated review.

**Verification of Harsh Critic's Claims:**

1. **Eq. 4 (Loss function):** The critic is correct that as written, the negative-class term `-(1 - log P_θ(...))` is non-standard. Standard BCE would be `-log(1 - P_θ(...))`. This is a legitimate concern — the equation appears inconsistent. However, the differentiable masking framework (HardConcrete, Louizos et al. 2018) is a well-established technique, and this is likely a typographical error in the equation rather than a flaw in the implementation. The core detection pipeline does not depend on this specific (incorrect) formulation. **Keep as Major** but note it could be a presentation error.

2. **Leakage metric definition:** The paper says "Leakage measures the attack model's accuracy in predicting sensitive tokens" but doesn't specify how this is computed for sentence-level attacks (Vec2text, GEIA) that reconstruct entire sentences. For MLC (token-level classifier), accuracy is straightforward. For sentence reconstruction, the procedure needs clarification. **Keep as Minor.**

3. **Noise variance comparison:** The critic claims Table 2 doesn't show the suppress method applied to all dimensions. But the paper explicitly states "Table 2 presents results for applying these functions across all dimensions r=100%." The critic is wrong about this — the paper does include r=100% (all dimensions) for the suppress method. **Remove/modify this criticism.**

4. **Overlap ratio (32-51%):** Valid observation that overlap is modest but performance is near-Oracle. The paper acknowledges this in Figures 4-5 and briefly discusses implicit protection. This is a genuine insight but not necessarily a weakness — it could indicate that many neuron subsets are equally effective. I'll keep this as a minor discussion point.

5. **Strength Finder strengths:** All listed strengths are concrete and supported by evidence in the paper. No generic/nonsense strengths to filter out.

6. **Other critic points:**
   - "Downstream task definition" - valid clarity point, minor
   - "Effect of k" - valid suggestion, minor
   - "Scalability" - valid observation about limitations, minor

Let me write the final review.## Summary

This paper introduces DPPN (Defense through Perturbing Privacy Neurons), a framework that protects text embeddings against inversion attacks by (1) identifying a small subset of "privacy-sensitive" embedding dimensions (neurons) via differentiable mask learning, and (2) perturbing only those dimensions with a neuron-suppressing directional noise function. Experiments across multiple datasets, attack models (Vec2text, GEIA, MLC), and embedding models (GTR-base, Sentence-T5, SBERT) show that DPPN achieves a better privacy-utility tradeoff than existing full-dimension perturbation baselines (LapMech, PurMech), reducing leakage by 5–78% while improving downstream utility by 14–40%.

## Strengths

- **Demonstrated superior privacy-utility tradeoff.** Table 1 shows that on STS12 at ε=2, DPPN reduces Leakage from 60% (unprotected) to 13%, while LapMech and PurMech only reach 22%; downstream performance is also higher for DPPN. This directly supports the claimed 5–78% less leakage and 14–40% better utility.

- **Black-box detection performs nearly as well as white-box.** Section 5.1 and Figure 4 show DPPN achieves only a 3–6% absolute difference in Leakage and less than a 5% relative difference in downstream metrics compared to DPPN-Oracle (white-box FGSM-based detection), confirming comparable performance without access to attack model internals.

- **Effectiveness on real-world sensitive data.** Table 4 reports that on MIMIC-III clinical notes, DPPN reduces sex information leakage to 17%, whereas LapMech and PurMech only reduce it to 43%. Table 6's case study further shows DPPN preserves 62% semantic similarity while protecting sensitive tokens, versus baselines dropping to 11%.

- **Validation of the privacy-neuron hypothesis.** Figure 2 shows top privacy neurons exhibit significantly higher sensitivity (average 0.04) than tail neurons (near zero), with a Wilcoxon p-value of 1.30e−21, supporting the premise that privacy information concentrates in few dimensions.

- **Neuron-suppressing perturbation is more effective than isotropic noise on the same neurons.** Table 2 demonstrates that at r=10% and ε=2, the suppress method reduces leakage by 15.44% and improves downstream by 45.12% over full perturbation, while LapMech and PurMech on the same neurons show negligible change. Figure 3 provides geometric intuition for why directional noise increases indistinguishability.

- **Robustness across diverse attack models and embedding models.** Table 3 shows DPPN consistently outperforms baselines against Vec2text, GEIA, and MLC (leakage reductions of 88%, 51%, and 29% at ε=1). Table 5 verifies the method is effective with GTR-base, Sentence-T5, and SBERT.

## Weaknesses

### Fatal

None.

### Major

1. **Eq. 4 (the mask learning objective) is incorrectly specified as written.** The loss is given as:
   \[
   \mathcal{L}(\mathbf{m},\theta)=-\Sigma_{x^{+}\in D^{+}}\log P_{\theta}(\Phi(x^{+})\odot\mathbf{m})-\Sigma_{x^{-}\in D^{-}}(1-\log P_{\theta}(\Phi(x^{-})\odot\mathbf{m})).
   \]
   For negative examples, standard binary cross-entropy would use `-log(1 − P_θ(...))`, not `−(1 − log P_θ(...))`. As written, the negative-class term has problematic behavior: if P_θ → 0 (correct prediction for a negative), log P_θ → −∞, and the loss term → +∞ — the opposite of what is needed for minimization. While the differentiable masking framework (HardConcrete, Louizos et al. 2018) is well-established and the experimental validation suggests the method works in practice, the equation as presented is technically inconsistent. **The authors must provide the correct loss formulation and confirm that the reported experiments used it.** This is the most significant weakness in the paper.

### Minor

2. **The Leakage metric is not fully specified for sentence-level attack models.** The paper states Leakage measures "the attack model's accuracy in predicting sensitive tokens." For the token-level MLC classifier this is clear. But Vec2text and GEIA reconstruct entire sentences — the paper does not specify how token-level accuracy is computed from reconstructed text. Is it exact string match? Substring match? Entity extraction followed by matching? This ambiguity makes the reported numerical values (e.g., 60% Leakage for unprotected STS12) difficult to interpret or reproduce.

3. **The modest overlap between black-box and white-box neuron sets (32% for top 10%, 51% for top 20%) vs. near-Oracle performance is not discussed.** Figure 5 shows this discrepancy, and Figure 4 shows DPPN approaches DPPN-Oracle despite only ~50% agreement on the top 20% of neurons. The paper attributes this to implicit protection from semantic clustering (Section 5.3), but does not quantify whether this fully explains the gap. A discussion of whether many neuron subsets are equally effective, or whether the black-box and white-box methods simply rank the same neurons differently, would strengthen the analysis.

### Trivial

- The utility metric for STS12 (Spearman correlation?) and FIQA (what task?) is not stated explicitly — only "dataset-specific downstream performance." This should be specified in the evaluation section.
- The choice of k = 0.2d is presented without justification or sensitivity analysis. A brief note on how k was selected would help.

## Nice-to-Haves

- **Sensitivity analysis on k (number of privacy neurons).** The paper fixes k = 0.2d. Showing how Leakage and downstream performance vary with k (e.g., 5%, 10%, 30%) would strengthen the claim that only a small fraction of neurons need perturbation.
- **Discussion of scalability.** The current method trains a separate mask for each sensitive token. For applications with many tokens (e.g., all PII types in medical records), this is impractical. A brief discussion of how this could be extended (e.g., clustering tokens or training a single detector) would improve practical relevance.

## Removed Points

These points were raised by reviewers but are removed or downgraded per policy:

- **"Noise variance comparison is not controlled" — critic's point #3.** *Reason:* The paper actually does show the suppress method applied to r=100% (all dimensions) in Table 2 ("applying these functions across all dimensions r=100%"), which is precisely the ablation the critic asks for. The critic misread the paper on this point.
- **"The loss function issue invalidates all results" — critic's claim that detection results may be artifacts.** *Reason:* The critic overstates severity. The differentiable masking framework (HardConcrete, Louizos et al. 2018) is a standard technique. The white-box Oracle (FGSM-based, completely different method) independently validates the core claim that perturbing privacy-sensitive neurons works. Eq. 4 is likely a presentation error in the equation, not evidence of a failed implementation.
- **"Formatting nits and missing appendix" concerns.** *Reason:* Per policy, parser-stripped appendix content and formatting artifacts are not author errors.

## Novel Insights

The reviews surface a genuine tension in the paper: DPPN achieves near-Oracle performance while agreeing with the Oracle's neuron selections only ~50% of the time. This could mean either (a) the two detection methods find different but equally effective neuron subsets, or (b) the overlap metric itself is misleading because neuron rankings are noisy. Neither the authors nor the reviewers resolve this — it points to an interesting open question about whether "privacy neurons" are a uniquely identifiable set or whether many subspaces are equally effective for obfuscation. The qualitative finding that semantically similar words share neuron clusters (Figure 6) suggests the latter interpretation may be correct.

## Suggestions

1. **Correct Eq. 4.** Provide the actual training objective (presumably standard binary cross-entropy of the form −Σ log P(positive) − Σ log(1 − P(negative))). If the equation in the paper is a typo, state this explicitly.
2. **Specify the Leakage metric for sentence-level attacks.** For Vec2text and GEIA, describe exactly how token-level accuracy is computed from reconstructed sentences (e.g., "we check whether the target token appears as a substring of the reconstructed sentence").
3. **Add a brief discussion of the overlap vs. performance discrepancy** in Section 5.1, explaining why modest neuron-set overlap still yields near-Oracle defense.
4. **State the downstream task and metric** explicitly for STS12 and FIQA (e.g., "Spearman rank correlation for STS12 semantic textual similarity").

## Score and Decision

The paper addresses a meaningful problem with a well-motivated idea and provides extensive experimental validation across diverse settings. The main concern is the incorrectly specified loss function in Eq. 4, which needs correction. Given the overall experimental strength and the independent validation from the white-box Oracle, this is likely a presentation error rather than a fatal methodological flaw, but it must be fixed for the paper to be trustworthy.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>