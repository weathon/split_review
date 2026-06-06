## Summary

SparseFW reformulates layerwise LLM pruning as a convex relaxation of the combinatorial mask-selection problem and solves it with the Frank-Wolfe (FW) algorithm, which is projection-free and naturally yields sparse updates via an efficient Linear Minimization Oracle. The method also provides a theoretical approximation guarantee bounding the gap between the rounded relaxed solution and the optimal binary mask. Empirically, SparseFW is compared against Wanda and RIA on five GPT architectures (LLaMA-3.1-8B, Gemma-2-9B, Yi-1.5-9B, DeepSeek-7B, Qwen2.5-7B/14B) across 50%, 60%, and 2:4 sparsity regimes.

---

## Strengths

- **Analytical unification of greedy methods:** Section 2.1 derives that Wanda and RIA are both greedy approximations to the one-shot single-weight version of MASK SELECTION (Equations 4–7). Recovering Wanda's saliency score `|w_q| ‖X_{q,:}‖₂` from the per-weight pruning objective is a clean, non-trivial insight that adds value regardless of SparseFW's practical performance.

- **Tractable convex relaxation with efficient LMO:** The key observation that the convex hull of binary k-sparse masks corresponds to the ℓ₁-ball constraint (Equation 10) enables a projection-free FW approach whose LMO reduces to a top-k selection (Equation 12). This is algorithmically clean and memory-efficient — the paper precomputes G = XXᵀ once, making each FW iteration independent of sequence length and sample count.

- **Consistent improvements at 60% and 2:4 sparsity:** Table 1 shows clear wins for SparseFW at higher sparsity. At 60% on LLaMA-3-8B: SparseFW(Wanda) achieves perplexity 17.97 vs. 21.53 for Wanda and 19.14 for RIA. At 2:4 on LLaMA-3-8B: 20.45 vs. 24.82/23.7. Zero-shot accuracy improvements are also consistent across models and regimes.

- **Substantial per-layer pruning error reduction:** Figure 2 shows reductions of up to 80% in per-layer reconstruction error relative to the Wanda warmstart, with the text noting average reductions of 20–40% across settings. This validates that the FW optimization is meaningfully solving its local objective.

- **Honest transparency about limitations:** Section 2.3 and the conclusion explicitly disclose that α=0.0 (vanilla SparseFW) is worse than baselines and that the local-global objective mismatch is unresolved. This intellectual honesty is commendable and allows the community to build on the work with clear knowledge of the boundary conditions.

- **Compute-accuracy trade-off analysis:** Figure 3 shows that SparseFW benefits more from additional calibration samples than Wanda (64→512 samples drops perplexity from ~22 to ~19.5, vs. 25.1→24.6 for Wanda). This is actionable insight for practitioners.

---

## Weaknesses

### Fatal
None.

### Major

- **Theory covers the undeployed variant; the deployed variant lacks theoretical coverage.** Lemma 1 provides an approximation bound for vanilla SparseFW (α=0.0) — the version that "consistently yields worse results than the baselines" (Section 2.3). The actually deployed method constrains the feasible set to the 10% of weights not frozen by Wanda (α=0.9), changing the problem in a way the bound does not address. The paper acknowledges this gap in limitations ("inductive biases still appear necessary") but does not confront what it means for the theoretical contribution. As stated, the theoretical section provides formal justification for a non-functional method. This needs either: (a) a bound tailored to the constrained variant, or (b) an explicit acknowledgment that the theory is aspirational/motivational rather than a guarantee for the evaluated system. 

- **The core claim that FW "accounts for weight interactions" is partially undermined by α=0.9.** With 90% of mask decisions pre-decided by Wanda's saliency heuristic, the interactions *between* the fixed 90% and the optimized 10% are still handled by Wanda's greedy criterion. The contribution that remains is more precisely: "FW-based local refinement over a Wanda-initialized 10% residual reduces per-layer error." That is a real and useful contribution, but weaker than the "full weight interaction" framing in the abstract and introduction. The paper should reframe accordingly, especially since the conclusion still states SparseFW "explicitly accounts for weight interactions" without qualification.

- **Standard deviations omitted at tight margins.** Table 1 omits standard deviations "for legibility." At 50% sparsity, where several SparseFW results are within 0.1 perplexity of baselines — or worse than them — this makes it impossible to determine which differences are meaningful. SparseFW(Wanda) is numerically worse than Wanda on DeepSeek-7B (7.89 vs. 7.79) and LLaMA-3-8B (10.21 vs. 10.09) at 50% sparsity. Without variance, it is unclear whether these are within noise or genuine regressions. Figure 3 uses min-max ranges rather than standard deviations, which is less informative.

### Minor

- **Inconsistent performance at 50% sparsity weakens the generality claim.** At 50% unstructured sparsity, SparseFW(Wanda) is strictly worse than the Wanda baseline on two of six models (DeepSeek-7B: 7.89 vs. 7.79; LLaMA-3-8B: 10.21 vs. 10.09). At 60% and 2:4 the gains are much cleaner. The text acknowledges "much more consistent and bigger improvements in the higher sparsity regimes," but the claim that SparseFW "outperforms strong baselines" in the abstract should be qualified by sparsity level.

- **Abstract perplexity-reduction claim is relative to initialization, not an absolute baseline.** The abstract says SparseFW "reduces the per-layer pruning error by up to 80%." As clarified in Section 3, this is relative to the Wanda warmstart — meaning relative to the mask SparseFW initializes from. Calling this "outperforming state-of-the-art" in the abstract is accurate for Wanda/RIA comparisons, but "80% reduction" carries more weight in context if it were against an independent baseline.

- **The local-global objective mismatch is described but not analyzed.** Section 2.3 states that vanilla FW "can still produce worse final perplexity, likely due to a mismatch between local and global objectives," and the conclusion repeats this. However, no analysis is offered: Is the calibration loss unrepresentative of downstream behavior? Is there overfitting to C4? Understanding *why* the mismatch occurs would make the α=0.9 finding scientifically coherent rather than a pragmatic workaround.

### Trivial

- Line 7 in Algorithm 1 is labeled as "Threshold" inside the loop body but belongs logically outside the loop (it returns the final binary mask). The algorithm structure could be clearer.

---

## Nice-to-Haves

- Even an informal comparison to SparseGPT (e.g., one table row at a single model/sparsity) would help readers calibrate the practical significance of SparseFW. The paper's stated reason for exclusion (different problem formulation — mask selection vs. weight reconstruction) is principled and should be kept, but a single data point would allow the community to understand where SparseFW stands in the broader landscape.

- Theory tailored to the α-constrained variant (α=0.9) would align the theoretical and empirical sections. Since the constraint reduces to FW over a smaller feasible set, the analysis should extend with limited additional effort and would make the paper internally coherent.

- Reporting variance (standard deviations, not just min-max) in Table 1 and Figure 3 would make the significance of gains at 50% sparsity assessable.

- An analysis of *why* the local-global mismatch occurs (e.g., calibration distribution mismatch, per-layer objective non-monotonicity) would substantially increase scientific value.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: SparseGPT exclusion as "tendentious" or misleading.** The paper explicitly states the exclusion rationale ("we hence do not compare directly to methods that involve a reconstruction step, such as SparseGPT") and this is a principled methodological distinction. SparseFW solves MASK SELECTION; SparseGPT solves a joint mask-and-reconstruction problem. Comparing them conflates different objectives. The exclusion is strategically convenient, but it is also methodologically defensible. This is at best a Minor concern about abstract framing, not a structural validity issue. Demoted to the "abstract framing" note under Minor.

- **Harsh Critic: "Fatal" framing of the α=0.9 structural incoherence.** The paper is fully transparent about this (two explicit disclosures in Sections 2.3 and 5). The deployed method does improve over Wanda and RIA in most settings, especially at higher sparsity. The theory-practice gap is Major, not Fatal.

- **Strength Finder: "Consistent empirical improvements across diverse GPT architectures."** This is partially valid but must be qualified: at 50% sparsity, SparseFW is worse than baselines on two models. The strength is real for 60% and 2:4 sparsity.

- **Strength Finder: "Theoretical approximation guarantees" as a core strength.** The guarantee (Lemma 1) applies to the undeployed vanilla SparseFW (α=0.0), not the actual deployed method. Keeping it as a supporting strength only, not a core claim.

- **Any criticism of missing appendix content** (proofs, extended ablations): per review policy, the parser strips appendix sections. Not a valid basis for criticism.

---

## Novel Insights

The most genuinely novel analytical observation in this paper is the unification of Wanda, RIA, and (implicitly) SparseGPT as greedy approximations to the same combinatorial MASK SELECTION problem, derived from first principles in Equations (4)–(7). This framing clarifies the landscape of LLM pruning methods and provides a principled basis for comparing them. The finding that vanilla FW over the full relaxation performs *worse* than the greedy baseline it is designed to surpass — while FW restricted to a Wanda-guided residual 10% consistently improves it — is itself a substantive empirical discovery about the relationship between local pruning objectives and global perplexity, even if it currently lacks a theoretical explanation.

---

## Suggestions

1. Reframe the abstract and introduction to be more precise about what SparseFW contributes: a Wanda-initialized hybrid where FW optimizes over the residual search space, not a full convex relaxation that replaces Wanda. This is a smaller claim but one that is fully supported by the evidence.

2. Provide a theoretical bound or at least an informal argument covering the α-constrained variant (FW over the unfixed 10% of weights). This is the method that is actually evaluated and would make the theoretical section coherent with the experimental section.

3. Report standard deviations in Table 1, at least for the 50% sparsity regime where differences are small or negative, or add a statement about statistical significance.

4. Include a brief investigation of the local-global mismatch: e.g., does using WikiText (the test set) as the calibration set instead of C4 eliminate or reduce the mismatch? Even a single ablation would clarify whether the issue is distributional or structural.

---

## Evaluation on Key Axes

- **Originality:** Moderate. Applying FW to LLM pruning and the analytical derivation of Wanda/RIA as greedy approximations are novel. The method is an incremental but principled extension of existing ideas.
- **Importance:** Moderate. LLM pruning is a high-impact area, and demonstrating a principled optimization approach is valuable, though the competitive landscape (SparseGPT, quantization) limits the practical deployment significance.
- **Claims supported:** Partial. The empirical claims hold clearly at 60% and 2:4 sparsity, weakly at 50%. The theoretical claims apply to a different variant than what is evaluated.
- **Soundness of experiments:** Moderate. Good breadth of models and sparsity levels; missing variance estimates and one-sided comparison scope limit confidence.
- **Clarity:** Good. The paper is well-structured and unusually transparent about its own limitations.
- **Value to research community:** Moderate-to-good. The FW framework and the analytical unification of greedy methods are reusable contributions even if the practical gains are bounded.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>