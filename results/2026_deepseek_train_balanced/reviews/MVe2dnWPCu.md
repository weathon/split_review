## Summary

The paper proposes PICLE, a modular continual learning framework that uses two probabilistic models (one for perceptual/few-shot transfer based on input-distribution matching, one for latent transfer based on a Gaussian process in function space) to estimate the fitness of module compositions without training each candidate path. This enables constant-per-problem search costs. The method is evaluated on CTrL benchmarks and a new compositional extension (BELL), showing it is the first modular CL method to simultaneously achieve all three transfer types with scalability.

## Strengths

1. **Probabilistic fitness proxy is a well-motivated technical contribution.** The core insight — replacing costly full-network training of candidate paths with a tractable posterior approximation — is concretely realized. The PT model (Eqs. 1–2) factors the generative model so that activations can be marginalized out, yielding a closed-form posterior used in a greedy search that evaluates only L paths per problem.

2. **Two distinct probabilistic models correctly handle fundamentally different transfer settings.** The paper correctly identifies that PT (perceptual/few-shot) and NT (latent) transfer require different inference strategies. For PT paths, pre-trained modules can be evaluated directly on new-problem data; for NT paths, the paper introduces a GP with a function-space kernel over pre-trained suffixes. This division is principled and well-explained.

3. **Quantitative results demonstrate that PICLE covers the full combination of transfer types with scalability.** Table 1 shows PICLE is the only method among those compared with checkmarks for all three transfer types (perceptual, few-shot, latent) plus scalability. This is backed by concrete measurements: +34.65 higher transfer than MNTDP-D on few-shot (S^few), 69.65% vs. 65.64% on the 100-problem CTrL S^long, and resource curves (Figure 2) confirming sub-linear FLOPs/memory growth.

4. **The BELL benchmark is a well-motivated addition** that explicitly tests compositional module reuse (combining modules from different prior solutions), which is not covered by existing CTrL sequences.

5. **The performance-based prior p(m^i) provides a measurable and cleanly attributable benefit** on the hardest perceptual-transfer sequence S^{out**}, where PICLE achieves +10.33 higher transfer than MNTDP-D — directly attributable to the prior that MNTDP-D's k-NN lacks.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The GP distance metric d(λ, λ′) is critically underspecified (Section 5, Eq. 6).** The kernel is κ(λ,λ′) = σ²exp{−d(λ,λ′)²/(2γ²)} where d is "the distance between two functions" (line 205). The paper mentions storing hidden activations to form "a set of function inputs" (line 207), but never specifies how d is actually computed — L2 distance between suffix outputs? Cosine? MMD? This is the central quantity defining the GP and makes the NT search irreproducible as written. A reader could infer L2 as a default, but the paper should state this explicitly.

2. **Key hyperparameters for the NT search are not reported.** The number of BO evaluations c, the minimum suffix length ℓ_min, and the random projection dimensionality k (line 160) are described as hyperparameters without concrete values or selection procedures. The paper would benefit from stating these values and how they were chosen.

3. **Results are reported without confidence intervals, standard deviations, or significance tests.** Metrics are averaged over only 3 versions per sequence (line 257), and fine-grained differences (e.g., "+10.33," "+34.65") are reported without any variance information. Three replicates with no error bars make it difficult to assess whether the claimed margins are statistically reliable.

4. **No systematic ablation study.** A "PT-only ablation" is mentioned in passing for two sequences (line 272), but there is no dedicated ablation table. The paper would be substantially stronger with a proper ablation isolating: PICLE full, PT-only, NT-only, and a version replacing the probabilistic model with a simpler heuristic. Without this, it is unclear whether the GP-based NT search independently contributes value beyond the PT search.

5. **The NT path prior is restrictive and its limitations are not discussed.** The prior p(m^{L-ℓ+1},...,m^L) ∝ 1 only if the modules are a suffix of a previously used full path (line 195). This prevents composing modules from *different* previous solutions for latent transfer — the very kind of compositional recombination the paper touts for few-shot transfer. The justification ("unnecessary for our sequences," line 196) is benchmark-specific and should be acknowledged as a limitation rather than assumed away.

6. **The PT posterior derivation (Eq. 4) contains a denominator Σ_{m∈L_i} p(h^{i-1}|m)p(m) that does not follow from standard marginalization of the graphical model in Eq. (3).** The paper states "we can marginalize out the activations" (line 145) but the resulting expression sums over modules in the library — a heuristic normalization. The paper calls this an "approximation," which is appropriate, but the presentation somewhat overstates the formality. Clarifying the gap between the idealized Bayesian framing and the implemented approximation would improve transparency.

### Trivial
- The paper ends without a limitations or discussion section, where the restrictive NT prior and other caveats could be addressed.

## Nice-to-Haves
- A brief validation of the BELL benchmark (e.g., human performance or a random-guessing baseline) would strengthen the new suite.
- Clarify how the results of the PT and NT searches are combined — does the algorithm select the best-performing validated path among both search results?
- Report what happens when the NT search finds no useful suffix — is there a fallback to the standalone model or best PT path?

## Removed Points
(Points from the reviewers that were evaluated and filtered out.)
- **"The PT model is an ad-hoc heuristic, not principled."** The paper calls Eq. (4) an "approximation" (line 146) and the denominator is a reasonable normalization. The probabilistic framing remains a genuine contribution. This criticism is captured in weakened form as Minor #6.
- **"No limitations section."** Purely presentational; moved to Trivial.
- **"HOUDINI also achieves all three transfer types."** The paper's claim is "first to achieve all three **while scaling**" — Table 1 shows HOUDINI lacks scalability (✗). The claim is accurate.
- **"No explanation of how PT and NT searches combine."** Moved to Nice-to-Haves.
- **Strength Finder's claim of "systematic comparison with clear ablation"** is overstated; the ablation is mentioned in passing, not systematic. Weakened to Minor #4.
- **"The greedy PT search does not guarantee optimality."** This is obvious for any greedy method and not a meaningful weakness.
- **"BELL benchmark lacks validation."** While true, BELL is an extension of established CTrL and targets specific compositional capabilities. Moved to Nice-to-Haves.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Specify d(λ,λ′) explicitly.** State the distance metric used (e.g., L2 distance between suffix outputs evaluated on the combined set of stored activations).
2. **Report concrete values** for c, ℓ_min, and k, along with how they were selected.
3. **Add a systematic ablation table** (PICLE full, PT-only, NT-only, random-projection baseline).
4. **Add confidence intervals or standard deviations** to all reported metrics, or acknowledge the low number of replicates as a limitation.
5. **Add a limitations/discussion section** addressing the restrictive NT prior, the heuristic nature of the PT posterior approximation, and potential failure modes of the GP distance metric.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>