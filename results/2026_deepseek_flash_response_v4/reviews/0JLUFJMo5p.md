## Summary

This paper proposes DTERM (Dynamic Task-Embedded Reward Machine), a framework that uses a hypernetwork to generate task-dependent weights for multiple reward components in reinforcement learning for code generation and manipulation tasks. The hypernetwork takes task embeddings (e.g., from CodeBERT) and produces softmax-normalized weights for sub-rewards such as compilation success, test passing rate, code similarity, style adherence, and computational efficiency. Experiments on five benchmarks (summarization, translation, completion, repair, competitive programming) show consistent improvements over Uniform, Expert-Tuned, and GradNorm baselines, with an ablation study confirming that removing the hypernetwork or task embeddings causes the largest performance degradations.

## Strengths

1. **Hypernetwork-driven dynamic reward weighting demonstrably improves over static weighting**: The ablation study (Table 2) isolates this component: removing the hypernetwork drops HumanEval Pass@1 from 22.7 to 18.1 (~20% relative decline), providing direct evidence that the dynamic weighting mechanism drives gains beyond the multi-reward setup alone. This is the paper's core empirical contribution and is properly tested.

2. **Consistent improvements across five diverse benchmarks**: Table 1 shows DTERM outperforms Uniform, Expert-Tuned, and GradNorm on every task/metric combination — summarization (BLEU-4 26.5 vs. best baseline 24.3), translation (46.4 vs. 42.0), completion (Exact Match 69.5 vs. 66.8), repair (Fix Rate 62.1 vs. 58.7), and competitive problems (Pass@1 22.7 vs. 19.2). The consistency across tasks supports the claim that task-adaptive reward weighting broadly benefits code RL.

3. **Zero-shot generalization to unseen tasks has empirical backing**: Figure 2 (tabular data lines 229–234) shows DTERM achieving 0.70 normalized reward on unseen tasks vs. baselines (GradNorm 0.47, Expert-Tuned 0.39, Uniform 0.28), maintaining advantage across all 10 tasks (reaching 0.93 vs. next-best 0.66).

4. **Dynamic reward analysis shows meaningful task differentiation**: Figure 3 reveals substantial variation in learned sub-reward proportions across task types (e.g., "translation" assigns weight 0.29 to Style Adherence but only 0.09 to Compilation Success; "repair" assigns 0.22 to Compilation Success), suggesting the model genuinely adapts to task demands rather than memorizing a single weighting.

## Weaknesses

### Fatal
None.

### Major

1. **The base policy model is never specified** — Section 5.1 states "We train using PPO" with a learning rate of 3e-5 and batch size 32, but never names which code generation LLM is being fine-tuned (e.g., CodeGPT, CodeT5, StarCoder, CodeLlama). Without this, the results are uninterpretable: a Pass@1 of 22.7 on HumanEval could be excellent or mediocre depending on the base model, and the experiments cannot be reproduced or situated in the literature. This is the most significant gap in the paper — it undermines the entire experimental contribution because readers cannot assess whether the reported values represent strong, moderate, or weak performance.

2. **Baselines are not representative of the state of the art in RL for code generation** — The paper compares against Uniform, Expert-Tuned, and GradNorm, which are general multi-task/multi-objective optimization approaches, not actual RL-for-code-generation methods. There is no comparison against CodeRL (Le et al., 2022, cited in the paper), execution-guided synthesis (Chen et al., 2018a, cited), or any compiler-feedback RL method. Since the paper is specifically about improving RL for code generation, the evaluation should include the methods that define the current SOTA in that sub-area. The claimed gains (+18.4% fix rate, +12.7% BLEU) may simply reflect weak baselines rather than DTERM's strength.

3. **No variance or statistical significance reported despite using 3 random seeds** — The paper states "3 random seeds" were used (Section 5.1), but Tables 1 and 2 report only point estimates. Without standard deviations or confidence intervals, it is impossible to assess whether the margins (e.g., 22.7 vs. 19.2 for GradNorm on HumanEval) are meaningful or noise. This is a basic reporting requirement that is not met.

4. **The cross-task generalization experiment (Figure 2) is critically underspecified** — The paper tests on "10 unseen tasks" but does not define what these tasks are, where they come from, or how they differ from the training tasks. The "normalized reward" metric is not explained (normalized by what baseline or maximum?). Without this information, the experiment provides no scientific evidence that can be interpreted or reproduced.

5. **Multiple described components are never evaluated** — CLIP-based multi-modal fusion (Section 4.4) and RLHF integration (Section 4.6) are presented as features of the framework but are never used in any experiment. The qualitative examples (Section 5.6) consist of a single sentence about one case study. An architecture with multiple loosely-connected mechanisms where several are untested undermines the paper's credibility and raises questions about whether the framework is over-engineered relative to what is actually validated.

### Minor

1. **The conclusion section is essentially absent** — Section 6 contains only one generic sentence ("The success of DTERM has implications for the wider field of reinforcement learning systems...") after garbled text that is a parser artifact. There is no synthesis of findings, no acknowledgment of limitations, and no discussion of failure cases. The paper ends abruptly.

2. **"Reward Machines" framing is misleading** — The title and framing invoke reward machines (Icarte et al., 2022) as a motivation, but the method does not use finite state machines or exploit state-machine structure. Section 3.5 acknowledges this ("While our approach differs in implementation..."), but the framing still over-promises. The method is a hypernetwork-based dynamic weighting scheme, not a reward machine.

3. **Ablation does not fully isolate the hypernetwork's standalone contribution** — "w/o Hypernetwork" (18.1 on HumanEval, Table 2) still includes task embeddings, FiLM modulation, compiler feedback, and prototypes. The gap relative to Uniform (15.8) could be driven by these other components. A cleaner ablation would jointly remove all task-adaptive mechanisms.

### Trivial
None.

## Nice-to-Haves
- Report standard deviations or confidence intervals from the 3 seeds in Tables 1 and 2.
- Include at least one SOTA RL-for-code-generation baseline such as CodeRL.
- Define the 10 unseen tasks used in the generalization experiment and explain what "normalized reward" means.
- Either run experiments on CLIP fusion and RLHF integration, or remove those sections from the method description.
- Expand the conclusion to synthesize findings, discuss limitations, and identify failure cases.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Criticisms about garbled text** ("The Word xog", "Bat var", garbled conclusion text): Per the filtering rules, these are parser artifacts and not present in the original submission. The conclusion being thin (just one generic sentence) is retained as a Minor weakness, but the garbled text itself is not counted.
- **Claim that the ablation is "internally inconsistent"** (w/o Hypernetwork vs. Uniform): This misunderstands what "w/o Hypernetwork" removes — it keeps FiLM modulation, task embeddings, compiler feedback, and prototypes, so 18.1 > 15.8 is explainable, not inconsistent. The non-isolation concern is worth noting and has been weakened to a Minor point.
- **Criticisms about unresolved "(?)" citations**: These are parser artifacts per the filtering rules.
- **Criticism that the paper "needs rebuilding from ground up"**: Overstates severity given the paper's conceptual merits; the evaluation needs improvement but the core idea is sound.
- **Strength Finder's generic/superficial strengths**: Strengths about "the problem being important" or "this paper addresses an important challenge" — these lack specific citation to paper content and are removed.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Specify the base policy model** — this is the single most important missing piece. The entire experimental contribution is opaque without it.
2. **Include at least one SOTA RL-for-code-generation baseline** such as CodeRL, to establish that DTERM's gains hold against meaningful competitors.
3. **Report variance from the 3 seeds** in all tables (mean ± std).
4. **Define the 10 unseen tasks and the normalized reward metric** for the generalization experiment.
5. **Evaluate or remove untested components** — CLIP fusion and RLHF integration should either have dedicated experiments or be cut from the description.
6. **Expand the conclusion** to synthesize findings and explicitly discuss limitations.

---

## Score and Decision

**Round 1 bracket**: I examined 3 score bands. Low-band anchors (score < 3.5): FALCON (3.0), LARG2 (3.0), Improve Code Generation (3.0) — all rejected papers on code+RL. Middle-band anchors (3.5–7.5): HyperMask (3.67), AdaQN (6.67), HyPoGen (7.0), Non-Markovian Reward (4.0), Magnitude Invariant Hypernetworks (6.25). High-band anchors (score > 7.5): GenSim (8.0), RM-Bench (8.0), WizardMath (8.0), SMC control (8.0), LLM-SR (8.0). DTERM clearly falls in the middle band, between ~3.5 and ~5.5.

**Round 2 narrowing** (3.0–5.5): LangProp (5.00), Coarse-Tuning (4.75), RLEF (4.50), HyperLoRA (4.75), HART (5.33), Non-Markovian Reward (4.0) are the closest anchors. Reading these in full shows: Coarse-Tuning (4.75) and RLEF (4.50) name their base models and report complete experimental setups — DTERM is weaker on reporting transparency. Non-Markovian Reward (4.0) has similar score but better experimental rigor. LangProp (5.00) has high variance but stronger experimental scope.

| Anchor | Path | Avg Score | Round | Comparison to DTERM |
|--------|------|-----------|-------|---------------------|
| FALCON | N18Z2MkMEa.md | 3.00 | 1 | Weaker method clarity, worse paper quality → DTERM is better |
| LARG2 | Q6HYM1EMu8.md | 3.00 | 1 | Different domain, cleaner evaluation → comparable quality |
| Improve Code Gen | CscKx97jBi.md | 3.00 | 1 | Similar evaluation gaps but narrower scope → similar |
| Non-Markovian Reward | VnNSkUXejc.md | 4.00 | 1,2 | Similar score, better evaluation rigor → DTERM slightly weaker |
| Coarse-Tuning | vLqkCvjHRD.md | 4.75 | 2 | Names its model, clearer experiments → DTERM weaker |
| RLEF | zPPy79qKWe.md | 4.50 | 2 | Names its model, better evaluation → DTERM weaker |
| LangProp | UgTrngiN16.md | 5.00 | 2 | Broader scope, higher variance → DTERM comparable |
| HyperMask | LhNZqkuVte.md | 3.67 | 1 | Hypernetwork domain, different task → DTERM somewhat better |
| AdaQN | leACdxBEgv.md | 6.67 | 1 | Stronger evaluation, theory → DTERM much weaker |
| HyPoGen | CJWMXqAnAy.md | 7.00 | 1 | Stronger evaluation, clearer method → DTERM much weaker |
| HyperLoRA | u6vC7KaFel.md | 4.75 | 2 | Hypernetwork for LLM adaptation, cleaner eval → DTERM weaker |
| HART | iP8ig954Uz.md | 5.33 | 2 | Hypernetwork for adaptation, better analysis → DTERM weaker |
| BigCodeBench | YrycTjllL0.md | 9.00 | 1 | Benchmark paper, not comparable outlier |

DTERM's core idea (dynamic reward weighting via hypernetwork) is sound and the experimental trends are consistent. However, the evaluation has multiple significant gaps: the policy model is unnamed, baselines are not SOTA, no variance is reported, and the generalization experiment is underspecified. These issues place it below Coarse-Tuning (4.75) and RLEF (4.50), which at least meet basic experimental reporting standards. It is comparable to Non-Markovian Reward (4.00), though DTERM has more practical relevance but weaker reporting.

**Final Score: 4.0** — The paper presents a reasonable direction but the experimental evaluation has significant gaps that prevent acceptance in the current form. The issues are addressable (name the model, add baselines, report variance, define the generalization tasks), and the core method is not fundamentally flawed. However, as submitted, the evidence is insufficient to establish the claimed contributions.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>