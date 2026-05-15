Now I have a complete picture of the paper. Let me synthesize the final consolidated review.

---

## Summary

This paper introduces NOVOBENCH-100K, a large-scale TadA protein variant dataset containing 101,687 unique DNA sequences (avg. 11.1 amino acid mutations each) derived from two rounds of Phage-Assisted Non-Continuous Evolution (PANCE). Instead of using absolute read counts as labels, the dataset employs a ranking-based format (via a proposed SEQ2RANK algorithm), with ranking lists of lengths 2, 10, and 100. The paper benchmarks 80 biological language models across 24 papers on both in-domain (random 7:3) and out-of-domain (split by evolution round) ranking tasks, finding that models perform well in-domain but struggle out-of-domain.

## Strengths

- **Large-scale, deep-mutation TadA dataset.** NOVOBENCH-100K provides 101,687 unique variants with an average of 11.1 amino acid mutations per variant (Section 1, Figure 3), substantially exceeding the shallow mutation landscapes of typical deep mutational scanning benchmarks. The scale and mutation depth are specifically tailored for the TadA evolution task.

- **Comprehensive multi-modal benchmarking.** The paper evaluates 80 BLMs spanning protein, DNA, RNA, and multimodal domains (Section 4.1.1, Table 1). This breadth enables comparative analyses of modality, scaling law, and k-mer effects (Sections 4.2.1–4.2.3), providing a useful landscape of current model capabilities on this specific protein evolution task.

- **Realistic out-of-domain split design.** The out-of-domain split by actual evolution rounds (Section 3.5) is a well-motivated design choice that mirrors real-world protein evolution scenarios where future rounds are unknown. This is a genuine feature of the dataset that goes beyond standard random splits.

- **Ranking-based label format.** The paper's shift from regression on absolute read counts to ranking lists (Section 3.3) is a conceptually motivated approach to mitigate batch effects and experimental noise, making the dataset more robust for multi-experiment integration.

## Weaknesses

### Fatal
None.

### Major

1. **OOD evaluation rests on a single, uncharacterized split from only two evolution rounds.** With data from only two rounds of evolution (stated in abstract and conclusion), there is exactly one possible out-of-domain split. The paper provides no analysis of sequence overlap between rounds, distribution of mutations per round, or comparability of ranking lists across rounds. The claim that "BLMs cannot generalize to new evolution rounds" is too strong given that the domain shift between these two specific rounds is not characterized and could be extreme (near zero-shot). The paper acknowledges plans to expand (conclusion), but as presented, the core negative finding is structurally limited by the dataset size. This is the most significant weakness because it constrains how much can be concluded.

2. **The "near random guessing" claim is supported by weak baselines.** The paper compares fine-tuned BLM performance to "a randomly initialized ranking head without any training" (Figure 7 caption). This is not a meaningful random baseline — an untrained head is guaranteed to produce random outputs. A proper baseline should include (a) performance on shuffled test labels to establish the dataset-specific chance level, or (b) a simple non-BLM model (e.g., logistic regression on one-hot vectors) trained on the same OOD split. The paper does report one-hot baselines for in-domain but not for OOD. The fine-tuning experiments are also limited: only 3 learning rates, no variation in fine-tuning strategy (adapters, layer-freezing choices), and while the paper claims "training loss decreases while test metrics remain unchanged," no training curves are shown to support this. The central negative result — the paper's most impactful claim — needs substantially stronger evidence.

3. **SEQ2RANK is presented without validation or ablation.** SEQ2RANK is the core algorithm that generates the dataset's ranking labels, yet no experiment validates its effectiveness. The paper does not compare downstream model performance when training on (a) SEQ2RANK-generated rankings vs. (b) raw read counts used as regression targets, (c) simple sorting by read count without DAG consistency, or (d) rankings with different credibility weighting schemes. There is no analysis of how many cycles the DAG prevented or whether any sequences/rankings were excluded due to inconsistency. Without this, the reader cannot assess whether the ranking format adds value or whether the algorithm discards useful signal. This gap undermines the dataset's core construction methodology.

### Minor

1. **K-mer analysis draws strong conclusions from negligible differences.** The paper reports 3UTRBERT nDCG@10 scores of 0.870 (6-mer), 0.860 (5-mer), 0.869 (4-mer), and 0.870 (3-mer) and argues that 3-mer/6-mer being higher than 4-mer/5-mer "aligns well with the actual biological k-mer patterns." With differences ≤0.01 and no confidence intervals or error bars reported, these differences are well within noise. The biological interpretation is overclaimed.

2. **SEQ2RANK description lacks algorithmic detail needed for reproducibility.** Key details of the greedy sampling strategy are underspecified: the sampling ratio, how read counts are binned (if at all), the number of ranking lists generated per NGS list, and the exact behavior when no "safe" sequence is found for a given read key (Section 3.3). The DAG cycle-handling description — "A new sequence to sample is considered 'safe' when it will not introduce a circle" — does not specify what happens when all candidate sequences for a read key would introduce cycles (skipped? discarded? tie-breaking rule?). These details significantly affect reproducibility.

3. **No confidence intervals or error bars on key results.** Comparisons across modalities (e.g., 0.900 vs. 0.896) and the K-mer analysis lack any measure of variance. Single-run results make it impossible to assess whether observed differences are meaningful.

### Trivial

- The relationship between "77,900 ranking lists" and "101,687 unique DNA variants" is not explicitly explained (each variant can appear in multiple lists due to the greedy sampling from NGS data, but this is left implicit).

## Nice-to-Haves

- A synthetic domain shift experiment (e.g., train on sequences with ≤5 mutations, test on sequences with >10 mutations) would provide a controlled complement to the single available real OOD split.
- t-SNE/UMAP visualization of BLM embeddings colored by evolution round would help characterize the domain shift.
- Concrete example ranking lists (ground truth vs. predicted) for OOD successes/failures would improve interpretability.

## Removed Points

These points were raised by reviewers but removed because they conflict with verified weaknesses, are factually incorrect, or violate the review rules.

- **"SEQ2RANK novel design is better suited for robust evaluation"** (Strength Finder): Moved here because the weakness about no validation directly conflicts with the claimed superiority — without validation, the paper cannot support the claim that SEQ2RANK is "better suited."
- **"Clear demonstration of out-of-domain failure"** (Strength Finder): Moved here because the weakness about thin OOD evidence (weak baselines, single uncharacterized split) directly conflicts with the characterization of the demonstration as "clear" or providing "strong evidence."
- **"Table 12 results not visible"**: Removed per rule — the appendix containing Table 12 was stripped by the PDF parser; this is not an author error.
- **"Conversion from read count to editing efficiency not explained"**: The paper explicitly states that read counts are "indicative of the editing efficiency" and explains the biological mechanism (higher deaminase activity → faster proliferation → higher read counts). The mapping is correlational but clearly stated.
- **"Fine-tuning too limited" demands for comprehensive fine-tuning ablations (adapters, multi-layer freezing)**: Weakened to a minor note; the paper tests 3 learning rates for multiple models, which is reasonable for a benchmark survey paper. More exploration would strengthen, but the current scope is not unreasonable.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's ambitious claims about BLM out-of-domain failures and the thinness of the evidence base, but this is a straightforward assessment of methodological rigor rather than a novel observation.

## Suggestions

1. **Add proper OOD baselines.** Report performance of (a) a simple ML model (e.g., XGBoost on k-mer frequencies, 1-layer MLP on one-hot vectors) on the OOD split, and (b) the same BLM evaluation with shuffled test labels over multiple seeds to establish the dataset-specific chance level. Without these, the "near random" claim is ungrounded.

2. **Characterize the OOD split.** Report the number of sequences and ranking lists per evolution round, the percentage of test sequences appearing in the training set, and the average sequence identity of nearest neighbors between train and test. This would clarify the nature of the domain shift and allow readers to calibrate the difficulty of the OOD task.

3. **Validate SEQ2RANK with a controlled experiment.** Compare a representative model (e.g., ESM-2 linear probing) trained on SEQ2RANK rankings vs. raw counts as regression targets vs. simple sorted rankings without the DAG. This is essential to validate the core construction methodology.

4. **Report variance.** Report results over multiple random seeds (e.g., 5) for key experiments, especially the K-mer comparison and modality comparisons, to establish which differences are meaningful.

5. **Show training dynamics for OOD fine-tuning.** Provide a plot of training loss and test metrics across fine-tuning epochs to substantiate the claim that "training loss decreases while test metrics remain unchanged."

6. **Temper the K-mer conclusion.** Acknowledge that the 0.01 differences across k-mers are within noise and cannot support strong biological interpretations without confidence intervals.

---

## Score and Decision

The paper presents a genuinely useful dataset and a large-scale benchmark survey that will likely be a resource for the protein engineering community. The ranking-based formulation is conceptually interesting. However, the paper's most impactful claim — that BLMs fail on out-of-domain ranking — is supported by weak baselines and structurally limited by the availability of only two evolution rounds. The SEQ2RANK algorithm, central to the dataset's construction, receives no validation. These are significant gaps that prevent the paper from fully delivering on its claims. The dataset contribution is valuable enough to warrant publication in a suitable venue, but the paper needs substantial strengthening of the OOD analysis before the central finding can be considered established.

**Originality:** Moderate — the dataset is novel and targeted, the ranking formulation is interesting, but the benchmark methodology is standard.  
**Importance of research question:** High — TadA evolution for base editing is a timely and important problem.  
**Claims support:** Weak — the core OOD claim needs substantially stronger evidence.  
**Soundness:** Moderate — in-domain experiments are sound; OOD experiments and SEQ2RANK validation are incomplete.  
**Clarity:** Good — the paper is well-structured and clearly written.  
**Value to community:** Moderate-high — the dataset itself will be a useful resource, but its impact depends on the credibility of the benchmark results.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>