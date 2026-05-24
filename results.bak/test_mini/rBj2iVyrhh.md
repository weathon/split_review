Now I have enough calibration context. Let me write the consolidated review.

## Summary

This paper proposes CCAT (Classifier-Constrained Alternating Training), a two-stage framework for mitigating modality imbalance in multimodal learning. First, a shared classifier is pretrained using bidirectional cross-attention fusion with a regularization term that penalizes modality contribution disparity. This classifier is then frozen during alternating training, with each modality equipped with LoRA adapters. A sample-level secondary update targets severely imbalanced samples. Experiments on CREMA-D, Kinetic-Sound, and MVSA benchmarks show consistent improvements (+1.35%, +6.76%, +1.92%) over prior SOTA.

## Strengths

1. **Novel conceptual bridge between class and modality imbalance.** Section 3.1 provides a gradient-dynamics analysis showing that both class imbalance and modality imbalance share a recursive cycle of early dominance → gradient suppression → feature degradation → preference entrenchment. This framing gives clean theoretical motivation for applying classifier-constraining strategies (borrowed from class-imbalance literature) to the modality-imbalance setting.

2. **Well-motivated frozen-classifier design with clear empirical validation.** The paper identifies that prior alternating training methods (e.g., MLA) reduce encoder interference but leave classifier bias unaddressed. The two-stage solution — pretraining a contribution-regularized classifier, then freezing it as a stable decision anchor — is novel. The ablation in Table 2 confirms that classifier freezing alone adds +3.09% on CREMA-D (82.80→85.89), directly validating the central claim.

3. **Consistent and substantial SOTA improvements across three diverse benchmarks.** Table 1 shows gains on both multimodal accuracy (+1.35% CREMA-D, +6.76% KS, +1.92% MVSA) and weaker-modality unimodal accuracy (e.g., video on CREMA-D: 68.01%→73.79%). These gains are consistent across audio-visual and text-image tasks, suggesting general applicability.

4. **Thorough hyperparameter analysis.** Table 3 and Figure 4 systematically explore LoRA rank r and imbalance threshold β across all three datasets, providing practical guidance for deployment.

## Weaknesses

### Fatal

None. The core contribution — freezing a contribution-regularized classifier during alternating training — is well-supported by the ablation study and main results. No experimental or theoretical flaw invalidates the central claims.

### Major

1. **Underspecified contribution estimation during alternating training (Sections 3.2–3.3, Algorithm 1).** The paper states (line 237) that during alternating training, "the computation of c follows the same decision-level fusion used in the inference stage." However, Eq. (5)–(6) define contribution scores as softmax over MI(z_i^m, f_i), where f_i is a fused *feature vector*. Decision-level fusion combines *predictions* (logits/probabilities), not feature vectors, so it is unclear what f_i refers to in this stage. Algorithm 1 (Step 10) calls "Estimate contributions via Eq. (6)" but does not specify whether a fused feature vector is constructed (and how) or whether an alternative contribution metric is used. This is a significant clarity gap: the secondary update mechanism — a core component of the method — cannot be reliably reproduced without resolving this inconsistency. *This is not a fatal flaw (the mechanism is likely implementable with a simple feature-level aggregation before the classifier), but it must be resolved in revision.*

2. **Missing standard deviations on all main results (Tables 1–2).** The paper reports "average test accuracy (%) of three random seeds" without standard deviations or confidence intervals. While three seeds is standard, the absence of variance information makes it impossible to assess whether gains such as +1.35% on CREMA-D or +1.92% on MVSA are statistically reliable. Several baselines show large variance across unimodal scores (e.g., video-only LFM at 45.83 vs. MLA at 68.01 on CREMA-D), which further motivates reporting variance. This is an evidential gap that should be addressed.

### Minor

1. **Pretraining effect is not fully ablated.** The ablation removes classifier freezing (Fix ✗ in Table 2), but the classifier is still initialized from pretrained weights and then fine-tuned. A stronger ablation would compare against a randomly initialized classifier with the same alternating+LoRA+secondary-update pipeline. This would isolate whether pretraining (with cross-attention and contribution regularization) is essential, or whether a frozen random classifier with LoRA suffices. The existing ablation still supports the method's overall effectiveness; this comparison would strengthen the claims about pretraining's role.

2. **The "theoretical framework" in Section 3.1 is a motivating analogy, not a rigorous proof.** The derivation assumes a linear fusion model f = γ₁f₁ + γ₂f₂ with "implicitly learned modality utilization coefficients," whereas the actual architecture uses bidirectional cross-attention. The gradient analysis (Eq. 3) does not account for nonlinear interactions in cross-attention fusion. The paper does not over-claim this as a formal proof, but the framing as a "theoretical framework" (contribution i) overstates what is provided.

### Trivial

- Figure 1 caption describes the Ours lines as showing "a more pronounced imbalance" (0.65/0.35) compared to MLA (0.90/0.10), when the intended meaning is clearly "more balanced." This is a wording error.
- The paper would benefit from a brief discussion of the computational cost of the secondary update, which doubles per-batch forward/backward passes.

## Nice-to-Haves

- **Reproduce a key baseline under the same codebase.** The large spread in unimodal baseline scores (e.g., video-only LFM at 45.83 vs. MLA at 68.01 on CREMA-D) may reflect different implementation protocols. Re-implementing MLA or LFM within the same framework would strengthen the comparison.
- **Analyze inference-time distribution mismatch.** The paper notes (Section 3.3) that P(z^m|y) ≠ P(f|y) when switching from cross-attention to unimodal processing, but does not analyze how the frozen classifier handles this shift, beyond noting that LoRA helps.

## Removed Points

- **"Stronger multimodal accuracy on KS comes primarily from audio encoding, not video"** — The paper's task is multimodal, not individual modality optimization. Improving the weaker modality is the goal. (Removed: not a weakness.)
- **Criticism that Section 3.1 derivation is "overly simplistic"** — Retained this as Minor weakness #2 since it's valid but does not harm the core claim. The harsh critic's characterization is accurate; the paper presents a motivating analogy, not a rigorous proof.
- **Figure 1 caption garbled** — Retained as Trivial since it's a wording issue, not parser artifact (the numbers in the table are clear and correct).
- **Missing complexity analysis of secondary update** — Moved to Nice-to-Haves; useful but not a core flaw.
- **Scope limited to two modalities** — The paper explicitly scopes this in future work. Not a fair criticism.
- **Generic concerns about baseline comparisons** — The harsh critic's speculation about baseline implementations is removed as it's unsupported speculation. However, the large variance in unimodal scores is a genuine concern about comparability, so it's kept as a Nice-to-Have.

## Novel Insights

None beyond the paper's own contributions. The two reviewers raised standard concerns (clarity of implementation, missing std devs, ablation completeness) that are typical for a method paper at this stage.

## Suggestions

1. **Clarify contribution estimation during alternating training.** Specify what f_i refers to when decision-level fusion is used, or provide the alternative formula for computing c_i^m. If a fused feature vector is still constructed for contribution computation (e.g., by averaging unimodal features after LoRA correction), state this explicitly.
2. **Add standard deviations** (or confidence intervals) to Tables 1 and 2.
3. **Add a random-classifier ablation** to disentangle the effect of pretraining from the freezing mechanism.

## Score and Decision

**Round-1 Bracket:** Between 4.5 and 6.5. Below the 8.0 oral-level papers, clearly above the 2.5–3.0 rejected papers.

**Round-2 Anchors (used for narrowing):**
- GOAL (avg 4.50, Reject) — Related modality-imbalance paper; gradient modification method. CCAT has stronger novelty and better-motivated methodology.
- MoRA (avg 5.50, Accept Poster) — LoRA-based approach for missing modalities. Comparable methodological quality; CCAT has more specific theoretical motivation while MoRA has broader evaluation diversity. CCAT is slightly stronger on contribution novelty.
- MASAM (avg 5.50, Accept Poster) — SAM for multimodal imbalance. CCAT's evaluation is on 3 datasets vs. MASAM's 5, but CCAT's method is more distinct from prior work.
- Plug/Play/Fortify (avg 5.00, Accept Poster) — Frequency-domain imbalance solution. CCAT has stronger empirical gains and theoretical grounding.
- Closing Modality Gap (avg 5.00, Accept Poster) — Modality gap reduction. CCAT has more substantial methodological contribution.

**Final Score:** 5.5. The paper has a genuinely novel idea (frozen classifier as decision anchor for alternating training) with consistent SOTA results and a reasonable ablation study. The main weaknesses — an underspecified implementation detail for contribution estimation during alternating training and missing variance estimates — are resolvable in revision and do not threaten the core contribution. However, these gaps prevent the paper from reaching the 6+ tier, where methodological clarity and evidential completeness are expected.

THE PAPER IS ACCESSIBLE AND COMPLETE — no issues with broken content.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>