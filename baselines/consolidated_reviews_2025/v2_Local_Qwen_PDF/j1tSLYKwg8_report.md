## Summary
This paper proposes a practical adaptation recipe to convert autoregressive (AR) language models into diffusion language models (DLMs), addressing the scaling challenges that have limited DLM research to smaller model sizes. By unifying AR and diffusion objectives through attention mask annealing and a shift operation, the authors successfully adapt GPT2 and LLaMA2 models (up to 7B parameters) into DiffuGPT and DiffuLLaMA using less than 200B tokens. The adapted models demonstrate state-of-the-art performance among existing DLMs, showing particular strengths in infilling tasks, unconditional generation speed, and commonsense reasoning. However, the adaptation process incurs a noticeable trade-off in factual knowledge retention (e.g., TriviaQA, PIQA) compared to the base AR models. The paper provides a comprehensive benchmark and open-source release, contributing valuable resources to the DLM community.

## Strengths
1. **Practical Scaling Recipe:** The paper provides a clear, reproducible adaptation framework (attention mask annealing + shift operation) that successfully bridges the objective gap between AR and DLMs, enabling the training of 7B-parameter diffusion models.
2. **Comprehensive Benchmarking:** The evaluation goes beyond perplexity, covering reasoning, commonsense, infilling, and unconditional generation. This offers a more nuanced view of DLM capabilities compared to prior works.
3. **Strong Infilling & Speed Advantages:** The adapted models demonstrate natural support for filling-in-the-middle tasks and competitive inference speeds for long sequences, highlighting practical advantages of the diffusion paradigm.
4. **Open-Source Contribution:** Releasing models (127M-7B), code, and evaluation toolkits significantly lowers the barrier for future DLM research and fosters community exploration.

## Weaknesses
1. **Knowledge Retention Trade-off:** The adaptation process causes significant performance drops on factual knowledge benchmarks (TriviaQA, PIQA) compared to base AR models. The paper attributes this to insufficient training tokens but does not deeply analyze whether the diffusion objective inherently struggles with precise fact memorization.
2. **Unfair Infilling Comparison:** The infilling advantage of DLMs is highlighted against AR models that lack explicit FIM training. Without a FIM-tuned AR baseline, the performance gap is inflated by training asymmetry rather than pure architectural superiority.
3. **Overclaimed Competitiveness:** The abstract and contributions claim the models are "competitive with their AR counterparts," which is misleading given the substantial gaps in knowledge and instruction-following tasks. This overstatement weakens scientific credibility.
4. **Speculative Analysis:** Explanations for Plaid 1B's poor conditional performance and CoT failure are presented as hypotheses without controlled ablations, limiting the analytical depth.

## Key Issues
1. **Claim-Evidence Misalignment (Major):** The assertion that DiffuGPT "outperforms GPT2 in most tasks" is contradicted by Table 1, which shows underperformance on TriviaQA and PIQA. This requires immediate bounding to specific task categories.
2. **Evaluation Fairness (Major):** The infilling comparison lacks a FIM-tuned AR baseline, making the DLM advantage appear larger than it is under matched training conditions.
3. **Novelty Positioning (Minor):** The claim that AR-to-DLM adaptation "remains unexplored" is too broad given prior MLM-based adaptation works. It should be refined to distinguish from bidirectional MLM initialization.
4. **Reproducibility Detail (Minor):** The selection of existing vocabulary tokens as [MASK] tokens lacks frequency reporting, leaving potential semantic interference risks unassessed.

## Actionable Suggestions
1. **Bound Competitiveness Claims:** Revise the abstract and contribution bullets to explicitly state that competitiveness is limited to infilling, unconditional generation speed, and specific reasoning tasks, while acknowledging knowledge retention gaps.
2. **Add FIM-Tuned Baseline:** Include a FIM-tuned AR model (e.g., CodeLLaMA or a LLaMA variant with SPM/PSM objectives) in the infilling evaluation to provide a fair comparison and isolate architectural advantages from training asymmetries.
3. **Deepen CoT Analysis:** Expand the discussion on CoT failure to hypothesize whether diffusion-specific factors (e.g., parallel denoising conflicts) exacerbate reasoning limitations beyond general instruction-tuning deficits.
4. **Report Mask Token Frequency:** In the appendix, report the corpus frequency of the selected [MASK] tokens and briefly discuss how the model handles natural occurrences of these tokens to address reproducibility concerns.

## Storyline Options + Writing Outlines
**Abstract Outline:**
- S1 (Problem): DLMs offer parallel generation and infilling advantages but are limited by small scale and high training costs.
- S2 (Gap): Training DLMs from scratch is resource-intensive, and prior adaptation attempts from MLMs lose base capabilities.
- S3 (Method): We propose a simple adaptation recipe unifying AR and diffusion objectives via attention mask annealing and shift operations.
- S4 (Result): We scale DLMs to 7B parameters (DiffuLLaMA), outperforming prior DLMs and showing competitive infilling/speed, though with knowledge retention trade-offs.
- S5 (Impact): We release models and code to foster DLM research as a viable alternative to AR paradigms.

**Introduction Outline:**
- P1: AR dominance and inherent limitations (sequential generation, planning).
- P2: DLM potential (parallelism, infilling) but scaling gap vs AR.
- P3: Adaptation challenges (objective mismatch, causal mask bias).
- P4: Proposed solution (unified objectives, annealing, shift op).
- P5: Contributions (scaling to 7B, comprehensive benchmark, open-source release).
- P6: Bounded claim preview (strengths in infilling/speed, trade-offs in knowledge).

## Priority Revision Plan
| Priority | Action | Expected Impact |
|---|---|---|
| P0 (Critical) | Bound "competitive" claims in Abstract/Intro to specific tasks (infilling, speed). | Restores scientific credibility and aligns claims with Table 1 evidence. |
| P0 (Critical) | Add FIM-tuned AR baseline for infilling comparison. | Isolates architectural advantage from training asymmetry. |
| P1 (Major) | Qualify novelty claim in Related Work to distinguish from MLM adaptation. | Prevents reviewer criticism on broad novelty assertions. |
| P1 (Major) | Report mask token frequency and interference handling in Appendix. | Improves reproducibility and robustness assessment. |
| P2 (Minor) | Deepen CoT failure analysis with diffusion-specific hypotheses. | Enhances analytical depth and insight into DLM reasoning. |

## Experiment Inventory & Research Experiment Plan
**Completed Experiment Inventory:**
| Exp ID | Objective | Setup | Metrics | Main Outcome | Limitation |
|---|---|---|---|---|---|
| E1 | Benchmark DLM vs AR | Table 1 (QA, Commonsense, Math, Infilling) | Acc, ROUGE | DLMs win infilling/speed; lag in knowledge | Unfair infilling comparison |
| E2 | Unconditional Gen Quality | Fig 3 (Perplexity, Dist-2) | PPL, Dist-2 | DiffuGPT excels at low steps | Plaid 1B analysis speculative |
| E3 | ICL & Reasoning | Table 2 (MAWPS, SATMath) | Exact Match | ICL helps; CoT drops | CoT failure analysis shallow |
| E4 | Ablation | Table 3 (GSM8K-symbolic) | Acc | Shift/anneal critical | Limited to small models |

**Proposed Research Experiments:**
1. **FIM-Tuned AR Baseline (P0):** Train LLaMA with SPM/PSM objectives on 100M tokens. Compare infilling ROUGE to isolate architectural vs training advantages.
2. **Knowledge Retention Probe (P1):** Evaluate on NQ/OpenBookQA with varying adaptation token counts to map the scaling law of fact preservation.
3. **Continuous vs Discrete Ablation (P2):** Train a continuous diffusion variant under identical settings to DiffuGPT to validate the hypothesis on conditional generation gaps.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10
The paper makes a valuable contribution by providing a practical recipe for scaling DLMs and releasing open-source resources. However, the score is moderated by overclaimed competitiveness, unfair infilling comparisons, and superficial analysis of reasoning failures. Bounding claims and adding fair baselines would significantly strengthen the work.

**Post-Revision Target:** [7.5, 8.5]/10
If the authors bound their claims to match the evidence, add a FIM-tuned AR baseline, and deepen the analysis of knowledge retention and CoT failures, the paper would present a much more credible and impactful contribution to the DLM field.