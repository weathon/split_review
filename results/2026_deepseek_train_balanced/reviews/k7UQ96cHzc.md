Now let me finalize the review.

## Summary
The paper introduces "anti-classes" and the one-cold cross entropy (OCCE) loss for supervised classification. The key idea is to set a uniform target of 1/(N-1) over all non-ground-truth (complementary) classes, which is combined with standard CE as L = L_CE + γ·L_OCCE. This encourages symmetric, equiangular relationships among complementary class representations. Experiments across closed-set classification, transfer learning, open-set recognition, and OOD detection show consistent improvements.

## Strengths
- **Gradient analysis revealing distinct convergence dynamics (Equations 6–7, Figure 2)**: The paper derives that under CE, complementary-class activations independently diverge to −∞, whereas under OCCE they converge to equal finite values. The gradient-field visualization (Figure 2b) further shows that OCCE produces large gradients across a much wider region of activation space than CE, providing concrete theoretical grounding for why the method works.

- **Quantitative demonstration of controlled neural collapse (Figure 4)**: Using all four NC metrics from Zhu et al. (2024), the paper shows that OCCE provides explicit, tunable control over the geometric structure of the feature space — NC metrics monotonically increase with γ. This goes beyond prior work where neural collapse arises incidentally in late training.

- **Causal evidence that OCCE resolves independence deficit (Figure 5a)**: Following Feng et al. (2024), the paper shows that with CE alone, 80% classification accuracy is recovered from only 22 of 100 dimensions, whereas with γ=10, 73 dimensions are needed. This directly demonstrates that OCCE forces class representations to be linearly independent rather than redundantly determined by one another.

- **Consistent empirical gains across diverse settings (Tables 1–4)**: Adding OCCE reduces test error for 7 different baseline losses (CE, label smoothing, focal loss variants, COT/CCE, etc.) across ResNet, MobileNet, DenseNet, and Swin-T on CIFAR-100 and TinyImageNet. OOD detection improves on all 5 ID/OOD dataset pairs. The breadth of this evidence supports the method's general usefulness.

## Weaknesses

### Major
- **Missing variance reporting for main results**: Tables 1 and 2 report test errors as point estimates without standard deviations or confidence intervals, despite the paper stating 10 seeds were used for the sensitivity analysis and 5 for OSR. For improvements like 21.88% → 20.98% with CE on CIFAR-100, the reader cannot assess statistical significance. This undermines rigorous comparison.

- **No direct comparison isolating OCCE's advantage over complement-entropy methods**: Table 1 includes COT/CCE as baselines, but the critical head-to-head comparison is absent: CE+OCCE vs. CE+COT or CE+CCE directly. The paper claims in Section 4 that OCCE is "better positioned in the loss landscape" than COT/CCE and can be "naturally integrated with soft labels and knowledge distillation," but provides no experiment demonstrating that the anti-class formulation yields marginal improvement over the entropy-based formulation. Without this, we cannot attribute the gains to the specific anti-class mechanism rather than to adding *any* complementary regularization. (Note: COT/CCE are included as baselines in Table 1, and CE+OCCE can be compared against the COT/CCE column; the weakness is that the paper never frames or analyzes this critical comparison.)

### Minor
- **γ selection for OOD experiments is unexplained**: Closed-set experiments use γ=1 (optimal on CIFAR-100), but OOD experiments switch to γ=0.1 (line 184) without justification. This raises the question of whether OOD benefits are robust or require re-tuning. A brief sensitivity analysis for OOD would clarify.
  
- **Neural collapse vs. accuracy trade-off not reconciled**: Figure 4 shows NC metrics monotonically improving with γ, but Figure 5b shows accuracy peaks at γ=1 then declines. The paper notes this trade-off ("as γ becomes large, it also constrains the achievable training accuracy") but does not analyze whether OCCE's benefits are separable from NC's increase or where the relationship breaks. A plot of NC metrics against validation accuracy across γ values would strengthen the analysis.

### Trivial
- The gradient expression in the text (lines 78–80, near Equation 6) appears misformatted, though the conceptual message is clear.

## Nice-to-Haves
- Report standard deviations for Tables 1 and 2.
- Add an explicit head-to-head: CE+OCCE vs CE+COT vs CE+CCE in the same unified framework.
- Provide a brief γ-sensitivity analysis for OOD tasks.

## Removed Points
These points from the inputs were removed with justification:

1. **"The core method is CE + RCE, which the paper acknowledges but does not fully reckon with"** — The paper explicitly states (line 74): "When a uniform one-cold target distribution is used as a standalone objective, then we acquire, as a special case, the reverse cross entropy (RCE) loss." It then explains (line 74) that RCE alone is not competitive, while CE+OCCE is. The paper is fully transparent; this is not a weakness.

2. **"No head-to-head comparison against COT/CCE"** (strong framing) — COT/CCE *are* included as baselines in Table 1. The specific comparison the critic wants (CE+OCCE vs CE+COT without OCCE) is present in the table but not highlighted. The weakness is retained in weakened form (lack of explicit framing/analysis of this comparison).

3. **"Gradient equation corrupted"** — This is a parser artifact, not an author error.

4. **"NC versus generalization causality"** — The paper acknowledges the trade-off (line 127) and does not claim strict causal direction. The critique overstates what the paper asserts.

5. **Strength Finder's generic strengths** (e.g., "addressed an important problem") — Removed as lacking concrete evidence or being superficial or conflicting with verified weaknesses.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Report standard deviations for all main results (Tables 1–2).
2. Add a clean head-to-head comparison of CE+OCCE vs CE+COT vs CE+CCE in the experimental framework.
3. Justify the γ=0.1 choice for OOD, or show that the OOD benefit is robust across γ values.
4. Plot NC metrics against validation accuracy across γ to clarify where the relationship with generalization breaks.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>