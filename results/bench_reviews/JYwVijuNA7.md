Now let me run the calibration search with a batch of queries:Now I have enough to write the final consolidated review.

---

## Summary

This paper revisits $\psi$-divergence distributionally robust optimization (DRO) with non-convex smooth loss functions. The central contribution is showing that the dual objective $\hat{\mathcal{L}}(x,\eta)$ satisfies a *partially generalized* $(L_0,L_1,L_2)$-smoothness condition and *partially affine variance* noise — i.e., $\mathcal{L}$ is standard $L_2$-smooth in $\eta$ while exhibiting generalized smoothness only in $x$, with variance affine in $|\nabla_\eta \mathcal{L}|^2$ (not $\|\nabla_z \mathcal{L}\|^2$). Leveraging this finer structure, the authors propose D-SGD-C, matching Jin et al. (2021)'s O(ε⁻⁴) complexity without momentum, and D-SPIDER-C, achieving the improved O(ε⁻³) complexity with in-expectation convergence.

---

## Strengths

- **Genuinely novel structural characterization (Lemmas 1 & 3).** The observation that $\mathcal{L}(x,\eta)$ is standard $L_2$-smooth in $\eta$ (not merely $(L_0,L_1)$-smooth), and that gradient variance is affine only in $|\nabla_\eta \mathcal{L}|^2$, is a precise and useful decomposition absent from prior work. This enables bounding $|\nabla_\eta \mathcal{L}|$ via standard smooth descent and then treating $x$ as effectively smoothly optimizable — breaking the circularity in Jin et al. (2021)'s analysis.

- **Simplified algorithm for O(ε⁻⁴) rate.** D-SGD-C achieves the same sample complexity as Jin et al. (2021) without requiring momentum. This is a meaningful algorithmic simplification arising directly from the more precise structural characterization. The proof sketch in Section 3.3.1 is clean and convincing.

- **O(ε⁻³) complexity with in-expectation convergence.** D-SPIDER-C improves over Jin et al.'s O(ε⁻⁴) rate by one order. Critically, the convergence is in expectation — stronger than the high-probability guarantee in Reisizadeh et al. (2023). The proof approach via Lemma 4 (cross-Lipschitz continuity of per-sample gradients) is technically sound.

- **Honest positioning of D-SGD-C.** The body of the paper clearly states D-SGD-C "matches" Jin et al.'s complexity; the improvement is in simplicity, not rate.

---

## Weaknesses

### Fatal
None.

### Major

- **Weak experimental validation relative to the "large-scale non-convex" framing.** The sole numerical experiment uses N = 2413 samples (2000 training), 34 input dimensions, and a regularized linear regression loss (Eq. in Section 4). This is not the "large-scale non-convex" setting the title and abstract build toward. The main theoretical motivation for stochastic algorithms is scalability when N is large — but at N = 2000, full-batch methods are equally cheap. No neural network task, image classification, or meaningful distributional shift evaluation is provided. This prevents evaluation of whether the theoretical advantages translate to the regimes actually motivating the paper, and stands in sharp contrast to accepted DRO papers at comparable venues that demonstrate results across tabular, vision, and language domains.

- **The stochastic estimator (line 191 / Eq. 16) introduces a $G$-scaling on $\eta$ absent from the original dual formulation.** The dual objective is $\hat{\mathcal{L}}(x,\eta) = \lambda \mathbb{E}[\psi^*\left(\frac{\ell(x,S)-\eta}{\lambda}\right)] + \eta$ (Eq. 5), but the stochastic estimator used throughout Section 3.3 is $\dot{\mathcal{L}}(x,\eta,S) = \lambda\psi^*\left(\frac{\ell(x,S)-G\eta}{\lambda}\right)+G\eta$, with $G$ (the Lipschitz constant of $\ell$) appearing as a factor on $\eta$. This discrepancy is never explained in the main text. If it is a reparametrization $\tilde{\eta}=G\eta$, it should be stated and the constants in Lemma 3 ($D_0, D_1, D_2$) and Theorems 3–4 should be derived in terms of the reparametrized variable. If it is not intentional, it could affect the correctness of the stochastic gradient estimates and the resulting complexity bounds.

### Minor

- **Abstract "outperform" claim is imprecise.** The abstract states algorithms "outperform the existing DRO method (Jin et al., 2021)." Section 4 clarifies that D-SPIDER-C has "similar performance" to Normalized-SPIDER (Chen et al., 2023), and that both proposed methods outperform SGD and *Normalized-SGD with momentum* (the Jin et al. method). While technically consistent, the unqualified "outperform" in the abstract overstates the empirical picture, particularly for D-SPIDER-C vs. Normalized-SPIDER.

- **Missing comparison to Adam and AdaGrad in experiments.** The paper's related work (Section 1.2, line 53) explicitly acknowledges that AdaGrad and Adam also apply to this setting; they are not compared against in Table 1/Figure 2. Their omission from experiments is unexplained and weakens the empirical positioning of D-SGD-C as a preferred method.

### Trivial

- **No analysis of the $\lambda$ dependence of complexity constants.** The constants $L_0, L_1, L_2, D_0, D_2$ all scale with $\lambda^{-1}$. As $\lambda \to 0$ (corresponding to the most robust DRO regime), these blow up. A brief remark on how the useful DRO regime interacts with algorithmic complexity would improve the paper's practical relevance.

---

## Nice-to-Haves

- Experiments on at least one non-convex neural network task to ground the "large-scale non-convex" framing.
- Convergence curves plotted in terms of total gradient oracle evaluations (not just iterations), since D-SPIDER-C uses larger batches at epoch boundaries — an honest comparison of O(ε⁻³) vs. O(ε⁻⁴) in practice.
- A brief formal argument (counterexample or inequality chain) for Remark 1's claim that partially generalized $(L_0,L_1,L_2)$-smoothness is strictly intermediate between standard $L$-smooth and $(L_0,L_1)$-smooth — currently stated without proof.
- Discussion of whether the partially-smooth structure extends to Wasserstein-distance DRO.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic "overclaim" about D-SGD-C**: The critic states that "D-SGD-C result matches Jin et al.'s O(ε⁻⁴) complexity — it does not improve upon it" and calls the abstract's "outperform" claim an overstatement of the D-SGD-C contribution. However, the paper itself explicitly says D-SGD-C "matches" the rate; the "outperform" language in the abstract refers to empirical convergence speed (Figure 2 shows D-SGD-C outperforming Normalized-SGD with momentum in practice, even at matched theoretical complexity). The main contribution of D-SGD-C is simplicity, which is clearly stated. The imprecision of the "outperform" phrasing is noted as a minor issue but this is not a major scientific error.

- **Harsh Critic Issue 3 (G-scaling as likely typo)**: Elevated to a real Major weakness in the main review because the discrepancy is present throughout Section 3.3 and Eq. 16 — it is consistent enough to be intentional, but the paper never explains the derivation. Retained as a substantive concern, not a nitpick.

- **Strength Finder generic strengths**: Removed "Empirical validation" as a standalone strength, since the experiments are thin and this was listed generically. The more specific theoretical strengths from the Strength Finder are incorporated.

- **Harsh Critic: "missing Adam/AdaGrad" as a major weakness**: Downgraded to Minor because it does not undermine the core algorithmic contributions; it is an experimental gap worth noting, not a flaw in the theory.

- **Harsh Critic: "λ dependence" analysis**: Moved to Trivial/Nice-to-Have; the paper makes no claims about the small-λ regime and this analysis would enrich but not correct the paper.

---

## Novel Insights

The paper's most genuinely novel observation is that the DRO dual variable $\eta$ plays a structurally different role from the primal variable $x$: $\mathcal{L}$ is *standard smooth* in $\eta$ with *bounded gradient variance* in $\eta$, while exhibiting generalized smoothness and affine variance only along the $x$-direction. This asymmetry means that bounding $|\nabla_\eta \mathcal{L}|$ via a single descent step effectively "collapses" the generalized-smooth problem to a standard-smooth one along $x$ — a realization that renders the normalized-gradient and momentum machinery of Jin et al. unnecessary. This is a clean, reusable insight: any DRO dual formulation satisfying similar separability structure may admit the same simplification, suggesting the technique could transfer to related $f$-divergence or Wasserstein-penalty DRO formulations.

---

## Suggestions

1. **Replace or supplement the life expectancy regression experiment** with a non-convex neural network experiment (e.g., a two-layer MLP on a standard benchmark subject to label noise or covariate shift), so that the "large-scale non-convex" framing is empirically supported.
2. **Explain the $G\eta$ stochastic estimator** explicitly in the main text — either as a deliberate reparametrization with a derivation of how gradient estimates remain unbiased, or correct it if unintentional.
3. **Add gradient oracle count to x-axis** in Figure 2 to allow an apples-to-apples comparison of D-SGD-C and D-SPIDER-C.
4. **Soften the abstract's "outperform" claim** to "outperform... in convergence speed, and our variance-reduced method achieves a strictly lower gradient complexity" for precision.

---

## Score and Decision

**Anchor papers and comparison:**

| Path | Avg Human Score | Comparison to this paper |
|------|-----------------|--------------------------|
| TTrzgEZt9s (DRO with bias/variance reduction) | 8.00 | Stronger: novel algorithm for spectral risk DRO, linear convergence guarantee, experiments across 3 domains (tabular/vision/language). This paper has narrower scope, weaker experiments, and only first-order stationary point guarantees. |
| 0h6v4SpLCY (Wasserstein DRO generalization) | 7.33 | Stronger: exact generalization bounds, broader class of losses including deep learning, accepted. More complete theoretical package. |
| sq5LLWk5SN (Mitigating overfitting in WDRO) | 6.50 | Somewhat stronger: addresses a different DRO problem with both theoretical and empirical robustness demonstration; accepted. |
| Zb6qOouUJO (Bilevel optimization LSVRG) | 5.75 | Close comparator — incremental adaptation of SPIDER/SVRG to a new setting (bilevel vs. DRO), solid theory, limited novelty. Rejected. Similar scope and depth. |
| BAX3NXJ6vU (Saddle-point bilevel optimization) | 5.33 | Similar tier — second-order stationarity for hierarchical optimization, somewhat more novel problem setting but comparable theoretical depth. Rejected. |
| viC3cpWFTN (Clip21 gradient clipping) | 5.33 | Related via gradient clipping; has more empirical content than this paper, similar theoretical depth. Rejected. |
| tsNLIBlG4p (Soft-clipping analysis) | 4.00 | Weaker — more incremental, weaker experiments, narrower claim. This paper is clearly stronger. |
| 1NYhrZynvC (Adaptive stepsize theory) | 2.50 | Much weaker — unclear contribution, near-trivial analysis. This paper is clearly stronger. |
| cCcaJzPAnb (Universal concavity-aware descent) | 3.80 | Much weaker — vague framing, limited rigor. |

**Assessment:** This paper's theoretical contributions are genuine but incremental — it refines the structural analysis of Jin et al. (2021) by separating the roles of $x$ and $\eta$, achieves a useful O(ε⁻³) improvement, and proves in-expectation convergence stronger than prior high-probability results. The structural insight is clean and reusable. However, the experiments are thin (one small regression dataset, no neural networks), the "large-scale" framing is not supported, and the $G\eta$ estimator discrepancy is an unexplained inconsistency in the main text. Compared to accepted DRO papers scoring 6.5–8 (which have richer experiments, linear convergence, and often address broader problem classes), and to rejected papers scoring 5–5.75 with similar incremental-but-correct theoretical profiles, this paper sits in the 5.0–5.5 range.

**Axes evaluation:**
- *Originality*: Moderate. The partial smoothness decomposition is a genuinely new observation in the DRO context; the algorithmic techniques (clipping, SPIDER) are standard.
- *Importance of research question*: Good. Non-convex DRO is an active and relevant area.
- *Claims supported by evidence*: Mixed. Theoretical claims are well-supported; the "large-scale" empirical claims are not.
- *Soundness of experiments*: Weak. Single small-dataset regression experiment.
- *Clarity*: Good in the theory sections; the $G\eta$ estimator and contributions section (parsed as empty) are unclear.
- *Value to research community*: Moderate. The structural insight may be useful for future DRO work, but the paper's reach is narrow.

**Final score: 5.0** — Borderline reject. The theoretical contribution is real and correct, but the experiments fail to support the paper's framing and the unexplained $G\eta$ estimator discrepancy should be resolved before publication.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>