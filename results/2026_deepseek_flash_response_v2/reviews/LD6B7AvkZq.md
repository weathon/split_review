## Summary

This paper studies how small autoregressive transformers learn probabilistic context-free grammars (PCFGs), focusing on the subgrammar decomposition of CFGs. The authors define inner and outer subgrammars, derive a decomposition of the KL-divergence (equivalently, the language modeling loss) into subgrammar-specific terms, and present empirical observations on parallel learning dynamics, subgrammar pretraining benefits, and depth generalization difficulty. The core conceptual contribution—that CFG structure induces a natural decomposition of the loss—is interesting and understudied, but the execution has significant problems.

## Strengths

1. **Clean subgrammar definitions (inner/outer, Definitions 3.3–3.5).** The formalization of CFG substructure into precise mathematical definitions is a useful conceptual contribution. The distinction between inner subgrammars (subtrees of derivations) and outer subgrammars (simplified versions of the full language) is well-motivated and provides a vocabulary for studying hierarchical structure learning.

2. **Theorem 4.6 (KL-divergence with expected recursion).** This theorem gives a closed-form expression \(D_{\text{KL}} = \frac{\sum_i p_i D_{\text{KL}}(P_{A_i} \parallel Q_\theta(A_i))}{1 - \mathbb{E}[R]}\), predicting that the KL divergence blows up as the expected recursion approaches 1. This is crisp and testable—it goes beyond prior CFG-learning work (Cagnetta & Wyart, 2024; Allen-Zhu & Li, 2023) by connecting a grammar's recursion probability to model error in a specific functional form.

3. **Clean separation of depth difficulty from length difficulty (Figure 3).** The paper designs two controlled conditions (flat context \((a)^i\) vs. recursive context \((^i\)) that isolate recursive depth from sequence length. The model achieves 0.017 error at depth 200 in the flat condition but 0.173 at the same depth in the recursive condition. This cleanly disentangles two phenomena that are often confounded in prior work on neural network generalization with recursive structures.

## Weaknesses

### Major

1. **Mathematical derivation error in the main text (Equation 4, lines 124–130).** The paper's central derivation—supposed to show that the KL-divergence decomposes over subgrammars—contains a critical error. Equation (2)–(3) correctly decomposes log-probabilities into additive terms via the chain rule. But Equation (4) presents *ratios* of log-probabilities (\(\log P_G / \log Q_\theta\)) instead of *differences* (\(\log P_G - \log Q_\theta\)), which is the correct form for a KL expansion. KL divergence involves \(P(s) \cdot \log(P(s)/Q(s))\); the decomposition should yield differences of log-terms weighted by probabilities, not ratios of logs. As presented, Equation (4) does not follow from the preceding equations, and the text's claim that "the KL-divergence evaluates to a sum of conditioned KL-divergences" is not supported by the equations shown. The full proof is deferred to Appendix A (which is stripped), so the reader cannot verify whether a correct derivation exists. This is not a formatting artifact—the structural error (ratio vs. difference) makes the derivation incoherent as displayed. For a paper whose main theoretical contribution hinges on this derivation, this is a significant problem.

2. **Corollary 4.7 (parallel learning) is circular.** The "corollary" states that if gradient updates on one subgrammar do not hurt performance on other subgrammars, then the model learns subgrammars in parallel. This is a tautology: non-interference *means* parallel learning by definition. It adds no insight into *why* or *under what conditions* transformers learn subgrammars in parallel—which is the genuinely interesting empirical finding. The paper itself acknowledges this indirectly (line 214: "Future work can aim to weaken the assumptions"), but presenting it as a "corollary" inflates its substance.

3. **Thin empirical evaluation relative to the scope of claims.** The paper claims to study how "language models" acquire syntax but tests only one architecture family (2-layer and 4-layer transformers). No comparison to RNNs, LSTMs, or other architectures is provided, despite these being standard baselines in formal language learning (Avcu et al., 2017; Suzgun et al., 2018), and despite the fact that the paper's own Section 6 shows transformers struggle with recursive depth—a result that would be more informative with a cross-architecture comparison. Additionally, the CKA analysis (Table 1) reports only mean values across 30 seeds with no standard deviations, confidence intervals, or statistical tests. The reported differences are small (e.g., 0.258 vs. 0.281, a 0.023 difference labeled "+8.9%") and could fall within the noise. Without variance estimates, the reader cannot assess the robustness of these claims.

### Minor

1. **Context-insensitivity assumption (Corollary 4.5) is strong and only partially validated.** The assumption that \(Q_\theta\)'s conditional distribution over subgrammar strings is identical regardless of context is the linchpin for simplifying the decomposition to weighted KL divergences. The paper acknowledges this is a strong assumption and provides some empirical justification ("varying the prefix did not result in qualitatively different results," line 200), but this justification is qualitative rather than quantitative. A formal measurement of how much the condition is violated across different subgrammars and training stages would be needed to assess how reasonable this assumption is.

2. **Theorem 4.3's decomposition is partially definitional.** The restricted KL \(D_{\text{KL}}(P_G \| Q)_A\) (Definition 4.2) is constructed as "the portion of the KL-divergence attributable to subgrammar A," so the fact that the total KL equals the sum of these restricted terms follows largely from the construction. The contribution is in recognizing that this decomposition maps naturally onto CFG structure, not in proving a non-trivial identity about how neural networks learn.

3. **Theorem numbering inconsistency.** The paper refers to both "Theorem 4.2" and "Theorem 4.3" for what appears to be the same result (line 156 references "Theorem 4.2 and Corollary 4.4," while the theorem statement itself is labeled 4.3 and appears on line 146). This is confusing.

### Trivial

None.

## Nice-to-Haves

- Compare to other architectures (RNNs, LSTMs) to test whether parallel subgrammar learning is specific to transformers.
- Add error bars or confidence intervals to the CKA analysis.
- Provide a quantitative measure of context-insensitivity violation (e.g., the KL divergence between \(Q_\theta(\cdot \mid \text{context}_1)\) and \(Q_\theta(\cdot \mid \text{context}_2)\) across different contexts for the same subgrammar).
- Clarify whether the recursion probability formula in Theorem 4.6 applies to all self-looping grammars or only to a specific subclass.

## Removed Points

These points were flagged by the inputs but filtered out. Treat them with caution—some may still be worth checking.

- *"Theorem 4.3 is just the chain rule"* (Harsh Critic) — REMOVED because the decomposition into subgrammar-specific terms is a non-trivial mapping of CFG structure onto loss terms, even if the main-text derivation is flawed.
- *"Context-insensitivity assumption is circular"* (Harsh Critic) — REMOVED because a strong assumption is not the same as a circular one; the paper acknowledges the assumption is strong and provides some empirical validation.
- *"Missing CFG definitions from main text"* (Harsh Critic) — REMOVED because grammar definitions are in the appendix which was stripped by the parser; this is a parser artifact.
- *"Depth difficulty replicates known findings without novelty"* (Harsh Critic) — REMOVED because the paper's cleaner separation of depth vs. length (Figure 3) goes beyond prior work.
- *"No standard metrics reported"* (Harsh Critic) — WEAKENED/REMOVED because KL-divergence is directly linked to cross-entropy loss (Proposition 3.9) and is a standard metric for distribution matching.
- *"GPT-5.1 anecdotal experiment is objectionable"* (Harsh Critic) — REMOVED because the paper explicitly calls this "purely anecdotal."
- *"Theorem 4.3 is genuinely novel and prior work does not establish any such decomposition"* (Strength Finder) — WEAKENED to reflect that the contribution is more about recognizing the decomposition exists than proving a non-trivial identity.
- *"Empirical validation of the decomposition (Figure 1)"* (Strength Finder) — WEAKENED because if the restricted KL is defined as the portion of total KL, the sum equaling the total is partially definitional.

## Novel Insights

None beyond the paper's own contributions. The calibration search revealed that the paper's core approach—studying learning dynamics through subgrammar decomposition of PCFGs—is a genuinely underexplored direction, and the empirical observation that small transformers learn subgrammars in parallel (rather than sequentially) is worth deeper investigation. However, the paper's own theoretical framing (the "fundamental theorems") and the mathematical derivation meant to support it are the weakest parts of the submission.

## Suggestions

1. **Fix the mathematical derivation in Section 4.2.** Equation (4) must show differences of log-probabilities weighted by probabilities, not ratios of logs. If the full proof in Appendix A is correct, bring the key steps into the main text so the reader can follow the argument.
2. **Either remove Corollary 4.7 or reframe it honestly** as an observation/definition rather than a substantive theoretical result. The parallel learning finding is the paper's most interesting empirical result—discuss it empirically and leave the "theorem" framing for a result that actually adds analytical leverage.
3. **Add statistical rigor to the CKA analysis.** Report standard deviations or confidence intervals across the 30 seeds. If the effects are statistically significant, this should be demonstrated; if not, the claims about "definitive" representational alignment should be tempered.
4. **Include at least one comparison architecture** (e.g., LSTM) to test whether the findings are specific to transformers.

## Score and Decision

Calibration anchors:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| uOnElfFuey.md (Recovering Knowledge by Hardening LMs) | 3.00 | R1 | Clearly weaker—narrower scope (regular languages only), flawed methodology, fewer insights |
| F0Zd3knG9j.md (How transformers learn structured data) | 5.00 | R2 | Comparable—both study hierarchical structure learning; that paper has cleaner experiments but less ambitious theory |
| fp77Ln5Hcc.md (Depth Extrapolation of Decoders) | 4.50 | R2 | Slightly weaker—our paper has broader scope (subgrammars vs. just depth) |
| Oz9FTPINRe.md (Causal Study on Learnability) | 5.75 | R1/R2 | Stronger—methodologically more rigorous, cleaner framing |
| aWLQTbfFgV.md (Training NNs as Recognizers) | 6.25 | R1/R2 | Clearly stronger—multi-architecture comparison, statistical rigor, clean framing |

Round 1 bracket: 3.0–6.25. Round 2 narrowed to ~4.0–5.5. The paper is comparable to the 5.00 hierarchical filtering paper but has more significant flaws (mathematical error in the main derivation, circular corollary, missing architecture comparisons and error bars). It is stronger than the 4.50 depth extrapolation paper (broader scope, more readable) and clearly weaker than the 5.75+ anchors. Score: 4.5.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>