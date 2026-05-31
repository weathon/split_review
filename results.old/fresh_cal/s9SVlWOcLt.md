Now I have all the information needed. Let me compose the final consolidated review.

## Summary

The paper introduces Proto Successor Measures (PSM), a framework that represents successor measures (and thus all possible solutions of RL in a given MDP) as an affine combination of policy-independent basis functions plus a bias term. The key theoretical claim (Corollary T1) is that any successor measure can be written as $\sum_i \phi_i w_i^\pi + b$, where $\phi_i$ and $b$ are policy-independent. A practical algorithm is derived via a discrete codebook of policies that reduces basis learning to a single-player optimization, and inference for a new reward reduces to solving a linear program over the basis coefficients. Experiments on gridworld, FetchReach, and continuous control benchmarks (Walker, Cheetah, Quadruped, Pointmass) show competitive or superior zero-shot performance compared to Laplacian, Forward-Backward (FB), and HILP.

## Strengths

1. **Theoretically grounded affine-set characterization of successor measures.** Corollary T1 proves that successor measures satisfy a linear (Bellman flow) equation, so they form an affine set that can be represented by policy-independent basis functions plus a bias. This is mathematically correct and well-articulated in Section 4. The proof is derived from the linearity of the Bellman flow constraint and is a valid foundation for the method. This goes beyond prior work (FB, Laplacian) which either ties representations to the reward/optimal policy or relies on policy-dependent eigenvectors.

2. **Single-player optimization via discrete codebook.** Section 5.2 introduces a practical seed-based policy generation scheme that converts a two-player game into the single-player objective in Equation (6): $\argmin_{\Phi,b,w(z)} \mathbb{E}_z[L^{\pi_z}(\Phi,b,w(z))]$. This makes learning the basis functions computationally feasible from reward-free offline data. The connection between the theoretical affine structure and a concrete learning algorithm is a genuine contribution.

3. **Theorem T2 — stronger representation capacity than value-function bases.** The paper shows that for the same dimensionality, the set of value functions expressible via the successor-measure basis strictly contains those expressible via a value-function basis (like PVFs). This formalizes an advantage over spectral/value-function-basis methods.

4. **Competitive empirical results across multiple domains.** Table 1 shows PSM achieving the highest average scores across Walker (689.07 vs. FB 594.67), Cheetah (607.61 vs. FB 586.31), Quadruped (618.74 vs. FB 568.64), and Pointmass (514.09 vs. FB 427.34), all with representation dimension $d=128$ and averaged over 5 seeds. The gridworld visualizations (Figure 2) qualitatively demonstrate sharper Q-functions and fewer policy errors than baselines.

5. **The paper is clearly written and well-organized.** The progression from linear programming preliminaries → affine space theory → practical algorithm → experiments is logical and easy to follow. The toy example in Section 4 is helpful for building intuition.

## Weaknesses

### Fatal
None.

### Major

1. **The discrete codebook's policy coverage is unanalyzed.** The paper claims (line 257) that the seed-based approach "provably samples from among all possible deterministic policies uniformly." While this statement is correct about the sampling *distribution* (each sampled policy is uniformly drawn), it says nothing about how many seeds are needed for the learned basis $\Phi, b$ to span the full affine set of successor measures. In practice, a finite number of seeds covers only a tiny fraction of the $|A|^{|S|}$ possible deterministic policies. The paper provides no analysis — theoretical or empirical — of how the number of seeds affects representation quality, how seeds are sampled, or what coverage guarantees exist. Without this, the central claim that the basis can represent *any* successor measure for zero-shot RL rests on an unverified assumption. This is the single most significant gap in the paper.

2. **Continuous-control experiments use a restricted decomposition that is not the full PSM.** The paper adopts $\phi(s,a,s^+) = \phi_\psi(s,a)^T \varphi(s^+)$ for all continuous-control experiments (Section 5, lines 371-373). The paper acknowledges this "reduces the representation capacity of the basis" (line 302) and says "PSM does not assume this decomposition and can learn a larger representation space." However, the empirical results that support the paper's claimed improvements over FB are all obtained with this restricted decomposition — which is structurally identical to FB's forward-backward factorization. The paper does not isolate whether the improvements come from PSM's algorithmic differences (e.g., the codebook sampling, the inference procedure of Equation 8) or simply from implementation/tuning differences. A controlled ablation is needed to attribute the gains to PSM's method.

3. **The novelty of the core theoretical result is overstated.** That successor measures form an affine set is a direct consequence of the Bellman flow equation being linear. The paper presents this as a novel theoretical insight, but it follows immediately from the linear programming formulation of RL (which the paper cites). The actual novelty is in *learning* these basis functions from data. The paper should more clearly delineate what is a standard mathematical observation versus the novel algorithmic contribution. The distinction matters for assessing the paper's contribution.

### Minor

1. **Theorem T2's notation is imprecise.** The statement writes $\{span\{\Phi\}r\}$ and $V^\pi=\sum_{s^+}[\Phi w^\pi.r(s^+)]$, mixing a dot product with what appears to be element-wise multiplication. This makes the theorem difficult to interpret rigorously. While the high-level claim (successor-measure bases represent a superset of value-function bases) is plausible, the theorem as stated is not formally precise.

2. **The inference procedure (Equation 8) uses $\min(\Phi w + b, 0)$ as a penalty for non-negativity, but the paper does not discuss how to guarantee convergence to a feasible $w$.** The min-max optimization in the Lagrangian dual may not yield a $w$ that strictly satisfies $\Phi w + b \geq 0$ with finite optimization.

3. **No analysis of representation dimension.** The paper's limitations section acknowledges this is unknown, but the experiments provide no ablation varying $d$ or guidance on how to choose it. Given that the representation dimension directly affects the capacity to span the affine set, this is an important missing analysis.

4. **The experimental claim of "marked improvement" over baselines is unevenly supported.** While PSM achieves the highest averages on most environments, there are individual tasks where it underperforms (e.g., Pointmass Reach Top Left: HILP 944.46 vs. PSM 831.43; Cheetah Run Backward: FB 307.07 vs. PSM 286.13). Several tasks show overlapping standard deviations (e.g., Cheetah Walk Backward: FB 980.76±2.32 vs. PSM 980.90±2.04). The headline claim is fair as an average trend but should be qualified.

### Trivial

None beyond typical formatting issues attributable to the PDF extraction process.

## Nice-to-Haves

- **Isolate the source of improvement over FB.** Since the continuous-control experiments use the same forward-backward decomposition as FB, an ablation comparing (a) PSM codebook + PSM inference vs. (b) FB latent-variable sampling + PSM inference vs. (c) PSM codebook + FB inference would clarify which component drives the gains.
- **Provide coverage analysis for the codebook.** Even an empirical study (how does performance vary with number of seeds?) would significantly strengthen the paper.
- **Evaluate robustness to limited dataset coverage.** The paper assumes full dataset coverage. Testing on datasets with partial coverage would assess practical applicability.
- **Report computational cost.** Training time and number of seeds/policies used for the codebook are not discussed, making it hard to assess practical trade-offs.

## Removed Points

- **"FB uses policy evaluation, not optimality backups"** — The paper claims FB uses Bellman optimality backups (line 72, 366). Whether this is accurate depends on the specific FB implementation. I cannot verify this without the FB paper, and the paper under review is entitled to describe cited work as it understands it.
- **"FB scores are much lower than reported in the original FB paper"** — Not verifiable from the paper under review. Baseline performance depends on many factors (dataset, hyperparameters, etc.), and the paper states it controls for representation dimension, discount factor, and inference procedure (line 417).
- **"No statistical significance tests"** — Generic criticism applicable to most ML papers. Standard deviations are reported. The field norm for large-scale benchmarks is single-run evaluation with error bars.
- **"The affine structure is not novel"** — While the linear programming view is standard, explicitly connecting it to a learnable basis representation for zero-shot RL is the paper's contribution. The paper cites the standard LP references; the novelty claim is about the overall framework, not the mathematical fact itself.
- **"Missing related works"** — I cannot verify missing citations without external sources.
- **"Formatting/presentation nitpicks"** — These are parser artifacts, not author errors.
- **Strength: "This paper addressed an important problem"** — Generic, not specifically supported by concrete evidence.
- **Strength Finder's claim of "sharpest Q-functions"** — Retained as a genuine strength since it's backed by Figure 2.

## Novel Insights

None beyond the paper's own contributions. The two reviews provide useful complementary perspectives: the harsh critic correctly identifies the codebook coverage gap and the decomposition issue as significant concerns, while the strength finder correctly identifies the affine-set characterization and practical optimization as genuine contributions. The key tension is between the paper's strong theoretical framework and the unverified practical instantiation — a gap that future work should address.

## Suggestions

1. **Analyze the codebook coverage empirically.** Vary the number of seeds/policies used during training and measure how the downstream zero-shot performance changes. This would directly address the most significant concern about the method.
2. **Add an ablation study for continuous control.** Compare PSM with the decomposition vs. without it, and compare PSM's codebook sampling against FB's latent-variable sampling while holding the inference procedure constant.
3. **Clarify Theorem T2 notation.** Provide a clean mathematical statement and either include a proof sketch or reference to an appendix.
4. **Include a sensitivity analysis on representation dimension $d$.** Show how performance varies across a range of $d$ values to provide practical guidance.
5. **Discuss the number of seeds/policies used** and the computational budget for training to contextualize the results.

## Score and Decision

Overall, the paper presents a theoretically sound framework (affine structure of successor measures) with a creative practical instantiation. The theoretical contribution is solid: Corollary T1 is mathematically correct and provides a clean characterization of the representation space. The empirical results across multiple environments are competitive and suggest the method works in practice. The main weaknesses — the unanalyzed codebook coverage and the reliance on a restricted decomposition in continuous-control experiments — are significant but addressable. They do not invalidate the core contribution.

The paper would benefit from additional analysis and ablations, but in its current form it represents a meaningful step toward principled zero-shot RL representations.

**Originality:** Good. The affine-set view of successor measures is a distinct perspective from prior work (FB, Laplacian, PVFs). **Importance of research question:** High. Zero-shot RL is an important open problem. **Claims support:** Adequate. The theoretical claims are well-supported; the empirical claims are supported on average but would benefit from tighter controls. **Soundness of experiments:** Fair. The baselines are reasonable but the decomposition issue weakens the comparison. **Clarity:** Good. The paper is well-structured and clearly written. **Value to community:** Positive. The framework provides a clean theoretical lens and a practical baseline for future zero-shot RL research.

I rate the paper as a borderline accept with major revisions recommended.

<score>6.0</score>
<decision>Accept</decision>