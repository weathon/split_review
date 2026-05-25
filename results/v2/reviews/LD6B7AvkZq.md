I've gathered sufficient calibration data. Let me now write the final consolidated review.

## Summary

The paper introduces a framework for studying how language models learn context-free grammars (CFGs) by decomposing them into "subgrammars" (inner and outer subgrammars, Definitions 3.3–3.5). The main theoretical contribution (Section 4) is a set of theorems showing that the KL divergence between a target PCFG distribution and a language model can be decomposed recursively over subgrammar structure. Empirically, the paper studies whether small transformers learn subgrammars "in parallel" (Figure 1), whether pretraining on a subgrammar improves performance (Section 5), and whether models exhibit depth-limited generalization (Section 6). The paper contains several novel definitions and an interesting experimental observation about depth vs. length generalization, but the theoretical results are mathematical identities rather than substantive insights about learning dynamics, the parallel learning claim is not properly defined or demonstrated, there is a mathematical error in a core derivation, key figures are missing, and the empirical work lacks the rigor to support the paper's strong claims.

## Strengths

1. **Novel formalization of subgrammar structure.** Definitions 3.3–3.5 (inner and outer subgrammars) and Theorem 4.1 (unique DAG decomposition) provide a clean formal vocabulary for discussing substructure in PCFGs. This framework is well-motivated by the analogy to studying monomials in polynomial learning and could be useful for future work, even if the present theorems built on it are limited.

2. **Clean depth-vs-length generalization experiment.** Figure 3 cleanly separates the effects of sequence length and recursive depth, showing that a small transformer maintains low error on long non-recursive contexts but degrades with deeper recursion, even when the next-token distribution is identical. This controlled methodology provides clear evidence about the limiting factor, confirming and extending prior results (Bhattamishra et al., 2020; Lampinen, 2024).

3. **CKA analysis provides preliminary evidence of representational effects of subgrammar pretraining.** Table 1 shows that models pretrained on a subgrammar exhibit modestly higher CKA similarity across attention layers compared to models trained from scratch, with effects that increase with longer pretraining (e.g., +21.7% for 2-layer attention on full grammar sequences with 20 epochs vs. +8.9% with 10 epochs). While preliminary, this directional evidence is suggestive and could motivate more rigorous work.

## Weaknesses

### Major

1. **Mathematical error in the illustrative KL derivation.** The transition from Equation (2) to Equation (4) in Section 4.2 replaces differences of log probabilities (log P − log Q) with ratios of logs (log P / log Q), which is mathematically incorrect. The expression shown, `(log P(α|ε)) / (log Q(α|ε))`, does not follow from the preceding lines. While this appears in a motivating example rather than in the formal theorem statements, it is a core derivation meant to build intuition for the main results, and it undermines confidence in the paper's mathematical rigor. The formal theorems (4.3, 4.6) may be correctly stated in the appendix, but this cannot be verified from the main text alone.

2. **The core empirical claim — parallel subgrammar learning — is not properly defined or demonstrated.** The paper asserts that small transformers "learn all subgrammars in parallel" based on Figure 1, which shows that subgrammar-specific KL divergences all decrease over training. However, (a) no operational definition of "parallel" vs. "sequential" learning is given; (b) no baseline is provided for what sequential learning would look like (e.g., a model that masters subgrammars one at a time); and (c) given the KL decomposition identity (Theorem 4.3), if the total KL decreases, the weighted sum of component KLs must also decrease — so the observation is close to a mathematical necessity, not an empirical discovery about learning dynamics. Corollary 4.7 (informal) is essentially a tautology: if gradients for one subgrammar do not harm others, then parallel learning occurs. This does not advance understanding.

3. **Missing Figures 5 and 6.** The paper references Figures 5 and 6 to support claims about robustness to subgrammar location and lower final loss from pretraining (Section 5.1), but these figures are absent from the manuscript. This makes it impossible to evaluate two of the paper's key empirical claims: that pretraining is robust to subgrammar position and that it can achieve lower final loss for small models.

4. **Overclaiming relative to evidence.** The paper uses language such as "fundamental theorems," "quite definitively" (for the CKA analysis), and "unraveling syntax" (title) that significantly overstate what is delivered. The CKA results (Table 1) show small absolute differences (e.g., 0.258 to 0.281 for 2-layer attention), no confidence intervals, and no significance tests. The phrase "quite definitively" is unearned. The theoretical results are mathematical identities following from the chain rule and the definitions of PCFGs and autoregressive models; they are not "fundamental" in the sense of revealing new properties of learning dynamics.

5. **No empirical comparison with closely related prior work.** The paper cites Cagnetta & Wyart (2024) and Allen-Zhu & Li (2023) as studying how neural networks learn CFGs, but does not benchmark against them or explain what the present framework reveals that theirs does not. Given that these works also study learning dynamics and representational structure in PCFGs, the absence of any comparison (even conceptual or through shared grammars) makes it difficult to assess the incremental contribution.

### Minor

6. **Theoretical results are straightforward consequences of definitions.** Theorems 4.3 and 4.6 restate the chain rule of probability grouped by subgrammar structure. They are correct but do not constitute a substantive theoretical result about learning — they say nothing about optimization, sample complexity, or why models succeed or fail. The paper frames them as "fundamental recurrences," but they are closer to bookkeeping identities. The connection of Theorem 4.6 to PCFG consistency is also standard. This framing needs to be recalibrated.

7. **Definition 4.2 of the restricted KL divergence is convoluted and uses undefined notation** (e.g., `D_KL(P||Q | ¬s)`). This makes the key technical definition difficult to parse, which is a barrier to evaluating the theory.

8. **The GPT-5.1 anecdote (Section 6) adds little value.** While correctly caveated as informal, the 5-example test on GPT-5.1 is too thin to support any conclusion and should be removed or replaced with a systematic evaluation. The controlled experiments in Section 6 are already sufficient.

9. **Experimental reproducibility details are sparse.** The architecture, hyperparameters, data generation procedure, and KL computation method for subgrammars are not specified in the main text. While the appendix (which is not available in this version) may contain some of these, the main text should be more self-contained.

### Trivial

- Theorem numbers are sometimes inconsistent (e.g., "Theorem 4.2" appears where "Theorem 4.3" is likely intended).
- The description of Figure 1 in the caption and floating text overlap with substantial repetition.
- "different Transformers" in Table 1 caption is a grammatical error ("different Transformers" → "different transformers").

## Nice-to-Haves

- The parallel learning claim would be strengthened by a quantitative measure that distinguishes parallel from sequential (e.g., comparing the rates of KL decrease across subgrammars, or testing whether the ordering of convergence is consistent across random seeds).
- Error bars or confidence intervals on the CKA results (Table 1) would greatly improve interpretability.
- A comparison of the subgrammar pretraining effect against other forms of inductive bias (e.g., different pretraining tasks, curated curricula) would help isolate whether the effect is specific to subgrammar structure.
- The paper could explicitly acknowledge that the KL decomposition is an identity following from the chain rule, and then pivot more cleanly to the empirical conditions under which subgrammar structure matters for learning.

## Removed Points

- **Criticism about questioning existence/release of cited models (GPT-5.1, Pythia, etc.):** Removed per hard rules — if the paper cites a model, it is assumed to exist.
- **"The paper lacks sufficient experimental detail to be reproducible" from the Harsh Critic:** This is partially valid but was raised at a general level. The specific missing details (architecture, hyperparameters) are kept as Minor weakness 9. The broader framing was removed as it was not specific enough.
- **"Child language acquisition comparison is asserted without any developmental data":** The paper does not claim to provide developmental data — it frames the comparison as suggestive. Removed as the criticism demands content outside the paper's scope.
- **"The unique decomposition Theorem 4.1 is standard CFG theory":** The paper acknowledges the connection to Gruska (1971) and does not claim the decomposition itself is novel — it claims the formulation in terms of language model learning is novel. The criticism overstates the issue.
- **"Corollary 4.7 is a tautology":** This is kept in Major weakness 2 (the parallel learning claim), not as a separate point.
- **Strength about "rigorous evaluation" in the depth generalization experiment:** The original Strength Finder claimed "rigorous evaluation with rigorous evaluation" — the writing was garbled. The experiment is well-controlled but uses a single metric; downgraded to a standard strength.
- **Strength about "parallel subgrammar learning as a new research direction":** This conflicts with retained weaknesses 2 and is a framing/aspiration, not a demonstrated result. Removed.

## Novel Insights

Beyond the paper's own contributions, the reviews surface two observations worth noting: (1) There is a recurring pattern in this subfield (CFG learning in transformers) where papers present mathematical identities as theoretical discoveries and then claim empirical findings from small-toy experiments that are not properly baselined. The current paper is a case study in this pattern. (2) The clean depth-vs-length control in Figure 3 is methodologically stronger than many studies in this area and could serve as a template for future work — but it confirms existing results rather than breaking new ground.

## Suggestions

- Remove or substantially rewrite the parallel learning claim: provide an operational definition, a baseline, and a quantitative measure, or else acknowledge that the observation is a direct consequence of the KL decomposition.
- Fix the mathematical error in Equation (4) or replace the entire illustrative derivation with a correct one.
- Provide confidence intervals and significance tests for the CKA results.
- Replace the GPT-5.1 anecdote with a systematic evaluation or remove it entirely.
- Recalibrate the framing: the paper contributions are (a) a novel formalization of subgrammar structure and (b) preliminary empirical observations about how subgrammar structure interacts with learning. The language of "fundamental theorems" and "quite definitively" should be scaled back to match the evidence.
- Add a table with experimental hyperparameters (architecture, learning rate, batch size, training epochs, data generation details) to improve reproducibility.
- Clarify Definition 4.2 with a concrete example and explicit notation.
- Compare to Cagnetta & Wyart (2024) and Allen-Zhu & Li (2023) more substantively, either by evaluating on shared grammars or by discussing what the subgrammar lens reveals that their analyses do not.

## Anchors Used for Calibration

| Path | Avg Score | Round/Query | Comparison |
|------|-----------|-------------|-----------|
| uOnElfFuey | 3.00 | R1-topic-low | Weaker paper (recovering knowledge from hardened LMs); current paper is more novel |
| 4y3GDTFv70 | 3.25 | R1-topic-low | Latent space theory paper; comparable in rigor but different topic |
| 0pLCDJVVRD | 7.00 | R1-topic-mid | *A Percolation Model of Emergence* — much stronger: rigorous theoretical model, multiple seeds, clear empirical claims. Current paper is ~3 points weaker |
| MO5PiKHELW | 5.50 | R1-topic-mid | *Sudden Drops in the Loss* — more rigorous experimental work with causal interventions; current paper is ~1.5 points weaker |
| q5lJxCXjiY | 5.40 | R1-topic-mid | *Geometric Signatures of Compositionality* — rejected, overclaiming from limited evidence similar to current paper; current paper is ~1 point weaker |
| aMBSY2ebPw | 7.33 | R1-topic-mid | Grammar book translation — stronger empirical work, different topic |
| f4gF6AIHRy | 8.00 | R1-topic-high | Top-tier papers; current paper not in same league |
| F0Zd3knG9j | 5.00 | R2-hierarchical-filtering | *How transformers learn structured data* — rejected, limited novelty but more rigorous; current paper slightly weaker |
| hFQZmKFtlT | 3.50 | R2-memorization | *Rethinking Memorization in LLMs* — very weak, re-labeled overfitting; current paper is somewhat stronger |
| fp77Ln5Hcc | 4.50 | R2-depth-extrapolation | *Depth Extrapolation* — rejected, similar topic but more theoretical substance; current paper comparable or slightly weaker |
| eRkNNQRppH | 3.50 | R2-FOL-dynamics | *(Pre-)training Dynamics: FOL* — very weak, vague claims; current paper is stronger |
| CIcMuee69B | 4.40 | R3-automata-LLM | Only tangentially related |

**Round 1 bracket:** Based on R1 queries, the plausible range was 3.5–5.5. The weak-band papers (3.0–3.25) were clearly lower quality than the current paper, while the strong-band papers (7.0–8.0) were far superior. The mid-band papers included both the "Percolation" paper (7.0, much stronger) and the "Geometric Signatures" paper (5.4, somewhat stronger but with similar overclaiming issues). This suggested a range of 3.5–5.0.

**Round 2 narrowing:** The R2 queries pulled more topically relevant anchors. "How transformers learn structured data" (5.0, rejected) is more rigorous in its experiments but similarly limited in novelty; the current paper has more novel definitions but is less rigorous. "Depth Extrapolation" (4.5, rejected) has a clearer theoretical contribution but is about a narrower problem. "(Pre-)training Dynamics: FOL" (3.5, rejected) is clearly weaker. The comparison shows the current paper shares the overclaiming pattern of the 5.0–5.4 rejected papers but has additional concrete issues (mathematical error, missing figures, underspecified experiments) that place it below them.

**What the low-band anchors failed at:** Papers scoring 3.0–4.0 typically had vague or unsubstantiated claims, trivial theoretical contributions, experiments that did not support the conclusions, or fundamental framing issues. The current paper shares the "trivial theoretical contribution" and "overclaiming" failure modes but has somewhat more coherent definitions and one clean experiment (depth generalization). However, the mathematical error and missing figures are additional liabilities.

**Final score: 4.0** — The paper has genuinely novel definitions (subgrammar framework) and one well-controlled experiment (depth vs. length), but the theoretical centerpiece is a mathematical identity, the central empirical claim (parallel learning) is underspecified and undemonstrated, there is a mathematical error in a core derivation, key figures are missing, and the paper systematically overstates what it has accomplished.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>