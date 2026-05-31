Now I have my calibration anchors. Let me write the final consolidated review.

## Summary

The paper demonstrates that normalized training loss curves (TLCs) collapse across model sizes (300M–3.9B parameters) when the AdamW timescale τ and tokens-per-parameter (TPP) ratio are matched, under practical LLM scaling recipes (μP, weight decay, co-scaled batch size, linear decay schedule). This extends prior small-scale observations (Qiu et al., 2025) to the LLM regime. The authors introduce the Celerity model family trained with fixed TPP and optimal τ, and show two applications: collapse residuals as an early diagnostic of training pathologies, and a surrogate model for normalized TLCs that enables early stopping in hyperparameter tuning.

## Strengths

1. **Demonstration of collapse at LLM scale under practical conditions**: The paper shows clean collapse across 300M–3.9B parameters (Fig. 1 middle, Fig. 6) using μP with weight decay, co-scaled batch size, and linear LR schedules—precisely the gap left open by Qiu et al. (2025), who validated collapse only on small-scale vanilla Adam without weight decay. This is the paper's strongest contribution.

2. **Identification of τ as the key modulator of TLC shape**: Sweeps over η, λ, and B (Fig. 3) demonstrate that normalized curves match when τ is held constant even when individual HPs differ. The paper provides a theoretical mechanism via a noisy quadratic model (Eq. 3, Appendix B.3) that links τ to the bias–variance trade-off.

3. **Formalization of TPP's effect on TLC shape**: The paper explains how higher TPP causes earlier flattening via scaling-law arguments (Appendix B.2) and shows scale-invariance when both TPP and τ are fixed (Fig. 4 right), connecting to known neural scaling laws.

4. **Deviation-from-collapse as an early diagnostic**: A concrete case study shows collapse residuals detecting a numerical instability in the 1.8B model at ~60% of training, well before raw loss shows a visible signal (Fig. 1 right vs. Fig. 6 right). This is a practical improvement over the subjective, late-stage criteria used in prior large-scale reports.

5. **Early stopping via small-scale surrogate model**: Fitting a parametric form (Eq. 4) on 111M-scale data and using it to predict final loss from partial large-scale runs enables selection of the best λ after only 10–30% of training (Fig. 9), outperforming the "current best" heuristic used in practice.

6. **Celerity as a principled testbed**: The Celerity family provides a useful open resource for studying scaling, trained with consistent methodology and without benchmark-targeted annealing or data contamination.

## Weaknesses

### Fatal
None.

### Major

1. **Conflation of "matched τ" with "optimal τ" as the condition for collapse**: The abstract states collapse occurs "precisely when optimization hyperparameters are set optimally for the given data budget," and the paper frames collapse as a "signature of compute-efficient training." However, the experiments directly demonstrate that collapse requires τ to be **matched** across model sizes (Fig. 3), not that the matched value must be optimal. The link to optimality is via Bergsma et al. (2025a): optimal τ depends only on TPP, so if τ is optimal for a given TPP it will be matched. But the paper provides no experiment comparing a matched-τ regime that is optimal to one that is suboptimal, nor does it test whether collapsed runs are actually more compute-efficient than non-collapsed ones at the same budget. The evidence says "matched τ → collapse," not "optimal τ → collapse." This overstates the connection between collapse and efficiency and weakens the paper's headline narrative. (Relevant text: Abstract lines 9-10: "loss curves collapse across scales precisely when optimization hyperparameters are set optimally for the given data budget"; Sec. 3 Key takeaway 1.)

2. **Uncontrolled comparison for the compute-efficiency frontier claim**: Figure 2 positions Celerity on the accuracy/compute Pareto frontier against open models. The paper itself notes (Sec. 4, line 159) that most public LLMs "anneal on training subsets of downstream benchmarks," making evaluation problematic, yet the frontier plot uses average accuracy on the same types of benchmarks (arc-c, arc-e, boolq, hellaswag, piqa, siqa, winoqrande) that other models may have been tuned for. The paper cannot simultaneously argue that benchmark-specific training invalidates comparisons and then use those same benchmarks to claim frontier status. A controlled comparison (e.g., against models known to forgo such techniques, or on held-out tasks not in any model's training data) would be needed.

### Minor

1. **Diagnostics evidence rests on a single anecdote**: The entire evidence that collapse residuals provide an "early, sensitive diagnostic of training pathologies" (abstract) is one example—the 1.8B numerical issue. There is no false-positive analysis, no test across multiple pathology types, no baseline comparison with other detection methods. While the example is compelling, the paper presents this as a general capability without systematic support.

2. **Early stopping validated only on λ sweeps**: The early stopping procedure is tested on λ sweeps at two model sizes (1.7B and 3.3B, Fig. 9). The paper frames the method as general for hyperparameter tuning (Sec. 5), but it is not tested on other HP types (learning rate, batch size, or combinations). Cases where τ must vary (e.g., B > B_crit) are noted but not experimentally addressed.

3. **Early-align normalization not validated against full normalization**: The "early-align" strategy (aligning partial curves to the smallest-scale curve over 25–50% of training, Sec. 4) is used for online diagnostics, but the paper does not evaluate how accurately this estimates L(T) across scales compared to knowing L(T) directly.

4. **No uncertainty quantification for surrogate model predictions**: The surrogate model predictions (Fig. 8) and early stopping results (Fig. 9) are shown without error bands or run-to-run variability. Multiple runs per setting would demonstrate robustness to noise.

5. **TPP trade-off analysis uses power-law coefficients from prior work without refitting**: The analysis showing 62% parameter reduction for 67% FLOPs increase (Fig. 5, Sec. 4) uses Hoffmann et al.'s coefficients, implying a precision unwarranted without fitting to Celerity's own scaling data.

6. **Sensitivity of surrogate model parameters not explored**: The functional form (Eq. 4) fixes ε₁=0.001, ε₂=0.1, and m=0.05. The sensitivity of predictions to these choices is not examined. The alternating fitting procedure (b then q, iterate) is described without convergence evidence.

### Trivial
None.

## Nice-to-Haves

- Testing the diagnostic on at least 2–3 additional pathology types (e.g., loss spikes, data contamination) or a controlled injection experiment to measure detection latency.
- Validating early stopping on at least one additional HP type (e.g., learning rate or batch size sweep).
- Providing error bars or confidence intervals for the surrogate model fits and early stopping gaps.
- Validating the early-align normalization strategy against the full normalization by comparing estimated L(T) with known values.
- Refitting Chinchilla-style coefficients on Celerity's own data for the TPP trade-off analysis.

## Removed Points

Points removed from the harsh critic's review because they are either factually incorrect, misunderstandings, style nitpicks, or speculative:

1. **"Check the definition of τ in Eq. 2... should be explicitly linked to the equation."** — The definition is already clear from Eq. 2 and the surrounding text. This is a minor presentation preference, not a substantive weakness.

2. **"The effect of TPP is explained via the power-law perspective... the paper could be clearer about when the explanation applies to linear decay schedules."** — The paper explicitly discusses both constant-LR and linear decay schedules in Sec. 3 (line 133: "LR schedules deform the curves, but deformation is also scale invariant given consistent curvature of the loss landscape"), which adequately addresses this.

3. **"The paper would benefit from a clearer statement of limitations."** — This is a suggestion for improvement, not a weakness. The paper's conclusion could be more thorough, but this is a presentation preference, not an evidential gap.

4. **"The derivation of Eq. 3 assumes a noisy quadratic model with constant LR... The claim that 'the normalized TLC depends only on τ and t̂' relies on the assumption that residual bias at end-of-training is negligible. This is not checked empirically."** — The paper explicitly states "Provided residual bias at end-of-training is negligible relative to the variance floor" (line 131) as a caveat to the theoretical model. This is a reasonable simplifying assumption for a theoretical model; the empirical validation in Fig. 3-4 provides practical support.

5. **"Falcon's final LR was chosen by simply continuing the run performing best after warmup" — the paper cites this as an example of lacking principled account but this is about the criticism of the paper not about the paper itself.** — Removed because this is part of the paper's motivation, not a weakness of the paper.

## Novel Insights

The harsh critic's framing of the "matched τ vs. optimal τ" distinction is the most incisive observation across the reviews. While the paper presents collapse as a "signature of compute-efficient training," the experiments actually establish that collapse requires matched τ across model sizes — the efficiency claim is parasitic on Bergsma et al. (2025a)'s result that optimal τ depends on TPP, which the paper does not independently verify. This distinction matters because it changes the practical recommendation: practitioners can use collapse as a diagnostic of consistent training even when not training at the compute-optimal TPP. The core empirical finding (collapse at LLM scale under practical recipes) is robust independent of this framing debate.

## Suggestions

1. **Reframe the abstract and introduction**: State that collapse occurs when τ and TPP are **matched** across model sizes (which the evidence directly supports), and note that optimality is aligned with collapse via Bergsma et al.'s finding that optimal τ depends only on TPP. This separates the well-supported claim from the overextension.

2. **Caveat the compute-efficiency claim**: Either provide a controlled comparison (e.g., compare Celerity against models that also forgo benchmark-targeted annealing, or show that non-collapsed runs trained at the same budget are worse) or clearly frame the frontier plot as "among models trained without benchmark-specific data annealing."

3. **Strengthen the diagnostic evidence**: Add at least 2–3 additional cases (e.g., a controlled injection experiment) or explicitly characterize the diagnostic as an initial demonstration rather than a validated method.

4. **Broaden early stopping validation**: Test on at least one additional HP type (learning rate or batch size sweep) at one scale.

5. **Add uncertainty quantification**: Provide error bands or seed variability for the surrogate model predictions and early stopping results.

6. **Validate early-align**: Show how accurately the early-align strategy recovers L(T) across scales.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| SaOxhcDCM3.md (Self-consuming loop) | 3.20 | R1 | Different topic (model collapse from synthetic data) |
| f7aWmxgSN4.md (Universality in KG learning) | 3.00 | R1 | Different topic |
| 6Mdvq0bPyG.md (EfficientQAT) | 3.00 | R1 | Different topic (quantization) |
| BUpdp5gETF.md (Decoupled LR schedules) | 2.50 | R1 | Different topic |
| o9YC0B6P2m.md (Scaling Law with LR Annealing) | 6.75 | R1 | Very relevant — loss curve prediction. Current paper is stronger (more empirical substance, released models, concrete applications) |
| KnoS9XxIlK.md (Multi-Power Law) | 6.00 | R1 | Very relevant — loss curve prediction. Current paper is stronger (up to 3.9B, actual trained models, applications) |
| xGM5shdGJD.md (Hitchhiker's Guide) | 5.20 | R1 | Somewhat relevant (scaling law estimation meta-study) |
| BDisxnHzRL.md (Scaling Laws Downstream) | 4.25 | R1 | Partially relevant |
| d8w0pmvXbZ.md (Small-scale proxies for instabilities) | 8.00 | R1 | Very relevant — training stability at scale. Current paper is weaker (less clean comparisons, overselling) |
| wg1PCg3CUP.md (Scaling Laws for Precision) | 8.00 | R1 | Somewhat relevant |
| Tzh6xAJSll.md (Scaling Laws for Associative Memories) | 7.60 | R1 | Partially relevant |
| et5l9qPUhm.md (Strong Model Collapse) | 8.00 | R1 | Different "collapse" (model collapse from synthetic data) |

**Bracket after R1:** 5.0 to 7.5

**Round 2 (Narrowing):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| o9YC0B6P2m.md (Scaling Law with LR Annealing) | 6.75 | R2 | Very relevant. Current paper is stronger — more empirical contributions |
| P7KRIiLM8T.md (u-μP) | 7.33 | R2 | Very relevant (HP transfer). Current paper is weaker — cleaner experiments, better controlled |
| 5HCnKDeTws.md (When Scaling Meets Finetuning) | 6.75 | R2 | Partially relevant |
| KZJehvRKGD.md (Depthwise HP Transfer) | 7.50 | R2 | Somewhat relevant |

### Final Score Determination

The paper is stronger than the loss-curve prediction anchors at 6.00-6.75 (o9YC0B6P2m, KnoS9XxIlK) because it demonstrates a concrete empirical phenomenon at LLM scale, releases a trained model family, and has two practical applications. However, it is weaker than the clean, well-controlled papers at 7.33-8.00 (P7KRIiLM8T, d8w0pmvXbZ) because of its overselling of claims (conflating matching with optimality), uncontrolled comparison for the frontier claim, and limited validation of the applications. The core phenomenon is genuinely useful and the paper has real contributions, but the framing issues and insufficient validation prevent it from reaching the top tier.

**Score: 6.5** — A solid paper with a real contribution that deserves acceptance after revisions addressing the framing and validation concerns.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>