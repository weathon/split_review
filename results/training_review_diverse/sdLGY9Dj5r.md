Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes ZO-PoG, a black-box prompt learning framework that alternates between optimizing discrete prompts (via policy gradient with Gumbel-Softmax reparameterization) and continuous prompts (via zeroth-order gradient in a low-dimensional intrinsic subspace) for language models accessed solely through APIs. The paper provides a convergence analysis establishing sub-linear convergence and evaluates the method on five GLUE tasks across three backbone models (RoBERTa-large, GPT2-XL, Llama3), showing consistent improvements over discrete-only (BDPL) and continuous-only (BBT, SSPT) baselines.

## Strengths

1. **First joint optimization of discrete and continuous prompts for black-box PTMs**: The paper proposes a principled framework combining both modalities of prompt optimization. The empirical results consistently validate the approach: ZO-PoG outperforms both discrete-only and continuous-only baselines in all 15 settings across three backbone models and five tasks (Tables 1–3). For example, on RoBERTa-large with WNLI (len=50), ZO-PoG achieves 77.34% vs. BDPL's 69.72% and BBT's 71.75%.

2. **Ablation studies confirm both components contribute positively**: Figure 3 shows that removing either the policy-gradient (discrete) or zeroth-order (continuous) optimization component degrades performance across all backbone models and prompt lengths, providing clear evidence that the collaborative design, not just one component, drives gains.

3. **Gumbel-Softmax ablation demonstrates its value**: Figure 2 shows that incorporating the Gumbel-Softmax trick improves over the policy-gradient-only baseline (BDPL-style), suggesting the reparameterization meaningfully affects optimization quality.

4. **Convergence guarantee with explicit complexity**: Theorem 1 establishes that ZO-PoG reaches an ε-stationary point with total query complexity O(√(nκ)/ε³). Proposition 1 provides a bounded-variance guarantee for the variance-reduced policy gradient estimator, linking stability to sample size I and mini-batch size B — a level of theoretical formality absent from most black-box prompt learning works.

5. **Clean empirical methodology**: Experiments use realistic few-shot (16-shot per class) settings, report means and standard deviations over 3 seeds, and compare against appropriate baselines. The code is provided.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Unclear description of the discrete gradient estimator (Section 3.2)**. The paper introduces Gumbel-Softmax as a reparameterization (Eq. 3), then computes a score-function (policy gradient) estimator `∇_{α_i} log P(t_i | α_i)` (Eq. 4) rather than a pathwise reparameterization gradient. It never clarifies: (a) whether `P(t_i | α_i)` is the Concrete (Gumbel-Softmax) distribution's probability mass or the underlying categorical's; (b) whether samples from `GS(α, τ)` in Algorithm 1 are the continuous Gumbel-Softmax relaxation (requiring an argmax to get discrete tokens) or are directly treated as discrete indices; and (c) why Gumbel-Softmax "reduces bias" relative to a standard REINFORCE on a softmax-parameterized categorical, since the score-function estimator is already unbiased. These ambiguities make the precise gradient computation difficult to reproduce from the paper alone. The method works empirically, but the methodological narrative needs rewriting for clarity.

2. **Hyperparameter values not disclosed in the paper**. While Algorithm 1 lists the input hyperparameters (subspace dimension *d*, temperature *τ*, smoothing parameter *μ*, sample counts *I₁* and *I₂*, learning rates *η_α*, *η_z*, mini-batch size *B*), the paper does not report their actual values or selection procedure for any experiment. The code is provided, but the paper itself is incomplete as a standalone reference. A brief table or footnote with these values would significantly improve reproducibility.

3. **Convergence analysis, while standard, makes assumptions that are stated without justification**. Assumption 1 (block-wise smoothness of the loss w.r.t. the distribution parameters *α*) is mathematically plausible but the paper provides no reasoning or citations linking the Concrete distribution's properties to the smoothness of the composition with a neural network loss. This weakens the theory section somewhat — it follows standard block-coordinate stochastic analysis rather than deriving insight specific to the Gumbel-Softmax / alternating structure. The theory is not invalid, but its marginal contribution is incremental.

### Trivial

1. **Task diversity limited to GLUE (NLU only)**. All five tasks are English-language natural language inference / acceptability tasks. No generation tasks (e.g., summarization, QA) are included, which limits breadth of the generalization claim.

2. **No discussion of limitations or failure cases in the conclusion**. The paper does not address computational cost trade-offs (I₁+I₂ forward passes per iteration) or potential sensitivity to hyperparameters, which would help practitioners.

## Nice-to-Haves

- **Sequential two-stage baseline**: The reviewer suggests comparing ZO-PoG (alternating optimization) against a simpler pipeline: first optimize discrete prompts with BDPL, then freeze them and optimize continuous embeddings with BBT/SSPT on top. This would directly test whether the alternating schedule provides synergy beyond a better initialization point. Adding this experiment would strengthen the paper's core claim about *collaborative* (rather than sequential) optimization.

- **Computational cost comparison**: Reporting wall-clock time or total query budget relative to baselines would help practitioners assess the practical trade-off of using both I₁ + I₂ forward passes per iteration.

- **Convergence plots**: Including empirical loss-vs-iterations curves would connect the theory (Theorem 1) to practice and make the convergence analysis more impactful.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Smoothness assumption unverified" (from Harsh Critic #3, in full)**: The reviewer argued Assumption 1 is a "methodological gap" because it is not grounded. However, block-wise smoothness (gradient Lipschitz) is a universal assumption in non-convex optimization; nearly every convergence analysis in this area makes it. The reviewer acknowledges it is "mathematically plausible." This is not a meaningful weakness of the paper — it is standard practice. *Justification for removal: the criticism holds the paper to an unrealistic standard for a theory assumption in ML optimization; the assumption is standard and well-accepted.*

- **"Missing baseline to justify alternating optimization" (from Harsh Critic #2) downgraded to Nice-to-Have**: The reviewer claims this is "evidential" and the central claim is incompletely supported. However, the paper's central claim is that *jointly* optimizing both discrete and continuous prompts beats optimizing either alone — this is already demonstrated by Tables 1–3 and the ablations in Figure 3. The sequential-vs-alternating question is a finer-grained design choice. *Justification for downgrade: this is a reasonable additional experiment but does not threaten the paper's core contribution; it belongs in Nice-to-Haves.*

- **"Convergence analysis not tied to innovations"**: The reviewer notes the theory "is standard and not tied to the specific algorithm's innovations." While true, this applies to most convergence analyses in ML systems papers, which typically extend existing block-coordinate frameworks. The paper's theory is a formal contribution that exceeds what most black-box prompt learning papers provide. *Justification for removal of this as a core weakness: this is a generic critique applicable to many papers and does not represent a flaw specific to this work that threatens acceptance.*

- **Weaknesses complaining about task diversity / missing computational cost**: These are scope-creep or wishlist items, moved to Nice-to-Haves or Trivial.

- **Generic strengths from Strength Finder**: The Strength Finder's "#4 Variance-reduced policy gradient with theoretical bound" is kept as a supporting strength but downgraded in emphasis — it is standard VR-PGE theory. Its "#3 Strong empirical results across diverse models and tasks" is merged into Strength #1 above.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the method's implications that the paper itself does not already articulate.

## Suggestions

1. **Clarify the discrete gradient estimator in Section 3.2**. Specify (i) whether `P(t_i|α_i)` is the Concrete distribution or a categorical with softmax probabilities, (ii) whether the Gumbel-Softmax sample is discretized via argmax (and what happens during backward), (iii) explicitly state that the gradient is a score-function (REINFORCE) estimator on the Concrete distribution, not a pathwise reparameterization gradient, and (iv) clarify what "bias reduction" refers to (e.g., smoother optimization landscape vs. variance reduction vs. optimization bias from the Concrete relaxation).

2. **Add a table of hyperparameter values** used in the main experiments (d, τ, μ, I₁, I₂, B, η_α, η_z, truncation threshold ε) in the main paper or appendix.

3. **Include a sequential two-stage baseline** (e.g., optimize discrete prompt with BDPL → freeze → optimize continuous with ZO/BBT) to further validate the alternating design choice.

4. **Add convergence plots** (loss vs. iterations) to connect the theory with practice.

## Score and Decision

The paper proposes a sensible combination of existing techniques (discrete prompt optimization via policy gradient + continuous prompt optimization via zeroth-order gradient) with consistent empirical validation across three models and five tasks. The ablations convincingly demonstrate that both components contribute. The convergence analysis, while standard, provides useful formal support. The main weakness is the unclear description of the discrete gradient estimator (the role of Gumbel-Softmax vs. score-function gradient), which needs clarification but does not invalidate the method or results. No fundamental issues are present. The paper represents a solid empirical contribution with adequate theory.

**Score**: 6.0  
**Decision**: Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>