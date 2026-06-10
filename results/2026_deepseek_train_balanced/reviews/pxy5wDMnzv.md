Now let me write the final review.

## Summary

This paper proposes InvestAlign, a method that generates SFT training data from the theoretical solution of a simpler optimal investment problem (absolute herd behavior, P2) to fine-tune LLMs for a more complex problem (relative herd behavior, P1). The authors collect real-user data from 119 participants, validate that the P2 theoretical solution matches this data statistically, construct a 1000-sample SFT dataset from the P2 solution, and fine-tune four LLMs. They report 44–61% MSE reductions versus untuned models on both P2 and P1, and provide a theoretical convergence analysis arguing that training on clean synthetic data converges faster than on noisy real-user data.

## Strengths

- **Real data collection and validation of the theoretical proxy.** The paper collects actual investment decisions from 119 participants to validate that the P2 theoretical solution is a reasonable proxy for real investor behavior (Section 3.3). This goes beyond purely synthetic work and provides an empirical grounding for the data-generation pipeline.

- **Consistent empirical improvement across multiple LLM families.** Table 1 reports that InvestAlign reduces MSE by 45–61% on P2 and 44–57% on P1 across four LLMs (GPT-3.5-Turbo, GLM-4-9B-CHAT, Qwen2-7B-Instruct, Llama-3.1-8B-Instruct). Testing on multiple architectures strengthens the claim that the effect is not model-specific.

- **Structured problem decomposition.** The paper clearly formulates four research questions (A–D) and systematically addresses each one, providing a clear logical structure.

- **Theoretical convergence analysis.** Section 4.2 derives that gradient norms are larger when training on clean synthetic data versus noisy real-user data (Eq. 12), and validates this experimentally on three open-source models. While the analysis relies on simplifications, it is a novel formal addition beyond typical SFT work in finance.

## Weaknesses

### Major

1. **Missing comparison: SFT on real-user data.** The paper's central value proposition is that synthetic theoretical-solution data can *substitute* for expensive real-user data. Yet no experiment compares InvestAgents (fine-tuned on synthetic P2 data) against models fine-tuned on real P2 data of comparable size, or against models fine-tuned on real P1 data. The only baseline is a pre-SFT LLM — i.e., no fine-tuning at all. Without this comparison, the core claim that synthetic data is a viable substitute remains unsubstantiated. The paper reports that "pre-SFT LLMs fail to align with real-user data" (Figure 2) and then shows that fine-tuning on *any* data improves over that — but this is expected and does not test the method's value.

2. **Transfer from P2 to P1 is not isolated from the effect of any fine-tuning.** The paper fine-tunes on P2 data and evaluates on P1, finding improvement. But there is no control condition (e.g., fine-tuning on randomly generated investment data, on P1's theoretical solution, or on shuffled P2 labels) to determine whether the improvement stems from the specific content of the P2 theoretical solution or simply from the model learning general task structure (parameter ranges, output format, the concept of time-dependent investment decisions). This is critical because the baseline is an *untuned* model; any amount of task-relevant fine-tuning would likely improve over it. The paper's own framing (Question D: "How to adapt the fine-tuned LLMs to solve the original complex problem?") promises a bridging mechanism that is never explicated — the "adaptation" is simply "fine-tune on P2 data and hope it transfers."

3. **Mentioned experiments are described but not executed.** Lines 235–236 state that the authors "also: 1) supplement smaller samples of real-user data with theoretical solutions to construct a training dataset to improve robustness; 2) compare InvestAgents with LLMs fine-tuned using the baseline FinGPT dataset." No results for either experiment are reported. These are non-trivial ablations that directly bear on the paper's claims, and omitting them makes the paper feel incomplete.

### Minor

1. **Statistical validation of the theoretical solution has methodological gaps.** The paper tests whether the mean correlation differs from 0.85, but provides no justification for choosing 0.85 as the null value. Additionally, "failing to reject" the null hypothesis that the mean difference is zero (t = −1.075) is weak evidence of alignment — it could also arise from limited sample size (119 participants) or high variance. Effect sizes and confidence intervals would be more informative than null-hypothesis tests alone.

2. **Convergence analysis relies on strong simplifications disconnected from the actual implementation.** The derivation assumes: (a) the loss only considers investment decision values, ignoring all language tokens; (b) the LLM's output layer is a Sigmoid unit (rather than a vocabulary-size softmax over subword tokens); (c) real-user noise is additive and uniformly distributed. The paper acknowledges these are simplifications (Section 4.2: "To gain insights and ensure mathematical tractability"), but they sever the connection between the theoretical model and the actual LLM fine-tuning setup used in the experiments, limiting the analysis's force. The claim that the theoretical solution follows a Pareto distribution is stated without derivation.

3. **Influence coefficient elicitation is coarse.** The parameter θ is derived from a single 0–10 Likert question ("how much do you rely on the investment assistant"). The transformation θᵢ = kᵢ × 10⁻⁸ is given without justification for the scaling factor. This introduces measurement noise into the real-user data that serves as ground truth for all evaluations.

4. **No absolute MSE values reported in the text.** The paper reports only percentage reductions (e.g., "45.59%–61.26%") and refers to Table 1 (an image) for absolute values. The reader cannot assess whether the absolute errors are economically meaningful without extracting numbers from a figure.

### Trivial

- The paper references footnotes (superscript 7, superscript 9) for prompts and additional experiment details that do not appear in the extracted text — these are presumably in the original submission's appendix, which the parser strips. Standard practice, but the footnotes should ideally be in the main text.

## Nice-to-Haves

- An ablation on synthetic dataset size (the fixed 1000-sample dataset is not varied) would strengthen the claim about addressing data scarcity.
- Investigating what the model actually learns (e.g., does it approximate the P2 closed-form solution from the prompt parameters, or memorize training samples?) would clarify the nature of the transfer to P1.
- Reporting confidence intervals or significance tests for the MSE comparisons would improve statistical rigor.
- A comparison with models fine-tuned on real P2 data — even a small-sample version — would directly test the "substitute" claim.

## Removed Points

These points were flagged by one or both input reviewers but are removed or downgraded after verification against the paper:

1. **"The central logic of the method is structurally unsupported"** — Removed as overstatement. The paper provides a reasoned argument (mathematically similar problems → transfer is plausible) and empirical evidence. The missing baselines weaken the claim but do not make it "structurally unsupported"; the criticism is addressed more precisely above as incomplete experimental design.

2. **"GPT-3.5 may not appear in fine-tuning experiments"** — Removed. The paper lists GPT-3.5 as one of four studied models. Table 1's caption refers to results across all models. Only the convergence experiment (Section 4.2) explicitly limits to open-source models because gradient access requires it. The criticism is speculative.

3. **"No ablation on dataset size"** — Moved to Nice-to-Haves. Useful but not required.

4. **"No investigation of what the model learns"** — Moved to Nice-to-Haves. Interesting but beyond the paper's current scope.

5. **"Prompt templates are not shown"** — Removed. They are referenced as in the appendix/supplementary material (standard practice), which the parser strips.

6. **Various formatting/style nitpicks** — Removed per instructions (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same set of issues (missing comparisons, weak baselines) from different angles, and no genuinely novel observation emerges from synthesizing them beyond what each reviewer individually stated.

## Suggestions

1. **Add an experiment fine-tuning on real P2 data** (the same size as the synthetic dataset) and compare directly — this is the single most important missing comparison and the only way to substantiate the "substitute" claim.
2. **Add a control condition**: fine-tune on randomly generated investment trajectories or on P1's (expensive but computable) theoretical solution to isolate whether the P2 theoretical solution's specific content drives the improvement over a generic "fine-tuning helps" effect.
3. **Report absolute MSE values and confidence intervals** in the text, not just in a figure.
4. **Provide results for the two additional experiments** mentioned in lines 235–236 (data supplementation and FinGPT comparison), or remove the mention if the experiments were not conducted.

## Score and Decision

This paper proposes a sensible high-level idea — using closed-form solutions to simpler problems to generate training data — and executes a clear, well-organized study from problem formulation through data collection, validation, and empirical evaluation. The strengths include real data validation, multi-model consistency, and a structured approach.

However, the experimental evaluation has critical gaps that prevent the paper from demonstrating its claimed contribution. The most important missing comparison (fine-tuning on real data) means the "substitute for expensive real-user data" claim is untested. The missing control for generic fine-tuning effects means the transfer from P2 to P1 is not convincingly attributed to the P2 theoretical solution's specific content. The additional experiments mentioned but not delivered make the paper feel incomplete. These gaps are significant enough that the paper does not meet the bar for acceptance at a top venue.

The idea has merit and the paper is coherently written, but the experimental validation is insufficient to support the core claims. Substantial additional work (particularly the missing comparisons) would be needed to make a convincing case.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>