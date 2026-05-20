Now I have sufficient calibration. Let me write the final consolidated review.

---

## Summary

This paper proposes a meta-learning method for learning classifiers from a limited number of noisy multi-annotator labels, leveraging clean labeled data from related source tasks. The method embeds examples with a neural network, models the latent space with a Gaussian mixture model combined with annotator-specific confusion matrices, and adapts to a target task via a closed-form, differentiable EM algorithm. The neural network is meta-learned by backpropagating through the EM steps, and the method simulates noisy annotators during meta-training via a pseudo-annotation strategy. Experiments on Omniglot, Miniimagenet, and the real-world crowdsourcing dataset LabelMe show consistent improvements over 13 baselines.

## Strengths

1. **Novel and principled integration of multi-annotator learning with meta-learning.** The paper formulates a natural probabilistic model (GMM + annotator confusion matrices) for the inner-loop adaptation and derives closed-form, differentiable EM updates (Eqs. 6-7). This allows efficient backpropagation through the entire adaptation procedure without second-order gradients, giving the method a clear computational advantage (meta-training 1361s vs. 3499s for MAML-based MaMV).

2. **Strong and consistent empirical results across multiple datasets.** The method outperforms all 13 baselines on Omniglot (avg. 0.892 vs. next-best meta-method PrDS at 0.858), Miniimagenet (0.542 vs. 0.495), and the real-world LabelMe crowdsourcing dataset (0.520 vs. next-best PrMV at 0.490). The margins are substantial, especially in the low-data regimes that the paper targets.

3. **The pseudo-annotation ablation cleanly demonstrates the key innovation.** The "w/o PA" ablation (removing simulated noisy annotators during meta-training) drops accuracy substantially (Omniglot avg: 0.892 → 0.758; Miniimagenet: 0.542 → 0.449), providing direct causal evidence that the pseudo-annotation strategy is essential.

4. **Principled connection to prototypical networks.** Section 3.2 explicitly shows that with uniform priors, clean labels, and one-hot responsibilities, the classifier reduces to the prototypical network (Snell et al., 2017). This theoretical connection grounds the method in established meta-learning and distinguishes it from ad-hoc adaptations.

5. **Robustness to mismatched annotator distributions between source and target.** Figure 3 shows that as the spammer ratio in target tasks varies from 0.1 to 0.6 (while source uses a fixed (0.1, 0.7, 0.2) distribution), the proposed method consistently outperforms all baselines, demonstrating generalization to unseen annotator compositions.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The pseudo-annotator distribution mismatch is explored only over a modest range.** The paper meta-trains with a single annotator distribution (0.1 expert, 0.7 hammer, 0.2 spammer) and evaluates target distributions that vary the spammer ratio from 0.1 to 0.4. The gap between meta-training (0.2 spammer) and the farthest target distribution (0.4 spammer) is not extreme. The paper acknowledges this in Footnote 4 ("determining a better distribution will be a future challenge"), and Figure 3 does show robustness within the tested range. However, the question of how performance degrades when meta-training and target distributions are *severely* mismatched (e.g., meta-training with mostly experts, target with mostly spammers) remains unexplored. This is a practical limitation worth noting.

2. **The number of pseudo-annotators `R` used during meta-training is not specified.** Algorithm 1 takes `R` as a requirement, and target tasks are evaluated with `R ∈ {3,5,7}`. However, the paper does not state what value(s) of `R` are used during meta-training (e.g., a single fixed value, or drawn at random per task). While the results are strong regardless, this omission makes it harder to assess potential sensitivity — for example, meta-training with `R=5` may be suboptimal for target tasks with `R=3`.

3. **Sensitivity analysis for prior hyperparameters (τ, b, c) is absent.** While the paper provides a sensitivity analysis for the number of EM steps `J` (Figure 4), it does not analyze sensitivity to the precision prior `τ`, the class prior parameter `b`, or the confusion matrix prior `c`. These hyperparameters affect the regularization strength in the closed-form EM updates (Eq. 7), and a brief study would strengthen the paper.

4. **Standard errors are deferred to the appendix.** The paper notes "We did not include the standard errors of the results due to the lack of space. The full results including the standard errors are described in Section I.12." This is a presentation choice, and the appendix presumably contains them, but their absence from the main tables (especially when many results are bolded via t-tests) reduces interpretability for the reader.

5. **The advantage of pseudo-annotation diminishes in high-data regimes.** On Omniglot with 20 support examples and 7 annotators, Ours=0.982 and w/o PA=0.981 (both bolded). The paper implicitly acknowledges this diminishing return (the method targets the low-data regime), but a brief discussion would clarify the scope of the contribution.

### Trivial

- The paper uses the notation `$\bar{\mathcal{S}}$` for the clean support set but then reuses `$\mathcal{S}$` for the pseudo-annotated version, which can be momentarily confusing.

## Nice-to-Haves

- A visualization (e.g., t-SNE) of the learned embeddings before and after meta-training, demonstrating that the GMM with noisy labels recovers well-separated class prototypes, would strengthen the intuition behind the method.
- A brief ablation varying the *fidelity* of the pseudo-annotator distribution used in meta-training (e.g., what if meta-training uses a distribution very different from the target?) would sharpen the understanding of how much prior knowledge about annotator behavior is needed.

## Removed Points

- **Criticism about baselines being "constructed by the authors, not from prior work as-is"**: The paper explicitly states that existing meta-learning methods for multi-annotator settings cannot be directly used, so constructing these baselines is necessary and appropriate. The paper is transparent about this. The large performance gap (e.g., 0.892 vs. 0.858) further mitigates baseline tuning concerns. This point is not a genuine weakness.

- **Criticism about missing appendix content (Appendix J on noisy source tasks)**: The parser strips appendix sections from all papers; these exist in the original submission.

- **Criticism about "overclaim" regarding existing methods not learning classifiers**: The paper qualifies this claim appropriately — it says specific methods (Zhang et al., 2023; Han et al., 2021a) "cannot directly learn classifiers on target tasks," which is accurate for those methods, and acknowledges that other methods like crowd layer do learn classifiers.

- **Strength Finder's generic claims** (e.g., "this paper addressed an important problem"): Removed as generic. Only concrete, evidence-grounded strengths are kept.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an observation about the paper that the authors themselves do not already articulate.

## Suggestions

- Specify the value(s) of `R` used during meta-training in the experimental setup (Section 4.1).
- Add a brief sensitivity analysis for the prior hyperparameters `τ`, `b`, `c` (e.g., varying across one order of magnitude in each direction) in the appendix, and summarize the finding in the main paper.
- Explicitly note the diminishing returns of pseudo-annotation in high-data regimes as a discussion point in Section 4.3 or Section 5.

## Score and Decision

### Calibration Summary

**Round 1 (Bracketing):** Queried for papers on meta-learning / noisy labels / multiple annotators across three score bands:
- Weak anchors (score < 3.5): Found 4 papers scoring 2.00–3.40 (e.g., "Meta-Tasks: Improving Robustness in Few-Shot Classification" avg 2.50). The current paper is dramatically stronger than these.
- Middle anchors (3.5–7.5): Found 4 papers scoring 4.00–5.40 (e.g., "Learning a Reusable Meta Denoiser" avg 4.25, "Estimating the conformal prediction threshold from noisy labels" avg 5.40). The current paper is clearly stronger.
- Strong anchors (>7.5): Found 4 papers scoring 8.00–8.50 (e.g., "Understanding and Mitigating Label Noise in Pre-training" avg 8.50, "Probabilistic Learning to Defer" avg 8.00). The current paper is not at this level — these papers have broader impact, deeper analysis, or more extensive theoretical contributions.

**Initial bracket:** 5.5 – 7.5

**Round 2 (Narrowing):** Targeted search within the bracket:
- "meta-learning few-shot classification with probabilistic model EM algorithm" (4.5–6.5): Found papers at 5.33–6.00 (e.g., "Efficient Heterogeneous Meta-Learning via Channel Shuffling Modulation" avg 6.00, accepted poster). The current paper is comparable or slightly stronger — it has more thorough experiments and a cleaner evaluation.
- "meta-learning multiple annotators crowdsourcing noisy labels prototype" (6.0–7.5): Found papers at 6.25–7.00 (e.g., "MetaCoCo" avg 7.00, accepted poster; "Learning under Temporal Label Noise" avg 6.25, accepted poster; "A Hierarchical Bayesian Model for Few-Shot Meta Learning" avg 6.67, accepted spotlight). The Hierarchical Bayesian paper (6.67) had issues with novelty overclaiming and insufficient empirical support for its central claims — the current paper is cleaner and better-supported. The current paper is stronger than the 6.0–6.25 anchors but not as strong as the 7+ anchors which typically have deeper analysis or broader impact.

**Final score determination:** The paper lands between the 6.0 anchors (accepted poster level) and the 6.67–7.0 level. It has a well-motivated problem, a clean method, and thorough experiments, but the minor gaps (missing R specification, limited distribution sensitivity analysis, no hyperparameter sensitivity) prevent it from reaching the 7+ tier. **Score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>