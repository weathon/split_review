## Summary

This paper demonstrates that training loss curves (TLCs) collapse across model sizes (111M–3.9B parameters) under practical LLM pre-training when the AdamW timescale τ, tokens-per-parameter ratio (TPP), and LR schedule are held fixed. The authors identify τ (governing bias–variance trade-off via the optimizer's EMA timescale) and TPP (governing the pace of power-law improvement) as the key scale-invariant controls, grounding their analysis in a noisy-quadratic model (Appendix B.3). The paper introduces the **Celerity** model family—trained at fixed TPP bands with optimal τ per band—which achieves competitive accuracy on the compute-efficiency frontier. Two practical applications are demonstrated: (1) collapse residuals as an earlier diagnostic for training anomalies (e.g., a kernel bug detected at 60% vs. 90% of training via raw loss), and (2) a parametric surrogate fit at 111M scale that predicts normalized TLCs at 3.3B scale, enabling early stopping in λ-sweep tuning after only 10–30% of training.

## Strengths

- **Demonstrates TLC collapse at LLM scale under a practical scaling recipe, directly addressing the gap left by Qiu et al. (2025).** Section 3 and Figure 4 (right) show normalized loss curves collapsing across a ~30× scale range (111M to 3.3B) when both TPP and τ are fixed. This is the first such demonstration with weight decay, varying depth, and practical LLM architectures, confirming that the phenomenon observed in small autoregressive tasks persists at scale.

- **Identifies τ and TPP as the two scale-invariant controls governing TLC shape, with systematic empirical support and a theoretical grounding.** Figure 3 shows that matching τ (via independent sweeps over η, λ, or B) yields identical normalized TLCs. The noisy-quadratic derivation (Eq. 3, Appendix B.3) explains how τ controls the bias–variance trade-off and why the curvature factor cancels after normalization. This provides a clear framework for practitioners to reason about TLC shape.

- **Introduces Celerity as the first LLM family trained with demonstrable collapse that reaches the compute-efficiency frontier.** Figure 2 places Celerity models on the upper-left Pareto frontier versus open models (Gemma2, OLMo, SmolLM2). The paper reports a concrete trade-off: 62% parameter reduction with 67% extra FLOPs at 234 TPP relative to compute-optimal (20 TPP) training (Section 4, Appendix C.1).

- **The training anomaly detection via collapse residuals (Figure 1 right) is a clean and practical demonstration.** The 1.8B run's divergence from the collapse reference was detectable near 60% of training, while the raw loss only showed a visible blip after 90%. This provided actionable signals for diagnosis (kernel bug at specific microbatch size) and safe restart. The idea of using a universal reference curve as a quantitative diagnostic tool is practically valuable and well-illustrated.

- **The early stopping method is principled and shows clear gains on the tested settings.** Figure 9 demonstrates that aligning partial TLCs with the predicted surrogate at 111M scale selects the optimal λ setting within 10–30% of training, achieving negligible loss gap while the "current best" baseline can fail (e.g., 1.7B case). The connection between collapse and the ability to predict final loss from partial data is conceptually clean.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Overclaimed framing of "signature of compute-efficient training."** The abstract and Key Takeaway 2 state that collapse "emerges as a signature of compute-efficient training" (lines 14, 43). The paper demonstrates that under *their specific recipe* (fixed TPP, optimal τ, μP/CompleteP), both collapse and compute-efficiency occur. This establishes one direction (efficiency → collapse). However, the word "signature" could be read as implying a bidirectional diagnostic property (collapse → efficiency), which is neither shown nor argued. On careful reading, the paper's actual claim is the more modest one stated in line 36: that collapse occurs *when* τ is optimal and TPP is fixed. The framing in the abstract and key takeaways should be tightened to avoid overreach.

2. **The early stopping method is validated only on λ sweeps, and the baseline is weak.** Figure 9 tests λ sweeps at two model sizes (1.7B/20TPP and 3.3B/30TPP). The paper does not test other sweep types (e.g., learning rate η, batch size B) where the method's applicability would be less straightforward (varying η changes τ; varying B while fixing τ requires adjusting λ). Moreover, the "current best" baseline—picking the setting with lowest loss at the stop point—is simple. A stronger baseline like power-law extrapolation of each partial curve (a standard early-stopping heuristic) would better isolate the value added by collapse-based alignment. The method clearly works for the tested λ sweeps, but the generality of Key Takeaway 3 ("collapse enables reliable early stopping") is not fully established.

3. **Early-align normalization for online diagnostics has limited robustness characterization.** The paper uses early-align (choosing L(T) that best aligns the partial curve with a small-scale reference over 25–50% of training) for the diagnostic application. The paper does not evaluate: (a) sensitivity to the alignment window choice (e.g., 10–30% vs. 25–50%), (b) what happens if the reference curve is itself noisy or anomalous, or (c) performance on a broader set of synthetic training issues (gradient spikes, corrupted batches, LR spikes) at varying severities. The single case study is compelling but does not establish the method's reliability as a general diagnostic tool.

4. **Theoretical derivation assumes constant LR while experiments use linear decay.** The noisy-quadratic model (Eq. 3, Appendix B.3) is derived under constant LR. The paper acknowledges this gap qualitatively (lines 134–136: "With LR decay, ηₜλ decreases and the instantaneous timescale τₜ increases, enhancing late-stage variance suppression") and argues that normalizing by final loss preserves scale-invariance. However, the effect of schedule shape on the collapsed curves is not rigorously characterized. This does not undermine the empirical findings but limits the theory's predictive scope.

### Trivial
None.

## Nice-to-Haves
- Compare the early stopping method against a power-law extrapolation baseline (fit to each partial curve individually).
- Test early stopping on η and B sweeps, where the τ-adjustment mechanism is exercised.
- Run systematic diagnostic experiments: inject synthetic anomalies (corrupted batches, gradient spikes) at controlled severities and measure detection time vs. raw-loss monitoring.
- Provide empirical validation of the 234-TPP vs. 20-TPP trade-off (Figure 5) by directly training both at a fixed compute budget (though this is expensive).
- Release the fitted surrogate parameters (b_const, b_exp, q_const, q_exp) alongside code for reproducibility.

## Removed Points

**Critic Weakness: "The conclusion's claim about '$1B runs' extrapolates beyond the evidence."** The critic states that the largest models are 3.9B, making a claim about "for $1B runs" an unsupported extrapolation. This is factually incorrect: 3.9B > 1B, so the tested range (300M–3.9B) covers and exceeds the 1B scale. Removed.

**Critic Weakness: "The paper does not discuss related work in sufficient detail" (Tissue et al., Luo et al.).** The paper does cite these works (line 297) and positions its timescale-centric view as complementary. The criticism is a scope creak — the paper's contribution is about collapse, not loss-curve prediction broadly. Removed.

**Critic Weakness: "The TPP=234 trade-off analysis lacks empirical validation."** The paper transparently presents this as a theoretical estimate derived from power-law fits from prior work (Appendix C.1: "This expression leverages power law fits from prior work"). No empirical claim is made. Removed.

**Strength Finder: Generic strengths about "addressing an important problem" and "targeting an interesting question."** These are superficial and not specific to the paper's content. Removed.

**Critic Weakness: "Missing justification for optimal τ depending only on TPP."** This is cited as prior work (Bergsma et al., 2025a). Papers are not required to re-derive all cited results. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an observation about the work that the authors themselves had not already made.

## Suggestions

1. **Tighten the "signature" framing.** Replace "signature of compute-efficient training" with "consequence of compute-efficient training under μP" or "characteristic of optimal τ scaling" to avoid bidirectional overreading.

2. **Add one stronger baseline to the early stopping evaluation.** A per-curve power-law extrapolation (fit L(t) = A·t^(-α) + L∞ on the partial range and predict L∞) would directly show whether collapse-based alignment adds value over standard extrapolation heuristics.

3. **Include a robustness analysis of the early-align window.** A simple sensitivity sweep (e.g., alignment over 10–40%, 20–50%, 25–50%) with the 1.8B/234TPP diagnostic case would strengthen confidence in the method.

4. **Consider testing early stopping on at least one other hyperparameter type** (e.g., η or B sweep) to broaden the support for Key Takeaway 3. Even a single additional experiment would substantially improve generality.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>