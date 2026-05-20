## Summary

This paper introduces a framework for studying how language models learn context-free grammars (CFGs) by decomposing the language modeling loss (KL divergence) over the subgrammar structure of PCFGs. The authors define inner and outer subgrammars, prove that the KL loss obeys recurrences over the subgrammar decomposition (Theorem 4.3, Corollary 4.5, Theorem 4.6), and empirically explore several consequences: (1) small transformers learn subgrammars in parallel, (2) curriculum pretraining on a subgrammar can improve final loss and internal representational alignment for small models, and (3) transformers struggle with deep recursion despite mastering shallow structure.

## Strengths

- **A clean conceptual framework for studying LM learning of CFGs.** The subgrammar decomposition provides a formal lens through which to analyze how language modeling loss relates to grammar substructure. Theorem 4.3 (KL as a recursive sum over subgrammars) and Theorem 4.6 (KL with expected recursion) are stated clearly and, while following from the chain rule for KL, are packaged into a useful formalism that enables the subsequent empirical investigations.

- **Empirical validation of the decomposition.** Figure 1 demonstrates that throughout training, the total KL divergence of a small transformer on synthetic PCFGs equals the sum of individually measured subgrammar divergences — directly confirming the theoretical recurrence. The paper also verifies the weighted version and extends the analysis to deeper recursion hierarchies (Figure 2a) and outer subgrammars (Figure 2b), showing the decomposition holds across varied structural configurations.

- **Identification of parallel subgrammar learning as a phenomenon.** The loss curves in Figures 1 and 2 reveal that subgrammars are learned simultaneously rather than sequentially, contradicting the intuitive expectation (and the analogy to child language acquisition drawn in the introduction). Corollary 4.7 offers a sufficient theoretical condition for when this parallelism would arise from gradient independence, opening a direction for future study of optimization dynamics in structured output spaces.

- **Clean isolation of depth vs. length in generalization failure (Section 6).** Figure 3 cleanly demonstrates that a trained transformer achieves near-zero prediction error on contexts extended by length without recursion (depth 0, error 0.017) but suffers dramatically on contexts built by recursive depth (error 0.173 at depth 200). This experiment cleanly separates depth-handling from mere length-handling as the fundamental limitation.

## Weaknesses

### Fatal

None.

### Major

- **Limited theoretical depth beyond the chain rule.** The central decomposition (Theorem 4.3, equations 1–5) follows directly from the autoregressive factorization of KL divergence applied to the CFG derivation structure. The paper acknowledges this in its derivation but does not use the recurrences to derive non-obvious, falsifiable predictions about learning dynamics. The recurrences are largely descriptive — they state that loss sums over substructure — rather than predictive of *how* or *when* learning occurs. Theorem 4.6 (the expected-recursion formula) is the most substantive result beyond the basic decomposition, but even this is a geometric-series argument under the context-insensitivity assumption. The paper would be significantly strengthened if it derived a concrete, testable prediction from these recurrences (e.g., a functional form for relative subgrammar learning speeds) and tested it empirically.

- **The paper attempts too many directions without developing any to convincing depth.** The theoretical framework (Section 4), parallel learning dynamics (Section 4), curriculum learning with alignment analysis (Section 5), and depth generalization (Section 6) are each touched upon but none is explored systematically. The curriculum learning results use a single grammar; the CKA analysis reports modest absolute values (0.25–0.35) without establishing what level of alignment would indicate genuine subgrammar representation; the generalization experiment is on a single "Nested Parentheses" grammar. The result is a collection of initial observations that, while individually reasonable, does not cohere into a mature contribution. Focusing on one of these directions — and producing a deep, controlled investigation — would yield a much stronger paper.

### Minor

- **Narrow empirical scope limits generality.** All experiments use hand-crafted CFGs that are tiny relative to any realistic linguistic structure, and the models are small transformers (2-layer, 4-layer). The observation that subgrammar learning proceeds in parallel is shown on a few grammars; the paper offers no systematic investigation of when this property holds across grammar families or model scales. The curriculum learning benefit (Section 5.2) is present for 2-layer transformers but disappears with 4-layer models, which the paper notes honestly but does not analyze further.

- **Lack of a control condition in curriculum learning experiments.** The paper shows that pretraining on a subgrammar before training on the full grammar can improve final loss for small models. However, it does not compare against a control that receives equivalent additional training without subgrammar-specific pretraining (e.g., simply a longer warm-up phase on the full grammar). Without this, it is difficult to attribute the benefit specifically to the subgrammar structure rather than to additional optimization steps or a more constrained initialization basin.

- **CKA evidence is suggestive but not definitive.** The paper claims that pretraining "results in internal representations that are more aligned with the grammar's substructure" and that this is shown "quite definitively." However, the absolute CKA values in Table 1 are modest (0.25–0.35), and while the percentage increases are positive (8.9%–21.7% for attention layers), it is unclear whether higher cross-seed similarity necessarily reflects better internalization of subgrammar boundaries — it could simply reflect a more constrained loss landscape induced by the pretraining phase. The cosine-similarity-based segregation analysis (described for Table 3) would strengthen this story, but the relevant table was in the stripped appendix.

- **Connection between generalization experiments and subgrammar theory is thin.** Section 6 cleanly shows that depth is the key difficulty, but the experiment does not exploit the theoretical framework to diagnose or predict the failure. For instance, the paper could test whether the error accumulation mirrors the recursive KL formula from Theorem 4.6, or measure how well the context-insensitivity assumption of Corollary 4.5 holds at different recursion depths. Without such a connection, the generalization experiment reads as a separate (though well-executed) finding rather than an application of the paper's core framework.

### Trivial

- The self-caveated GPT-5.1 Instant anecdote (footnote 3 explicitly states it is "purely anecdotal") is harmless given the caveat but contributes little beyond what the controlled experiments already show.
- The DAG decomposition of Theorem 4.1 is referenced in the recursive expansion but is not deeply exploited in subsequent results or experiments; the outer subgrammar concept is similarly underused in the main text.

## Nice-to-Haves

- A systematic ablation varying grammar properties (number of subgrammars, recursion depth, rule probabilities) to map out when the decomposition holds in practice and when models deviate from context-insensitivity would significantly strengthen Section 4.
- The open problems in the Discussion (Section 7) are sensible but vague. More concrete conjectures — e.g., a specific scaling relationship between recursion depth and KL error — would better guide follow-up work.
- An investigation of whether the parallel learning phenomenon (Corollary 4.7) genuinely stems from gradient independence or from overparameterization (as the authors briefly speculate) would sharpen this direction.

## Removed Points

*These points were flagged for removal during consolidation; treat them with caution.*

- **"The notation is cumbersome and obscures rather than illuminates the reasoning"** — This is a presentation-style nitpick without a specific anchor showing where the notation causes confusion. The derivation in equations (1)–(5) is explicit and follows standard conventions. **Removed.**

- **"Table 3 (mentioned in the text but not shown in the provided excerpt)"** — The appendix is stripped by the parser; this is a processing artifact, not a paper flaw. **Removed.**

- **"GPT-5.1 Instant test is not rigorous"** — The paper explicitly labels these tests as "purely anecdotal" in footnote 3 and states they "should not be interpreted as direct evidence." The harsh critic's criticism is already acknowledged by the authors. **Removed.**

- **"The paper lacks a clear statement of the specific hypothesis it intends to test"** — The paper does state its goal clearly: studying language modeling of CFGs with respect to subgrammar structure. The criticism is closer to "the experiments don't test risky predictions from the theory," which is captured in the Major weakness about limited theoretical depth. **Removed (merged).**

## Novel Insights

The most interesting observation emerging from the review process is the tension the paper itself surfaces but does not resolve: the empirical finding of parallel subgrammar learning contradicts the developmental analogy the introduction draws to child language acquisition (where simpler structures are mastered first). This tension between the mathematical decomposition (which permits parallel optimization) and the psychological expectation (which predicts sequential mastery) is genuinely interesting and underexplored. The paper would have been strengthened by directly investigating this contradiction rather than noting it in passing.

## Suggestions

- **Pick one direction and go deep.** The paper currently surveys several phenomena. The strongest version of this work would focus on either (a) deriving and testing a non-obvious, falsifiable prediction from the recurrence formulas (e.g., a specific functional form for relative subgrammar learning speeds), or (b) a systematic empirical study of when and why subgrammar learning is parallel vs. sequential across grammar families, model scales, and optimization regimes.
- **Add a control condition for curriculum learning.** Compare subgrammar pretraining against an equivalent amount of additional training on the full grammar to isolate the subgrammar-specific effect.
- **Connect the generalization experiments to the theory.** For example, measure how well the context-insensitivity assumption (Corollary 4.5) holds at increasing recursion depths, and test whether the depth-failure can be predicted from the recursive KL formula (Theorem 4.6).
- **Be more measured in claims.** Phrases like "quite definitively" for CKA results with absolute values of 0.25–0.35 overstate the strength of evidence. Similarly, the introduction's analogy to child language acquisition is undermined rather than supported by the parallel-learning finding.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Recovering Knowledge by Hardening LMs (`uOnElfFuey`) | 3.00 | R1 | Significantly weaker — fundamental methodological issues, no theoretical framework |
| Sudden Drops in the Loss: Syntax Acquisition (`MO5PiKHELW`) | 5.50 | R1 | Comparable topic (syntax acquisition dynamics) but deeper causal intervention methodology on real models; our paper is slightly weaker |
| Geometric Signatures of Compositionality (`q5lJxCXjiY`) | 5.40 | R1 | Similar tier — interesting ideas, somewhat speculative evidence; our paper is comparable |
| How transformers learn structured data (`F0Zd3knG9j`) | 5.00 | R2 | Similar setup (PCFGs, hierarchical structure, transformer learning); our paper has broader coverage but similar depth; our paper slightly stronger |
| A Causal Study on Learnability of Formal Languages (`Oz9FTPINRe`) | 5.75 | R2 | Has a novel sampling method with independent value; our paper is slightly weaker |
| Training Neural Networks as Recognizers (`aWLQTbfFgV`) | 6.25 | R2 | More rigorous and comprehensive; clearly stronger than our paper |

**Round 1 bracket:** 3.0–7.0 (clearly above the weak 3.0-tier papers, below the strong 7.0+ tier, in the 5–6 range alongside "Sudden Drops" at 5.50 and "Geometric Signatures" at 5.40).

**Round 2 narrowing:** Compared to "How transformers learn structured data" (5.00), our paper has a clearer theoretical framework and broader empirical coverage, placing it slightly above 5.0. Compared to "A Causal Study" (5.75), our paper lacks a standalone methodological contribution of comparable novelty. Compared to "Sudden Drops" (5.50), our paper's empirical investigation is less deep and less causally rigorous.

**Final score:** The paper sits between the 5.00 and 5.50 anchors. It has a genuine conceptual framework and several interesting findings, but the theoretical depth is limited, the empirical scope is narrow, and the paper spreads itself across too many questions without developing any one to convincing depth. **Score: 5.0.**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>