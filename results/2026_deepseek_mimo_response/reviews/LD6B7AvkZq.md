Now I have sufficient calibration data. Let me finalize the review and score.

**Round 1 bracket: 5.0–7.0**. The paper is clearly above the 5.0 anchors (which face novelty and clarity issues) and below the 7.0 anchor (which has a more ambitious theoretical claim about predicting phase transitions). 

**Round 2 narrowing: 5.5–6.5**. Compared to "Training Neural Networks as Recognizers" (6.25, comparable topic, clear methodological contribution) and "Dynamics of Concept Learning" (6.5, similar theory-to-empirics approach), the paper sits in the same range. It has a stronger conceptual framework than the 6.25 paper but weaker statistical rigor.

**Final score: 6.0**. The paper initiates a genuinely novel research direction with clean theoretical decomposition and interesting empirical findings, but suffers from weakly justified assumptions and inconsistent rigor.

---

## Summary
This paper introduces "subgrammars" for context-free grammars (CFGs)—inner subgrammars (subtrees of derivations) and outer subgrammars (simplified subsets of the grammar)—and proves that KL divergence of language modeling decomposes as a recurrence over these subgrammar structures. Empirically, the authors show that small transformers learn all subgrammars in parallel, that pretraining on a subgrammar can improve final loss and align internal representations with grammar structure, and that models struggle with deep recursion even when achieving low training loss.

## Strengths
- **Novel conceptual framework for LM learning dynamics on CFGs**: The definition of inner and outer subgrammars, and studying LM training through this lens, fills a genuine gap. Prior work (Cagnetta & Wyart, 2024; Allen-Zhu & Li, 2023) studied static representations of trained models on CFGs; this paper studies the *dynamics* of learning with respect to grammatical substructure. The parallel to how function-class substructure (e.g., monomials in polynomials) guides learning dynamics research is well-motivated (line 17).
- **Clean KL-divergence decomposition with visual validation**: Theorem 4.3 shows loss decomposes over subgrammars, and Theorem 4.6 derives the 1/(1−E[R]) closed form for recursive grammars. Figure 1 provides striking empirical validation—per-subgrammar KL divergences visibly sum to total KL divergence throughout training, across different probability configurations.
- **Well-controlled depth vs. length experiment (Figure 3)**: Comparing (a)^i (increasing length, fixed depth) vs. ^i (increasing depth) with identical next-token distributions cleanly isolates recursion depth as the failure mode. Error stays at 0.017 for (a) but grows to 0.173 for (b), a tenfold difference.
- **Curriculum learning findings with representational analysis (Section 5.2, Table 1)**: CKA analysis across 30 random seeds shows pretrained models exhibit 8–22% higher attention-layer alignment. The finding that subgrammar pretraining helps 2-layer models achieve lower final loss, and that pretrained models better segregate subgrammar vs. non-subgrammar sequences (via cosine similarity analysis), provides concrete evidence that the subgrammar framework has practical utility beyond analysis.
- **Intriguing parallel learning observation**: The empirical finding that all subgrammars are learned simultaneously (Figures 1, 2) contrasts with children's sequential acquisition of syntactic constructions, opening a new research direction.

## Weaknesses

### Fatal
None

### Major
- **Context-insensitivity assumption is load-bearing and weakly justified**: The cleanest decomposition (Corollary 4.5, Theorem 4.6) requires the model's distribution over a subgrammar's strings to be independent of surrounding context. The paper acknowledges this is "a strong assumption" (line 168) but justifies it with a single qualitative observation: "varying the prefix did not result in qualitatively different results" (line 200) for one grammar/model combination. The paper argues deep-recursive prefixes are "rare" under the true distribution, but this is precisely the regime where context-sensitivity matters most for autoregressive models. The paper notes approximate versions are possible "out of interest of space" (line 168) but doesn't present them. Without systematic empirical quantification (e.g., max KL across different prefixes) or formal error bounds, the most elegant theoretical results rest on a weakly verified foundation.
- **Corollary 4.7 (parallel learning condition) provides limited explanatory power**: The sufficient condition—that gradient updates on one subgrammar don't increase KL on any other—is nearly vacuous in the paper's setting of small overparameterized transformers on tiny PCFGs, where the models have enough capacity to memorize the entire grammar. The paper acknowledges this (line 214: "they are likely still overparametrized with respect to the even tinier PCFGs") but offers no path to weakening the assumption or demonstrating when it might fail.
- **Inconsistent statistical reporting**: Variance bands appear in Figure 3 but are absent from Table 1 (CKA analysis) and Figures 1–2 (KL decomposition), despite using 30 random seeds for Table 1. The 8–22% CKA changes lack confidence intervals or significance tests. For a paper that invokes statistical arguments in its theoretical framework (e.g., context-insensitivity holding "statistically"), this omission undermines credibility of the key curriculum learning results.

### Minor
- **Theoretical depth is modest**: The central theorems apply the chain rule of KL divergence and PCFG conditional independence to the autoregressive setting—conceptually useful but technically straightforward. Theorem 4.1 is acknowledged to correspond to Gruska (1971). The framework names the right objects and provides the right language, but individual results are natural consequences of the setup.
- **Section 6 largely confirms known phenomena**: The finding that transformers struggle with deep recursion is well-established (Bhattamishra et al., 2020; Lampinen, 2024). The paper adds specificity via the clean depth-vs-length experimental design but doesn't substantially deepen understanding of *why* this occurs.
- **GPT-5.1 anecdote adds little**: With n=5, unspecified grammar, and the paper's own caveat (line 303: "purely anecdotal"), this doesn't strengthen the contribution. The controlled experiments already make the point convincingly.
- **Key results referenced but not shown in main body**: Figures 5, 6, and Table 3 (position robustness, curriculum learning loss curves, cosine similarity analysis) are referenced in the main text but their content is not visible in the main body sections I can verify. These contain results supporting Sections 5.1 and 5.2 and would benefit from main-text placement.

### Trivial
- Definition 4.2 notation may be garbled in the published version (line 136)—authors should verify.

## Nice-to-Haves
- Formally bound the approximation error of Corollary 4.5 as a function of model context-sensitivity, or at minimum report an empirical context-sensitivity measure systematically across grammars.
- Empirically measure cross-subgrammar gradient interference (e.g., cosine similarity of gradients) to test whether Corollary 4.7's condition is approximately satisfied.
- Include at least one grammar definition in the main text.
- Compare transformers to RNNs/LSTMs on the same grammars to assess architecture-specificity.
- Systematically vary grammar complexity, model size, and pretraining duration for the curriculum learning analysis.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Harsh critic's claim that Figures 5, 6, Table 3 are "not in the main body" — cannot fully verify whether these were in main text or appendix of the original submission since the parser strips appendix content. Kept as a minor concern with appropriate caveats.
- Harsh critic's request for comparison to RNNs/LSTMs — moved to nice-to-have as it's outside the paper's stated scope.
- Strength finder's claim about robustness of subgrammar retention (Figure 5) — relies on content not visible in the parsed text, potentially stripped appendix material.

## Novel Insights
The most genuinely novel observation from synthesizing the reviews is that the paper's strongest contribution may actually be the practical angle (Section 5.2) rather than the theoretical decomposition. The curriculum learning + CKA analysis demonstrates that the subgrammar framework has *actionable* utility—it can guide training strategies that produce structurally-aware representations—beyond being merely an analytical lens. This practical contribution is more novel and robust than the theoretical results, which are elegant but follow from standard tools. The theoretical contribution's primary value is providing the formal vocabulary ("subgrammar," "KL recurrence") that makes the empirical findings expressible and interpretable.

## Suggestions
- Strengthen context-insensitivity analysis: report empirical context-sensitivity measures across multiple grammars and model sizes, not just one qualitative observation.
- Move Figures 5, 6, and Table 3 into the main body—these contain the paper's most interesting empirical results.
- Add error bars/confidence intervals to Table 1 using the existing 30-seed data.
- Expand curriculum learning analysis with ablation over pretraining duration and model size.
- Either substantively develop Corollary 4.7 (e.g., empirical gradient interference analysis) or de-emphasize it in favor of the stronger empirical contributions.

## Score and Decision

**Calibration Anchors Retrieved:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Recovering Knowledge by Hardening LMs | uOnElfFuey | 3.0 | 1 | Much weaker—extracts DFAs from regular languages, limited scope |
| Inductive Transformers | NSBP7HzA5Z | 3.0 | 1 | Much weaker—vague claims about inductive bias, poor empirical support |
| Role of Task Complexity | OW5Gf4cse1 | 3.0 | 1 | Weaker—narrow ListOps focus, modest contributions |
| Self-Consuming Training Loop | SaOxhcDCM3 | 3.2 | 1 | Weaker—different topic, mixed reviews |
| Percolation Model of Emergence | 0pLCDJVVRD | 7.0 | 1 | Stronger theoretical ambition (percolation model predicts phase transitions), but faces similar criticism about insufficient evidence for claims |
| Sudden Drops in Loss | MO5PiKHELW | 5.5 | 1 | Our paper has stronger theoretical framework; that paper studies syntax acquisition in MLMs with phase transitions |
| Geometric Signatures of Compositionality | q5lJxCXjiY | 5.4 | 1 | Our paper has more concrete empirical validation; that paper's geometric approach is interesting but less grounded |
| Dual Process Learning | jDsmB4o5S0 | 6.0 | 1 | Comparable contribution level—clear framework with solid experiments |
| Self-Improvement in LMs | WJaUkwci9o | 8.0 | 1 | Stronger—more rigorous theoretical analysis of sharpening mechanism |
| Interpolating AR and Diffusion | tyEyYT267x | 8.0 | 1 | Stronger—sets new SOTA with rigorous theoretical + empirical contribution |
| Rethinking Reward Modeling | rfdblE10qm | 8.0 | 1 | Stronger—deeper theoretical analysis with practical impact |
| When can transformers reason | STUGfUz8ob | 7.6 | 1 | Stronger—proves generalization theorems for relational reasoning |
| Training NNs as Recognizers | aWLQTbfFgV | 6.25 | 2 | Comparable—clear methodological contribution with extensive experiments, but weaker theoretical component |
| How transformers learn structured data | F0Zd3knG9j | 5.0 | 2 | Our paper is stronger—more novel framework, cleaner theory, better experiments |
| JoMA: Demystifying Multilayer Transformers | LbJqRGNYCf | 5.75 | 2 | Comparable—mathematical framework for transformer training dynamics |
| Dynamics of Concept Learning | s1zO0YBEF8 | 6.5 | 2 | Similar approach (theoretical abstraction validated empirically), roughly comparable |
| How Transformers Implement Induction Heads | 1lFZusYFHq | 6.2 | 2 | Comparable—theoretical analysis with empirical validation |
| Limitation of Transformer for HMMs | b5lXUwZiD3 | 5.25 | 2 | Our paper is stronger—more novel framework and cleaner experiments |
| Injecting Structural Inductive Bias | Oashk4fDD9 | 6.0 | 2 | Comparable—structural inductive bias via pretraining, similar curriculum angle |

**Bracket and calibration logic**: Round 1 placed the paper between 5.0 and 7.0. Round 2 anchors clustered between 5.25 and 6.5. The paper is clearly stronger than the 5.0–5.25 anchors (which face novelty and clarity issues) and comparable to the 6.0–6.5 anchors. It is weaker than the 7.0 anchor (Percolation Model) which has a more ambitious theoretical claim. The paper sits near 6.0—comparable to "Dual Process Learning" (6.0) and "Injecting Structural Inductive Bias" (6.0), slightly below "Dynamics of Concept Learning" (6.5) which has more rigorous theory.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: Accept