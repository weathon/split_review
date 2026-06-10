Now let me produce the final consolidated review.

## Summary

This paper proposes Booster, an alignment-stage defense against harmful fine-tuning in LLMs. The key idea is identifying "harmful perturbation" — taking a gradient step on harmful data — as the mechanism that breaks safety alignment, and designing a regularizer that minimizes the gap between harmful loss before and after a simulated harmful gradient step during alignment. Empirically, Booster achieves substantial harmful score reductions across multiple models (Llama2-7B, Gemma2-9B, Qwen2-7B), datasets, and attack settings while maintaining competitive fine-tune accuracy.

## Strengths

- **Well-motivated and cleanly formalized method.** The objective function (Eq. 1) directly targets the identified mechanism: constraining the reduction in harmful loss after a simulated harmful gradient step. The use of a first-order MAML approximation (dropping the Hessian, leading from Eq. 2 to Eq. 3) is transparent and computationally practical, requiring only three forward/backward passes per step.

- **Consistent and substantial empirical gains across diverse settings.** In Table 1, Booster achieves an average harmful score of 10.94% across harmful ratios p=0.05–0.20, compared to 28.20% (Vaccine) and 31.02% (RepNoise). These gains hold across four downstream tasks (Table 3), three model architectures including Qwen2-7B where Booster achieves 1.6% HS with 95.64% FA (Table 4), and varying sample sizes (Table 2). The generalization to Gemma2-9B is particularly strong evidence that the method is not architecture-specific.

- **Transparent resource reporting and comprehensive ablation.** Table 6 honestly reports that Booster requires 1.86h alignment time (vs. 0.54h for SFT) and 57.86 GB GPU memory, and the paper explicitly frames this as a one-time alignment cost. The hyperparameter ablations (Tables 7–9) systematically characterize sensitivity to λ, α, and number of harmful samples, including failure modes (e.g., λ=100 causing catastrophic collapse), rather than hiding them.

- **Demonstrated combinability with existing defenses.** Table 5 shows Booster can be combined with Vaccine to further reduce harmful score, indicating compatibility with prior alignment-stage methods.

## Weaknesses

### Major

- **No variance or statistical reliability reporting.** Every experimental result (Tables 1–6) is reported as a single point estimate with no standard deviations, confidence intervals, or random seed disclosure. Given that the experiments use LoRA (with random adapter initialization), stochastic optimization (AdamW with batch sampling), and data subsampling, the numbers could meaningfully vary across runs. The paper's central quantitative claims (e.g., "22.64% lower harmful score than SFT on average") cannot be properly assessed without some measure of variability. This is the most significant weakness and must be addressed for the empirical claims to meet the standards of a top venue.

- **Missing empirical comparison with TAR, the closest concurrent method.** The paper cites TAR (Tamirisa et al., 2024) as "concurrent research [that] utilizes a similar meta-learning technique to simulate the harmful perturbation in the alignment stage" (line 57) and acknowledges the methods are related. Yet TAR is never included as a baseline in any experiment. Without this comparison, it is impossible for readers to assess whether Booster's design differences translate to meaningful performance advantages over its closest competitor. The authors should either add TAR as a baseline or provide a detailed explanation of why comparison is infeasible and discuss expected trade-offs.

- **Baseline hyperparameter tuning is not documented.** The paper provides no evidence that Vaccine and RepNoise (the two alignment-stage baselines) were tuned to reasonable settings. RepNoise achieves an average harmful score of 31.02% in Table 1 (only 2.56 points better than unprotected SFT's 33.58%), and is actually *worse* than SFT on Gemma2-9B (43.20% vs. 41.17%) in Table 4. This could reflect suboptimal hyperparameters rather than genuine limitations of these methods. The authors should either (a) document the hyperparameters used and how they were chosen, (b) show that baselines perform comparably to their reported results in the original papers, or (c) acknowledge this limitation explicitly.

### Minor

- **The "harmful perturbation" novelty claim is somewhat overstated.** The paper states "we are the first to identify harmful perturbation as the cause of alignment broken" (line 57). However, the definition — taking a gradient step on harmful data reduces harmful loss — is largely a formalization of the mechanism that the harmful fine-tuning literature (Qi et al., 2023; Yang et al., 2023; Zhan et al., 2023) already establishes: fine-tuning on harmful data degrades alignment. The paper's Figure 1 provides a useful controlled demonstration, but calling this a "discovery" is overselling. The methodological contribution (the regularizer and resulting algorithm) is the genuine novelty; the paper would benefit from toning down the causal discovery claims.

- **The gradient normalization design choice is not discussed.** The regularizer uses a *normalized* harmful gradient step ($\nabla h(\bm{w}) / \|\nabla h(\bm{w})\|$), making the simulated perturbation scale-invariant with respect to gradient norm. Real harmful fine-tuning uses unnormalized gradients, so the simulated perturbation magnitude depends only on $\alpha$, not on the actual gradient scale. This design choice is not justified or discussed, and its implications for the defense's fidelity to real attacks remain unexamined.

- **No discussion of potential risks from using the harmful dataset for alignment.** The method requires the service provider to maintain and train on a dataset of harmful prompt/harmful answer pairs. If the regularizer does not work perfectly, the model could learn harmful patterns from this data exposure. The paper does not discuss this concern or any mitigations.

- **The "3.88% reduction" claim in the Vaccine+Booster experiment (Section 5.5) is ambiguous.** The phrase "3.88% reduction of harmful score" describes an absolute 3.88-point reduction (45.08 → 41.20), not a relative percentage reduction. This wording could mislead a casual reader.

### Trivial

None.

## Nice-to-Haves

- A deeper analysis of why Booster's defense degrades at high harmful ratios (p=0.20, HS=25.50) would strengthen the paper's discussion of limitations.
- A discussion of whether LoRA's low-rank update subspace affects the validity of the harmful perturbation analysis (which is defined on the full weight space) would address a natural question.

## Removed Points

These points were flagged for removal. Treat them with caution:
- **"No discussion of cost model"** (Harsh Critic): The paper *does* discuss this in Section 5.3, explicitly acknowledging the overhead and framing it as a one-time alignment cost. Removed as factually incorrect.
- **"λ sensitivity causes catastrophic collapse"** (Harsh Critic): The paper already discusses this in the hyperparameter analysis (Section 5.4): "When λ is too large, defense performance downgrades." Removed as already addressed.
- **"Learning rate difference not explained"** (Harsh Critic): The paper states it follows Vaccine (line 153), and the method's inner step size α is separately controlled. Removed as already addressed.
- **General capability degradation trade-off not discussed** (Harsh Critic): This is scope creep — the paper evaluates finetune accuracy, which is the relevant capability metric. Removed.
- **Strengths about "first to identify harmful perturbation"** (Strength Finder): Overlap with a verified weakness; the weaker version of this claim is retained. The strength text was merged into the minor weakness about overstated novelty.
- **Strengths that are generic/superficial** (Strength Finder): Dropped strengths that merely praise the paper for addressing an "important problem" without specific evidence.

## Novel Insights

None beyond the paper's own contributions. However, the synthesis reveals that the paper's main empirical contribution (Booster's consistent and large improvements across diverse settings) is stronger than the causal discovery framing suggests. The method's effectiveness is well-demonstrated even if the "harmful perturbation" insight is less groundbreaking than claimed.

## Suggestions

1. **Add variance estimates.** Re-run the main experiments (at least Tables 1 and 3) with 3 random seeds and report means and standard deviations. If computationally infeasible, report the seeds used and add a discussion of expected variance.
2. **Include TAR as a baseline or explain its absence.** This is the most closely related concurrent method and the paper is incomplete without at least an attempted comparison.
3. **Document baseline hyperparameters.** Report how Vaccine and RepNoise hyperparameters were chosen, whether they follow the original papers' recommendations, and ideally show that the baselines are performing near their reported levels.
4. **Tone down the discovery claim.** Replace "first to identify harmful perturbation as the cause" with a more measured statement about formalizing and directly targeting the mechanism.
5. **Justify the gradient normalization choice.** Discuss whether the scale-invariance of the simulated perturbation affects the fidelity of the defense to real attacks.
6. **Address the risk of using harmful data in alignment.** Even a brief discussion would strengthen the paper.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>