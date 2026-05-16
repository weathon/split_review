Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper empirically investigates whether knowledge distillation (KD) from grokked models can induce grokking (delayed generalization) below the critical data regime — where standard training fails completely. It studies three settings: (1) cross-distribution transfer via KD from a teacher grokked on distribution p₁ to a student on p₂, (2) KD-induced grokking at data fractions as low as 10–20% where standard cross-entropy training yields no generalization, and (3) continual pretraining where KD from a grokked model prevents catastrophic forgetting during distribution shift. The key empirical findings are that student models trained via KD can achieve perfect test accuracy at data sizes where standard training gives zero generalization, and that this occurs even with increasing weight norms and zero weight decay.

## Strengths

- **KD enables generalization below the critical data regime where standard training fails.** Figure 4 directly demonstrates that at 20% training data, no generalization occurs with standard cross-entropy (regardless of optimizer or weight decay), while KD from a grokked teacher induces the student to achieve perfect test accuracy. This is the paper's most striking result and establishes practical value for grokked models in data-scarce settings.

- **Empirical demonstration of grokking with increasing weight norms under KD.** Figure 3 tracks L2 weight norms for students trained with Adam (no weight decay) and shows continuously increasing norms while grokking occurs. This provides a counterexample to the claim (Liu et al. 2022b, Varma et al. 2023, Nanda et al. 2023) that generalizing solutions must lie on smaller norm spheres — at least under distillation-based training.

- **Cross-distribution transfer via KD succeeds irrespective of optimizer choice.** Figure 2b shows that a student on distribution p₂ groks using KD from a teacher grokked on p₁ (different prime modulus), achieving generalization with both Adam and AdamW. This demonstrates a practical pathway for reusing grokked models across distribution shifts.

- **KD mitigates catastrophic forgetting during continual pretraining.** Figure 7 shows that without KD, accuracy on p₁ drops to near zero within a few steps when transitioning to p₂; with KD, accuracy on both tasks remains high. This is a clean and practically relevant result.

- **Extension to multi-distillation for larger models.** Figures 5b and 6 show that a larger transformer, trained solely via KD from smaller grokked models on p₁ and p₂, can generalize on joint distributions even when data for one distribution is below the critical size — whereas joint training with cross-entropy fails.

## Weaknesses

### Fatal
None.

### Major

- **The paper overstates its refutation of prior weight-decay/weight-norm theories.** The paper claims to "refute" Nanda et al. (2023), Varma et al. (2023), and Liu et al. (2022b) by showing grokking without weight decay and with increasing weight norms (lines 47–49, 118). However, the prior theories were developed for and under **standard cross-entropy training** — not KD. Introducing KD fundamentally changes the training objective and gradient dynamics. Showing grokking under this modified protocol is an interesting finding (and should be celebrated as such), but it does *not* directly refute claims about mechanisms operating under standard training. In fact, the paper's own Figure 2a shows that without KD and without weight decay, grokking does **not** occur within 30K iterations — which *supports* the prior theories rather than contradicts them. The paper should frame this contribution as "demonstrating an alternative mechanism by which grokking can arise" rather than claiming a refutation. This is the most significant weakness because it mischaracterizes the contribution throughout the text.

- **Missing training loss curves make it harder to verify the central phenomenon.** The paper defines grokking as "generaliz[ing] long after overfitting the training data" (abstract) and as a transition after "pure memorization" (line 25). The defining signature is a temporal gap between near-zero training loss and rising test accuracy. While the test accuracy curves in Figures 2b, 4b, and 5b show the characteristic delayed phase transition, the absence of training loss curves means the reader cannot independently verify whether the student models (a) overfit first (near-zero training loss) and then generalize (true grokking), or (b) follow a different optimization trajectory where accuracy rises without a prior period of complete memorization. This is not fatal — the test accuracy curves alone are strong suggestive evidence — but for a paper whose title and central theme is "grokking," training loss curves are a standard and expected piece of evidence.

### Minor

- **Single-seed experiments without error bars.** Given the known stochasticity of grokking (timing and even occurrence can vary with seed), reporting results from a single run without confidence intervals or multiple seeds weakens confidence in the findings. At minimum, 3–5 seeds should be reported for the key results.

- **No comparison with non-grokked teachers.** The paper attributes the student's success to the teacher being "grokked," but never tests whether a teacher trained on p₁ with abundant data (above critical, never grokking) would also enable successful distillation. This makes it unclear whether "grokked" is the critical property or simply "a good teacher."

- **Terminology inconsistency: "epochs" vs. "iterations."** The experimental setup (line 102) states "30,000 epochs of training with a batch size of 2048," while every other reference uses "iterations" (Figure 2 caption, lines 100, 106, 127). This is confusing — "epoch" normally means one full pass over the dataset. For a small dataset (e.g., 30% of 97×97 ≈ 2,822 examples at batch size 2,048), one epoch is ~1–2 batches. Clarifying whether training lasts 30K gradient steps or 30K data passes would aid reproducibility.

- **Critical data regime not independently verified for the exact experimental setup.** The paper relies on Varma et al. (2023) for the claim that 20% and 10% are below critical for modular arithmetic (line 92), and provides Figure 4a as a baseline showing failure at 20%. However, the paper does not systematically search for the exact critical threshold in its own model/task configuration, nor does it report training loss curves for the failure case. The baseline evidence is present but thin.

### Trivial

- The paper uses both "iterations" and "epochs" without consistent definition. This should be harmonized.

## Nice-to-Haves

- **Training loss curves** for all experiments to fully establish the memorization-then-generalization pattern.
- **Multiple random seeds** (3–5) with error bands on all key figures.
- **Ablation: non-grokked teacher.** Train a teacher on p₁ with abundant data (above critical) where standard training converges immediately to a generalizing solution without grokking. Does KD from this teacher also enable the student to generalize below critical? This would isolate whether the "grokked" property of the teacher is essential or whether any accurate teacher suffices.
- **Explicit statement of the primes P₁ and P₂ used**, and the exact model architecture dimensions (embedding size, number of heads, etc.).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism that Figure 5 caption contradicts the paper's own framing.** The harsh critic wrote: "The caption of Figure 5 even says 'In a it looks like an immediate generalization for 0.2 and 0.3, with no grokking' — directly contradicting the paper's own framing that KD induces grokking." This is a misreading. The caption refers to **Figure 5a** (Joint Training *without* KD, which is the baseline), not to the KD results in Figure 5b. The paper is not contradicting itself.

2. **Criticism that the paper does not verify the critical data regime.** The harsh critic claimed the paper "never quantifies or even verifies the 'critical data regime' for its own tasks." The paper explicitly states that 20% and 10% are below critical per Varma et al. (2023) and shows in Figure 4a that standard training at 20% fails. The evidence is present, albeit less thorough than one might wish. Downgraded to Minor.

3. **Criticism that "without training loss, it is impossible to tell whether the student models overfit first and then generalize (true grokking) or generalize immediately."** As noted above, this is an overstatement. Test accuracy curves showing delayed phase transition from near-chance to perfect are strong evidence of grokking and are the primary visualization used in the grokking literature (e.g., Power et al. 2022, Nanda et al. 2023). The point is valid but the critic's framing as "impossible to tell" is too strong.

## Novel Insights

The reviews surface a tension that the paper itself does not fully address: the paper's most compelling finding — that KD enables generalization at data fractions where standard training yields zero generalization — may be at least partially orthogonal to the grokking phenomenon. The paper frames its results as being *about* grokking, but the evidence suggests a potentially deeper insight: that the soft-label structure provided by a generalizing teacher can bypass the normal data-requirement threshold for generalization entirely. This suggests that the "critical data regime" may not be a fundamental property of the task or model, but rather a property of the *training objective*. If KD can shift the critical threshold downward by providing richer supervisory signals, this has implications beyond grokking — for semi-supervised learning, domain adaptation, and learning with limited labels. The paper does not fully articulate this, and the insight emerges more from the gap between the paper's framing and its evidence than from explicit discussion.

## Suggestions

1. **Reframe the paper's contribution relative to prior work.** Replace claims of "refuting" prior theories with the more accurate and still-valuable claim: "We demonstrate that under the modified training protocol of knowledge distillation, grokking can occur without weight decay and with increasing weight norms, revealing that weight-decay-independent mechanisms can also drive grokking when the loss landscape is shaped by soft targets."

2. **Add training loss curves** for all key experiments (Figures 2, 4, 5, 6). This single addition would substantially strengthen the grokking characterization.

3. **Add multiple seeds (3–5)** with error bands for the main results. Report the range of grokking step timings across seeds.

4. **Add a non-grokked teacher baseline.** Train a teacher on p₁ with abundant data (above critical, where models generalize immediately without grokking). Compare whether KD from this teacher also enables low-data generalization. If it does, the contribution shifts from "grokked models are special" to "KD itself lowers the data requirement for generalization."

5. **Clarify the "epoch" vs. "iteration" terminology** and report total gradient steps explicitly.

## Score and Decision

This paper explores a genuinely interesting and under-explored direction — leveraging grokked models as teachers for low-data generalization — and presents several novel experimental findings. The evidence for KD-enabled generalization below the critical data regime, for cross-distribution transfer, and for catastrophic forgetting mitigation is solid and well-illustrated.

However, the paper's presentation overstates its refutation of prior theoretical work, and the absence of training loss curves and multi-seed runs weakens the characterization of the central phenomenon. The contribution is better described as "using knowledge distillation from grokked models to enable low-data generalization" rather than the more ambitious "refuting existing grokking theories" that the current text claims.

With major revisions — particularly reframing the claims, adding training loss curves, and adding multi-seed experiments — the paper could be a solid contribution. In its current form, the framing issues and missing evidence prevent full acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>