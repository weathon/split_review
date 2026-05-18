Now I have thoroughly read and verified the paper against all reviewer claims. Let me write the consolidated review.

## Summary

This paper proposes a meta-learning method for learning classifiers from noisy labels provided by multiple annotators, when only small amounts of such noisy data are available on target tasks. The core technical innovation is a differentiable, closed-form EM algorithm that operates on a neural network's latent space to jointly infer a GMM-based classifier and annotator-specific confusion matrices from a small noisy support set. During meta-training, pseudo-annotators are simulated from clean source data to bridge the distribution gap between clean training and noisy test conditions. The neural network encoder is meta-learned by backpropagating through the unrolled EM steps.

## Strengths

- **Novel integration of noisy-annotator modeling into meta-learning with differentiable closed-form EM inner loop.** The E-step (Eq. 6) and M-step (Eq. 7) are both closed-form functions of the neural-network embeddings, making the entire adaptation pipeline differentiable without requiring second-order derivatives or gradient unrolling. This enables efficient meta-learning that directly accounts for annotator noise during adaptation (Section 3.2–3.3).

- **Pseudo-annotation strategy during meta-training is empirically critical.** Ablation results (w/o PA) across all settings show large performance drops — e.g., on Omniglot 5-shot/7-annotators: 87.4% vs. 77.2% without pseudo-annotators; on LabelMe 5-shot: 60.3% vs. 52.7% (Tables 1, 2). This cleanly isolates the value of simulating noisy annotators during meta-learning.

- **Strong and consistent empirical advantage over 13 baselines across three datasets, including a real crowdsourcing dataset with cross-dataset transfer.** The proposed method outperforms all comparison methods in every support-size/annotator-number condition (Tables 1, 2) by statistically significant margins. Notably, on LabelMe it transfers knowledge from MiniImagenet (different dataset/classes) and still beats the best baseline (MCNAL, 55.6%) by 4.7 points at 5-shot, confirming practical utility under distribution shift between source and target.

- **Computational advantages over second-order meta-learning.** Meta-training time is 1,361s (proposed) vs. 3,499s (MaMV/MAML), and meta-testing time is 0.96s vs. 2.19s on Omniglot (Section 4.3). This comes from the closed-form EM inner loop avoiding Hessian-vector products.

- **Principled generalization of prototypical networks.** Section 3.2 shows (Eq. 8) that under clean labels, uniform class priors, and τ=0, the classifier reduces exactly to a prototypical network, establishing a formal connection and theoretical baseline.

## Weaknesses

### Fatal
None.

### Major

- **Comparison to the most closely related prior work is indirect.** The paper cites Zhang et al. (2023) and Han et al. (2021a,b) as the most related methods for meta-learning with multiple annotators but does not compare against them directly. The paper constructs its own baselines (PrDS, MaDS, MCL, MCNAL) that are *conceptually similar* — meta-learning on clean data then applying MV/DS/CL/CNAL on target tasks. The justification (these prior methods "cannot directly learn classifiers on target tasks" and are designed for label estimation rather than classifier learning) is reasonable, but the mapping is not exact. Without direct comparison, the reader cannot fully assess whether the proposed method improves over these specific existing approaches under identical conditions. This is the most significant limitation of the experimental section.

### Minor

- **Pseudo-annotator distribution sensitivity is not explored.** The paper uses a single meta-training distribution (0.1 expert, 0.7 hammer, 0.2 spammer) for all experiments and shows robustness to varying *test* distributions in Figure 3. However, it does not investigate whether performance degrades if the *meta-training* distribution itself is varied (e.g., if the training distribution were very different from what is encountered at test time). This limits understanding of when the pseudo-annotation strategy is most beneficial.

- **The clean-labels-in-source-tasks assumption is a practical limitation.** The paper acknowledges this in its problem formulation, but many real applications will have noisy labels in source tasks as well. While this is a reasonable first step, the paper would benefit from at least a small-scale experiment assessing robustness when source tasks also contain some level of annotation noise.

- **Hyperparameter sensitivity (τ, b, c) not discussed.** The conjugate priors involve hyperparameters τ (precision), b (class prior strength), and c (confusion matrix prior strength), which influence the EM solution. The paper does not discuss how these were chosen or whether performance is sensitive to them.

### Trivial

- **Standard errors are relegated to the appendix.** The paper notes "We did not include the standard errors of the results due to the lack of space" (Section 4.3). Given the large number of conditions, including standard errors or confidence bars in the main tables/figures would help readers assess reliability directly.

## Nice-to-Haves

- An analysis of gradient behavior through the unrolled EM steps (e.g., gradient norms, whether short unrolls at J=2 produce stable meta-gradients) would strengthen the claim that the closed-form EM leads to efficient and stable meta-learning. The empirical result that J=2 works best is useful, but additional diagnostics would provide deeper insight.
- A visualization of the learned latent space (e.g., t-SNE of embedded support data before/after EM adaptation) would help build intuition for what the meta-learned encoder achieves.

## Removed Points

- The "EM gradient pathologies" concern from the Harsh Critic is moved here. The paper uses J=2–3 EM steps and the reviewer's concern about vanishing/exploding gradients through these short unrolls is speculative — empirically J=2 works best, and with only 2–3 steps gradient pathologies are highly unlikely. No evidence of a real problem.

## Novel Insights

The reviews converge on the observation that this paper's key insight — making the annotator-modeling EM algorithm closed-form and differentiable so that full meta-learning can backpropagate through it — neatly resolves a tension in prior work. Prior methods either (a) used pre-trained (frozen) features with off-the-shelf annotator aggregation, which cannot adapt the representation for the annotator-noise structure, or (b) used MAML-style inner-loop optimization, which is costly and requires tuning learning rates. The closed-form EM gives the best of both: representation learning adapts to the annotator setting, and the inner loop is both efficient and hyperparameter-light. The empirical dominance across 13 baselines confirms this design choice pays off.

## Suggestions

- For the most impactful revision, implement the closest existing method (e.g., Zhang et al., 2023 or Han et al., 2021a) directly and compare under identical conditions. If that is infeasible, provide a more detailed argument and analytical comparison showing that the generated baselines faithfully capture the behavior of those prior methods and that the performance gap is not an artifact of implementation choices.
- Vary the meta-training pseudo-annotator distribution (e.g., using each of the four test distributions as the training distribution across a grid) to characterize when the pseudo-annotation strategy is most and least beneficial.
- Report the hyperparameter values chosen for τ, b, c and include a brief sensitivity analysis in the appendix.

## Score and Decision

**Score and Decision:** The paper proposes a principled, well-executed method for an important practical problem. The core technical contribution — integrating noisy-annotator modeling into meta-learning via differentiable closed-form EM — is novel and convincingly validated across extensive experiments. The main limitation is the indirect comparison to the most closely related prior work, which somewhat weakens the novelty claim but does not invalidate the contribution. The paper merits acceptance at a strong venue.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>