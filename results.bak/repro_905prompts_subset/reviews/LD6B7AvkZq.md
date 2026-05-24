Now I have a complete picture. Let me write the final consolidated review.

---

## Summary

This paper introduces formal definitions of *inner* and *outer* subgrammars of probabilistic context-free grammars (PCFGs) and proves that the KL divergence of an autoregressive language model decomposes recursively over this subgrammar hierarchy (Theorems 4.3, 4.6). It empirically studies how small transformers learn CFGs, finding that models learn all subgrammars in parallel (rather than progressing hierarchically like children), that subgrammar pretraining improves CKA-based representational alignment and can modestly improve final loss, and that the primary axis of generalization difficulty is recursion depth rather than sequence length. The paper is positioned as an initial foray into studying learning dynamics through the lens of grammatical substructure.

---

## Strengths

1. **Novel formal definitions of inner and outer subgrammars (Defs. 3.3–3.5).** These provide a principled vocabulary for decomposing a CFG into its syntactic substructure and for stating theoretical results about how learning interacts with that substructure. The connection to Gruska's classical work on grammatical levels (Gruska, 1971) is appropriately acknowledged.

2. **Interesting empirical finding of parallel subgrammar learning (Figs. 1, 2).** The observation that small transformers improve on all subgrammars simultaneously throughout training — unlike the sequential progression seen in child language acquisition — is a genuinely thought-provoking finding that could open a new direction of inquiry. The plots showing KL divergence decompositions across training are visually compelling.

3. **CKA-based representational analysis (Table 1, Sec. 5.2).** Using centered kernel alignment across 30 random seeds to show that subgrammar pretraining induces higher cross-run similarity in attention layers, and that the embedding-space gap between subgrammar and non-subgrammar sequences widens, is a sound methodological choice. The finding that pretrained models' representations better reflect the grammar's substructure, even after subsequent full-grammar training, provides concrete evidence for an inductive bias effect.

4. **The decomposition framework itself is a novel perspective.** Treating the language modeling loss as decomposable over CFG substructure is a worthwhile intellectual contribution that bridges formal language theory and learning dynamics, distinct from prior work focused on static representations or whole-grammar behavior (Allen-Zhu & Li, 2023; Cagnetta & Wyart, 2024).

---

## Weaknesses

### Major

1. **The central theoretical claim is not directly verified against the experiments.** Theorem 4.3 states that the total KL divergence equals a sum of restricted KL divergences over subgrammars and terminal substrings. Figures 1 and 2 plot subgrammar KL divergences, and the caption claims "the KL divergence (loss) is the sum over the corresponding loss for each subgrammar," but the paper never performs the quantitative check: computing the predicted sum from the subgrammar divergences and comparing it to the measured total KL. Without this verification, the experiments are consistent with the theory but do not confirm it. This is a critical gap between the paper's strongest theoretical claim and its empirical evidence.

2. **Missing experimental details in the main text.** The extracted main text does not specify the model architecture (beyond "two-layer transformer" and "four-layer transformer"), training hyperparameters (learning rate, optimizer, batch size), data generation procedure, or training budget. While some of these may appear in the removed appendix, a paper whose central claims are empirical must be self-contained enough for a reader to assess methodology. This is a reproducibility concern.

3. **Overclaiming relative to evidence in several places.** 
   - The abstract and Section 5.2 claim to "show definitively" that pretraining results in representations "more aligned with the grammar's substructure," yet the CKA changes in Table 1 are modest (e.g., +8.9% for attention on full-grammar sequences with 10-epoch pretraining, −0.2% for MLP). No statistical significance or error bars are reported for these numbers despite using 30 seeds.
   - The claim that subgrammar pretraining "can even help achieve a lower final loss" (Sec. 5.2) is noted as diminishing with model size (works for 2-layer but not 4-layer), but the effect size and variability are not reported.
   - The "robustness to subgrammar location" claim (Sec. 5.1) is stated without showing the actual figure or data — the text says "this robustness is illustrated in Figure 5" which is not present in the extracted main text.

4. **Corollary 4.7 (parallel learning condition) is close to tautological.** It states that if gradient updates on one subgrammar do not hurt performance on others, then all subgrammars are learned in parallel. This is essentially a restatement of the definition of non-interference. The paper acknowledges this ("Stated informally," "An immediate future direction would be to study whether..."), but presenting it as a corollary inflates the theoretical contribution. The interesting question — *when* the independence condition actually holds for transformer training — is left entirely open.

### Minor

5. **Equation (4) rendering is garbled.** The derivation from (2–3) to (4) contains `\frac{\log P}{\log Q}` fractions that do not correspond to the KL divergence expansion. From the surrounding text and equation (5), the intended expression is clearly a sum of differences of logs (i.e., conditional KL divergences), so this is a formatting artifact rather than a mathematical error. But the garbled equation undermines reader confidence in the derivation.

6. **The kindest reading of the derivation sketch (Sec. 4.2, equations 1–4) is incomplete.** Even setting the rendering issue aside, the jump from equation (2) — a correct expansion of log(P/Q) via the chain rule — to equation (5) — the claim of additive decomposition — skips several steps about how the weighting `P_G(α a β)` factorizes over the subgrammar components. The text provides intuition but not formal justification. The proofs are said to be in the removed appendix, but the main-text sketch should be coherent on its own.

7. **CKA results lack error bars.** Table 1 reports average CKA across 30 seeds (a good practice) but no standard deviations or confidence intervals. Given the small percentage changes (e.g., −4.7% for MLP on full grammar at 20 epochs), it is impossible to assess whether these differences are statistically reliable.

8. **The GPT-5.1 anecdote (Sec. 6) is very informal.** Testing 5 vs. 5 examples and reporting 5/5 vs. 2/5 accuracy is not a meaningful experiment. The paper does acknowledge this ("purely anecdotal"), but including it alongside the other experiments creates a misleading impression of breadth.

9. **Generalization experiments (Sec. 6) use only one simple PCFG (nested parentheses).** The finding that depth (not length) drives difficulty is consistent with prior work (Bhattamishra et al., 2020; Lampinen, 2024). The paper's stated novelty is the subgrammar perspective, but the generalization experiments do not leverage subgrammar structure — they test a single recursive rule.

---

## Nice-to-Haves

- Explicitly compute and plot `Σ_i D_KL(P∥Q)_{A_i}` alongside the total KL to visually verify Theorem 4.3.
- Include error bars on all CKA and loss plots.
- Test the parallel learning claim on a grammar designed to violate the independence condition of Corollary 4.7, to see if interference can be induced.
- Ablate the "context insensitivity" assumption (Corollary 4.5) by measuring whether trained models actually satisfy it.

---

## Removed Points

- **"Fatal mathematical error in equations 1–4"** (Harsh Critic). The harsh critic claims equation (4) shows ratios of logs (`\frac{log P}{log Q}`) which would be mathematically wrong for KL divergence. This is a PDF extraction artifact (the original LaTeX almost certainly had minus signs, not fraction bars). The surrounding text and equation (5) correctly describe the result as a sum of KL divergences. The criticism is removed per the formatting-artifact rule.

- **"Missing proofs in appendix"** (Harsh Critic). Proofs are referenced to Appendix A, which is removed by the parser. Per instructions, missing appendix content is not a valid weakness.

- **"Theory/experiments connection never validated"** partial overlap with retained weakness #1. Merged and sharpened above.

- **"Condition for parallel learning is trivial"** merged into retained weakness #4.

- Strengths removed as generic/superficial: "The paper addressed an important problem," "The motivation is sensible," "The paper is well-positioned in related work." These are not specific to the paper's contributions.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. Restructure the paper so that the experimental section explicitly tests the theoretical decomposition: compute the predicted sum of subgrammar KL divergences and compare it directly to the measured total KL across training epochs.
2. Add experimental details to the main text: architecture specification (layers, heads, embedding dimension), optimizer and learning rate, batch size, training epochs, data generation method, and number of independent runs.
3. Report standard deviations or confidence intervals for all quantitative results (CKA values, final losses, prediction errors), especially those based on 30 seeds.
4. Either remove the GPT-5.1 anecdote or replace it with a systematic evaluation across multiple LLMs and CFG-derived test sets with adequate sample sizes.
5. Tone down overclaiming: replace "definitively" with more measured language, and clarify that the CKA changes are modest in magnitude.
6. Clean up the derivation in Section 4.2: rewrite equations (1–4) with proper subtraction of logs (not fractions) and show the factorization steps more explicitly.

---

## Calibration

**Round 1 bracket:** The paper sits between weak anchors (avg ~3.0: "Recovering Knowledge by Hardening Language Models," "Inductive Transformers") and strong anchors (avg ~7.0–8.0: "Percolation Model of Emergence," "When can transformers reason with abstract symbols?"), with the most topically similar papers centering around 4.5–6.5.

**Round 2 narrowing:** Compared against anchors:

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| "How transformers learn structured data" (F0Zd3knG9j) | 5.00 | Similar scope (CFG-based study of transformer learning). Our paper has more novel theoretical framework but less experimental rigor. Comparable quality. |
| "Depth Extrapolation of Decoders" (fp77Ln5Hcc) | 4.50 | Both study learning of nested structures. Our paper has broader scope and more original theory, but both share issues with limited experiments. Slightly above. |
| "Training Neural Networks as Recognizers" (aWLQTbfFgV) | 6.25 | Cleaner, more rigorous experimental methodology. Our paper has more ambitious theory but falls short on execution. Clearly below. |
| "Transformers Learn Variable-order Markov Chains" (TdgAtxP6G2) | 4.00 | Similar format (theory + experiments on formal languages), but our paper has more novel concepts. Above this. |
| "Mastering Syntax, Unlocking Semantics" (hNkXTqDrfb) | 3.75 | Similar theme (syntax learning dynamics) but weaker contributions. Above this. |

**Final score:** 5.0. The paper has genuinely novel ideas and an interesting perspective, placing it above the 3–4 range of papers with shallow contributions. However, the significant gap between the ambitious theoretical claims and the incomplete experimental verification, combined with missing methodological details and overclaiming, prevents it from reaching the 6+ range of well-executed papers. It is most comparable to the "How transformers learn structured data" (5.00) paper — both have interesting frameworks but fall short on evidence and rigor.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>