Now I have a thorough understanding of the paper and the calibration landscape. Let me synthesize the final review.

---

## Summary

This paper introduces a framework for analyzing how transformers learn probabilistic context-free grammars (PCFGs) through the lens of subgrammar structure. The core theoretical contribution is a suite of theorems proving that the KL-divergence loss of a language model trained on a PCFG decomposes additively over the grammar's subgrammars — a recurrence relation that holds recursively through the grammar's hierarchical DAG structure. The paper validates this decomposition empirically on small transformers trained on synthetic CFGs (Figures 1, 2), explores whether pretraining on subgrammars induces better internal representations (via CKA analysis), and demonstrates that recursion depth — not sequence length — is the primary obstacle to generalization (Figure 3).

## Strengths

- **Novel theoretical decomposition of KL loss over subgrammars.** The paper defines inner and outer subgrammars (Definitions 3.3, 3.5) and proves that the KL-divergence loss of a language model on a PCFG decomposes into a sum of conditional divergences for each top-level subgrammar (Theorem 4.3, Corollary 4.4), with an explicit formula for recursive blow-up (Theorem 4.6). The idea that grammatical substructure induces additive loss recurrences is genuinely original and well-motivated.

- **Direct empirical validation of the loss recurrence.** Figure 1 shows a two-layer transformer where the overall KL-divergence closely matches the sum of subgrammar divergences at every epoch, including both the deterministic case (Figure 1a) and the probabilistic case where subgrammar terms are scaled by their occurrence probabilities (Figure 1b). The match is visually convincing and provides strong experimental confirmation of the theoretical results.

- **Well-controlled depth-vs.-length experiment.** Section 6 contrasts prediction error on non-recursive prefixes (depth 0, error stays under 0.02) vs. deeply nested prefixes (depth i, error grows to 0.17), while holding the next-token distribution identical across both conditions. This cleanly isolates recursion depth as the source of difficulty, which is a crisp experimental finding.

- **Framework opens productive research directions.** The paper explicitly surfaces open questions about when models learn subgrammars in parallel, how depth generalization fails, and whether gradient descent can find solutions that in principle exist. The subgrammar decomposition provides a reusable theoretical lens for studying CFG learning dynamics.

## Weaknesses

### Fatal

None.

### Major

- **Statistical rigor is absent from the CKA analysis, and claims exceed the evidence.** Table 1 reports CKA similarity values (e.g., attention CKA on full-grammar sequences rises from 0.258 to 0.281 for the 2-layer model, a +8.9% change) without confidence intervals, standard deviations, or significance tests, despite the experiments being run across 30 random seeds. The paper then states that the analysis "definitively" shows pretrained models are more aligned with the grammar's substructure. The numerical differences are modest, and without variance estimates the reader cannot assess whether they reflect genuine effects or seed-level noise. This is a recurring pattern: the paper makes strong claims ("definitively," "quite definitively") on evidence that lacks statistical support.

### Minor

- **The KL decomposition in experiments uses a prefix approximation rather than the exact restricted KL from Definition 4.2.** The paper computes subgrammar divergences "using a random (but likely) prefix" and notes that varying the prefix did not qualitatively change results. While this is a reasonable practical shortcut and the paper is transparent about it, it means the empirical validation is an approximate test of Corollary 4.5's context-insensitivity assumption rather than a direct verification of the full decomposition from Theorem 4.3. A systematic characterization of how well the context-insensitivity assumption holds (e.g., across different prefixes, training stages, and subgrammars) would strengthen the empirical case.

- **The parallel learning claim is based on visual inspection, not quantitative measurement.** The observation that subgrammar loss curves decline concurrently (Figures 1, 2) is intriguing, but no metric is proposed to distinguish parallel from sequential learning, and no baseline (e.g., a curriculum that deliberately delays some subgrammars) is examined. The paper itself frames this as an open direction rather than a proven result, but the abstract and introduction state it as a finding ("we show empirically that small transformers learn subgrammars in parallel"), which overstates what the experiments actually demonstrate.

- **Table 3 referenced in Section 5.2 is not accessible in the provided manuscript.** The paper describes a segregation analysis comparing embedding similarities across sequence types and states that pretrained models "are better at internally segregating sequences with and without subgrammar subsequences (Table 3)." Without access to this table, the claim is unverifiable from the main text. This is likely an artifact of the appendix being stripped, but the main text should summarize the key numerical results rather than only citing a table.

- **The comparison to children's language acquisition is unsupported.** The abstract and introduction invoke child language learning as a contrastive framing ("unlike children — who first master simple substructures before progressing to more complex constructions"), but the paper provides no developmental-linguistics evidence or citations for this claim, nor does it test it. The paper would be on firmer ground presenting its observations without this analogy.

### Trivial

- The phrase "quite definitively" in Section 5.2 is an overstatement given the evidence; softer language would be more appropriate.
- Corollary 4.7 is stated informally and not proved, which is acknowledged, but the main text should consistently flag it as an informal sketch rather than a formal result.

## Nice-to-Haves

- For the CKA analysis, report confidence intervals across the 30 seeds and consider a permutation test to assess whether pretrained models are reliably more aligned than scratch models. This would turn the suggestive CKA results into a statistically grounded finding.
- Design a quantitative parallelism metric (e.g., the maximum lag between subgrammar loss curves reaching a fixed fraction of their final decrease) and compare against a sequential baseline.
- Compute the exact restricted KL from Definition 4.2 (summing over all contexts) for at least one small grammar and model, to directly verify the recurrence without the prefix approximation.
- Drop or downplay the children analogy, as the paper does not engage with developmental data and the comparison raises questions the paper cannot answer.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"The theoretical results are largely static rather than dynamical"** — This criticism misunderstands the paper's contribution. The recurrence relations describe how KL loss decomposes at any point during training, and the paper explicitly verifies this decomposition across training checkpoints (Figures 1, 2). Corollary 4.7 sketches a dynamical condition. The recurrence is the contribution; criticizing it for not being a gradient dynamics theorem is scope creep.
- **"The empirical validation of the theoretical decompositions is approximate and incomplete, which undermines the claimed link"** — Framed as a fatal concern in the harsh critic, but the paper is transparent about the approximation and provides evidence that varying the prefix does not qualitatively change results. This is a legitimate caveat (retained as Minor above), not a fatal flaw.
- **"No variance estimates are reported for any of the empirical figures"** — Figure 3 does include variance shading. The loss curves in Figures 1 and 2 appear to be single runs, but these are meant to illustrate the decomposition, not to test statistically for differences between conditions.
- **"The result that error grows with recursion depth is consistent with prior work and is not surprising"** — While true that depth generalization failure is known, the experimental design (controlling for identical next-token distribution across depth-0 and depth-i conditions) is genuinely clever and goes beyond prior work.
- **"Missing model and training details"** — These are almost certainly in the stripped appendix; not the authors' fault.
- **"The paper references a 'Table 3'... this table is absent"** — The appendix was stripped by the parser. The main text does summarize what Table 3 shows, though without the actual numbers. Retained as Minor because the claim should be verifiable from the main text.
- **"The GPT-5.1 Instant anecdotal test does not strengthen the paper's core claims"** — The paper itself explicitly marks these as "purely anecdotal" and states they "should not be interpreted as direct evidence." This is appropriately caveated.
- **Demand for confidence intervals on large-scale benchmarks where single-run is the norm** — The CKA experiments use 30 seeds explicitly, so the absence of variance reporting there is a genuine gap. But demanding CIs on the loss-curve figures (which illustrate a decomposition, not a comparison) is excessive.
- **Criticism about missing related work (e.g., Cagnetta & Wyart)** — The paper does cite Cagnetta & Wyart (2024) in the Related Work section. This claim is factually incorrect.

## Novel Insights

None beyond the paper's own contributions. The subgrammar-based decomposition of KL loss is the paper's genuinely novel insight.

## Suggestions

- The paper's strongest contribution is the theoretical decomposition and its empirical validation in Figures 1 and 2. Restructure to center these, and treat the CKA analysis and curriculum-learning exploration explicitly as secondary, exploratory investigations rather than as co-equal contributions.
- Add a clear limitations section that acknowledges: the prefix approximation, the lack of statistical tests on the CKA results, the observational nature of the parallel learning finding, and the scope of the theoretical results (static decomposition, not gradient dynamics).
- If Table 3 cannot be included in the main text, summarize its key numerical findings with a sentence or two rather than only a parenthetical reference.

## Score and Decision

### Calibration anchors used

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| uOnElfFuey | 3.00 | R1 (low) | Much weaker; no theoretical novelty |
| NSBP7HzA5Z | 3.00 | R1 (low) | Speculative; no empirical validation |
| OW5Gf4cse1 | 3.00 | R1 (low) | Narrow scope; no theory |
| f7aWmxgSN4 | 3.00 | R1 (low) | Hints at universality; weaker evidence |
| fp77Ln5Hcc | 4.50 | R1 (mid) | Depth extrapolation; presentation issues; this paper is stronger |
| b5lXUwZiD3 | 5.25 | R1 (mid) | HMMs + transformers; empirical but less novel theory; this paper is stronger |
| MO5PiKHELW | 5.50 | R2 | Syntax acquisition in MLMs; rigorous empirics on one model; comparable but this paper has more novel theory |
| Xr5iINA3zU | 5.75 | R2 | Synthetic data collapse; different topic; less relevant |
| aWLQTbfFgV | 6.25 | R1/2 | Formal language recognizers; solid contribution; this paper is comparable |
| rUC7tHecSQ | 6.33 | R2 | Retrieval problem + attention head emergence; comparable quality |
| 0pLCDJVVRD | 7.00 | R1/2 | Percolation model of emergence; stronger empirical execution; this paper is weaker |
| STUGfUz8ob | 7.60 | R1 (high) | Abstract symbol reasoning; stronger theory and execution |
| n2NidsYDop | 8.67 | R1 (high) | Transformers provably solve parity; far stronger |

**Round 1 bracket:** 4.50–7.00. The paper is clearly stronger than fp77Ln5Hcc (4.50, depth extrapolation with presentation issues) and b5lXUwZiD3 (5.25, HMM learning, less novel theory), but weaker than 0pLCDJVVRD (7.00, percolation model with stronger empirics) and STUGfUz8ob (7.60, abstract reasoning with rigorous proofs).

**Round 2 narrowing:** The paper is comparable to MO5PiKHELW (5.50) in ambition and scope, but has a more novel theoretical contribution (subgrammar KL decomposition) vs. MO5PiKHELW's more rigorous empirical execution on a single model. It sits near aWLQTbfFgV (6.25) and rUC7tHecSQ (6.33) in overall quality — a solid accept-level contribution with some empirical gaps.

**Final score rationale:** The subgrammar decomposition is genuinely novel and Figure 1 provides compelling validation of the core theoretical claim. These are real contributions. However, the CKA analysis lacks statistical rigor while making strong claims, the parallel learning finding is observational rather than quantitative, and the children analogy is unsupported. These weaknesses are addressable but prevent the paper from reaching the 7.0+ tier where empirical execution matches theoretical ambition. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>