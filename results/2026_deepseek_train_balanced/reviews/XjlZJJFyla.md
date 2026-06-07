Now I have all the verification I need. Let me write the consolidated review.

## Summary

The paper proposes PBPrompt, a Bayesian prompt tuning method for vision-language models (CLIP) that combines two ideas: (1) hierarchical generation of label-specific stochastic prompts via variational inference, where a latent vector is sampled from a class-conditional distribution and decoded into prefix tokens by a lightweight self-attention generator; and (2) conditional transport (CT) regularization that aligns the distribution of text prompt embeddings with visual patch embeddings bidirectionally. The method is evaluated on few-shot learning, base-to-new generalization, cross-dataset transfer, and domain generalization across 15 datasets.

## Strengths

- **Principled hierarchical Bayesian generation of label-specific prompts.** The paper models each label as a variational distribution in latent space ($q(\mathbf{r}_c|c) = \mathcal{N}(\mu(\mathbf{e}_c), \Sigma(\mathbf{e}_c))$) and generates prefix tokens via a deterministic decoder, cleanly separating conceptual uncertainty from token generation. The label-specific prior $p(\mathbf{r}_c) = \mathcal{N}(\mathbf{e}_c, I)$ incorporates label semantics into the prior — a concrete design choice absent from CoOp/CoCoOp.

- **Bidirectional CT regularization with a clear motivation against mode collapse.** The CT distance (Eq.~7–10) includes both a patch-to-prompt term ($\mathcal{L}_{\mathbf{u}\rightarrow\mathbf{g}}$, clustering effect) and a prompt-to-patch term ($\mathcal{L}_{\mathbf{g}\rightarrow\mathbf{u}}$, covering effect), which together prevent the stochastic prompts from collapsing to a single mode. This is a substantive methodological advance over PLOT, which uses OT to learn multiple local prompts but lacks bidirectional regularization. The ablation (Tables 5 and 6) confirms that both directions contribute and that the combined model outperforms either variant alone (e.g., Caltech101 H: B-Prompt 96.16, P-Prompt 95.47, PBPrompt 96.74).

- **Ablation studies directly isolate the contribution of each component.** The paper explicitly compares the SPG-only variant (B-Prompt) and CT-only variant (P-Prompt) against the full PBPrompt on both few-shot learning (Table 5) and base-to-new generalization (Table 6). The consistent pattern that PBPrompt > max(B-Prompt, P-Prompt) provides direct evidence that the two mechanisms are complementary and that the combined ELBO objective is effective.

- **Evaluation across multiple standard benchmarks and two backbones.** The paper covers 11 datasets for few-shot/base-to-new, 10 target datasets for cross-dataset transfer, and 4 domain-shifted variants of ImageNet. Results are reported for both ViT-B/16 and RN50 backbones (Table 5), showing that PBPrompt does not suffer the performance drop that PLOT exhibits on ViT-B/16.

- **Domain generalization improvements are consistent across all four distribution shifts.** Table 3 shows PBPrompt achieves the highest accuracy on ImageNetV2 (+0.46 over CoCoOp), ImageNet-Sketch (+0.57), ImageNet-A (+1.01), and ImageNet-R (+0.53). While the margins are small, the pattern is uniform across all shifts.

## Weaknesses

### Major

- **Factual error in a central claim, contradicted by the paper's own data.** Line 186 states: *"We find that PBPrompt surpasses other stochastic baselines in terms of H score across all datasets."* This is false. In Table 6 (base-to-new), on the DTD dataset, ProDA achieves an H score of 66.44 while PBPrompt achieves 66.42 — PBPrompt is lower. The claim of superiority *"across all datasets"* is directly contradicted by the numbers in the same paper. This is not a rounding issue (the numbers differ in the hundredths place). An empirical paper making an absolute claim that is immediately falsified by its own reported results has a credibility problem that requires correction.

- **The most directly relevant stochastic baselines are absent from key experimental settings.** The paper's motivation is that prior stochastic prompt methods (ProDA, VPT, SHIP) have shortcomings, and PBPrompt is itself stochastic. Yet in three of four experimental settings, these most comparable methods are missing:
  - **Cross-dataset transfer (Table 2):** only CoOp and CoCoOp are compared. ProDA, VPT, SHIP, and PLOT are absent.
  - **Domain generalization (Table 3):** only CLIP, CoOp, and CoCoOp are compared. All stochastic baselines are absent.
  - **Few-shot learning (Fig.~1):** CoOp, CoCoOp, and PLOT are shown; ProDA, VPT, and SHIP are absent from the main figure.
  
  The base-to-new table (Table 6) is the only setting where all baselines appear. If PBPrompt cannot match or outperform ProDA/VPT/SHIP on cross-dataset transfer and domain generalization, the contribution is considerably narrower than claimed. The reader cannot tell because the data is not shown.

- **No measure of variance reported, despite very small margins.** Results are reported as "mean value over three seeds" (line 149) with no standard deviations, confidence intervals, or any variability metric. This is a critical omission because the reported improvements are consistently <1% in the cross-dataset and domain generalization settings (e.g., +0.66% average over CoCoOp across 10 datasets; +0.46 to +1.01 on domain shift variants). With only 3 seeds and no error bars, the reader cannot distinguish between genuine but small improvement and random seed variation, making the quantitative evidence uninterpretable for these settings.

### Minor

- **Dimensional inconsistency in the self-attention generator affects reproducibility.** The paper states (line 70) that $\phi$ outputs $b$ prefix tokens, but the actual formulation (Eq.~5, line 77) produces $b+1$ outputs ($[\hat{\mathbf{r}}_c, \mathbf{v}_{c,1}, ..., \mathbf{v}_{c,b}]$). Line 80 explicitly calls this $b+1$-length sequence "the class-specific prefix sequence." The final prompt then concatenates $\phi$'s output with the class embedding $\mathbf{e}_c$, producing $b+2$ total tokens, whereas CoOp uses $b+1$ ($b$ prefix + class embedding). It is unclear whether $\hat{\mathbf{r}}_c$ is included as an additional prefix token or discarded, and whether $b$ in the self-attention formulation refers to the same $b$ as the prompt length (stated as 4). This ambiguity must be resolved for the method to be reproducible.

- **"Further ablation study" (lines 320–324) consists almost entirely of references to appendix sections.** The paragraph states that "neither of these two terms can be omitted" and that "our method is very tolerant to changes in the harmonic mean" but provides no concrete numbers or findings. All substantive results are deferred to appendix sections (Sec.~\ref{sec: balance}, Sec.~\ref{tab: trade_off}, Sec.~\ref{sec: more}, Sec.~\ref{sec: cost}) that are not present in the main paper. The reader cannot evaluate these claims from the main text.

### Trivial

- The phrase "fix the prompt length as 4 for the four primary image classification tasks across all datasets" (line 146) is unclear — the paper covers 11 datasets across multiple task categories, making it ambiguous what "four primary" refers to.

## Nice-to-Haves

- A computational cost comparison (training/inference overhead) relative to baselines would strengthen the practical contribution.

- The CT formulation (Eq.~6) defines $Q$ using predicted probabilities $p_c$, making the alignment loss image-dependent. This creates a potential self-reinforcing loop: peaked predictions concentrate CT weight on one class, which could counteract the regularization goal. The paper does not discuss this interaction.

## Removed Points

The following points raised in the reviews are removed with justification:

- **Criticism about "fundamentally distinct" claim being oversold** (harsh critic): This is a subjective assessment of framing, not a concrete weakness. The paper clearly delineates its differences from prior work.
- **Criticism that the paper "over-claims novelty" vs VPT/ProDA**: The paper acknowledges these methods and states they are "fundamentally distinct" in terms of the hierarchical generation vs. direct noise addition — this is a reasonable distinction to draw.
- **Strength Finder's claim that the paper "addressed an important problem"**: Generic; not a specific, evidence-backed strength.
- **Criticism about missing related works**: Cannot be verified without external knowledge; excluded per instructions.
- **Formatting and parser artifact complaints**: Excluded per instructions.
- **Speculation about whether appendix content exists or was stripped**: Excluded per instructions.
- **The "four primary" criticism as a formatting/presentation issue**: Could be a parser artifact; downgraded to Trivial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the factual error** on line 186. Either soften the claim to "surpasses other stochastic baselines on most datasets" or explicitly acknowledge the DTD exception.
2. **Complete the baseline comparisons** by reporting ProDA, VPT, and SHIP results for cross-dataset transfer and domain generalization. If these numbers are already in the appendix, move them to the main paper.
3. **Report standard deviations** for all results, especially given the sub-1% margins in the cross-dataset and domain generalization tables.
4. **Clarify the dimensional ambiguity** in the self-attention generator: specify whether $\hat{\mathbf{r}}_c$ is part of the prefix and how many total tokens the prompt contains.
5. **Move concrete findings from the appendix into the main text** for the "Further ablation study" section, or remove the paragraph if the appendix is not accessible.

## Score and Decision

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>