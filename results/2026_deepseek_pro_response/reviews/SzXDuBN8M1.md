Now I have a clear picture. Let me synthesize the final review.

**Comparative calibration analysis:**

| Anchor | Score | Comparison to TD-JEPA |
|--------|-------|----------------------|
| FB-CPR | 6.50 | TD-JEPA has more novelty (new TD-JEPA objective vs. adding regularizer to FB) and far broader evaluation (13 datasets vs. one environment). TD-JEPA is stronger. |
| Proto Successor Measure | 6.75 | PSM has elegant theory but experiments limited to grid world + FetchReach. TD-JEPA has comparably novel theory + comprehensive 65-task evaluation. TD-JEPA is stronger. |
| Bridging State & History Reps | 6.75 | Unification paper with strong theory, inconclusive experiments. TD-JEPA has sharper empirical contribution. TD-JEPA is stronger. |
| Video Representation Learning | 7.25 | Tighter theory (PAC bounds), but limited experiments (GridWorld, ViZDoom). TD-JEPA has broader empirics but less tight theory. Roughly comparable; TD-JEPA slightly below. |
| Predictive Auxiliary Objectives | 8.00 | Different type of contribution (neuroscience-inspired analysis). TD-JEPA doesn't reach this tier. |

**Bracket:** Round 1 placed TD-JEPA at 6.5–8.5. Round 2 narrows to **6.75–7.25**, with TD-JEPA clearly above the 6.75 anchors but slightly below the 7.25 Video RL paper on theoretical tightness. Final score: **7.0**.

---

## Summary

TD-JEPA introduces a temporal-difference latent-predictive objective for unsupervised RL that learns policy-conditioned, multi-step dynamics representations from offline, reward-free data. The key insight is that training a predictor via a TD loss to match future latent states implicitly recovers successor features of multiple policies, enabling zero-shot policy extraction for any reward in the span of a learned task encoder. The paper provides theoretical gradient-matching results (Theorems 1, 3) connecting the latent-predictive losses to successor measure approximation — generalizing prior analyses to multi-policy, multi-step settings — and demonstrates consistent empirical performance across 13 diverse datasets covering locomotion, navigation, and manipulation from both proprioceptive and pixel observations.

## Strengths

- **Novel TD-based latent-predictive objective unifying representation learning with successor-feature estimation**: Proposition 1 establishes the equivalence between the MC-JEPA loss and successor feature approximation, showing the predictor directly approximates successor features in latent space. This enables latent prediction to serve as the core training objective rather than an auxiliary loss, with the entire pipeline (encoders, predictors, policies) trained from offline, reward-free data (Algorithm 1). The extension from one-step/MC to TD (Eq. 7, 9) is natural and enables off-policy training.

- **Theoretical gradient-matching results with breadth**: Theorems 1 and 3 show that gradients of the latent-predictive losses match those of direct successor measure approximation and forward/backward TD losses, respectively. This generalizes prior analyses (Tang et al., 2023; Voelcker et al., 2024; Khetarpal et al., 2025) from single-policy/single-step to multi-policy/multi-step settings. Theorem 2 provides a non-collapse guarantee under idealized dynamics, and Theorem 4 bounds the policy evaluation error — together these form a coherent theoretical narrative justifying why the method should work.

- **Comprehensive and consistent empirical performance**: Table 1 shows TD-JEPA achieves top aggregate returns on DMC_RGB (628.8 vs. next-best 582.4 for BYOL-γ*) and competitive results on proprioception. The probability-of-improvement analysis (Figure 2) is particularly informative — it reveals TD-JEPA is consistently among top algorithms across all 13 datasets, while competitors like FB or HILP excel only on subsets. TD-JEPA significantly outperforms FB and HILP in visual domains (lines 271-272), which has been one of the most challenging settings for unsupervised RL.

- **Well-motivated asymmetric architecture**: The design training separate φ (state encoder) and ψ (task encoder) via symmetric latent-predictive losses (Eq. 9) is motivated by the intuition that state representations should capture low-level dynamics while task representations capture higher-level features. Figure 3 (right) demonstrates this separation is empirically beneficial more often than not.

- **Fast downstream adaptation from frozen representations**: Figure 4 shows that frozen TD-JEPA state representations enable rapid offline and online fine-tuning matching or exceeding training from scratch, providing evidence that the learned state encoder captures transferable structure beyond zero-shot evaluation alone.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Theory-practice gap in the theoretical analysis**: Theorems 1 and 3 are stated "for fixed φ, ψ" (lines 148, 173), meaning the gradient-matching equalities for the optimal predictors hold when predictors are at their optima for the current representations. Theorem 2 (line 161) assumes a continuous-time relaxation where optimal predictors are computed first, then a gradient step on representations follows. In practice, Algorithm 1 trains predictors and encoders jointly via SGD. While this mirrors the situation in Tang et al. (2023) and the broader self-supervised learning theory literature, and the paper is transparent about these assumptions, readers should understand that the theorems describe an idealized dynamics that may not fully govern the practical training trajectory.

- **Restrictive assumptions in the main-text theory**: Assumptions A2 (uniform state distribution) and A3 (symmetric transition matrices, lines 148-149) are not satisfied in the evaluated environments — which include locomotion with directed dynamics and navigation with irreversible transitions. The paper notes these can be relaxed (line 157, "as shown in App. C"), but the main text carries these limitations without visible mitigation. A brief discussion of which assumptions are essential vs. artifacts of the proof technique would help practitioners interpret the theory.

- **Ablation of prediction targets conflates multiple factors**: The comparison in Figure 3 (left) — BYOL* (one-step, behavior-policy, unconditional), BYOL-γ* (multi-step, behavior-policy, unconditional), and TD-JEPA (multi-step, learned-policy, policy-conditional, TD loss) — varies prediction horizon, conditioning policy, and loss type simultaneously. The paper's conclusion is appropriately measured ("suggesting that directly modeling policy-conditional successor measures is on average beneficial," line 273), but a controlled ablation isolating individual factors (e.g., TD-JEPA conditioned on behavior policy vs. learned policy, keeping the multi-step TD objective fixed) would sharpen the central claim.

### Trivial

- The orthonormality regularizer (Algorithm 1, lines 126-127) is important for stability and directly relates to the theoretical orthonormality assumption (A1), but receives limited discussion in the main text. Its sensitivity to λ and batch size is not analyzed.

## Nice-to-Haves

- Report compute requirements, training time, or wall-clock comparisons against baselines. Since TD-JEPA trains two predictor-encoder pairs symmetrically, it likely incurs more computation than single-encoder methods.
- Discuss sensitivity of test-time performance to the size of the inference dataset used for linear regression of z_r. This matters for practical zero-shot deployment.
- A controlled ablation varying only the conditioning policy (behavior vs. learned) while keeping multi-step TD fixed would isolate the benefit of policy-conditional prediction more cleanly than the current Figure 3 (left) comparison.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **HC: Novelty of baseline instantiations complicates the empirical story**: The paper is transparent about BYOL*, BYOL-γ*, and ICVF* being novel zero-shot instantiations (footnote 5). The authors tuned these over comparable hyperparameter grids and explicitly note the adaptation. Creating fair baseline adaptations to enable clean ablation of prediction targets is a methodological strength, not a weakness. REMOVED.

- **HC: The transition from Eq. 7 to Eq. 9 is "surprisingly abrupt"**: The paper provides a clear rationale in Section 3.2 (lines 96-104): "we follow existing literature – according to which joint representations should be predictive of each other (Guo et al., 2020; Tang et al., 2023)." The motivation is explicit and references established practice. This is a presentation nitpick at most. REMOVED.

- **SF: "Unified self-contained algorithm design" as a standalone strength**: This is generic — every method paper presents an algorithm. Not a substantive, evidence-backed strength. REMOVED.

- **HC: "Missing Parts — Appendix C unavailability"**: The parser strips appendices from all papers. The original submission includes Appendix C with relaxed assumptions and further derivations. REMOVED.

- **HC: "the paper does not analyze what happens under simultaneous gradient updates" as a structural/fatal concern**: The paper is explicit about the optimal-predictor and continuous-time assumptions (lines 148, 161), and this pattern is standard in the self-supervised learning theory literature (Tang et al., 2023; BYOL theory). The paper already acknowledges the gap implicitly. This is a limitation worth noting (included as Minor above), not a structural flaw. DEMOTED to Minor rather than treated as fatal.

## Novel Insights

The review process reveals that the paper's core strength — the gradient-matching connection between latent-predictive losses and successor measure approximation — is also its most theoretically fragile point under the joint-training regime actually used. This tension (optimal-predictor analysis capturing essential dynamics while the joint-training regime remains formally unanalyzed) recurs across self-supervised learning theory more broadly (BYOL, SimSiam). TD-JEPA's contribution of extending this style of analysis to the multi-policy, TD-learning setting is genuine and useful, but the community benefits from clarity about where this analytical approach does and does not provide formal guarantees.

## Suggestions

- Add a paragraph in Section 4 explicitly discussing which theoretical assumptions (A1-A3) are essential to the core mechanism and which are artifacts of the proof technique. This would significantly improve the theory's accessibility and honest appraisal.
- Consider a controlled ablation where only the conditioning policy differs (behavior vs. learned) while keeping the multi-step TD objective fixed, to isolate the benefit of policy-conditional prediction more cleanly than the current three-way comparison.
- Discuss the orthonormality regularizer's role, sensitivity to λ, and connection to Theorem 2 in the main text rather than only in the algorithm listing.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>