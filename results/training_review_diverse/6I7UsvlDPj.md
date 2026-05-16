Now I have enough information to verify the reviewer claims against the actual paper. Let me compile my consolidated review.

## Summary

The paper introduces LaMPP (Language Models as Probabilistic Priors), a framework for using language model token probabilities as Bayesian priors in probabilistic graphical models for non-linguistic perception and control tasks. The method is demonstrated on three diverse tasks: semantic segmentation (using room-object co-occurrence priors), object navigation (using priors over where objects are found), and video action recognition (using priors over action transition parameters). The paper claims consistent improvements on rare, out-of-distribution, and structurally novel inputs across all three tasks.

## Strengths

1. **Principled integration of LM knowledge with structured probabilistic inference.** The paper formalizes two distinct ways to incorporate LM priors — at prediction time (via Bayes' rule combining LM priors with domain likelihoods) and at learning time (via MAP estimation with Dirichlet priors over parameters). This goes beyond ad-hoc model chaining and is supported by quantitative comparisons: in segmentation (Table 1), LaMPP improves shower curtain IoU by +18.9 while harming only desk (−2.16), whereas model chaining improved shower curtain by +16.9 but caused a −37.2 drop on toilet.

2. **Strong zero-shot navigation result with clear mechanism.** On the object navigation task, LaMPP improves class-averaged success rate from 52.7% (base) to 66.5%, a substantial +14% gain. The per-category analysis cleanly supports the claimed mechanism: objects with strong room affinities (TV Monitor: +33.0) improve dramatically, while objects with diffuse priors (Plant: −0.0) are unaffected. The comparison against a uniform prior baseline correctly isolates the effect of the LM knowledge.

3. **Clear, reproducible four-step methodology that applies across task types.** The paper's recipe (choose domain model, design label space, query LM, inference) is applied identically to three structurally different problems — a graphical model with latent rooms, a binary success variable for navigation, and a Dirichlet prior over transition parameters — demonstrating genuine generality of the framework.

4. **Transparent per-category breakdowns across all experiments.** Rather than reporting only aggregate metrics, the paper tracks best/worst per-category changes in every experiment, revealing the distribution of effects and enabling readers to assess where the method helps and where it does not.

## Weaknesses

### Fatal
None. The core idea is valid, the framework is principled, and the navigation experiment provides a compelling positive result.

### Major

1. **Overall gains on two of three tasks are very small, and no statistical significance is reported.** Semantic segmentation improves by only +0.5 mIoU (ID) and +0.2 mIoU (OOD). Video action recognition improves by +1.3% (ZS) and +0.5% (OOD) in class-averaged recall. No confidence intervals, bootstrapped estimates, or significance tests are provided anywhere in the paper. While the per-category improvements on rare classes are large (shower curtain +18.9, nightstand +8.92, held-out transitions +8.2%), the overall metrics are close to noise level. This weakens the paper's claim that LaMPP "consistently improves performance" — the evidence is concentrated in one task (navigation) with strong results, while the other two tasks show marginal support. The paper partially acknowledges this in the action recognition section (lines 488–489) but does not address it for segmentation.

2. **No calibration analysis of LM probabilities, which are the method's core component.** The method relies on extracting numeric probabilities from GPT-3 token scores (e.g., "plausible" vs. "implausible"), yet the paper provides no analysis of how well these scores are calibrated, how sensitive they are to prompt phrasing, or whether probabilities are meaningfully comparable across different object-room pairs. The abstract claims LMs "encode distributional information about real-world environments," but this is asserted rather than empirically verified against ground-truth co-occurrence frequencies. For action recognition, the paper candidly notes that LM priors are "heavily biased towards returning actions in the order they are presented" (line 489) and that over 20 prompts were tried with mixed results — this honesty is commendable, but it also reveals that the method's effectiveness depends substantially on ad-hoc prompt engineering rather than a robust probabilistic foundation.

3. **The model-chaining (MC) baseline for segmentation is suspiciously poor and inadequately diagnosed.** MC achieves 37.5 mIoU vs. the base model's 47.8 — a catastrophic 10+ point drop. While the paper notes that MC "introduces new prediction errors on far more classes," this could easily stem from a poorly chosen prompt, suboptimal decoding strategy, or an unfairly-designed string interface rather than an inherent limitation of model chaining. The paper does not provide diagnostic experiments (e.g., using a better prompt, trying different decoding strategies, or ablating components of the MC interface) to rule out implementation artifacts. This makes the claimed superiority of LaMPP over MC less convincing.

### Minor

1. **Manual annotation of room labels for navigation without mention of blinding.** The paper states (line 299) that "the first two authors of the paper manually annotated room labels in the evaluation set." It does not state whether this annotation was done blindly with respect to the evaluation results. If annotation decisions could have been influenced by knowledge of which rooms would benefit the method, this introduces potential experimenter bias.

2. **No ablation studies in the main text.** For segmentation: how much does the latent room variable help vs. directly using object co-occurrence priors? For navigation: what is the contribution of selection-step uncertainty integration vs. a simple threshold? For action recognition: how does performance vary with λ (prior strength)? The paper mentions an ablation in the appendix (line 357: "when model uncertainties are ablated, our agent actually underperforms a comparable model chaining baseline"), but this analysis is not in the main text and its details cannot be verified from the parsed content. Ablations would directly test the claimed mechanisms.

3. **The simplified decision rule for segmentation is not justified in the main text.** Line 145 mentions "several simplifications for computational efficiency" whose details are relegated to the appendix. Without understanding what these simplifications are, it is unclear whether they significantly affect the results or whether a different approximation could yield different conclusions.

4. **No discussion of limitations beyond LM calibration.** The conclusion mentions LM quality as a limitation, but other important limitations go unaddressed: reliance on manual specification of latent variables (rooms, noisy labels), sensitivity to prompt design, the need for a task-specific generative model that is not always available, and the computational cost of API calls in terms of latency and dollars (only query count is mentioned).

### Trivial
None.

## Nice-to-Haves

- A focused analysis of LM probability calibration against empirical co-occurrence frequencies (e.g., from SUN RGB-D) would strengthen the claim that the method is principled rather than ad-hoc.
- Qualitative examples (segmentation outputs before/after LaMPP, navigation trajectories) would help readers assess whether the improvements are perceptually meaningful.
- A more competitive MC baseline for segmentation (e.g., better prompt tuning) would make the comparison more convincing. For navigation, a MC baseline that precomputes room priorities (removing per-episode query overhead) would isolate whether the advantage is solely in the selection step.

## Removed Points

- **"The restriction to single-floor episodes limits generalizability"** — The paper explicitly states this is a limitation of the base Stubborn agent (line 312–313), not of LaMPP. This is a domain constraint, not a weakness of the method.
- **"One could precompute room-object probabilities for MC, making the efficiency argument less principled"** — Precomputing room priorities for MC would effectively make it resemble LaMPP, undermining the comparison. The paper's efficiency argument (LaMPP needs a fixed number of queries ahead of time vs. MC needing per-episode queries) is valid for the MC implementation described.
- **"The comparison with MC for navigation is muddled by functional equivalence"** — The paper explicitly states the equivalence applies only to the navigation step (line 352), then explains that the difference is in the selection step where uncertainty integration matters. The reviewer's criticism restates what the paper already discusses.
- **"The paper does not offer guidelines for when the label space mapping is tractable"** — This is a scope-creep request; the paper demonstrates feasibility on three tasks and does not claim to provide a complete taxonomy of tractable label spaces.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective not already present in the paper's own framing of LM priors vs. model chaining, or in its per-category analysis of where LM knowledge helps.

## Suggestions

1. **Add statistical significance testing or bootstrapped confidence intervals** for all main results (segmentation mIoU, navigation SR, action recognition recall). Given the small absolute gains on two tasks, readers need to know whether these improvements are reproducible or within noise.
2. **Add at least one ablation study to the main text** that isolates a specific component of the framework (e.g., the effect of the room variable in segmentation, or the contribution of selection-step uncertainty integration in navigation).
3. **Provide a calibration analysis** showing that LM-derived room-object probabilities correlate with empirical frequencies, or at minimum acknowledge this as an important limitation more prominently than in a single sentence.
4. **Diagnose the MC segmentation baseline** with a simple follow-up experiment (e.g., try a different prompt format for MC) to rule out prompt-engineered failure as the source of the 10-point drop.
5. **State whether room label annotation was done blindly** to evaluation outcomes.

## Score and Decision

The paper presents a conceptually appealing and principled framework for integrating LM knowledge into structured prediction. The navigation result is strong and cleanly supports the claimed mechanism. However, the empirical support is uneven — the segmentation and action recognition experiments show only marginal overall gains — and the lack of calibration analysis, statistical significance testing, and ablation studies makes it difficult to assess how much of the improvement is attributable to the framework versus prompt engineering or chance. The paper overclaims "consistent improvements" when the evidence is concentrated in one task.

This is a borderline paper with genuine contributions (the framework itself, the navigation result) but notable empirical shortcomings. I lean toward acceptance because the core idea is novel and the navigation result is compelling, but the paper would be significantly strengthened by addressing the statistical and diagnostic gaps.

**Score:** 6.0

**Decision:** Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>