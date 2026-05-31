Now let me write the final consolidated review.

## Summary

This paper initiates the study of how language models learn context-free grammars (CFGs) through the lens of "subgrammars" — inner subgrammars (subtrees of derivations) and outer subgrammars (restricted rule sets). The authors prove recurrence theorems relating the KL divergence of a language model to sums over subgrammar-restricted divergences (Theorems 4.3, 4.6), show empirically that small transformers learn all subgrammars in parallel, explore curriculum learning via subgrammar pretraining with CKA-based representation analysis, and demonstrate that models struggle with deep recursion even when handling long non-recursive sequences.

## Strengths

1. **Novel conceptual framework.** The definitions of inner and outer subgrammars (Definitions 3.3–3.5) formalize an intuitive but underexplored notion — that CFGs decompose into substructures, and that learning dynamics may be understood through this decomposition. This provides a new lens for studying CFG acquisition beyond prior work on static representations (Allen-Zhu & Li, 2023) or overall learning curves (Cagnetta & Wyart, 2024).

2. **The depth–length controlled experiment (Section 6, Figure 3).** The paper cleanly isolates the effect of recursion depth from sequence length by comparing contexts `(a)^i` (depth 0, low error 0.017) against `(^i` (depth i, error rising to 0.173). This sharp dissociation goes beyond prior observations (Bhattamishra et al., 2020; Lampinen, 2024) and provides clear evidence that recursive depth, not length per se, is the bottleneck — a well-designed experiment.

3. **CKA-based analysis of pretraining effects (Table 1, Section 5.2).** Using Centered Kernel Alignment across 30 random seeds, the paper shows that subgrammar-pretrained models have higher representational alignment in attention layers (e.g., +21.7% for two-layer transformers with 20-epoch pretraining on full grammar sequences). The cosine-similarity probe further shows pretrained models better segregate subgrammar-containing from subgrammar-free strings. This provides mechanistic evidence that pretraining induces internal structure aligned with the grammar's substructure.

4. **Robustness to subgrammar position (Section 5.1).** The finding that pretraining benefits transfer regardless of whether the subgrammar appears as a prefix, infix, or suffix is non-obvious for autoregressive models and shows that the subgrammar structure itself drives the learning advantage, not positional convenience.

## Weaknesses

### Fatal

None.

### Major

1. **Equation (4) contains a mathematically incorrect step in the core derivation.** The paper presents (lines 136–143):
   
   (2)–(3): D_KL = Σ P_G(αaβ)[log P_G(α|ε) + log P_G(a|α) + log P_G(β|aα) − log Q_θ(α|ε) − log Q_θ(a|α) − log Q_θ(β|aα)]
   
   (4): = log P_G(α|ε)/log Q_θ(α|ε) + Σ_a P_G(a)·log P_G(a)/log Q_θ(a|α) + Σ_a P_G(a)·log P_G(β|aα)/log Q_θ(β|aα)
   
   The KL divergence is Σ P(s)·[log P(s) − log Q(s)], a sum of *differences* of logs. Equation (4) incorrectly replaces these differences with *fractions* of logs. The sum over `a` has also changed form. This is not a typographical artifact — the fractions are rendered LaTeX. Because this derivation is the main text's only walk-through of how the subgrammar KL decomposition works, this error undermines confidence in the theoretical development. Even if the full proof (deferred to the stripped appendix) is correct, the main text's presentation of the core idea is mathematically unsound.

2. **Definition 4.2 is unclear and uses undefined notation.** The "restricted" KL divergence is defined as:
   
   D_KL(P_G ‖ Q)_A = Σ_{s∈Σ^*} P(s|ε) P_G(A|s) Σ_{a∈Σ^*} D_KL(P_G ‖ Q | ¬s)
   
   The quantity P_G(A|s) for nonterminal A given string s is never formally defined (what does the probability of a nonterminal given a string prefix mean?). The notation D_KL(P_G ‖ Q | ¬s) is similarly unexplained. The paper says this "can be seen as the 'restriction' of the KL-divergence to substrings from subgrammar A" but does not provide a precise measure-theoretic definition. This makes Theorems 4.3 and Corollary 4.5 — which depend on this definition — hard to evaluate.

3. **The central empirical claim of "perfect decomposition" (Figure 1) is validated only qualitatively.** The paper asserts that "scaling the divergences by their probabilities give a perfect decomposition" and that the plots "show visually how … the KL divergence (loss) is the sum over the corresponding loss for each subgrammar." However, no quantitative error analysis is provided — no scatter plot of predicted vs. actual total KL, no residual computation, no statistical test of whether the sum of subgrammar-restricted divergences matches the total divergence to within noise. All curves in Figure 1 decrease monotonically, which is consistent with any set of correlated measures under the same training signal; it does not confirm the claimed additive decomposition. Given that Corollary 4.5's clean additive form requires a "context-insensitivity" assumption that is stated as "perhaps not so strong" but never directly tested, the experimental support for the paper's central theoretical claim is substantially weaker than the text suggests.

4. **Corollary 4.7 (parallel learning) is a definitional restatement, not a substantive prediction.** The corollary states: if gradient updates on one subgrammar do not hurt performance on other subgrammars, then all subgrammars are learned in parallel. This is essentially the definition of "no negative interference" restated as a conclusion. The paper provides no experiment that tests whether actual transformers satisfy this independence condition (e.g., by measuring cross-gradient interference or performing a controlled experiment with partial training data). The observation that multiple KL curves descend together (Figures 1–2) is consistent with trivial explanations (the model fitting the joint distribution). The paper frames this as a nontrivial phenomenon, but it is not properly tested.

### Minor

1. **Theorem 4.6's grounding in PCFG consistency theory is not connected to standard results.** The paper treats E[R] (the expected number of S occurrences in the top-level rule) as a branching factor and writes the denominator 1−E[R], remarking that if 1−E[R] < 0 the KL is unbounded. For the specific case of a single self-looping nonterminal, this matches the branching-process condition for consistency. However, the paper does not connect this to known PCFG consistency theory (where the condition is spectral radius of the expectation matrix < 1), nor does it discuss how the result generalizes to grammars with multiple interacting nonterminals. The derivation reads as ad hoc rather than grounded in established theory.

2. **The "context-insensitivity" assumption of Corollary 4.5 is central but untested.** This assumption (that Q_θ(A_i | s) is the same for all contexts s where P_G(A_i | s) > 0) is required for the clean additive decomposition. The paper notes it is "perhaps not so strong" and that results with varying prefixes were "qualitatively similar," but no formal test is reported (e.g., measuring the variance of Q_θ(A_i | s) across contexts). This leaves the scope of the main theoretical result unclear.

3. **CKA results lack formal significance testing.** The reported changes (e.g., +8.9%, +21.7%) are cited as evidence of "higher alignment" and "segregation," but no confidence intervals or statistical tests (e.g., permutation tests) accompany the 30-seed averages. The interpretation that higher CKA reflects "internal representations aligned with the grammar's substructure" is plausible but speculative without further analysis linking CKA to functional behavior.

4. **The GPT-5.1 anecdotal result (Section 6) adds little.** The paper appropriately hedges this as "purely anecdotal," but it occupies space that could be used for more rigorous analysis.

### Trivial

None.

## Nice-to-Haves

- A quantitative evaluation of the KL decomposition: compute the total KL, the sum of subgrammar-restricted KLs using the paper's own definition, and report the residual error across training steps.
- A direct test of context-insensitivity: measure the variance of Q_θ(A_i | s) across different contexts s and report how much this variance affects the decomposition.
- For the parallel learning claim: a controlled experiment where training data is limited to subsets of the grammar to test whether learning one subgrammar transfers to others.

## Removed Points

*The following points were raised by reviewers but removed for the stated reasons:*

1. **"Proofs are missing from the main text, relegated to the appendix."** — Removed per instructions: the appendix was stripped by the parser; proofs exist in the original submission.
2. **"Criticism about the condition 1−E[R] < 0 implying unbounded KL being 'not justified and may be false.'"** — Removed: for the specific single-nonterminal self-loop case in Theorem 4.6, the condition 1−E[R] < 0 correctly identifies when the branching process is supercritical and the PCFG is not proper, so this specific criticism is factually wrong.
3. **"Missing related work / comparisons."** — Removed per instructions: the reviewer lacks external sources to verify whether related works exist.
4. **"The grammar definitions are 'given in the appendix' but absent from the main text" / "reproducibility concern about missing definitions."** — Removed per instructions: the appendix (including grammar definitions) was stripped by the parser.
5. **"The sum over 'a ∈ Σ^*' is mis-specified (should sum over strings generated by subgrammar A)."** — Removed: this is a plausible interpretation given the context of equation (1) that is supported by the surrounding text discussing the subgrammar A's strings; the notation could be clarified but is not definitively an error.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix equation (4).** Replace the fraction-of-logs form with the correct difference-of-logs form and clearly show how the sum over strings decomposes into subgrammar terms. Provide a clean, self-contained derivation of Theorem 4.3 in the main text.

2. **Give a precise definition of the restricted KL divergence (Definition 4.2).** Define D_KL(P_G ‖ Q)_A as an expectation over a well-specified probability space. Clarify what P_G(A | s) means and how it is computed.

3. **Provide quantitative validation of the decomposition.** Report the residual ‖KL_total − Σ_i KL_{A_i} − Σ_α KL_α‖ across training steps.

4. **Test context-insensitivity directly.** Measure and report the variance of Q_θ(A_i | s) across different contexts s for the grammars used in the experiments.

## Score and Decision

**Round-1 bracket:** [3.5, 5.5], based on comparisons with "Automata Learning and Identification of the Support of Language Models" (7.00, stronger on all axes), "Context-free Recognition with Transformers" (5.50, stronger theory but similar experimental limitations), "Constrained Decoding of Diffusion LLMs with CFGs" (5.50, cleaner applied contribution), and "Measuring Scarcity–Complexity Collision" (4.50, similar level of theoretical ambition vs. execution issues).

**Round-2 narrowing:** Anchors in the [3.0, 5.0] and [5.0, 7.0] bands were inspected. Compared to "How Transformers Get Rich" (4.50, withdrawn/reject) — this paper has a more novel conceptual contribution but more serious mathematical errors in its core derivation. Compared to "Empirically Testing Expressivity Bounds" (4.50, reject) — this paper has more interesting experiments but less rigorous methodology. Compared to "Context-free Recognition with Transformers" (5.50, reject) — that paper's theory, though sloppily presented, is structurally sound; this paper's main-text derivation has an actual mathematical error. The paper is below the 5.5 tier and comparable to the 4.0–4.5 tier.

**Final score: 4.0.** The paper identifies a genuinely interesting research direction and contains some well-designed experiments (depth vs. length, CKA analysis). However, the core theoretical development — which the paper frames as "the most important contribution" — contains a verifiable mathematical error in equation (4) and a poorly-formalized key definition (Definition 4.2). The central empirical claim of decomposition is supported only by qualitative plots. These issues are not speculative or based on missing appendix content; they are present in the main text as rendered. The paper would need substantial revision — including fixing the mathematical derivation, properly formalizing definitions, and adding quantitative validation — before its contributions can be reliably assessed.

### Anchor Summary

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| voB9vaGcx1.md | 2.50 | 1 | Much weaker paper on constrained decoding; far less substantial |
| EltjRajCVI.md | 2.50 | 1 | Chess skill acquisition; different topic, similar score tier |
| YBt6cvPK0k.md | 3.00 | 1 | BERT probing; less ambitious, more polished |
| psDyG1FDzX.md | 2.40 | 1 | Solomonoff induction connection; speculative theory |
| L8SMNWsxfK.md | 7.00 | 1 | Clean theory + experiments on automata learning; clearly stronger |
| 7Sph4KyeYO.md | 5.50 | 1 | Applied constrained decoding; cleaner contribution |
| ACn1hhGcV4.md | 5.50 | 1 | CFG recognition theory; structurally sound but sloppy presentation |
| bkSKvJjziW.md | 4.50 | 1 | Scarcity-complexity causal framework; similar ambition but clearer theory |
| EAfMzT8ZLy.md | 4.50 | 2 | Induction head theory; similar issues with restrictive setup |
| UjDE4mmOBB.md | 4.50 | 2 | Expressivity bounds testing; similar level though cleaner methodology |
| yUvvOVO6Yu.md | 3.00 | 2 | CoT reasoning dynamics; less relevant |
| Vv8mXtf8Lx.md | 3.50 | 2 | ICL limitations; different topic |
| m5KplPzCzM.md | 5.33 | 2 | PCG learning; stronger empirical methodology |

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>