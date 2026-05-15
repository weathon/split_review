Now I have thoroughly verified all claims against the paper. Let me compose the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None.

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

---

Let me write the full review now.

I should also think carefully about the Strengths from the Strength Finder. Let me evaluate each:

1. "First one-shot generative model for directed graphs that overcomes fundamental limitations of prior work" - This is valid and well-supported. The paper shows why Spectre/DiGress can't handle directed graphs and proposes a genuine alternative.

2. "Closed-form noising encoder that avoids learning a separate network" - Valid. The heat diffusion equations provide a closed-form solution.

3. "Theoretical connection to heat kernels and RKBS provides principled motivation" - CONFLICT with verified weakness (the RKBS claim is never developed). Per rules: "Drop strengths that conflict with a verified weakness — when a strength and weakness disagree, the weakness wins." So this strength should be dropped or moved. Actually, the strength says the paper connects to heat kernels (which it does) AND RKBS (which it doesn't develop). The heat kernel part is valid. I'll drop the RKBS part and keep the heat kernel connection as a supporting strength.

4. "Quantitative MMD evaluation outperforms the autoregressive baseline GRAN" - Valid, though the evaluation is limited.

5. "Empirical analysis shows learned representations capture Laplacian column space" - Valid.

6. "Proposed low-rank SVD approximation enables scalability" - Valid, though only tested on small graphs.

Let me finalize.Here is my final consolidated review, based on careful verification of every claim against the actual paper text.

---

## Summary

This paper proposes DGDK, a one-shot generative model for directed graphs. The method uses a closed-form heat-diffusion encoder (based on the random-walk Laplacian) to corrupt input digraphs with controlled noise, and a denoising decoder (node decoder + edge decoder) trained to reconstruct the original graph structure. The claimed novelty is extending heat-kernel-inspired generative ideas to the non-symmetric (directed) setting, where existing one-shot methods like Spectre and DiGress fail. Experiments are conducted on synthetic directed graphs (Erdős–Rényi and stochastic block model) with small sizes (n=15, n=21).

## Strengths

- **First one-shot generative model designed explicitly for directed graphs.** The paper clearly identifies why existing one-shot approaches (Spectre, DiGress, Top-n) cannot handle directed graphs: Spectre relies on symmetric Laplacian eigen-decomposition with real, unitary eigenvectors; DiGress requires spectral features defined via symmetric scalar products; Top-n assumes symmetric similarity functions. DGDK sidesteps these limitations by using the random-walk Laplacian and working with singular vectors rather than eigenvectors. This is a genuine methodological advance.

- **Closed-form noising encoder avoids training a separate diffusion network.** The heat-equation-based noising process (Proposition 1, Equation 4) is computed analytically from the Laplacian and initial node representations, without learning. The noise ratio is controlled by two hyperparameters (α, T) and can be driven arbitrarily close to the uniform matrix M. This design is cleaner than learned noising processes and provides a direct geometric interpretation.

- **Empirical analysis shows the learned node representations capture the Laplacian column space.** Section 5.1 and Figure 3 demonstrate strong cosine correlation between the leading singular vectors of e^{tΔ}N and e^{tΔ}, confirming that the jointly learned representation matrix N preserves the most informative singular directions of the Laplacian exponential. This is a non-trivial validation of what the model internalizes.

- **Low-rank SVD approximation is proposed and shown to preserve reconstruction quality.** Replacing e^{tΔ} with a rank-s truncated SVD (Section 3.2) reduces memory while maintaining full edge reconstruction (Section 5.2). This is a practical contribution for scaling to larger digraphs.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation is far too narrow to support the paper's claimed generality.** The model is tested only on two synthetic datasets (Erdős–Rényi, SBM with 3 blocks) at small fixed sizes (n=15, n=21). No real-world directed graphs are used — not citation networks, knowledge graphs, causal graphs, traffic networks, or any benchmark. The only baseline is GRAN (an autoregressive method), compared on MMD without confidence intervals or variance estimates. No comparison is made to any directed-graph-specific generative method, nor are ablation experiments provided for adapted versions of Spectre or DiGress (the paper claims these cannot be adapted but does not demonstrate attempted adaptations). Without real-world evaluation, it is impossible to assess whether the method has practical utility beyond trivial synthetic distributions. The claim that "our model is able to generate directed graphs that follow the distribution of the training dataset" is only shown for these two simple cases.

2. **The sampling-time distribution shift is acknowledged but not rigorously analyzed.** During training, the encoder computes heat diffusion on the *target graph's own Laplacian* Δⁱ. At inference (Algorithm 1), it computes heat diffusion on the Laplacian of a *random graph* sampled from a Bernoulli distribution with edge probability μ. The decoder therefore sees node representations derived from a random graph's structure, not from a target-distribution graph. The paper provides only a high-level justification ("we need to construct graphs that... diffuse toward noisy graphs similar to those encountered during training") and an analogy to VAEs. While the high noise ratio (≈90%), edge-perturbation augmentation during training, and bounded range of X(T) elements partially mitigate this concern, the paper offers **no quantitative evidence** that representations from random graphs resemble those seen during training (e.g., comparison of singular value spectra, entry-wise distributions, or manifold distances). This gap undermines confidence that the method generalizes beyond the tested distributions.

3. **Only one baseline and no confidence intervals or statistical testing.** Comparisons are limited to GRAN, with no error bars, standard deviations, or significance tests reported for any MMD value. The MMD scores themselves are very small (<0.06 for DGDK on all metrics), which could indicate either strong performance or a non-discriminative metric — neither possibility can be assessed without variance estimates or comparisons on more challenging data.

### Minor

1. **The RKBS / heat-kernel generalization claim in the abstract is never developed in the paper body.** The abstract states: "Our approach generalizes a special class of exponential kernels over discrete structures, called diffusion kernels or heat kernels, to the non-symmetric case via Reproducing Kernel Banach Spaces (RKBS)." The paper discusses heat kernels in the context of undirected graphs and mentions connections to Gaussian processes, but never defines an RKBS, never shows how the non-symmetric case maps to one, and never returns to this framing after the introduction. This is a misleading over-claim that should either be substantiated or removed.

2. **Evaluation metrics do not fully capture directed structure.** The clustering coefficient uses the undirected neighborhood N_i = {v_j : (v_i, v_j) ∈ E or (v_j, v_i) ∈ E}, which discards directionality. The Laplacian-spectrum metric bins absolute values of eigenvalues, discarding phase information that is essential for directed graphs. Only the in-degree histogram captures direction-specific information. As a result, the evaluation does not convincingly demonstrate that the generated graphs have correct *directional* properties (e.g., edge asymmetry, reachability, feedback loops, hierarchical structure). Metrics that specifically assess directed structure (e.g., directed clustering variants, spectral phase distributions) would strengthen the paper.

3. **The multimodal generation analysis (Section 5.3) is purely qualitative.** The paper shows visual examples of generated graphs with varying numbers of components and discusses the impact of α and γ, but provides no quantitative assessment — e.g., histograms of the number of components per generated graph, mode-frequency distributions, or measures of diversity across modes. This limits the strength of the multimodal claims.

4. **The jointly learned node representation N is shared across all graphs of the same size, tying the model to a fixed size or requiring padding.** The model can handle different sizes during training (via an upper-submatrix of the max-size matrix O), but the largest graph encountered during training bounds the generation size. The paper tests only on fixed-size graphs (n=15, n=21), leaving the scaling behavior and performance on variable-size graphs unexplored.

### Trivial

- The target node representation is arbitrarily set to Tⁱ = e^{Δⁱ}N (t=1) with no justification for choosing t=1 over any other t ∈ (0, T]. Any such choice is equally valid, but the paper does not discuss this.
- The hyperparameter choices T=1, α=2.3 are justified by the noise ratio ≈0.9 but are not cross-validated; the paper mentions cross-validation is possible but does not perform it.
- The paper uses "heat diffusion" to distinguish from "diffusion models in machine learning" (Section 2) but later uses "diffusion" loosely — some clarifications would help.

## Nice-to-Haves

- Experiments on real-world directed graph benchmarks (e.g., citation networks, metabolic networks, Web graphs) would substantially strengthen the paper.
- An analysis comparing the distribution of node representations from random graphs at inference time vs. those from training graphs (e.g., singular-value spectra, entry-wise histograms) to quantify the distribution shift.
- Comparing against an adapted version of DiGress (using directed spectral features) or Spectre (using SVD-based features) would make the "cannot be easily adapted" argument more concrete.
- Quantitative metrics for the multimodal experiment (e.g., distribution of component counts per generated graph).
- Runtime and memory profiling for different graph sizes to substantiate the scalability claim of the low-rank SVD approximation.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The claim that existing methods cannot be easily adapted is asserted rather than demonstrated."** — Removed as factually wrong. The paper provides detailed reasoning in Section 4: Spectre's Stiefel-manifold approach requires real, unitary eigenvectors (which fail for directed graphs), and DiGress requires symmetric spectral features (Beaini et al., 2021). This is genuine technical justification, not mere assertion.

2. **"The 'state-of-the-art' claim in the conclusion is unsupported."** — Removed as factually wrong. The paper never claims DGDK is state-of-the-art. It calls GRAN "the state-of-the-art autoregressive baseline" (line 181), which is a factual description of GRAN's status, not an over-claim about DGDK.

3. **"The 100% uniqueness and novelty scores are suspiciously perfect."** — Removed. For directed graphs with n=21, the space of possible adjacency matrices is 2⁴²⁰. Obtaining 10,000 non-isomorphic samples is trivially easy in such a vast space and is not suspicious.

4. **"The paper never explains why the specific heat source term Q(s) in Proposition 1 is chosen."** — Removed. The paper states this goal explicitly: "Our goal is to formulate Q so that X(T) tends to some non-informative matrix M as T tends to +∞." The derivation follows directly.

5. **"The concatenation operation in the edge decoder is not permutation-invariant."** — Removed. For directed graphs, order matters by definition. The paper even notes that for undirected graphs, addition can be substituted. This is a feature, not a bug.

6. **"The negative elements in X(t) for t∈(0,T) are relevant for the stochastic interpretation."** — Removed. The paper addresses this: "This is not a problem in practice since our goal is to reconstruct Z(t) which is column stochastic for all t≥0." The negative elements occur only during the intermediate noising process, not in the input to the decoder.

7. **"Spectre could potentially be adapted using singular vectors instead of eigenvectors."** — Removed. This misunderstands Spectre's core mechanism, which fundamentally relies on the Stiefel-manifold structure of orthogonal eigenvectors with real eigenvalues. Replacing eigenvectors with singular vectors would require an entirely different method (which is what the paper proposes).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension: the paper has a genuinely novel methodological idea (heat-kernel-based one-shot generation for directed graphs) that is mathematically well-grounded, but the empirical validation is too thin to substantiate the claimed generality. The most interesting observation from the synthesis is that the distribution-shift problem (random graph → encoder → decoder) is structurally analogous to the fundamental challenge in denoising autoencoders for generation — but the paper does not leverage this analogy to provide any theoretical or empirical analysis of when such a scheme can succeed.

## Suggestions

1. **Add at least one real-world directed-graph dataset** (e.g., a citation network or metabolic network) with size n=50–200, comparing against GRAN and at least one adapted undirected baseline. Report MMD with standard deviations or confidence intervals across multiple runs.

2. **Provide quantitative evidence that the inference-time representations from random graphs lie within the training-time representation manifold.** This could be a simple histogram comparison of entry values, singular-value spectra, or a 2D embedding of representations from both sources.

3. **Either develop the RKBS connection substantively or remove it from the abstract.** As it stands, the claim is misleading and invites skepticism about the paper's rigor.

4. **Add directed-specific evaluation metrics** — e.g., directed clustering coefficient (Fagiolo, 2007), spectral phase distribution, or reachability-profile MMD — to demonstrate that the generated graphs have correct directional properties.

5. **For the multimodal experiment, report quantitative mode distributions** (e.g., histogram of the number of generated components) to support the qualitative claims.

## Score and Decision

**Originality:** 7/10 — First one-shot directed graph generator; heat-kernel-based noising is a novel application.

**Quality of research question:** 7/10 — Directed graph generation is an under-explored and important problem.

**Claims supported?:** 4/10 — The paper claims a general generative framework but only evaluates on two small synthetic datasets with one baseline, no real data, and no confidence intervals.

**Soundness of experiments:** 4/10 — Limited baselines, no statistical rigor, metrics miss directional structure, no analysis of the training/inference distribution mismatch.

**Clarity:** 6/10 — Generally well-written but the RKBS claim is misleading and the framings (VAE analogy, heat kernel generalization) are claimed but not substantiated.

**Value to community:** 5/10 — The method is interesting and could be impactful, but the evaluation is too preliminary to be useful to practitioners.

The paper presents a technically interesting approach with genuine novelty, but the evaluation is insufficient to support the claimed generality. The weaknesses are not fatal — the method is not fundamentally broken — but they are significant enough that the paper in its current form does not meet the evidentiary standard for acceptance. With real-world experiments, more baselines, and rigorous analysis of the inference-time mechanism, this could be a strong contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>