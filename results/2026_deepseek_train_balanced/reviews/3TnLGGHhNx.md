## Summary

This paper proposes applying Byte-Pair Encoding (BPE) to quantized visual tokens (from VQ-GAN) as an alternative to standard visual encoders in multimodal LLMs. The authors provide a theoretical analysis of why tokenization can benefit 2D sequence learning with Transformers (extending prior 1D analyses), design a 2D BPE algorithm that merges spatially co-occurring token pairs, and present preliminary experiments comparing VQ+BPE against a VQ-only baseline using a LLaMA-3.1-8B backbone. The paper identifies a genuinely interesting research direction but the evaluation substantially undersupports the claims made.

## Strengths

1. **Formal theoretical extension of tokenization benefits from 1D to 2D sequence data.** Proposition 1 proves that unigram models (which Transformers default to on raw 2D sequences) have an optimal loss bounded below by \(H(\pi)\), while the optimal loss is \(H_\infty\), and Remark 1 shows the gap can be arbitrarily large for the defined 2D Markov process. Proposition 2 then proves that a suitable tokenizer can achieve loss arbitrarily close to \(H_\infty\). This is a nontrivial extension of prior 1D analyses (Rajaraman et al. 2024, Makkuva et al. 2024).

2. **Controlled synthetic experiments that directly validate the theoretical prediction.** Figures 1–2 show that Transformers across many hyperparameter configurations fail to surpass the unigram baseline on 2D Markov data without a tokenizer, but achieve optimal loss with one. This isolates the effect of tokenization from confounding factors like dataset scale.

3. **Consistent gains across all six benchmarks when BPE is added to the VQ baseline.** In Table 1, comparing the best configurations of LLM+VQ vs LLM+VQ+BPE under the same training protocol (PT(freeze)+SFT), the BPE variant improves on every benchmark, with notable jumps on MME\(^p\) (+169 points) and MME\(^c\) (+30.1 points). The improvement is systematic rather than cherry-picked.

4. **Vocabulary-size analysis revealing an optimal balance between VQ-GAN base tokens and BPE merged tokens.** Figure 2 and the accompanying weight visualization show that small BPE vocabularies (4K) cause over-reliance on merged tokens, large ones (16K) cause over-reliance on base VQ tokens, and only a balanced 8K vocabulary yields uniform usage and peak performance. This non-obvious finding provides actionable guidance.

## Weaknesses

### Major

1. **No comparison to any standard MLLM paradigm, despite claiming a paradigm shift.** The paper repeatedly frames its approach as a "new learning paradigm" (abstract, §1, §7) that "unlike conventional approaches that rely on separate visual encoders" directly tokenizes visual data. Yet every experiment in Table 1 only compares within the paper's own family (LLM+VQ vs LLM+VQ+BPE). There is no comparison to a CLIP-based baseline (e.g., a simple projector-based LLaVA-style model) trained on the same data. Without this anchor, the reader cannot evaluate whether the BPE approach is competitive with, let alone a replacement for, existing paradigms. The absolute scores (VQAv2 57.1, MMBench 40.9) are far below what even small CLIP-based models achieve, and while the paper notes its limited data, a same-data baseline would have resolved whether this gap is due to the paradigm or the resource constraints. The paper cannot claim a new paradigm and evaluate only within it.

2. **The theoretical analysis does not connect to the actual BPE algorithm.** Proposition 2 constructs a tokenizer by applying the 1D result to each column (or row) separately and concatenating the per-column tokens. This constructed tokenizer is not the BPE algorithm described in Section 4, which simultaneously merges the most frequent adjacent pairs in both spatial directions. There is no proof that BPE achieves the bound in Proposition 2, nor any analysis of how BPE's iterative merging dynamics relate to the column/row decomposition used in the proof. Additionally, the bound depends on \(\delta = \min P(a'|a) > 0\); for a VQ-GAN codebook of size 8192, many transitions will have near-zero probability, making \(\delta\) extremely small and the bound potentially vacuous. The gap between theory and practice means the formal results motivate "some tokenizer can help for a specific synthetic process" rather than "BPE helps for real VQ-GAN-quantized images."

### Minor

3. **"Scalability" claims are disproportionate to the evidence.** The data scaling experiments add 50.6K–70K examples to a ~1.2M training corpus — increments of roughly 4–6%. This is called "scalability" and "scalability potential" (§5.3, §7). Scaling studies typically involve orders-of-magnitude increases. The marginal improvements observed could be attributed to dataset-specific characteristics rather than a generalizable scaling property. The paper would be better served by characterizing these as "additional data improvements" rather than scalability.

4. **The BPE adjacency tracking for composite tokens is underspecified.** Algorithm 1 uses an `UpdateMatrix` function and an adjacency matrix to count co-occurrences, but once tokens are merged into composite tokens with irregular shapes (1×2, 2×1, 2×2, etc.), it is not specified how the algorithm determines which pairs of composite tokens are adjacent, nor how the adjacency matrix is updated after each merge. Without this detail, the results are partially unverifiable. This is a nontrivial algorithmic question because the merge quality depends entirely on which pairs are counted as adjacent after composite tokens form.

5. **No error bars or significance measures.** The reported improvements are modest (typically 1–4 points on VQAv2, MMBench, POPE, VizWiz). Without standard deviations or confidence intervals, the reader cannot assess whether these gains are reliable. Single-run evaluation is common in this area, but the small delta relative to the VQ-only baseline makes variance reporting more consequential than usual.

## Nice-to-Haves

- **Add at least one same-data CLIP-based baseline** (e.g., a ViT-L/14 + MLP projector trained on the same PT+SFT data). This single comparison would either strongly support or refute the paradigm claim and is the most impactful improvement the paper could make.
- **Connect theory to practice** by analyzing whether real VQ-GAN token distributions exhibit the kind of structured co-occurrence that BPE exploits, or whether the empirical improvement correlates with the entropy gap measured on the actual distributions.
- **Provide a qualitative analysis** of what the learned BPE merges represent (e.g., object parts, textures, edges) to ground the claim that merged tokens capture "higher-level semantic concepts."
- **Compare against simpler 2D structure baselines** within the VQ framework (e.g., concatenating neighboring tokens, using 2D positional encodings, or processing tokens with a convolutional layer) to isolate whether BPE's specific merging strategy is better than other ways of incorporating 2D structure.

## Removed Points

These points were considered but removed per filtering rules:

- **Criticism about missing appendix content (proofs, details).** The paper's appendix was stripped by the parser; the original submission likely contains these. Removed per hard rule.
- **Criticism that "the paper cannot claim a paradigm shift" was softened** — the point is kept as a major weakness but reformulated to note the paper's own acknowledgment of being preliminary (Section 4, line 186: "this implementation ... is preliminary and does not involve extensive scaling ... to directly compare with state-of-the-art foundation models"). The core criticism remains: the claims in the abstract and introduction exceed what even a preliminary evaluation would support.
- **Formatting/style nitpicks.** Removed per hard rule.
- **Generic "could the metric be measuring a proxy" speculation.** Removed per filtering discipline.
- **Criticism about "the paper's explanation for PT(freeze) being better is weakly supported"** — kept but classified as too minor to list separately; it is a secondary speculation point.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the predictable tension between the paper's ambitious framing ("new paradigm") and its narrow evaluation (only VQ-only baseline). The most insightful observation from the reviewers is that the theoretical section, while mathematically sound, functions as an independent motivation for *tokenization in general* rather than a foundation for the specific BPE algorithm — but this observation follows directly from reading the paper rather than being a novel synthesis.

## Suggestions

1. **Re-frame the contribution.** Present the work as "a proof-of-concept demonstration of BPE for visual tokenization" with honest characterization of current performance limitations, rather than as a paradigm that already surpasses existing approaches. This would align the claims with the evidence.
2. **Add one external baseline.** A CLIP-based MLLM trained on the same data would resolve the central question about the approach's viability.
3. **Specify the adjacency tracking** in Algorithm 1 with pseudocode or a clear spatial rule (e.g., 4-neighborhood on the quantized grid, with merged tokens treated as a single cell).
4. **Run at least 3 random seeds** for the main comparison (LLM+VQ vs LLM+VQ+BPE under PT(freeze)+SFT) to assess variance, given the modest performance gaps.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>