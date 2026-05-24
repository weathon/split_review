Here is my consolidated final review.

## Summary

This paper introduces formal definitions of *inner* and *outer* subgrammars for PCFGs and proves that the KL divergence between the true PCFG distribution and an autoregressive language model decomposes recursively over these subgrammars (Theorem 4.3). It then presents experimental evidence that small transformers learn all subgrammars in parallel, explores whether subgrammar-based pretraining helps, and studies how models fail on deep recursive structures. The paper opens a new direction of studying language model learning dynamics through the lens of grammar substructure.

## Strengths

- **Clean formalization of subgrammar structure.** Definitions 3.3 (inner subgrammar) and 3.5 (outer subgrammar) give precise, composable notions of grammatical substructure. Theorem 4.1 (unique decomposition into a DAG of inner subgrammars) provides a canonical decomposition that the rest of the paper builds on. This is a genuinely useful conceptual contribution.

- **KL divergence decomposition over subgrammar structure (Theorem 4.3, Corollary 4.4).** The paper proves that the KL divergence of an LM from a PCFG decomposes as a sum over top-level subgrammars plus fixed terminal strings. While the derivation follows from the autoregressive factorization, the connection to grammar substructure is novel and provides a formal language for discussing how error breaks down across grammatical components.

- **Controlled depth-vs-length experiments (Figure 3).** The paper cleanly demonstrates that transformers fail on deep recursive contexts (error rising to 0.173 at depth 200) while handling long non-recursive contexts nearly perfectly (error < 0.05). This controlled comparison, even on a single grammar, isolates the difficulty of depth from sequence length — a clear and well-designed experiment.

- **Honest discussion of limitations.** The paper explicitly acknowledges several weaknesses: that the parallel learning condition is insufficiently explored (Section 7), that the difficulty of depth is not novel (citing prior work), and that the GPT-5.1 test is purely anecdotal. This candor improves the paper's credibility.

## Weaknesses

### Fatal
None.

### Major

1. **KL decomposition claimed but not quantitatively verified.** The paper states that Figure 1 shows "the KL divergence (loss) is the sum over the corresponding loss for each subgrammar" and that "scaling the divergences by their probabilities give a perfect decomposition." However, the actual sum of subgrammar divergences is never computed, plotted, or compared to the total KL divergence. Without this check, the central empirical claim of Theorem 4.3 is unverified. The paper should report the numerical sum and compare it to the total KL with error bars.

2. **Curriculum learning experiments lack a critical control.** The paper reports that subgrammar pretraining can lower final loss for small models (Section 5.2), but does not compare against pretraining on an equally sized *random* subset of the grammar's data (matched for token count). Without this control, the claimed benefit cannot be attributed to the subgrammar *structure* rather than simply to more training data or a warm-start effect. This undermines the paper's strongest practical claim.

3. **"Parallel learning" observation is based on visual inspection alone.** The claim that models "learn all subgrammars in parallel" (Section 4.2) is supported only by the visual observation that all KL curves decrease simultaneously. No quantitative metric of parallelism is provided, no baseline (e.g., a scenario where sequential learning would be expected) is constructed, and the theoretical condition for parallel learning (Corollary 4.7) is stated informally and is essentially a tautology ("if gradient updates do not interfere, then learning is parallel"). The paper itself acknowledges this is "insufficiently explored," but the prominence of the claim in the abstract and introduction overstates the evidence.

### Minor

4. **Equation (1)–(4) derivation is garbled.** Equation (4) appears to divide log probabilities rather than summing KL terms, making the derivation unreliable as written. The paper acknowledges this is "in an abuse of notation," but the exposition is confusing. The main theorem (4.3) is stated clearly afterward, so this does not invalidate the theoretical result, but it harms readability.

5. **Definition 4.2 is unclear.** The notation "¬s" and the overall expression for \(D_{\text{KL}}(P_G \parallel Q)_A\) are not well-defined. The definition is important for the theorem statements but is hard to parse.

6. **Context insensitivity (Corollary 4.5) is asserted but not quantitatively tested.** The paper claims "varying the prefix did not result in qualitatively different results, suggesting these models are largely context-insensitive," but provides no quantitative test (e.g., measuring how much the next-token distribution for a subgrammar varies across different valid contexts). This is a strong assumption underlying the simplified decomposition.

7. **Key Table 3 is deferred to the appendix.** The claim that pretrained models better segregate subgrammar vs. non-subgrammar sequences is referenced to Table 3, which is not in the main text. Given that this table is central to the CKA analysis conclusions, its absence weakens the claim.

8. **Generalization experiments are limited to one grammar.** The depth-vs-length study (Section 6) uses only the nested parentheses grammar. While the result is clear, generalizability to other grammars is unknown.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- For the curriculum learning experiments, comparing against a sequential learning baseline (e.g., train on subgrammar until convergence, then train on full grammar) would help contextualize the "parallel learning" phenomenon.
- The paper could benefit from t-SNE/UMAP visualizations of hidden states to complement the CKA analysis.
- A quantitative measure of context insensitivity (e.g., variance of next-token distributions across contexts) would strengthen Corollary 4.5.

## Removed Points

- **"The theoretical core is mathematically shallow and provides no meaningful new understanding"** — This is an opinion, not a verifiable weakness. The decomposition connecting grammar substructure to LM loss is a novel contribution, even if the mathematics is straightforward.
- **"Figure 5 not in main text"** — The parser strips figures; the original paper includes them.
- **"Missing related works"** — Per instructions, I cannot verify claims about missing citations.
- **"Overstating contributions"** — The paper is actually quite measured in its claims and explicitly acknowledges limitations. The abstract uses "fundamental" and "definitively" which are somewhat strong but not unreasonable for a first-results paper.
- **"Grammar definitions are not provided"** — The paper states grammar definitions are in the appendix, which was stripped by the parser.
- **"The difficulty of depth is not a new finding"** — The paper itself cites Bhattamishra et al. (2020) and Lampinen (2024) for this, and frames the experiment as a probe, not a discovery. The controlled depth-vs-length comparison still has value as a clean demonstration.

## Novel Insights

The two reviews largely converge on the paper's strengths and weaknesses. The key insight that emerges from reading both reviews together is that the paper's most valuable contribution is its *framework* (the subgrammar definitions and KL decomposition) rather than its experimental findings. The experiments are best viewed as illustrative demonstrations of what the framework enables, not as definitive empirical discoveries. The harsh critic correctly identifies that the experimental validation is incomplete, but the strength finder correctly identifies that the formal framework is novel and well-motivated. The paper would be significantly strengthened by treating the experiments as preliminary case studies and focusing the contribution on the framework itself.

## Suggestions

1. **Quantitatively verify the KL decomposition** by computing the sum of subgrammar KL divergences and comparing to the total KL, with error bars. This is the single most important addition.
2. **Add a control for the curriculum learning experiments:** compare subgrammar pretraining against pretraining on a matched random subset of the data.
3. **Provide a quantitative measure of parallelism** (e.g., relative loss reduction per epoch per subgrammar) and a baseline scenario where sequential learning would be expected.
4. **Clean up the derivation in equations (1)–(4)** and clarify Definition 4.2.
5. **Move the key representation analysis results (Table 3) to the main text** or provide a clear summary of the findings.
6. **Add a quantitative test of context insensitivity** to support the claim in Corollary 4.5.

## Score and Decision

**Calibration anchors (all from the batch):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| STUGfUz8ob.md — "When can transformers reason with abstract symbols?" | 7.60 | Significantly stronger theoretical contributions with rigorous proofs; our paper has weaker theory |
| n2NidsYDop.md — "Transformers Provably Solve Parity Efficiently with CoT" | 8.67 | Much more rigorous theoretical analysis; our paper is less mathematically deep |
| oYjPk8mqAV.md — "Magnushammer: premise selection" | 8.00 | Unrelated topic but stronger empirical validation; our paper lacks comparable rigor |
| yEox25xAED.md — "Grammar Reinforcement Learning" | 6.60 | Similar topic (CFG + transformer), similar scope. That paper has a clearer applied contribution, ours has a cleaner theoretical framework but weaker experiments |
| F0Zd3knG9j.md — "How transformers learn structured data" | 5.00 | Most similar topic. Both study transformers learning from PCFG-structured data. Our paper has stronger theoretical framing but shares similar weaknesses in limited experimental scope and synthetic settings |
| kpnW12Lm9p.md — "Circuit Transformer" | 6.67 | Unrelated topic but similar level of theoretical formality with stronger experimental validation |
| u859gX7ADC.md — "Recursive composition augmented Transformer" | 6.25 | More applied but with stronger empirical evaluation |
| uOnElfFuey.md — "Recovering Knowledge by Hardening Language Models" | 3.00 | Fundamentally weaker paper with methodology issues; our paper is stronger in both theory and experimental design |
| HYsU5X4kE5.md — "GCNFT" | 3.00 | Unrelated topic, much weaker paper |
| NSBP7HzA5Z.md — "Inductive Transformers" | 3.00 | Vague claims with no rigorous support; our paper is substantially stronger |
| zUDbPgskDS.md — "Crystals with Transformers" | 3.25 | Unrelated topic |

The paper defines a clean framework for studying how LMs learn CFG substructure, which is a novel and worthwhile direction. However, the experimental validation is incomplete in several respects (KL decomposition not quantitatively verified, parallel learning claim visually based, curriculum learning lacks controls), and the theoretical results are relatively straightforward consequences of the definitions. The paper is comparable in quality to F0Zd3knG9j (5.00, Reject) and weaker than yEox25xAED (6.60, Accept) — it has a more principled framework than the former but less rigorous empirical support than the latter.

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**