Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper proposes RECO, a method that equips frozen vision-language models (e.g., CLIP) with a lightweight retrieval-and-fusion module to improve zero-shot fine-grained recognition. The key design is **uni-modal search** (using image-to-image and text-to-text nearest-neighbor retrieval from a large memory) followed by **cross-modal fusion** (augmenting image queries with retrieved text and text queries with retrieved images) via a learned one-layer transformer. Experiments show substantial gains on fine-grained classification benchmarks (e.g., +10.9 on Cars, +10.2 on CUB) and on the OVEN benchmark, where it even surpasses fine-tuned models on unseen classes.

## Strengths

- **Substantial and consistent gains on fine-grained classification** — Table 1 shows CLIP-B/32 improves by +10.9 on Stanford Cars, +10.2 on CUB-2011, and +5.8 on Flowers, with improvements consistent across all four backbones tested (CLIP-R50, CLIP-B/32, CLIP-L/14, LiT-L16L).

- **The core design choice (uni-modal search + cross-modal fusion) is convincingly validated** — Table 5 (tab:fusion) compares four search/fusion combinations; the proposed combination yields +9.0% average relative improvement over CLIP, while cross-modal search gives only +1.7% and uni-modal fusion hurts (−0.4%). This directly pins down the novel insight.

- **Strong control experiment rules out "more training" confound** — Figure 3 (left) shows that training a CLIP-style MLP on the same retrieved data *degrades* CUB accuracy from 52.8 to 44.8, while RECO raises it to 63.0. This cleanly demonstrates the gains are from retrieval-augmented learning, not additional parameters or training data.

- **Memory can be scaled/updated without retraining** — Figure 3 (center) shows that a model trained with only 1% of the memory still benefits dramatically when evaluated with the full memory. This is a practically valuable property.

- **Lightweight architecture** — The fusion transformer adds only 3.16M parameters (≈2% of CLIP-B/32), making the approach parameter-efficient.

## Weaknesses

### Fatal
None.

### Major

- **All headline results rely on a proprietary memory (WebLI), with no public-memory replication in the available text.** The paper uses WebLI (1B image-text pairs), a Google-internal dataset, as the retrieval memory for all experiments. While the method itself is memory-agnostic, this means: (a) the central results cannot be independently verified by the community, and (b) it is unclear whether the impressive gains depend on idiosyncrasies of WebLI (e.g., specialized fine-grained coverage). The Limitations section mentions "While we have shown that large public dataset such as LAION can serve this purpose" (line 526), but no experiments with a public memory are presented in the available text. Adding experiments with LAION-5B or another public source would substantially strengthen the paper's claims.

- **Missing comparison to the most directly related retrieval-augmented zero-shot method, SuS-X.** The paper cites SuS-X (Udandarao et al., 2022) in Related Work and notes that it also retrieves from a large databank (LAION) to improve CLIP zero-shot. It even categorizes SuS-X as a "cross-modal search and cross-modal fusion" variant. However, SuS-X is not included as an experimental baseline anywhere. Since both methods aim to improve CLIP zero-shot via retrieval, a direct comparison is needed to contextualize the claimed improvements. REACT is less directly comparable (it requires task-specific fine-tuning), but SuS-X is a near-neighbor baseline.

### Minor

- **Small numerical discrepancy between Table 1 and Table 5 (tab:fusion) for CLIP-B/32 on Places365.** The main results (Table 1, line 252) report 42.2 (+1.6) for RECO, while the ablation table (Table 5, row 1, line 342) reports 42.5 (+1.9) for the same configuration. The baseline is 40.6 in both tables, and all other dataset values match (Cars 68.1, CUB 63.0, Flowers 67.9, Im1k 64.6). This 0.3-point discrepancy is not acknowledged or explained. While small, it raises questions about experimental noise and should be clarified.

- **No confidence intervals or variance measures reported anywhere.** It is unclear whether the reported gains are statistically significant relative to run-to-run variation. Given that the paper reports only single-run numbers and includes a small unexplained discrepancy, some measure of variability (even on key ablations) would improve reliability.

### Trivial
None.

## Nice-to-Haves

- Reporting the retrieval hit-rate (how often the top-1 retrieved item matches the ground-truth class) would help build intuition for why the method works.
- A sensitivity analysis for the near-duplicate removal threshold would be informative but is not required.

## Removed Points

The following points from the reviewer inputs were removed after verification:

- **Criticism about "no analysis of retrieval quality" and "no sensitivity analysis for deduplication threshold"** — These are generic requests for additional experiments that don't correspond to specific problems in the paper.

- **Criticism about the paper not acknowledging its reliance on a large memory** — The paper explicitly discusses this limitation (Section "Limitations", lines 523-533) and even discusses using search engine APIs as an alternative.

- **Criticism about the paper not discussing reproducibility** — The paper discusses the reliance on a large memory as a limitation; the reproducibility concern is inherent to the use of WebLI, which is acknowledged.

- **Strength about "Zero-shot OVEN performance exceeds fine-tuned models" fully kept** — it is concrete and evidenced.

- **Strength about "Performance gain is not from additional training" fully kept** — valid control experiment.

## Novel Insights

None beyond the paper's own contributions. The reviews largely confirm the paper's own narrative (uni-modal search + cross-modal fusion is key; the method works well on fine-grained tasks; the lightweight fusion is efficient; the gains are not from extra training).

## Suggestions

1. **Add public-memory experiments** — Replicating the main results using LAION-5B (or a subset) as the retrieval memory would be the single most impactful addition. This would directly address the central reproducibility concern and demonstrate the method's generality beyond WebLI.
2. **Include SuS-X as a baseline** — Since SuS-X also improves CLIP zero-shot via retrieval (from LAION), including it in Table 1 would allow proper contextualization of the reported gains.
3. **Clarify the Places365 discrepancy** — Acknowledge and explain the 0.3-point difference between Tables 1 and 5, or ensure the numbers are consistent.
4. **Report variance** — Adding standard deviations for at least the main results or key ablations (e.g., over 3 runs) would strengthen statistical reliability.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>