Now I have all the data I need. Let me write the final consolidated review.

---

## Summary

This paper proposes a training-free, MCMC-based sampling algorithm that draws from the *power distribution* \(p^\alpha\) (with \(\alpha>1\)) of a base LLM, arguing that this distribution upweights tokens with fewer but higher-likelihood future completions — a property beneficial for reasoning. Since exact sampling is intractable, the authors design a progressive Metropolis-Hastings sampler that resamples token suffixes using the base model's own likelihoods. Experiments on Qwen2.5-Math-7B, Qwen2.5-7B, and Phi-3.5-mini-instruct show that power sampling substantially improves single-shot performance over vanilla and low-temperature sampling, and in several cases matches or exceeds GRPO-posttrained models while preserving sample diversity.

## Strengths

- **Clear theoretical motivation distinguishing power sampling from low-temperature sampling.** Proposition 1 and Example 1 (Section 4.1) provide a crisp, non-trivial analysis showing that \(p^\alpha\) favors tokens with few but high-likelihood future completions (sum of exponents), while low-temperature sampling greedily averages future likelihoods (exponent of sums) and can favor tokens with many mediocre completions. This directly connects to the critical-window phenomenon in reasoning failures.

- **Strong empirical results across model families and task types.** Table 1 demonstrates near-universal boosts over base and low-temperature baselines across three distinct model families (Qwen2.5-Math-7B, Qwen2.5-7B, Phi-3.5-mini-instruct) and four benchmarks spanning math, coding, science, and general helpfulness. Gains reach +25.2% on MATH500 and +51.9% on HumanEval (Phi-3.5-mini). The method approaches GRPO on in-domain MATH500 while outperforming it on out-of-domain tasks.

- **Preservation of generation diversity unlike RL posttraining.** Figure 5 convincingly shows that power sampling's pass@k on MATH500 continues to improve with k (reaching ~0.98 at k=16), while GRPO saturates around 0.90. This directly addresses a known downside of RL posttraining — diversity collapse — and shows the method achieves strong single-shot performance without sacrificing multi-shot capability.

- **Truly training-free and verifier-free operation.** Algorithm 1 uses only the base model's likelihoods and requires no training, no curated dataset, and no reward signal — only a small set of hyperparameters (\(\alpha\), \(B\), \(N_{\text{MCMC}}\)). This is evidenced by the complete absence of any training step in the method description and contrasts sharply with the engineering needed for GRPO. The method also works on unverifiable domains (AlpacaEval 2.0).

- **Practical block-progressive algorithm design for high-dimensional token spaces.** The progressive scheme in Algorithm 1 (Section 4.3) uses intermediate distributions \(\pi_k\) to circumvent mixing-time issues of standard MCMC in \(\mathcal{X}^T\), and provides an analytical expected-token formula (Eq. 12).

## Weaknesses

### Fatal

None.

### Major

- **The key hyperparameter \(N_{\text{MCMC}}\) is never specified, leaving compute cost unquantified.** The paper provides the analytical formula \(\mathbb{E}_{\text{tokens}} \approx N_{\text{MCMC}} T^2/(4B)\) (Eq. 12) and states \(T=3072\), \(B=192\), but never reports the actual \(N_{\text{MCMC}}\) used in experiments. Without this, it is impossible to assess the compute–accuracy tradeoff or compare against other inference-time scaling methods. The paper also lacks any compute-matched baselines (e.g., best-of-\(N\) with likelihood selection, majority voting at the same token budget) that would isolate whether the MCMC construction adds value beyond repeated sampling with equivalent compute. This omission weakens the core empirical claim that the specific MCMC approach is effective, as it could be that the gains come primarily from spending more compute rather than from the sampling principle.

### Minor

- **The "outperform RL" framing needs more careful qualification.** The GRPO baseline was posttrained only on the MATH training split. The paper is transparent about this (using "in-domain" and "out-of-domain" terminology), and the out-of-domain comparison does illustrate a genuine advantage — the sampling method does not suffer from domain specialization. However, the headline claim that power sampling "outperforms RL" should be tempered since the RL model was never intended to generalize to coding or general chat tasks. The paper would benefit from explicitly acknowledging this limitation of the RL baseline rather than letting the numbers speak for themselves.

- **No error bars or multi-seed evaluation.** Results in Table 1 are reported as single numbers with no confidence intervals or analysis of variance across runs. On small benchmarks like HumanEval (164 problems) and GPQA Diamond (198 problems), a handful of correct answers can shift accuracy by several points. While the observed gains are large enough that the qualitative conclusions are unlikely to change, reporting variance would strengthen the evidence.

- **No hyperparameter sensitivity analysis for \(\alpha\) and \(B\).** The values \(\alpha=4.0\) and \(B=192\) are stated as empirically chosen, but no sweep or sensitivity analysis is provided. If the method is brittle to these choices, the reported gains may be less reproducible. A brief sensitivity study would address this.

- **No empirical check of MCMC convergence or mixing.** The paper acknowledges that mixing time is a concern for MCMC in high-dimensional spaces and proposes the progressive block scheme as a remedy, but provides no diagnostic evidence (e.g., trace plots, acceptance rates, effective sample size) that the chain actually explores the target distribution rather than annealing to a local mode.

### Trivial

None.

## Nice-to-Haves

- A compute–accuracy tradeoff curve sweeping \(N_{\text{MCMC}}\) and comparing against baselines matched for total tokens (best-of-\(N\) with likelihood selection, repeated sampling with majority voting) would substantially strengthen the paper and help the community judge the method's practical value.
- Situating the method relative to other inference-time compute scaling approaches beyond MCMC (e.g., tree search, contrastive decoding) in the related work would better contextualize the contribution.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The abstract overstates the contribution"** (Harsh Critic) — This is a subjective judgment about framing, not a verifiable weakness. The abstract accurately describes what the paper does. REMOVED.

- **"The claim that the sampler is 'verifier-free' ignores that it uses the base model likelihood as a quality signal"** (Harsh Critic) — This misunderstands the paper. "Verifier-free" means no external reward signal or ground-truth verifier, which is what RL methods need. Using the base model's own likelihoods is the entire point of the method and is explicitly contrasted with external verifiers. REMOVED as a misunderstanding.

- **"Table 1 intermixes bold/underline conventions in a slightly confusing way"** (Harsh Critic) — Pure formatting nitpick. REMOVED.

- **Missing discussion of tree search, contrastive decoding, and other inference-time methods in related work** (Harsh Critic) — The paper cites relevant MCMC/SMC work for LLMs (Zhao et al. 2024, Faria et al. 2024). Demanding coverage of all inference-time scaling methods is scope creep. Moved to Nice-to-Haves.

- **"The pass@k analysis... without compute normalisation, the comparison to base-model pass@k is not equitable"** (Harsh Critic) — Pass@k by definition costs k times the per-sample cost for all methods. While power sampling's per-sample cost is higher, the pass@k comparison is still meaningful for the diversity preservation claim. The cost-per-sample issue is already captured under the Major weakness about N_MCMC. REMOVED as conflating two separate issues.

- **"The computational cost is unstated, making the entire evaluation uninterpretable"** (Harsh Critic, framed as fatal) — While the N_MCMC omission is a genuine gap (retained as Major), the claim that the evaluation is "entirely uninterpretable" and that the problem is "structural" requiring "a full reframing of the evaluation" overstates the severity. The paper explicitly provides the compute formula (Eq. 12) and frames the method as inference-time scaling. The missing detail is significant but fixable. DEMOTED from fatal to Major.

## Novel Insights

The paper's distinction between the power distribution \(p^\alpha\) and low-temperature sampling (Proposition 1, Observation 1, Example 1) is genuinely insightful: low-temperature sampling implements an "exponent of sums" that greedily averages future likelihoods, while \(p^\alpha\) implements a "sum of exponents" that accounts for each future path individually before aggregation. This formalizes a non-obvious limitation of temperature scaling and provides a principled motivation for MCMC-based sampling that looks beyond the next token. The connection to critical-window reasoning failures (Li et al., 2025) further anchors this insight in an existing empirical phenomenon.

## Suggestions

- Report the actual \(N_{\text{MCMC}}\) value used in all experiments and provide a sweep showing how accuracy and total token count vary with \(N_{\text{MCMC}}\). This is the single most important missing piece of information.
- Add at least one compute-matched baseline (e.g., generate many independent sequences from the base model and select the one with highest average log-likelihood, using the same total token budget as the MCMC chain) to isolate the value of the MCMC construction from simply spending more inference compute.
- Report standard deviations over at least 3 random seeds for the main benchmarks, or justify why single-run evaluation is sufficient (e.g., by noting that pass@k curves implicitly aggregate over multiple samples).
- Include a brief hyperparameter sensitivity sweep for \(\alpha\) and \(B\) to demonstrate robustness.
- Qualify the "outperform RL" language by explicitly noting that the GRPO baseline was specialized to MATH, and frame the out-of-domain results as demonstrating generalization rather than superiority.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Large Language Monkeys (0xUEBQV54B) | 5.00 | R1 | Repeated sampling study; simpler method, narrower novelty. Our paper is stronger. |
| Inference Scaling Laws (VNckp7JEHn) | 5.75 | R1/R2 | Compute-optimal inference study; math-only, empirical. Our paper has more algorithmic novelty and broader tasks. |
| TSMC for Math Reasoning (Ze4aPP0tIn) | 6.60 | R2 | SMC for math verification; needs training, math-only. Our paper is training-free and broader, most comparable anchor. |
| Smaller, Weaker, Yet Better (3OyaXFQuDl) | 7.00 | R2 | Surprising finding about compute-optimal data generation; well-executed. Our paper is comparably novel with broader evaluation but has the N_MCMC gap. |
| SMC for LLM Control (xoXn62FzD0) | 8.00 | R1 | Rigorous SMC framework with component ablations and KL analysis. Our paper has less experimental rigor. |
| Min-p Sampling (FBkpCyujtS) | 8.50 | R1 | Simple, widely-adopted sampling method. Our paper is more complex but less battle-tested. |

### Round 1 Bracket: 5.0 – 8.0
### Round 2 Bracket: 6.0 – 7.5

The paper compares most directly to the TSMC paper (6.60), which also applies Monte Carlo methods to LLM reasoning. Our paper has the advantage of being completely training-free, covering more model families and task types, and demonstrating diversity preservation. However, the TSMC paper has more rigorous experimental controls. The paper is stronger than "Inference Scaling Laws" (5.75) due to greater algorithmic novelty and task breadth, but falls short of the SMC for LLM Control paper (8.0) due to weaker experimental rigor and the N_MCMC omission. Placed against "Smaller, Weaker, Yet Better" (7.00), our paper has comparable novelty and breadth but more significant experimental gaps. The score lands at 7.0, reflecting a solid contribution with a clear, well-motivated idea, strong empirical results, but an important missing detail (N_MCMC) and the absence of compute-matched baselines that prevent full assessment of the method's practical value.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>