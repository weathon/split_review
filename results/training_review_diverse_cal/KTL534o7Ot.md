Now I have sufficient evidence to write the consolidated review.

## Summary

This paper introduces ProgSyn, a framework for programmable synthetic tabular data generation that unifies differential privacy, logical constraints, statistical manipulations, and downstream specifications in a single pipeline. The key technical insight is pre-training a generative model and then fine-tuning it with differentiable losses automatically derived from user-provided specifications. On the Adult dataset, ProgSyn achieves state-of-the-art results in fair synthetic data generation (2.3% higher accuracy and 2× lower demographic parity distance than specialized methods) while also supporting customization types that no prior method can handle.

## Strengths

- **First general framework unifying diverse customization types**: ProgSyn supports differential privacy, logical/implication constraints, statistical manipulations, and downstream model specifications within a single programmable pipeline (Section 4.2, Figure 3). No prior work offers this breadth — DECAF, TabFairGAN, PreFair, and AIM each handle only a subset.

- **Outperforms specialized methods on their own task**: On Adult fair synthetic data generation (Table 1), ProgSyn achieves 86.1% accuracy with 0.01 demographic parity distance (non-private) and 83.9% / 0.03 (private, ε=1), surpassing methods that were designed solely for fairness. This is strong evidence that generality need not sacrifice performance.

- **Novel differentiable relaxation for logical constraints with strong empirical results**: Table 2 shows that ProgSyn with fine-tuning + rejection sampling achieves 100% constraint satisfaction on hard implications (e.g., I3) while retaining 84.7% accuracy, whereas rejection sampling alone fails to reach 100% CSR and AIM's structural zeros drops to 81.1%. The differentiable binary mask computation (Section 4.2) is a clean technical contribution.

- **Effective composability under multiple simultaneous specifications**: Table 3 shows that stacking five diverse specifications (fairness, two statistical, two logical) only reduces accuracy from 86.1% to 84.0%, with all constraints remaining satisfied. This directly supports the programmability claim.

- **Downstream specification achieves genuine fairness**: Using a single DOWNSTREAM command, ProgSyn reduces balanced accuracy for predicting sex from 83.3% to 50.2% (random guessing) while retaining 84.4% accuracy on the original task — a concrete and verifiable result.

## Weaknesses

### Fatal
None.

### Major

1. **DP fine-tuning formulation is inconsistent as written**. The fine-tuning objective in Equation (1) is defined as $\mathcal{L}_{\text{fine}}(g_\theta(z), X, X_r) := \mathcal{L}_M(g_\theta(z), X) + \sum_i \lambda_i \mathcal{L}_{\text{spec}}^{(i)}(g_\theta(z), X_r)$. Here $\mathcal{L}_M$ takes the original dataset $X$ directly. However, Section 4.1 (line 85–86) states that "fine-tuning does not access the original dataset $X$" when DP is required. The paper then says $X_r$ is "a sample generated at the end of fine-tuning" (line 74) — which is circular: $X_r$ would not be available during fine-tuning. These two statements are contradictory, and the formulation as given implies the DP guarantee is violated. The authors likely have a correct procedure (e.g., reusing pre-computed marginals $M(X)$ from the DP pre-training phase and replacing $X_r$ with a pre-training sample), but the paper does not state this. The inconsistency must be resolved, and the fine-tuning objective rewritten or clarified for the DP case.

2. **Downstream gradient mechanism is asserted without explanation**. The paper claims that $\psi^* = \arg\min_\psi \mathcal{L}_{CE}(h_\psi(\hat{X}[\text{features}]), \hat{X}[\text{target}])$ "depends (differentiably) on $\theta$ through $\hat{X}$" (line 115). The minimizer of a neural network training loss does not generally have a closed-form differentiable dependency on the training data. The paper provides no description of the mechanism used — whether it is unrolled optimization, implicit differentiation, or treating the trained surrogate as a fixed function. In practice the authors likely train $h_\psi$ for a fixed number of steps and backpropagate through those steps, which is a standard heuristic, but this should be stated explicitly along with a discussion of how gradient approximation error affects convergence. As written, the downstream specification loss — a key claimed advantage — rests on an unsupported claim.

3. **Experimental results on non-Adult datasets are presented without numerical evidence**. The paper claims state-of-the-art fair synthetic data generation and generality across four datasets (Adult, Health Heritage, German Credit, Compas), but Tables 1 and 2 only show Adult results. The three other datasets are covered in a single paragraph (line 148) with qualitative statements like "it often prevails as the best method" and "we draw similar conclusions." No accuracy numbers, fairness metrics, standard deviations, or baseline comparisons are provided for these datasets. Given the strength of the claimed state-of-the-art, full experimental tables for all datasets are necessary to support the generality claim. (This also invalidates the corresponding "strength" from the Strength Finder.)

### Minor

4. **Privacy accounting details are missing**. The paper adapts the iterative DP framework of McKenna et al. (2022) with a modified budget adaptation step (line 66), but provides no analysis of how the per-iteration DP budget is set, how composition is accounted for, or what $(\epsilon, \delta)$ guarantee is claimed. Experiments use $\epsilon=1$ but it is unclear whether this is total or per-iteration. The DP claims are not verifiable without this accounting.

5. **Rejection sampling rates are not reported**. Logical constraints achieve 100% CSR via post-generation rejection sampling (Table 2), but the paper never reports what fraction of generated rows are rejected. A constraint that requires discarding 95% of generated rows is practically much less useful than one that requires discarding 5%. This cost metric is important for assessing practical utility.

6. **No comparison to alternative generative backbones within the ProgSyn framework**. The paper uses a marginal-matching GAN with straight-through Gumbel-softmax (following Liu et al., 2021) but does not show that the fine-tuning procedure is backbone-agnostic by testing with alternatives (e.g., TVAE, CTGAN). The contribution would be stronger with evidence that the fine-tuning approach works with different base generative models.

7. **XGBoost accuracy as the sole quality metric is limited**. The paper uses only downstream XGBoost accuracy to measure synthetic data quality. While the authors justify this choice (line 124), supplementary fidelity metrics (pairwise correlation differences, marginal distribution comparisons) would strengthen the evaluation, especially for statistical manipulations where the goal is not just high downstream accuracy but faithful control of specific statistics.

### Trivial

- Line 74 states $X_r$ is "a sample generated at the end of fine-tuning," which is self-contradictory (it would not be available during fine-tuning). This likely should read "at the end of pre-training" or similar.

## Nice-to-Haves

- A discussion of how continuous features are discretized and how this affects the precision of constraints (e.g., "age > 35" becomes a bin-level condition). This is a limitation of the one-hot encoding assumption worth acknowledging.
- A comparison to unconstrained baselines (CTGAN, TVAE) on nominal data quality to establish that the pre-training itself is competitive with standard approaches.
- Ablation of the $\lambda_i$ regularization weight sensitivity.

## Removed Points

- **"Programmable overselling"** (Harsh Critic): The reviewer claims the term "programmable" is inflated because the system supports a fixed set of constraint types. However, the paper clearly defines the supported types and uses "programmable" to distinguish from prior single-task methods. This is a terminology preference, not a technical weakness. Removed.
- **"Results generalize across four datasets"** (Strength Finder #7): This strength claims generalization is supported by evidence, but the paper only provides qualitative summaries without numerical results for three of the four datasets. This conflicts with verified Weakness #3. Removed.
- **Various formatting/style nitpicks**: Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews identify gaps in presentation and evidence but do not surface a deeper technical insight about the method or problem.

## Suggestions

1. **Fix the DP fine-tuning formulation explicitly**: State that under DP, $\mathcal{L}_M$ is computed using pre-computed marginals $M(X)$ obtained during the DP pre-training phase (with no additional access to $X$), and $X_r$ is a synthetic sample drawn from the pre-trained model. Rewrite the fine-tuning objective for the DP case to avoid the current contradiction.
2. **Describe the downstream gradient mechanism precisely**: State whether gradients through $\psi^*$ are obtained via unrolled optimization, implicit differentiation, or treating the surrogate as a fixed function after $K$ gradient steps. Discuss the implications for gradient accuracy and convergence.
3. **Provide full experimental tables** for all four datasets (Health Heritage, German Credit, Compas) covering fair generation (private and non-private), logical constraints, and statistical manipulations. Include standard deviations and baseline comparisons.
4. **Add privacy accounting details**: State the per-iteration budget mechanism, composition theorem used, and the $(\epsilon, \delta)$ guarantee. Clarify whether $\epsilon=1$ is total or per-iteration.

## Score and Decision

The paper presents a genuinely novel and promising framework. The three major weaknesses — the DP formulation inconsistency, the underdescribed downstream gradient mechanism, and the missing experimental detail for non-Adult datasets — are fixable but cannot be dismissed as minor. They undermine core claims in their current form: the DP guarantee cannot be verified as written, the downstream gradient mechanism (a key claimed advantage) is unspecified, and the state-of-the-art claim rests almost entirely on one dataset. However, none of these issues is fatal — they reflect incomplete presentation rather than flawed methodology — and the Adult results are strong. This is a borderline paper that would benefit substantially from a revision cycle.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>