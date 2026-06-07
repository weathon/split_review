Now I'll produce the final consolidated review.

## Summary
This paper develops a Sequential Monte Carlo (SMC) framework for controlled LLM generation that targets a global product-of-experts distribution combining an LM prior with arbitrary syntactic and semantic constraints. The key algorithmic contribution is separating constraints into "efficient" potentials (used per-token via masking in the proposal) and general "inefficient" potentials (evaluated via importance weights), combined with resampling to focus computation on promising partial sequences. The method is evaluated on four challenging domains (Python code generation for data science, text-to-SQL, goal inference, and molecule synthesis) with systematic ablations.

## Strengths

- **Systematic ablation isolating three algorithmic components across seven methods and four domains.** The experimental design (pLM → Locally-constrained → Grammar-only IS → Grammar-only SMC → Sample-Rerank → Full IS → Full SMC) lets the reader attribute gains to weight correction, semantic potentials, and resampling separately. Each component's contribution is assessed in Table 2 and the accompanying discussion. This is a clean and informative evaluation structure.

- **Integration of heterogeneous constraint types that prior locally-constrained decoding cannot handle.** The paper demonstrates that domain-specific semantic potentials — plan validation (VAL), test-case execution (DS-1000), column-alias checking (Spider), SMILES prefix validation (partialsmiles) — can be wrapped as non-differentiable, non-incremental potentials within the SMC framework. This goes beyond the grammar-only masking that dominates prior work (Shin et al., 2021; Scholak et al., 2021; Willard & Louf, 2023) and is concretely shown to improve accuracy.

- **Empirical connection between posterior approximation quality and downstream performance.** Section 3.3 estimates the KL divergence between each method's distribution and the target global posterior (Figure 2), and the ordering of methods by KL divergence (Full SMC < Full IS < Sample-Rerank) matches their ordering by accuracy in Table 2. Table 3 further reports Pearson correlations between particle weights and accuracy scores. This provides evidence that the accuracy gains reflect better Bayesian inference rather than artifacts of a particular aggregation scheme.

- **Multi-domain evaluation covering structurally diverse tasks.** The four domains (code generation, structured query generation, planning-goal inference, molecular generation) differ in their formal languages, constraint structures, and evaluation metrics. This breadth strengthens the claim that the SMC framework is general-purpose rather than tuned to a single application.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **"Posterior-weighted accuracy" is not defined in the visible main text (Table 2, line 159).** For methods that produce a posterior distribution over particles (Full SMC, Full IS, Sample-Rerank), the natural interpretation is accuracy weighted by the normalized importance weights. For the base LM and locally-constrained decoding — which produce a single sample — it is unclear what weighting scheme is used (uniform? averaged over multiple runs?). The reader should not have to guess how the headline metric is computed for every baseline. Since the paper reports bootstrapped 95% confidence intervals, the procedure was clearly defined in the author's code, but it needs to be stated in the paper.

2. **The KL divergence analysis in §3.3 is limited to one instance per domain** (the instance with median unique accuracy). While 100 runs per algorithm with t-tests provide statistical robustness for those specific instances, the paper's claim that "generation quality is correlated with how well each method approximates the global product of experts" would be stronger if demonstrated across multiple instances. The estimator used to compute the KL divergence is also not described in the main text. These are not fatal issues — the analysis is still informative as a diagnostic — but the evidence is thinner than the claim warrants.

3. **Different base LMs are used across domains without discussion of the confound.** Goal inference and molecule synthesis use Llama 3.1 8B, text-to-SQL uses Llama 3.1 8B-Instruct, and data science uses Llama 3 70B (a ~9× larger model). The paper does not acknowledge that the results in different domains are not comparable in any absolute sense due to these model-size and instruction-tuning differences. Each domain's within-domain comparisons are valid, but this should be noted.

4. **No compute-performance trade-off is reported.** SMC with N=10 particles requires roughly 10× the LM forward passes of single-sample baselines. The accuracy gains in Table 2 are real, but the paper does not report wall-clock time, FLOPs, or inference cost. This information is important for practitioners deciding whether to adopt the method. (The appendix reportedly varies the number of particles, which is useful, but does not substitute for time/cost reporting.)

5. **The grammar constraint in the DS-1000 domain is trivial (φ_CFG = 1),** making methods 2–4 (locally-constrained, Grammar-only IS, Grammar-only SMC) equivalent to the base LM for that domain. The paper is transparent about this (line 148), but does not explicitly note that the ablation results for DS-1000 therefore test only the semantic potential component, not the grammar+SMC combination. This limits what can be concluded from that domain about the grammar-related components.

6. **No dedicated limitations discussion.** The paper does not address boundary conditions: (a) the method's dependence on the existence of informative semantic potentials, (b) domains where designing such potentials would be difficult or costly, (c) risk of particle diversity collapse with small N, or (d) when simpler baselines might be preferable.

### Trivial
None.

## Nice-to-Haves
- A compute-performance analysis (accuracy vs. wall-clock time or LM forward passes) would help assess whether the ≈10× cost of SMC is justified.
- The line-level SMC extension mentioned in §2 (intermediate targets over Python statements) is an interesting idea; a dedicated experiment or discussion comparing token-level vs. line-level SMC would strengthen the paper.
- A calibration analysis of particle weights (beyond the Pearson correlations in Table 3) — e.g., does a weight of 0.8 correspond to ~80% accuracy? — would strengthen the probabilistic claims in §3.3.

## Removed Points
*These points were flagged by the reviewers but removed after verification against the paper. They are documented here for transparency.*

- **"KL divergence from samples is notoriously difficult to estimate reliably"** (harsh critic): Generic concern, not a specific identified problem in the paper's methodology. The paper uses 100 runs per algorithm and reports t-test significance, which is standard practice.
- **"The paper does not discuss simpler alternatives like beam search with scoring"**: The paper already evaluates 7 methods including multiple baselines; requesting additional baselines is scope creep.
- **"The practical severity of local decoding distortion is not quantified"**: The paper addresses this explicitly in §3.2 (line 171): "the bias from locally constrained decoding may be less severe in these semantic parsing domains than has been observed in other domains."
- **"How sensitive are results to the choice of few-shot examples?"**: Speculative concern without evidence that this is a problem.
- **"The related work discussion is adequate but brief"** and **"The discussion is thin"**: Vague qualitative judgments without specific, actionable content.
- **Formatting/style nitpicks**: Typos, whitespace, broken characters (these are PDF parser artifacts, not author errors).
- **Missing appendix content criticisms**: The parser strips appendices; they exist in the original submission.
- **Strength Finder's generic praise** ("addressed an important problem", "interesting question"): Removed as superficial.

## Novel Insights
None beyond the paper's own contributions. The harsh critic and strength finder correctly identified the paper's main contributions (SMC-based integration of heterogeneous constraints, systematic multidomain ablation, empirical link between posterior approximation and accuracy) but did not surface genuinely novel observations that the paper itself does not already state.

## Suggestions
1. **Define "posterior-weighted accuracy" explicitly** in the main text, specifying how it is computed for each baseline method (especially pLM and locally-constrained decoding, which produce single samples).
2. **Add a limitations paragraph** covering: dependence on informative semantic potentials, the DS-1000 grammar triviality, the cross-domain model-size confound, and compute costs.
3. **Report wall-clock time or inference cost** for each method at N=10 particles.
4. **Expand the KL analysis** to at least a handful of instances per domain (or describe the estimator more precisely in the main text).
5. **Note the model-size confound** when describing the experimental setup in §3.1.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>