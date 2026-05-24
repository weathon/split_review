Now I have all the information needed. Here is my final consolidated review.

---

## Summary

This paper proposes SECToR (Self-Education via Chain-of-Thought Reasoning), a method that uses chain-of-thought reasoning as a policy improvement operator to enable self-learning in language models. A 582M ByT5 model, after supervised fine-tuning only on 1–6 digit addition, uses CoT reasoning to generate solutions for longer problems, filters those solutions via a novel Simplify-and-Guess (S&G) decoding procedure and commutativity consistency checks, and then distills them back into the model without CoT. Over 22 self-training iterations, the model reaches 98–100% accuracy on 1–29 digit addition and 88% on 30-digit addition without any ground-truth data beyond the initial 1–6 digit supervised phase.

## Strengths

1. **Novel and well-framed core idea.** The analogy between chain-of-thought reasoning and a policy improvement operator (like MCTS in AlphaZero) is clearly drawn and intellectually compelling. The paper formalizes the self-training loop as: use CoT to solve problems the base policy cannot → distill those solutions into the direct policy → repeat with an improved base policy. This framing cleanly connects the paper to the RL literature and provides a principled motivation.

2. **Identification and targeted mitigation of error avalanching.** The paper names the *error avalanching* phenomenon (Section 2.2) — the compounding of model-generated errors during iterative self-training that has stymied prior work (Star, Impossible Distillation, etc., typically failing after a few steps). Two concrete mitigation strategies are introduced: (a) Simplify-and-Guess (S&G) decoding, which decouples each guess from subsequent reasoning errors by taking majority votes across independent fast-addition guesses after progressive CoT simplifications; and (b) commutativity consistency checks that discard problems where \(a+b\) and \(b+a\) yield different answers. Figure 5 quantifies how each component reduces error rates in generated training data. These are real algorithmic contributions that directly enabled the 22-step self-training run.

3. **Clean empirical demonstration of the central phenomenon.** The paper shows that a 582M ByT5 model, after supervised training on up to 6-digit addition, reaches 98–100% accuracy on 1–29 digit addition problems after 22 self-training steps with no further ground-truth data (Table 1, Figure 3). The model also exhibits generalization beyond the trained range (88% at 30 digits). This constitutes a concrete proof-of-concept that the proposed self-training loop can work — a result that prior work on self-improving language models had not achieved for arithmetic.

4. **Simplify-and-Guess decoding is a concrete algorithmic contribution.** The S&G decoding method (Section 3.3.1, Figure 2) is described clearly and combines least-to-most simplification with multiple independent fast-addition guesses and a majority vote. It is a well-motivated synthesis of ideas from least-to-most prompting and self-consistency, adapted specifically for the self-training data generation setting.

## Weaknesses

### Fatal
None.

### Major

1. **Single training run without variance estimates.** The paper explicitly states "We report the results for a single training run for the 582M parameter model" (Section 4). Self-training loops are known to be fragile — error avalanching can produce collapse even with mitigation measures. Without multiple seeds (at least 3–5) or any discussion of run-to-run variability, the reader cannot distinguish between a reproducible phenomenon and a lucky seed configuration. For a paper whose central claim is that CoT can serve as a *reliable* policy improvement operator, this is an evidential floor issue. The paper would be substantially strengthened by reporting mean accuracy and standard deviation across seeds, and by characterizing any runs that failed.

2. **Missing baselines that would isolate the effect of the iterative self-training loop.** The paper argues that the iterative application of CoT-as-policy-improvement drives improvement. However, the experiments do not rule out simpler explanations:
   - **One-shot distillation baseline:** How does SECToR compare to simply using the initial supervised model (which already generalizes well with CoT, per Figure 1) to generate CoT solutions for all lengths in a single pass, then distilling those into fast addition without any iterative loop? If one-shot distillation achieves similar accuracy, the iterative "policy improvement" framing adds nothing.
   - **Supervised upper bound:** Training the same architecture on ground-truth data for all lengths up to 30 digits would contextualize the results — does SECToR achieve a meaningful fraction of what is possible with full supervision, or does it merely scrape by?
   - **Commutativity ablation on final accuracy:** Figure 5 shows that commutativity checks reduce error rates in *generated data*, but the paper does not report final model accuracy *without* the commutativity check. A reader cannot tell whether this component is essential for the final 98–100% result or merely a minor improvement.

   Without these comparisons, the accuracy curve over iterations (Figure 3) could be produced by mechanisms other than the claimed policy improvement loop (e.g., simply training on more high-quality CoT-generated data, regardless of iteration structure).

### Minor

3. **Coarse accuracy reporting per digit length.** Table 1 groups 1–29 digits into a single "98–100%" bin. This binning obscures whether accuracy is flat or decaying within that range (e.g., 100% for 1–10 digits, 99% for 11–20, 95% for 21–29 would all be consistent with "98–100%"). While Figure 3 provides per-length information as a heatmap, a per-digit accuracy table (e.g., every 5 digits) with sample counts would allow readers to assess the uniformity of performance. This matters particularly at the boundary where self-training terminated (28 digits): does accuracy drop sharply at 28 compared to 20?

4. **Robustness of the CoT length generalization precondition is underexplored.** The entire self-training loop depends on the 582M model's ability to generalize from 1–6 digit CoT training to 7-digit CoT problems (Figure 1). This is shown for one model of one size. If smaller models or different seeds during supervised training fail to exhibit this generalization, the entire SECToR pipeline would not start. Reporting whether this generalization holds across multiple supervised training seeds and whether smaller models also exhibit it would clarify the method's preconditions. This is a concern about generality but not about internal validity of the reported results.

5. **No sensitivity analysis for K (S&G hyperparameter).** K=5 is used for S&G decoding (Section 3.3.1) with the justification "was found to be a good balance between computational speed and accuracy." No experimental support (e.g., K=1,3,5,10) is provided. This matters because the quality of generated training data — and therefore the success of the self-training loop — depends on this parameter.

### Trivial

- The "22 steps of self-improvement" claimed in the abstract and results (line 115, line 311) is stated only in prose and never explicitly annotated in a figure. Consider adding step numbers to Figure 3's axes or caption.
- The paper reports "98–100%" for 1–29 digits, but the model was trained on only up to 28 digits. The fact that 29-digit accuracy (one digit beyond training) is also 98–100% is a noteworthy generalization result that deserves explicit commentary rather than being merged into the bin.

## Nice-to-Haves
- An analysis of error modes (e.g., single-digit carry errors vs. complete failures) at different digit lengths would give insight into whether the model is learning genuine addition procedures or exploiting shallow patterns.
- Reporting the volume of generated training examples and rejection rates from commutativity checks would help assess data efficiency and the noise level in the self-training data.
- A comparison to other CoT-based self-training methods (e.g., Star, Huang et al. 2022) on the same addition task, even if those methods plateau quickly, would anchor the improvement.

## Removed Points
These points were flagged by reviewers but are removed from the final assessment with brief justification:

- *"The paper does not state how many training examples were used at each digit length"* and *"hyperparameters are not disclosed"* — The paper explicitly references Appendix Section `sec:hyperparameters` for these details. The appendix was stripped by the PDF parser; the details exist in the original submission.
- *"y-axis labels are not readable in the teaser figure"* — This is a formatting artifact of the PDF extraction, not an author error.
- *"It is unclear whether the model is also trained on slow addition for new digit lengths during self-training"* — The paper states this clearly: "Model accuracy both with and without chain-of-thought continues to grow after self-training begins" (Figure 3 caption), and Section 3.3 separately describes generating both fast and slow training data.
- *"The abstract claims 98+% for up to 28-digit but table shows 1–29 digits"* — The model was trained up to 28 digits via curriculum; 29 digits is an extrapolation length that still achieves 98–100%. The abstract and table are consistent, and the merged bin actually understates the generalization result.
- *Missing related works* — Per instruction, I cannot evaluate the completeness of the related work section without external sources.
- *Various reproducibility concerns about undisclosed hyperparameters, implementation details, or large artifacts* — These are either in the stripped appendix or are minor details inappropriate to penalize for a proof-of-concept paper.

## Novel Insights
None beyond the paper's own contributions. The reviewer inputs did not surface any observation that the paper itself does not already state or imply.

## Suggestions
1. **Run multiple seeds.** Report mean and standard deviation of accuracies over 3–5 training runs, and characterize the failure rate and modes. This is the single highest-leverage improvement.
2. **Add the three key baselines:** (a) one-shot CoT distillation without iterative refinement, (b) supervised upper bound on all lengths, (c) SECToR without commutativity checks. These directly test whether the "policy improvement operator" framing is causally responsible for the results.
3. **Report per-digit-length accuracy** in the main table (e.g., every 5 digits from 1–30) to replace the coarse 1–29 bin. Explicitly note the 29-digit generalization result.
4. **Add a sensitivity analysis for K** in S&G decoding, even if only in an appendix.
5. **Discuss run-to-run variability explicitly** in the limitations section, acknowledging that only one run was performed.

## Score and Decision

This paper presents a genuinely novel and well-motivated idea — using chain-of-thought reasoning as a policy improvement operator for self-learning in language models — and provides an impressive proof-of-concept on the addition task with 22 steps of self-improvement, carefully designed error mitigation strategies, and clear exposition. However, the experimental evidence is thinner than needed to fully support the central claims: a single training run without variance estimates, missing baselines that would isolate the effect of the iterative loop from simpler alternatives, and coarse accuracy reporting. These omissions leave the paper as a suggestive demonstration rather than a fully convincing one. While the contribution is real and the research direction is important, the paper needs stronger empirical grounding to warrant acceptance at a competitive venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>