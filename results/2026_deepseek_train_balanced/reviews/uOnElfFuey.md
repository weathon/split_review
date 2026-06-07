Here is the final consolidated review.

---

## Summary

This paper proposes LaMFA, a pipeline for extracting deterministic finite automata (DFAs) from trained generative language models (LSTM and decoder-only GPT) by clustering latent states, estimating transition probabilities, and applying a merging/denoising step. Experiments on five regular languages show that extracted DFAs often match or exceed the original model's valid generation rate, and the paper reports that context dependency matters more than circuit complexity for model performance.

## Strengths

- **First extension of DFA extraction to generative probabilistic language models**: Prior work (Giles et al., 1991; Weiss et al., 2018) extracted DFAs from RNNs trained on language *recognition* (classification). This paper targets generative models trained with next-token prediction, which output distributions rather than binary accept/reject — a genuinely different setting that requires handling probabilistic transitions (Section 2, line 50).

- **First demonstration of DFA extraction from decoder-only transformers**: Extends the extraction pipeline to GPT-style architectures (GPT-nano, GPT-tiny), where prior extraction work covered only RNNs, GRUs, and LSTMs (Section 2, line 49; results in Table 2). This is a non-trivial extension because the latent state in transformers depends on the full prefix through self-attention, which the paper handles via a clearly stated hypothesis (Section 4).

- **OOD generalization evaluation with explicit OOD splits**: The paper constructs out-of-distribution evaluation sets (longest 20% of strings for length-based languages, top 20% largest digit sum for mdY) and reports that LaMFA-extracted DFAs often achieve higher OOD valid rates than the original neural models (Section 5.2.3), going beyond typical in-distribution-only evaluations in prior DFA extraction work.

- **Code and checkpoint release**: All code and model checkpoints are released.

## Weaknesses

### Major

1. **Abstract overclaims relative to reported results.** The abstract states "achieving 100% accuracy even in out-of-distribution scenarios" as if it were a general finding. The paper's own results contradict this for several important cases — e.g., on parity0 the OOD valid rate for the extracted DFA is substantially below 100% (Section 5.2.3 describes large drops from 70.4→50.52 and 98.05→76.56 for GPT-tiny and GPT-nano). The abstract's phrasing presents a best case (which holds for some languages like end0, alter, mdY) as a blanket achievement. This is not a minor framing issue; it misrepresents the evidence.

2. **The main empirical claim ("context dependency dominates circuit complexity") is stronger than the experimental design supports.** The paper claims context dependency is "the dominant factor" (Section 6). The evidence: end0 (TC⁰, local context) performs well alongside alter/mdY (AC⁰, local), while parity0/div3 (TC⁰, global) perform poorly. This indeed suggests context dependency matters for the languages tested. However, there is no AC⁰ + global-context language in the set. Without that cell, one cannot fully disentangle the two factors — the claim that context dependency *dominates* rather than *is a significant factor separable in the current data* overreaches. Adding an AC⁰ language requiring global context (or explicitly noting this gap as a limitation) would be needed.

3. **Evaluation never directly tests DFA equivalence, which is the paper's own central question.** The paper asks: "can one recover an equivalent automaton?" (Section 1). The primary metric (valid rate on generated strings) can detect over-approximation (strings that don't match the target regex) but cannot distinguish a correct DFA from one that accepts a strict *subset* of the target language: both yield 100% valid rate because all generated strings are valid by construction. The standard practice in DFA extraction literature includes directly checking equivalence — e.g., enumerating strings up to a bounded length or using automata-theoretic tests. Without this, the paper's central question remains unanswered.

### Minor

4. **Choice of K (number of clusters) not discussed.** K is a critical hyperparameter — for end0 (minimal DFA = 2 states), choosing K=2 vs K=50 would produce fundamentally different results. The paper provides no guidance on how K is selected for each language-model pair.

5. **Uneven training data sizes across languages.** alter has 44 training examples while mdY, parity0, end0 have 50,000 and div3 has 10,000. Cross-language comparisons are confounded by this disparity — poor performance on alter could partly reflect data sparsity rather than language complexity.

6. **No explanation of how accept/final states are identified from the generative model.** The paper defines a DFA as a 5-tuple including accept states, and estimates a transition matrix P and output matrix O (line 105). But in a generative model that can stop at any position, how these outputs are converted to a set of accept states is not discussed.

7. **The "k-means" column in Table 2 is unexplained.** The caption describes it as the model "after the k-means step in LaMFA" but does not explain how a k-means clustering (which produces discrete cluster assignments, not a generative model) is evaluated for valid rate and cross-entropy loss. Readers cannot interpret this column.

8. **The merging/denoising procedure is described at only a high level in the main text.** The paper says "an additional merging and denoising procedure is applied to merge redundant cluster classes... and remove noisy transition patterns" (Section 4) with no criteria, thresholds, or conflict-resolution logic. The algorithms are referenced but not summarized. A reader of the main text alone cannot understand, criticize, or reproduce this critical step.

### Trivial

9. No variance or confidence intervals reported for any result, despite stochasticity in training, sampling, and k-means.

10. The paper does not discuss whether the GPT latent state (before the final linear layer) satisfies the Markov property required for a DFA state, nor whether other representations might be more appropriate.

## Nice-to-Haves

- A comparison to grammatical inference baselines (e.g., L*, RPNI) that learn DFAs directly from training data, to clarify what the neural model adds beyond what standard DFA learning achieves.
- An AC⁰ + global-context language to fully disentangle circuit complexity from context dependency.

## Removed Points

The following points from the reviewer inputs were filtered during consolidation:

- **Universal language criticism (valid rate blindness)**: The harsh critic claimed a universal DFA would achieve 100% valid rate. This is factually wrong for the paper's evaluation setup, which *generates strings from the extracted DFA* — a universal DFA would produce mostly invalid strings, yielding a very low valid rate. The broader concern (subset-vs-equivalence discrimination) is retained as Major #3.
- **Perfect confound claim**: The critic asserted all local-context languages are AC⁰ and all global-context languages are TC⁰. This is incorrect: end0 is TC⁰ + local context. The weaker claim (missing AC⁰+global cell) is retained as Major #2.
- **"Non-reproducible" severity label for merging/denoising**: Downgraded from the critic's "non-reproducible" to Minor #8, acknowledging that algorithmic details likely reside in the (stripped) appendix. The main-text underspecification is a genuine concern but not fatal.
- **Strength about "systematic separation"**: The strength finder's claim that the paper "systematically separates" circuit complexity from context dependency overstates the design; this is instead treated as a weakness (Major #2).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Recalibrate the abstract to match the evidence — replace "100% accuracy even in out-of-distribution scenarios" with a precise statement about which languages and architectures achieve this.
2. Add a direct DFA equivalence evaluation: enumerate strings up to a bounded length and check agreement with the ground-truth DFA, or use automata-theoretic equivalence checking.
3. Add at least one AC⁰ + global-context language, or explicitly discuss the missing cell as a limitation of the empirical finding.
4. Discuss how K is chosen and how accept states are identified from the generative model.
5. Add variance estimates across training runs and clustering initializations.
6. Clarify what the "k-means" column in Table 2 represents — how a clustering intermediate becomes a generative model with a measurable valid rate.

## Score and Decision

The paper addresses a genuinely interesting question and makes a real methodological contribution (first DFA extraction from generative LMs and decoder-only transformers). However, it is held back by (1) abstract claims that overstate the evidence, (2) an experimental design that does not fully support the headline finding about context dependency, and (3) an evaluation that does not directly test DFA equivalence — the paper's own central question. These are addressable with major revisions, but in the current form the core conclusions are not as well-supported as required for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>