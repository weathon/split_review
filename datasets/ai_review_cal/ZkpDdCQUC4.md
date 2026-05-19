- Decision: Reject
- Avg Score: 4.60
- Scores: 3, 6, 6, 3, 5
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper introduces NOVOBENCH-100K, a large-scale ranking dataset for TadA (a base-editing enzyme), constructed from two rounds of in vitro evolution (PANCE) with 101,687 unique variants averaging 11.1 amino acid mutations. The key methodological contribution is SEQ2RANK, an algorithm that converts raw NGS read counts into internally consistent ranking lists by using experiment credibility (later rounds deemed more reliable) and a directed acyclic graph to prevent transitive conflicts. The paper provides in-domain (random 7:3) and out-of-domain (by evolution round) splits, and benchmarks 80 biological language models across protein, DNA, RNA, and multimodal families. The in-domain results show strong performance, but the out-of-domain results indicate near-random performance — a finding the paper interprets as a domain generalization gap.

## Strengths

1. **Ranking-based labels via SEQ2RANK**: The use of ranking lists rather than absolute read counts (Section 3.3) is well-motivated: it sidesteps the well-known batch effects and measurement noise that plague raw NGS read data. The DAG-based consistency enforcement is a principled engineering solution to the transitive-conflict problem that arises when constructing rankings from overlapping partial orders.

2. **Out-of-domain split by actual evolution rounds**: Providing a train-test split that separates experimental rounds (Section 3.5) is the paper's most distinctive design choice. It directly models the real-world protein evolution scenario where future rounds are unknown, and the finding that all 80 BLMs fail under this split (approaching random performance) is the paper's most striking result — regardless of whether it reflects a fundamental limitation of current models or a confound to be resolved.

3. **Scale and mutation diversity**: With 101,687 unique variants averaging 11.1 amino acid mutations (Section 3.4), this dataset is substantially larger and more mutationally diverse than typical deep mutation scanning benchmarks, making it a more realistic proxy for directed evolution.

4. **Comprehensive multi-modality benchmarking**: Evaluating 80 models across 24 papers spanning protein, DNA, RNA, and multimodal architectures (Section 4.1.1) provides a broad and useful snapshot of the current BLM landscape on a functional task.

## Weaknesses

### Fatal

None.

### Major

1. **The out-of-domain split construction is underspecified, and this matters for the paper's headline result.** The paper states that the split is "based on actual in-vitro evolution rounds" (lines 23, 98), but never clarifies whether individual ranking lists can contain sequences from both rounds. SEQ2RANK operates on the entire pool of sequences across all rounds (the DAG is global), so it is possible that ranking lists straddle rounds. If this is the case, a clean round-based split at the list level is impossible without breaking list integrity. Since the near-random out-of-domain result is the paper's most important finding, this ambiguity must be resolved — the authors should explicitly state whether lists are per-round or cross-round, and provide statistics (e.g., "zero ranking lists contain sequences from both rounds") to demonstrate the split is valid.

2. **SEQ2RANK's credibility weighting creates a potential confound for the out-of-domain evaluation.** The algorithm prioritizes later experimental rounds as "more reliable" (line 91: "later experimental rounds are considered more reliable, as the effects of initial randomness decrease over time"). Since the out-of-domain split uses earlier-round data for training and later-round data for testing, the training ranking lists could be systematically noisier/less consistent than the test lists. This would mean the model is trained on lower-quality labels, potentially contributing to the observed failure independently of any genuine domain shift. The paper partially mitigates this concern by noting that training loss decreases while test metrics remain flat (line 27) — the classic signature of distribution shift, not simply label noise — but the concern is not fully resolved. The authors should analyze whether ranking-list quality (e.g., internal consistency, conflict rate) differs between rounds, or provide a sensitivity analysis that removes the credibility ordering.

### Minor

3. **The claim that nucleotide BLMs "gain knowledge about protein functionality" is over-interpreted.** Section 4.2.1 (line 150) concludes this from the observation that DNA and RNA models perform comparably to protein models on the ranking task. An equally plausible explanation is that the ranking task is solvable from low-level sequence features that correlate with editing efficiency — such as GC content, codon bias, or local sequence similarity to the starting sequence — without requiring any deep understanding of protein function. The one-hot baseline is far too weak to rule this out. Stronger controls (e.g., ablation of specific sequence statistics, or training on shuffled sequences) would be needed to support the functional-knowledge interpretation.

4. **The out-of-domain evaluation covers only a single domain shift (two rounds).** The paper's dataset includes exactly two evolution rounds, so the out-of-domain split amounts to one training round and one test round. While the paper acknowledges this limitation (line 185), the conclusions in the abstract and conclusion — e.g., "BLMs struggle to generalize effectively on out-of-domain ranking" — imply a general phenomenon. A single data point cannot establish generality. The results are valuable as an existence proof, but the scope of the generalization claim should be explicitly bounded.

5. **Benchmark results lack error bars or variance estimates.** All reported scores (Table 1, Figure 5, Figure 6) are point estimates with no indication of variance across random seeds, different ranking-list constructions, or different training/validation splits. This makes it impossible to assess whether observed differences (e.g., between modalities, or between in-domain and out-of-domain) are statistically meaningful. The paper's main result — that out-of-domain performance is "comparable to random guessing" — would be significantly strengthened by reporting standard deviations or confidence intervals.

6. **The scaling law analysis is based on a small number of model families.** The paper states "Most BLM model families in Figure 6 demonstrate the scaling law" (line 159), but Figure 6 appears to show only 3–4 families, several with just 2–3 model sizes. The claim is not misleading per se — those families do show the trend — but the evidence is too thin to support a general statement about BLMs on this task.

7. **The k-mer analysis relies on a single model family.** Section 4.2.3 uses only 3UTRBERT to examine the effect of k-mer choices. The conclusion that "NOVOBENCH-100K aligns well with actual biological k-mer patterns" depends on a single model family, which is insufficient. Testing additional RNA models with different k-mer configurations would strengthen this claim.

8. **The only non-BLM baseline is one-hot encoding.** The paper uses one-hot vectors as the sole baseline (Table 1, line 143). Stronger non-learned baselines — such as BLOSUM scores, k-mer frequency features, or sequence identity to the starting TadA8e sequence — would provide a more informative lower bound for contextualizing BLM performance.

### Trivial

None.

## Nice-to-Haves

- **Validate the credibility weighting:** Compare ranking-list distributions (e.g., internal conflict rate, concordance with held-out experimental indicators) built with and without credibility-based sorting to confirm that the weighting does not systematically degrade training-set quality.
- **Per-round dataset statistics:** Report the number of unique variants, number of ranking lists, and distribution of list lengths for each round separately.
- **Add a learnability diagnostic:** Train a model on a random sample of test-round data (same distribution as the test set) to confirm that the ranking task is inherently learnable from that round's distribution, which would strengthen the case that the out-of-domain failure is genuinely about distribution shift.

## Removed Points

These points were surfaced in the reviews but filtered out as speculative, factually incorrect, or outside the paper's scope. They are listed here for completeness but should not be weighed in the final assessment.

- **"Credibility bias is a fatal/structural issue"** — Demoted from fatal to Major (see Major Weakness #2). The confound is plausible but the paper's own observation of decreasing training loss with flat test metrics (line 27) is more consistent with distribution shift than with simple label noise, meaning the concern does not invalidate the core finding.
- **"SEQ2RANK lacks quantitative details"** — Partially valid but merged into weaker form above. Dataset descriptions at this level of algorithmic detail are standard for benchmark papers.
- **"Ranking two items is trivial"** — The paper provides three tracks (2, 10, 100) of varying difficulty. The triviality of @2 does not harm the paper.
- **"Only one model per paper shown in Table 1"** — The paper explicitly states this is due to space and that full results are in the appendix (line 121). Standard practice.
- **"Fine-tuning details missing / in stripped appendix"** — Removed per instructions: parser strips appendices from all papers; they exist in the original submission.
- **"Dataset not available at review time"** — Removed per instructions: criticisms questioning release status of cited entities must be removed.
- **"Missing comparison with prior TadA optimization methods"** — Scope creep. The paper constructs a dataset and benchmark; it is not required to implement and compare against every prior computational method for the same protein.
- **Various formatting/grammar nitpicks** — Removed per instructions (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The most interesting takeaway from the review process is that the out-of-domain failure finding — while attention-grabbing — has a subtle confound (the SEQ2RANK credibility ordering) that the field should investigate before treating the result as a definitive statement about BLM generalization. The paper would benefit from red-teaming its own data construction pipeline rather than treating it as a neutral evaluation platform.

## Suggestions

1. **Clarify the out-of-domain split construction explicitly.** State whether ranking lists are intra-round or cross-round, and provide per-round statistics (list counts, variant counts, conflict statistics) to demonstrate the split is clean.
2. **Diagnose the credibility confound.** Compare ranking-list quality between rounds (e.g., using the DAG conflict rate as a proxy) and/or provide an ablation that rebuilds the dataset without credibility-based sorting.
3. **Tone down interpretive claims.** Replace "nucleotide BLMs gain knowledge about protein functionality" with the more factual "nucleotide BLMs encode features useful for predicting TadA editing efficiency."
4. **Add error bars.** Run a subset of models with 3–5 random seeds and report mean ± std for the main results.
5. **Bound the out-of-domain claim.** Explicitly state that the result is demonstrated for a single two-round TadA evolution, not claimed to generalize to all protein evolution scenarios.
6. **Add stronger non-BLM baselines** (BLOSUM, k-mer frequency) to better contextualize BLM performance.
