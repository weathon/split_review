Now I have enough data for calibration. Let me synthesize my analysis and write the final review.

**Round 1 Bracket:** After comparing with REPA (9.00), SANA (8.50), PaRa (7.50), and the 5.80–6.00 anchors, Neon falls in the **8.0–9.0** range. It has stronger theoretical grounding and broader architectural coverage than PaRa (7.50), and offers more conceptual novelty than SANA (8.50, which combines known techniques). It is comparable to REPA (9.00) in insight quality and simplicity, though REPA's 17.5× training speedup is arguably more impactful.

**Round 2 Narrowing:** Comparing more closely: Neon's theoretical analysis (Theorems 1–2) plus its coverage of 4 model families gives it an edge in breadth over REPA, but REPA addresses a more central problem (training efficiency for diffusion transformers). SANA (8.50) is a strong engineering contribution but reviewers noted limited technical novelty. I'd place Neon at **8.5** — slightly below REPA (whose speedup is more transformative) but clearly above PaRa and SANA in conceptual novelty and breadth of validation.

---

## Summary

Neon introduces a post-hoc parameter-merge technique that improves generative models by extrapolating away from the weight change induced by fine-tuning on the model's own synthetic outputs. The key insight — that common mode-seeking inference samplers create an anti-alignment between synthetic-data and real-data population gradients — is formalized through two theorems and validated across diffusion, flow matching, autoregressive, and few-step models on CIFAR-10, FFHQ, and ImageNet. The method requires no new real data, no auxiliary models, and uses <1% additional compute, yet delivers consistent FID improvements including a state-of-the-art 1.02 on ImageNet-256.

## Strengths

- **Novel and well-motivated insight:** The paper identifies that self-training degradation is not noise but a structured, reversible signal, formalized through Theorems 1 and 2. The theoretical analysis connecting mode-seeking samplers to anti-alignment is clean, non-trivial, and directly motivates the method. The toy Gaussian example (Figure 2) provides accessible intuition before the formal treatment.

- **Exceptional breadth of empirical validation:** Neon is demonstrated on four distinct model families — EDM-VP (diffusion), flow matching, xAR/VAR (autoregressive), and IMM (few-step) — across three datasets (CIFAR-10, FFHQ, ImageNet). This is substantially broader than typical generative modeling papers and strongly supports the claim of architectural universality.

- **State-of-the-art results with negligible overhead:** On ImageNet-256, Neon elevates xAR-L from FID 1.28 to 1.02 using only 0.36% additional training compute, surpassing prior SOTA (UCGM's 1.06). The IMM results are particularly striking: 4-step inference with Neon nearly matches 8-step base model quality, effectively halving inference cost.

- **Thorough and well-designed ablation studies:** Cross-architecture transfer (Figure 8), base-model quality sensitivity (Figure 9), synthetic-data quality robustness (Figure 10), and the CIFAR-10C null control are all thoughtfully executed and directly address natural questions about the method's scope and limitations.

- **Mechanistic understanding via precision-recall:** Figure 4's dissection of the precision-recall trade-off as a function of extrapolation weight provides concrete evidence for the claim that Neon redistributes probability mass from over-represented to under-represented modes, grounding the FID improvements in an interpretable mechanism.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Hyperparameter tuning on evaluation distribution:** The paper reports using 10k samples for hyperparameter search and 50k for final FID evaluation. If these are drawn from the same test set (as is common when using standard ImageNet/CIFAR-10 validation splits), this constitutes model selection on the evaluation distribution. The FID gains are large enough that this is unlikely to change the qualitative conclusion, but reporting results with a fixed default protocol (e.g., one fixed \(w\) and \(\gamma\)) or confirming that a fully disjoint validation split was used would strengthen the comparison's fairness.

- **Limited reporting of diversity metrics beyond precision/recall:** For a method that explicitly manipulates the precision-recall balance, reporting Inception Score (standard on ImageNet) or Density/Coverage metrics would give a more complete picture of how the trade-off affects generation quality. This does not undermine the core claims but would enrich the analysis.

### Trivial

- **Figure 4 caption error:** The caption states that \(w = -1\) corresponds to \(\theta_{\text{Neon}} = \theta_r\) and \(w = 0\) corresponds to \(\theta_{\text{Neon}} = \theta_r\). From Equation (2), \(w = -1\) yields \(\theta_{\text{Neon}} = \theta_s\), not \(\theta_r\). The text in Section 4.1 describes the behavior correctly; only the caption is wrong.

## Nice-to-Haves

- A head-to-head numerical comparison with a recent self-training improvement method (e.g., DDO or Discriminator Guidance) on a shared base model would make the practical advantage more tangible, though the paper already provides a clear qualitative contrast with these methods.
- A brief discussion of when the precision-for-recall trade-off might be undesirable (e.g., applications requiring high precision) would help practitioners understand Neon's practical scope.
- An explicit negative-control experiment with diversity-seeking samplers (showing that interpolation, not extrapolation, is optimal in that regime) would tighten the theory-practice connection.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Theoretical assurances in a non-convex landscape"** (from Harsh Critic): The paper is appropriately cautious, stating that local convexity is sufficient but not necessary, and the empirical results across architectures validate the approach. The harsh critic themselves acknowledge this is minor. This is demoted from the main weakness list because it is a generic concern about any theoretical analysis of deep learning, not a specific problem with this paper's theory. The paper does not overclaim.

- **"Include a failure analysis" / "Expand the discussion of the precision–recall trade-off"** (from Harsh Critic's Strengthening the Paper section): These are suggestions for improvement, not weaknesses. Moved to Nice-to-Haves.

- **"Missing related works"**: Removed per instructions — no external confirmation possible.

- **Formatting/style/typo nitpicks beyond the Figure 4 caption**: Removed per instructions. Only the Figure 4 caption error is retained as it affects mathematical correctness of the caption.

## Novel Insights

The paper's reframing of self-training degradation as a structured, harnessable signal — rather than noise to be avoided — is genuinely novel. The theoretical connection between mode-seeking inference samplers and gradient anti-alignment (Theorems 1–2) provides a principled explanation for both why naïve self-training fails and why reversing it succeeds, unifying observations that previously required separate explanations. The finding that the degradation direction transfers across architectures (Figure 8) further suggests this signal is a property of the data distribution's relationship to model biases rather than an artifact of any specific parameterization.

## Suggestions

- Fix the Figure 4 caption: \(w = -1\) should read \(\theta_{\text{Neon}} = \theta_s\), not \(\theta_r\).
- Clarify whether the 10k hyperparameter-search samples and 50k evaluation samples are fully disjoint, or report results with a fixed protocol (e.g., default \(w = 1\)) to eliminate any concern about test-set tuning.
- Consider adding Inception Score or Density/Coverage metrics to complement the precision-recall analysis.

## Score and Decision

**Originality:** High. The insight that self-training degradation is anti-aligned with the population gradient and can be reversed for improvement is fresh and counterintuitive.

**Importance:** High. The method addresses a fundamental bottleneck (data scarcity) without requiring new data, making it practically valuable as models continue to scale.

**Claims supported:** Well-supported. The theoretical claims are formalized and the empirical evidence spans four model families with consistent, substantial gains.

**Soundness:** Strong. The experiments are carefully designed with appropriate controls (CIFAR-10C null), ablations, and consistent evaluation protocols.

**Clarity:** Good. The paper is well-structured, the algorithm is precisely specified, and the theoretical section builds intuition through the toy example before formalization.

**Value to community:** High. The method is simple to implement (a parameter merge), requires no auxiliary models or new data, and works across architectures. It has immediate practical value.

**Anchor comparison summary:**
- `DJSZGGZYVi` (REPA, avg 9.00, Round 1): REPA has a similarly clean insight and strong results but is limited to one model family; Neon's broader coverage and theoretical depth make it comparable.
- `svIdLLZpsA` (Real-Fake, avg 6.00, Round 1): Weaker than Neon — narrower scope, less novelty, lower impact.
- `ZYd5wJSaMs` (Diff-2-in-1, avg 5.80, Round 1): Clearly weaker than Neon in both novelty and experimental validation.
- `KZgo2YQbhc` (PaRa, avg 7.50, Round 2): Good novel idea but narrower scope and weaker evaluation; Neon is stronger.
- `N8Oj1XhtYZ` (SANA, avg 8.50, Round 2): Strong system paper but reviewers noted limited technical novelty; Neon offers more conceptual depth and broader validation.
- `LyJi5ugyJx` (Consistency Models, avg 9.20, Round 2): Major contribution to a new model family at scale; Neon is simpler and less transformative — scoring below this anchor.

MY FINAL SCORE: <score>8.5</score>
MY FINAL DECISION: <decision>Accept</decision>