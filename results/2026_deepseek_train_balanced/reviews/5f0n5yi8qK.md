Now I have all the evidence needed to produce the final merge review.

---

## Summary

This paper proposes using video instructions (instead of text) combined with a "dual-pathway encoder-decoder" architecture (adding intention-aware cross-attention) for online PPO fine-tuning of a video-conditioned policy (GROOT) in Minecraft. The authors identify a "latent vocabulary overfitting" problem where the latent bottleneck $z$ memorizes training tasks, and introduce a secondary visual pathway to provide fine-grained visual features alongside the semantic pathway. They evaluate on three task categories (MineBlock, CraftItem, KillEntity) and report zero-shot generalization to unseen tasks.

## Strengths

1. **Specific mechanistic diagnosis of a real problem.** The paper identifies a concrete failure mode for online fine-tuning of video-conditioned policies: the latent $z$ in the encoder-decoder has limited dimensionality shaped during pretraining for action prediction, so online fine-tuning on a few tasks forces $z$ dimensions to encode task-specific "vocabulary" that fails on unseen tasks (Section 3.3, lines 75–78). This goes beyond generic "overfitting" and offers a testable hypothesis.

2. **Dual-pathway architecture directly targets the diagnosed bottleneck.** The proposed architecture adds an intention-aware cross-attention layer that creates a separate visual information channel using observation and instruction patches, while preserving the original semantic pathway through $z$. This design is a concrete architectural extension beyond GROOT's simpler encoder-decoder, motivated by a specific failure mode (Section 3.3, lines 82–91).

3. **Ablation partially disentangles architecture from modality.** The ablation (Section 4.4, Figure 6) compares PPO fine-tuning of STEVE-1 (text instructions) and STEVEv (video instructions) against the proposed method on MineBlock tasks, showing the proposed method outperforms both. This provides some evidence the architecture contributes beyond merely switching to video modality, though the comparison is across different base models (STEVE-1 vs. GROOT).

4. **Diagnostic task design.** The three task categories (MineBlock, CraftItem, KillEntity) are designed to probe different generalization challenges — viewpoint invariance, fine-grained visual discrimination, and subtle appearance differences — which is more informative than a single aggregate metric.

## Weaknesses

### Fatal
None.

### Major

1. **Train/test task split is never specified, making the zero-shot generalization claim unverifiable.** The paper claims zero-shot generalization to "unseen tasks" throughout (abstract, lines 40, 105, 112, 149) and mentions a "train dataset" and "test dataset" (lines 103, 114), but never states which tasks are used for training and which for testing, nor the fraction held out. The reader is told there are 160 blocks, 64 items, and 13 entities in total, but has no way to assess whether the held-out tasks are genuinely different from training tasks or whether the split is easy. This is the single most important piece of experimental design information for a paper whose core claim is zero-shot generalization, and its absence undermines the entire evaluation.

2. **Missing critical control: GROOT + PPO without the proposed architecture.** The method bundle contains three components — (a) video instructions, (b) online PPO fine-tuning, (c) the intention-aware cross-attention architecture — that are never fully disentangled. The main results (Table 1) compare against GROOT (no fine-tuning), STEVE-1 (no fine-tuning), and VPT. There is no baseline that applies the same PPO procedure to unmodified GROOT (without the proposed attention layer). Such a baseline would isolate whether the architectural contribution adds value beyond simply applying online RL to the existing video-conditioned policy. The ablation in Section 4.4 uses STEVE-1/STEVEv rather than GROOT as the base, which changes multiple variables simultaneously.

3. **Core architectural contribution is under-specified.** Section 3.3 (lines 84–91) describes the intention-aware cross-attention in critically vague terms. Key details are unclear: (a) "the patches from the observation are used as the query key" — the term "query key" is non-standard and ambiguous; (b) "the keys and values derived from the other patches" — it is not specified whether "other patches" refers to instruction video patches, the linear projection of $z$, or both, and how they are combined; (c) the patches are "subsequently sent to the encoder for encoding and decoding operations in the original workflow" — but the patches were already produced by "a freezing ViT encoder" at the start of the process, creating confusion about data flow. Figures 2 and 3 are referenced but rendered as inaccessible images. The paper's central architectural claim cannot be fully understood or reproduced from the text alone.

### Minor

4. **No variance or significance measures.** Results are reported over 500–1000 rollouts (line 112), which is substantial enough for variance estimation, yet no standard deviations, confidence intervals, or error bars are provided anywhere. The paper itself notes that success rate and accuracy can be negatively correlated (line 114), making it especially important to know whether differences are meaningful or within noise.

5. **Advantage estimation equation contains an indexing error.** The GAE formula at line 66: $\hat{A}_{t}=\sum_{l=t}^{t+T}(\gamma\lambda)^{l}(r_{l}+\gamma V_{\theta}(s_{l+1})-V_{\theta}(s_{l}))$ uses $(\gamma\lambda)^l$ instead of $(\gamma\lambda)^{l-t}$ (or a similar shift), meaning the exponent grows with absolute $l$ rather than the distance from $t$. Standard GAE is $\hat{A}_t = \sum_{l=0}^T (\gamma\lambda)^l \delta_{t+l}$. As written, the formula is incorrect.

6. **$\pi_{\theta*}$ is referenced but never defined.** In the KL-constrained PPO loss (line 60), $\pi_{\theta\ast}$ appears in the KL term $KL(\pi_\theta, \pi_{\theta\ast})$ but is never defined. Context suggests it is the original/base policy, but this should be explicit.

7. **Instruction video generation process is ambiguous.** Line 103 states videos were "recorded manually and generated using the model" without specifying which model, whether these are human demonstrations or model rollouts, or what fraction came from each source. This matters because model-generated demonstrations could bias the instruction distribution toward behaviors the model already exhibits.

8. **Success rate and accuracy definitions are imprecise.** Line 112 describes the left metric as "accuracy, i.e., how well the target task was completed" and the right as "precision, i.e., the exactness with which the task was completed." These are not standard or precisely operationalized — e.g., is accuracy proportion of correct actions out of all actions? Is it a per-rollout or per-action metric? Without clear definitions, the negative correlation the paper discusses (line 114) is difficult to interpret.

9. **The central "latent vocabulary" motivation is empirically unverified.** The paper's entire architectural motivation rests on the claim that $z$ learns a discrete task-code vocabulary during fine-tuning (lines 77–78), with concrete examples ("a value of 1 could indicate Mine Obsidian, 2 for Kill Cow, 3 for Craft Clock"). This is presented as analysis but no empirical evidence is provided — no latent probing, no PCA or clustering of $z$ vectors, no mutual information analysis. While the hypothesis is reasonable, it remains speculative, and the architecture is justified by an unverified diagnosis.

10. **All PPO hyperparameters and training details are absent.** No learning rate, clip range, number of epochs, batch size, GAE $\lambda$, training duration, convergence criteria, or specification of which model components are frozen vs. fine-tuned are reported, making the work irreproducible.

### Trivial
None.

## Nice-to-Haves

- The framework could be strengthened by reporting a combined metric (e.g., F1 or AUROC) that handles the success/accuracy tradeoff reported by the paper.
- A limitations section acknowledging known failure cases, sensitivity to instruction video quality, or scenarios where generalization fails would improve the paper's scientific completeness.

## Removed Points

The following criticisms from the inputs were removed or demoted after cross-checking:

- **"Conflates RLHF and PPO"**: The paper states "online reinforcement learning methods like PPO have shone in important works such as Instruct GPT" (line 14). InstructGPT did use PPO; this characterization is factually correct. Removed.
- **"Section 4.3 appears to be missing / numbering broken"**: This is a PDF extraction artifact. The original submission is intact. Removed.
- **"Section 2.2 could be condensed"**: Subjective style preference, not a concrete weakness. Removed.
- **"InstructGPT used PPO with a learned reward model, not 'PPO' per se"**: Factually incorrect nitpick — PPO is the algorithm; it was used in InstructGPT. Removed.
- **Strength Finder's generic framing ("addressed an important problem", "targeted an interesting question")**: These are not paper-specific claims. Removed.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's diagnosis and its evidence. The "latent vocabulary" hypothesis — that $z$'s limited dimensionality forces task-ID-like encoding during fine-tuning — is a genuinely specific and testable mechanistic claim that goes beyond typical overfitting narratives. However, the paper treats this as established fact when it is entirely unverified. An analysis probing the latent space of $z$ before and after fine-tuning (e.g., showing that $z$ dimensions correlate with task identity under GROOT fine-tuning but not under the proposed architecture) would simultaneously validate the diagnosis and the cure. The paper currently has the diagnosis-cure narrative inverted: it motivates an architecture with an unvalidated claim and then validates the architecture with an experiment that lacks the critical control to attribute the gains.

## Suggestions

1. **Report the train/test split explicitly** — number of tasks per category used for training vs. testing, and the principle behind the split (random, difficulty-stratified, etc.). This is non-negotiable for a zero-shot generalization claim.

2. **Add the missing control**: evaluate GROOT + PPO (without the proposed attention layer) on the same task set. This directly tests whether the architecture adds value beyond online fine-tuning alone.

3. **Clarify the intention-aware cross-attention mechanism** with a precise mathematical description (input tensors, dimensions, query/key/value definitions, output). The current paragraph-level description is insufficient for ICLR.

4. **Fix the GAE equation** — the exponent should be $(\gamma\lambda)^{l-t}$ (or equivalently, sum over $\delta_{t+l}$ with $(\gamma\lambda)^l$).

5. **Provide variance estimates** for all reported metrics given the 500–1000 rollout budget.

6. **Define $\pi_{\theta*}$** explicitly in the loss equation description.

## Score and Decision

This paper identifies a genuine problem and proposes a plausible architectural solution, but the contribution is not verifiable from the paper as written. The central claim of zero-shot generalization depends on an unspecified train/test split. The architectural improvement cannot be disentangled from online fine-tuning because the critical control is missing. The core mechanism itself is described too vaguely to evaluate. These are structural reporting omissions, not debatable interpretations. The underlying idea has merit and the diagnosis is interesting, but the paper does not meet the evidential bar for ICLR.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>