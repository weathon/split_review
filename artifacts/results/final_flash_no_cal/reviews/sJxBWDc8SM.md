Now I have a thorough understanding of the paper. Let me construct the consolidated review.

## Summary

This paper systematically compares Transformers and modern recurrent models (Mamba, Hyena, Mamba2, DeltaNet) on multi-query associative recall (MQAR) and copying tasks. The central finding is that SSMs exhibit a critical optimization instability — their success is confined to a narrow learning rate window, while Transformers are robust across orders of magnitude. This re-contextualizes prior expressivity comparisons that may have been confounded by suboptimal tuning. The paper also documents opposing scaling preferences (width for SSMs, depth for Transformers), shows through ablations that the 1D convolution is the key enabler of 1-layer Mamba expressivity, and identifies DeltaNet as an architecture that achieves Transformer-like LR robustness.

## Strengths

- **Empirical isolation of a critical optimization instability:** Figure 1 and Figure 5 definitively demonstrate that on both MQAR and copying tasks, Mamba and Hyena succeed only within an extremely narrow learning rate window, while Attention maintains high accuracy across orders of magnitude. This is the paper's most impactful finding, directly supporting its thesis that prior performance comparisons were confounded by optimization issues.

- **Systematic characterization of opposing scaling behaviors:** Figures 3–4 and Table 1 reveal that Transformers and SSMs benefit from diametrically opposed scaling strategies — width for SSMs, depth for Transformers. Table 1 is particularly striking: a deeper-but-narrower Mamba with 150M parameters achieves 0% on the copy task while a wider version with the same parameter count achieves 100%. This provides a clear explanation for why parameter-matched comparisons can be misleading.

- **Mechanistic ablation identifying the 1D convolution as the driver of 1-layer expressivity:** Table 2 shows that removing the convolution from a 1-layer Mamba collapses accuracy from 99% to 2%, and conversely, adding a convolution to a 1-layer Transformer raises accuracy from 2% to 99%. This provides direct causal evidence that the convolution — not the SSM recurrence per se — enables 1-layer MQAR performance, while the narrow LR window remains a persistent property of the SSM sequence mixer.

- **Scale and rigor of the empirical study:** The conclusions are supported by over 3,000 runs and approximately 20,000 GPU hours (Section 1), with results averaged across 5 seeds using relative max-min error metrics, lending statistical credibility to the observed brittleness and scaling patterns.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The central thesis statement in Section 1 overstates the findings.** The paper claims: "*Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics.*" However, the paper's own ablations (Table 2, Section 7) show that the 1D convolution creates a genuine expressivity difference in the 1-layer setting — a 1-layer Mamba without convolution fails at 2% accuracy, matching the 1-layer Transformer's 2%, while a 1-layer Mamba with convolution achieves 99%. This indicates that the convolution contributes expressivity, not just optimization dynamics. While the paper correctly shows this gap can be bridged (adding convolution to a Transformer also reaches 99%), the absolute phrasing "not in terms of expressive power" is too strong. The abstract and conclusion use more measured language ("not just in their expressivity but in their fundamental learnability properties"), which better reflects the evidence. This framing mismatch does not undermine the core contribution but should be corrected.

2. **The induction head interpretation in Section 6 is speculative.** The paper observes a loss bump in 1-layer Transformer training and suggests it "resembles the formation of an induction head circuit" (Figure 6). While the paper uses appropriately cautious language ("reminiscent," "attempts to form"), this interpretation is not supported by direct mechanistic evidence (e.g., attention pattern analysis, head-specific ablation). It remains a plausible hypothesis but should be clearly distinguished from the paper's better-supported empirical findings. The strength of the paper does not depend on this claim.

3. **The explanation for the optimization instability is hypothesized but not directly measured.** The paper attributes Mamba's LR sensitivity to vanishing gradients in the off-diagonal terms of the state-transition matrix (citing Trockman et al., 2024), supported by the observation that DeltaNet's Householder-based updates avoid this. However, no direct gradient measurements (e.g., gradient norms through the recurrence, spectral radius of the state transition matrix during training) are provided to confirm the mechanism. The authors acknowledge this as future work ("a formal theoretical explanation… remains an important open question"), but the paper would be strengthened by direct causal evidence for the hypothesized mechanism.

### Trivial

None.

## Nice-to-Haves

- **Direct gradient analysis during training** — tracking the norm of gradients with respect to recurrent parameters (A_i, B_i) across the learning rate sweep for Mamba vs. DeltaNet would move the instability explanation from circumstantial to direct causal evidence.
- **Validation on downstream language modeling tasks** — the paper acknowledges this limitation and rightly identifies it as critical next step.

## Removed Points

- **Harsh Critic's claim that Section 7 contradicts the paper's thesis** — This misreads the paper: Table 2 shows that convolution differences explain the 1-layer expressivity gap, and that this gap can be bridged (adding convolution to Transformer = 99%). This supports the paper's argument that once architectural differences are controlled, the persistent differentiator is optimization stability, not pure expressivity.
- **Harsh Critic's characterization of the causal mechanism gap as a "methodological gap"** — The paper explicitly scopes this out as future work. The observation is valid but is a scope limitation, not a methodological flaw.
- **Strength Finder's "induction head dynamics" as a supporting strength** — While interesting, this observation is speculative and the paper's cautious language limits its evidentiary weight. It is not a core strength but is included as context.

## Novel Insights

The paper's central insight — that the SSM vs. Transformer performance gap on recall tasks is substantially confounded by optimization instability, with SSMs succeeding only in a narrow learning rate window — is genuinely novel and timely. The discovery that this instability has concrete architectural determinants (the diagonal state matrix in Mamba, mitigated by DeltaNet's Householder updates) and that scaling strategies must be chosen to match the architecture's preferred axis (width vs. depth) provides actionable guidance for practitioners and reframes the debate around efficient sequence models.

## Suggestions

- Rephrase the central thesis in Section 1 to accurately reflect the evidence: e.g., "optimization dynamics are a crucial, underappreciated differentiator" rather than "not in terms of expressive power."
- Add a caveat to the induction head claim in Section 6 clarifying that this interpretation is a hypothesis requiring further verification.
- Consider adding gradient norm measurements in a camera-ready version to support the hypothesized instability mechanism.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>