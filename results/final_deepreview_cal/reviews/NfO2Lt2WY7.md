## Summary

This paper systematically decomposes the GRPO (Group Relative Policy Optimization) loss function for post-training LLMs on mathematical reasoning. Through controlled ablations, the authors find that (1) negative feedback (not masking out negative-advantage actions) is important for stable training, (2) group-relative advantage estimation is crucial, and (3) PPO-style policy ratio clipping is unnecessary. From these observations they propose RGR (REINFORCE with Group Relative Advantage), which retains group-relative advantage and KL regularization while discarding clipping. Experiments on 0.5B–1.5B models trained on 1800 GSM8K problems evaluate RGR against GRPO, positive-only GRPO, REINFORCE, RAFT, and supervised fine-tuning across nine math and STEM benchmarks.

## Strengths

- **Clean, well-motivated ablation design.** The paper systematically isolates three components of GRPO (negative feedback, advantage estimation, and clipping) in a principled way. The positive-only GRPO variant and the direct-reward REINFORCE baseline cleanly demonstrate what happens when each component is removed, and the experiments are interpretable throughout.

- **Convincing demonstration that clipping is unnecessary.** Across all three models and nine benchmarks, RGR (which removes clipping) trains stably and never substantially underperforms GRPO. The training curves (Figure 1) show near-identical dynamics between GRPO and RGR, and aggregate performance across Tables 1–3 is comparable or slightly favors RGR. This is a practically useful simplification.

- **Multi-lingual, multi-domain evaluation.** The paper evaluates on English math (5 benchmarks), Chinese math (2 benchmarks), and STEM (2 benchmarks) across three model families (Qwen2.5 0.5B, Qwen2.5 1.5B, Llama3.2 1B). This breadth strengthens the generality of the findings beyond a single benchmark or language.

- **Clear and well-organized exposition.** The background section provides accessible derivations of PPO, GRPO, and the proposed RGR. The experimental design is transparent about training data, models, and reward structure. Code is provided.

## Weaknesses

### Major

- **No statistical validation or variance reporting.** All benchmark tables (Tables 1–3) report single-number accuracies without error bars, confidence intervals, or multi-seed averages. The key comparative claim — that RGR "surpasses GRPO" (Section 5) — rests on margins that are often 1–2 percentage points (e.g., GSM8K: RGR 72.7 vs. GRPO 71.0 on Qwen2.5-1.5B; MATH: 46.7 vs. 44.2). With 0.5B–1.5B models trained on only 1800 examples, run-to-run stochastic variation could easily account for differences of this magnitude. Without variance estimates, the reader cannot assess whether RGR genuinely outperforms GRPO or merely performs comparably. This undermines the paper's strongest empirical claim. The training curves (Figure 1), while informative about stability, do not substitute for statistical rigor on the benchmark evaluations.

- **The "negative feedback is indispensable" conclusion is overstated relative to the evidence.** The paper's conclusion states that "negative feedback is indispensable: methods that ignore it… exhibit instability, collapse, and consistently degraded performance" (Section 5). However, the data tells a more nuanced story. On the Qwen2.5-1.5B model, GRPO-pos (positive-only) achieves 35.7 avg on Math-English vs. GRPO's 37.3 — a small gap. On Llama3.2-1B, GRPO-pos scores 19.8 vs. GRPO's 20.1 — negligible. The paper does acknowledge in Section 4 that "the 1.5B and 1B models… avoid immediate collapse," but the concluding language erases this nuance. The evidence supports a finding that negative feedback is important for smaller models and beneficial at larger scales, not that it is universally indispensable. This overclaim weakens an otherwise well-supported point.

### Minor

- **Hyperparameter handling across methods is unspecified in the main text.** The paper references Appendix A for hyperparameters (which is stripped in the provided PDF) but does not state whether learning rates, KL coefficients, and other settings were tuned independently per method or held constant. Since RGR and GRPO have different gradient structures, using identical hyperparameters could disadvantage GRPO or favor RGR. Clarifying the tuning procedure would strengthen confidence in the fairness of the comparison.

- **Limited training data and model scale.** Training is performed on only 1800 examples from a single dataset (GSM8K). While the evaluation spans nine benchmarks, the narrow training distribution may exaggerate sensitivity to loss components. The paper acknowledges hardware constraints and suggests larger-model experiments as future work, but the findings may not extrapolate to the data scales and model sizes typical of production GRPO usage (e.g., DeepSeek-R1 scale).

- **"Efficient" claim is unsupported.** The abstract and introduction describe RGR as a "more transparent and efficient alternative to GRPO," but no wall-clock time, memory, or throughput measurements are reported. Since RGR removes the policy ratio computation, there is likely a modest computational saving, but the paper should either provide measurements or replace "efficient" with "simpler."

- **Qualitative reasoning analysis is anecdotal.** The "emergence of reasoning behaviors" (Figure 2) is based on a single example from the Countdown dataset. While illustrative, one example does not constitute systematic evidence that "robust training regimes… foster the development of interpretable reasoning strategies." This claim should be tempered or supported with quantitative analysis of reasoning traces.

- **RAFT training-curve reporting is unusual.** Figure 1 tracks "average reward" for RAFT, which is an offline SFT method that selects top-ranked responses and trains with cross-entropy. How RAFT's "average reward" is computed during training is not explained, and presenting a reward drop as evidence of instability conflates the training objective (cross-entropy) with an evaluation metric (reward of generated outputs). This needs clarification.

### Trivial

- The paper uses inconsistent naming: "RGR" in abstract and introduction, "RGR A" and "RGRA" in experiments and figures. Settling on one name would improve clarity.

## Nice-to-Haves

- **Include an ablation removing KL from RGR.** Since RGR retains the KL penalty, it is unclear whether stability derives from group advantage alone or from continued KL regularization. An experiment removing KL from RGR (or adding KL to plain REINFORCE) would sharpen the contribution.
- **Report a small sensitivity analysis** varying the learning rate or KL coefficient to demonstrate that the RGR advantage is not brittle to hyperparameter choice.
- **Discuss scale dependence of the negative-feedback finding** more explicitly, hypothesizing why larger models tolerate positive-only training better.

## Removed Points

These points from the Harsh Critic were considered but removed or downgraded:

- **"RAF training curve collection confuses the narrative about stability"** — Kept as a minor point but the harsh critic's suggestion that this is a critical flaw was downgraded; it is a presentation clarity issue, not a threat to the core claims.
- **"The paper does not state whether hyperparameters were tuned independently"** — Kept as minor rather than major because the paper references Appendix A; the stripped PDF prevents verification, making this a documentation gap, not a demonstrated unfairness.
- **"Could the metric be measuring a proxy?" / "Are confounders controlled?"** — The harsh critic raised these as generic area-of-concern sweeps. No specific confounder was identified in the paper, so these are removed.
- **"Absence of Appendix A"** — The parser strips appendices; this is not an author error. Removed.
- **"The ablation should also consider a simple value-function baseline"** — This is scope creep; the paper studies group-relative methods and already includes a direct-reward REINFORCE baseline. Removed.

## Novel Insights

The paper's most interesting and underemphasized finding is the *scale-dependent* nature of negative feedback necessity. The 0.5B model collapses under positive-only training while the 1B and 1.5B models largely tolerate it. This suggests that smaller models may rely more heavily on negative signals to avoid representation collapse or reward hacking, while larger models' stronger initial policies provide enough signal from positive examples alone. This scale dependence is noted in the results but dismissed in the conclusions, and it deserves more attention as a genuinely novel observation about how RL training dynamics interact with model capacity.

## Suggestions

- Run each configuration with at least 3 seeds and report mean ± standard deviation for the main benchmark tables. This alone would substantially strengthen the comparative claims.
- Replace "negative feedback is indispensable" with a more precise claim, e.g., "negative feedback is critical for stable training in smaller models and beneficial at larger scales."
- Either measure and report computational efficiency (wall-clock time, memory) or replace "efficient" with "simpler" throughout.
- Clarify how RAFT's training reward is computed in Figure 1, or consider removing RAFT from the training-curve plots and presenting it only in the benchmark tables.

## Score and Decision

**Round-1 bracket:** After comparing against weak-band anchors (avg scores 2.50–3.00) and strong-band anchors (avg score 8.00, e.g., WizardMath), this paper plausibly sits in the 5.0–7.0 range.

**Round-2 narrowing:** Anchors inside the bracket:
- F0GNv13ojF (5.17, Reject): "On Designing Effective RL Reward at Training Time for LLM Reasoning" — similar RL-for-reasoning domain but less systematic ablation, weaker baselines. Our paper is clearly stronger.
- ZRDa2IT1sQ (6.00, Reject): "Step-Controlled DPO" — proposes a new DPO variant with stepwise error supervision; both papers share systematic design but SCDPO has stronger statistical presentation. Our paper is similar in quality.
- RFqeoVfLHa (6.50, Accept): "Progress or Regress? Self-Improvement Reversal in Post-training" — thorough evaluation framework, important phenomenon. Our paper is somewhat weaker due to less rigorous evaluation.
- s5N7p5UjgR (6.75, Reject): "Markovian Transformers" — novel architecture, strong gains on GSM8K, but limited evaluation scope. Our paper has broader evaluation but less novelty.

The paper is better than the 5.17 anchor but does not reach the 6.50 anchor's level of evaluation rigor. It sits closest to the 6.00 anchor ZRDa2ITs1Q. The lack of statistical validation and the overstated negative-feedback claim pull it slightly below 6.0. Score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>