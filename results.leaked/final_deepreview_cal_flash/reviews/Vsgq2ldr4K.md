## Summary

This paper proposes a training-free inference-time sampling algorithm based on MCMC to sample from the power-sharpened distribution \(p^\alpha\) of a base language model. The core idea is that by spending additional compute at inference time to iteratively resample token subsequences via Metropolis-Hastings, one can elicit single-shot reasoning performance comparable to — and in some cases exceeding — RL post-training (GRPO), without requiring any training data, verifier, or reward model. The paper provides a theoretical clarification that \(p^\alpha\) differs from low-temperature sampling (Proposition 1) and presents experiments across three model families (Qwen2.5-Math-7B, Qwen2.5-7B, Phi-3.5-mini-instruct) and four benchmarks (MATH500, HumanEval, GPQA, AlpacaEval 2.0).

## Strengths

1. **Clear theoretical distinction between power distribution and low-temperature sampling.** Proposition 1 and Example 1 in Section 4.1 rigorously prove that sampling from \(p^\alpha\) is not equivalent to low-temperature (\(\tau=1/\alpha\)) sampling, and demonstrate that \(p^\alpha\) preferentially up-weights tokens with fewer but higher-likelihood future completions — a property intuitively tied to handling "pivotal tokens" that cause reasoning failures. This provides principled motivation for targeting \(p^\alpha\) rather than simply lowering temperature.

2. **Strong empirical results across diverse models and tasks.** Table 1 shows that power sampling matches GRPO on in-domain MATH500 (e.g., 74.8% vs. 78.5% for Qwen2.5-Math-7B) and outperforms GRPO on multiple out-of-domain tasks — most strikingly on HumanEval where power sampling achieves 73.2% vs. GRPO's 13.4% for Phi-3.5-mini-instruct. These gains are consistent across three model families and four benchmarks, lending credibility to the approach.

3. **Preservation of generation diversity.** The pass@\(k\) curves in Figure 5 demonstrate that power sampling avoids the diversity collapse characteristic of RL post-training: its multi-shot performance rises with \(k\) and eventually matches the base model at high \(k\), whereas GRPO plateaus after \(k\approx4\). The likelihood and confidence histograms in Figure 4 further confirm that power sampling maintains a broader distribution than GRPO. This addresses a known limitation of RL fine-tuning.

4. **Thoughtful algorithmic design for the MCMC mixing challenge.** Algorithm 1's progressive block-extension scheme (Equation 10) partitions generation into shorter intervals and uses samples from intermediate distributions to initialize the next stage — a practical approach to mitigating the exponential mixing time that plagues naive MCMC in high-dimensional token spaces. The accompanying token-cost analysis (Equation 12) quantifies the compute trade-off.

5. **Verifier-free and training-free formulation.** The method requires no training data, no reward model, and no verifier signal. The strong results on AlpacaEval 2.0 (a subjective helpfulness benchmark with no ground-truth verifier) demonstrate applicability beyond domains with easily verifiable rewards, which is a genuine practical advantage over RLVR methods.

## Weaknesses

### Fatal
None.

### Major

1. **The MCMC step count \(N_{\text{MCMC}}\) is never reported.** Algorithm 1 defines \(N_{\text{MCMC}}\) as a core hyperparameter, and the token-cost analysis (Equation 12) scales as \(N_{\text{MCMC}} \cdot T^2/(4B)\). Yet the paper never states what value was used in the experiments. The only guidance is a qualitative statement that "we empirically find a value for \(B\) that makes Algorithm 1 performant for relatively small values of \(N_{\text{MCMC}}\)" (end of Section 4.3). Without \(N_{\text{MCMC}}\), the method cannot be reproduced, the computational cost cannot be assessed, and readers cannot judge whether the claimed gains come from the algorithm's design or from an enormous inference budget.

2. **Missing the most natural inference-time baselines.** The paper compares only to low-temperature sampling (single-pass) and GRPO (RL-trained). It does **not** include standard inference-time scaling techniques such as **best-of-\(N\) sampling** (generate \(N\) samples, select the one with highest base-model likelihood) or **self-consistency / majority voting**. These are the direct competitors for a method that spends extra compute at inference time without training. Because the MCMC procedure is computationally expensive (Equation 12), it is entirely possible that a simple best-of-\(N\) baseline with matched token budget would match or exceed the reported results. Without this comparison, the paper's central claim that the *specific MCMC procedure* adds value beyond merely spending more compute is not adequately supported.

3. **No ablation studies of key hyperparameters.** The method introduces several free parameters: \(\alpha\) (power exponent), block size \(B\), MCMC steps \(N_{\text{MCMC}}\), and proposal temperature \(\tau\). Only a single configuration (\(\alpha=4.0\), \(B=192\), unspecified \(N_{\text{MCMC}}\), \(\tau=1/\alpha\)) is reported for reasoning tasks, with \(\tau\) changed to 0.5 for AlpacaEval without any analysis of the impact. The sensitivity of the algorithm to these choices is unknown, making it impossible to assess robustness or provide practical guidance.

4. **Unexplained discrepancy between Table 1 and Figure 5.** Table 1 reports Power Sampling at **74.8%** on MATH500 for Qwen2.5-Math-7B. Figure 5 shows the same method on the same model and dataset at ~**72%** for \(k=1\) (pass@1). Both should measure single-shot accuracy. The \(\sim\)2.8 percentage point gap needs explanation — it could stem from different random seeds, different subsets, or a plotting artifact, but the paper does not address this.

### Minor

5. **Results are point estimates without uncertainty quantification.** All numbers in Table 1 and Figure 5 lack error bars, confidence intervals, or variance across seeds. Given the stochasticity of the MCMC sampling process, it is difficult to assess whether differences between methods are statistically significant.

6. **The out-of-domain RL comparison is overclaimed.** The paper repeatedly states that power sampling "outperforms RL" on HumanEval, GPQA, and AlpacaEval, but the GRPO baseline is trained *only* on the MATH training split. Its degraded performance on non-mathematical tasks is expected and reflects the narrow training distribution, not a fundamental limitation of RL. The paper acknowledges this in passing ("out-of-domain") but the headline framing ("outperforms RL") lacks the necessary caveat that the comparison is against a domain-specialised RL model, not a general-purpose one.

7. **Pass@\(k\) diversity analysis limited to MATH500.** The diversity advantage claim would be substantially stronger if pass@\(k\) curves for at least one additional task (e.g., HumanEval) appeared in the main paper rather than being relegated to the appendix.

### Trivial

- The paper could report the acceptance rate of the MH steps, which would help assess mixing efficiency.
- The bar chart in Figure 1 is visually appealing but the underlying table duplicates information — one representation would suffice.

## Nice-to-Haves

- A compute-matched comparison against best-of-\(N\) sampling (with \(N\) chosen so that the total forward-pass cost equals that of power sampling) would cleanly separate the benefit of the MCMC procedure from the benefit of additional compute.
- Ablations of \(\alpha\) (e.g., 2, 4, 8) and \(B\) (e.g., 96, 192, 384) on at least one task would greatly improve reproducibility and practical guidance.
- Reporting wall-clock time per sample, or at minimum the average number of tokens generated per sample, would help readers assess practical viability.
- A brief discussion of failure cases or settings where power sampling underperforms low-temperature sampling would improve the paper's balance.

## Removed Points

These points were raised by reviewers but are not included in the main weaknesses above because they are either factually incorrect, misread the paper, or are noise:

- **The claim that the method is misleadingly described as "the base model is smarter than you think."** The paper explicitly states it "leverages additional compute at inference time" and describes the algorithm's computational cost. The framing is an accurate reflection of the finding that base models, when sampled differently, can match RL-trained models.
- **The criticism that Observation 1 is "speculative" and that experiments do not isolate whether benefits come from the target distribution or extra compute.** The experiments do show power sampling outperforming low-temperature sampling (which also involves no extra training), isolating at least part of the benefit to the distribution choice. The missing compute-matched baseline is already listed as a major weakness.
- **The criticism that the method's training-free advantage is overstated because the method uses expensive sampling.** The paper (Section 4.3, Equation 12) explicitly discusses the inference-time compute cost. The advantage is framed as "training-free, dataset-free, and verifier-free," which is factually accurate.
- **Various presentational nitpicks about the abstract, introduction, and conclusion framing.** These do not affect the paper's technical contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not provide.

## Suggestions

1. **Report \(N_{\text{MCMC}}\) immediately** in the experimental setup, alongside the average token-generation cost per sample. This single fix resolves the most serious reproducibility gap.
2. **Add a compute-matched best-of-\(N\) baseline.** Generate \(N\) low-temperature samples where the total token budget approximates that of power sampling, then select the sample with the highest base-model likelihood. This directly tests whether the MCMC procedure adds value beyond spending compute to find high-likelihood sequences.
3. **Ablate \(\alpha\), \(B\), and proposal temperature** on at least MATH500 to show sensitivity and guide practitioners.
4. **Resolve the Table 1 / Figure 5 discrepancy** — explain whether the 2.8pp gap is due to a different random seed, a subset difference, or a plotting error.
5. **Add error bars** (e.g., bootstrap 95% CIs over 5 seeds) to all point estimates, or at minimum state that results are from a single run and note the limitation.
6. **Move at least one additional pass@\(k\) curve** (e.g., HumanEval) to the main paper to strengthen the diversity claim.

## Score and Decision

### Calibration Summary

**Round 1 (Bracketing):** Queried three bands on topics similar to the paper. Weak band (avg < 3.5) returned papers on unrelated MCMC topics (FlashSampling, EBM training) with scores 2.50–3.25. Middle band (3.5–7.5) returned: DQfHkEcUqV (4.75, Reject — MCMC for extrapolative generation; flawed validation, weak baselines), Ouj6p4ca60 (5.50, Accept — GFlowNets for intractable inference), VNckp7JEHn (5.75, Accept — Inference Scaling Laws), and Ze4aPP0tIn (6.60, Accept — TSMC for math reasoning). Strong band (avg > 7.5) returned papers at 8.00–8.50 (SMC for controlled generation, min-p sampling).

**Round 1 bracket:** 4.5–6.5.

**Round 2 (Narrowing):** Queried within (4.5, 6.5) and (5.5, 7.5) on more focused topics. Retrieved DQfHkEcUqV (4.75, Reject), Ouj6p4ca60 (5.50, Accept), DzKdjWe59v (5.75, Reject — Hint Marginalization; rejected due to narrow evaluation and insufficient justification), alongside VNckp7JEHn (5.75, Accept) and Ze4aPP0tIn (6.60, Accept).

**Comparison to anchors:** The paper is clearly stronger than DQfHkEcUqV (4.75) — it has a cleaner theoretical contribution and more impressive results. It is comparable to Ouj6p4ca60 (5.50) and DzKdjWe59v (5.75) in overall quality, though its evaluation gaps (missing \(N_{\text{MCMC}}\), missing baselines, no ablations) are more concrete and arguably more serious. It is weaker than Ze4aPP0tIn (6.60), which has stronger empirical validation. The paper sits in the 5.0–6.0 range.

**Final score: 5.5**

The core idea is novel and the theoretical contribution is solid. The empirical results are striking and suggestive. However, the evaluation has significant gaps — most critically, the unreported \(N_{\text{MCMC}}\) hyperparameter and the absence of compute-matched inference-time baselines — that prevent the paper from fully supporting its central claims. The paper is borderline and would benefit substantially from addressing these issues in revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>