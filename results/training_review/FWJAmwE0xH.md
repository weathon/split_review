Now I have thoroughly verified the paper's content against every substantive claim from both reviewers. Let me write the consolidated review.

## Summary

The paper introduces the Neural-Symbolic Recursive Machine (NSR), a modular architecture that jointly learns a grounded symbol system (GSS) — integrating neural perception, transition-based dependency parsing, and functional program induction — to achieve systematic generalization across sequence-to-sequence tasks. A probabilistic learning framework with a deduction-abduction algorithm enables end-to-end training without intermediate GSS supervision. The model is evaluated on SCAN, PCFG, HINT, and a compositional machine translation task, achieving 100% on SCAN and PCFG splits and surpassing prior work on HINT by ~23 percentage points.

## Strengths

- **Strong cross-domain empirical results.** NSR achieves 100% on all SCAN and PCFG splits, and 90.1%/76.0% (symbol/image) on HINT, outperforming Transformer baselines especially on the extrapolation-heavy SL/LL subsets (e.g., 95.9% vs 11.7% on SL symbol input). This demonstrates that the framework generalizes across semantic parsing, string manipulation, and arithmetic reasoning — not just a single domain.

- **The GSS representation is well-motivated and interpretable.** The unified tree structure (grounded input, abstract symbol, semantic value) provides a clean bridge between neural and symbolic reasoning. Figure 3a convincingly shows the dependency parser learning permutation-equivalent word groups (verbs, modifiers, conjunctions) on SCAN's Length split without any predefined categories — a qualitatively compelling visualization of emergent syntax.

- **Learned syntactic structure emerges without domain knowledge.** The parser discovers syntactic categories from data alone, in contrast to NeSS which requires manually engineered category predictors and a curated training curriculum. This makes a credible case that NSR reduces the domain-specific engineering burden compared to prior neural-symbolic approaches.

- **Broad evaluation suite.** Experiments span four diverse tasks (semantic parsing, string manipulation, arithmetic reasoning with handwritten input, compositional MT), strengthening the claim that the approach transfers across domains.

## Weaknesses

### Fatal
None.

### Major

- **No ablation studies decompose the contribution.** The NSR has three trainable modules (perception, parser, program induction) plus the deduction-abduction algorithm. Without ablations, it is impossible to determine which components drive the strong results. Would a standard pretrained dependency parser (rather than learned) work as well? Could program induction be replaced with simpler rule lookup? Is the abduction step essential, or would a one-pass greedy deduction suffice? The paper claims these design choices matter but provides no controlled experiment to support the claim. This is the most significant gap in the evaluation.

- **The deduction-abduction algorithm is unevaluated as a learning method.** The algorithm is presented as a novel methodological contribution, yet the paper provides: (i) no comparison to alternative latent-variable training methods (REINFORCE, Gumbel-Softmax, Viterbi EM, straight-through estimators); (ii) no analysis of convergence, acceptance rate, or number of search steps required; (iii) no diagnostic evaluation of how often the abduction search finds a valid GSS vs. failing. The paper mentions "theoretically, this method acts as a Metropolis-Hastings sampler" (line 146) but provides no empirical validation of its behavior. This leaves the reader unable to assess whether the algorithm is practical or whether strong results depend on lucky search successes.

- **The theoretical framing around equivariance and compositionality is asserted, not demonstrated.** The paper defines equivariance and compositionality (Definitions 1–2), claims that NSR's three modules "exhibit equivariance and compositionality, functioning as pointwise transformations" (line 183), and then poses a Hypothesis linking these properties to compositional generalization. However, the dependency parser is a transition-based sequential state machine (line 85: "operating as a state machine... iteratively applying predicted transitions") — it processes tokens left-to-right and is not a pointwise transformation. The claim that it satisfies the formal definition of equivariance under a permutation group is not argued, let alone proven. The Hypothesis is never tested. This section creates the appearance of theoretical grounding that the paper does not deliver.

### Minor

- **No variance estimates or multiple runs.** All results are reported as single numbers without standard deviations or ranges. Since the deduction-abduction algorithm involves randomness (sampling neighbors in the search), variability across runs is expected. This makes it impossible to assess whether the HINT gains of ~23% are statistically robust.

- **HINT Transformer baselines are cited without reproduction.** The paper uses ResNet-18 as the image encoder for NSR and states that baselines (GRU, LSTM, Transformer) from Li et al. (2023) also use ResNet-18. However, the Transformer results are cited directly rather than reproduced in the same training pipeline. While this is common practice, given the large performance gap claimed (NSR 90.1% vs Transformer 61.5% on symbol input), reproducing baselines in the exact same setting would substantially strengthen the comparison.

- **The equivariance/compositionality Hypothesis is not tested.** The paper proposes a Hypothesis (line 185–187) that models achieving compositional generalization must instantiate an equivariant and compositional mapping. This is an interesting claim, but the paper provides no experiment designed to test it — e.g., measuring whether NSR actually achieves better generalization on instances where its learned representations satisfy the definitions versus instances where they do not, or comparing to a version of NSR where these properties are broken. As presented, the Hypothesis is motivational rather than empirical.

- **Some implementation details are absent.** The paper does not describe how handwritten HINT images are segmented into tokens for the perception module, nor does it specify the modifications made to DreamCoder to handle noise in training examples. These details are important for reproducibility.

### Trivial
None.

## Nice-to-Haves

- An error analysis on HINT's SL and LL splits (categorizing errors by perception vs. syntax vs. semantics) would clarify where the model's extrapolation strength lies.
- Dependency tree visualizations for HINT (analogous to Figure 3a for SCAN) would strengthen the claim that the parser generalizes across domains.  
- A study of the abduction search's success rate and step distribution on a sample of training instances would greatly increase confidence in the algorithm.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"NeSS achieving 0% on PCFG/HINT is suspicious and suggests a bug"** — The paper provides a concrete architectural explanation: NeSS's stack operations cannot represent binary functions (PCFG) and the trace search is hindered by large vocabulary (HINT). This is a genuine architectural limitation, not evidence of a bug. Removed as factually unsupported.

- **"NSR is slightly worse than Transformer on HINT SS"** — Table 2 shows NSR 97.3% vs Transformer 96.8% on symbol-input SS. NSR is better, not worse. Removed as factually incorrect.

- **"The Theorem is trivially true of any model with sufficient capacity"** — The paper itself acknowledges this (line 169: the lookup-table program "lacks in generalization capacity"). The Theorem is presented to show expressiveness, not generalization. The criticism ignores the paper's own caveat. Removed as strawman.

- **"Test on COGS or CFQ" / "Compare to Neural Theorem Provers / Neuro-Symbolic Concept Learner"** — These demand the paper address problems outside its stated scope. The paper's claims are about the benchmarks it evaluates on. Moved here as scope creep.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest empirical results (HINT extrapolation splits) and its weakest theoretical justification (equivariance/compositionality) co-occur. This suggests that the NSR's modular decomposition itself — independent of whether it formally satisfies specific algebraic properties — may be the actual driver of generalization. The parser's emergent syntactic categories (Figure 3a) are a genuinely striking finding that deserves deeper analysis: the fact that a sequential transition-based parser discovers discrete equivalence classes of words without any supervision is arguably more novel than the paper's formal framing suggests. One line of future work the reviews hint at is whether a much simpler version of this framework (e.g., a fixed parser + nearest-neighbor program lookup) would retain most of the HINT gains, which would reframe the contribution as being primarily about the GSS representation rather than the full learning machinery.

## Suggestions

1. **Add ablation studies as the highest priority.** At minimum: (a) train with greedy deduction only (no abduction refinement) to measure the algorithm's contribution; (b) replace the learned parser with a fixed pretrained dependency parser; (c) replace program induction with simpler rule extraction. Even partial ablations would substantially strengthen the attribution.

2. **Report multiple runs (3–5 seeds) with standard deviations** for all experiments, especially given the randomness in the abduction search.

3. **Diagnose the deduction-abduction algorithm empirically.** Report the percentage of training instances where the initial greedy GSS is already correct, the distribution of abduction steps when refinement is needed, and how often the search fails entirely.

4. **Tone down the theoretical framing.** Either provide a rigorous argument that each module satisfies Definitions 1–2 (especially the parser), or reframe the equivariance/compositionality discussion as motivation/intuition rather than formal grounding. The paper is empirically strong enough that it does not need overclaimed theory.

5. **Reproduce at least one baseline** (e.g., Transformer on HINT) in the same pipeline to rule out implementation confounds.

## Score and Decision

This paper makes a genuine empirical contribution: the GSS representation and modular architecture produce strong results across multiple systematic generalization benchmarks, with particularly impressive gains on HINT's extrapolation splits. The framework is novel and the emergent syntax analysis is compelling. However, the complete absence of ablation studies and the lack of any diagnostic evaluation of the deduction-abduction algorithm are significant gaps that prevent full assessment of the contribution. The theoretical section overclaims without delivering. These weaknesses are real but addressable — the core empirical findings are not invalidated.

The paper should be accepted — the empirical contributions are strong enough to warrant publication — but with the expectation that the authors will address the ablations and algorithm evaluation in a revision or proceedings version.

**Originality:** 7/10 — The GSS framework is novel; the individual components are adapted from prior work.

**Research Question Importance:** 8/10 — Systematic generalization is a central challenge.

**Claims Supported:** 6/10 — The main empirical claims are supported; the theoretical claims are not.

**Soundness of Experiments:** 5/10 — Missing ablations and multiple runs weaken the evaluation.

**Clarity of Writing:** 7/10 — Clear exposition of the architecture and results.

**Value to Community:** 7/10 — The empirical results and GSS design will likely inspire follow-up work.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>