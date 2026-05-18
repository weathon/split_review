Here is my consolidated review after careful cross-verification against the paper:

---

## Summary

This paper proposes PIT (implicit self-improvement), a framework that enables LLMs to learn to improve their own responses without explicit rubrics. PIT reformulates RLHF: instead of maximizing absolute response quality, it maximizes the *quality gap* between the generated response and a reference response, conditioned on the input. The reference response is progressively hardened via curriculum RL (first round on ground-truth preference pairs, second round on policy-sampled responses). Experiments on Anthropic/HH-RLHF, OpenAI/Summary, and a synthetic dataset show that PIT improves response quality and outperforms prompting-based Self-Refine.

## Strengths

1. **Novel and principled approach to rubric-free self-improvement.** The paper clearly identifies the bottleneck of prompting-based self-improvement—manually defining comprehensive rubrics is expensive and often infeasible (Section 1). PIT elegantly sidesteps this by reusing the same preference data that trains reward models, learning an implicit improvement objective. This is a genuine conceptual contribution.

2. **Empirical evidence across multiple datasets and evaluators.** Table 1 shows that PIT consistently improves original responses across all three datasets, evaluated by both GPT-4 and a DeBERTa reward model (Δ ranging from 7.2% to 33.59%). This provides converging evidence that PIT achieves its primary goal of quality improvement.

3. **Controlled ablation demonstrating the necessity of curriculum RL.** Table 2 and Figure 4 clearly show that using only Round 0 or only Round 1 of curriculum RL yields marginal or negative improvement (Δ = 0.0% and 1.7% respectively vs. 13.0% for full PIT). This validates the claim that the two-round curriculum is essential and is the strongest experimental contribution of the paper.

4. **Temperature and iteration analysis adds practical depth.** Figure 3 shows PIT improves most at low temperatures (0.4–0.6) and outperforms Self-Refine at nearly all temperatures (up to 9.2% at optimal temperatures). Table 3 honestly reports that response quality does not monotonically increase with iterations, and the paper correctly cautions that stop conditions need careful design—a credible and useful finding.

## Weaknesses

### Fatal
None.

### Major

1. **Human evaluation—the arbitrator of the central comparison—is critically under-reported.** The paper's main claim (PIT > Self-Refine) hinges on human evaluation because GPT-4 and DeBERTa disagree: GPT-4 favors Self-Refine (+3.91%), DeBERTa favors PIT (+3.70%). The paper then states: "we conduct human evaluations to determine which is better and find that human prefers PIT more (23.53% better than Self-Refine)." This single sentence contains no information about: number of annotators, inter-annotator agreement, test set size, how the comparison was presented to annotators, or what instructions they received. The claim that "DeBERTa correlates more closely with human preferences than GPT-4" rests entirely on this one evaluation on one dataset. For a paper whose main quantitative comparison depends on resolving an evaluator disagreement, this is insufficient. The human evaluation covers exactly one of the central comparisons, leaving the rest of the results relying on unvalidated automatic evaluators.

2. **Training hyperparameters are absent, undermining reproducibility.** The paper uses PaLM 2 (Bison) with multi-round RL but never specifies: model size (parameter count), learning rate, batch size, number of PPO steps, KL penalty coefficient β, or number of training steps per RL round. For a method whose optimization difficulty is central to the paper's narrative (curriculum RL is needed because the second round is "too hard to be optimized directly"), these details are not trivial—they directly affect whether the curriculum claim holds under different settings. The reader cannot reproduce or assess the robustness of the training pipeline.

### Minor

1. **Synthetic dataset is never described.** The synthetic dataset is used for Figure 2 (reward distribution analysis), Table 1 (main results), and temperature analysis. Yet the visible text contains no description of what task it involves, how preference pairs were constructed, its size, or the model that generated the responses. The paper says "this conclusion does not hold on synthetic data, which is expected since a much larger LLM produces y_w" and "we only evaluate the instruction following ability," but these scattered hints do not constitute a description. Without knowing what the synthetic dataset measures, the reader cannot interpret results on it.

2. **Reward model loss design (Equation 2) is not ablated.** The paper states "we find Equation 2 is the best fit" for the reward gap loss, but provides no comparison against simpler alternatives (e.g., using the difference of two independently trained reward model scores). Given that the reward model is central to the RL training signal, this gap weakens the claim that the specific formulation is important.

3. **Confidence intervals or standard deviations not reported for key metrics.** Win-rate differences in Tables 1 and 2 and ELO scores in Table 3 are reported as point estimates without variance. The paper acknowledges that ELO order can change with shuffling but does not quantify the uncertainty. While single-run evaluations are common in this setting, given that the evaluators themselves disagree on the central comparison, readers need a sense of statistical reliability.

4. **Computational overhead claim needs qualification.** The paper says PIT "does not bring extra computational overhead compared with... Self-Refine" (Section 3.5). This is arguably true at *inference time* (PIT: original + improvement = 2 calls vs. Self-Refine: original + feedback + improvement = 3 calls), but PIT requires substantial training compute (SFT + RM training + two rounds of RL) that Self-Refine does not. The paper should clarify this distinction.

### Trivial
- The human evaluation result (23.53%) appears to be the difference in win rate; this should be stated explicitly rather than leaving it ambiguous.
- The ELO computation is referenced to Zheng et al. (2023), but details like the initial rating and K-factor are missing.

## Nice-to-Haves
- An ablation comparing Equation 2 against a simpler reward gap computed as the difference of two standard reward model scores (R_P).
- A more extended human evaluation covering at least one additional comparison (e.g., on the synthetic dataset or OpenAI/Summary) with full reporting of annotator counts and agreement.
- Reporting variance estimates (e.g., bootstrap confidence intervals) for win-rate and ELO metrics.

## Removed Points
These points are flagged to be removed; treat them with caution:

- **Self-Refine prompt not disclosed:** The harsh critic argues the Self-Refine prompt is never provided. The prompt text would naturally appear in the appendix (which the parser strips from all papers). The paper does describe the Self-Refine procedure. Per the hard rule about parser-stripped appendix content, this criticism is removed.
- **Section 4.1 is empty:** The extracted text shows Section 4.1 as empty, which may be a parsing artifact (the reviewer acknowledges this). The synthetic dataset is indeed undescribed in the visible text, which I retain as a Minor weakness above. The pure "Section 4.1 is empty" framing is removed.
- **Missing failure cases / reward hacking discussion:** The paper does not discuss limitations of PIT. While this would improve the paper, it is standard for conference papers to omit explicit limitations sections. Not a genuine weakness.
- **Strength Finder claim #5 ("Rigorous multi-evaluator validation with human resolution"):** Overstated. The human evaluation is a single sentence with no detail, so calling it "rigorous" is inaccurate. Removed from strengths.

## Novel Insights

The most interesting observation from the reviews is the tension between the two automatic evaluators (GPT-4 and DeBERTa) and the structural reason the paper gives for this disagreement: GPT-4 and Self-Refine both use manually written prompts, creating an evaluator–baseline confound that systematically favors the prompting-based method. The paper claims humans break this tie in favor of PIT. This is a plausible and important dynamic, but the human evidence is too thin to fully substantiate it, and the paper does not test whether a differently-prompted Self-Refine or a different LLM-as-judge would produce different outcomes. The real novel insight here is that implicit methods may need different evaluation protocols than prompting-based methods, not just more data.

## Suggestions

1. **Expand and fully report the human evaluation.** Provide: number of annotators, inter-annotator agreement (e.g., Cohen's κ), test set size, annotation instructions, and whether the annotators were shown the responses blind to which method generated them. If possible, extend the human evaluation to at least one more dataset or comparison.
2. **Add a reproducibility section** with all training hyperparameters (learning rate, batch size, PPO steps, KL penalty β value, number of steps per RL round).
3. **Describe the synthetic dataset** in the main text or cite a paper that defines it: what task, how preference pairs are constructed, dataset size, and which LLM generated the responses.
4. **Provide an ablation** for the reward model loss (Equation 2) against a simpler gap computed via two independently trained standard reward models.
5. **Add confidence intervals** (via bootstrapping) for win-rate differences in Tables 1 and 2 and the ELO scores in Table 3.

## Score and Decision

The core idea is valuable and the paper has solid evidence for PIT improving responses. However, the central claim (PIT > Self-Refine) rests on a human evaluation described in a single sentence with no methodological details, and the training pipeline is missing hyperparameters essential for reproducibility. These are significant gaps that prevent the paper from being accepted in its current form, though they are addressable through revision.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>