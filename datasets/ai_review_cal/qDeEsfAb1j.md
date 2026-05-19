- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5
Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

The paper proposes **ALGN/ALGSN** (referred to as LASR by the reviewer) — a method for training neural networks on data from multiple sources with unknown, heterogeneous reliability. It maintains per-source counters reflecting cumulative deviation from other sources' loss distributions, then uses these counters to depress gradient contributions from sources that appear unreliable during training. The method is evaluated on nine datasets spanning vision, time-series, NLP, and tabular regression, comparing against ARFL, IDPA, Co-teaching, and RRL.

---

## Strengths

1. **Broad and consistent empirical gains across diverse noise types and vision datasets.** Table 1 shows LASR achieves the highest mean accuracy on 5–6 of 7 noise types for each of CIFAR-10, CIFAR-100, and F-MNIST (e.g., CIFAR-10 Random Label: 62.74% vs next-best 57.71%; CIFAR-100 Batch Label Flip: 59.98% vs next-best 56.34%). The advantage is clearest on high-noise settings.

2. **Compatibility with existing noisy-data methods.** Table 2 shows adding LASR to RRL improves accuracy on CIFAR-10 for 5 of 7 noise types (e.g., Random Label: 80.31% vs 76.04%, Batch Label Flip: 82.02% vs 78.81%), demonstrating the method can augment rather than replace existing techniques.

3. **Robustness as the number of noisy sources increases.** Figure 2 (PTB-XL, CIFAR-10N) shows LASR maintains performance as the number of noisy sources grows, while standard training degrades sharply (e.g., PTB-XL AUC PR holds ~0.7–0.8 for LASR vs dropping to ~0.2 for standard training at high noise levels).

4. **Negligible performance loss on clean data.** "Original Data" rows in Table 1 show LASR matches standard training within standard deviation on all datasets (e.g., CIFAR-10: 67.76% vs 67.89%; CIFAR-100: 64.46% vs 64.46%), supporting the claim that the method does not harm performance when all sources are reliable.

5. **Cross-domain applicability.** Results span computer vision (CIFAR-10/100, F-MNIST, Tiny-ImageNet, ImageNet, CIFAR-10N), healthcare time-series (PTB-XL), NLP (IMDB), and tabular regression (California Housing), demonstrating versatility.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unresolved λ=0 inconsistency between method description and experiments.** The paper specifies "λ > 0" in both the method description (line 95: "setting λ > 0") and Algorithm 1 ("REQUIRE λ > 0 : Leniency"). The toy example (Figure 2, caption) uses λ=1.0 and explicitly discusses how λ controls the probability of falsely incriminating a clean source. Yet the experimental setup (line 181) states: "In our experiments, ALGSN parameters were set at H=25, δ=1.0, λ=0." This reduces the threshold to a mean-only comparison (whether the source's loss exceeds the weighted mean of other sources, with no variance term), which contradicts the method's own motivating narrative about standard-deviation-based leniency. The reader cannot tell whether λ=0 was chosen because it worked best empirically, or whether the method genuinely relies on the variance term. This gap substantially weakens confidence in the methodological story. The authors should provide a sensitivity analysis on λ for at least one dataset (e.g., CIFAR-10 with random label noise, λ ∈ {0, 0.5, 1.0, 2.0}) and clarify whether the variance-based threshold is essential or incidental.

### Minor

2. **IMDB results where Co-teaching outperforms LASR are acknowledged but not analyzed.** On IMDB "Original Data" and "Random Permute," Co-teaching (85.12%, 85.60%) outperforms LASR (83.20%, 83.26%). The paper offers a hypothesis (uniformly distributed human noise across sources) but provides no supporting analysis — e.g., reporting per-source losses or verifying that losses across sources were similar during training. On the other hand, these are the only two settings across all experiments where another method clearly beats LASR, and the gap is modest (~2pp). This is worth discussing but does not undermine the core claim; it points to a boundary condition the authors themselves identify (uniform noise across sources).

3. **No hyperparameter sensitivity analysis on real data.** The effect of H, δ, and λ is only demonstrated on a toy simulation (Figure 2). Given that λ=0 was used in experiments (contradicting the method's stated λ > 0 requirement), real-data sensitivity analysis is needed to understand how robust the method is to these choices.

4. **Wall-clock timing absent.** The paper claims LASR is "significantly faster than the baselines" based on asymptotic complexity (O(S×Sb+B) per step vs. training two models or k-NN per epoch), but provides no actual runtime measurements. The claim is plausible but unverified.

### Trivial
None.

---

## Nice-to-Haves

- Provide a sensitivity plot for λ on a real dataset (e.g., CIFAR-10 with random label noise) and clarify whether λ=0 was an empirical choice or a simplifying decision.
- Include a standard training baseline with early stopping on a held-out clean validation set — the most natural competitor for practitioners.
- Provide confidence intervals with statistical tests (e.g., paired tests) given the variance in some results.
- Report per-source loss trajectories during training on the IMDB dataset to verify the uniform-noise hypothesis.

---

## Removed Points

- **"The method's advantage is inconsistent, and some results weaken the core claim" (from Harsh Critic, point 2 regarding CIFAR-10/100 "Replace with Noise").** On CIFAR-10 "Replace with Noise," Standard (61.11) and LASR (61.52) are within each other's error bars; on CIFAR-100 "Replace with Noise," Standard (60.06) and LASR (59.99) are essentially identical. These are not cases where LASR is *outperformed* — the methods are statistically tied. The claim of "inconsistent advantage" is overstated. This is different from the IMDB case where Co-teaching does show a clear advantage.
- **Point about "the baselines are operating in a setting they were never designed for" (Harsh Critic, point 3).** The paper explicitly acknowledges this in Section 2 (lines 47–55: "our setting differs enough such that methods do not apply or under-perform"), and standard training is already included as a baseline. The implicit suggestion that baselines are inherently disadvantaged is true, but the paper transparently frames this as evaluating whether source-aware methods help in a setting where source information exists — which is precisely the paper's stated scope.
- **"The tanh² choice is not fully justified" (Harsh Critic, Section-by-Section notes).** The paper states (line 163): "the use of tanh² ensures that the scaling applied to g_s is in (0,1] and small perturbations of C_s around 0 do not have a significant effect on ĝ_s, making it more robust to randomness." This is a reasonable justification for the specific choice; no alternative is demanded.
- **Strength Finder claims regarding "highest mean accuracy on 6 of 7 noise types for CIFAR-10" and "6 of 7 for CIFAR-100."** These counts are slightly inflated: on CIFAR-10, LASR is highest on 5 of 7 (Standard beats LASR on Original Data and Co-teaching beats LASR on Replace With Noise); on CIFAR-100, LASR is highest on 5 of 7 (tied with Standard on Original Data, Standard beats LASR on Replace With Noise). The core conclusion (LASR is consistently among the best methods) is unaffected, but precision matters.
- **Generic strength about "addressing an important problem"** — removed as it lacks specific content tied to this paper.

---

## Novel Insights

The harsh critic identifies a genuine and non-trivial tension in the paper: the method is carefully motivated with a variance-based leniency parameter (λ) that controls false-incrimination probability, but the experiments use λ=0, collapsing it to a mean-only heuristic. This is not a fatal flaw — the per-source tempering still works — but it means the paper's theoretical framing is richer than its actual deployed mechanism. A single figure showing test accuracy vs. λ on CIFAR-10 would resolve whether this is a meaningful parameter or a vestige. The strength finder correctly identifies the paper's strongest empirical evidence: the PTB-XL and CIFAR-10N curves (Figure 2) show a clear and widening gap between LASR and standard training as noise increases, which is more compelling evidence than any single row in Table 1.

---

## Suggestions

- **Resolve the λ=0 inconsistency:** Add a sensitivity analysis on λ for at least one real dataset. If λ=0 yields the best results, state this clearly and explain why the variance term is not needed; if other λ values perform similarly, note robustness.
- **Verify the IMDB hypothesis:** Report per-source loss trajectories during training to confirm whether noise is indeed uniformly distributed across sources, as hypothesized.
- **Add wall-clock timing:** Provide training time measurements for LASR vs. each baseline on a common architecture to substantiate the complexity claim.

---
