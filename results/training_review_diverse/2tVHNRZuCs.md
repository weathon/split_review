Here is my final consolidated review after cross-checking all claims against the paper.

---

## Summary

This paper proposes PIT (imPlicit Self-ImprovemenT), a framework that learns self-improvement from preference data without requiring explicit rubrics or hand-written prompts. The key idea is to reformulate the RLHF objective: instead of maximizing absolute response quality, PIT maximizes the quality gap between the improved response and a reference response. This is achieved through a two-stage curriculum RL pipeline (first training on ground-truth preference pairs, then on policy model samples). Experiments on Anthropic/HH-RLHF, OpenAI/Summary, and a synthetic dataset show that PIT consistently improves response quality and outperforms the prompting-based Self-Refine baseline across multiple evaluators (GPT-4, DeBERTa, human judges).

## Strengths

- **Novel formulation of self-improvement as gap maximization.** Rather than requiring hand-crafted rubrics for prompting-based self-improvement, PIT reformulates the RLHF objective to maximize the quality gap between a response and a reference response (Sections 3.1–3.4). This is a principled way to extract improvement direction directly from preference data, addressing a genuine limitation of prompting-based approaches that struggle when goals are complex to articulate (as the paper documents in Section 1, e.g., "make the response more helpful" leading to off-topic additions).

- **Consistent empirical advantage across evaluations.** Table 1 shows PIT improves over original responses by 7.2%–33.59% Δ across three datasets, with both GPT-4 and DeBERTa. The temperature analysis (Figure 3) shows PIT outperforms Self-Refine under most temperatures, including a 9.2% advantage at their respective best temperatures (Section 4.5). The ELO analysis over 55,000 comparisons (Section 4.7) confirms PIT is consistently better than Self-Refine regardless of iteration count.

- **Curriculum RL design is validated as essential.** Section 4.6 and Table 2 demonstrate that omitting either RL stage leads to marginal improvements and large performance gaps. Figure 4 shows that only the full two-stage curriculum enables PIT to break into the "Better" reward region, while the variant with only the second RL stage remains stuck in "Similar" or "Worse" regions. This ablation directly supports the paper's central methodological design choice.

- **Multi-faceted evaluation.** The paper uses three distinct evaluators (GPT-4, DeBERTa, human judges), analyzes temperature sensitivity, iteration effects, and curriculum design, and provides ELO-based ranking — going beyond a single metric or dataset.

## Weaknesses

### Fatal
None.

### Major

- **Human evaluation is critically underdocumented.** The paper reports one aggregate number (Δ=23.53% for PIT vs. Self-Refine on Anthropic/HH-RLHF) with no details: no number of annotated examples, no number of annotators, no inter-annotator agreement (Cohen's κ), no confidence intervals, and no annotation instructions. Since GPT-4 and DeBERTa disagree on the relative ranking (GPT-4 favors Self-Refine by 3.91%; DeBERTa favors PIT by 3.70%), the human evaluation is the tie-breaker, and its inadequate reporting substantially weakens the paper's strongest comparative claim. This is the single largest evidential gap in the submission.

### Minor

- **Only one prompting baseline with an underspecified prompt.** PIT is compared only against Self-Refine. The exact prompt used is not provided in the paper (Section 4.2 describes it generically as instructing the model "to reflect the current response and give feedback to improve the response"). While Self-Refine is a representative prompting-based method, the lack of prompt documentation makes it difficult to assess whether the baseline is reasonably strong. Adding a second baseline with a manually crafted detailed rubric (even just to show PIT remains competitive) would strengthen the paper.

- **Training cost is not quantified.** PIT requires training a separate M_PIT model plus two rounds of RL, which is substantially more expensive than zero-training prompting methods. The paper's claim that "PIT does not bring extra computational overhead compared with prompting methods such as Self-Refine" (Section 3.5) refers only to inference. No training FLOPs, TPU-hours, or comparable cost metric is reported, making it impossible to assess the practical trade-off between the improvement and the training expense.

- **RL hyperparameters not reported.** The paper uses a KL coefficient β in the RL objective (Equations 3–5) but never reports its value, learning rate, number of RL steps, batch size, or any training hyperparameters. This hurts reproducibility.

- **No ablation on the reward model loss design.** Equation 2 uses five pairwise comparisons (gap(w,l) > gap(w,w), gap(w,l) > gap(l,l), gap(w,l) > gap(l,w), gap(w,w) > gap(l,w), gap(l,l) > gap(l,w)). The paper simply states "we find Equation 2 is the best fit" without showing results from simpler alternatives (e.g., only using the gap(w,l) comparison, or computing rewards via R_P subtraction). A systematic ablation is missing.

- **GPT-4 length bias claim is asserted but not quantified.** The paper attributes GPT-4's preference for Self-Refine over PIT to GPT-4's inclination toward long responses and Self-Refine's tendency to generate such responses (Section 4.4). However, no actual length analysis (average response lengths, length distributions, correlation between length and win rate) is provided to substantiate this claim.

- **No failure case analysis or limitation discussion.** The paper does not discuss cases where PIT fails to improve, where Self-Refine outperforms PIT, or what types of tasks or data distributions are ill-suited for the approach. This limits the reader's ability to understand the method's boundaries.

### Trivial

- **Ambiguous phrasing in Section 2.** "Our method does not require modifying model weights, interactive environment, or explicitly prompting" — the phrase "modifying model weights" is ambiguous because PIT does train M_PIT from scratch, though the original policy model weights are not modified. The claim would be clearer as "does not require modifying the base policy model's weights" or "does not require fine-tuning the original model."

## Nice-to-Haves

- A comparison against a prompting baseline with a carefully engineered rubric (e.g., derived from the Anthropic/HH-RLHF annotation axes) would cleanly address the concern that the current baseline is suboptimally prompted.
- A length analysis comparing PIT and Self-Refine responses to substantiate the GPT-4 bias claim.
- A discussion of computational cost with rough TPU-hour estimates and inference latency comparisons.
- Intermediate training curves for the curriculum RL stages beyond the final reward plot in Figure 4.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Critic claim about "modifying model weights" being contradictory.** The critic states PIT "does modify model weights" because it trains M_PIT from scratch. However, the paper's claim is that the *original policy model's* weights are not modified — PIT trains a separate model. The critic's interpretation is overly literal and ignores that "modifying" in this context refers to fine-tuning an existing model. The method section is fully consistent. This is at most a clarity nitpick.

- **Critic claim about synthetic dataset not being described.** Section 4.1 is empty in the parser-extracted text, which is a parser artifact — the original submission contained this content. The paper references the synthetic dataset across multiple sections with contextual hints (e.g., "a much larger LLM produces y_w," "we only evaluate the instruction following ability"). The missing description is a parser issue, not an author error.

- **Critic claim about overstating the difficulty of writing rubrics and not acknowledging tasks with clear evaluation criteria.** The paper explicitly discusses summarization and other tasks with evaluation criteria (Section 1, citing Stiennon et al. and Rafailov et al.), and acknowledges that prompting works well when goals are "clear, simple, and well-defined." The critic's characterization is a misreading.

- **Critic claim about missing comparison with methods that "learn to improve from data."** The paper discusses self-training and iterative DPO methods in the Related Work section on alignment. The paper's scope is self-improvement through prompting, and the comparison against Self-Refine is appropriate for evaluating prompting-based methods.

## Novel Insights

The most interesting observation emerging from this review is the asymmetric evaluator disagreement: GPT-4 (an LLM-as-judge) prefers the prompting-based Self-Refine, while DeBERTa (a learned reward model based on preference data) prefers the implicitly-trained PIT, with humans siding with PIT by a wide margin. This suggests a systematic evaluation bias: LLM-based evaluators may favor responses that are similar to what LLM-based self-improvement (Self-Refine) produces — potentially because both use similar rubrics or reasoning patterns. If this pattern holds generally, it raises questions about the reliability of LLM-based evaluation for comparing methods that do/don't use explicit prompting, and underscores the value of the paper's triangulation approach. However, the lack of human evaluation details means this important finding remains suggestive rather than conclusive.

## Suggestions

1. **Document the human evaluation rigorously** — report N, number of annotators, inter-annotator agreement (Cohen's κ), confidence intervals, and the exact instructions given to annotators. If possible, evaluate on a second dataset as well.
2. **Add a prompting baseline with a detailed rubric** — construct a rubric from the Anthropic/HH-RLHF data itself (e.g., using the annotation axes or discriminative features) to show PIT remains competitive even against a well-tuned prompt.
3. **Quantify training cost** — report approximate TPU-hours for each training stage and note inference cost relative to Self-Refine.
4. **Report RL hyperparameters** — provide β, learning rate, number of RL steps/batches, and any reward normalization used.
5. **Add the pairwise-loss ablation** — compare the full Equation 2 against simpler variants to justify the design.
6. **Include a length analysis** — report average response lengths and their correlation with win rates to substantiate the GPT-4 bias claim.

## Score and Decision

This paper makes a genuinely novel contribution: reformulating self-improvement as implicit learning from preference data via gap maximization, supported by a clean curriculum RL design. The method is well-motivated, the core idea is sound, and the experimental results are broadly positive across multiple evaluations and datasets. The main weaknesses are (1) insufficiently documented human evaluation (the most critical gap), (2) a single underspecified prompting baseline, and (3) missing reproducibility details. These are fixable issues that do not invalidate the core contribution. Given the novelty of the approach and the breadth of automatic evaluation, the paper merits acceptance pending the strengthening of the human evaluation reporting and baseline specification.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>