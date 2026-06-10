## Summary

This paper identifies and formalizes a previously unrecognized cause of optimization failure in reinforcement finetuning (RFT) of language models: the expected gradient for an input vanishes when its reward standard deviation under the model is small, regardless of whether the expected reward is near-optimal. The paper proves this theoretically (Theorem 1), demonstrates its prevalence across the GRUE benchmark, validates the mechanism through controlled experiments that eliminate exploration confounds, proves an exponential optimization-time separation for a simplified setting, and explores practical mitigation strategies — finding that partial SFT (as few as 1% of labeled inputs) suffices to overcome the problem.

## Strengths

1. **Theorem 1 provides a rigorous, generalizable theoretical foundation (Section 3, Eq. 2):** The bound $\|\nabla_\theta \mathcal{R}(\mathbf{x};\theta)\| \leq 6 L_{out} \gamma(\mathbf{x};\theta) \cdot \text{std}[r]^{2/3}$ establishes a mathematical link between low reward variance and vanishing gradients that is strictly more general than the known near-deterministic-distribution special case (explicitly distinguished at lines 199–204). The paper correctly argues this distinction matters for language models, which rarely produce near-deterministic outputs.

2. **Controlled experiments cleanly isolate the mechanism from exploration confounds (Section 4.2, Figure 3):** By designing environments where expected gradients can be computed exactly (not estimated), the paper rules out the well-known exploration challenge in large action spaces as the sole explanation. Even under perfect exploration, RFT fails for low-std inputs across MLP/MNIST, ResNet18/CIFAR10, and BERT-mini/STS-B, while SFT succeeds.

3. **Multi-level empirical validation bridging theory to practice (Section 4.1–4.3):** The GRUE benchmark analysis (Figures 1–2, Table 1) shows that the 10th-percentile of pretrain reward std predicts RFT-vs-SFT reward gaps across 7 datasets (Pearson correlations of 0.48/0.46 for RFT vs. 0.05/0.16 for SFT on NarrativeQA/ToTTo). The theoretical analysis in Section 4.3 proves an exponential separation ($\Omega(1/\sigma^2)$ for RFT vs. $O(\log(1/\sigma))$ for SFT) in a simplified linear setting, showing the problem is not merely a slowdown.

4. **Partial SFT finding is practically impactful (Section 5.2, Figure 4):** SFT on as few as 1% of labeled inputs with 40% of optimization steps allows RFT to reach 96% of the reward achieved with full SFT. This is a concrete, actionable result with direct implications for reducing data labeling costs in RFT pipelines.

5. **Conventional heuristics systematically tested and shown inadequate (Section 5.1, Table 2):** The paper tests increased learning rates, temperature scaling, and entropy regularization — all of which fail to improve upon default RFT (train reward ~0.10 vs. SFT+RFT achieving 0.54 on NarrativeQA). This rules out trivial fixes and strengthens the case that the problem requires a more fundamental solution.

## Weaknesses

### Fatal

None.

### Major

1. **The causal link between SFT and std-increase remains correlational, not directly tested (Section 5.2):** The paper's central explanatory narrative at the solution level is that SFT helps *because* it increases reward std, thereby alleviating vanishing gradients. However, the evidence for this is correlational: SFT increases std, and subsequent RFT performs better. An alternative hypothesis — that SFT simply moves the model's output distribution closer to good outputs, reducing the distance RFT must traverse, independent of the std effect — is not directly ruled out. The partial SFT experiments (showing 1% of data suffices) are consistent with the std-focused mechanism but do not constitute a causal test. A direct intervention (e.g., artificially increasing reward std without changing the output distribution, or showing that the amount of std increase predicts the degree of RFT improvement at varying SFT budgets) would substantially strengthen this claim. The paper's language is appropriately cautious ("suggest," "can help"), but the narrative arc frames std increase as the explanatory mechanism, and this remains unvalidated at the causal level.

### Minor

1. **No empirical quantification of the $\gamma(\mathbf{x};\theta)$ term in Theorem 1 (Section 3):** The upper bound depends multiplicatively on $\gamma$, the maximum Jacobian spectral norm over all positions and prefixes. For deep neural networks, this term could be large, making the bound potentially loose for non-zero but small std. The empirical results (Figures 1, 3) confirm the phenomenon holds in practice despite this, but reporting empirical estimates of $\gamma$ for the GPT-2 and T5-base models used would allow readers to assess how tight or loose the bound actually is in the relevant regime.

2. **Reward std estimates based on only 10 generations per input (Section 4.1, Figure 1):** The scatter plots estimate reward std from 10 samples per input. With such a small sample size, these estimates have high variance. Since reward std is the paper's central explanatory variable, noisy estimates could blur the relationship between true std and gradient vanishing. Confidence intervals or at least a discussion of estimation noise would strengthen the analysis.

3. **Gap between controlled experiments and autoregressive RFT (Section 4.2):** The controlled experiments use classification settings (MNIST, CIFAR10, STS-B) with atomic label outputs rather than autoregressive token-by-token generation. They are explicitly designed to rule out exploration confounds, which is a valid scientific strategy, but the gap between these simplified settings and real RFT (where the $L_{out} \gamma$ chain-rule structure from Theorem 1 is present) is wider than the prose acknowledges. The GRUE experiments bridge this gap, but the paper could more clearly articulate what each evidence type contributes to the overall case.

### Trivial

None.

## Nice-to-Haves

- A direct plot linking the amount of std increase from partial SFT (at varying data fractions) to the subsequent RFT reward gain would test whether std increase is the mechanism, rather than merely correlated with SFT.
- A brief discussion of why the exponent in Theorem 1 is $2/3$ rather than $1$ (which the intuitive gradient expression $(r - V) \cdot \nabla \log p$ might suggest) would be illuminating, even if a tightness analysis is left for future work.
- Quantitative analysis (e.g., a table) of how the 10th percentile of reward std changes after partial SFT at various data fractions, rather than only a qualitative/appendix visualization.

## Removed Points

*The following points from the reviews were removed under the filtering rules; they are preserved here only for completeness and should be treated with caution:*

- **"Theorem 1 provides only an upper bound, leaving a looseness gap that the paper does not address"** — Removed because Theorem 1 is an upper bound by design; it proves that as std → 0, the gradient → 0. This is sufficient for the claimed result. The bound being one-sided is standard, and the practical relevance is confirmed empirically.
- **"Controlled experiments do not capture autoregressive generation"** — Removed because the paper's evidence is multi-pronged: the GRUE experiments (Section 4.1) DO involve autoregressive generation. The controlled experiments are scoped to rule out exploration confounds where exact gradient computation is feasible. The combination supports the overall claim.
- **"Missing appendix proofs / missing related works / formatting nitpicks"** — Removed per instructions (parser artifacts, presumed absent due to extraction, or outside scope).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a direct causal test of the SFT-std-RFT link: for a GRUE dataset, perform SFT to varying degrees, measure (a) the increase in the 10th percentile of reward std, (b) the subsequent RFT reward gain, and plot (b) vs. (a) to show that std increase predicts RFT improvement.
2. Report empirical estimates of $\gamma$ (maximum Jacobian spectral norm) for the models used, to assess bound tightness.
3. Discuss the estimation noise from 10-sample std estimates and consider adding confidence bands to the scatter plots.
4. Add a brief note on why the exponent in Theorem 1 is $2/3$ rather than $1$, to preempt reader questions about tightness.

## Score and Decision

This paper makes a genuine contribution by identifying and formalizing a previously unrecognized optimization obstacle in RFT. The theory is clean and well-proved, the empirical design is multi-pronged and thorough, and the partial SFT finding has immediate practical value. The main weakness is that the causal mechanism at the solution level (SFT → increased std → better RFT) is correlational rather than directly tested, and the bound's dependence on $\gamma$ is unquantified. These are real but not fatal — the overall evidence base is sufficient to establish the phenomenon and its practical relevance.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>