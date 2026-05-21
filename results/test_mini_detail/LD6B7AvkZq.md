Now I have enough information to write the final review. Let me compose it.

## Summary

This paper introduces a framework for studying how language models learn context-free grammars through the lens of "subgrammars" — substructures of CFGs corresponding to subsets of non-terminals or rules. The authors define inner and outer subgrammars, prove a decomposition theorem showing that every PCFG can be uniquely decomposed into inner subgrammars, and derive a recurrence formula showing that the KL divergence between a PCFG distribution and an autoregressive LM decomposes into a sum over subgrammar-specific terms. The paper then provides empirical demonstrations: (1) small transformers learn all subgrammars in parallel rather than sequentially, (2) pretraining on subgrammars improves performance and alters internal representations (measured via CKA), and (3) models struggle with recursive depth but not with linear length, even for distributions with identical next-token probabilities.

## Strengths

1. **Novel formal framework for CFG substructure.** The definitions of inner subgrammars (Definition 3.3 — a PCFG over a subset of non-terminals with renormalized probabilities) and outer subgrammars (Definition 3.5 — a subset of rules yielding a simplified language) are well-motivated and capture natural notions of "simpler components" within a CFG. Theorem 4.1 (unique decomposition into a DAG of inner subgrammars) provides a rigorous foundation for studying how CFG learning decomposes by substructure, connecting to classical work by Gruska (1971) while offering a formulation suited to the learning setting.

2. **KL divergence recurrence over subgrammars (Theorem 4.3 and Corollary 4.5).** The core theoretical claim — that the KL divergence between a PCFG distribution and an autoregressive model decomposes into a sum of terms corresponding to subgrammars — is a genuinely novel and potentially useful conceptual contribution. The simplified form under "context-insensitivity" (Corollary 4.5) is particularly elegant: D_KL(P_G || Q_θ) = Σ_i p_i D_KL(P_{A_i} || Q_θ(A_i)). Theorem 4.6 linking KL divergence to expected recursion count (with blow-up when E[R] ≥ 1) makes a quantitative prediction about depth difficulty.

3. **Empirical demonstration of parallel subgrammar learning.** Figures 1 and 2 show that KL divergence on all subgrammars decreases simultaneously throughout training, rather than sequentially (as one might naively expect). This is a non-trivial and interesting observation, and the paper honestly frames it as a phenomenon requiring explanation rather than claiming it's proven.

4. **CKA analysis showing representational effects of subgrammar pretraining.** Table 1 shows that models pretrained on subgrammars exhibit higher CKA similarity across attention layers (+21.7% for two-layer transformers with 20 epochs of pretraining on full grammar sequences). Table 3 further shows that pretrained models better segregate subgrammar and non-subgrammar sequences in embedding space. These findings provide concrete evidence that curriculum learning with subgrammars changes internal representations in a measurable way.

5. **Clean isolation of depth as a separate failure mode.** Figure 3 provides a controlled experiment showing that prediction error grows with recursive depth (contexts of the form `(^i`) but stays low with linear length (contexts `(a)^i`), despite the next-token distribution being identical for both. This precisely isolates depth as a distinct difficulty beyond sequence length.

## Weaknesses

### Fatal
None.

### Major

1. **The main-text derivation of the KL recurrence is too sketchy to verify.** The derivation in Section 4.2, which is the only theoretical justification for the paper's central claim (Theorem 4.3), is presented in a highly compressed form. Equation (4) as rendered is garbled (showing log-ratio fractions that are not standard KL divergence forms), and the steps from (1)–(3) to (4) rely on an "abuse of notation" that is acknowledged but not sufficiently justified. The full proof is deferred to the appendix (which is stripped by the PDF parser). For a paper whose main contribution is theoretical, the main text must provide a clearer, self-contained sketch of the reasoning. As it stands, a reader cannot verify the core claim from the main text alone, and the key theorem's validity rests entirely on the unverifiable appendix.

2. **The empirical "validation" in Figure 1 is potentially circular.** The paper plots subgrammar-specific KL divergences and their sum, showing that the sum tracks the total KL. But if the subgrammar KL terms are defined as the decomposition terms in the (unverified) Theorem 4.3, then the sum equaling the total is true by construction, not by empirical discovery. The paper needs to specify how the subgrammar KL terms are independently computed from the model's outputs (e.g., by restricting the model's next-token distribution to subgrammar-relevant tokens in specific contexts) so that the equality is non-trivial to verify.

3. **Corollary 4.7 (parallel learning) is close to a tautology.** The corollary states that if gradient updates on one subgrammar do not harm others, then subgrammars are learned in parallel. This essentially restates the definition of "no interference" as a sufficient condition for parallel learning. While it formalizes a conceptual point, it doesn't provide a testable or novel condition. The paper acknowledges this is "stated informally" and suggests future work on weakening the assumptions, but the corollary as presented adds little substance.

### Minor

1. **Incomplete experimental reporting.** The paper mentions "two-layer, two-head transformer" but does not state the embedding dimension, number of attention heads, training data size, learning rate, or optimization hyperparameters in the main text. The grammar definitions are referenced only in the (stripped) appendix. This makes the experiments not independently reproducible from the main text.

2. **No error bars or statistical significance for CKA results.** Table 1 reports CKA similarity averaged over 30 seeds but shows no variance or significance tests. While the percentage changes (e.g., +21.7%) are suggestive, the reader cannot assess whether these differences are statistically meaningful.

3. **The GPT-5.1 anecdote adds little value.** The paper includes informal tests on GPT-5.1 for arithmetic expressions but explicitly states these are "purely anecdotal" and should not be interpreted as evidence. The anecdote is consistent with the paper's depth findings but the space could be better used for more rigorous experiments or fuller theoretical exposition.

### Trivial
- The equation numbering in Section 4.2 is inconsistent (Theorem 4.2 is referenced but the main theorem is Theorem 4.3; Corollary 4.4 is referenced as the "Corollary" to Theorem 4.2).
- Figure captions are duplicated in the extracted text (parser artifact but worth noting).

## Nice-to-Haves
- A more thorough discussion of how the subgrammar KL terms are computed in practice (e.g., whether they require access to the PCFG's parse trees or can be estimated from samples).
- A comparison to the prior work of Cagnetta & Wyart (2024) and Allen-Zhu & Li (2023), which the paper cites but does not contrast with in detail.
- An exploration of whether the "context-insensitivity" assumption of Corollary 4.5 holds for larger models or more complex grammars.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Harsh critic's claim that the derivation is invalid because PCFG probabilities cannot be factorized left-to-right.** This is factually incorrect. By the chain rule of probability, any distribution over Σ* can be factorized as P(x₁)P(x₂|x₁)...P(xₙ|x₁...xₙ₋₁). The PCFG distribution P_G is a well-defined distribution over terminal strings, and the conditional probabilities P_G(a|α) are well-defined marginal conditionals. The paper explicitly acknowledges the "abuse of notation" and defines what the notation means. This criticism reflects a misunderstanding of basic probability theory.

2. **Harsh critic's claim that "P(α|ε)" is undefined for a PCFG.** The paper clearly defines this as "the probability of a partial sequence beginning with α" — this is the marginal probability of the prefix under the PCFG distribution, which is well-defined.

3. **Harsh critic's claim that the experiments are "circular" because they simply assume the decomposition.** The experiments do compute subgrammar KL terms independently using the model's output distributions restricted to different contexts. The paper states that varying the prefix did not change results, suggesting the terms are computed from model outputs, not just defined as the decomposition terms.

4. **Harsh critic's claim that Section 6 "does not add much" because it's consistent with known results.** Reproducing and extending known results in a controlled setting is a valid scientific contribution. The paper's specific finding — that depth but not length causes errors even when the next-token distribution is identical — is a clean demonstration that goes beyond prior work.

5. **Harsh critic's criticism about missing appendix content.** The appendix is stripped by the PDF parser; the original submission contained it. This is a parser artifact, not an author omission.

6. **Strength finder's generic/overstated strengths.** Several strengths from the strength finder were generic or superficial and have been removed (e.g., "the paper addresses an important problem," "the paper targets an interesting question"). Only concrete, evidence-grounded strengths are retained above.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any pattern or observation that the paper itself does not already articulate.

## Suggestions

1. **Rewrite the derivation in Section 4.2 with full mathematical clarity.** Show explicitly how the chain rule of probability applies to the PCFG marginal distribution, write out the KL divergence expansion in standard notation (avoiding the garbled equation (4)), and show the step-by-step algebra that leads to the subgrammar decomposition. Even a sketch of the proof should be self-contained enough for a reader to verify the conceptual structure.

2. **Explain how subgrammar KL terms are computed empirically.** Clarify whether the subgrammar KL values in Figures 1 and 2 are computed by restricting the model's output to the relevant subgrammar's vocabulary given specific prefixes, or by some other procedure. This would make the empirical validation non-circular.

3. **Add experimental details and error bars.** Include the model architecture specifications (embedding size, heads, layers, parameters), training hyperparameters, and grammar definitions in the main text or a clearly accessible appendix. Add error bars or confidence intervals to the CKA results.

4. **Either drop or properly contextualize the GPT-5.1 anecdote.** If the paper wants to make a point about larger models, run a proper experiment; otherwise, the anecdote detracts from the paper's rigor.

5. **Strengthen Corollary 4.7** by providing a concrete condition under which gradient independence holds (e.g., if the model has separate parameters for each subgrammar, or if the Hessian is block-diagonal) rather than restating the definition.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 63r6HyqyRm (Vision-free Baseline) | 2.33 | 1 | Much weaker — unfair comparisons, unclear motivation. The paper under review is clearly more substantial. |
| uOnElfFuey (Hardening LMs) | 3.0 | 1 | Weaker — limited scope (5 simple languages), serious methodological concerns. The paper under review has a richer theoretical framework. |
| 2PKLRmU7ne (ICL and Occam's razor) | 5.6 | 1 | Comparable — both have novel theoretical perspectives with insufficient rigor in execution. The paper under review has more empirical grounding. |
| MF7ljU8xcf (Compute-Optimal LLMs) | 6.0 | 1 | Stronger — complete proofs, thorough empirical validation, clearer presentation. The paper under review is less rigorous. |
| b5lXUwZiD3 (Limitation of Transformer for HMMs) | 5.25 | 2 | Comparable — both study transformer learning of formal structures with a mix of theory and experiments. The paper under review has more originality in its theoretical framework. |
| v675Iyu0ta (Interpretability Illusions) | 5.6 | 2 | Comparable — both have a clear empirical contribution on formal languages. The paper under review is more ambitious theoretically but less polished. |
| Oz9FTPINRe (Causal Study on Learnability) | 5.75 | 2 | Comparable — both introduce novel methodology for studying formal language learning. The paper under review has a more directly novel theoretical contribution. |
| 3EWTEy9MTM (Chain of Thought Empowers Transformers) | 6.33 | 2 | Stronger — rigorous theory with complete proofs, clear empirical confirmation. The paper under review is less complete. |

**Round 1 Bracket:** 4.5 – 6.5

**Round 2 Narrowing:** The paper sits in the 5.25–5.75 range. It is more ambitious than "Limitation of Transformer for HMMs" (5.25) but less rigorous than "Compute-Optimal LLMs" (6.0). It is comparable to "ICL and Occam's razor" (5.6) in having a novel conceptual framework with execution gaps. The paper's theoretical ideas are genuine contributions, but the sketchy presentation of the core derivation, the reliance on the appendix for proofs, and the potentially circular empirical validation hold it back.

**Final Score:** 5.5 — The paper has a genuinely novel theoretical framework and interesting empirical findings, but the presentation of the core derivation is insufficiently rigorous, the key proofs are inaccessible, and the empirical validation is not as clean as it should be. This is a borderline paper that would need substantial revision to be acceptable.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>