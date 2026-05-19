- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes a theoretical and empirical framework linking the adversarial robustness of individual data points to the *perceived curvature* of the data manifold during neural network training. The authors define data sensitivity (a pointwise Lipschitz constant of the label map), connect it to Finsler-Haantjes curvature under a key assumption about perceived manifold distance, and provide empirical evidence via diffusion-model cloning and adversarial training experiments. The core idea — that non-robust regions correspond to regions of high perceived curvature, explaining why adversarial training remains weak there even when margins are large — is novel and interesting.

## Strengths

1. **Novel theoretical framing.** The paper introduces a formal connection between data robustness and perceived manifold curvature using metric geometry (rectifiable arcs, Finsler-Haantjes curvature). The construction of the data manifold via the arc-length metric avoids assumptions of differentiability or constant intrinsic dimension. This is a genuinely new perspective on why adversarial training underperforms in non-robust regions even when margins are theoretically sufficient. (Section 3, equations for $\tilde{d}$, $\tilde{\kappa}$, and $s_y$)

2. **Interesting empirical probe via diffusion models.** The cloning experiment (Figure 3, Table 1) is a creative way to probe manifold structure: clones of non-robust points show larger semantic changes relative to pixel changes compared to clones of robust points, which is consistent with the curvature hypothesis. The data that pixel distances are *smaller* for non-robust point clones while semantic changes are *larger* (Table 1, O:C and C:C columns) is genuinely non-trivial and supports the claimed high-curvature interpretation.

3. **Non-obvious practical result.** Focusing stronger adversarial training on just 1024 non-robust images (~0.005% of training data) yields a small but consistent improvement in test-set AutoAttack accuracy (~0.2 pp), which the paper notes is comparable to the gain from 800 additional epochs in the baseline (Table 2, rows 4-5). That such a tiny fraction of the data can produce a measurable global improvement is surprising and worth documenting, even if the effect size is small.

4. **Metric-geometry formalism for the data manifold.** The paper reframes the data manifold through rectifiable arcs and the length metric, circumventing issues of differentiability and varying intrinsic dimension. Theorem 1 shows Lipschitz continuity of the sensitivity functional under local constancy, ensuring robustness to small perturbations. (Section 3, Theorem 1)

## Weaknesses

### Fatal
None.

### Major

1. **The central theoretical link rests on an untested and debatable assumption.** The paper's core derivation — that the ordering of sensitivity values matches the ordering of perceived curvature — depends on the assumption that a model perceives $\tilde{d}_{\text{perc}}(y, p_i, p_j) = \delta(y)$ as a *constant* for all differently-labelled pairs (lines 75-77). The paper calls this the "main assumption" and justifies it by citing literature on random-label training (Zhang et al., 2016; 2021; Arpit et al., 2017, etc.). However, the jump from "networks can fit random labels" to "perceived manifold distance between any two differently-labeled points is a constant" is not logically entailed by those results and is never directly tested. The paper itself acknowledges the need for "additional empirical and theoretical evidence" (conclusion), which undercuts the claim of providing a "new and rigorous explanation" (contributions list). Without this assumption, the claimed monotonic correspondence between sensitivity and curvature collapses. This is a structural gap in the theoretical contribution.

2. **The experimental design does not isolate the curvature mechanism from generic hard-example mining.** The paper selects points for focused training based on sensitivity (which correlates with being non-robust/loss-incurring). The observed improvement could equally arise from any strategy that upweights difficult points — a well-known heuristic in adversarial training (e.g., margin-based or loss-based re-weighting). No ablation compares sensitivity-based selection to selection based on margin, current loss, confidence, or random selection under the same computational budget. Without such comparisons, the results do not distinguish the curvature explanation from a generic "focus on hard points" baseline. This undercuts the paper's central claim that the curvature mechanism drives the improvement.

3. **The main robustness improvements lack statistical rigor and the baseline comparison is ambiguous.** The reported improvements are approximately 0.2–0.4 percentage points in AutoAttack accuracy (Tables 2–4). No confidence intervals, standard deviations across multiple seeds, or significance tests are reported. The text mentions "new random seeds" for Tables 3 and 4 but does not specify how many seeds were used per setting or report variance. Given that state-of-the-art adversarial training results typically exhibit variance of 0.3–0.5 pp across runs, the claimed improvements could fall within noise. Furthermore, the paper mentions a "glitch" in the Wang et al. (2023) training pipeline (line 95) that it "circumvented and emulated" but never describes what the glitch was or how it was handled. This makes it difficult to assess whether the comparison to the baseline is fair, and is a reproducibility concern.

4. **Overclaiming relative to evidence.** The paper lists as its first contribution: "We provide a new and **rigorous** explanation for the weaker effect of adversarial training in regions of non-robust data" (line 25, emphasis added; also line 142). Given that the theoretical link depends on an untested assumption, and the empirical evidence does not isolate the proposed mechanism from simpler alternatives, the "rigorous" label is unjustified. The paper's framing would be more accurately described as proposing a novel hypothesis with supporting, but not definitive, evidence.

### Minor

1. **Theorem 1's local-constancy assumption is not discussed.** Theorem 1 assumes $y$ is locally constant around each $p_i \in \mathcal{D}$. Since $y$ is defined as a continuous extension of one-hot labels (line 47), this condition fails for points near class boundaries where the continuous label function must change. The paper does not address this limitation or test whether the condition holds for the points used in experiments. Theorem 1 is only a supporting result (showing local consistency of sensitivity), so this does not invalidate the paper's core claims, but it should be acknowledged.

2. **The diffusion model experiment provides supporting but indirect evidence.** The experiment uses a diffusion model to probe the data manifold's structure, which is conceptually distinct from the *classifier's* perception during adversarial training. While the results are consistent with the curvature hypothesis, they do not directly show that the classifier's internal geometry during training produces the claimed curvature distortion. The paper acknowledges this indirectly by using the phrase "seem to" (line 110), but the evidential gap between the diffusion model's behavior and the classifier's perceived curvature is worth flagging.

3. **The "800 epoch" comparison is not independently validated.** The paper claims the 0.2 pp improvement "amounts to the same boost gained by extending training for 800 epochs" based on results from Wang et al. (2023). This single-point comparison is not replicated in the paper's own experiments. While it is a reasonable illustrative comparison, it should be treated as approximate.

### Trivial
None.

## Nice-to-Haves

- Directly test the constant-$\delta$ assumption, e.g., by training on a simple 2D manifold where the true manifold distance is computable and measuring whether the model's internal representations collapse differently-labeled points to a constant distance.
- Compare sensitivity-based point selection against selection based on margin, loss, or random sampling with the same computational budget to distinguish the curvature mechanism from generic hard-mining.
- Report mean ± std over at least 3-5 random seeds for the main results in Tables 2-4.
- Describe the "glitch" in the Wang et al. pipeline and how it was circumvented/emulated.
- Discuss why doubling or quadrupling $s$ does not yield further improvements — this is an interesting saturation effect that could deepen the analysis.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh Critic: "The average pixel distances being smaller for clones of non-robust points is an odd result"** — The paper *does* discuss this (lines 110-111) and correctly interprets it as consistent with the curvature story (small pixel change + large semantic change = high curvature). The critic misunderstood the paper's own explanation. **Removed.**

- **Harsh Critic: "Theorem 1 is mathematically trivial"** — This is a subjective judgment, not a concrete, verifiable weakness. The theorem serves its purpose (showing local consistency of sensitivity under the stated conditions). **Removed.**

- **Harsh Critic: "The MDS visualizations are qualitative and do not provide a quantitative test of Theorem 1"** — The paper presents them as "visual evidence" (line 86), which is appropriate for qualitative support. The paper never claims they are a quantitative test. **Removed.**

- **Harsh Critic: "The sensitivity plots (Figure 2) ... are descriptive, not explanatory"** — The paper uses these plots as *motivation* for the relationship, not as an explanation. Descriptive analysis is valid for this purpose. **Removed.**

- **Strength Finder: Several generic or sycophantic claimed strengths** (e.g., "rigorous theoretical framing" overstates given the untested assumption; "improvement over SOTA across multiple settings" overstates given the small effect size). I have retained the concrete strengths (novel connection, diffusion experiment, practical result) and dropped or reframed the inflated ones.

## Novel Insights

A genuinely interesting observation emerges from the interaction of the diffusion-model cloning experiment and the adversarial training results: the paper shows that non-robust points occupy regions where pixel-space distances understate semantic differences (high curvature), and that a targeted training emphasis on just 1024 such points (0.005% of data) produces measurable improvements on *unseen* test data. This suggests that the manifold's local geometry in these regions acts as a bottleneck for robust generalization, and that relieving this bottleneck at a few key points has global effects. This is a non-trivial finding that goes beyond straightforward hard-example mining intuition, even if the mechanism is not yet cleanly isolated.

## Suggestions

1. **Distinguish from hard-mining explicitly.** Add an ablation comparing sensitivity-based selection to margin-based, loss-based, and random selection. If sensitivity selection outperforms, it directly supports the curvature mechanism. If all hard-point strategies perform similarly, the paper should reframe its contribution accordingly.

2. **Test the constant-$\delta$ assumption.** Even a simple synthetic experiment (e.g., on a 2D Swiss roll or concentric spheres with known geometry) measuring the model's internal feature distances between differently-labeled points would substantially strengthen the theoretical claim.

3. **Provide statistical rigor.** Report means and standard deviations over at least 3 seeds for Tables 2-4, and explain the "glitch" in the baseline pipeline for reproducibility.

4. **Tone down the "rigorous" claim.** The paper's theoretical contribution is more accurately described as a novel hypothesis with a formal framework, not a rigorous proof. Adjusting this language would better match the evidence presented.
