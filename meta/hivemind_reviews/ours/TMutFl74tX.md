## Summary
The paper proposes a meta-learning method for learning from multiple noisy annotators with limited data. The key idea is to meta-learn a neural network embedding by simulating noisy annotations from multiple pseudo-annotators during meta-training, then adapt a Gaussian mixture classifier with annotator-specific confusion matrices via a differentiable closed-form EM algorithm. The method is evaluated on Omniglot, Miniimagenet, and the real crowdsourcing dataset LabelMe, consistently outperforming 13 baselines.

## Strengths
1. **Pseudo-annotation during meta-training is shown to be essential via clean ablation**: The comparison against "w/o PA" (same method without pseudo-annotations) demonstrates a large and consistent performance gap across all settings (e.g., Omniglot 1-shot, R=3: Ours 72.0% vs. w/o PA 65.8% in Table 1a). This directly and cleanly supports the paper's central claim that simulating noisy labels during meta-learning is critical.

2. **Closed-form differentiable EM steps enable efficient inner-loop optimization**: The derivation of closed-form EM updates (Eqs. 6–7) using conjugate priors makes the entire adaptation differentiable without second-order derivatives. The computation time results (Section 4.3) confirm this: meta-training (1361s) is substantially faster than MAML-based MaMV (3499s) and only marginally slower than prototypical networks (1281s).

3. **Consistent and substantial improvements across diverse datasets and settings**: The method outperforms all 13 baselines across all conditions in Tables 1–2 on Omniglot, Miniimagenet, and the real crowdsourcing dataset LabelMe, often by >5–10 absolute percentage points over the best meta-learning baseline. The cross-dataset transfer experiment (meta-train on Miniimagenet, test on LabelMe) serves as a strong stress test.

4. **Theoretical connection to prototypical networks is clearly established**: Section 3.2 shows that under uniform priors and clean labels, the classifier reduces to that of a prototypical network, providing a principled extension that generalizes a well-known method.

## Weaknesses
### Fatal

None.

### Major

None. No identified weakness threatens the paper's core claims or invalidates its results.

### Minor

1. **Ambiguity in how the number of annotators $R$ is handled during meta-training vs. evaluation**: Algorithm 1 takes $R$ as input and generates $R$ pseudo-annotators each iteration. The experiments evaluate $R \in \{3,5,7\}$, but it is never stated whether a separate meta-trained model is used for each $R$ or a single model handles all $R$ values. While the EM algorithm is naturally agnostic to $R$ (confusion matrices are per-annotator parameters learned in the inner loop), this underspecification prevents full reproducibility. The authors should clarify this in revision.

2. **Meta-learning baselines are disadvantaged by design, and the paper's framing overstates the comparison**: The baselines (PrMV, MaMV, etc.) are meta-trained on clean data and only see noisy annotations at test time, creating an inherent disadvantage. The paper correctly includes the w/o PA ablation — which controls for this — but the narrative framing could more clearly position w/o PA as the primary competitor rather than the adapted MAML/prototypical-network baselines, which were not designed for noisy annotator settings.

3. **No sensitivity analysis of prior hyperparameters ($\tau, b, c$)**: These are treated as fixed hyperparameters, but the paper provides no analysis of how sensitive the results are to their values. Such an analysis would increase confidence in the method's robustness.

4. **No discussion of limitations or failure cases**: The paper ends with future extensions but does not candidly discuss when the method might underperform (e.g., when source tasks are too dissimilar from target tasks, or when annotator noise is structured in ways the model cannot capture).

### Trivial

- Standard errors are deferred to the appendix (Section I.12) rather than reported in the main tables. While this is a space choice, including at least standard deviations for key results would strengthen presentation.

## Suggestions
1. Clarify whether a single meta-trained model is used across all $R \in \{3,5,7\}$ or separate models are trained per $R$. If the former (which the EM formulation suggests is possible), state this explicitly and explain why it works.
2. Add a limitations paragraph to the conclusion discussing when the method might struggle.
3. Add a brief sensitivity study of the prior hyperparameters ($\tau, b, c$) in the appendix if space is constrained.
4. Reposition the narrative emphasis from "outperforming MAML/PROTO baselines" to "the pseudo-annotation strategy drives performance" (which the w/o PA ablation already cleanly demonstrates).

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
