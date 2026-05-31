## Summary

This paper investigates the effect of the L0 hyperparameter (average number of active latents per token) on Sparse Autoencoders (SAEs) trained for LLM interpretability. Through controlled toy model experiments and real LLM validation on Gemma-2-2b and Llama-3.2-1b, the authors demonstrate that: (1) an L0 below the "true" data L0 causes SAEs to mix correlated and anti-correlated features, producing polysemantic latents; (2) an L0 too high also degrades feature recovery through degeneracy; (3) standard sparsity-reconstruction tradeoff plots are actively misleading since an incorrect SAE can out-reconstruct a correct SAE at low L0; and (4) a new proxy metric—decoder pairwise cosine similarity, $c_\text{dec}$—can identify the correct L0 and coincides with peak sparse probing performance in LLM SAEs.

---

## Strengths

- **Clear causal demonstration via toy models.** The toy model setup is well-designed: ground-truth features are known and orthogonal by construction, enabling direct measurement of feature mixing. The authors show that even initializing a low-L0 SAE at the correct (ground-truth) solution leads gradient descent to corrupt it (Section 3.3). This makes the causal story for *why* low L0 fails compelling.

- **Important invalidation of a community-standard evaluation.** The sparsity-reconstruction tradeoff plot is the dominant evaluation tool across Cunningham et al. (2024), Gao et al. (2024), and Rajamanoharan et al. (2024). Figure 4 demonstrates concretely that an SAE with ground-truth correct features scores *worse* on this metric than an incorrect SAE at low L0 — meaning the field's standard benchmark would cause practitioners to *discard* a correct SAE. This is a strong and counterintuitive result.

- **Simple, practical metric with validation.** $c_\text{dec}$ (Eq. 4) is cheap to compute (no additional data required beyond the decoder itself), interpretable, and validated on both toy models (Figure 6) and real LLMs (Figures 8, 9). The correspondence between the $c_\text{dec}$ elbow and peak k-sparse probing performance across both models and two layers is a meaningful empirical validation without requiring ground-truth features.

- **Coverage of both SAE architectures.** The paper validates findings on both BatchTopK and JumpReLU SAEs, and interestingly finds that JumpReLU SAEs are more robust at high L0 due to per-latent threshold flexibility — a mechanistically interesting and novel secondary finding.

- **Direct practical relevance.** The observation that commonly deployed SAEs on Neuronpedia largely use L0 < 100 (Appendix A.13), and that the authors' metric suggests the optimal value is closer to 200–300 for the models tested, is directly actionable.

---

## Weaknesses

### Fatal
None.

### Major

1. **$c_\text{dec}$ does not always provide a clear, unique optimum.** The authors acknowledge that for Gemma-2-2b layer 5 (Figure 8 top-left), the curve has a "long shallow region" with no clean elbow, and the global minimum is in that shallow region rather than at an identifiable inflection. The practical procedure for identifying the "correct L0" from $c_\text{dec}$ reduces to finding an "elbow just before the jump," which is visually interpretable but lacks an automatic or principled threshold. For practitioners working in settings where the curve lacks a clear shape, the metric may offer limited guidance.

2. **The "true L0" concept does not generalize cleanly to real LLMs.** The paper's core claim rests on the toy model paradigm — a data-generating process with known, discrete, orthogonal features. In real LLMs, features may be graded, non-orthogonal, or non-linear (cf. Engels et al., 2025, cited in the paper). There is no model-level ground truth, so the claim "most SAEs have too low an L0" is validated only through sparse probing performance — a proxy whose correspondence to true feature disentanglement is not demonstrated. The paper would be strengthened by discussing how robust the toy model conclusions are when the LRH holds only approximately.

3. **LLM experiments cover limited scope.** Only two LLMs (Gemma-2-2b and Llama-3.2-1b) and a small number of layers are tested. Patterns like whether the $c_\text{dec}$ curve has a clean minimum or a flat region likely vary by model, training data, and layer depth. Without broader evaluation, it is difficult to assess how consistently $c_\text{dec}$ elbow detection generalizes.

### Minor

1. **Mechanism for high-L0 failure is less explained than low-L0 failure.** Section 3.2 shows that high L0 causes degenerate solutions (Figure 1 right panel), but the theoretical explanation is briefer than for the low-L0 case. The asymmetry (high L0 corrupts some latents, low L0 corrupts all) is noted but not fully explained.

2. **The JumpReLU "sticking" observation (Section 3.6)** — that a wide range of sparsity coefficients $\lambda_s$ cause the SAE to naturally settle near the correct L0 — is presented as a positive finding, but it also implies that JumpReLU may naturally find the right L0 without the need for a sweep. This apparent advantage over BatchTopK is not fully analyzed: if JumpReLU self-corrects, does the $c_\text{dec}$ metric remain necessary for JumpReLU SAEs?

3. **The sparse probing benchmark used as validation (Kantamneni et al., 2025)** may itself be sensitive to L0 in ways that create circularity. The paper does not discuss whether k-sparse probing F1 is a reliable ground truth for "correct feature recovery," or whether it too could be optimized by polysemantic latents under some circumstances.

### Trivial

- Minor grammatical artifact in Section 3.5: "We pairwise calculate similarity $c_\text{dec}$…"

---

## Nice-to-Haves

- An automated rule or threshold for identifying the $c_\text{dec}$ elbow (e.g., first derivative, curvature threshold) would make the metric more practically actionable than visual inspection.
- Testing $c_\text{dec}$ on publicly released SAEs (e.g., Anthropic's open-source SAEs, Eleuther SAEs) would allow the community to immediately apply the diagnosis.
- A brief discussion of whether the "correct L0" is expected to scale predictably with model size, layer depth, or training data distribution would help practitioners plan hyperparameter sweeps.

---

## Novel Insights

The most genuinely novel contribution is the inversion of the dominant SAE evaluation paradigm. The sparsity-reconstruction tradeoff plot has been treated as a reliable proxy for SAE quality across essentially all prominent SAE papers. This work provides a concrete, reproducible counterexample: in toy models with known ground-truth features, an incorrect SAE (with polysemantic, feature-mixing latents) achieves *better* variance explained than the ground-truth correct SAE at low L0. This means the field's standard benchmark is not merely imperfect — it is directionally wrong in the regime where most deployed SAEs operate. The secondary insight that negative correlations (which are ubiquitous in language) are particularly damaging when L0 is too low (producing e.g. a negative "Harry Potter" component in a "French poetry" latent) provides an interpretability-relevant intuition that grounds the formalism.

---

## Suggestions

- Provide a concrete procedure (not just visual inspection) for using $c_\text{dec}$ in practice: e.g., "train SAEs at L0 values $\{50, 100, 200, 400, 800\}$; select the lowest L0 where $c_\text{dec}$ stops declining sharply."
- Evaluate whether $c_\text{dec}$ is sensitive to SAE width $h$ — the number of latents may affect pairwise similarity independently of L0 correctness.
- Expand LLM experiments to at least 3–4 layers per model, and ideally one additional model, to characterize how reliably the $c_\text{dec}$ elbow identifies the optimal L0 across different settings.

---

## Score and Decision

The paper makes a clear, well-supported, and practically important contribution. It identifies a fundamental flaw in the community's dominant evaluation methodology and provides an alternative metric grounded in theory and validated empirically. The main limitations — the metric's ambiguity in some practical settings and the gap between toy model assumptions and LLM reality — are genuine but do not invalidate the core findings, which are supported by converging evidence from toy models, two LLMs, and two SAE architectures. This is solidly above-average work for the interpretability community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>