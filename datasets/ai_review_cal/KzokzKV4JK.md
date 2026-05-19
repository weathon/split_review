- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6
Now I have a thorough understanding of the paper. Let me compose the final consolidated review after verifying each claim against the paper text.

---

## Summary

This paper proposes SSNI (Sample-specific Score-aware Noise Injection), a lightweight add-on for diffusion-based purification (DBP) that replaces the globally fixed noise-injection timestep \(t^*\) with a per-sample value derived from the score norm of the input. The core intuition — that cleaner samples need less noise and adversarial samples need more — is well-motivated. SSNI uses a pre-trained score network to estimate score norms, then applies a linear or sigmoid reweighting function to adapt \(t^*\) per sample. Experiments on CIFAR-10 and ImageNet-1K with three DBP methods (DiffPure, GDMP, GNS) show consistent improvements in the accuracy-robustness trade-off with modest computational overhead (~0.5s per image on CIFAR-10).

## Strengths

1. **Clear empirical motivation for the problem.** Figure 1 concretely demonstrates that a fixed \(t^*=100\) produces both under-purified and over-purified samples, establishing that per-sample noise levels are needed. This observation is visually compelling and directly motivates the paper's central idea.

2. **Consistent improvements across multiple DBP methods and datasets.** Tables 1–3 show that SSNI-N improves clean accuracy (up to +3.58% on DiffPure, CIFAR-10, ℓ∞) while robust accuracy is maintained or improved (up to +4.23% on GDMP), across three different baseline methods and two datasets. This demonstrates generality rather than being a method-specific patch.

3. **Lightweight overhead.** Section 5.5 reports that SSNI adds only ~0.5 s per image on CIFAR-10 and ~5 s on ImageNet-1K over the baseline DBP methods, making it practical. The authors acknowledge this cost transparently in the Limitations section.

4. **Principled use of score norms as a proxy for denoising difficulty.** The paper builds on prior work (Yoon et al., 2021; Zhang et al., 2023) showing that score norms distinguish clean from adversarial examples, and extends this to differentiate perturbation strengths — a reasonable and well-supported extension.

5. **Ablation studies on design choices.** Table 4 (DDPM vs. DDIM sampling), Figure 3 (temperature τ), and the bias-term ablation (described below Figure 3) systematically probe the method's sensitivity to design choices, showing robustness across settings.

## Weaknesses

### Fatal
None.

### Major

1. **Unclear whether the adaptive attack differentiates through the score network.** The paper states that it uses "adaptive white-box attacks by considering the entire defense mechanism of SSNI" (Section 5.1) and that gradients are "computed from a surrogate process" following Lee & Kim (2023). However, it never explicitly states whether the PGD+EOT attack's gradients flow through the score network \(s_\theta\) and the reweighting function \(f\) to account for how an adversarial perturbation changes the chosen \(t(x)\). If the attack treats \(t(x)\) as constant, it cannot exploit the new vulnerability surface that SSNI introduces (e.g., crafting inputs whose score norm is artificially low, causing insufficient noise injection). The paper should clarify this and, if needed, confirm with an ablation comparing attacks that do vs. do not differentiate through the score network. This is a gap in the evaluation reporting rather than a fatal flaw, but it needs to be addressed for the robustness claims to be fully supported.

### Minor

1. **The link between score norm and oracle-optimal \(t^*\) is only indirectly validated.** The paper shows that (a) score norms correlate with perturbation budget ε, and (b) SSNI improves over fixed \(t^*\). These are consistent with the hypothesis, but the paper never directly validates that score norm predicts the oracle-optimal per-sample \(t^*\) (e.g., by finding the true optimal \(t^*\) for a subset of samples via grid search and plotting against EPS norm). A direct validation experiment would strengthen the theoretical framing and rule out the possibility that simpler heuristics (e.g., confidence-based adjustment) would perform equally well. As is, the evidence for the proposed method is empirical (it works), but the specific claim that score norms capture the *optimal* adjustment is circumstantial.

2. **Missing details on the score network.** The paper states that a "pre-trained score network" is used (following Song & Ermon, 2019), but does not specify its architecture, training data split, or whether it is the same network used in the diffusion model itself. Since the score network is a separate component whose differentiability matters for the adaptive attack, these details should be provided for reproducibility.

### Trivial

- The paper reports a 0.06% robust accuracy decrease for DiffPure+SSNI-N on ℓ₂ (CIFAR-10) and a 0.39% decrease for GDMP+SSNI-N, which is within the standard deviation of their own three runs. The paper's claim that this represents an improved "accuracy-robustness trade-off" is reasonable given the simultaneous clean-accuracy gains, but it would benefit from explicitly noting that these decreases are statistically negligible.

## Nice-to-Haves

- **Oracle-optimal \(t^*\) validation.** A small-scale experiment that performs a grid search over \(t^*\) per sample and plots the optimal value against the EPS norm would provide direct evidence for the claimed relationship and would nicely close the loop between theory and experiment.
- **Comparison to a simpler per-sample heuristic.** A natural baseline is setting \(t^*\) adaptively based on classifier prediction confidence (low confidence → more noise). This would isolate whether the benefit comes from per-sample adjustment *per se* or specifically from score-based adjustment.
- **Pareto frontier visualization.** Showing the accuracy-robustness Pareto frontier for SSNI vs. fixed \(t^*\) across multiple operating points would make the trade-off improvement claim more precise.

## Removed Points

- **Speculative concern about Lemma 1/Proposition 1 missing proofs.** The paper's Remark 1 explicitly frames these as "conceptual motivation" rather than rigorous theory, and the harsh critic admits they are "not a flaw." Removed.
- **Statistical significance tests.** Requesting p-values is not standard practice for DBP defense evaluations in this community, and the paper already reports means and standard deviations over three runs. Removed.
- **Hyperparameter sensitivity beyond τ and b.** The paper already provides ablation on τ (Figure 3), bias term, and sampling method (Table 4). The request for \(T'\) and reference-set-size sensitivity goes beyond what is standard for an empirical paper. Removed.
- **Criticism about small robust accuracy decreases being "glossed over."** The paper explicitly reports these decreases in Section 5.2 and contextualizes them within the overall trade-off improvement. Removed as factually inaccurate.
- **Generic formatting nitpicks and reproducibility concerns about undisclosed hyperparameters.** Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that the authors themselves do not already articulate.

## Suggestions

1. In the evaluation section, **explicitly state whether the adaptive PGD+EOT attack differentiates through the score network \(s_\theta\) and the reweighting function \(f\)**. If the current attack does not, acknowledge this limitation and either rerun the attacks or justify why the concern is negligible (e.g., the score network is a standard differentiable architecture, and the reweighting function is a simple smooth transformation, so gradients would naturally flow through both in a properly implemented adaptive attack).
2. Add a small-scale validation experiment directly showing that EPS norm correlates with oracle-optimal \(t^*\) (e.g., per-sample grid search on a 100-sample subset).
3. Provide basic details about the score network architecture and training setup to aid reproducibility.

The paper identifies a genuine and previously overlooked limitation of fixed-noise-level DBP, proposes a simple and principled fix, and supports it with solid experimental evidence across multiple methods and datasets. The main issue is a missing clarification in the attack evaluation protocol, not a fundamental flaw. I recommend acceptance.
