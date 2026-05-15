Now I have a thorough understanding of the paper and can verify the reviewers' claims against the actual text. Let me synthesize the final review.

---

## Summary

This paper presents a normative reinforcement learning model in which place field parameters (amplitude, center, width) and actor-critic weights are jointly optimized via TD error to maximize cumulative reward. The model reproduces three experimentally-observed phenomena — high place field density at reward locations, backward field elongation against the trajectory, and representational drift with stable behavior — under a single reward-maximization framework. The paper further shows that field width and amplitude optimization accelerates policy convergence, and that noisy field updates facilitate learning of new targets, suggesting a functional role for drift.

## Strengths

- **Theoretical perturbative analysis linking field dynamics to value** — Equation 7 (Section 4.1) analytically shows that field center shifts are proportional to the squared critic weight \(w_{v,i}^2\), explaining why fields at high-value locations shift first. A similar analysis shows amplitude growth is likewise proportional to \(w_{v,i}^2\). This provides genuine theoretical insight beyond what is typical in this area and is a highlight of the paper.

- **First model to jointly reproduce three phenomena under a single TD-error-driven framework in a navigation task** — While drift requires exogenous noise (see Weaknesses), the model nonetheless offers a unified account of density at reward (Section 4.1) and field elongation (Section 4.2) via the same learning objective, and provides a tractable framework for studying drift within a policy-learning context. Prior work modeled each phenomenon in isolation.

- **Demonstration of differential contribution of field parameters to policy convergence** — The ablation in Fig. 4A–B cleanly separates the roles of width, amplitude, and center optimization, showing that width matters most and that center optimization does not help (and can hurt). The result that representation flexibility allows few-field agents to match many-field agents is insightful.

- **Noise-dependent drift regimes replicate a specific experimental finding (Qin et al., 2023)** — Under small Gaussian noise, high-amplitude fields become more stable while low-amplitude fields drift more (Fig. 3F). This emerges naturally from the model rather than being explicitly imposed, providing a mechanistic explanation with empirical support.

- **Distinct dynamics from the successor representation yield testable predictions** — The RM and SR agents exhibit qualitatively different field dynamics (anti-correlation vs. tracking occupancy early in learning, Fig. 2C–E), which could be distinguished in experiments that track fields throughout learning.

## Weaknesses

### Fatal
None.

### Major

1. **Representational drift is not produced endogenously by the reward-maximization objective; it requires explicit noise injection, which weakens the "unification" claim.** The paper states (Section 4.3) that without noise, the population vector correlation remains "extremely stable" (Fig. 3B, blue). Drift only emerges after adding Gaussian noise to field parameter updates. The abstract and introduction frame the model as "unifying" all three phenomena, but drift is not a natural consequence of the core TD-error-driven learning rule — it is imposed via a separate mechanism. While the paper is transparent about this, and while noise may have biological plausibility (discussed in Section 5), the framing overstates the degree of unification. The core learning objective produces density and elongation directly, but drift requires an auxiliary noise source. This should be clearly caveated in the abstract and introduction.

2. **The center optimization that drives the density phenomenon provides no computational benefit for the task, creating an unresolved tension.** The ablation in Fig. 4B shows that optimizing field centers \((\lambda)\) does not improve policy convergence and can even degrade performance when combined with amplitude optimization. Yet the density-at-reward phenomenon (Section 4.1, Fig. 1B) relies critically on center shifts — the paper states that Fig. 1B shows results "when only optimizing place field centers \((\Delta\lambda)\)." This means the most prominent experimental match (density clustering at reward) is driven by a parameter whose optimization is functionally irrelevant or harmful for the task that supposedly drives it. The paper does not acknowledge or discuss this paradox. The density phenomenon may be an epiphenomenon rather than an adaptive reorganization, or it may confer benefits in settings beyond the single-target task tested — but either possibility should be explicitly addressed.

### Minor

1. **The SR comparison conflates architectural differences with differences in learning objective.** The SR agent uses fixed place fields for policy learning and learns successor features separately (Section 4.2, App. C), while the RM agent learns adaptive fields jointly with policy. The paper presents this as a comparison of two normative accounts, which is valid in principle — the architectural asymmetry is inherent to how each theory works. However, the paper states that "both algorithms eventually learn similar spatial representations" (Section 4.2) based on a similarity matrix correlation that appears moderate (~0.4 from Fig. 2E). This claim is somewhat overstated, and the absence of any control isolating the effect of the learning objective from the effect of adaptive vs. fixed policy features means the comparison should be interpreted more cautiously.

2. **RM's stronger 2D field elongation is noted but not explained.** The paper observes that RM agents produce "significantly larger elongation" than SR agents in 2D (Fig. 2F, Section 4.2), but offers no analysis of why this occurs or what drives the difference. Since this could be a key experimental prediction distinguishing the two accounts, the absence of discussion is a missed opportunity.

3. **Simulation-theory fit for center shifts is not quantitatively validated.** The perturbative approximation (Eq. 6–7) provides a good fit for amplitudes (Fig. 1F) but the paper acknowledges that "additional approximations are needed" for centers (App. B). No quantitative comparison between predicted and simulated center dynamics is shown. While the theory is clearly presented, its coverage is incomplete.

4. **The new-target learning experiments (Fig. 4C) conflate two roles of noise.** Noise serves two distinct functions in the paper: (a) producing representational drift that mimics experimental observations (Section 4.3), and (b) enabling relearning of new targets (Section 4.4). The paper presents these together but does not clarify whether the same noise regime and mechanism underlies both phenomena, or whether they reflect different computational roles. The discussion in Section 5 partially addresses this but the distinction could be drawn more sharply.

### Trivial
- The gradient update equations for field parameters are relegated to Appendix A. Including a sketch in the main text would improve readability, though this is not essential.

## Nice-to-Haves
- Testing whether the learning rule itself (without injected noise) produces slow drift over very long timescales (e.g., 500k+ trials) due to finite-sample effects or stochasticity in the policy. If such drift exists, it would strengthen the unification claim.
- Varying noise magnitude in the single-target ablation (Fig. 4A–B) to clarify whether noise helps only for new targets or for learning in general.
- Testing in larger or more complex environments (multiple reward locations, continuous-action variants) to probe the generality of the results.

## Removed Points
These points were flagged by reviewers but are removed or weakened after cross-checking against the paper:

1. **"SR comparison is not a fair test" (original Critical Issue 3)** — This criticism demands that the SR agent be given adaptive place fields for policy learning. However, the architectural asymmetry is by design: the SR framework inherently separates representation learning (successor features) from policy learning (fixed features). Giving SR adaptive policy features would transform it into a fundamentally different algorithm and defeat the purpose of comparing two distinct normative theories. The comparison fairly contrasts RM (representation and policy jointly optimized for reward) with SR (representation optimized for transition prediction, policy learned separately). **Removed.** The remaining concern about the strength of the "similarity" claim is kept as a minor weakness.

2. **"Missing related works"** — Not verifiable without external sources. **Removed per instructions.**

3. **"Missing appendix / proofs in appendix"** — The parser strips appendix content; these exist in the original submission. **Removed per instructions.**

4. **Various formatting and grammar nitpicks** — These are parser artifacts or fall below relevance threshold. **Removed per instructions.**

5. **"Paper does not test in larger arenas"** — This is acknowledged as a limitation in Section 5 ("further work should test... in larger, more complex environments"). The paper explicitly scopes its contribution. **Weakened to nice-to-have.**

6. **"SR correlation never exceeds ~0.4"** — The paper describes the representations as "positively correlated" and "similar," not "highly similar." While the claim could be more precise, it is not misleading. Incorporated into Minor Weakness #1 with appropriate framing.

## Novel Insights
Beyond the paper's own contributions, the most interesting insight emerging from the reviews is the tension between the density phenomenon (driven by center shifts) and the ablation showing center optimization is functionally irrelevant. This paradox suggests a provocative hypothesis: the most visually striking experimental phenomenon (density clustering at reward) may be an epiphenomenon of value-gradient dynamics rather than an adaptive specialization. If this holds, it would challenge a common implicit assumption in the hippocampal literature that reward-associated place field reorganization is necessarily computational beneficial. The paper does not draw this conclusion, but the evidence it presents points in that direction, and doing so would sharpen its contribution.

## Suggestions
1. **Tone down the "unification" claim** regarding drift in the abstract and introduction. Explicitly state that drift requires an auxiliary noise mechanism, while density and elongation emerge directly from the TD-error objective. The paper already describes this honestly in Section 4.3 — the framing should match.

2. **Directly address the center-optimization paradox.** Discuss whether the density phenomenon (center shifts) might be an epiphenomenon, or whether it would provide benefits in more complex environments (e.g., multiple goals, changing reward locations). This would significantly strengthen the paper's theoretical contribution.

3. **Quantitatively compare predicted and simulated center dynamics** from the perturbative approximation, even if only in a simplified setting. This would fill the gap noted in the current analysis.

4. **Sharply distinguish the two roles of noise** (drift as a phenomenon to be explained vs. drift as a mechanism for new-target learning) in Section 4.3–4.4.

5. **Provide a clearer characterization of what "similar" means for the RM–SR representation comparison** (Fig. 2E), including the actual correlation values, to avoid overstatement.

## Score and Decision

The paper makes a genuine contribution to computational neuroscience by providing a tractable normative model that jointly addresses three experimentally-observed phenomena, with a clean theoretical analysis and informative ablations. The weaknesses are real but addressable: the drift-unification claim needs tempering, the center-optimization paradox needs direct discussion, and a few claims need precision. These issues do not invalidate the core contribution but require revision. I recommend acceptance with a request for major revision on the framing issues.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>