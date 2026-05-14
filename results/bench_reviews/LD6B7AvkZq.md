Now I'll write the final consolidated review.

## Summary

This paper introduces a framework for studying how language models learn context-free grammars (CFGs) by decomposing them into "subgrammars" (inner subgrammars as subtrees of derivations, and outer subgrammars as restricted rule sets). The authors claim a theoretical result — that the KL divergence of a language model from a PCFG decomposes recursively over subgrammars (Theorems 4.3, 4.6). Empirically, they show that small transformers' losses decompose accordingly (Figure 1), observe that all subgrammar losses decrease simultaneously during training ("parallel learning"), study whether subgrammar pretraining improves representations via CKA analysis (Table 1), and demonstrate that models fail on deep recursive structures (Figure 3).

## Strengths

1. **Novel formalization of subgrammar structure.** The definitions of inner and outer subgrammars (Definitions 3.3–3.5) are clean, and the idea of decomposing CFG learning dynamics over substructure is a well-motivated research direction that prior work on CFG learning has not pursued. Theorem 4.1 (unique DAG decomposition) provides a useful organizing principle.

2. **Empirical validation of loss decomposition.** Figure 1 convincingly shows that the KL divergence decomposes into subgrammar-specific components throughout training, consistent with the claimed recurrence. This is a concrete empirical demonstration that the subgrammar decomposition is measurable and meaningful in practice.

3. **Depth-failure experiment is clean and insightful.** Figure 3 isolates depth of recursion (not length) as the key difficulty: the model maintains low error on long flat contexts (error 0.017) but degrades on deep recursive contexts (error 0.173). This is a well-controlled experiment that cleanly separates two confounded factors and extends prior length-generalization work.

4. **The paper opens a productive research direction.** The subgrammar decomposition lens for studying grammar learning dynamics is genuinely novel and could stimulate follow-up work on curriculum learning, mechanistic interpretability, and understanding what makes certain grammatical structures hard for neural networks.

## Weaknesses

### Major

1. **The illustrative derivation (Equations 1–4) is mathematically invalid as presented.** Equation (4) writes `\frac{\log P_G(\alpha|\epsilon)}{\log Q_\theta(\alpha|\epsilon)}` — a ratio of logs — which does not follow from the sum of `P(αaβ)[log P - log Q]` in equations (2)–(3). The quantity `log P / log Q` is not equal to `log(P/Q)` and does not arise from any standard manipulation of the KL divergence. The paper says "In an abuse of notation" but does not explain what notational abuse is being committed or provide a correct intermediate step. While the *conceptual* claim that the KL decomposes into conditioned divergences is clear and the formal theorems (4.3, 4.6) are stated separately, this error undermines reader confidence in the theoretical development at a critical juncture. The proofs in the appendix (stripped by the parser) cannot be evaluated here, but the main text's derivation is not salvageable as written.

2. **Definition 4.2 is incoherent as stated.** The definition `D_KL(P_G || Q)_A = sum_s P(s|ε) P_G(A|s) sum_a D_KL(P_G || Q | ¬s)` uses the notation `D_KL(P_G || Q | ¬s)` which is never defined, and `P_G(A|s)` where `A` is a subgrammar (not a string-generating event) — its probabilistic interpretation is not specified. This definition is the core of how the paper connects subgrammars to KL divergence, and its imprecision makes the theoretical results that depend on it (Theorems 4.3, 4.6) difficult to assess from the main text alone.

3. **The empirical evidence for "parallel learning" is purely observational and not tested against alternative accounts.** The paper claims transformers "learn all subgrammars in parallel" based on the observation that all subgrammar KL divergences decrease simultaneously (Figures 1–2). This is consistent with the training data containing all subgrammar strings, so all losses naturally decrease. The paper acknowledges "one could cook up a pathological scenario where a model independently optimizes each subgrammar in sequence" and offers Corollary 4.7 as a condition for parallel learning, but this condition is stated informally and is nearly tautological ("if gradients on one subgrammar don't hurt others, then all improve simultaneously"). Without a controlled experiment that distinguishes genuinely parallel optimization from coincident decreases driven by shared training signal, this claim is not established beyond being a visual observation.

### Minor

4. **CKA analysis reports percentage changes on tiny absolute differences without confidence intervals.** In Table 1, the reported differences are small (e.g., 0.258 vs. 0.281, an absolute difference of 0.023 on a 0–1 scale), yet the paper highlights "+8.9% change" which inflates the apparent effect. No confidence intervals, bootstraps, or significance tests are provided despite 30 random seeds. The text says the pretraining effect "diminishes as the model size increases," which further limits the generality of this finding. The claim about "definitive" alignment differences (abstract, Section 5) is not supported by the reported numbers.

5. **Theorem 4.6 (expected recurrence formula) and Corollary 4.5 (context-insensitive decomposition) crucially depend on a "context-insensitivity" assumption that is not empirically verified.** The paper mentions that "our experiments suggest that this condition is perhaps not so strong" and cites a qualitative observation about varying prefixes, but provides no quantitative test. This weakens the connection between theory and experiments.

6. **Corollary 4.7 is essentially a tautology.** It states: if gradients on subgrammar Aᵢ do not increase the loss on other subgrammars, then all subgrammar losses decrease. This is close to restating the definition of "not hurting" and provides no testable or falsifiable condition, nor any architectural or algorithmic insight into *why* this property might hold.

### Trivial

7. Equation (2) and (3) appear to be split across two separate equation blocks with the closing bracket on (3), making the parsing of the algebra harder to follow.

## Nice-to-Haves

- The anecdotal GPT-5.1 results (5/5 shallow vs. 2/5 deep) are explicitly disclaimed as "purely anecdotal" and "should not be interpreted as direct evidence." Including them is a stylistic choice that some readers may find useful for context. Properly controlled experiments would be needed to draw any conclusions.
- Testing the parallel learning claim with controlled interventions (e.g., introducing subgrammars at different phases of training) would substantially strengthen the empirical contribution.
- A mechanistic analysis of *why* models fail on deep recursion (e.g., attention pattern analysis, probing hidden states at varying depths) would add value beyond the behavioral observation.

## Removed Points

These points from the reviewers are flagged to be removed; treat them with caution:

- **"The equations in Section 4.2 are 'fundamentally incomplete and incoherent' / invalidate the paper's central claim."** — While the illustrative derivation (Eq. 1–4) is indeed broken as presented, the formal theorems (4.3, 4.6) are stated independently as separate mathematical claims with proofs deferred to the appendix. The harsh critic conflates a sloppy illustrative example with the formal contribution. The core conceptual claim — that KL divergence decomposes over subgrammars — is meaningful even if the in-line derivation is garbled. However, I have kept the substance of this criticism as a Major weakness above (points 1 and 2), tempered to reflect that the theorems may still be correct.
- **"Frontier model experiments should not be in the paper."** — The paper explicitly disclaims these as "purely anecdotal" and "should not be interpreted as direct evidence." Including exploratory/disclaimed results is a common practice in ML papers to suggest future directions, not a scientific error.
- **"The paper never delivers on explaining 'how language models learn.'"** — This is a framing critique about the ambitious title, not a substantive technical weakness. The paper defines subgrammar decomposition and shows empirical correlations, which is a meaningful start even if causal mechanisms are not fully established.
- **"The paper overclaims novelty relative to prior work."** — The paper properly cites Gruska (1971) regarding the DAG decomposition and discusses related work (Cagnetta & Wyart, 2024; Allen-Zhu & Li, 2023). The claim to novelty is about the *learning dynamics* lens applied to subgrammar structure, which is a reasonable distinction.
- **Strength Finder's generic strengths** (e.g., "the paper addressed an important problem" — these are dropped when they lack specific content or conflict with verified weaknesses).
- **Missing appendix / missing references / formatting nitpicks** — The appendix is stripped by the parser; these are not missing from the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the work that the paper itself does not already make. The depth-failure result (Figure 3) and the subgrammar decomposition framing are the paper's own contributions; no reviewer offers a genuinely new synthesis beyond what is already in the text.

## Suggestions

1. **Fix the illustrative derivation in Section 4.2.** Rewrite equations (1)–(5) to show a correct algebraic path: the sum `sum_a P(αaβ)[log P(...) - log Q(...)]` should be grouped into separate terms for prefix, subgrammar A, and suffix, each of which is a weighted KL-like term. The current equation (4) with `log P / log Q` must be replaced.

2. **Clarify Definition 4.2.** The notation `D_KL(P_G || Q | ¬s)` and `P_G(A|s)` need precise definitions. What does it mean to condition the KL divergence on "not s"? How is the probability of a subgrammar (a set of rules, not a string) conditioned on a prefix defined? The appendix may contain these details, but the main text should be self-contained at the definition level.

3. **Add a controlled experiment for the parallel learning claim.** Train on a grammar where subgrammar A appears only in the first half of training and subgrammar B only in the second half. If the KL for A continues to decrease during the B-only phase, that would genuinely demonstrate parallel/non-interfering learning.

4. **Report confidence intervals or bootstrap distributions** for the CKA values in Table 1, and avoid reporting percentage changes on absolute differences of <0.05 on a 0–1 scale unless effect sizes are clearly stated.

5. **Quantitatively test the "context-insensitivity" assumption** (Corollary 4.5) by measuring the variance of `Q_θ(A|s)` across different contexts `s` for each subgrammar `A`.

6. **Provide the mechanistic analysis of the depth-failure** that is currently missing. The paper shows *that* models fail on deep recursion but not *why* — an analysis of attention patterns, hidden state dynamics, or probing results would substantially strengthen this finding.

## Score and Decision

**Calibration anchors (all from the human review corpus):**

| Anchor Path | Avg Human Score | Comparison to this paper |
|---|---|---|
| `/home/.../L8SMNWsxfK` (Automata Learning & LM Support) | 7.00 | Significantly stronger: clean theoretical results, rigorous proofs, well-structured experiments. This paper is far less polished and rigorous. |
| `/home/.../ACn1hhGcV4` (Context-free Recognition with Transformers) | 5.50 | Stronger theory but weaker experiments; this paper has more empirical content but weaker theory. Comparable overall quality. |
| `/home/.../JkitQScjuL` (Alignment Between Supervised & Self-Supervised CL) | 5.50 | Tightly argued with clear theory and experiments. This paper is less focused and less rigorous. |
| `/home/.../bkSKvJjziW` (Scarcity–Complexity Collision) | 4.50 | Similar level: interesting ideas with presentation issues and limited scope. This paper has more experiments but weaker theory. |
| `/home/.../ADeeoMY4Dn` (Compositional Generalization) | 4.50 | Better presented and more systematic investigation. This paper is less well-structured. |
| `/home/.../zkeRriSIEl` (Bearing Syntactic Fruit) | 4.00 | Similar tier: interesting research direction, clear motivation, but limited empirical scope and overstated claims. |
| `/home/.../Fq1pyj9xQm` (Length Generalization with LDRU) | 3.60 | Narrower scope but cleaner experiments. This paper has more conceptual ambition but messier execution. |
| `/home/.../Vv8mXtf8Lx` (Randomly Sampled Language Reasoning) | 3.50 | Weaker: less rigorous and less clear contributions. This paper is somewhat stronger in originality. |

Positioning relative to these anchors: The paper scores below the well-executed 5.5–7.0 papers due to its unclear theoretical presentation and overstated claims. It is comparable to the 4.0–4.5 tier of papers that have interesting ideas but significant execution issues. The theoretical flaws (invalid illustrative derivation, unclear definitions) and the gap between claims and evidence (parallel learning, CKA analysis) prevent a higher score.

**Score:** 4.0

**Decision:** Reject — The paper introduces a genuinely interesting research direction and contains one well-executed experiment (depth-failure), but the theoretical section contains a mathematically invalid derivation (equation 4) and an unclear central definition (Definition 4.2) that undermine confidence in the core contribution. The empirical claims about parallel learning and representational alignment are overstated relative to the evidence. A substantially revised version with corrected mathematics, controlled experiments, and toned-down claims could be suitable for resubmission.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>