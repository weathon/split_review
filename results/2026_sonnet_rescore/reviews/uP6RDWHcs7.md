## Summary

Marginal Flow is a density estimation framework that defines a model $q_\theta(\mathbf{x}) = \frac{1}{N_c}\sum_{i=1}^{N_c} q(\mathbf{x}|\mathbf{w}_{\theta,i})$ by marginalizing latent parameters $\mathbf{w}$ sampled from a learnable distribution $q_\theta(\mathbf{w})$, implemented via an unconstrained MLP. By avoiding bijection constraints, Jacobian computation, and ODE solvers, the model provides efficient density evaluation and single-step sampling, with the flexibility to learn lower-dimensional manifolds and adapt to non-Gaussian families (e.g., Wishart). Experiments demonstrate faster training convergence on synthetic 2D datasets, application to simulation-based inference, Wishart mixture modeling, and manifold learning in VAE latent spaces.

---

## Strengths

- **Efficient density evaluation and single-step sampling without architectural constraints (Table 1, Figure 3):** Marginal Flow avoids Jacobian computation, ODE solvers, and bijectivity constraints. Figure 3 empirically confirms orders-of-magnitude speedup over NF, FM, and FFF for both sampling and density evaluation across dimensions up to $10^5$. The advantage is real and well-demonstrated.
- **Marginalization prevents collapse to a finite GMM (Figure 1):** The paper clearly shows that resampling $\mathbf{w}_i$ from $q_\theta(\mathbf{w})$ at each iteration yields a smooth continuous mixture, while directly optimizing a fixed set of $N_c$ components collapses to a coarse GMM. This distinction is well-motivated in Section 2.1.
- **Manifold learning capability demonstrated cleanly (Figure 4):** By choosing a lower-dimensional base distribution ($m < d$), Marginal Flow recovers a 1D spiral manifold embedded in 2D that competing methods (NF, FM, FFF) either cannot handle or learn incorrectly. This is a concrete, specific advantage with a clean qualitative demonstration.
- **Fast training convergence (Figure 7):** Test log-likelihood curves across five synthetic datasets show Marginal Flow reaching higher values in substantially less wall-clock time than NF, FM, and FFF. This is a consistent and meaningful finding.
- **Wishart adaptation demonstrates genuine framework flexibility (Section 4.3):** Switching $q(\mathbf{x}|\mathbf{w})$ to a Wishart distribution for positive-definite matrix modeling requires minimal modification and outperforms NF substantially (orders of magnitude better KL in Figure 9 left). The $100 \times 100$ experiment ($d=5050$) is a genuine scaling advantage.
- **Flexible training objectives (Section 2.3):** Because the model supports both efficient density evaluation and efficient sampling, it can be trained via both forward and reverse KL divergence — a genuine advantage over NF (slow sampling) and FM (no exact density) that is validated in Figure 8.

---

## Weaknesses

### Fatal
None.

### Major

- **"Exact likelihood" framing is imprecise and misleading in Table 1 and the abstract.** The paper defines its model as Eq. 2: a finite average of $N_c$ kernels with freshly resampled $\mathbf{w}_{\theta,i} \sim q_\theta(\mathbf{w})$ at each evaluation. The paper itself states: "the parameters $\mathbf{w}_{\theta,i}$ are not fixed themselves but rather *resampled* from $q_\theta(\mathbf{w})$ at each iteration." This means that calling $q_\theta(\mathbf{x})$ twice at the same point $\mathbf{x}$ yields different values — the density is a stochastic Monte Carlo approximation of the ideal marginal $\int q(\mathbf{x}|\mathbf{w})q_\theta(\mathbf{w})\,d\mathbf{w}$. A normalizing flow, in contrast, yields a deterministic, reproducible density at every point via the change-of-variables formula. Checking the same "Efficient exact likelihood" box for both methods in Table 1 equates two fundamentally different properties. The paper's statement that "evaluation does not require inverting $f_\theta$, computing $\det \mathcal{J}_{f_\theta}$ or solving an ODE" is accurate — but conflates the *mechanism* of evaluation with its *exactness*. This affects the paper's central differentiator. The fix is honest framing: the model evaluates a closed-form Monte Carlo estimator of the marginal density (not requiring ODE or Jacobian), with accuracy controlled by $N_c$. This would still clearly distinguish the method from VAEs, FM, EBMs, and FFF while being technically sound.

- **Experimental evaluation is confined to 2D synthetic datasets and niche applications; no standard density estimation benchmarks.** The quantitative results that demonstrate competitive performance vs. prior art (SBI, Reverse KL on synthetic datasets) are either 2D or deferred to the appendix. There are no experiments on widely-used tabular benchmarks (e.g., UCI-style density benchmarks used in the NF/FM literature), which would allow direct numerical comparison to published baselines. All experiments in the main text are either qualitative (Figures 4, 5, 6, 10, 11), convergence speed on 2D datasets (Figure 7), or niche (Wishart matrices). The state-of-the-art SBI claim is asserted in Section 4.2 with results "in the Appendix in Figure 14 due to space constraints" — the main paper cannot substantiate this claim without the reader consulting the appendix. The paper would be significantly stronger with at least one widely-used high-dimensional tabular density benchmark in the main text.

### Minor

- **The $N_c$ hyperparameter is neither ablated nor analyzed in the main text.** Runtime, accuracy, and training dynamics all depend on $N_c$, yet the value used in Figure 3 is not stated in the main text (the paper defers to Appendix A.3.1). No ablation over $N_c$ appears in the main paper. Since $N_c$ controls the fundamental cost-accuracy tradeoff of the Monte Carlo approximation, practitioners cannot calibrate the method without this guidance. An ablation showing how test log-likelihood and density estimate variance vary with $N_c$ would substantively strengthen the paper.

- **The Figure 5 evaluation regime (150 training points, uniform base) is favorable to Marginal Flow.** The paper asserts "For a fair comparison, all models use a uniform base distribution." However, a uniform base is better suited to Marginal Flow — which needs to cover a multi-modal target by sampling kernel centers — than to flow-based models, which must deform a unimodal base into multiple modes through a smooth map. The caption does not acknowledge this potential asymmetry. This comparison is illustrative at best; its generalizability to realistic multi-modal learning scenarios is unclear.

- **Analysis of why Marginal Flow converges faster is absent.** Figure 7 shows a significant convergence speed advantage, but the paper offers no explanation of whether this is due to simpler gradient computation, fewer parameters, or a better-conditioned loss surface. This is not fatal, but a brief analysis would transform an empirical observation into an actionable insight.

### Trivial
None beyond parser formatting artifacts.

---

## Nice-to-Haves

- **Variance analysis with $N_c$:** A figure showing how the variance of $q_\theta(\mathbf{x})$ across repeated evaluations scales with $N_c$ — and how this variance affects downstream metrics like test log-likelihood — would provide practitioners with principled guidance on choosing $N_c$ and would directly address the "approximate vs. exact" framing issue.
- **Universality conditions:** The claim in Section 2.1 that the marginal $q(\mathbf{x})$ is "universal for many families" relies on the Micchelli (2006) citation without discussing what conditions on $q_\theta(\mathbf{w})$ (e.g., architectural expressiveness of $f_\theta$) are actually needed. Even a brief discussion would strengthen the theoretical grounding.
- **Revising Table 1 language:** Distinguishing "no Jacobian/ODE required for density evaluation" (accurate) from "exact density" (imprecise) in Table 1 would eliminate the main framing problem while preserving the substantive advantage being claimed.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Connection to deep kernel density estimation / neural KDE (Harsh Critic §2):** The observation that Marginal Flow with a Gaussian kernel resembles KDE with a learned generator is conceptually interesting but constitutes a missing-related-work criticism. Under the Hard Rules, missing related works are excluded because external sources cannot be confirmed. The claim that prior "deep KDE" methods exist as baselines is not verifiable without external sources.

- **NF underfitting in Figure 9 may be due to insufficient tuning (Harsh Critic §Section 4.3):** The critic speculates that NF underfits the Wishart mixture because of insufficient hyperparameter search effort rather than architectural limitations. This is speculative; the paper presents empirical comparisons, and dismissing them as possibly under-tuned requires evidence not in the paper.

- **MNIST/JAFFE "easier problem" concern (Harsh Critic §Section 4.4):** The critic argues that doing manifold learning in a 20D/10D latent space is the "easier problem" since VAE has already done the hard work. The paper explicitly frames Section 4.4 as demonstrating manifold learning *in latent spaces of images*, which is what it does. The concern is scope creep.

- **Strength: "multi-modal targets" (Strength Finder):** This strength (Figure 5) conflicts with the verified weakness that the evaluation regime (150 points, uniform base distribution) is not clearly fair. Demoted from strength.

- **Strength: "disentanglement" in MNIST/JAFFE (Strength Finder):** The disentanglement observation in Figures 10–11 is qualitative and subjective, and the JAFFE experiment has only 214 images. This is too weak a basis for a concrete strength.

---

## Novel Insights

The most genuinely novel insight the paper contributes — beyond efficient density estimation — is the demonstration that choosing the *support geometry* of the base distribution ($m < d$) implicitly specifies the dimensionality of the density's support, enabling simultaneous density learning and manifold discovery without post-hoc dimensionality reduction. This is cleanly illustrated in Figure 4 and Section 4.3 (Wishart manifold). The combination of (a) no architectural constraint on $f_\theta$, (b) exact evaluation of the kernel mixture without Jacobians or ODEs, and (c) free choice of $q(\mathbf{x}|\mathbf{w})$ is a genuinely useful trifecta that opens the framework to domains (positive-definite matrices, conditional manifolds) that most generative models cannot address without non-trivial engineering.

---

## Suggestions

1. **Reframe "exact likelihood" → "closed-form Monte Carlo density evaluation"** in the abstract, Table 1, and conclusions. Acknowledge that evaluation is a finite-sample approximation of the true marginal, add a brief characterization of how the approximation error scales with $N_c$, and distinguish this from NF's deterministic evaluation.
2. **Add a standard tabular density benchmark** (e.g., at least one common benchmark used in the NF/FM literature) to the main text, even as a single table. This would let readers directly compare the method's density quality against published numbers.
3. **Move the SBI results summary to the main text.** Section 4.2 currently makes a "state-of-the-art" claim supported only by an appendix figure. Even a summary table (top-level C2ST scores vs. baselines) in the main text would make the claim verifiable.
4. **Add an $N_c$ ablation.** Show test log-likelihood and density variance as a function of $N_c$ for one representative task, and provide a concrete recommendation for practitioners.

---

## Score and Decision

**Originality:** The framework is simple and elegant, with a genuine insight (marginalization over learned parameter distributions avoids all major bottlenecks). The connection to mixture models is acknowledged; the connection to KDE is implicit and unaddressed but not a blocking concern. Moderate-high originality.

**Importance:** Density estimation with efficient exact evaluation and flexible architecture is genuinely valuable for scientific applications (SBI, manifold learning on structured objects). The problem is important and the proposed solution is practical.

**Claims supported:** The speed and flexibility claims are well-supported. The "exact likelihood" claim is imprecise. The state-of-the-art SBI claim is only in the appendix. The quantitative evidence in the main text is primarily on 2D synthetic tasks.

**Soundness of experiments:** The synthetic experiments are solid; the Wishart experiment is compelling; MNIST/JAFFE are demonstrative but qualitative. The lack of standard benchmarks limits the assessment of how competitive the method is on non-toy problems.

**Clarity:** The paper is clearly written and well-organized. The model is presented concisely and the figures support the narrative.

**Value to the community:** Moderate-to-high. The framework is simple to implement and offers a genuine practical advantage for applications needing both fast density evaluation and flexible architecture. The "exact" framing issue, if corrected, would not reduce the method's utility.

Overall: a promising, practically useful contribution with real empirical advantages, hindered by a misleading central framing claim and a limited quantitative evaluation on standard benchmarks. Borderline accept; the core contribution is real but the paper needs honest reframing of its main claim and stronger empirical validation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>