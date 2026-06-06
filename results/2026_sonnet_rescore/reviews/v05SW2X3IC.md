## Summary

The paper proposes a learnable three-channel codec grounded in Gray-Wyner Network (GWN) theory to separate common and task-specific information across multiple computer vision tasks. The central theoretical contributions are Theorem 1 (extending Wyner's lossless common-information bounds to the lossy regime via interaction information) and Theorem 2 (reformulating the GWN optimization as a Lagrangian over conditional entropies, yielding a single-hyperparameter β objective amenable to neural entropy models). Experimentally, the system demonstrates strong BD-rate reductions over independent single-task codecs across six vision benchmarks.

---

## Strengths

- **Theorem 1 (Section 3.1, Eqs. 6–7)**: The extension of Wyner's lossless bound to the lossy case via interaction information is non-trivial and provides a useful separability condition for equality between the two common-information measures. This directly motivates why complete disentanglement is often unattainable in practice.

- **Theorem 2 (Section 3.2, Eq. 10–12)**: The reformulation of the GWN objective for deterministic encoders replaces mutual-information terms with conditional entropies estimable by neural entropy models, enabling end-to-end training with a single Lagrangian hyperparameter β ∈ [1, 2]. The bridge between classical theory and modern learnable codecs is both principled and practically actionable.

- **Synthetic experiment with known information-theoretic quantities (Section 4.1, Figure 3)**: Training with β = 1, 3/2, and 2 predictably shifts the common-channel rate above, at, and below the empirical mutual information, validating the tradeoff mechanism. The Shared architecture Pareto-dominates the Separated and Combined alternatives, providing quantitative support for the architectural design choice.

- **MNIST edge-case study (Section 4.2, Figure 4)**: The Dependent, Independent, and Mixture PMFs span the full range of statistical overlap between tasks, and the method adapts its common-channel usage accordingly. This provides targeted evidence that the system does not require a fixed level of mutual information to function.

- **CV results against Independent coding (Figure 5)**: The proposed method achieves large BD-rate savings of +23.32% to +51.97% vs. Joint and dramatically better than Independent (+143.69% and +77.36% vs. Joint), confirming that separating common and private information substantially reduces redundancy in real multi-task settings.

- **Entropy model conditioning (Section 3.3)**: Conditioning private-channel entropy models on the common representation to handle residual redundancy (since I(Y₁, Y₂; Y₀) = 0 is hard to achieve) is a practically motivated and sound design choice.

---

## Weaknesses

### Fatal
None.

### Major

- **Single-source scope vs. distributed-coding motivation.** The paper explicitly acknowledges "our experiments, the proposed architecture specializes to a single source X, so that (X₁, X₂) = X" (Section 4). While the motivating scenario in the introduction (a single camera encoding for multiple downstream tasks) is indeed consistent with X₁ = X₂ = X, the GWN framework is classically meaningful only when sources differ (X₁ ≠ X₂), giving the transmit/receive tradeoff genuine operational weight (e.g., stereo pairs or temporally adjacent frames where different tasks are deployed on separate devices with distinct inputs). Every experiment in the paper uses the single-source specialization, so the regime where the GWN's original distributed architecture is most powerful remains undemonstrated. The paper acknowledges the simplification but does not discuss what is lost by it, and the conclusion's framing as a "distributed inference" system is not experimentally substantiated.

- **No direct comparison to existing multi-task codecs.** Chamain et al. (2021), Feng et al. (2022), and Guo et al. (2024) are cited as directly relevant prior art with common-channel-only architectures. The paper argues in Section 2 that "their rate is optimal only when all the tasks involved are performed jointly," equating them to the Joint baseline. This equivalence is logically argued but not demonstrated. Given that the proposed method is 23–52% worse than Joint in transmit rate (Figure 5), and given that the equivalence of Joint and prior multi-task codecs is asserted rather than empirically confirmed, the paper's standing relative to the field is unclear.

### Minor

- **Masking mechanism (Eq. 14) lacks empirical characterization.** The masking operation is the core architectural novelty: it zeros out positions where Y₀⁽¹⁾ and Y₀⁽²⁾ disagree after quantization. The paper fixes γ = 1 without analysis of how many Y₀ elements are non-zero at convergence across β values or tasks. This matters because gradient flow is blocked at disagreeing positions, and the auxiliary loss (Eq. 15) is the sole driver of the common channel at those sites. Without sparsity statistics or a sensitivity curve for γ, the masking mechanism remains an undercharacterized design choice rather than a validated contribution. The paper acknowledges the pitfalls of γ but defers entirely to tuning β instead.

- **Headline BD-rate figure in the conclusion is one-sided.** Section 5 reports "BD-rate advantage of −81.58% in transmit rate against single-task codecs," computed relative to the Independent baseline. The companion figure—that the proposed method is 23–52% worse than Joint in transmit rate—is visible in Figure 5 but absent from the conclusion. Both facts should appear prominently to give readers an honest assessment of the method's practical position.

- **"Order of magnitude" validation language (Section 4.2).** The claim "we operate within an order of magnitude of theoretical bounds" spans a factor-2 to factor-10 gap, and it is unclear which PMF or rate range drives the statement. Since the theoretical bounds are a core reference point, reporting the actual ratio or BD-rate distance would be more informative.

### Trivial

- **Low-compression dip for Cityscapes (Figure 5a)** is noted informally ("often attributed to lack of regularization") without any ablation. This does not affect the core claims but is left as an unexplained artifact.

---

## Nice-to-Haves

- A stereo-pair or adjacent-frame experiment (X₁ ≠ X₂) would demonstrate the GWN framework in a genuinely distributed-sensor setting, substantially strengthening the paper's stated motivation.
- Reporting the fraction of non-zero Y₀ elements at convergence across β values and task pairs (trivial to extract from a trained model) would convert the masking mechanism from an undercharacterized heuristic into a validated architectural contribution.
- Showing the architecture comparison (Shared vs. Separated vs. Combined) for all β values in the main text, rather than deferring β ≠ 1 cases to the appendix, would make the ablation more informative given that β is the paper's sole tunable hyperparameter.
- Normalizing MNIST BD-rates by the theoretically achievable minimum (rather than just using Dependent PMF as anchor) would make comparisons across PMFs with very different mutual information more interpretable.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Markov conditions inconsistency (Harsh Critic, Section 3.3):** The critic argues that feeding both X₁ and X₂ to each analysis branch is an "undiscussed departure" from the Markov conditions in Eq. 1. However, when X₁ = X₂ = X (the actual experimental setting), the Markov conditions Z₂ ↔ X ↔ X and Z₁ ↔ X ↔ X are trivially satisfied. The paper explicitly states that shared access to both sources "effectively removes the requirement for the conditions in 1," which is accurate in the single-source regime. In the general X₁ ≠ X₂ case this would be a real issue, but since no such experiment is run, the inconsistency is moot. Removed as a strawman given the experimental scope.

- **Missing variance/training stability (Harsh Critic):** Requesting variance across training runs for learned codecs is a reproducibility nitpick not standard in the compression community for main-paper results. Removed per soft rules.

- **Appendix C compatibility analysis (Harsh Critic):** The appendix is stripped by the parser; cannot assess. The paper cites it as theoretical justification (Section 3.3). Per hard rules, removed.

- **Quantifying the theoretical-vs-empirical gap in Figure 3 (Harsh Critic):** The paper cites Bajić (2025) as context that empirical rates exceed theoretical values, and the Harsh Critic asks for "a ratio or BD-rate difference." While quantifying this would be informative, it is a minor presentational request that does not affect the validity of the results. Demoted below Trivial.

- **Strength: Appendix C compatibility analysis (Strength Finder):** Appendix stripped; cannot verify. Removed from strengths.

---

## Novel Insights

The paper's most genuinely novel observation—implicit in Theorem 1's equality condition and the discussion around the GK block-diagonal structure (Eq. 8)—is that achieving perfect common-information separation in the lossy regime is *harder* than in the lossless case, not merely equivalent, because excess non-separable interaction information in the distorted representations cannot be discarded from the common channel. This insight, that the lossy tradeoff space has non-trivial interior even for sources where lossless GK common information is zero (e.g., Gaussian), provides principled motivation for exploring β ∈ (1, 2) rather than operating at the endpoints, which is a useful conceptual contribution beyond the experiments.

---

## Suggestions

1. Add at least one experiment where X₁ ≠ X₂ (e.g., temporally adjacent frames or stereo image pairs), or explicitly reframe the paper as addressing single-source multi-task compression and explain clearly what GWN features are and are not exercised by this setting.
2. Include a sparsity analysis of the Y₀ mask at convergence (percentage of non-zero elements as a function of β and task pair) to empirically characterize the masking mechanism.
3. Report BD-rate results for at least one of the cited prior multi-task codecs (Chamain et al., Feng et al., or Guo et al.) directly in Figure 5, or provide a rigorous argument for why the Joint baseline is a valid proxy.
4. In Section 5, report both the −81.58% improvement over Independent and the +23–52% gap to Joint in the same sentence to present a balanced summary.

---

## Score and Decision

**Originality**: The theoretical extension of GWN to the learnable lossy setting and the β-parameterized Lagrangian are novel and non-trivial. Architectural novelty is moderate. Score: 4/5.

**Importance**: Multi-task coding for machines is a timely and practically relevant research area; the GWN framing adds principled structure to what is otherwise a heuristic design space. Score: 4/5.

**Claims supported**: Core theoretical claims (Theorems 1, 2) are well-stated. Empirical claims are supported for the single-source case but the distributed-coding framing in the introduction is not fully demonstrated. Score: 3/5.

**Soundness**: Experimental design is reasonable; the synthetic experiment is well-designed for theory validation. The missing multi-task codec comparison and undercharacterized masking mechanism are notable gaps. Score: 3/5.

**Clarity**: Writing is generally clear and the theoretical presentation is well-organized. Some framing issues (headline BD-rate, "order of magnitude" language) reduce precision. Score: 4/5.

**Community value**: Useful to both the compression and information-theory communities; bridges classical theory with learned codecs. Limited by experimental scope. Score: 3/5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>