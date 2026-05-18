Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual content. Let me compose my final consolidated review.

## Summary

This paper proposes FI (First-order local Influence), an information-geometric stability measure for LLMs/VLMs that quantifies local sensitivity to perturbations in inputs or parameters. The key theoretical contribution is reparameterization invariance (Theorem 2.3), which avoids scaling artifacts that plague Euclidean-gradient measures like the Jacobian norm. Experiments demonstrate that FI can identify vulnerable input pixels in VLMs, locate fragile parameters via sparsification, and guide channel-selection strategies for quantization and model merging. However, the empirical validation is substantially weaker than the paper's claims warrant.

## Strengths

1. **Invariance under reparameterization (Theorem 2.3)** — A genuine theoretical advantage. The paper correctly identifies that neural networks with ReLU activations have weight symmetries (scaling invariance), and proves that FI remains constant under diffeomorphic reparameterizations while standard measures like the Jacobian norm do not. This addresses a known limitation of Euclidean-gradient-based importance measures and is well-motivated via the Fisher-Rao metric on the perturbation manifold.

2. **Clear mathematical framework** — The construction of the perturbation manifold, the metric tensor \(G_\omega\), and the closed-form solution (Theorem 2.4) are presented rigorously. The handling of low-rank \(G_\omega\) via compact SVD and reparameterization to \(\nu = \Lambda_0 V_0^\top \omega\) (Section 2) provides a tractable computational path for the otherwise problematic low-dimensionality issue in LLMs.

3. **FI identifies fragile parameters more effectively than random selection** — Section 3.2 (Figure 3) shows that sparsifying 2–3% of high-FI parameters can reduce MMLU accuracy by up to 75%, while random sparsification of the same proportion causes negligible loss. This establishes that FI captures genuine parameter sensitivity, and the effect size is dramatic.

4. **FI-guided channel protection improves quantization outcomes** — Section 3.3 shows that protecting only 5% of high-FI channels in FP16 while aggressively quantizing the rest recovers over 90% of the performance loss with only 0.1 GB extra memory, and consistently outperforms random/low-FI channel selection across subjects.

5. **FI-guided exclusion reduces forgetting in model merging** — Table 2 shows that excluding the top-10% high-FI parameters from arithmetic merging yields 15–20% improvements on math benchmarks compared to random exclusion, demonstrating that FI identifies domain-critical parameters.

## Weaknesses

### Fatal
None.

### Major

1. **No comparison to existing importance/salience measures for sparsification.** The parameter sensitivity experiments (Section 3.2) compare FI-guided sparsification only against *random* sparsification. This is a minimal sanity check — every sensible importance measure should outperform random. Without comparisons to gradient magnitude, diagonal Fisher information, Hessian-based criteria, or Jacobian norm, the paper cannot support its implied claim that FI provides a *practical advantage* over simpler alternatives. A reader cannot tell whether the dramatic effects in Figure 3 are unique to FI or would be equally achieved by any reasonable importance measure.

2. **External perturbation analysis is a single anecdotal example.** Section 3.1 studies one image from ScienceQA with one model (Qwen-VL). No statistics, no success rate, no evaluation across multiple images, tasks, or models. The paper notes that masking random pixels does not cause the same error, but does not quantify what fraction of random 10-pixel masks cause errors, nor compare to alternative salience maps (gradient-based, occlusion, integrated gradients). This does not establish that FI reliably detects vulnerable pixels — it only shows that a particular example is consistent with FI being useful.

3. **Computational feasibility is unaddressed.** The paper provides no runtime, memory, or scaling analysis for computing FI. For parameter-level analysis on models with billions of parameters, the cost of computing and inverting (via SVD) the Fisher information metric per perturbation component is non-trivial. The paper uses \(L=5, N=10\) for sequence generation but provides no analysis of variance, convergence, or whether these values are sufficient. Without any discussion of computational cost, the claim of a "practical" or "universal" stability measure is unsupported. (The paper does acknowledge computational limitations in the conclusion — "develop methods that can accelerate the computation" — but this does not substitute for analysis.)

### Minor

1. **No discussion of sensitivity to the choice of objective function \(f\).** All experiments use \(-\log P(y_{\text{pred}}|x,\theta,\omega)\) as the objective. The paper does not discuss whether results would change under alternative choices (e.g., entropy, margin-based objectives), making it unclear how robust FI rankings are to this design decision.

2. **Title overclaims relative to demonstrated scope.** The title calls FI a "Universal Stability Measurement," but the experimental validation is limited to three model families (Qwen, LLaMA2, LLaMA3) up to 13B parameters, one VLM (Qwen-VL), and one image for external perturbation. "Universal" is not supported.

3. **The sequence generation extension (Equations 5–8) has limited empirical impact.** Table 1 reports results using only one aggregation method (\(L=5\) fixed horizon) and one model family comparison. The discounted variant (\(\mathbf{FI}_{\text{seq}}^{\infty,\gamma}\)) is never evaluated, and the per-token FI analysis is not visualized or analyzed qualitatively.

### Trivial

- In the paragraph before Table 1, the paper refers to "average Fisher Information (FI)" rather than the defined term "First-order local Influence (FI)." This is a minor terminological inconsistency that does not affect technical content.

## Nice-to-Haves

- A dedicated empirical demonstration of the invariance property itself: e.g., apply the scaling transformation \(T_k\) to ReLU layers and show that FI remains constant while the Jacobian norm changes. This would directly validate the paper's core theoretical selling point.
- A comparison of FI to at least one existing importance measure (e.g., gradient magnitude) for the sparsification experiments.
- A runtime and memory breakdown for FI computation on a 7B model.
- For the quantization experiment, the paper could show whether GPTQ's or AWQ's internal importance metrics produce similar or different channel rankings to FI.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The paper never defines what 'stability' means beyond local sensitivity."** — Removed because the paper *does* define stability operationally: FI quantifies the change in the objective function relative to perturbation distance on the manifold. This is a standard local-sensitivity definition and is clearly stated (Definition 2.2, surrounding text).
- **"Comparing to GPTQ/AWQ for quantization."** — Removed because the paper proposes a *channel-selection strategy* (which channels to keep at high precision), not a complete quantization algorithm. Comparing FI-guided selection to GPTQ/AWQ is comparing different things; the paper's within-method comparison (FI vs. random) is appropriate for its stated goal. The suggestion is scope creep.
- **"The paper's own example does not rule out that simple object detection would do as well."** — Removed because this is speculative and unsupported. The paper's claim is that FI identifies particularly *vulnerable* pixels (whose perturbation flips the answer), not that FI uniquely identifies relevant objects. A salience map and an object detector measure different things.
- **"The reviewer questioned whether the computation can scale to 70B."** — Removed because the paper states "models of varying sizes, from 1.5B to 13B parameters," and the reviewer's 70B example is scope creep. The paper's scope is clearly stated.

## Novel Insights

The reviews reveal that the paper's strongest structural vulnerability is the gap between its *theoretical* contribution and its *comparative* validation. The invariance property (Theorem 2.3) is theoretically principled and genuinely solves the scaling-ambiguity problem for gradient-based importance measures in ReLU networks. However, the paper never directly demonstrates this empirically — it proves the invariance but does not show a case where it *matters* by comparing FI rankings to Jacobian-norm rankings under parameter rescalings. The weakest link is not that FI fails to capture sensitivity (it clearly does, outperforming random), but that the experiments do not establish whether FI captures sensitivity *better* or *differently* than simpler existing methods. This makes the paper feel incomplete: a theoretical advance paired with a proof-of-concept that stops short of demonstrating practical superiority.

## Suggestions

1. Add at least one existing importance measure as a baseline for the sparsification experiments (e.g., gradient magnitude, diagonal Fisher information, or Jacobian norm). Without this, the paper cannot support claims of practical advantage.
2. Expand the external perturbation study to more images and quantify success rates. Even 10–20 examples with statistics would dramatically strengthen this section.
3. Include a direct empirical demonstration of invariance: rescale ReLU layer parameters by \(k\) and show FI unchanged while Jacobian norm changes. This would validate the paper's core theoretical selling point.
4. Provide a brief computational cost analysis (runtime, memory) for FI computation on a 7B model, even if approximate.
5. Soften the title's "Universal" claim or scope it to reflect the experimental coverage.

## Score and Decision

The paper has a solid theoretical core — the information-geometric influence measure with reparameterization invariance is a genuine contribution that addresses a known limitation of gradient-based importance measures. The empirical results consistently show FI outperforming random baselines across multiple tasks, which is necessary but not sufficient evidence. The critical gap is the absence of comparisons to existing importance/salience measures, which prevents the paper from demonstrating whether FI offers practical advantages over simpler alternatives. The external perturbation study is a single anecdotal example, and computational feasibility is not analyzed. These weaknesses collectively mean the paper's evidence does not yet match the breadth of its claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>