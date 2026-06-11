Now I have sufficient calibration data to finalize. Let me write the complete final review.

## Summary

The paper introduces a formal framework for analyzing how language models learn context-free grammars by decomposing the grammar into "inner" and "outer" subgrammars. It proves that language modeling KL divergence obeys a recursive decomposition over subgrammar structure (Theorems 4.3, 4.6), with expected recursion controlling a multiplicative blow-up factor. Empirically, the paper shows that small transformers learn subgrammars in parallel (not sequentially), that subgrammar pretraining yields internal representations better aligned with grammar structure (CKA analysis, Table 1), and that recursive depth—not sequence length—is the primary failure mode for these models (Figure 3).

## Strengths

1. **Novel subgrammar framework (Definitions 3.3, 3.5):** The paper formalizes "inner" and "outer" subgrammars of PCFGs, providing a clean vocabulary for analyzing how language model learning interacts with grammatical substructure. These definitions are the paper's most solid conceptual contribution and are well-motivated, with appropriate connections to classical work (Gruska, 1971).

2. **Formal KL-divergence recurrence over subgrammar structure (Theorems 4.3, 4.6):** The paper proves that the language modeling loss for a PCFG decomposes into subgrammar-specific KL divergences and provides a closed-form recurrence (Theorem 4.6) showing how expected recursion creates a multiplicative "blow-up" factor 1/(1−E[R]). This is a genuinely new formal connection between CFG substructure and the language modeling objective — prior work studied static representations or final trained behavior, not learning dynamics through the lens of subgrammar decomposition.

3. **Clean separation of depth difficulty from length difficulty (Section 6, Figure 3):** The experimental design isolates recursive depth from sequence length: flat extensions `(a)^i` (error stays below 0.05) vs. deep recursive contexts `(^i` (error rises to 0.173 at depth 200). Because the ground-truth next-token distribution is identical in both cases, this directly pinpoints recursive depth as the specific failure mode, not length or distributional mismatch. This is cleaner than most prior work on recursive generalization (Bhattamishra et al., 2020; Lampinen, 2024).

4. **CKA-based evidence for representational alignment (Section 5.2, Table 1):** Using Centered Kernel Alignment across 30 random seeds, the paper shows that subgrammar-pretrained models exhibit quantifiably higher representational alignment (e.g., from 0.258 to 0.303, +21.7% for 2-layer attention after 20 epochs of pretraining), providing mechanistic evidence beyond loss curves that pretraining induces representations respecting the grammar's compositional structure.

5. **Empirical finding that small transformers learn subgrammars in parallel (Figures 1, 2):** The paper demonstrates that all subgrammar losses decrease simultaneously during training, contrasting with child language acquisition patterns — a non-obvious empirical observation worth documenting.

6. **Robustness control for subgrammar position (Section 5.1):** The paper tests whether pretraining benefits depend on subgrammar position (prefix, suffix, infix) and finds the effect is robust — a methodologically sound control that strengthens the claim the effect operates at the representational level rather than surface positional memorization.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Weakness of Corollary 4.7 (parallel learning condition):** Corollary 4.7 states that if gradient updates on one subgrammar do not increase loss on others, then models learn all subgrammars in parallel. This is a valid but nearly content-free sufficient condition — it essentially restates the definition of "no interference" without providing insight into *when or why* the condition would actually hold for transformers trained by gradient descent. The paper itself acknowledges this is an open direction, but presenting it as a numbered corollary in the main text overstates its weight. It would be better framed as a remark or observation.

2. **Incomplete experimental details:** The paper does not report basic training hyperparameters (learning rate, optimizer, batch size, number of training steps, vocabulary size, sequence length distribution, train/test split) and gives only minimal architecture information ("2-layer, 2-head transformer" without specifying hidden dimension, embedding size, or activation function). While some of these details may reside in the (stripped) appendix, the main text should be self-contained enough for a reader to understand what was done.

3. **No variance estimates in Table 1:** CKA values in Table 1 are averages across 30 seeds without standard deviations or confidence intervals. The percentage changes (e.g., +8.9%, +21.7%) cannot be assessed for statistical significance, which is especially important since the absolute CKA differences are small (e.g., 0.258 vs. 0.281). The paper notes that the analysis was "much to our surprise," making variance information important for interpretation.

4. **Definition 4.2 uses undefined notation:** The definition `D_KL(P_G || Q)_A = Σ_s P(s|ε) P_G(A|s) Σ_a D_KL(P_G || Q | ¬s)` uses `P_G(A | s)` (probability of subgrammar A given context s — intuitive but not formally defined over the probability space on strings) and `D_KL(P_G || Q | ¬s)` where "¬s" is not standard conditioning notation. While the intended meaning is clear from context, the definition is not formally precise, which undermines the theoretical development that builds on it.

5. **Overclaimed language in abstract and introduction:** Phrases like "prove a suite of fundamental results" and "use alignment analysis to show definitively" are stronger than what the evidence supports. The theoretical results are interesting but build on informal notation (Definition 4.2), and the CKA numbers show moderate effects without variance bounds. The experiments should speak for themselves without needing to pre-claim their definitiveness.

6. **No explicit comparison with prior depth generalization results:** Section 6's finding that transformers fail at recursive depth is consistent with Bhattamishra et al. (2020) and Lampinen (2024), which the paper cites but does not discuss *how* its results compare to or extend these prior findings. The paper's contribution here is the cleaner experimental control (same next-token distribution for depth vs. length), but this point could be made more explicit.

7. **Anecdotal GPT-5.1 evidence works against the paper's thesis:** The footnote about GPT-5.1 Thinking solving all deep recursion examples undercuts rather than supports the claim that deep recursion is a fundamental limitation — it shows that a sufficiently capable model *can* handle depth. The paper appropriately caveats this as anecdotal, but including a counterexample to one's own thesis without commentary weakens the narrative.

### Trivial

1. Equation (4) on line 130 appears garbled (showing `log P / log Q` ratio form rather than the standard `P log(P/Q)` form of KL divergence). This is likely a PDF extraction artifact, but should be checked against the original submission.

## Nice-to-Haves
- Adding variance bars or confidence intervals to Table 1 would make the CKA results more interpretable.
- Including an ablation comparing subgrammar pretraining against simpler pretraining strategies (e.g., pretraining on random sequence subsets or simpler non-grammatical sequences) would clarify whether the benefit is specific to subgrammar structure or any form of easier pretraining.
- Providing full training hyperparameters and model architecture details (hidden dimension, embedding size, learning rate, optimizer, batch size) would improve reproducibility.
- A discussion connecting the depth generalization results to the specific findings of Bhattamishra et al. (2020) or Lampinen (2024) would help position the contribution.

## Removed Points

**Weaknesses removed with justification:**
1. "Equation (4) is fundamentally flawed / the math derivation is incorrect" — The garbled equation (ratio of logs) is likely a PDF extraction artifact. The paper's conceptual claim about KL decomposing over subgrammars is clearly stated in prose, and the garbled equation does not propagate to Theorem 4.3/4.6. Removed per formatting-artifact instructions.
2. "Empirical evaluation is too thin to support breadth of claims" / "Figures 5, 6 and Table 3 are referenced but not shown" — Missing figure/table references are parser artifacts (images stripped during extraction). The paper clearly conducted these experiments.
3. "Grammar definitions are entirely in the appendix" — Standard practice for papers of this type; the main text defines the key concepts (Def 3.3, 3.5) and references the appendix for specifics.
4. "Corollary 4.7 is vacuous / a tautology" — Demoted from the harsh critic's framing to Minor #1. The corollary is weak but not vacuous — it is a valid sufficient condition, albeit a shallow one that the paper itself identifies as needing future work.
5. "The paper lacks comparison with existing work on learning formal languages" — The paper does cite and discuss Bhattamishra et al. (2020), Suzgun et al. (2018), Cagnetta & Wyart (2024), and Allen-Zhu & Li (2023) in Section 2. The comparison could be deeper (kept as Minor #6), but the accusation that it is absent is incorrect.

**Strengths removed with justification:**
- None removed.

## Novel Insights
The harsh critic's observation that the paper's strongest empirical contribution is the depth-vs-length separation (Section 6) — not the subgrammar decomposition experiments — is worth emphasizing, as it is the cleanest and most interpretable experiment in the paper. The strength finder's identification that the CKA analysis provides representation-level evidence (not just loss curves) is a useful framing that the paper could lean into more explicitly. Both reviewers' inputs agree that the subgrammar definitions (Section 3) are the paper's most solid conceptual contribution, while the mathematical development in Section 4.2 is the weakest part — the informal notation and garbled presentation prevent the theoretical framework from being as impactful as it could be. The key tension in the paper is between genuinely novel conceptual ideas (subgrammar decomposition, clean depth experiment) and execution-level issues (informal notation, incomplete experimental reporting) that prevent those ideas from landing with full force.

## Suggestions
1. Clean up Section 4.2: replace the informal notation in Definition 4.2 (drop `¬s`, explicitly define what conditioning means), ensure equations use standard KL divergence forms throughout.
2. Add variance estimates (standard deviations or confidence intervals) to Table 1.
3. Report training hyperparameters (learning rate, optimizer, batch size, hidden dimension, embedding size) either in the main text or a clearly referenced appendix section.
4. Reframe Corollary 4.7 as a remark or observation rather than a numbered corollary, to avoid overstating its contribution.
5. Add a sentence or two explicitly comparing Section 6's depth generalization findings to Bhattamishra et al. (2020) and Lampinen (2024), highlighting the cleaner experimental control as the differentiating factor.
6. Tone down language in the abstract: replace "prove a suite of fundamental results" with "prove theoretical results" and "show definitively" with "provide evidence that."

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>