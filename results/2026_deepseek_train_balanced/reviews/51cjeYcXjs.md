Now let me produce the final review.

## Summary

The paper proposes DDG Fingerprinting: a representation for binary programs that extracts data dependency graphs from basic blocks of disassembled binaries, hashes them for isomorphic uniqueness using Weisfeiler-Lehman graph hashing, and encodes each program as a one-hot Hamming vector for k-NN search. The claimed contributions are (1) a new interpretable representation for behavioral similarity, (2) adjustable feature resolution enabling coarse-to-fine search, and (3) training-free retrieval that can identify functionality in unseen malware. The main experimental finding is that the ZeusGameover Trojan shares a Jaccard coefficient of 1.0 with csrss.exe (Windows Client/Server Runtime Subsystem), suggesting the malware contains this benign system utility as a proper subset.

## Strengths

1. **Discovery of a specific exploitation mechanism through unsupervised search.** The paper reports that ZeusGameover Feb2014 has a Jaccard coefficient of 1.0 with csrss.exe (Section 3.1), meaning the Trojan contains this Windows system utility as a proper subset. This is concrete evidence that the DDG Fingerprint representation can capture semantically meaningful behavioral similarity without any training. The paper connects this to known CVE disclosures (line 190), showing the finding has real security relevance.

2. **Interpretable, training-free representation.** The representation produces search results that list specific known programs by name along with Hamming distances (Figures 6 and 7), allowing an analyst to see which known functionality a novel binary resembles. This contrasts favorably with black-box deep learning models whose internal representations are opaque, and the training-free nature is genuinely useful for zero-day scenarios where no labeled data exists.

3. **Quantitative characterization of functional overlap across the malware/benign boundary.** The paper reports specific Jaccard coefficients (Zeus vs. ls = 0.179, Linux.Wirenet vs. benign Linux programs: median 0.204, range [0.064, 0.270]), providing interpretable measurements of how much data-dependency structure is shared versus distinct across the malware/benign divide. These numbers constitute a concrete empirical finding about the structure of obfuscated malware.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative validation of search/retrieval performance.** The paper's central claim is that DDG Fingerprinting enables search and retrieval of programs based on behavioral similarity. However, no standard retrieval metrics (precision@k, recall, F1, ROC, accuracy) are reported. Figures 6 and 7 show k=7 nearest neighbors with Hamming distances, but this is a demonstration that the pipeline executes, not a validation that the retrieved neighbors are genuinely semantically similar. Prior work (Jang et al., Section 1.1) is cited as achieving "precision and recall above 90%" — which underscores the absence of comparable numbers here. The single csrss.exe finding is suggestive but constitutes one data point, insufficient to support broad claims about general retrieval effectiveness (Sections 3.3, 4). Without ground-truth evaluation, there is no evidence that the Hamming distance metric correlates with genuine functional similarity.

2. **No baseline comparisons despite comparative claims.** The paper claims the representation is "more explainable than existing approaches" (Section 1.2) and provides "an increase in accuracy and feature resolution" (Section 4) — comparative statements that require comparative evidence. Yet no experiment compares DDG Fingerprinting against any existing representation: not tf-idf, not n-gram hashing (as in Jang et al.), not CFG features, not function-level semantic hashing, not LLM embeddings. Without baselines, the paper cannot establish that DDG Fingerprinting adds value over simpler alternatives.

3. **"Adjustable resolution" — the paper's most distinctive claimed advantage — is never technically defined.** The term "resolution" and its adjustment appear over 20 times (abstract, Sections 1.2, 2.3, 3.1, 3.2, 3.3, 4) as a core contribution. Yet the paper never specifies the operational mechanism: is resolution adjusted by frequency-thresholding hashes? By selecting subsets of dimensions? By clustering hashes into coarser equivalence classes? Line 131 says "the feature resolution can be adjusted once the specific characteristics of the search have been refined, which reduces the dimensionality to several hundred dimensions between a set of programs" — but this describes the *outcome* (reduced dimensionality), not the *procedure*. Figure 5 shows t-SNE projections at "progressive increases in resolution" without explaining what changes between panels. For a claimed contribution that distinguishes the work from prior representations, this is a significant gap.

4. **Dataset is too small to support the scope of claims.** The benign set is ~500 programs from Windows System32 plus Linux /usr/bin. The malicious set consists of exactly two malware families (ZeusGameover Feb2014, Win32.APT28.SekoiaRootkit), plus one cross-platform example (Linux.Wirenet). The paper draws broad conclusions — "able to recognize patterns in novel malware with functionality not previously identified" (abstract), "identification of malicious behavior and functionality on a fine-grained level... is possible" (Section 3.3) — from experiments on two families. The csrss.exe finding could reflect genuine code reuse, or it could be an artifact of coarse hashing if the hash space is small enough that many programs produce overlapping sets; the paper does not analyze which case holds.

### Minor

1. **DDG construction captures a narrow slice of program semantics.** The data dependency graph captures only `mov` instructions between two operands, constructed as undirected graphs (Section 2.2.2). This excludes arithmetic, control flow, system calls, memory access patterns, and all other instruction types. The paper acknowledges this (lines 101-107) but provides no analysis of how much semantic information is lost or any evidence that the retained information is sufficient for meaningful behavioral similarity judgments. The undirected construction further loses directionality of data flow.

2. **k-NN results are not validated for semantic meaningfulness beyond the csrss.exe case.** Figures 6 and 7 list neighbors for both malware samples, but the paper only discusses the csrss.exe finding in detail. The other returned neighbors (e.g., AtBroker for the SekoiaRootkit, mentioned in passing in Figure 7's caption) are not analyzed for functional relevance. Without such analysis, the reader cannot assess whether the Hamming distance metric correlates with real behavioral similarity in general.

3. **Cross-platform claim is not demonstrated.** The paper mentions cross-platform capability (Section 2.1) but provides no results showing that DDG Fingerprinting successfully matches semantically similar programs across Windows/Linux. This is especially problematic since cross-platform comparisons involve different instruction sets (x86 vs. other architectures), and the DDG construction is tied to assembly-level operands.

4. **No discussion of runtime or scalability.** The Hamming space has "over 40k unique patterns" for ~500 programs (Section 2.3). The paper acknowledges the space must be recomputed for new data (Section 3.3) but gives no computation times, no scalability analysis, and no discussion of how k-NN search performance degrades as the dataset grows.

### Trivial
None.

## Nice-to-Haves

- Define "resolution adjustment" operationally (e.g., frequency thresholding, hash clustering, feature subset selection) and show a concrete example where changing resolution changes the returned neighbors.
- Report standard retrieval metrics (precision@k, recall@k) even using coarse ground truth (e.g., class labels for leave-one-out classification or manual analysis of returned neighbors).
- Compare against at least one simple baseline (e.g., tf-idf on assembly instructions, n-gram hashing) using the same k-NN retrieval setup.
- Analyze the remaining k-NN neighbors beyond csrss.exe to assess whether the distance metric correlates with functional similarity.
- Report runtime for DDG extraction, hashing, and k-NN search stages.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Related work is broad but shallow" / "citation style is unusual"** — Presentation/style criticisms that do not affect the paper's technical evaluation. Removed.
- **"Statistical variance is absent"** — Single-run evaluation is standard in this setting for retrieval tasks. Demoting to Nice-to-Haves. Removed.
- **"The paper does not discuss WL-hash collisions"** — Standard knowledge about Weisfeiler-Lehman hashing; impacts all work using it equally. Removed.
- **"One-hot encoding in 40k dimensions affecting Hamming distance meaningfulness"** — Hamming distance is well-defined in high-dimensional binary spaces. This is not an inherent problem. Removed.
- **"How are basic blocks identified? conditional jumps, call, ret"** — The paper explicitly says "jump instruction (jmp), or other control transition instruction" (Section 2.2.1). Already addressed. Removed.
- **Strength Finder's "adjustable resolution" as a demonstrated strength** — Since "adjustable resolution" is never technically defined, its status as a demonstrated strength is unsupported. Removed.
- **Figures not readable / parser artifacts** — Criticisms about figure content that are artifacts of PDF extraction, not the actual submission. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Define "resolution adjustment" operationally.** This is the single most important missing piece, as it is the paper's core claimed advantage over prior work. Specify the exact procedure (threshold? clustering? dimension selection?) and provide a repeatable example.
2. **Add at least one baseline comparison.** The simplest useful baseline would be tf-idf on assembly instructions (or n-gram hashing following Jang et al.) with the same k-NN retrieval setup. This directly tests whether the DDG abstraction adds value.
3. **Report precision@k or recall@k** using the available class labels as a coarse ground truth, or manually analyze the functional relevance of returned neighbors for a small sample.
4. **Either expand the malware dataset** substantially (more families, more variants) or **explicitly restrict the paper's claims** to a demonstration of a new representation rather than a validated retrieval system.
5. **Analyze all k-NN results** for functional coherence, not just the csrss.exe case. If the remaining 6 neighbors for each query are also semantically meaningful, this would substantially strengthen the paper.

## Score and Decision

The paper presents a coherent pipeline and one genuinely interesting finding (csrss.exe identification), but the evaluation is fundamentally insufficient for a top-tier venue. The paper's most distinctive claimed advantage ("adjustable resolution") is never technically defined. No quantitative retrieval metrics or baseline comparisons are provided, and the dataset (2 malware families) is too small to support the broad claims made. The method is reasonable and the csrss.exe result is intriguing, but in its current form the paper does not meet the standard of evidence required at ICLR.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>