Now I have a clear picture. Let me compose the final review.

**Round 1 Bracket**: Based on comparison with PDA (4.75), FormalAlign (6.50), and RAutoformalizer/BEq (7.20), the paper plausibly sits in the **5.5–7.5** range.

**Round 2 Narrowing**: Comparing with Lyra (6.00), Don't Trust: Verify (6.25), FormalAlign (6.50), and BEq (7.20), the paper is stronger than Lyra and Don't Trust: Verify, comparable to FormalAlign, and slightly below BEq. The consistency-tool evaluation concerns and under-described ablation are real but do not invalidate the core contributions. **Final score: 6.5**.

---

## Summary

This paper proposes ATF (Autoformalizer with Tool Feedback), a framework that trains a language model (Qwen3-32B) to use external tools — a Lean 4 compiler for syntax checking and an ensemble of two LLMs for semantic consistency checking — to iteratively refine autoformalizations of natural-language math problems into Lean 4 statements. The training pipeline has three stages: cold-start on synthetic tool-calling trajectories, expert iteration using the tool as a filter, and DPO to reduce ineffective revisions. ATF achieves large gains over prior formalizers on three benchmarks, validated by a small human evaluation, and the authors release a 750K-statement dataset.

## Strengths

- **Substantial and well-triangulated empirical gains.** ATF-32B achieves Pass@1 consistency scores of 94.51% on FormalMath-Lite, 89.78% on ProverBench, and 65.38% on CombiBench, outpacing the best baseline Goedel-V2-Formalizer-32B by margins of 9.1, 10.08, and 29.13 percentage points respectively (Table 3). Gains persist at Pass@8 and Pass@16, and the 8B distilled model also comfortably beats all 32B baselines.

- **Human evaluation confirms the relative ordering.** On the hardest benchmark (CombiBench), ATF achieves 49% human-judged consistency versus 22% for the best baseline — more than a 2× improvement (Table 3, Human Evaluation rows). The human evaluation, though modest in scale (100 instances per benchmark, 3 experts each), directly validates that the automatic metric is not fabricating the advantage.

- **Ablations isolate the contribution of tool feedback.** Removing all tools drops CombiBench consistency from 65.38% to 23.69%; removing only the consistency check drops ProverBench consistency from 89.78% to 75.68% (Table 4). These gaps are large enough that the qualitative conclusion — tools are the critical driver — is robust even if the precise training setup of the ablated variants is not fully specified.

- **Inference-time scaling analysis is informative.** ATF continues to improve with additional revision attempts beyond its training budget (Figure 4a) and reaches near-perfect consistency with sufficient parallel sampling (Figure 4b), demonstrating that the learned revision strategy generalizes.

- **Practical contribution via open-sourced dataset.** The release of Numina-ATF (750K formal statements from competition-level problems) is a concrete resource for the autoformalization and ATP communities.

## Weaknesses

### Fatal

None.

### Major

- **The consistency-check tool — used as both a training filter and the primary evaluation metric — has a significant reliability gap that the paper does not fully contend with.** On the synthetic validation benchmark, the ensemble tool achieves a low false-positive rate (5.79%) but poor recall (59.67%) (Table 1). On real model outputs, the gap between tool and human scores is stark: on CombiBench, the tool rates ATF-32B at 65.38% consistency while humans rate it at 49% (Table 3). The Pearson correlation of 0.746 (Section 4.2) confirms a positive relationship, but a correlation of 0.746 with a systematic 16-point offset on the hardest benchmark means the tool's absolute numbers should not be taken as ground truth. Because the same tool filters trajectories during expert iteration, the training procedure could inadvertently optimize toward the judge's idiosyncrasies. The paper acknowledges the recall sacrifice in passing but does not analyze how the tool's error modes interact with the training loop, nor does it examine whether the model is overfitting to the judge. This is not fatal — the human evaluation independently confirms ATF's superiority — but it qualifies the headline numbers and leaves a gap in the paper's self-understanding.

### Minor

- **The "no tools" ablation is insufficiently described.** Section 4.3 and Table 4 present results for a configuration with "no tools," but the paper does not explain how this variant was trained (same base data? same number of training steps? what does the model output without tool calls?). Without these details, the reader cannot fully assess whether the 41-point gap on CombiBench is attributable to the tools themselves or to confounds in the training setup. The qualitative conclusion remains clear, but a key piece of internal evidence is harder to interpret than it should be.

- **Human evaluation lacks inter-annotator agreement and sample-size justification.** The evaluation uses 100 instances per benchmark with 3 experts each (Section 4.1). No inter-annotator agreement metric (e.g., Fleiss' κ) or confidence intervals are reported. For CombiBench, where the tool-human gap is largest, knowing whether the three experts agreed closely would substantiate the gold-standard numbers.

- **The DPO phase's effect on revision efficiency is asserted but not quantitatively demonstrated.** The motivation (Section 3.2) is to reduce "ineffective revisions," yet no metric such as average tool calls per successful formalization is reported before and after DPO. Table 4 shows only small improvements from DPO over expert iteration (e.g., CombiBench CC from 63.88% to 65.38%), which could reflect noise rather than a systematic efficiency gain.

### Trivial

- The paper does not discuss the computational cost of running the multi-LLM consistency judge during training; this would help readers assess practicality and reproducibility.

## Nice-to-Haves

- A manual analysis of a sample of trajectories where the consistency tool accepted or rejected a formalization, categorizing error types the tool makes, would substantially strengthen the paper's self-awareness about the metric it relies on.
- Expanding the human evaluation to a larger sample with reported inter-annotator agreement would more firmly ground the paper's claims.
- Reporting revision-efficiency metrics (e.g., average tool calls per success) across training stages would make the DPO contribution concrete.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *Harsh Critic: "the paper does not engage seriously with the consequences of using this imperfect metric as both a training signal and a primary evaluation criterion."* — Partially retained as the Major weakness, but the harsh critic's framing as "fatal" is demoted because the human evaluation independently validates the relative gains, and the paper does acknowledge the recall limitation.
- *Harsh Critic: "The paper does not discuss the engineering cost of running the multi-LLM judge at training time."* — Moved to Trivial; this is a practical note, not a weakness that affects the paper's contributions.
- *Harsh Critic: "The contribution of the open-sourced dataset is noted but not evaluated."* — Removed. The dataset release is a contribution in itself; demanding that the paper also evaluate downstream prover training is scope creep. The paper's stated scope is autoformalization, not ATP.
- *Strength Finder: "The consistency-check tool is rigorously benchmarked and shown to be reliable."* — Removed. This overstates the tool's reliability given the documented recall issues and the tool-human gap on CombiBench.
- *Strength Finder: "ATF exhibits strong inference-time scaling behavior... consistency continues to improve with additional revisions."* — Retained but qualified; note that these measurements use the same tool whose reliability is in question.

## Novel Insights

The most interesting finding is the gap between the synthetic consistency benchmark and real deployment: the ensemble tool achieves a low false-positive rate on perturbed statements (5.79%) yet shows a large absolute gap from human judgment on real CombiBench outputs (65.38% tool vs. 49% human). This discrepancy suggests that the synthetic perturbation strategy — while clean and controllable — does not capture the error distribution of real autoformalizer outputs. This is a useful methodological signal for the community: validating evaluation tools only on synthetic perturbations may give a misleading picture of their real-world reliability, and instrumenting the training loop with such a tool requires more caution than the paper currently exercises.

## Suggestions

- Explicitly discuss how the consistency tool's false positives and false negatives might affect expert iteration (e.g., does the model learn to produce formalizations that pass the tool but are actually inconsistent?).
- Describe the "no tools" training configuration — at minimum, whether it uses the same base data and number of training steps, and what the model output format is without tool calls.
- Report inter-annotator agreement for the human evaluation and consider confidence intervals for the human-judged consistency rates.

## Score and Decision

**Anchor comparison summary (all rounds):**

| Anchor | Avg Score | Round | Comparison to ATF |
|--------|-----------|-------|-------------------|
| PDA (k8KsI84Ds7) | 4.75 | R1 | ATF clearly stronger: better results, human eval, cleaner method |
| Lyra (9Z0yB8rmQ2) | 6.00 | R2 | ATF stronger: more novel method, more comprehensive evaluation |
| Don't Trust: Verify (V5tdi14ple) | 6.25 | R2 | ATF stronger: more substantial system, larger empirical gains |
| FormalAlign (B5RrIFMqbe) | 6.50 | R1,R2 | ATF comparable: both have evaluation-tool concerns; ATF has human eval, FormalAlign has cleaner metric design |
| BEq/RAutoformalizer (hUb2At2DsQ) | 7.20 | R1,R2 | ATF slightly below: BEq's metric contribution is more novel and better validated; ATF has stronger system results but metric concerns are more consequential |

**Round 1 bracket**: 5.5–7.5. **Round 2 narrowing**: ATF lands between FormalAlign (6.50) and BEq (7.20), closer to the FormalAlign side due to the more pronounced evaluation-tool concerns (circular use in training + evaluation, larger tool-human gap). The paper is a solid contribution with strong empirical results confirmed by human evaluation, but the reliance on an imperfect metric as both oracle and evaluator is a substantive limitation that prevents placement in the 7+ tier.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>