Now I have all the evidence I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes Di-SkilL, a method for learning diverse skills in Contextual Episode-Based Policy Search (CEPS) by combining a non-linear Mixture of Experts (MoE) policy with energy-based per-expert context distributions for automatic curriculum learning. The key ideas are: (i) using deep neural network experts instead of linear ones to improve representational capacity, and (ii) modeling each expert's preferred context region as an energy-based model (EBM) that can represent multi-modal, bounded distributions without requiring hand-tuned penalty terms. Experiments on four simulated robotic tasks (Reacher, Table Tennis, Box Pushing, Minigolf) show that Di-SkilL outperforms BBRL (single-mode non-linear policy) and SVSL (linear MoE with Gaussian context distributions).

## Strengths

1. **Consistent empirical improvement over strong CEPS baselines on multiple tasks.** Di-SkilL achieves substantially higher success rates than BBRL on Box Pushing (~85% vs ~65%) and Robot Minigolf (~70% vs ~50%), and outperforms SVSL on Table Tennis (Fig 3b). These are challenging tasks with non-Markovian/sparse rewards where multi-modal solutions are required.

2. **Ablation demonstrates that automatic curriculum learning (ACL) is necessary for efficient learning.** The ablation in §4.1 shows that disabling ACL (Di-SkilLwoCurV1, same 50 samples per expert as Di-SkilL) causes the success rate to collapse, while increasing to 260 samples per expert without ACL (V2) still results in much slower convergence. This cleanly validates the core design choice of optimizing per-expert context distributions, with sample count controlled between Di-SkilL and V1.

3. **Principled use of EBMs to handle multi-modal, bounded context distributions without environment-specific engineering.** The paper identifies three challenges (complex distributions, multi-modality, bounded validity) and shows how the EBM formulation with Monte Carlo normalizing-constant approximation circumvents the need for hand-tuned penalty terms that prior work (Celik et al., 2022) requires.

4. **Stable optimization via trust-region updates for the bi-level MoE problem.** The use of trust-region layers (Otto et al., 2021) for the expert update and PPO for the per-expert context distribution provides a coherent optimization framework that converges reliably across all environments.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative evaluation of diversity.** The paper's title and central framing are about "diverse skills" and "multi-modality in the behavior space," yet the only evidence for diversity is a single qualitative figure (Figure 5) showing a few box-pushing trajectories. No diversity metric is reported — not entropy of expert selection for a given context, variation in trajectory outcomes per context, number of distinct solutions discovered, or any other measure. The quantitative results (success rate, return) measure only task performance, not diversity. For a paper whose contribution hinges on multi-modal behavior, this is a fundamental evidential gap. The strength of the diversity claim cannot be assessed without quantification.

2. **Missing component-isolation baselines.** The paper's claimed technical contributions are (i) non-linear (deep) experts and (ii) EBM-based context distributions. The only method that replaces *both* components with simpler alternatives (SVSL: linear experts + Gaussian context distributions) is compared only in the ablation (Fig 3b). No baseline isolates a single component — there is no comparison to a method with non-linear experts + Gaussian context distributions, nor to the method the paper itself proposes (LinDi-SkilL, i.e., linear experts + EBM context distributions). The paper states in §4.2 that "We report the performances of Di-SkilL, Lin-DiSkill and BBRL," but the figure captions (Fig 3c, 4a–c) only describe Di-SkilL and BBRL, while LinDi-SkilL is never discussed quantitatively. This makes it impossible to attribute performance gains to either component individually.

3. **LinDi-SkilL results are promised but not clearly presented.** Section 4.1 states "We therefore propose comparing to BBRL and LinDi-SkilL instead of SVSL," and §4.2 claims "We report the performances of Di-SkilL, Lin-DiSkill and BBRL." However, the figure captions for the main experimental results (Fig 3c, 4a–c) only reference Di-SkilL and BBRL. LinDi-SkilL results are never described or discussed in the text. Since figures are embedded as images, it is possible LinDi-SkilL appears in the plots without being mentioned in the captions, but this confusion itself is a presentation failure. The reader cannot verify the contribution of the EBM component without this baseline being clearly reported and analyzed.

### Minor

4. **Missing implementation and hyperparameter details.** The paper does not specify network architecture (layers, hidden units), learning rates, batch sizes, trust-region KL constraint epsilon, PPO clipping parameter, number of PPO epochs, or the number of experts used (except "five experts" in the ablation). While CEPS papers often defer such details to a supplementary, their absence in the main text makes it impossible to assess the method's sensitivity to these choices or to reproduce the results without contacting the authors.

5. **No analysis of the EBM approximation quality.** The method approximates the EBM normalizing constant using Monte Carlo samples from the environment's context distribution. The paper states that "a large enough batch" is used but does not discuss how batch size is chosen, how many context samples are used per expert per iteration, or whether this approximation degrades when the context space is high-dimensional or has narrow discontinuities.

6. **The automatic curriculum learning ablation (§4.1) could be cleaner.** While the comparison between Di-SkilL (50 samples, ACL on) and Di-SkilLwoCurV1 (50 samples, ACL off) is fair on sample count, the ACL-disabling procedure simultaneously modifies multiple terms (setting $\log\tilde{\pi}(o|\mathbf{c})=0$ and raising $\beta$ from 0.5 to 2000). A more informative ablation would vary one thing at a time (e.g., only the intrinsic bonus term, or only the entropy scaling). The current design conflates them.

### Trivial
None.

## Nice-to-Haves

- A controlled comparison with non-linear experts + Gaussian context distributions would cleanly isolate the benefit of the EBM formulation.
- The diversity analysis would be strengthened by reporting a quantitative metric such as: (a) entropy of the gating distribution $\pi(o|\mathbf{c})$ for fixed contexts, (b) variance of trajectory outcomes (e.g., final box position/orientation) per context, or (c) number of experts that contribute non-negligible probability for a given context.
- The paper could mention computational cost (wall-clock time, scaling with number of experts) to help practitioners assess practical feasibility.

## Removed Points

- **Ablation confounded by sample count (from Critical Issue 1)**: The reviewer claimed "V1 and V2 use different numbers of context-parameter samples, so even that comparison is confounded." The paper explicitly states "For Di-SkilLwoCurV1, we provide the same number of 50 context-parameter samples per expert as in Di-SkilL." Thus V1 vs Di-SkilL is controlled on sample count. Removed as factually incorrect.
- **"Overlapping CIs on Table Tennis" (from Section 4.2 notes)**: The paper's own language for TT is "Di-SkilL achieves similar performance as BBRL, but eventually surpasses BBRL's success rate slightly" — this is appropriately cautious and does not overclaim. For Minigolf, the 70% vs 50% gap is meaningful even with overlapping CIs. This criticism is downgraded.
- **"The ablation changes both the objective and the sample count simultaneously"**: Partially removed as the V1 vs Di-SkilL comparison uses the same 50 samples. The remaining point about changing multiple terms simultaneously (log term and beta) is kept in Minor #6 but with reduced severity since these changes are what's minimally required to disable ACL.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between a reasonable method-level contribution and an experimental evaluation that is incomplete for the scope of the claims. The key insight from the review process is that the paper would be substantially stronger if it provided (a) a controlled component analysis and (b) a quantitative diversity metric — both of which are standard expectations for a paper whose title and framing center on "diverse skills."

## Suggestions

1. Add two controlled baselines to the main experiments: (a) non-linear experts + Gaussian context distributions (to isolate the EBM contribution), and (b) LinDi-SkilL (linear experts + EBM context distributions, already mentioned in the text) clearly plotted and discussed in every figure.
2. Report at least one quantitative diversity metric — the entropy of the gating distribution $\pi(o|\mathbf{c})$ for a fixed context, or the variance of trajectory outcomes per context — to substantiate the diversity claim beyond qualitative trajectories.
3. Provide implementation details (network architecture, learning rates, trust-region parameters, PPO settings, number of experts) either in the main text or in an appendix, and discuss the EBM's sensitivity to batch size.

## Score and Decision

The paper proposes a sensible combination of ideas (MoE + max-entropy RL + EBM context distributions + trust-region updates) and demonstrates consistent empirical improvements over strong baselines on challenging tasks. However, two major weaknesses prevent acceptance: (1) the central claim of "diverse skills" is supported only by qualitative evidence with no quantitative diversity metric, and (2) the experimental evaluation lacks controlled baselines that isolate the two claimed technical contributions, making it impossible to determine which component drives the gains. The LinDi-SkilL results are also unclearly presented despite being promised in the text. These gaps can be addressed with additional experiments, but the paper in its current form does not provide sufficient evidence for its core claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>