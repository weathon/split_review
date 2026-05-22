Here is my consolidated final review.

---

## Summary

This paper systematically ablates the GRPO loss function, testing whether PPO-style clipping, group-relative advantage estimation, and negative feedback signals are each necessary for post-training LLMs on math reasoning. The authors propose RGR (REINFORCE with Group Relative Advantage), a simplified variant that removes clipping and policy ratios while retaining group-relative advantage estimation and KL regularization. Experiments on three small models (0.5B–1.5B) trained on GSM8K and evaluated across nine math/STEM benchmarks show that (1) negative feedback is essential for stable training, (2) advantage estimation is indispensable, and (3) PPO-style clipping can be removed without harming stability or benchmark performance.

## Strengths

- **Clean ablation design isolating component necessity.** The paper tests positive-only advantages, REINFORCE with raw rewards, and the simplified RGR variant against full GRPO. The training dynamics in Figure 1 are the strongest evidence: they clearly show that positive-only GRPO and RAFT collapse (reward and response length drop to near zero for the 0.5B model by step 20), while methods using negative feedback and advantage estimation (GRPO and RGR) maintain stable learning. This directly supports the claim that negative feedback is essential and that clipping is not needed for stable optimization.

- **PPO-style clipping removal does not harm stability.** Figure 1 shows nearly identical reward and response-length trajectories for GRPO and RGR across all three model scales (e.g., reward ~0.9 for Qwen 1.5B, response length ~150). This is a clean, visually convincing result that supports the paper's core thesis that GRPO's complexity can be reduced.

- **Multi-benchmark evaluation across languages and domains.** The paper evaluates on five English math benchmarks (GSM8K, MATH, Gaokao2023-Math-En, OlympiadBench, AMC23), two Chinese math benchmarks (CMATH, CN-Middle-School), and two STEM benchmarks (MMLU-STEM, Gaokao2024). RGR achieves the highest average on the Math-English benchmarks for all three models and shows strong results on Chinese math and STEM benchmarks, suggesting the simplified approach generalizes beyond the training distribution.

- **Well-motivated and clearly written.** The paper situates itself clearly within the recent GRPO-variant literature and positions its contribution as a systematic simplification rather than yet another modification.

## Weaknesses

### Major

- **No statistical uncertainty quantification for central performance claim.** All benchmark results are single-run point estimates. The paper claims RGR "surpasses GRPO on 17 over 27 tasks" (conclusion) and "outperforms GRPO in most settings" (Section 4), but the reported differences are often within a few percentage points (e.g., GRPO 71.0 vs. RGR 72.7 on Qwen2.5-1.5B GSM8K; GRPO 44.2 vs. RGR 46.7 on MATH). Without multiple seeds, standard deviations, or confidence intervals, these differences cannot be distinguished from noise. Given the known variance of RL-based LLM training, this is an evidential gap that undermines the stated performance comparison. The training dynamics evidence (Figure 1) supports the stability claims well, but the benchmark superiority claim requires statistical support.

- **Narrow experimental scope relative to the paper's broad framing.** The title asks whether complicated loss functions are necessary for "teaching LLMs to reason," but experiments use only small models (0.5B–1.5B), train on a single dataset (GSM8K, 1,800 instances), and evaluate exclusively on mathematical/STEM reasoning. Whether the findings generalize to larger models (7B+), other reasoning domains (logical reasoning, code generation, multi-hop QA), or non-math training data is unknown. The paper acknowledges this limitation in one sentence in the future-work section, but the abstract and introduction frame the conclusions far more broadly.

- **Performance claim is overstated relative to the evidence.** The conclusion states that RGR "surpasses GRPO on 17 over 27 tasks," which invites a level of scrutiny that single-run results cannot withstand. The paper's actual strength is showing that RGR performs *comparably* to GRPO while being simpler. The language throughout (abstract: "has the potential to achieve stronger performance"; conclusion: "surpasses") should be moderated to match the evidential basis.

### Minor

- **REINFORCE baseline under-specified.** The "REINFORCE with Direct Rewards" variant is described as starting from RGR A and removing group-relative advantage estimation. It is not stated whether this variant still samples 8 completions per prompt (and if so, how the gradient is aggregated across them) or uses a single rollout. The tables label it simply "REINFORCE," conflating it with Williams (1992)'s standard algorithm, but it may be a non-standard group-sampled variant. This ambiguity weakens the ablation's interpretability.

- **Naming inconsistency.** Section 3.2 introduces the method as "RGR A," Table 1 uses "RGR," the conclusion uses "RGRA," and Figure 1 uses "RGRa." While the referent is clear, this inconsistency is noticeable.

- **No ablation of the KL regularization coefficient β.** Given that the paper's framing is about identifying which GRPO components are necessary, omitting an ablation of the KL penalty coefficient is a gap. The paper shows clipping is unnecessary but never tests whether the KL regularization strength could also be simplified.

- **Training stop point unexplained.** Figure 1 shows a vertical dashed line at step 65 labeled "Stop" in a paper that states 70 steps of training. The reason for early stopping is not explained, and it is unclear whether training had converged.

- **Countdown dataset appears without description.** Section 4 introduces results "On the Countdown dataset" but this dataset is not listed in the benchmarks described in Section 3.1. The reader cannot assess what task this is or whether it is an appropriate evaluation.

- **Qualitative reasoning analysis is anecdotal.** Figure 2 shows a single example of an RGR/GRPO model producing reasoning traces vs. a positive-only model producing a direct answer. This is presented as evidence that these models "exhibit emergent reasoning" but no systematic analysis (e.g., proportion of responses with reasoning traces, average chain length) is provided.

- **LoRA rank (r=128, ~10% parameters) is not discussed as a potential confound.** Since LoRA constrains the effective parameter update per step, it could reduce the relevance of PPO-style clipping. The paper does not consider whether the finding that "clipping is unnecessary" might interact with the use of low-rank adapters.

### Trivial

None.

## Nice-to-Haves

- Add multiple random seeds (at least 3) and report mean ± std for all benchmark scores.
- Provide a direct measure of simplicity (training wall-clock time per step, memory usage, or number of hyperparameters).
- Quantify the emergence of reasoning behaviors systematically (proportion of responses containing explicit reasoning traces before and after training).
- Include a proper single-rollout REINFORCE baseline for completeness.

## Removed Points

These points were considered but removed per filtering rules (see below for rationale):

- **Criticism that Countdown dataset is "never described":** The appendix (stripped by parser) likely contains details. However, Countdown is indeed not listed in the Section 3.1 benchmark table, which is a genuine presentation gap kept as a minor weakness above.
- **Criticism about "no discussion of training budget or convergence":** The 70-step/65-step discrepancy is real but minor; kept above as minor weakness.
- **Criticism about "paper claims GRPO is complex but never defines complexity":** The concept of complexity is clear enough from context (additional components in the loss function), and defining it formally is not essential to the paper's contribution.
- **Criticism that positive-only variant notation is "confusing":** The description is reasonably clear given the equations.
- **Strength that "RGR outperforms GRPO on most benchmarks":** This conflicts with the verified weakness about lack of statistical support; the weakness wins. The strength is re-framed in the review under "comparable or slightly better" language.
- **Strength about "qualitative evidence of emergent reasoning":** The single-example evidence is too thin to constitute a meaningful strength; kept as a weakness (anecdotal) instead.
- **Criticism about "missing error bars" framed as fatal:** The training dynamics (Figure 1) strongly support the stability claims even without error bars; the performance comparison claim is where the lack of error bars is damaging, not the ablation claims.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Moderate all claims about RGR "surpassing" or "outperforming" GRPO.** Replace with language like "RGR achieves comparable or slightly higher average scores while being substantially simpler" throughout the abstract, conclusion, and Section 4. The paper's strongest contribution is the ablation finding that clipping is unnecessary — let that take center stage.
- **Add a variance analysis.** Even a small-scale multiple-seed comparison (e.g., 3 seeds for the primary condition pairs) would transform the paper's credibility on the performance comparison claim.
- **Acknowledge the LoRA confound explicitly.** Discuss whether the use of low-rank adapters (10% parameter updates) could reduce the effective policy ratio change and thus make clipping less relevant.
- **Describe the REINFORCE baseline implementation precisely.** State whether it uses group sampling and how gradients are aggregated.
- **Fix the method naming inconsistency** (RGR A / RGR / RGRA / RGRa) throughout the paper.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:**
- Weak anchors (<3.5): ZK1NnjpjEs (3.00, PPO for NLU), 28TLorTMnP (2.50, listwise rewards), jOuHjFw71C (3.00, planning evaluation), FaOeBrlPst (3.00, explainable rewards). These papers have clear fatal flaws or narrow scope; this paper is substantially stronger.
- Middle anchors (3.5–7.5): F0GNv13ojF (5.17, RL reward design), gdzpnRBP4F (4.50, RLSF), ZRDa2IT1sQ (6.00, Step-Controlled DPO), O0sQ9CPzai (6.33, TPO). The paper under review sits within this band.
- Strong anchors (>7.5): rfdblE10qm (8.00, reward modeling theory), mMPMHWOdOy (8.00, WizardMath). These papers have larger-scale experiments and/or theoretical contributions; this paper is weaker.

**Round 2 — Narrowing (bracket 4.5–6.0):**
- F0GNv13ojF (5.17, RL reward design): Similar in scope (math reasoning RL, small models). The anchor paper has mixed reviews on novelty and generality; this paper has a cleaner conceptual contribution (systematic ablation vs. reward clipping tricks) but similar empirical limitations. Comparable or slightly better.
- cijO0f8u35 (5.25, scaling relationships): Limited to GSM8K only. This paper uses more benchmarks (9 vs. 1) but the anchor had larger model scale. Comparable quality.
- OD9pwKQzXl (5.25, VerifierQ): Similar model scales and datasets, similar writing issues. The paper under review has a stronger conceptual contribution. Comparable.
- ZRDa2IT1sQ (6.00, SCDPO): Larger models (20B), more thorough evaluation, cleaner experiments. This paper is weaker than SCDPO.

**Final score determination:** The paper falls between the 5.17–5.25 anchors and the 6.00 anchor — closer to the lower end. The ablation methodology is a genuine strength, but the lack of error bars on the central performance claim, narrow scope (small models, one training dataset), and overclaiming prevent it from reaching the 6.0 level. Score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>