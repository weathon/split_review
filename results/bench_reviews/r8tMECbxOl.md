## Summary
The paper proposes TDTransformer, a tabular classification framework that applies distinct embedding pipelines for categorical, numerical, and binary columns, alignment layers projecting them to a common space, an adapted (label-free) piecewise linear encoding (PLE) for numerical features, a column-type-aware (CTA) positional encoding, and a contrastive pre-training stage. Experiments on an OpenML-derived suite report gains over XGBoost, CatBoost, SubTab, SCARF, and SwitchTab.

## Strengths
- **Type-specific embedding pipelines with alignment layers** (Sec. 3.1, Eqs. 2–7) are a clean, well-motivated design that explicitly addresses tabular heterogeneity, distinguishing categorical (tokenized text), numerical (PLE), and binary (scalar) channels.
- **Label-free quantile-based PLE adaptation** (Eq. 4, Table 1) makes PLE usable in unsupervised pre-training without target-fitted trees, and the [-1,1] codomain rationale tied to LayerNorm is a sensible architectural fit.
- **SSCL vs. SCL comparison on the same backbone** (Fig. 3) is a genuinely useful side experiment that is rare in the tabular SSL literature, and the t-SNE diagnostic (Fig. 4) gives concrete visual support for the positional-encoding ablation.
- **Honest reporting of a failure mode** — Sec. 4.2 admits XGBoost wins when column names/values are semantically void (V1…V100, v1…vk), which is unusually transparent.

## Weaknesses

### Fatal
None — the method and results, while empirically under-supported, are not fabricated.

### Major
- **The strongest contemporary transformer-based tabular baselines are absent.** The headline "significantly improves SOTA" claim is made against XGBoost, CatBoost, SubTab, SCARF, and SwitchTab only. FT-Transformer, FT-Transformer+PLE (Gorishniy et al., 2022), TabTransformer, and SAINT are not run — even though PLE is borrowed directly from Gorishniy et al. (2022) and TabTransformer is the paper's stated motivation for the permutation-invariance argument (Sec. 3.2). Without the FT-Transformer+PLE comparison in particular, the empirical contribution cannot be separated from "PLE in a transformer," which is already established in prior work.
- **Title and framing overstate the method.** "Language Models Are Good Tabular Learners" and Sec. 5's "rethink of the power of language models" are not supported by what the system actually does. Only the BERT *tokenizer* (i.e., a static token-embedding table) is reused (Sec. 4.1); the backbone is the gated transformer of Wang & Sun (2022) trained from scratch with contrastive pre-training per dataset. No pretrained LM weights are leveraged. The "semantic understanding" claim reduces to the token embedding table.
- **Internal inconsistency in benchmark size.** The abstract and Tables 2–3 cite "76 datasets," while Sec. 4.1 ("Datasets") states "56 real-world tabular classification datasets in the standard OpenML benchmark." The body never gives the dataset list, IDs, or selection protocol. With small reported gaps (1.67% binary, 3.62% multiclass), readers cannot tell which suite the numbers correspond to.
- **No ablation isolating the contributions of TDTransformer's components.** PLE vs. plain normalization, the Hadamard product with column-name embeddings (Eq. 5), the three-way embedding split, and the alignment layers are not individually ablated. Only positional encoding, pre-training objective, and batch size are ablated. As a result, it is not possible to attribute the headline gains to any particular component the paper proposes.
- **CTA positional encoding contradicts its own motivation and offers no measurable gain over standard PE.** Sec. 3.2 argues against positional encoding citing permutation invariance, but Table 4 shows CTA and standard PE are "similar," and removing PE causes a 5.45% multiclass drop. So one of the three listed contributions is effectively interchangeable with vanilla sinusoidal PE.

### Minor
- **No significance testing or variance reporting.** No multi-seed runs, no Wilcoxon/critical-difference analysis. 1.67%/3.62% average gaps are reported as point estimates only. Standard for OpenML-scale benchmarks would include at least seed variance.
- **Baseline tuning protocol unspecified.** XGBoost/CatBoost are notoriously tuning-sensitive; no search space, budget, or validation protocol is described for the tree baselines.
- **The V1…V100 failure mode is described anecdotally** (Sec. 4.2) without quantifying how many such datasets exist in the suite or how the gap scales with column-name entropy — yet this is exactly the |D| ≥ 2000 regime where tabular DL is expected to be strongest.
- **Hadamard product of column-name embedding with numerical-value embedding (Eq. 5) is unjustified** — no comparison to addition/concatenation.
- **Numerical-embedding related-work coverage is thin** (Sec. 2) given that this is one of two stated contributions.

### Trivial
- Notation collision noted by the paper itself between Eqs. 2 and 6 for column-name tokens is mildly confusing.
- Tables 2 and 3 are described as containing "a subset of 76 tables," which conflicts with the body's 56-dataset description.

## Nice-to-Haves
- Per-dataset win/loss plots against XGBoost (and ideally FT-Transformer) rather than only averages and scatter.
- A figure showing PLE bin distributions vs. plain linear embeddings to visually justify PLE's contribution inside this framework.
- An experiment freezing vs. reinitializing the BERT-tokenizer embedding table to test whether tokenizer "semantics" actually matter, given the from-scratch backbone.

## Removed Points
These points are flagged to be removed, treat them with caution.
- *Reproducibility nitpicks on corruption probabilities, exact augmentation, and complete hyperparameter sweeps* — these are typically deferred to an appendix that the parser may have stripped; not a substantive flaw.
- *"Missing related works"* in numerical-feature embeddings — cannot verify externally; partly already mitigated since FT-Transformer/Gorishniy et al. are cited (just not benchmarked, which is captured as a Major weakness above).
- *Strength: "comprehensive evaluation across 76 real-world tabular datasets"* — kept in spirit, but downgraded because the 76-vs-56 inconsistency and absent dataset list mean the scale claim is not verifiable from the paper alone.
- *Strength: "thorough ablation across multiple axes"* — dropped: the ablations omit the most important components (PLE, alignment, Hadamard product), and the CTA ablation actively undermines a stated contribution.

## Novel Insights
None beyond the paper's own contributions. The combination of type-specific embedding pipelines + label-free PLE is a reasonable engineering recipe, but the underlying ideas (PLE, column-type-specific encoders, CLIP-style alignment) are each pre-existing, and the paper does not surface a new conceptual finding about tabular learning beyond a moderate empirical bump on an unspecified subset of OpenML.

## Suggestions
- Add FT-Transformer, FT-Transformer+PLE, TabTransformer, and SAINT as baselines on the explicit OpenML/Grinsztajn suite with seeds and Wilcoxon tests.
- Reconcile the 76-vs-56 discrepancy and publish the exact dataset list, splits, and per-dataset numbers.
- Add component ablations: ‑PLE (plain normalization+linear), ‑alignment, ‑three-way split, ‑Hadamard column-name product.
- Reframe the title and Sec. 5 narrative. The method does not use a pretrained LM; "good tabular learners" is unsupported by the experiments. A title like "A column-type-aware transformer with PLE for tabular data" would be honest and still publishable on its own merits.
- Quantify the semantic-name failure mode by stratifying performance by column-name informativeness across the full suite.

---

**Axis-by-axis appraisal.** *Originality:* low-to-moderate; PLE-in-transformer and column-type-aware embedding are incremental over Gorishniy et al. (2022) and TabTransformer. *Importance of question:* moderate; closing the gap between transformers and GBDTs on tabular data is a well-motivated open question. *Claim support:* weak; the SOTA claim is undermined by missing key baselines, an unspecified dataset suite, and no significance testing. *Soundness of experiments:* weak; no component ablation for the central pieces, no seed variance, no baseline tuning protocol. *Clarity:* fair; method is readable, but the 76 vs. 56 discrepancy and unsupported "language model" framing damage clarity of contribution. *Value to community:* limited as written — without comparisons to FT-Transformer/SAINT/TabTransformer, practitioners cannot tell whether to adopt TDTransformer over already-published tabular transformer baselines.

## Score and Decision

Anchors retrieved (all from `/home/wg25r/split_review/datasets/deepreview_13k_calibration/`):
- `anzIzGZuLi.md` — TP-BERTa, avg 7.00 (high). Genuinely pretrains an LM on tabular data with relative magnitude tokenization. Much stronger than the paper under review, which only reuses a tokenizer; this anchor sits clearly above.
- `6LLho5X6xV.md` — UniTabE, avg 6.33 (high). Real universal pretraining protocol; better-supported empirical case; sits above the paper.
- `a06UO11IrQ.md` — TabPTM, avg 6.00 (high). Cohesive pre-training story with proper baselines; above.
- `rhgIgTSSxW.md` — TabR, avg 5.75 (medium). Strong empirical work with proper FT-Transformer/MLP baselines and big benchmark; sits clearly above.
- `EraNITdn34.md` — token-transfer paper, avg 5.67 (medium). Cleaner contribution, more focused ablations; above.
- `FDMlGhExFp.md` — TabDPT, avg 5.25 (medium). Comparable framing, better-supported; above.
- `zbpzJmRNiZ.md` — Marginal-effects tabular transformer, avg 5.25 (medium). Similar engineering paper with sharper ablations; above.
- `kFNxjehevx.md` — TabFlex, avg 5.25 (medium). Above.
- `wElgE9qBb5.md` — Mambular, avg 4.25. Architectural adaptation with mixed reviews; closest peer. The paper under review is weaker due to overclaimed title and missing transformer baselines, so it sits at or below.
- `0bjIoHD45G.md` — Fourier/Implicit Categorical Features, avg 4.20. Comparable scope; the paper under review has worse baseline coverage and stronger framing problems, so similar or below.
- `pE0UM18TQh.md` — TabForest, avg 4.33. Similar tier; this paper sits below.
- `a6XE2GJHjk.md` — TabGraphs benchmark, avg 4.00 (low). Different focus but a useful low anchor.
- `hz2zhaZPXm.md` — Foundation models for tabular, avg 3.50 (low). Overclaim issues similar to this paper; comparable.
- `3qDhqj6qfu.md` — TabKANet, avg 3.00 (low). Single-axis modification with thin baselines and overclaim — very close analogue to this paper.
- `ioOgrS0UKx.md` — PlicoTabTransformer, avg 3.00 (low). Engineering extension of TabTransformer/FT-Transformer with limited support — strong analogue to this paper.

Comparing directly: TDTransformer's missing FT-Transformer/TabTransformer baselines, internal 76-vs-56 inconsistency, unsupported "language model" framing, and absence of component ablation place it close to TabKANet (3.0) and PlicoTabTransformer (3.0), and below Mambular/Fourier-categorical (4.2). It is not as weak as foundation-model overclaim papers (3.5) because the engineering ideas are coherent, and individual diagnostics (Fig. 3, Fig. 4) have some value.

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>