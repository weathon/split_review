Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper introduces NOVOBENCH-100K, a large-scale protein dataset for in silico evolution of TadA (an enzyme critical for adenine base editing), containing 101,687 unique DNA variants from two rounds of Phage-Assisted Non-Continuous Evolution (PANCE) experiments. Instead of using raw read counts as labels, the authors propose SEQ2RANK, an algorithm that converts NGS data into 77,900 ranking lists (of lengths 2, 10, and 100) by enforcing experiment-level credibility sorting and sequence-level consistency via a directed acyclic graph. The paper benchmarks 80 biological language models (BLMs) across 24 papers spanning protein, DNA, RNA, and multimodal modalities. Key findings: BLMs perform well on in-domain ranking (random 7:3 split), but all models perform near random on the out-of-domain split (training on round 1, testing on round 2), even after fine-tuning.

---

## Strengths

1. **Novel ranking-based label format with principled consistency guarantees.** The paper moves beyond absolute read counts, which are sensitive to experimental noise and batch effects, to a ranking formulation. The SEQ2RANK algorithm uses credibility-based experiment sorting and a DAG to resolve transitivity conflicts — a methodological contribution that is principled and applicable beyond TadA (Section 3.3, Figure 4).

2. **Large-scale, realistic protein evolution data with high mutational diversity.** At 101,687 unique variants with an average of 11.1 amino acid mutations per variant, NOVOBENCH-100K far exceeds the scope of typical deep mutational scanning datasets (which often probe single or few mutations). The data comes from actual PANCE evolution experiments rather than synthetic mutagenesis, grounding the benchmark in real biological selection dynamics (Section 3.2, Figure 3).

3. **Comprehensive, multi-modal benchmarking of 80 BLMs with consistent methodology.** The evaluation spans protein (ESM2, ESM3, ProtTrans, SaProt), DNA (EVO, NucleotideTransformer, HyenaDNA, DNABERT series), RNA (RNA-FM, SpliceBERT, 3UTRBERT, RNA-MSM, RiNALMo), and multimodal models (LucaOne, Chai1), all evaluated with the same head architecture, ListNet loss, and learning rate sweeps. This provides a systematic and reproducible resource for the community (Table 1, Section 4.1).

4. **Practical relevance to gene editing.** TadA is a clinically relevant enzyme for adenine base editing, and the dataset is derived from actual directed evolution campaigns rather than synthetic benchmarks. This grounds the work in a real therapeutic application (Section 2.2, Section 3.1).

5. **Scaling law analysis across BLM families within three modalities.** The paper demonstrates empirically that within the same model family, larger models yield better in-domain ranking performance across protein, DNA, and RNA modalities — providing evidence that scaling laws observed in NLP transfer to biological sequence models on this task (Figure 6).

---

## Weaknesses

### Fatal

None.

### Major

1. **The out-of-domain evaluation is based on only two evolution rounds, making the generalization claim narrow.** The OOD split uses round 1 as training and round 2 as testing — a single domain shift. With only two rounds, it is impossible to tell whether the poor performance reflects a fundamental limitation of BLMs or idiosyncratic properties of this particular round pair (e.g., different starting pool, altered selection pressure, or batch effects). A robust evaluation would require multiple round-to-round splits (1→2, 2→3, etc.) and ideally a temporal holdout with ≥3 rounds. The paper acknowledges ongoing wet experiments to add more rounds (Section 5), but the current claim that "all BLMs perform poorly... resembling random guessing" is supported by only one data point. This limitation also interacts with the SEQ2RANK credibility weighting: with only two rounds, all round-2 data is automatically prioritized over round-1 data, which could artificially amplify the observed domain gap.

2. **The ranking labels lack independent validation against ground-truth functional measurements.** The paper asserts that rankings reflect editing efficiency because "higher deaminase activity leads to faster proliferation of bacteria" in the PANCE system (Section 3.2). While the biological mechanism is explained, the paper provides no empirical validation that the final ranking lists correspond to meaningful differences in TadA activity. It does not compare rankings to any independently measured activity values, show ranking consistency across experimental replicates, or demonstrate that known functional mutations are ranked appropriately. The absence of such validation cuts across the paper's main claims: if the rankings capture artifacts of the construction pipeline rather than genuine biology, both the in-domain success and OOD failure could be artifacts rather than meaningful findings. Even a small-scale validation (e.g., testing a handful of high-ranked vs. low-ranked variants) would substantially strengthen the paper.

### Minor

1. **Missing explicit random baselines for out-of-domain metrics.** The paper states that OOD results are "comparable to random guessing" (abstract) and compares against a "randomly initialized ranking head without any training" (Figure 7 caption). However, it does not report the theoretical expected values of nDCG, mRR, and SP under random ranking for each list length (e.g., expected nDCG@2 ≈ 0.5, expected nDCG@100 ≈ 0.63 under uniform random ordering). This makes the "like random" claim less precise than it could be. Furthermore, the one-hot baseline reported for in-domain (Table 1) is not reported for OOD, making it harder to calibrate how much worse than trivial the BLMs perform.

2. **Statistics on SEQ2RANK's DAG cycle-check process are not reported.** The DAG consistency check is a core component of the algorithm (Section 3.3), but the paper does not report how often sequences were rejected due to cycle creation, how many ranking lists were pruned or discarded, or how much the DAG step reshapes the dataset relative to naive ranking by read counts. Reporting these statistics would help readers understand how much the dataset is shaped by the algorithm versus the raw data.

3. **The k-mer analysis for 3UTRBERT is suggestive but lacks controlled comparisons.** The paper notes that 3-mer and 6-mer perform similarly (nDCG@10 of 0.870 for both) and interprets this as aligning with biological codon structure (Section 4.2.3). However, the differences across k-mer values are very small (0.860–0.870), and no comparison against a random or biologically meaningless k-mer is provided to rule out the possibility that any reasonable k-mer would perform similarly. The evidence is consistent with the biological interpretation but does not strongly support it.

### Trivial

- The scaling law analysis (Figure 6) shows within-family scaling, which is informative but expected; cross-family analysis is not attempted. This does not weaken the paper but limits the depth of the finding.

---

## Nice-to-Haves

- **Validate ranking labels on a small subset.** Even testing a handful of high- vs. low-ranked variants for actual editing efficiency in the lab, or showing ranking concordance across independent experimental replicates, would dramatically strengthen the paper's central contribution.
- **Report statistics on DAG cycle-check rejections.** This would clarify how much SEQ2RANK changes the data relative to a naive ranking.
- **Analyze the domain shift between rounds** (e.g., distribution of mutation counts, sequence diversity, read-number range) to help readers interpret whether the OOD failure reflects a true biological shift or an experimental confound.
- **Ablation of the ranking loss function.** A brief justification or comparison showing that ListNet loss is appropriate, or that other listwise/pairwise losses give similar results, would strengthen the benchmarking methodology.
- **Provide explicit theoretical random baselines** (expected metric values under random permutation) alongside the empirical "untrained head" baseline for all OOD tracks.

---

## Removed Points

These points were flagged by reviewers but are not retained as valid weaknesses:

- **Data/code availability criticism** ("these will be released 'soon' ... a major omission during review"): Removed per the hard rule that questions about the existence/release status of cited artifacts are not valid criticisms.
- **Table 12 not visible in extracted text**: Removed per the hard rule that missing appendix content is a parser artifact, not an author error.
- **Criticism that the paper does not discuss alternative ranking losses**: This is a methodological suggestion, not a weakness; moved to Nice-to-Haves.

---

## Novel Insights

The review highlights a tension not fully discussed in the paper: the very design choice that makes the dataset robust (credibility-weighted rankings that emphasize later rounds over earlier ones) may paradoxically *guarantee* a performance drop on the OOD split. If SEQ2RANK prioritizes round-2 data as more reliable and constructs rankings that are dominated by round-2 sequences, then the round-1 training set may contain systematically lower-quality or differently-structured rankings. The poor OOD performance could then reflect this algorithmic asymmetry as much as a true biological domain shift. Disentangling these two explanations — algorithmic artifact vs. genuine distribution shift in protein fitness — is an important direction for future work that the authors should address as they add more experimental rounds.

---

## Suggestions

1. **Add a small-scale validation experiment.** Even 10–20 ranked variants tested in a wet-lab editing assay (or compared against previously published TadA variant activity data, if available) would transform the ranking label concern from a potential fatal flaw to a non-issue.
2. **Report full results of the OOD fine-tuning** (the Table 12 results) in the main text or a clearly visible table, not only in an appendix.
3. **Characterize the round-to-round domain shift** with distributional statistics (mutational burden, sequence diversity, read-count range, overlap) so readers can assess whether the failure is biological or experimental.
4. **Compute and report explicit random baselines** for all OOD metrics and list lengths.
5. **Add a one-hot baseline for OOD** to match the in-domain comparison and calibrate the difficulty.

---

## Score and Decision

**Originality:** The dataset is novel — there is no existing large-scale ranking benchmark specifically for TadA evolution, and the SEQ2RANK algorithm is a genuine methodological contribution.  
**Importance of research question:** Gene editing is a high-impact application, and a reliable in silico evaluation benchmark for TadA design would be valuable to the community.  
**Claims support:** The in-domain results are well supported. The OOD claim is supported by the data but is limited by the single train/test pair (only 2 rounds). The ranking label validity claim is mechanistically explained but lacks independent empirical validation.  
**Soundness of experiments:** The benchmarking methodology is thorough (80 models, consistent setup, multi-metric evaluation), but the missing random baselines and lack of ranking validation are gaps.  
**Clarity of writing:** Clear and well-structured.  
**Value to the research community:** Potentially high, contingent on the dataset being released and the ranking labels being validated. The finding that BLMs fail on cross-round generalization is notable and could drive research on domain-robust protein models.

MY FINAL SCORE: <pineapple>6.0</pineapple>  
MY FINAL DECISION: <orange>Accept</orange>