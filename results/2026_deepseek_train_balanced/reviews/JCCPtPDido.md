Here is my final consolidated review.

## Summary
This paper introduces "jet expansion," a mathematical framework for rewriting residual network computations into sums of interpretable input-to-output paths using jets (generalized truncated Taylor series). It provides systematic algorithms (decompose, exp_jet_expansion) that generalize the logit lens and extend the exponential path decomposition of linear residual nets to non-linear networks. The paper demonstrates the framework through case studies on LLMs: component role identification, pretraining dynamics tracking, and model diffing for fine-tuning effects (code fine-tuning and RLHF/toxicity).

## Strengths

1. **Mathematically principled generalization of the logit lens.** The paper proves that the logit lens is a zeroth-order jet expansion (decompose(q, L, {h_l}, 0)) and shows two strictly more general variants: iterative jet lenses (higher-order expansions with one center) and joint jet lenses (multiple non-linearity outputs as centers). Figure 2 (bottom) provides quantitative cosine similarity evidence that higher-order jet lenses maintain near-1 cosine similarity across GPT-2, GPT-Neo, Llama, and OLMo model families, directly addressing known failures of the logit lens on GPT-Neo.

2. **Explicit, implementable algorithms for systematic path decomposition.** Algorithm 1 (decompose) and Algorithm 2 (exp_jet_expansion) provide concrete procedures for transforming residual networks into 2^L input-to-output jet paths with stated computational complexity O(|C|(F + kB)). This is a material advance over Veit et al. (2016) — who only recovered exponential path counts in the gradient — and Elhage et al. (2021), who simplified away nonlinearities.

3. **Data-free extraction of n-gram statistics from LLMs.** The paper shows that jet paths can be evaluated on the entire vocabulary Cartesian product without any probing data, producing symbolic n-gram databases. This is qualitatively different from dataset-dependent interpretability approaches. The toxicity case study (Table 3) demonstrates a practically interesting finding: jet bi-gram mass changes minimally (0.03445 → 0.03377) after RLHF even as ToxiGen drops to 0.0, suggesting retained toxic knowledge — a finding corroborated by RealToxicityPrompts scores with hard context (84% vs. 88%).

4. **Broad validation across multiple model families.** Results are reported on GPT-2, GPT-Neo, Llama-2-7B, OLMo-7B, and CodeLlama families, demonstrating generality across architectures and scales.

## Weaknesses

### Fatal
None.

### Major

1. **No baselines or comparisons to alternative methods.** The paper presents jet expansion as a new interpretability tool but never quantitatively compares it to any existing approach. For component role identification, no comparison to activation patching, direct logit attribution (Wang et al. 2022), or circuit discovery methods. For n-gram extraction, no comparison to directly prompting the model or computing logit-lens statistics. For model diffing, no comparison to parameter-space differencing. Without any baselines, it is unclear whether jet expansion provides genuinely complementary insights or reproduces what simpler methods already reveal. One well-chosen comparison would substantially raise the evidential bar.

2. **Remainder magnitude is characterized only for jet lenses, not for the n-gram expansions used in the headline case studies.** The paper reports cosine similarities (Figure 2, bottom) for jet lenses — limited expansions applied to specific input sentences — but no analogous faithfulness metrics are reported for the full path expansions used in the pretraining dynamics, toxicity, and code fine-tuning analyses. The paper acknowledges this in Remark 1 ("we cannot expect reminders to vanish") and the Limitations section, but the n-gram studies extract scores from jet paths and treat them as meaningful measures of model knowledge. For the toxicity comparison (Table 3), the ~2% relative change in jet bi-gram mass (0.03445 vs 0.03377) cannot be interpreted without knowing the remainder's magnitude relative to these values — the difference could reflect meaningful model change, expansion noise, or anything in between.

3. **Key methodological details are underspecified, compromising reproducibility.** (a) The toxicity analysis uses a "predefined list of keywords" to identify toxic bigrams (line 468), but the list itself, its size, and construction methodology are not provided. (b) No confidence intervals, standard errors, or significance tests are reported for any numerical result (cosine similarities, logit drops, bi-gram masses). (c) The pretraining dynamics analysis (hit ratios w.r.t. the final step, Figure 3) uses the final checkpoint as "ground truth" without discussing the circularity or stability of this reference.

### Minor

1. **Intervention evidence for component roles is correlational.** Ablating components causes logit drops (Table 1: -0.58 to -14.61), but this only shows the component *matters* for the prediction — not that it performs the specific claimed function (e.g., "adding -ing suffix"). The paper partially acknowledges overdetermination (line 354), but the orders-of-magnitude variation in logit drops for components assigned the same role (-0.58 vs -14.61 for "-ing") remains unaddressed and undermines the specificity of the role attributions.

2. **The exclusion of positional embeddings from the n-gram analysis (footnote, line 294) is acknowledged but its practical significance is not discussed.** Positional information is central to how transformers process language. Ignoring it means the jet n-grams reflect only token identity, not position-dependent behavior. The extent to which this limits conclusions — particularly for the pretraining dynamics analysis — is not addressed.

3. **The process for filtering paths by module type is underspecified.** The paper states "filtering out all paths that involve self-attention modules" (line 297) but does not explain how paths are associated with specific modules in the algorithmic framework. This is important for reproducibility of the n-gram studies.

### Trivial
None.

## Nice-to-Haves
- Reporting wall-clock time and memory usage for the n-gram extractions on the described hardware (128 CPU servers, 1TB memory) would help readers assess practical applicability.
- Validating jet n-gram scores against the model's actual output probabilities (averaged over many contexts) for a subset of bigrams would strengthen the "sketch" framing.
- The Lemma 1 dependency on the distance between centers (r = max_i w_i ‖x_i - ∑_j x_j‖) when centers are far apart could be discussed more explicitly.

## Removed Points
These points were raised in the input reviews but are removed per the filtering rules:

- The broken citation at line 490 ("g.][]{griewank2008evaluating}") is a PDF parsing artifact, not an author error. → REMOVED (formatting artifact)
- Claim that "jet n-gram statistics do not equal the model's actual n-gram probabilities" attacks a claim the paper does not make — the paper explicitly frames them as "sketches" and "databases" (line 300). → REMOVED (strawman)
- Claim that pretraining dynamics results "could be an artifact" of the expansion is speculative and unsupported by evidence in the paper. → REMOVED (speculative)
- Criticism that computing higher-order jets is "not trivial" and that the complexity claim "only holds for k=1" — the paper cites established efficient Taylor-mode techniques (Griewank 2008, Bettencourt 2019) and the standard O(kB) cost for k-th order jets via Taylor-mode AD is well-known. → REMOVED (factually questionable)
- Criticism that the introduction is "overly dismissive" of hypothesis-driven MI. → REMOVED (subjective opinion about framing)
- Criticism that the "notable expansions" section is "too brief" — the descriptions are concise but adequate for the presented content. → REMOVED (style preference)
- Criticism about Algorithm 1 being "confusing" — the conditional logic is standard for the described operation. → REMOVED (presentation preference)

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add at least one baseline comparison: for component role identification, compare jet-derived roles to those from direct logit attribution (e.g., the logit lens or activation patching) on the same set of components.
2. Compute faithfulness metrics (e.g., KL divergence or cosine similarity between jet n-gram scores and full model probabilities averaged over many contexts) for the specific truncated expansions used in the case studies.
3. Release the toxic keyword list and the construction procedure to make the toxicity analysis reproducible.
4. Report variance estimates (confidence intervals or standard errors) for all reported numerical quantities.
5. If the ablation results are to support specific role claims, test whether ablation selectively reduces the *target linguistic function* more than other functions (e.g., if MLP 3 adds "-ing", show its ablation specifically reduces "-ing" continuations relative to alternatives).

## Score and Decision
MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>