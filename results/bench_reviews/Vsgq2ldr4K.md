Now I have everything. Let me write the final review.

## Summary

This paper proposes "power sampling," a training-free, verifier-free inference-time method that uses MCMC (Metropolis-Hastings with a random-resampling proposal) to approximately sample from the power distribution \(p^\alpha\) of a base LLM. The authors show that this approach elicits single-shot reasoning capabilities that nearly match—and on out-of-domain tasks sometimes exceed—GRPO-based RL posttraining, while also preserving multi-sample diversity that RL collapses. Results are presented across three base model families (Qwen2.5-Math-7B, Qwen2.5-7B, Phi-3.5-mini-instruct) and four benchmarks (MATH500, HumanEval, GPQA, AlpacaEval 2.0).

## Strengths

- **Training-free method that achieves RL-comparable reasoning.** Power sampling matches GRPO on in-domain MATH500 (e.g., 74.8% vs 78.5% on Qwen2.5-Math-7B) and outperforms GRPO on out-of-domain HumanEval (57.3% vs 53.7%) and AlpacaEval 2.0 (2.88 vs 2.38) (Table 1). This directly supports the paper's central claim that base-model reasoning is underutilized by standard sampling.

- **Principled distinction between power sampling and low-temperature sampling.** Proposition 1 and Example 1 rigorously prove that the power distribution \(p^\alpha\) is not equivalent to low-temperature sampling, and illustrate that \(p^\alpha\) upweights tokens with few but high-likelihood future paths—a property the paper connects to avoiding "critical windows" in reasoning. This provides theoretical motivation beyond heuristic temperature tuning.

- **Preservation of multi-sample diversity.** Figure 5 shows that power sampling's pass@k reaches 0.98 at k=16 (matching the base model and far exceeding GRPO's 0.90), demonstrating that the method avoids the diversity collapse that is a known weakness of RL posttraining.

- **Generalizability beyond verifiable domains without external signals.** The method is verifier-free and training-free, yet improves AlpacaEval 2.0 scores (from 1.61 to 2.88 on Qwen2.5-Math-7B, outperforming GRPO's 2.38), demonstrating applicability to tasks where automated rewards are unavailable.

- **Consistent gains across multiple model families and tasks.** Results on Qwen2.5-Math-7B, Qwen2.5-7B, and Phi-3.5-mini-instruct across MATH500, HumanEval, GPQA, and AlpacaEval 2.0 show the method does not depend heavily on a particular base model.

## Weaknesses

### Fatal
None.

### Major

- **\(N_{\text{MCMC}}\) is not reported.** Algorithm 1 lists \(N_{\text{MCMC}}\) (number of MCMC steps per block) as a key hyperparameter, but its value is never stated in the experimental setup (Section 5.1). This is a critical omission: without it, the reader cannot assess whether the chain has had enough steps to mix, and the token-cost estimate in Eq. 12 is vacuous. The paper claims to find "a value for \(B\) that makes Algorithm 1 performant for relatively small values of \(N_{\text{MCMC}}\)," but never says what that value is. This directly impacts reproducibility.

### Minor

- **No verification that the chain samples the target distribution.** The paper provides no synthetic experiment (e.g., on a tiny vocabulary where \(p^\alpha\) can be computed exactly) to confirm that the MCMC chain actually converges to the intended power distribution. While the algorithm is theoretically well-motivated (random-scan Metropolis-Hastings), the lack of any diagnostic of sampling quality weakens the claim that the observed gains are due to sampling from \(p^\alpha\) rather than a heuristic resampling procedure.

- **Compute cost is not quantified.** The paper provides a token-count estimate (Eq. 12) but no wall-clock time, FLOPs, or compare cost against baselines. For a method that trades training compute for inference compute, this is needed to judge practical value. The estimate itself depends on the unreported \(N_{\text{MCMC}}\).

- **Temperature for Low-temperature baseline not explicitly stated.** Table 1 includes "Low-temperature" as a baseline but does not state the temperature used. The experimental setup gives the proposal temperature (1/\(\alpha = 0.25\) for reasoning, 0.5 for AlpacaEval) but it is unclear whether these same values were used for the baseline.

- **The Phi-3.5-mini-instruct HumanEval comparison amplifies the out-of-domain advantage.** GRPO trained on MATH catastrophically forgets coding ability for Phi-3.5-mini-instruct (HumanEval drops from 0.213 to 0.134). The paper transparently reports this, but the strong out-of-domain advantage partly reflects this degradation rather than pure sampling superiority. The Qwen models do not show this degradation. A brief discussion of this phenomenon would be helpful.

### Trivial
- The pass@k plot (Figure 5) would benefit from error bars or standard deviations to confirm the observed trends.
- The example in Table 2 is anecdotal.

## Nice-to-Haves

- **Ablation on \(N_{\text{MCMC}}\).** Showing how performance changes as \(N_{\text{MCMC}}\) varies from 1 to, say, 100 would clarify the role of MCMC versus simple resampling.
- **Synthetic verification experiment.** Running a small-vocabulary, short-length experiment where exact \(p^\alpha\) sampling is tractable and comparing the empirical distribution of MCMC samples to the true target would confirm correctness.
- **Comparison with a multi-task RL baseline.** Training GRPO on both MATH and code data would provide a stronger out-of-domain comparison.

## Removed Points

1. **"MH acceptance ratio is incorrectly specified"** (Harsh Critic, Critical Issue 1) — **REMOVED as factually wrong.** The critic claimed the reverse proposal probability \(q(x|x')\) is computed incorrectly because it "appears to assume the same \(m\) works in reverse." However, Algorithm 1 constructs \(x'\) by keeping the prefix \(x_{0:m-1}\) fixed (Step 6), so \(x'_{0:m-1} = x_{0:m-1}\). The reverse probability \(p_{\text{prop}}(x \mid x')\) then correctly computes \(p_{\text{prop}}(x_m\ldots \mid x_{0:m-1})\), and the uniform factor \(1/((k+1)B)\) cancels. This is a standard random-scan Metropolis-Hastings-within-Gibbs proposal and the acceptance ratio is correctly specified.

2. **"GRPO baseline comparison is fundamentally unfair"** (Harsh Critic, Critical Issue 2) — **WEAKENED and moved here.** The critic claims the comparison is "fundamentally unfair" because GRPO is trained only on MATH. However, for the Qwen2.5 models, GRPO improves on HumanEval (e.g., 0.329→0.537 on Qwen2.5-Math-7B), showing that the RL training transferred positively to coding. The Phi-3.5-mini case (0.213→0.134) does show catastrophic forgetting, but the data is transparently reported. The paper's claims about out-of-domain performance are qualified as such. This is a minor limitation for discussion, not a structural flaw.

3. **"Critical hyperparameters are missing" regarding temperature** (Harsh Critic, Critical Issue 3, part about temperature) — **Partially removed.** The critic claimed temperature is not reported. In fact, Section 5.1 states: "\(\alpha = 4.0\) coupled with a proposal LLM \(p_{\text{prop}}\) chosen as the base model with sampling temperature \(1/\alpha\)" and "For AlpacaEval 2.0... higher temperature (\(\tau = 0.5\))." The proposal temperature IS reported. However, the "Low-temperature" baseline temperature is not explicitly stated — this is preserved as a minor weakness above.

4. **"Missing appendix/proofs/references"** — Removed per instructions (parser strips these).

5. **Strength Finder strengths about "analysis linking likelihood/confidence distributions" and "concrete example demonstrating failure case"** — Retained as supporting but noted as minor evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report \(N_{\text{MCMC}}\)** — This is the single most important addition. Without it, the results are not reproducible and the cost estimate is uninterpretable.
2. **Report compute cost** (wall-clock time or FLOPs) and compare against single-pass low-temperature sampling and GRPO inference.
3. **Add a small-scale synthetic verification experiment** (tiny vocabulary, short sequences) showing that the MCMC chain empirically converges to \(p^\alpha\).
4. **Explicitly state the temperature used for the Low-temperature baseline** in Table 1.
5. **Briefly discuss the Phi-3.5-mini HumanEval degradation** in GRPO to contextualize the out-of-domain comparison.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/MFDkLbcydi.md` | 6.50 (Accept) | Stronger theoretical guarantees for test-time sampling; weaker empirical breadth. Current paper has broader empirical validation. |
| `/home/wg25r/review_agent/human_reviews_2026/3Gy5mmyuxn.md` | 6.50 (Accept) | Strong theoretical analysis of verifier imperfections; current paper has weaker theory but more practical appeal. |
| `/home/wg25r/review_agent/human_reviews_2026/BBDhQJh6GB.md` | 6.00 (Accept) | Theoretical framework for test-time verification; current paper is more applied but comparable in scope. |
| `/home/wg25r/review_agent/human_reviews_2026/flBRtdIihA.md` | 5.00 (Accept) | Has some inaccuracies but accepted as poster. Current paper is cleaner methodologically with stronger empirical results. |
| `/home/wg25r/review_agent/human_reviews_2026/8ta0xgtsJK.md` | 5.50 (Accept) | Verifier-free test-time scaling for diffusion models. Current paper is comparably positioned with broader empirical scope. |
| `/home/wg25r/review_agent/human_reviews_2026/ckAQ31T4Qv.md` | 4.00 (Reject) | MCMC for LLM test-time alignment; criticized for derivation errors. Current paper's MH implementation is correct. |
| `/home/wg25r/review_agent/human_reviews_2026/IE8N8MFNLi.md` | 3.50 (Reject) | MCMC for LLMs with limited experiments (jokes only). Current paper has far stronger empirical validation. |
| `/home/wg25r/review_agent/human_reviews_2026/7C5oMGnbV4.md` | 1.00 (Reject) | Not a serious submission; not comparable. |

The paper presents a novel, principled sampling method with strong empirical results (3 model families, 4 benchmarks, matching or exceeding RL). The core methodological concern (MH ratio correctness) is a misunderstanding — the algorithm is valid. The main weakness is the failure to report \(N_{\text{MCMC}}\), which damages reproducibility and makes the cost estimate meaningless, but is fixable. The paper falls short of the strongest tier (6.0+) due to this gap, but is clearly stronger than papers scoring 3.5–4.0 in this space.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>