Now I have enough information for calibration. Let me compile my final review.

**Calibration Summary:**

Round 1 bracket: The paper sits between weak anchors (~3.0-3.4) and strong anchors (8.0). Middle-band anchors (3.5-7.5) are the relevant comparison. Initial bracket: **5.0-6.5**.

Round 2 anchors consulted:
- **DDPP (Ombm8S40zN, 6.25, Accept)**: Steering masked discrete diffusion via posterior prediction. Requires fine-tuning a secondary model. More rigorous evaluation but different approach. IterRef is comparable in scope and novelty but has weaker empirical rigor (no error bars, conflated NFE). IterRef is slightly weaker.
- **DRAKES (G328D1xt4W, 6.00, Accept)**: Fine-tuning discrete diffusion via Gumbel-softmax. Similar domain. IterRef has a more novel approach (inference-time, no training) but DRAKES has cleaner evaluation. Comparable quality, IterRef slightly below.
- **DNO (x1uv2gdjKV, 5.50, Reject)**: Inference-time noise optimization for continuous diffusion. IterRef is stronger — more novel method, broader evaluation across modalities. IterRef is above DNO.
- **Guidance Paper (XsgHl54yO7, 6.50, Accept)**: Guidance for discrete state-space models. Similar space. IterRef has stronger theory (MTM convergence) but weaker evaluation. IterRef is slightly below.
- **SVDD (2fgzf8u5fP, 3.80, Reject)**: Derivative-free guidance for diffusion. IterRef is significantly stronger in both method and evaluation.

Final score anchored between DNO (5.50, reject) and DRAKES/DDPP (6.00-6.25, accept). IterRef is stronger than DNO but weaker than DDPP due to evaluation gaps.

**Final score: 5.5, Decision: Reject** (borderline, needs revision)

Now let me write the consolidated review.

Actually, wait. Let me reconsider the NFE issue more carefully. The harsh critic says "IterRef makes numerous reward model evaluations per proposal (one per candidate in Algorithm 2, Line 7), whereas baselines like BoN use far fewer reward evaluations for a given generative budget."

Let me think about this:
- IterRef at a given timestep: N candidates, each gets one reward evaluation → N reward evaluations per refinement step
- If there are k refinement steps at that timestep: k × N reward evaluations
- BoN: generate N full sequences, evaluate reward on each → N reward evaluations total

But the paper counts NFE as "both generative model calls and reward model calls on equal footing." So if IterRef uses k×N reward evaluations and BoN uses N reward evaluations, under the same NFE budget, IterRef would have fewer generative model calls. This is the core issue.

However, the paper does acknowledge this (line 178): "aggregating these into a single NFE value may obscure meaningful differences, and it is preferable to report generative-model calls and reward-model calls separately."

This is a genuine weakness because:
1. The main results use conflated NFE
2. The separate reporting is deferred to the appendix
3. The wall-clock time analysis is also deferred to the appendix

Without seeing the appendix (which was stripped), I can't verify whether the separate reporting resolves the concern. But based on what's in the paper, this is a real weakness that needs addressing.

OK, final score: **5.5** with **Reject** decision. Let me write the review.Now I'll write the consolidated final review.

## Summary

This paper proposes **IterRef**, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with noising-denoising transition kernels to iteratively refine intermediate states toward a reward-aligned distribution. The approach is grounded in MCMC theory with a convergence guarantee, and uses a cleverly chosen balancing function to simplify the acceptance rule to a reward-dependent comparison. Experiments span two language diffusion models (MDLM, LLaDA-8B) and one image model (MaskGIT) across multiple reward objectives.

## Strengths

1. **Novel, principled methodology.** The framing of iterative refinement for discrete diffusion through the MTM framework with a noising-denoising transition kernel is technically novel and well-motivated. The balancing function design (Eq. 2) that yields a tractable acceptance rate (Eq. 3) is a genuine technical contribution, and Proposition 1 establishes convergence in principle. This gives IterRef a theoretical foundation that heuristic guidance methods (BoN, FK) lack.

2. **Consistent empirical gains across diverse settings.** IterRef achieves higher reward scores than all baselines (FK, SVDD, SoP, BoN) on essentially all tasks with the MDLM backbone and on most tasks with the LLaDA-8B backbone (Figure 2). On Sentiment, CoLA, and Perplexity with MDLM, IterRef at only 2T NFEs surpasses all baselines at 32T NFEs — a dramatic efficiency gain. The image results with MaskGIT (Table 1) confirm the pattern holds across modalities, with IterRef reaching 33.7 CLIPScore at budget 2 vs. 32.1 for the best baseline.

3. **Useful analysis of discrete diffusion dynamics.** The effective timestep study (Table 2) shows that later denoising stages (0.1T) matter more for discrete diffusion, contrasting with continuous diffusion where early stages dominate. The k vs. N analysis (Table 3, Figure 4) cleanly demonstrates that iterative refinement is more effective than simply increasing the particle count — a finding that directly validates the paper's core design choice.

4. **Addresses a genuine gap.** The paper identifies a real problem: existing test-time scaling methods for discrete diffusion lack mechanisms for mid-trajectory correction, and IterRef's MCMC-based iterative refinement is a principled solution.

## Weaknesses

### Fatal
None.

### Major

1. **NFE accounting conflates generative and reward-model costs, and this obscures the fairness of comparisons.** The paper counts generative model calls and reward model calls on equal footing under "NFE." IterRef uses many more reward-model evaluations than baselines (N per refinement step, times k steps, vs. N total for BoN). The paper acknowledges this (Section 3.3: "aggregating these into a single NFE value may obscure meaningful differences") and defers separate reporting and wall-clock analysis to the appendix. However, the main results (Figure 2, Table 1) all use this conflated metric, so the reader cannot determine from the main paper whether IterRef's gains reflect better methodology or simply more reward-model budget. For a paper whose central claim is about test-time *scaling efficiency*, this is a significant evidential gap.

2. **No variance or significance reporting.** All quantitative results are reported as single mean values with no standard deviations, confidence intervals, or significance tests. With 300 generations per condition (15 prompts × 20 samples), the sample size is adequate for reporting variance. Many reported differences are small (e.g., 0.5–1.0 CLIPScore points in Table 1), making it impossible to assess reliability. This undermines confidence in the quantitative claims.

3. **Convergence guarantee is stated for an idealized setting that does not match the practical algorithm.** Proposition 1 guarantees convergence to the optimal intermediate distribution *p***(x_t)*, but requires exact access to the true reward-aligned distribution for intermediate states. In practice (Section 3.1, last paragraph), *r(x_t)* is approximated by evaluating the reward on the denoiser's predicted *x_0* given *x_t*. The paper does not discuss how this approximation affects the convergence guarantee, leaving a gap between theory and practice.

### Minor

4. **The CoLA-on-LLaDA counterexample is acknowledged but not fully analyzed.** On LLaDA-8B with the CoLA objective (Figure 2b), BoN outperforms IterRef at higher compute budgets. The paper attributes this to LLaDA already generating well-formed text, making refinement less effective. This explanation is plausible but post-hoc; the paper provides no ablation or failure analysis to understand *why* refinement hurts here, which would be valuable for understanding the method's limitations.

5. **Undefined baselines in the detoxification case study.** Figure 5(a) lists baselines "SLP, SR, SVTOD" that are never defined in the paper text. The main baselines section defines BoN, SoP, SVDD, and FK, but these acronyms do not match. This is a clarity issue that prevents the reader from understanding what is being compared.

### Trivial
None.

## Nice-to-Haves

- Sensitivity analysis for the temperature hyperparameter *α* (the paper studies *k* vs *N* and timesteps but not *α*).
- Per-prompt statistics showing whether gains are consistent or driven by a subset of prompts.

## Removed Points

These points were raised by reviewers but are removed per the filtering rules:

- **"Pool reuse may break convergence guarantee"** (Harsh Critic, Section 3.3 discussion): The paper's pool reuse is a practical optimization; whether it preserves the theoretical guarantee is a reasonable question but the critic's framing ("reusing correlated samples") is speculative and not verified against the paper's actual analysis. This is appropriately treated as a discussion point, not a weakness.
- **"Figure 1b 8× faster claim is only supported by one comparison"**: The paper explicitly contextualizes this claim to the Toxicity/MDLM setting (Section 4.2, MDLM Results), and also shows similar qualitative gains for LLaDA in Figure 1b. The claim is properly scoped; the reviewer overstated this.
- **Criticisms about missing related works**: Automatically removed per rules (no external verification possible).
- **Formatting/style nitpicks**: Removed per rules (parser artifacts).

## Novel Insights

None beyond the paper's own contributions. The strengths and weaknesses above are well-captured by the paper's own framing and the reviewer analysis.

## Suggestions

1. **Fix the NFE accounting in the main paper.** Report generative-model calls and reward-model calls separately for all methods in the main results (not just the appendix). Show that the advantage is not driven by a greater number of reward evaluations. Include wall-clock time comparisons.

2. **Add error bars or confidence intervals** to all quantitative results (Figure 2, Tables 1–3). This is essential for the community to assess whether the reported improvements are statistically reliable.

3. **Discuss the theory-practice gap explicitly.** State the convergence guarantee for the ideal case and explain what is lost (or preserved) when *r(x_t)* is approximated from *x_0* prediction.

4. **Analyze the CoLA failure case.** Add an ablation to explain why IterRef underperforms BoN on CoLA with LLaDA (e.g., is the intermediate reward approximation poor for CoLA? Does refinement disrupt already-fluent generations?). This would strengthen the paper's framing and help users understand when IterRef is beneficial.

5. **Define all baselines** used in the detoxification experiments (Figure 5a).

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched three bands — weak (≤3.5), middle (3.5–7.5), strong (≥7.5). Middle-band papers (avg 3.8–6.5) were most relevant. Initial bracket: **5.0–6.5**.

**Round 2 (Narrowing):** Searched within (4.5, 6.5) and (6.0, 8.0) for discrete diffusion guidance and inference-time alignment.

Anchors retrieved:

| ID | Avg Score | Round | Comparison |
|---|---|---|---|
| DDPP (Ombm8S40zN) | 6.25, Accept | R2 | Steering discrete diffusion via posterior prediction. More rigorous evaluation but requires fine-tuning. IterRef is slightly weaker due to evaluation gaps. |
| DRAKES (G328D1xt4W) | 6.00, Accept | R2 | Fine-tuning discrete diffusion. Similar domain. IterRef has more novel inference-time approach but weaker empirical rigor. |
| DNO (x1uv2gdjKV) | 5.50, Reject | R2 | Inference-time noise optimization (continuous diffusion). IterRef is stronger — more novel, broader evaluation. |
| Guidance Paper (XsgHl54yO7) | 6.50, Accept | R2 | Guidance for discrete state-space models. IterRef has stronger theory but weaker evaluation. Slightly below. |
| SVDD (2fgzf8u5fP) | 3.80, Reject | R2 | Derivative-free guidance. IterRef is significantly stronger. |
| C-CoDe (MBDH5zyxHM) | 4.60, Reject | R2 | Controlled denoising. IterRef is substantially stronger. |

**Final bracket reasoning:** IterRef is clearly above DNO (5.50) and below DDPP (6.25). It is comparable to DRAKES (6.00) but with weaker empirical rigor. The conflated NFE metric and lack of error bars are significant concerns that prevent the paper from reaching the acceptance-level confidence of DDPP or the Guidance paper.

**Final Score: 5.5**  
**Decision: Reject**

The paper introduces a novel and principled method for an important problem, and the empirical results are promising. However, the conflated NFE accounting in the main results and the absence of any variance reporting mean the quantitative claims are not securely supported. These are addressable issues, and a revised version that provides separate cost reporting, error bars, and explicit discussion of the theory-practice gap could be competitive for acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>