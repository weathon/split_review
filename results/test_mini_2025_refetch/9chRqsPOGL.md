Now I have sufficient calibration. Let me compose the final consolidated review.

**Bracket analysis:**
- Round 1 wide bracketing: weak anchors (avg 2.5-3.4), middle anchors (avg 4.0-6.5), strong anchors (avg 7.75-8.0). The paper clearly falls in or near the strong band.
- Round 2 narrowing: TPO (6.33) uses tree-structured preference data but has concerns about data noise and limited model diversity — SPAR is clearly stronger. WSPO (7.25, spotlight) is limited to Qwen models — SPAR has more comprehensive evaluation across 4 model families. Chain of Hindsight (7.0) only tests on GPT-J — SPAR tests on 8B-70B. SPAR is stronger than all these. It is comparable to Instruction Backtranslation (8.0, oral) and SCoRe (8.0, oral) in quality, though its causal story is slightly less isolated.
- Final score: **7.5**

---

## Summary

This paper introduces SPAR, a self-play framework that uses tree-search refinement to construct preference pairs for improving instruction-following in LLMs. The core insight is that independently sampled responses introduce irrelevant content variations (e.g., different storylines) that interfere with learning critical instruction-following constraints. SPAR iteratively trains an actor (via DPO on refined pairs) and a refiner (via RFT on judgment and refinement data), bootstrapped from a strong teacher. Experiments on LLaMA3-8B/70B, GLM-4-9B, and Mistral-7B show that SPAR-8B surpasses GPT-4-Turbo on IFEval after three iterations, and the method scales effectively to 70B. Ablations confirm the importance of tree-search refinement, iterative training, and the refinement pairs themselves.

## Strengths

1. **Clear motivation and well-designed method.** The problem of "interfering factors" in independently sampled preference pairs is concretely illustrated (Figure 1, the story-ending example) and the solution — using tree-search refinement to construct pairs that minimize irrelevant variation — is technically sound and directly addresses the identified problem.

2. **State-of-the-art results with thorough evaluation.** SPAR-8B-DPO-iter3 achieves 81.8% average accuracy on IFEval, surpassing GPT-4-Turbo (81.3%), and consistently outperforms strong baselines (Self-Rewarding, Meta-Rewarding, SELF) across all iterations (Figure 3, Table 1). The evaluation covers four backbone models (LLaMA3-8B, LLaMA3-70B, GLM-4-9B, Mistral-7B), two instruction-following benchmarks (IFEval, FollowBench), a judgment benchmark (LLMBar), and general capability benchmarks (GSM8k, MMLU, HumanEval, TriviaQA in appendix), ensuring no degradation.

3. **Tree-search refinement is empirically essential.** Ablations (Table 4) show removing tree search drops IFEval prompt-level strict accuracy by 2.0 points for the actor, and 4.3 points in adversarial judgment accuracy for the refiner (Table 5). This confirms the component's importance beyond being merely additive.

4. **Causal evidence from synthetic experiments.** Figure 4 provides controlled experiments showing that "interfering pairs" (where surface features like letter case vary) cause the model to learn spurious correlations, while refinement pairs yield higher task accuracy. This directly supports the paper's motivating hypothesis in simplified settings.

5. **Code and data release.** The paper commits to releasing code and data, supporting reproducibility and future research.

## Weaknesses

### Fatal
None.

### Major

1. **The "interfering factor" mechanism is not fully isolated from alternative explanations.** The paper's central thesis is that *minimizing irrelevant variation in preference pairs* drives improvement. However, refined pairs also (a) are more likely to contain a correct response, (b) involve a stronger reward signal (verified by the refiner), and (c) benefit from the tree search discovering solutions the actor would not generate independently. The synthetic experiment (Figure 4) isolates this mechanism but uses very simple tasks (letter case, story framing) that may not generalize to complex multi-constraint instructions. The "w/o refinement" ablation conflates loss of tree search, data quantity, and pair quality. The paper's explanation is plausible and well-motivated, but the causal role of "interfering factors" specifically remains somewhat indirect. This does not undermine the method's practical value — the method works — but it means the theoretical contribution is slightly less sharp than claimed.

2. **Reliance on a strong teacher for initialization.** SPAR bootstraps both the actor and refiner using data (prompts, responses, judgments) from GPT-4o-Mini (a strong LLM). While the refiner eventually matches or exceeds this teacher (Table 2), the initial dependency means the framework is not fully autonomous from the start. The paper acknowledges this but does not quantify how much of the final performance is attributable to the high-quality seed data vs. the subsequent self-play dynamics. An ablation starting from a weaker initial model or less seed data would clarify the method's robustness and autonomy.

### Minor

1. **Self-evaluation bias in the refiner.** Table 3 shows SPAR-8B-RFT-iter3's self-evaluated refinement accuracy (Acc-SPAR = 90.5) is substantially higher than GPT-4o's evaluation (Acc-GPT = 79.0). The paper notes this as "a potential issue of self-evaluation bias" but does not provide calibration against human judgments or discuss the gap's implications. Since the refiner's judgments are used throughout the self-play loop, understanding this bias would strengthen trust in the iterative improvement signal.

2. **Computational cost of tree-search refinement is not discussed.** The paper does not report how many tree nodes are evaluated per prompt, how many LLM calls are needed per iteration, or the overall training-time cost. This is a practical concern for reproducibility, scaling, and comparison with alternative methods.

3. **Potential data overlap between training prompts and evaluation benchmarks.** The prompt dataset is built from Infinity-Instruct seed prompts via taxonomy-based construction. Since IFEval and FollowBench are public benchmarks, a brief verification that training prompts do not overlap with evaluation sets would be reassuring.

4. **String-level similarity analysis is suggestive but not deeply explored.** The paper reports that refinement pairs have 0.90 string-level similarity vs. 0.85 for independent pairs, but does not analyze whether this similarity gap correlates with downstream performance across tasks or iterations.

### Trivial
None beyond the parser artifacts that should be ignored.

## Nice-to-Haves

- A more direct measure of "interfering factor removal" — e.g., computing cosine similarity or edit distance between responses in each preference pair and showing that after controlling for pair correctness, DPO performance correlates negatively with irrelevant variation.
- A baseline that uses refinement but does not explicitly minimize irrelevant variation (e.g., full-rewrite refinement rather than minimal-edit refinement) to strengthen the interference-removal argument.

## Removed Points

- **"The refiner evaluates its own refinements much more favorably than GPT-4o does"** — The paper already acknowledges this ("it also points to a potential issue of self-evaluation bias"). This is retained as a minor weakness (self-evaluation bias) but with the caveat that the paper partially addresses it.
- **Strength Finder's generic strengths about "important problem" and "timely topic"** — Removed as generic/superficial. Only strengths with concrete evidence and specific citations are retained.
- **No weaknesses about formatting, typos, or appendix content** were raised by reviewers, so no removals needed in those categories.
- The Strength Finder claimed SPAR-8B-SFT "outperforms the original LLaMA3-8B-Instruct" as a positive — but the paper actually says SPAR-8B-SFT *underperforms* on some metrics (Table 1 shows SPAR-8B-SFT at 78.0 vs 77.9 for the original — this is essentially tied, and the paper notes "suggests that incorporating the judgment SFT or refinement SFT data would reduce performance, likely due to the huge task gap"). This is a slight misreading; the strength is better stated as "the SFT initialization is competitive." Not included.

## Novel Insights

None beyond the paper's own contributions. The reviewers affirm the paper's claims and identify nuances in the evidence rather than uncovering phenomena the authors missed.

## Suggestions

1. **Strengthen the causal story.** Run an experiment that controls for response correctness while varying only the amount of irrelevant variation (e.g., by computing similarity scores between chosen/rejected responses and showing that DPO gain correlates negatively with variation after controlling for pair quality). This would directly connect the theoretical motivation to the empirical results.

2. **Quantify teacher dependence.** Run SPAR starting from a weaker teacher or less seed data (e.g., 1k instead of 8k responses) and show that the iterative improvement still holds. This would demonstrate the method's autonomy more convincingly.

3. **Report tree-search costs.** Provide the number of tree nodes evaluated per prompt, total LLM calls per iteration, and wall-clock training time. This addresses a practical concern for adoption and reproducibility.

4. **Add human calibration for refiner judgments.** Report inter-annotator agreement between the refiner and human raters on a subset of the refinement test set to calibrate the self-evaluation bias observed in Table 3.

## Score and Decision

**Calibration anchors used (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| aYYZBPoSHb.md (Multi-Objective ORPO) | 3.40 | R1 weak | Much weaker — limited evaluation, no tree-search |
| NtAXAvIYuN.md (iREPO) | 3.40 | R1 weak | Much weaker — limited scope |
| 28TLorTMnP.md (Soft Alignment) | 2.50 | R1 weak | Much weaker |
| CSpWgKo0ID.md (Playing repeated games) | 3.40 | R1 weak | Different topic, much weaker |
| tCfvktlrHI.md (Self-Play Non-Zero-Sum) | 4.75 | R1 mid | Different setting, weaker evaluation |
| RFqeoVfLHa.md (Self-Improvement Reversal) | 6.50 | R1 mid | Analysis paper, good but different genre |
| uIGnuyDSB9.md (SeRA) | 6.00 | R1 mid | Weaker — only applies implicit reward margins, less thorough |
| kQqZVayz07.md (Aligning Agents) | 4.00 | R1 mid | Different domain, weaker |
| 1oijHJBRsT.md (Instruction Backtranslation) | 8.00 | R1 strong | Comparable — both strong instruction-following papers |
| CjwERcAU7w.md (SCoRe) | 8.00 | R1 strong | Comparable — different task (self-correction), similar quality |
| rfdblE10qm.md (Rethinking Reward Modeling) | 8.00 | R1 strong | Different topic (theory of reward models) |
| or8mMhmyRV.md (MaestroMotif) | 7.75 | R1 strong | Different domain (game skills via LLM feedback) |
| O0sQ9CPzai.md (TPO) | 6.33 | R2 narrow | Weaker — limited model diversity, data noise concerns |
| I4YAIwrsXa.md (DeepSeek-Prover) | 6.25 | R2 narrow | Different domain (theorem proving), weaker |
| 2BfZMh9td4.md (MODPO) | 6.50 | R2 narrow | Different focus (multi-objective), weaker evaluation |
| SIE6VFps9x.md (ACT) | 6.25 | R2 narrow | Different setting (multi-turn clarification) |
| f7KxfUrRSb.md (WSPO) | 7.25 | R2 narrow | Slightly weaker — limited to Qwen models vs SPAR's 4 model families |
| 6xfe4IVcOu.md (Chain of Hindsight) | 7.00 | R2 narrow | Weaker — only tested on GPT-J (6B), limited scope |

**Bracket:** Round 1 identified the paper belongs in the strong band (7.5+). Round 2 narrowed: SPAR is clearly stronger than TPO (6.33), CoH (7.0), and WSPO (7.25), comparable to Instruction Backtranslation (8.0) and SCoRe (8.0), but has slightly less clean causal isolation of its mechanism. Final score: **7.5**.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>