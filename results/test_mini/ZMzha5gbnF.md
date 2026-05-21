Now I have all the evidence needed to write the consolidated review.

## Summary

This paper identifies and quantifies the *priming vulnerability* in Masked Diffusion Language Models (MDLMs)—the tendency for affirmative tokens appearing at intermediate denoising steps to steer generation toward harmful responses even in safety-aligned models. The authors design two attacks (anchoring attack with process intervention, and First-Step GCG without intervention) and propose Recovery Alignment (RA), a training method that conditions the model to generate safe responses from contaminated intermediate states. Experiments across three MDLMs, two datasets, and three evaluators show RA reduces anchoring attack ASR from 17.3% to 0.0% at step 1 on LLaDA while preserving general capability across 11 benchmarks.

## Strengths

- **Systematic quantification of a novel vulnerability.** Section 4.1 and Figure 2 use a controlled anchoring attack to show that injecting even a single affirmative token at the first denoising step increases ASR from 2% to 21% on LLaDA Instruct (and up to 85% on unaligned MMaDA). This provides a repeatable, quantitative measurement that goes beyond prior heuristic attacks (PAD, DiJA).

- **Recovery Alignment dramatically mitigates the vulnerability.** Table 2 shows RA reduces anchoring attack ASR from 17.3% to 0.0% at intervention step 1 (LLaDA), from 14.7% to 1.0% (LLaDA 1.5), and from 90.0% to 6.3% (MMaDA). The ablation "RA w/o inter" (same training but starting only from fully masked sequences) yields substantially higher ASR (e.g., 7.3% vs. 0.0% at step 1 on LLaDA), isolating the contribution of training on contaminated intermediate states.

- **Comprehensive and fair evaluation.** The paper spans three MDLMs, two datasets (JBB-Behaviors, AdvBench), three evaluators (GPT-4o, LLaMA Guard 3, keyword matching), four priming-exploiting attacks, and three conversational jailbreak attacks. ASR is reported as mean ± std over three runs (Tables 1–3). Baselines include SFT, DPO, MOSA, and the RA w/o inter ablation.

- **General capability is preserved.** Table 4 reports performance on 11 diverse benchmarks; RA shows no systematic degradation (e.g., LLaDA: avg 52.2% → 52.6%). This addresses a critical practical concern for any alignment method.

- **Informative ablation studies.** Figures 3a and 3b systematically compare linear vs. uniform vs. constant scheduling and the effect of the maximum intervention step t_max, providing actionable design guidance. The observation of reward hacking at excessively large t_max is honestly presented.

## Weaknesses

### Major

- **Theorem 4.1 relies on an unverified monotonicity assumption in the main paper.** The lower bound for First-Step GCG assumes log π_θ(˜r_{t+1} = r | q, r_t) ≥ log π_θ(˜r_1 = r | q, r_0) for all t. While the paper provides a plausible informal rationale (richer context → more concentrated probability mass) and claims empirical validation in Appendix C.2, the assumption is nontrivial: the model at later steps must assign higher probability to the *full target sequence* r, not just the already-fixed tokens. The main paper does not independently verify this. Importantly, the attack succeeds empirically regardless (Table 1 shows 20× speedup and up to 4× higher ASR than MC GCG), so the core contribution does not depend on a watertight theoretical justification. The authors should soften the theoretical framing or provide in-line evidence.

### Minor

- **Missing experimental detail: number of Monte Carlo samples for MC GCG.** Table 1 shows MC GCG as a baseline but does not report how many denoising trajectories were sampled per gradient step. This is needed to assess whether the comparison is fair and whether the MC baseline could be improved with more samples.

- **No analysis of reward model sensitivity.** RA is instantiated with DeBERTaV3 as the reward model, but there is no ablation varying the reward model (e.g., a different classifier, LLM-as-a-judge scores). The quality of the reward signal directly affects RA's behavior; without a sensitivity check, it is unclear how robust the results are to this design choice.

- **Missing variance estimates for general capability benchmarks (Table 4).** Unlike Tables 1–3, Table 4 reports only point estimates. Given the small differences across conditions, standard errors or confidence intervals would help assess whether observed changes are meaningful.

### Trivial

None.

## Nice-to-Haves

- A DPO-style variant of RA (acknowledged in the Limitations section) would provide an alternative instantiation if data-construction costs can be addressed.
- Reporting the computational cost of RA training (e.g., GPU-hours) would help practitioners—the paper notes this is in Appendix C.4 (stripped by parser).
- Clarifying whether the DeBERTaV3 reward model is the BeaverTails safety classifier or a generic reward model would improve reproducibility (the citation to Köpf et al. 2023 strongly suggests the former).

## Removed Points

These points were considered but removed with justification:

- **"Computational cost of RA training not reported"** — The paper explicitly states this is in Appendix C.4, which was stripped by the parser. Not a genuine omission.
- **"Reward model details not specified"** — The paper states DeBERTaV3 and cites Köpf et al. 2023 (BeaverTails), which provides sufficient context.
- **General formatting/style nitpicks** and **reproducibility nitpicks about trivial implementation details** — removed per hard rules.
- **Strength Finder: generic/superficial strengths** about "importance of the problem" without concrete evidence — removed.
- **Strength Finder: strength about Theorem 4.1 as a "tractable theoretical lower bound"** — retained but tempered; the practical benefit (efficient attack) is genuine and supported by Table 1, even though the theoretical justification has caveats.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Soften the claim in Theorem 4.1.** Present it as a practically motivated surrogate rather than a rigorous lower bound, or provide in-line empirical validation of the monotonicity assumption without relegating it entirely to the appendix.
2. **Report the MC sample count** used for Monte Carlo GCG in Table 1.
3. **Add a reward model ablation** (e.g., compare DeBERTaV3 with an LLM-as-a-judge reward or a different safety classifier) to bound sensitivity concerns.
4. **Report standard deviations or confidence intervals** for the general capability benchmarks in Table 4.

## Score and Decision

### Calibration Summary

**Round 1 (Bracketing):** Searched across three bands for "diffusion language model safety jailbreak."
- Weak band (< 3.5): returned papers averaging 2.5–3.0 (reject quality, clearly below the paper under review).
- Middle band (3.5–7.5): returned 4 relevant anchors — DIJA (avg 5.0, Accept Poster), DiffuGuard (avg 5.2, Accept Poster), and two off-topic papers at 4.0. The paper under review is clearly stronger than DIJA and DiffuGuard.
- Strong band (> 7.5): returned papers averaging 8.0 but on unrelated topics (multi-turn conversation, transduction, multimodal). Not directly comparable.
- **Bracket: 5.0–6.5.**

**Round 2 (Narrowing):** Searched for "diffusion language model safety alignment vulnerability mitigation" (5.5–7.5) and "priming vulnerability diffusion model defense recovery" (4.5–6.5). Retrieved Temporal Dynamics paper (avg 6.0, Accept Poster) and Self-Destructive LMs (avg 6.5, Accept Poster). The paper under review has a cleaner novelty story and fewer weaknesses than the Temporal Dynamics paper, which faced criticism about limited methodological novelty and dataset scope. It is clearly stronger than the 5.0–5.2 anchors and comparable to the 6.0 anchor.

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| DIJA ("The Devil behind the mask") | 5.0 | R1 | Weaker: attack-only, missing ablations, stronger baseline outperforms |
| DiffuGuard | 5.2 | R1 | Weaker: defense-only, major criticism about no adaptive attacks |
| Temporal Dynamics in dLLMs | 6.0 | R2 | Comparable: both have clear contributions, but current paper has better novelty |
| Self-Destructive LMs | 6.5 | R2 | Stronger: different topic but higher execution quality |
| VLM jailbreak ("UltraBreak") | 6.0 | R2 | Different domain, comparable quality tier |

**Final Score:** 6.0. The paper makes a well-supported empirical contribution (novel vulnerability + effective defense + thorough evaluation) with weaknesses that are addressable without changing the core findings.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>