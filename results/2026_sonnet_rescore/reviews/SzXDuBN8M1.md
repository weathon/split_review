## Summary

TD-JEPA introduces a temporal-difference (TD) based latent-predictive objective that allows learning state and task encoders, a multi-step policy-conditioned predictor, and a family of parameterized policies from offline, reward-free transition data. The core novelty is replacing a Monte Carlo multi-policy latent-predictive loss with a TD variant (Eq. 7, 9), enabling off-policy and multi-step training without on-policy rollouts. The learned predictor approximates successor features in latent space, enabling zero-shot policy optimization for any reward function. The paper provides theoretical justification through four theorems and evaluates across 65 tasks on ExoRL/DMC and OGBench with proprioceptive and pixel inputs.

---

## Strengths

- **Novel off-policy TD latent-predictive objective (Eq. 7, 9):** The derivation of the TD-JEPA loss from the Bellman equation for successor features is clean and non-trivial. It directly addresses the core limitation of MC-JEPA (Eq. 5), which requires on-policy rollouts from all trained policies. The off-policy compatibility is a genuine advancement enabling use of static offline datasets.

- **Gradient-matching theory (Theorems 1 and 3):** Theorem 1 shows that, for fixed encoders, the MC-JEPA loss shares gradients w.r.t. representations with the successor-measure approximation loss (L_SM). Theorem 3 establishes the analogous result for the TD variant, connecting TD-JEPA to forward/backward TD successor-measure losses (Eq. 11, 12). These results provide principled justification that the latent-predictive objective is genuinely learning to approximate successor measures rather than arbitrary latents. Per the paper, this "subsumes and expands" prior single-policy or single-step results.

- **Strong pixel-based performance across 65 tasks:** Table 1 and Figure 2 show TD-JEPA achieves the best aggregate score in DMC_RGB (628.8 vs. next-best 582.4) and OGBench_RGB (41.34, roughly tied with BYOL-γ*), and is significantly better than all competitors in the RGB probability-of-improvement heatmap. The advantage specifically in pixel settings is consistent across locomotion, navigation, and manipulation.

- **Asymmetric encoder ablation (Figure 3, right):** The direct comparison against a symmetric variant (shared φ=ψ) empirically substantiates the claim that separate state and task encoders generally improve performance, especially in pixel domains, justifying the added architectural complexity.

- **Policy-conditioned multi-step dynamics matter (Figure 3, left):** The comparison of TD-JEPA against BYOL* (one-step, behavioral policy) and BYOL-γ* (multi-step, behavioral policy) is the clearest ablative evidence for the value of directly modeling policy-conditional successor measures, rather than behavioral dynamics.

- **State representations enable fast adaptation (Figure 4):** The frozen pre-trained state encoder often suffices for rapid offline/online RL fine-tuning on DMC tasks, demonstrating practical utility beyond zero-shot deployment.

---

## Weaknesses

### Fatal

None.

### Major

- **Symmetry assumption (A3) in all three main theorems:** Theorems 1, 3, and 4 all require P^{πz} to be a symmetric matrix (A3). This assumption is extremely restrictive and is violated in virtually all practical environments, including all DMC and OGBench domains evaluated. The paper acknowledges the limitation in the conclusion ("formal guarantees rely on an assumption of symmetry") and claims the assumption can be relaxed in Appendix C, but the body of the paper does not show how the insights of Theorems 1 and 3 hold approximately or qualitatively without symmetry. The full theoretical narrative — that TD-JEPA optimizes a meaningful surrogate for successor-measure approximation — rests on theorems that may not describe the actual training dynamics of the practical system. This limits the theoretical contribution from a rigorous grounding to a motivated heuristic.

- **Unexplained large underperformance in proprioceptive manipulation:** On OGBench (proprioceptive), TD-JEPA scores 34.20 on cube-single vs. HILP's 74.20 and BYOL-γ*'s 79.40, and 3.60 vs. 20.00 on cube-double (Table 1). These are not marginal gaps. The paper's sole explanation — "many algorithms unsurprisingly achieve strong performance in some configurations while under-performing in others" — uses the same language for a 2× shortfall as for minor variation, and is uninformative. Given that TD-JEPA's core design targets multi-step policy-conditional dynamics, the failure on structured manipulation tasks (low-coverage data, compositional goal-reaching) suggests a setting-specific limitation in the method that warrants diagnosis. The ablations in Figure 3 do not illuminate this pattern. This failure pattern leaves the method's operating regime unclear.

### Minor

- **Practical anti-collapse mechanism is L_REG, but Theorem 2 covers an idealized regime:** Algorithm 1 achieves collapse prevention via covariance regularization (L_REG, lines 126–128), implemented as a batch-level orthonormality penalty. Theorem 2 analyzes a continuous-time relaxation in which optimal predictors are recomputed at every infinitesimal gradient step and establishes covariance preservation, not the effect of L_REG. The paper acknowledges Theorem 2 covers an "idealized variant" and that the practical algorithm uses EMA target networks and regularization. However, no ablation removes L_REG to quantify its contribution, leaving the relationship between the theoretical guarantee and the practical anti-collapse mechanism unclear. Removing L_REG would both validate its necessity and clarify what Theorem 2 is and is not explaining about the practical system.

- **Off-policy action sampling creates a theory–algorithm gap not discussed:** In Algorithm 1, next-step actions a′_i are sampled from π(φ^−(s′_i), z_i), where the policies depend on the current online encoder. This creates a feedback loop between the policy and the representation that the theorems — which treat the policy family {π_z} as fixed — do not analyze. The use of target networks (φ^−) partially addresses this, but the coupling is real and the paper does not discuss its potential effects on convergence or representation quality.

### Trivial

- The improvement from adding explicit state encoders to baselines (1.3× to 2.4× over published baselines) is mentioned only in footnote 6 and the body, but not highlighted in the abstract or contribution list, even though this is itself a methodological finding of some interest to practitioners.

---

## Nice-to-Haves

- An ablation removing L_REG would directly validate its role and clarify the relationship with Theorem 2, sharpening the paper's theoretical narrative.
- Fast-adaptation experiments (Figure 4) cover only DMC; analogous results on OGBench manipulation tasks — where zero-shot performance is weakest — would reveal whether the state encoder provides adaptation benefits even when zero-shot retrieval fails.
- A targeted analysis of learned representations (e.g., probing whether φ captures task-relevant spatial/temporal features differently from competitors) would help explain why the pixel advantage is strong while manipulation performance is lower.
- Explicitly reversing the theoretical emphasis to lead with the gradient-matching result (Theorems 1, 3) as the primary insight, and being clearer that Theorem 2 describes an idealized regime not fully covering the practical algorithm, would improve the coherence of Section 4.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Theorem 2 substantially overstates what is proven" (Harsh Critic):** Partially removed/demoted. The abstract explicitly says "an idealized variant of TD-JEPA avoids collapse with proper initialization," and the body (following Theorem 2) says the result "suggests that, if predictors are trained at a faster rate than representations, the overall dynamics preserve their covariance, thus preventing φ and ψ from collapsing to trivial solutions… when properly initialized." The language is careful and qualified. The legitimate residual concern (no L_REG ablation, practical algorithm not fully covered by Theorem 2) is retained as a Minor weakness above.

- **"Claim that Theorem 1 subsumes prior work cannot be evaluated (proof in appendix)" (Harsh Critic):** Removed per the hard rule on appendix content. The paper claims Theorem 1 is a special case of a more general theorem in Appendix C that implies all prior results; we treat this claim as supported.

- **"Baseline improvement transparency — stated only in footnote" (Harsh Critic):** Removed as formatting/presentation nitpick.

- **"PSM is closely related and deserves more than one sentence" (Harsh Critic):** Removed per the rule against requesting additional related-work discussion (we cannot independently verify the degree of relatedness or what constitutes appropriate discussion depth).

- **Generic strength "tackles an important problem in RL" (Strength Finder):** Removed as insufficiently specific per filter rules; retained only concrete, paper-specific strengths.

---

## Novel Insights

The paper's most intellectually distinctive contribution is the gradient-matching argument (Theorems 1 and 3), which shows that latent-predictive losses — despite operating entirely in embedding space without explicit successor-measure targets — descend in the same direction as successor-measure approximation losses for arbitrary fixed representations. This insight unifies latent-predictive and successor-feature learning under a single analytical framework, and extends naturally to the TD setting where prior work had only characterized single-policy or on-policy cases. The empirical finding that the benefit of TD-JEPA is specifically concentrated in pixel-based domains is also noteworthy: it suggests that the TD formulation's advantage may be tied to more expressive spatiotemporal abstraction under high-dimensional inputs, a hypothesis worth investigating in future work.

---

## Suggestions

1. **Run an L_REG ablation.** This is the single most informative missing experiment: disable L_REG while keeping everything else identical and report collapse behavior. It would either validate L_REG's necessity or reveal that target networks alone suffice, directly informing the theory–practice relationship.

2. **Diagnose the cube-single/cube-double failure.** Examine whether the underperformance stems from dataset coverage, the BC regularization setting, or the successor-feature parameterization. Even a failure analysis (e.g., checking if representations collapse or become task-agnostic in these settings) would sharpen the paper's understanding of its own operating regime.

3. **Include OGBench in the fast-adaptation evaluation.** Figure 4 demonstrates a compelling use case for the pre-trained state encoder, but the experiments are limited to DMC where TD-JEPA already performs well. Extending Figure 4 to cube-single — where zero-shot performance is weakest — would reveal whether the state encoder is still useful when retrieval fails.

4. **Reframe the theory section.** Lead with Theorems 1 and 3 (gradient matching) as the main insight, and qualify Theorem 2 more explicitly as covering an idealized continuous-time regime that does not map directly to Algorithm 1. This reordering would make the theory section more credible by avoiding overstatement and directing attention to the genuinely strongest result.

---

## Evaluation on Key Axes

- **Originality:** Solid. The TD-based multi-policy latent-predictive objective is a meaningful technical novelty. The gradient-matching argument is new to this literature.
- **Importance of research question:** High. Zero-shot RL from offline, reward-free data is a central problem, and the pixel setting is particularly underserved.
- **Claims well-supported:** Mostly. Empirical claims are well-supported; theoretical claims are carefully qualified but rely on restrictive symmetry assumptions.
- **Soundness of experiments:** Good. Comprehensive evaluation across 65 tasks; ablations address main design choices; unified architecture protocol is a methodological contribution; the manipulation underperformance is a gap in the analysis.
- **Clarity of writing:** High. The paper is well-organized and the motivation, algorithm, and theory are presented clearly.
- **Value to the research community:** High. Establishes a connection between latent-predictive learning and successor-measure approximation applicable to offline multi-task settings; provides a strong empirical baseline especially for pixel-based zero-shot RL.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>