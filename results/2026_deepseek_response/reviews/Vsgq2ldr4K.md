Now let me write the final consolidated review.

## Summary

This paper proposes a training-free inference-time sampling algorithm called "power sampling" that uses Metropolis-Hastings MCMC to sample from the power distribution p^α of a base LLM. The core insight is that if RL-posttraining merely "sharpens" the base model distribution, then directly sampling from p^α (which upweights high-likelihood regions) should achieve similar effects. The algorithm iteratively extends token sequences in progressive blocks, running MH steps with a random-resampling proposal at each stage. Experiments across three base models (Qwen2.5-Math-7B, Qwen2.5-7B, Phi-3.5-mini-instruct) and four benchmarks show the method matches or outperforms GRPO on several single-shot tasks while preserving diversity in multi-shot (pass@k) settings — all without any training or external verifiers.

## Strengths

- **Strong empirical results across multiple model families (Table 1).** Power sampling matches GRPO on in-domain MATH500 (within ~4 points on Qwen2.5-Math, within ~3 points on Qwen2.5-7B) and consistently *outperforms* GRPO on out-of-domain HumanEval (by +3.6% to +59.8%) and AlpacaEval 2.0 across all three tested models. These results directly support the claim that base models can deliver RL-level reasoning without training.

- **Pass@k analysis (Figure 5) convincingly shows diversity preservation.** Power sampling's pass@k curve rises from ~0.72 at k=1 to ~0.98 at k=16, strictly dominating GRPO (which plateaus at ~0.90) and matching the base model at high k. This quantifies a key advantage over RL-posttraining, which is known to collapse diversity.

- **Theoretical distinction between power distributions and low-temperature sampling (Proposition 1, Example 1) is novel and well-illustrated.** The insight that p^α upweights tokens with *few but high-likelihood future paths* (sum of exponents) while low-temperature sampling upweights tokens with *many but lower-likelihood future paths* (exponent of sums) is non-trivial, correctly proven, and directly motivates why the method should benefit reasoning tasks by avoiding "critical windows" / pivotal token failures.

- **Training-free, verifier-free, dataset-free nature is a meaningful practical advantage.** Unlike GRPO, which requires training data, reward signals, and careful hyperparameter tuning, the method works with only the base model at inference time. The strong AlpacaEval 2.0 results demonstrate applicability beyond verifiable domains.

## Weaknesses

### Fatal
None.

### Major

- **Algorithm 1 line 7 uses π_k in the acceptance ratio but the state and proposal are of length (k+1)B.** The pseudocode computes the MH ratio as π_k(x')/π_k(x), but π_k is defined only on sequences of length kB. The surrounding text clearly states the intent: "Suppose we have a sample from π_k. To obtain a sample from π_{k+1}..." — the target should be π_{k+1}. If the resampling index m > kB (resampling only the new B tokens), the ratio written as-is would collapse to 1, effectively ignoring the likelihood of the new tokens entirely. This is most likely a typo (the text is correct, the empirical results are meaningful), but it is a significant presentation error in the core algorithmic description that must be fixed.

- **N_MCMC (number of MH steps per block) is not reported.** The paper provides B=192, T=3072, α=4.0, and claims the method is performant "for relatively small values of N_MCMC," but never states what N_MCMC was used to produce any result in Table 1, Figure 4, or Figure 5. The expected token cost formula (Eq. 12) scales linearly with N_MCMC, so without this number readers cannot estimate computational cost, reproduce the results, or evaluate the central claim that the method is practical. (The paper's appendix section is stripped from the available file, so if N_MCMC appears there it should be moved to the main paper.)

### Minor

- **Inference cost vs. GRPO is not contextualized.** The paper correctly notes that GRPO requires expensive training, but does not quantify the inference cost of power sampling. For a practitioner choosing between methods, knowing that power sampling likely requires tens or hundreds of thousands of additional forward passes per problem (depending on N_MCMC) while GRPO inference costs a single forward pass is essential for practical decision-making. This does not invalidate the results but limits their interpretability.

- **Variance / statistical significance not reported.** Table 1 presents single point estimates without any measure of variability. Given the method's stochasticity (random seeds, MCMC randomness), reporting variance over multiple runs would strengthen the claims.

- **Handling of variable-length sequences (EOS) is not specified.** The paper sets T_max=3072 and notes "termination can happen earlier with an EOS token" but does not describe how the resampling proposal or acceptance ratio handles sequences of differing lengths. Since the proposal resamples from a random index to the end, the length can change across MH steps; the acceptance ratio must account for this, which is non-trivial.

### Trivial

- The low-temperature baseline temperature is not explicitly stated (can be inferred as τ=1/α=0.25). Should be stated directly.
- Algorithm 1 uses 1-based indexing (m ∈ {1, ..., (k+1)B}) while the paper elsewhere uses 0-based indexing — inconsistent.

## Nice-to-Haves

- Ablation study showing how performance and compute scale with N_MCMC and B.
- Best-of-N baseline from the base model to isolate the benefit of the MCMC procedure over simple rejection sampling.
- Wall-clock time or FLOPs comparison with GRPO inference.

## Removed Points

*These points were raised by one or both reviewers but are excluded from the main weaknesses for the following reasons:*

- **"Algorithm correctness: target distribution mismatch could invalidate entire empirical section"** (Harsh Critic point 1, second paragraph) — This framing is too strong. The text clearly states the correct target (π_{k+1}), and the empirical results demonstrate the method works. The bug is in the pseudocode, not the algorithm. Kept as Major but not Fatal.
- **"Connection to RL sharpening is purely suggestive"** (Harsh Critic, Section 4.1 note) — The paper does not claim to prove RL targets p^α; it uses sharpening as motivation. This is a legitimate scope choice.
- **"GRPO comparison incomplete without acknowledging training cost asymmetry"** (Harsh Critic point 3) — The paper explicitly notes it is training-free; the asymmetry is acknowledged. The remaining inference-cost gap is captured in the Minor weakness above.
- **"Missing related works"** — Cannot verify existence of external sources per policy.
- **Generic strengths from Strength Finder** ("addressing an important problem," "theoretical distinction is novel" without specifics) — Removed or folded into concrete strengths above.
- **"Reproducibility concern: code/data not provided"** — The paper references standard models and benchmarks; code availability is secondary for a NeurIPS/ICLR paper at submission stage.
- **"Statistical significance" framed as fatal omission** — Demoted to Minor; this is common and fixable.

## Novel Insights

The harsh critic's observation about the π_k/π_{k+1} ambiguity in Algorithm 1 is genuinely useful — it reveals that the paper's core algorithmic description has a concrete gap that needs fixing. Beyond this, no genuinely novel insight emerges from the reviews beyond the paper's own contributions.

## Suggestions

1. **Fix Algorithm 1 line 7** to use π_{k+1} (or equivalently p(x_{0:(k+1)B})^α) instead of π_k in the acceptance ratio. Also explicitly note in the text that the MH step targets the conditional distribution p(x_{kB+1:(k+1)B} | x_{0:kB})^α.
2. **Report N_MCMC** for all experiments. Add an ablation table showing how performance and cost (tokens generated, wall-clock time) vary with N_MCMC.
3. **Clarify EOS handling** — specify how the algorithm handles variable-length sequences in the resampling proposal and acceptance ratio.
4. **Add variance estimates** (e.g., over 3-5 seeds) to the main results table.
5. **State the low-temperature baseline temperature** explicitly in Section 5.1.
6. (Optional but recommended) Add a compute-performance Pareto plot comparing power sampling against GRPO (training + inference cost) and best-of-N baselines.

## Score and Decision

**Bracketing (Round 1):** Initial retrieval placed this paper between the weak band (<3.5, papers like "Planning with MCTS" at 3.0, rejected) and the strong band (>7.5, papers like "Syntactic/Semantic Control via SMC" at 8.0, accepted). Middle-band anchors included "Inference Scaling Laws" (5.75, accepted), "Step-by-Step Reasoning via TSMC" (6.60, accepted), and "Learning Extrapolative Sequence Transformations" (4.75, rejected).

**Narrowing (Round 2):** Focused retrieval inside (4.5, 7.5) returned "Large Language Monkeys" (5.0, rejected) and "Learning Extrapolative..." (4.75, rejected) as lower anchors, and "Amortizing Intractable Inference" (5.5, accepted) and "Inference Scaling Laws" (5.75, accepted) as upper-lower anchors. Reading these in full:

- *Large Language Monkeys* (5.0, rejected): Studied scaling inference compute with repeated sampling. Some reviewers found the core finding trivial/expected. The current paper has a stronger technical contribution (novel algorithm, theoretical grounding) and more surprising results.
- *Inference Scaling Laws* (5.75, accepted): Empirical study of compute-optimal inference with a novel tree search method. Solid but limited to math tasks. The current paper has broader evaluation (math, code, general QA), a more novel technical approach, and addresses a more fundamental question (can training-free sampling match RL?). Slightly stronger.
- *Step-by-Step Reasoning via TSMC* (6.60, accepted): MCMC method for math reasoning verification, strong theoretical framework, somewhat limited evaluation (2 math benchmarks). The current paper has comparable technical depth, broader evaluation (4 benchmarks, 3 model families), and more surprising headline results (matching GRPO), but has more presentation gaps (pseudocode, missing N_MCMC).

The current paper is clearly above the reject-level anchors (4.75-5.0) and sits between the 5.75 and 6.60 accepted papers. Given the two Major issues (pseudocode bug, unreported N_MCMC) which are fixable, the paper is at the lower end of this range.

**Final score: 6.0. Decision: Accept.** The paper's core contribution — that sampling from p^α via MCMC can match RL-posttraining without training — is conceptually novel, well-motivated, and supported by substantial empirical evidence. The weaknesses are real but addressable; they do not undermine the main findings.

**Anchor papers consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| sdpVfWOUQA.md (Planning with MCTS) | 3.00 | R1 | Weaker in all respects — less novel, narrower evaluation |
| 8LZ1D1yqeg.md (Task Calibration) | 7.00* | R1 | Different topic (calibration), not directly comparable |
| pTyEnkuSQ0.md (Intrinsic Self-Correction) | 5.25* | R1 | Different topic, mixed reviews |
| t15cWqydys.md (Inferring from Logits) | 3.00 | R1 | Much weaker — narrow evaluation, limited contribution |
| DQfHkEcUqV.md (Extrapolative Sequence Transforms) | 4.75 | R1/R2 | Weaker — flawed validation methodology, unclear contributions |
| VNckp7JEHn.md (Inference Scaling Laws) | 5.75 | R1/R2 | Comparable contribution, slightly weaker novelty, accepted |
| Ze4aPP0tIn.md (TSMC for Math) | 6.60 | R1 | Stronger presentation, narrower evaluation; comparable core contribution |
| lDbjooxLkD.md (Emergent Abilities) | 6.00 | R1 | Different topic, not directly comparable |
| xoXn62FzD0.md (Syntactic Control via SMC) | 8.00 | R1 | Stronger — polished presentation, extensive evaluation, more domains |
| Ouj6p4ca60.md (Amortizing Intractable Inference) | 5.50 | R2 | Different approach (GFlowNet fine-tuning vs. training-free), accepted |
| HHKboqbkec.md (Multimodal Theory-of-Mind) | 5.75 | R2 | Different topic, rejected |
| 0xUEBQV54B.md (Large Language Monkeys) | 5.00 | R2 | Weaker — some reviewers found analysis trivial, rejected |
| gU4ZgQNsOC.md (Dynamic Loss Reweighting) | 6.00 | R2 | Different topic (pretraining), not directly comparable |
| sL2F9YCMXf.md (Energy-Based Diffusion LM) | 6.75 | R2 | Different topic (diffusion), accepted |

*Note: Scores marked with * are from different-topic papers used only for wide bracketing, not direct comparison.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>