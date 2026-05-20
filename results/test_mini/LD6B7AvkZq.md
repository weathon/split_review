Now I have enough information for calibration. Let me write the final review.

**Round 1 bracket:** The paper sits between the weak anchors (2.5–3.33) and the strong anchors (7.5+). The most topically similar anchor is "Context-free Recognition with Transformers" (5.50, Reject), which had a similar mix of novel theory with presentation issues. This gives an initial bracket of roughly 4.0–6.0.

**Round 2 narrowing:** Comparing against "Context-free Recognition with Transformers" (5.50, Reject), "Evolutionary perspective on modes of learning" (5.33, Accept), and "Empirically Testing Expressivity Bounds" (4.50, Reject):

- The current paper has more theoretical novelty than the evolutionary perspective paper but has real mathematical imprecision in its key definitions — unlike the evolutionary paper which reviewers found "no fatal flaws."
- The current paper has more extensive empirical work than the CFG Recognition paper, but both have similar issues with theory presentation.
- The current paper is stronger than the 4.50 anchor (which had a fundamental methodological flaw) and marginally weaker than the 5.33 anchor (which had clean experiments with no fatal flaws).

Final score: 5.0. The paper has novel and interesting ideas but the theoretical presentation has real imprecision that needs addressing before acceptance.

---

## Summary

This paper studies how language models learn context-free grammars (CFGs) by introducing the concept of *subgrammars* — the recursive substructure of CFGs. The authors prove a suite of theoretical results showing that the KL divergence (equivalently, the language modeling loss) decomposes as a sum over subgrammars. Empirically, they train small transformers on synthetic PCFGs and observe that all subgrammars are learned in parallel (unlike the staged progression hypothesized for children), that pretraining on a subgrammar can improve final loss and induces representations more aligned with the grammar's substructure (measured via CKA and cosine similarity), and that models struggle with deep recursive structures even when they handle long non-recursive strings well.

## Strengths

1. **Novel theoretical framing — KL decomposition over subgrammars (Theorems 4.3, 4.6).** The idea that the language modeling loss inherits the recursive substructure of the target PCFG is genuinely novel and goes beyond prior work which studied static representations of trained models. Theorem 4.6, connecting expected recursion to divergence blow-up, provides a clean mathematical relationship between recursion depth and learning difficulty.

2. **Empirical identification of parallel subgrammar learning.** Figures 1 and 2 show that KL divergences for all subgrammars (inner and outer) decrease simultaneously from the start of training. While not a formal proof, this visual pattern is a nontrivial observation — subgrammars with different structural complexity could plausibly be learned at different rates.

3. **CKA-based activation analysis with 30 seeds (Table 1, Section 5.2).** The paper provides a systematic, multi-seed analysis showing that subgrammar pretraining yields higher representational alignment and better segregation of subgrammar vs. non-subgrammar strings. The use of CKA across both attention and MLP layers, with percentage changes reported for 2- and 4-layer transformers, offers concrete evidence for representational effects of curriculum learning on CFGs.

4. **Clean depth-vs-length experiment (Figure 3).** The controlled comparison between extending context at fixed recursion depth vs. increasing recursion depth cleanly isolates the failure mode: models fail on depth, not length, even though the next-token distribution is identical in both conditions. The finding is clear and reproducible.

## Weaknesses

### Fatal
None.

### Major

1. **Definition 4.2 is mathematically imprecise and incomplete.** The central quantity $D_{\text{KL}}(P_G \parallel Q)_A$ — used in every subsequent theorem — is defined with two issues: (a) the term $D_{\text{KL}}(P_G \parallel Q \mid \neg s)$ (with unexplained "$\neg s$") is not a standard conditional KL divergence and is left undefined anywhere in the paper; (b) the inner sum $\sum_{a \in \Sigma^*}$ has an unused summation variable $a$, making the expression formally undefined. While the surrounding text clarifies the intended meaning ("restriction of the KL divergence to substrings from subgrammar $A$"), the definition as written cannot be parsed mathematically. Since this definition anchors Theorem 4.3 and all subsequent results, the theoretical contribution would need a clean, self-contained definition to be fully assessable. **This is the paper's most significant weakness.**

### Minor

2. **Equation (4) uses nonstandard notation that obscures the derivation.** The fractions $\frac{\log P_G(\alpha \mid \epsilon)}{\log Q_\theta(\alpha \mid \epsilon)}$ are not a standard way to express a restricted KL divergence and are not defined in the paper. The intended conclusion — that the KL divergence decomposes into three conditioned terms — is stated clearly in Equation (5) and Theorem 4.3, so the core result survives. But the intermediate step is confusing and could mislead readers.

3. **No direct quantitative verification that per-subgrammar KLs sum to the total KL.** Figure 1 shows individual subgrammar KL curves and the text claims they sum to the full KL divergence, but no overlay, residual plot, or numerical comparison is provided. This is a straightforward experiment (compute the weighted sum and compare to the measured total) that would either validate or challenge the theoretical decomposition. Its absence weakens the link between theory and experiment.

4. **Table 1 reports CKA averages without confidence intervals or significance tests.** The percentage changes (e.g., +8.9%, +21.7%) are presented as meaningful, but without standard deviations or statistical tests across the 30 seeds, it is unclear which differences are robust and which may be noise. Parallel learning claim could benefit from a formal baseline — the paper asserts all subgrammars are learned "in parallel" but does not define or test what sequential learning would look like, nor compare against a null model.

### Trivial

5. The paper occasionally refers to Figure 6 and Table 3 for critical results (improved final loss from pretraining, cosine similarity gap analysis) that would ideally be presented in the main text rather than deferred to the (stripped) appendix.

## Nice-to-Haves

- A direct numerical verification that weighted per-subgrammar KLs sum to total KL within numerical error would substantially strengthen the empirical support for Theorem 4.3.
- Including confidence intervals or error bars in Table 1 would help readers assess the reliability of the CKA findings.
- Testing on a broader set of grammars (beyond the single family used in experiments) would help establish generality.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism that Equations (1)–(3) are "incoherent" or "mathematically nonsensical."** The expansion in (2)–(3) is a standard autoregressive factorization of the log-ratio $\log(P_G(\alpha a \beta) / Q_\theta(\alpha a \beta))$ and is mathematically correct. The confusing line break between (2) and (3) is a parser artifact, not an author error. *Removed: factually incorrect criticism.*

2. **Criticism about Figure 6 and Table 3 being absent from the main text.** These are appendix figures/tables stripped by the parser; they exist in the original submission. *Removed: parser artifact, not author error.*

3. **Criticism that the paper lacks comparison to child language data.** The paper mentions children only as an intuitive contrast in one sentence of the abstract and introduction; it does not claim to conduct a developmental study. Demanding child data is scope creep. *Removed: scope creep.*

4. **Criticism about grammar complexity / single-family grammars.** The paper explicitly studies small CFGs as a controlled surrogate. Testing broader grammars is a nice-to-have, not a requirement for this type of initial investigation. *Removed: requests beyond stated scope.*

5. **Criticism about missing experimental details (hyperparameters, architecture, etc.) in the main text.** These are standard appendix content. *Removed: missing appendix content.*

6. **Criticism about the "parallel learning" claim being "trivial."** The claim that all subgrammar KLs decrease together is not trivial — subgrammars with different complexity could in principle be learned at different rates. The observation is a genuine finding, even if a formal baseline would strengthen it. *Demoted to Minor, not removed entirely.*

7. **Criticism that the "cross-entropy" (Strenth Finder's terminology) comparison to children is never operationalized.** This appears in the Strength Finder, not the Harsh Critic. The paper only mentions children as a motivating contrast; a full developmental comparison is outside scope. *Removed: scope creep.*

## Novel Insights

The reviews surface a tension that the paper does not fully resolve: the theoretical contribution (KL decomposition over subgrammars) is presented as the paper's centerpiece, yet the key definition (Definition 4.2) is sloppy enough to make the theory hard to evaluate from the main text alone. Meanwhile, the strongest evidence comes from the empirical sections (CKA analysis, depth generalization) that are less dependent on the theory's precision. This suggests the paper might be better served by either (a) tightening the theory to the same standard as the experiments, or (b) repositioning the theory as a motivating framework rather than a formal contribution, and foregrounding the empirical findings as the primary result. As written, the paper falls between two stools: the theory is too imprecise to stand alone, and the experiments, while interesting, do not fully verify the theoretical decomposition they claim to support.

## Suggestions

1. **Fix Definition 4.2.** Replace $D_{\text{KL}}(P_G \parallel Q \mid \neg s)$ with a properly defined conditional KL divergence (e.g., $D_{\text{KL}}(P_G(\cdot \mid s) \parallel Q(\cdot \mid s))$ or a clearly defined restriction). Remove the unused summation over $a$. Provide an explicit expression in terms of string probabilities so the definition is self-contained.

2. **Add a direct verification of the decomposition.** Compute the weighted sum of per-subgrammar KL divergences from Figure 1, overlay it against the measured total KL, and report the residual (or relative error). This single addition would substantially strengthen the empirical grounding of the theory.

3. **Add error bars / confidence intervals to Table 1.** Since 30 seeds are used, reporting standard deviations would allow readers to assess the statistical significance of the reported differences.

4. **Clean up Equation (4).** Either replace it with the clear statement already present in Equation (5) and Theorem 4.3, or rewrite it using standard notation for restricted KL divergences.

## Score and Decision

**Round 1 bracket:** The paper is substantially stronger than the weak-reject anchors at scores 2.5–3.33 (papers with "Transformers Can Learn Connectivity" 2.50, "Token Dynamics" 2.67), weaker than the strong-accept anchors at scores 7.5+ (which are tightly executed papers on different topics), and comparable to middle-band anchors at 4.5–6.5. The closest topical anchor is "Context-free Recognition with Transformers" (5.50, Reject), which had a similarly sloppy theory presentation and a mix of strong/weak reviewers. Initial bracket: **4.0–6.0**.

**Round 2 narrowing:** Compared to "Evolutionary perspective on modes of learning in Transformers" (5.33, Accept) — a paper with clean experiments and no fatal flaws but modest novelty — the current paper has more theoretical ambition but real mathematical imprecision that the evolution paper lacked. Compared to "Empirically Testing Expressivity Bounds" (4.50, Reject) — a paper with a fundamental methodological issue (uncalibrated sampling) — the current paper is stronger in both novelty and methodology. The paper sits closest to the 5.0–5.5 range but on the lower end, because the theory issues are central (the paper claims theorems as its main contribution) whereas the cleaner experiments (CKA, depth generalization) are presented as secondary.

**Anchor comparison table:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| yUvvOVO6Yu (Kinetics of Reasoning) | 3.00 | R1 | Weaker — less novelty, less rigorous experiments |
| AlcHdWZZoF (Training Dynamics Parametric/ICL) | 3.33 | R1 | Weaker — narrower scope, less formal theory |
| 5WAGOydkNJ (Transformers with RL/SFT) | 3.00 | R1 | Weaker — incremental theory contribution |
| sLIk7DauaJ (Transformers Learn Connectivity) | 2.50 | R1 | Weaker — unclear claims, insufficient evidence |
| ACn1hhGcV4 (Context-free Recognition) | 5.50 | R1, R2 | Similar — both have theory with presentation issues; current paper has broader empirics |
| EAfMzT8ZLy (How Transformers Get Rich) | 4.50 | R1, R2 | Similar — both have theory with limited scope; current paper more original |
| CfFj68C9Cn (Learning to Recall with Transformers) | 6.50 | R1 | Stronger — cleaner theoretical analysis, better empirical validation |
| UjDE4mmOBB (Empirically Testing Expressivity) | 4.50 | R1, R2 | Similar rigor, but current paper has more novel contributions |
| m5KplPzCzM (Learning Pseudorandom Numbers) | 5.33 | R2 | Stronger empirics, weaker theory; comparable overall quality |
| 7Sph4KyeYO (Constrained Decoding Diffusion LLMs CFGs) | 5.50 | R2 | Stronger in practical contribution, but less novel theoretically |
| 5ubZyHPhnK (Evolutionary perspective) | 5.33 | R2 | Stronger — clean experiments, no fatal flaws; current paper has more ambitious but sloppier theory |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>