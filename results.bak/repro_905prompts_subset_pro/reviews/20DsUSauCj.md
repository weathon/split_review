Now I have all the calibration data I need. Let me synthesize the final review.

**Round 1 Bracket**: The paper falls between the weak anchors (~3.0, e.g., DXaUC7lBq1 — personality in LLMs with speculative claims) and the strong anchor 6Mxhg9PtDE (9.50 — Shallow Safety Alignment, a crisp paradigm-shifting insight). It is clearly stronger than IssPhpUsKt (6.80 — RepE for reasoning, limited tasks/models). Initial bracket: **6.5–8.5**.

**Round 2 Narrowing**: The most comparable anchors are:
- wozhdnRCtw (7.00): activation steering for instruction following. Narrower scope (3 tasks), no training-time intervention. Our paper is stronger.
- Oi47wc10sm (7.33): Conditional Activation Steering. One novel technique; our paper has broader scope with 5 applications + novel preventative steering. Our paper is comparably strong or slightly stronger.
- rwqShzb9li (7.50): Linear representations of political perspective. Very similar methodology (finding linear directions for subjective concepts), comparable depth. Our paper has more applications and preventative steering. Comparable or slightly stronger.

The paper is clearly in the **7.5–8.0** range. Final score: **7.5**.

---

## Summary

This paper introduces an automated pipeline that extracts linear *persona vectors* from LLM activations corresponding to personality traits (evil, sycophancy, hallucination, and others), requiring only a natural-language description as input. The extracted vectors are validated through causal steering, and the paper demonstrates five applications: (1) inference-time trait control, (2) pre-response monitoring of prompt-induced persona shifts, (3) monitoring finetuning-induced shifts via activation projection, (4) a novel *preventative steering* method that intervenes during training to avert unwanted persona drift while preserving general capabilities, and (5) pre-finetuning data screening using projection differences on training data. Experiments span two models (Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct), multiple traits, and diverse finetuning datasets including emergent-misalignment-like scenarios.

## Strengths

- **Automated, scalable pipeline**: The extraction pipeline requires only a trait name and description, automatically generating contrastive system prompts, evaluation questions, and rubrics via Claude — a practical advance over prior work requiring manual contrastive pair construction (Section 2).
- **Strong causal validation**: Steering with persona vectors produces clear, coefficient-dependent increases in trait expression (Figure 2), with compelling qualitative examples (explicitly evil, sycophantic, or hallucinated outputs).
- **Finetuning shift prediction is robust**: Activation shifts along persona vectors during finetuning correlate r = 0.76–0.97 with post-finetuning trait expression across two models and multiple datasets (Figure 4). Cross-trait baselines (r = 0.34–0.86) confirm the vectors carry trait-specific signal.
- **Preventative steering is genuinely novel and practically useful**: Steering *toward* the persona vector during training counteracts the finetuning objective's tendency to push the model along that direction, reducing undesirable trait expression while preserving MMLU accuracy — in stark contrast to destructive inference-time steering (Figures 5, 6). The fact-acquisition case study (Figure 6) is particularly compelling: preventative steering eliminates hallucination to near-baseline while retaining newly learned facts and MMLU, whereas inference-time steering degrades both.
- **Pre-finetuning data screening is predictive**: Dataset-level projection difference on training data correlates r = 0.88–0.95 with post-finetuning trait expression (Figure 7), and sample-level separability is clear (Figure 8), enabling proactive filtering before any training occurs.
- **Scope and generality**: The pipeline is validated across two model families, three primary traits plus four additional traits (including positive ones like optimism), multiple dataset types (intentional and EM-like), and compared against reasonable baselines (CAFT, regularization, prompt-based approaches).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the presented evidence.

### Minor

- **Structural dependence on LLM judge**: Nearly all quantitative evaluations rely on GPT-4.1-mini trait expression scores. The paper acknowledges this and points to human-evaluator validation and external benchmark comparisons in Appendix D, which is the right approach. The qualitative steered-output examples provide orthogonal face validity. This does not undermine the core claims but readers should be aware that the evidential chain flows through a single evaluation oracle.

- **Synthetic finetuning datasets**: All finetuning experiments use purpose-constructed datasets (trait-eliciting and EM-like). Testing on published real-world finetuning runs (e.g., the GPT-4o sycophancy incident cited in the introduction) would strengthen external validity, though the constructed datasets are well-motivated and cover meaningful scenarios.

### Trivial

- Single-layer preventative steering does not always *fully* prevent trait acquisition for target-aligned datasets like Evil II. The paper addresses this with multi-layer steering (Appendix L.3) and acknowledges the limitation in the main text (Section 5.1), so this is appropriately handled.

## Nice-to-Haves

- Moving key judge-validation evidence from Appendix D into the main narrative would directly address the largest structural concern readers may have about the evaluation pipeline.
- Testing persona-shift prediction or preventative steering on a published real-world finetuning run would increase external validity without diluting the paper's focus.
- A brief discussion of when linear additive steering leads to output quality degradation (beyond MMLU) would help practitioners gauge trustworthiness.

## Removed Points

*These points were raised in the input reviews but are removed from the final review with justification.*

- **"Monitoring correlations are heavily driven by prompt-type differences"** — The paper already explicitly acknowledges this in Section 3.3: "These correlations arise primarily from distinguishing between different prompt types... with more modest correlations when controlling for prompt type. This indicates the persona vectors are effective for detecting clear and explicit prompt-induced shifts, but may be less reliable for more subtle behavioral changes." This is a limitation the authors already flag; restating it as a criticism would be redundant.

- **"Cross-trait correlations indicate shared variance"** — The paper already acknowledges this in footnote 6 of Section 4.2: "it is worth noting that persona shifts are rather correlated between seemingly different traits." The paper also reports cross-trait baseline correlations explicitly. The paper already handles this nuance.

- **"Layer selection ties to the evaluation metric"** — Selecting layers by testing steering effectiveness is standard practice in the activation steering literature. The multi-layer approach (Appendix L.3) mitigates any inflation concern.

- **"CAFT comparison relegated to appendix"** — The main text (Section 5.1) already states the key finding: "CAFT is effective at preventing evil and sycophancy, but ineffective for hallucinations." The appendix details are appropriately placed.

- **"Missing real-world finetuning scenarios"** — Demoted to Nice-to-Have. The paper's synthetic datasets are well-motivated and cover meaningful scenarios.

- **"Computational cost of pipeline"** — Generating 400 responses and computing activations is standard-scale for this research area; not a substantive concern.

- **"Sensitivity to prompt templates and model differences"** — A reasonable ablation to request but not a weakness of the current work.

## Novel Insights

The most genuinely novel insight emerging from this work is the *preventative steering* paradigm: steering *toward* an undesirable direction during training to counteract the training objective's tendency to push the model in that direction, rather than steering *against* it at inference time. This inverts the standard activation steering logic and yields a qualitatively different trade-off curve — suppressing unwanted behaviors while preserving (rather than destroying) general capabilities. The fact-acquisition case study (Figure 6) crystallizes this: inference-time steering creates a destructive accuracy-safety trade-off, while preventative steering largely avoids it. This finding has implications beyond persona control, suggesting a general principle for training-time intervention that preserves capabilities while constraining representational drift.

## Suggestions

- The fact-acquisition case study (Figure 6) is among the paper's strongest results. Expanding it with a second competency benchmark (e.g., coding or summarization) would further solidify the preventative steering story without requiring major new experiments.
- Consider discussing the shared variance among negative traits more prominently in the main text (rather than only in a footnote), as it has practical implications for multi-trait preventative steering.

## Score and Decision

### Anchor Comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| DXaUC7lBq1 (LLM personality origins) | 3.00 | R1 | Much weaker: speculative claims, limited validation, confused presentation |
| IssPhpUsKt (RepE for reasoning) | 6.80 | R1 | Weaker: narrower scope, simpler tasks, mixed evidence on core claims |
| 6Mxhg9PtDE (Shallow safety alignment) | 9.50 | R1 | Stronger: crisper conceptual insight, more focused story |
| wozhdnRCtw (Activation steering for instruction following) | 7.00 | R2 | Weaker: 3 narrow tasks, no training-time intervention |
| rwqShzb9li (Linear representations of political perspective) | 7.50 | R2 | Comparable methodology; our paper has broader applications + novel preventative steering |
| Oi47wc10sm (Conditional Activation Steering) | 7.33 | R2 | Comparable; one novel technique vs. our paper's broader scope across 5 applications |

The paper is clearly stronger than the 7.00 anchor and comparable to or slightly stronger than the 7.33–7.50 anchors. It does not reach the 9.50 level of a paradigm-shifting conceptual contribution. Score: **7.5**.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>