Now I have a thorough understanding of the paper. Let me compile the final review.

## Summary

This paper investigates whether symbolic or black-box representations generalise better in learned optimisation for reinforcement learning. It introduces an LLM-based evolutionary pipeline to discover hyperparameter-free symbolic optimisers, enabling a like-for-like comparison with OPEN, a pretrained black-box optimiser. The authors evaluate generalisation across four axes (training length, network size, activation function, and unseen environments) and find that symbolic optimisers scale better out-of-distribution while OPEN performs better in-distribution. The paper also provides a roadmap for future symbolic optimisation research.

## Strengths

- **Fair comparison enabled by hyperparameter-free symbolic optimisers.** The paper explicitly designs symbolic optimisers without tuneable hyperparameters (Abstract, Section 1, Section 4), removing the many-shot vs. zero-shot confound that has complicated prior comparisons between symbolic and black-box optimisers. This is a genuine methodological contribution.

- **Comprehensive generalisation evaluation across multiple axes with proper statistics.** The paper evaluates on four distinct generalisation axes (training length, network size, activation function, unseen environments) using IQM with 95% stratified bootstrap confidence intervals from 16 seeds (Figures 3–5, Section 8). The results consistently show symbolic optimisers scaling positively where OPEN collapses — the first systematic like-for-like evidence in this setting.

- **Two-LLM discovery pipeline with separate reasoning and implementation.** The pipeline splits mutation into a "thinker" (proposes changes) and a "coder" (implements them faithfully), preventing proposal–implementation mismatch common in single-LLM approaches (Section 5.3.2). This is a well-motivated design improvement over earlier LLM-based discovery methods.

- **Scale-invariant selection via per-environment ranking.** Using average per-environment rankings instead of raw returns avoids reward-scale bias across environments and weeds out optimisers that overfit to a single environment (Section 5.3.1). This is a principled solution to a nontrivial aggregation problem.

## Weaknesses

### Fatal
None.

### Major

- **Single discovery run and single black-box instance.** The entire comparison rests on one symbolic discovery trajectory and one pretrained OPEN model. Neither the variability of the LLM-based evolutionary process nor the representativeness of this particular OPEN checkpoint can be assessed. The paper acknowledges this (Section 10: "Due to limited resources, we are only able to experiment with a single discovery run and a single learned black-box optimiser") but the central claim — that symbolic representations generalise better than black-box ones — demands evidence across repeatable discovery processes. The experimental evaluation is internally rigorous (16 seeds, IQM, 95% CIs), but the meta-level N=1 design means the comparative conclusions are preliminary. The paper would be more accurately framed as a case study of a particular discovery pipeline's outputs rather than a definitive comparison of representation classes.

### Minor

- **Potential mismatch between symbolic and OPEN meta-training environments.** The paper states it meta-trains on four MinAtar environments under the "Multi-Task Training" setting (line 97, line 174). However, the pretrained OPEN model "available online" (line 245) may have been trained on a different set of environments (e.g., five MinAtar environments including Seaquest, per Goldie et al. 2024). The paper does not verify whether the distributions match, so differences in generalisation could partially reflect a mismatch in meta-training distributions rather than a fundamental property of the representation class. This should be clarified.

- **Alternative interpretation of scaling results not discussed.** Figures 3 and 4 show symbolic optimisers improving with longer training and larger hidden sizes beyond the in-distribution point (1e7 transitions, hidden size 64). The paper interprets this as "symbolic optimisers do not overfit as strongly" (Section 9). However, an equally plausible interpretation is that the symbolic optimisers were undertrained at the in-distribution point — they may simply have more headroom to improve — while OPEN had already converged. The paper does not discuss this confound.

- **Missing implementation details for reproducibility.** The paper leaves unspecified the number of refinement steps *N*, the number of generations, the population size, the total number of LLM calls, and the exact set of hand-crafted initial optimisers (Section 5). These details affect reproducibility and the ability to calibrate the computational cost of symbolic discovery against OPEN's meta-training.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis of Adam's learning rate would strengthen the baseline comparison. The paper uses a fixed LR=1e-3 without exploring whether other values would change the qualitative patterns.
- Including the discovered optimiser code as a short snippet in the main body (beyond the appendix) would make the paper more self-contained and its primary outputs directly inspectable.

## Removed Points

These points were considered and removed, with justification:

1. **"Discovered optimisers not fully presented in main text"** (Harsh Critic #4) — The parser strips appendix content. The paper explicitly states "Below, we show the three highest average rank discovered optimisers" (line 174); the code appears in the appendix which is present in the original submission. Per instructions, this is a parser artifact.

2. **"Figure 5 conclusion unsupported"** (Harsh Critic, Section-by-Section) — The paper itself states "it is difficult to determine whether black-box or symbolic optimisers are more robust to changes of activations. Seemingly, all optimisers are overfit to their training activation" (line 274). The critic's claim that the paper draws a strong conclusion from this figure is factually wrong.

3. **"Abstract claims too strong"** (Harsh Critic) — The abstract says "we build a pipeline… enabling a fair comparison… Based on our analysis, we propose suggestions." This is appropriately measured. The paper does not claim a settled finding in the abstract.

4. **"Missing statistical significance at meta-level"** (Harsh Critic) — The paper already uses IQM with 95% stratified bootstrap CIs (Agarwal et al., 2021) for inner-loop evaluation, which is standard practice in this community. The critic's suggestion of bootstrapped confidence intervals is already implemented.

5. **"Adam hyperparameter sensitivity"** (Harsh Critic, Places to Improve) — This is a reasonable suggestion for additional analysis but not a weakness of the current paper. Adam with fixed standard hyperparameters is a standard baseline.

6. **"LLM stochasticity not analyzed"** (Harsh Critic, Limitations) — The paper acknowledges using a single closed-source LLM (GPT-4o) in the limitations section. Additional seed analysis for LLM calls would be interesting but is not standard practice.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the alternative interpretation that symbolic optimisers' better scaling could reflect underfitting at the in-distribution point rather than superior generalisation. This is a meaningful alternative hypothesis that the paper should address directly. The harsh critic also correctly notes that combining both reviewers' perspectives reveals a deeper tension: the paper simultaneously claims (a) symbolic optimisers are simpler and thus less prone to overfitting, and (b) they need more training/hidden size to reach their potential. These two claims are in mild tension if "simpler" implies faster convergence, and resolving this would strengthen the analysis.

## Suggestions

1. **Temper the comparative claim or add meta-seeds.** The highest-leverage improvement is either (a) running 3–5 independent symbolic discovery runs to estimate variability, or (b) reframing the paper as a case study of a particular pipeline's outputs rather than a definitive answer to "which representation class generalises better." Option (b) requires no additional experiments — just adjusting the title, abstract, and conclusion to match the evidence.

2. **Clarify the OPEN pretrained model's training distribution.** Verify and report whether the online OPEN checkpoint was trained on the same four MinAtar environments used for symbolic discovery. If there is a mismatch, discuss how it affects the comparison.

3. **Discuss the undertraining alternative hypothesis.** Acknowledge that the symbolic optimisers' improvement with longer training/larger hidden size could partly reflect insufficient in-distribution training, and state what evidence (if any) rules this out.

4. **Report the discovery pipeline's computational budget.** Include the number of generations, refinement steps *N*, population size, total evaluations, and total LLM calls in the main text to allow readers to calibrate the comparison.

## Score and Decision

This paper tackles an important and timely question with a well-motivated experimental design. Its core contributions — the hyperparameter-free symbolic discovery pipeline and the systematic generalisation evaluation — are valuable. However, the central comparative claim rests on a single discovery run and a single black-box instance, which is insufficient for a definitive conclusion. The paper should be accepted if the claims are tempered to match the preliminary nature of the evidence, or strengthened with additional meta-seeds otherwise.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>