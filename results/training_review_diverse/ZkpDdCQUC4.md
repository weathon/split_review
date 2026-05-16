Here is my consolidated review, after cross-checking all reviewer claims against the paper content.

---

## Summary

NOVOBENCH-100K is a large-scale ranking dataset (101,687 unique TadA variants, 77,900 ranking lists) derived from two rounds of real in vitro evolution experiments. The paper introduces SEQ2RANK, an algorithm that converts noisy NGS read counts into consistent ranking lists, and benchmarks 80 biological language models across 24 papers on in-domain and out-of-domain ranking tasks. The key finding — that all BLMs perform near random on out-of-domain ranking despite strong in-domain performance — is significant and highlights a real gap in current models' ability to generalize across experimental rounds.

## Strengths

- **Large-scale, realistically mutated TadA dataset from actual in vitro evolution.** The dataset contains 101,687 unique variants with an average of 11.1 amino acid mutations (vs. typical DMS datasets with few mutations), derived from real PANCE experiments (§3.4). This provides a biologically realistic rather than synthetic benchmark.

- **Novel ranking formulation (SEQ2RANK) addressing experimental noise and consistency.** The algorithm converts NGS data into ranking lists using experiment-level credibility weighting and a DAG-based cycle check to maintain transitive consistency across lists (§3.3). This is a principled solution to the problem of using noisy read counts directly as regression labels.

- **Out-of-domain evaluation split that reveals a fundamental limitation of current BLMs.** The OOD split partitions data by actual evolution rounds, and the paper shows that all 80 BLMs perform near random guessing even after fine-tuning (§4.3, Figure 7). This finding is important for the community and directly supports the claim that models lack generalization across domain shifts in real protein evolution.

- **Comprehensive benchmarking across modalities and model families.** The paper evaluates 80 models from protein, DNA, RNA, and multimodal domains (§4.1.1), providing a thorough landscape of current BLM performance on a functional protein task.

- **Insightful auxiliary analyses.** The scaling law analysis across model families (§4.2.2, Figure 6), modality comparability analysis showing DNA/RNA BLMs perform comparably to protein BLMs (§4.2.1, Figure 5), and k-mer analysis showing alignment with biological codon structure (§4.2.3) add value beyond raw benchmark numbers.

## Weaknesses

### Fatal
None.

### Major
None that threaten the paper's core claims. The issues below are substantive but addressable.

### Minor

- **SEQ2RANK description lacks three specific details needed to understand dataset construction at a standalone level.** (a) *Credibility quantification*: The paper states experiments are sorted by "credibility" informed by biological knowledge (later rounds more reliable) and experimental indicators (gel electrophoresis, qPCR, Sanger sequencing), but provides no concrete scoring function, weighting scheme, or decision rule (§3.3, lines 91–92). (b) *Tied read counts*: The paper says "one unique read key can be sampled only once within each ranking list" (line 90) but does not specify what happens when multiple distinct sequences share the same read count — a common occurrence in NGS data. (c) *DAG cycle-check*: No discussion of computational cost or the order in which sequences are considered for sampling. While the authors state they will release code (abstract), the paper's own description should be precise enough for a reader to understand the construction pipeline. This is a real limitation for a dataset paper.

- **Out-of-domain evaluation rests on a single train-test split from two evolution rounds with no characterization of the domain gap.** The OOD split uses actual evolution rounds, but with only two rounds there is exactly one possible partition. The paper shows training loss decreases while test metrics stay flat (Figure 7), which is consistent with overfitting to round-specific features, but it does not characterize what those features are — e.g., mutation depth, sequence diversity, or experimental conditions differing between rounds. The paper also does not explicitly state which round is used for training and which for testing (it implies earlier rounds → train via "outcomes of future rounds... are unknown" in line 23, but this should be explicit). The conclusion that BLMs fail on domain shift is directionally correct and the finding is valuable, but the evidence would be stronger with distributional analysis of the two rounds.

- **Out-of-domain results lack comparison to simple non-BLM baselines.** The OOD results are compared only to a randomly initialized ranking head (§4.3, Figure 7). In-domain results use one-hot vector baselines (Table 1), but this comparison is not extended to the OOD setting. Simple baselines (e.g., one-hot + linear regression, sequence identity features, conservation scores) would help establish whether the failure is specific to BLM representations or reflects fundamental task difficulty.

- **No limitations discussion of the ranking approach itself.** The paper acknowledges limited data (only two rounds, only TadA) in the conclusion, but does not discuss a more fundamental limitation: ranking discards absolute efficiency information, which some downstream applications may require. This should be acknowledged.

### Trivial
- No confidence intervals or variance across runs are reported for in-domain results. For a benchmark with fixed splits, single runs are acceptable, but the paper should state whether training was deterministic.

## Nice-to-Haves
- A brief characterization of the distributional differences between the two evolution rounds (entropy of read counts, sequence similarity, mutation density) would strengthen the OOD analysis without requiring new data.
- Mentioning approximate GPU-hours or runtime would help contextualize the scale of the benchmarking effort.
- A brief acknowledgment of dual-use considerations (gene editing enzyme sequences) would be responsible, though not required.

## Removed Points

These points are flagged for removal per policy — treat with caution:

1. **"Table 1 appears to show many models from the same paper (e.g., multiple ESM2 sizes), contradicting the statement 'we only report one model for each paper.'"** — Table 1 is an image that cannot be verified from the text. The paper's text explicitly states one model per paper is reported (line 121). This criticism cannot be confirmed and is removed.

2. **"The paper never tabulates the out-of-domain numbers for the reader... Table 12 would be a missing table."** — Table 12 resides in the appendix, which is stripped by the parser. The table exists in the original submission. The criticism is removed per the rule about parser-stripped appendix content.

3. **"The paper never states how many ranking lists are generated."** — The paper explicitly states "77,900 ranking lists" in the abstract (line 4) and §1 (line 19). This is factually incorrect and removed.

4. **"The reader should not have to piece together how many rounds there are."** — The paper states "two rounds" in the abstract (line 4) and conclusion (line 185). The number of rounds is clearly stated. Removed as factually incorrect.

## Novel Insights

None beyond the paper's own contributions. The key insight — that BLMs fail on out-of-domain ranking despite strong in-domain performance — is the paper's own finding, not a novel synthesis from the reviews.

## Suggestions

1. **Provide a formal or pseudocode description of SEQ2RANK** in the main paper or appendix (which will be visible in the camera-ready). Specifically: (a) the credibility scoring function, (b) how ties at equal read counts are resolved, and (c) whether the DAG cycle check has a tractable amortized cost or is handled via indexing.

2. **Characterize the distributional gap between evolution rounds** using the existing data (e.g., sequence similarity distributions, mutation density, entropy of read counts per round). This would strengthen the OOD analysis without requiring additional experiments.

3. **Extend the one-hot baseline to the OOD setting** to show that the failure is not specific to BLM representations. Also consider one additional simple biological baseline (e.g., training on sequence identity to parent or k-mer composition).

4. **Explicitly state which round is training and which is testing** in the OOD split, and whether the split is fixed or variable.

## Score and Decision

**Originality**: Good. The ranking formulation for NGS data and the focus on TadA evolution (a practically relevant protein) are novel contributions.  
**Importance of research question**: High. Understanding whether BLMs can generalize across experimental rounds is directly relevant to real-world protein engineering.  
**Claims well supported**: Mostly yes. The in-domain results are well-supported. The OOD finding is directionally correct but rests on limited data (single split, two rounds).  
**Soundness of experiments**: Solid. 80 models, appropriate metrics, thorough reporting of hyperparameter choices. Minor gaps in baselines for OOD.  
**Clarity of writing**: Generally clear. The SEQ2RANK description is the main area needing more precision.  
**Value to the community**: High. The dataset fills a gap (large-scale, multi-mutation protein evolution data with ranking labels), and the negative result on OOD generalization is a useful signal.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>