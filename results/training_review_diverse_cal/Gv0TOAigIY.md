Now I have all the information needed. Let me carefully construct the final consolidated review.

## Summary

This paper studies how reflection symmetries in loss functions cause neural networks to collapse into low-capacity states during training. It proves two mechanisms through which symmetries impair expressivity (feature masking and effective dimension reduction) and proposes *syre*, a simple algorithm that adds a fixed random bias to parameters while retaining weight decay. The paper proves that this modification provably removes all reflection symmetries (Theorems 1–6) without requiring knowledge of the symmetry. Experiments on reparameterized linear regression, ResNet classification, β-VAEs, self-supervised learning, and continual learning demonstrate that syre prevents or mitigates collapse-related phenomena across diverse settings.

## Strengths

1. **Provable symmetry removal via a simple, model-agnostic modification.** Theorem 1 (Section 5.1) proves that adding a static random bias together with weight decay eliminates all reflection symmetries from the loss with probability 1, without requiring any knowledge of the symmetry structure. This is a stronger theoretical guarantee than prior heuristics (e.g., Lim et al. 2024) that only handle permutation symmetries and require architecture-specific changes. The extension to uncountably many symmetries (Theorem 2) and general finite groups (Theorem 3) with favorable scaling (logarithmic in group size, not exponential) is theoretically elegant.

2. **Clear theoretical explanation of how symmetries impair capacity.** Propositions 1 and 2 (Section 4) formally demonstrate that reflection symmetries mask the gradient kernel (removing features from learning) and reduce the effective parameter dimension during training. This provides a concrete mechanism for the "collapse" phenomenon beyond prior dynamical characterizations.

3. **Broad experimental validation across diverse, symmetry-prone tasks.** The method is tested on reparameterized linear regression (Fig. 2, right), posterior collapse in β‑VAEs (Fig. 5–6), loss of plasticity in continual learning in both supervised and RL settings (Fig. 7–9), low-rank representations in supervised learning (Fig. 4), and self-supervised learning (Table 1). The controlled benchmark experiment (Fig. 3) cleanly shows that syre is the *only* method among those tested that smoothly interpolates between low-symmetry and well-optimized solutions.

4. **Compatibility with standard training and minimal overhead.** The ResNet-18 experiment (Fig. 2, middle) confirms near-identical performance for σ₀ < 0.2, and the ridge regression analysis shows equivalence to standard weight decay when no symmetries are present. The implementation is a one-line code change.

## Weaknesses

### Fatal
None.

### Major
None that are truly structural. The following are moderate issues that weaken individual pieces of evidence but do not invalidate the core contribution.

### Minor

1. **Missing weight-decay-only baseline in the VAE experiment.** The VAE experiment (Section 6.4) compares "vanilla" against "syre + weight decay," but it is unclear whether the vanilla baseline includes weight decay. The text states "after we use weight decay and *syre*" (line 286), and Figure 6 labels compare "vanilla" vs "*syre*." Since the method intrinsically requires both weight decay and the bias, the relevant control is weight decay alone (same γ, no θ₀). Without this, the reader cannot attribute the improvement to the static bias specifically. This concern is partially mitigated by the RL continual learning experiment (Fig. 9), which explicitly controls for weight decay ("we use a weight decay of 0.002 for both PPO with weight decay and with *syre*," line 348), but the VAE experiment remains ambiguous.

2. **Imprecise quantitative claim in the SSL experiment.** The paper states that *syre* "can explain about 50% of the performance difference" between penultimate and last layer representations (Table 1 caption). Computing from the reported numbers: vanilla penultimate accuracy is 46.8%, vanilla last-layer is 22.2% (gap = 24.6 pp); syre best last-layer reaches 32.5%, closing 10.3 pp of the gap. This is ~42%, not 50%. While "about 50%" is a rough approximation, the gap is noticeable and the claim should be corrected or the computation should be shown.

3. **The advanced method for uncountable symmetries (Eq. 2, σ_D) is introduced but never empirically validated.** Section 5.2 develops a separate theoretical framework (the diagonal D matrix) for removing uncountably many symmetries (rotation, double rotation). The paper then states "we always set σ_D = 0 as we find only introducing σ_0 to be sufficient for most tasks" (line 223), and no experiment uses the advanced method. Since the theoretical distinction between countable and uncountable symmetries is a major structural component of the paper, the lack of any validation undermines this part of the contribution. The paper should either test the method on a task known to involve uncountable symmetries, or explain more directly why σ_D=0 suffices even in those cases (the SSL experiment involves rotation symmetry and the simple method worked, which is relevant but not acknowledged as such).

4. **No ablation isolating the interaction of σ₀ and γ in a single controlled setting.** The theory predicts that both the static bias and weight decay are necessary. However, the paper never varies σ₀ and γ independently in a single task to show: (a) without the bias (σ₀=0, only γ), the model still collapses; (b) with the bias (σ₀>0) but without γ, the effect disappears. The reparameterized linear regression experiment (Fig. 2, right) comes closest but uses vanilla SGD (which may not even include weight decay) as the "no syre" baseline. The theoretical mechanism would be substantially strengthened by a dedicated ablation.

### Trivial

1. **Fixed vs. resampled bias across trials.** The ResNet-18 experiment (Fig. 2, middle) averages over 10 trials but does not state whether θ₀ is fixed or redrawn per trial. If fixed, results may depend on the specific draw; if redrawn, variance across draws should be reported.

2. **Computational overhead not discussed.** Adding a bias requires storing θ₀ (same size as parameters) and adding it at each forward pass. The paper could note that this can be implemented as a modified initialization without extra storage for large models.

## Nice-to-Haves

- A simple synthetic experiment with a known reflection symmetry where the method's effect can be directly visualized (the model escaping the symmetric subspace vs. remaining trapped without syre).
- Discussion of whether the recommended σ₀ = 0.01/√d transfers across architectures and tasks beyond ResNet-18 on CIFAR-10, and how sensitive results are to deviations from this value.

## Removed Points

These points were flagged by reviewers but are removed per the verification and hard-rule criteria:

- **"W-fix comparison is unfair"** — Removed. The paper acknowledges W-fix is designed for permutation symmetry (line 249) and tests it on a rescaling symmetry problem to demonstrate that existing methods are limited while syre is general. This is a legitimate demonstration of scope, not an unfair comparison.

- **"Theorem 4 undefined when Pθ = 0"** — Removed. The theorem explicitly states the condition Pθ ≠ 0 (line 157), and the corollary immediately handles the Pθ = 0 case by bounding the gradient.

- **"Proof sketch not included"** — Removed per hard rule; the parser strips appendix content.

- **"Figure placement/formatting"** — Removed per hard rule on formatting artifacts.

- **"Missing continual learning baselines (EWC, SI, etc.)"** — Removed. The paper is not proposing a new continual learning algorithm; it uses CL as a testbed for the loss of plasticity phenomenon. The claim is that symmetry removal prevents rank collapse during sequential training, not that syre beats dedicated CL methods. Requesting EWC/SI comparisons is scope creep.

- **"The reviewer's 'suspiciously round' 46.8%"** — Removed. The number is cited from Chen et al. (2020) and is not suspicious.

- **"The method's effectiveness may depend on the nature of symmetries, not discussed"** — Removed. The paper discusses this directly via Theorem 5 (scaling with N) and the hyperparameter section.

## Novel Insights

None beyond the paper's own contributions. The review process did not surface any observation not already present in or directly derivable from the paper.

## Suggestions

1. Add a weight-decay-only control to the VAE experiment, and to any other experiment where it is absent, so the marginal benefit of the static bias is cleanly isolated.
2. Correct the "about 50%" claim in the SSL experiment to reflect the actual ~42% figure, or show the computation that leads to 50%.
3. Either validate the advanced method (Eq. 2) on a task with uncountable symmetries, or add a paragraph explaining why σ_D=0 empirically suffices even for cases like rotation symmetry (SSL experiment).
4. Run a single controlled experiment (e.g., the reparameterized linear regression) that independently varies σ₀ and γ to demonstrate the joint necessity of both components.
5. Clarify whether θ₀ is fixed or resampled across trials and report variance if resampled.

## Score and Decision

The paper makes a genuine theoretical contribution (provable symmetry removal via an elegantly simple method) and demonstrates it across a diverse set of practically relevant problems. The weaknesses are experimental gaps that weaken individual pieces of evidence but do not threaten the core claim. The advanced method for uncountable symmetries is the most significant loose end. With the suggested corrections and ablations, the paper would be a strong contribution. In its current form, it is still a solid paper that advances our understanding of how symmetry affects training.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>