Now I have a clear picture. Let me write the final review.

## Summary

This paper introduces DelRec, a method for learning per-neuron axonal or synaptic delays in recurrent connections of spiking neural networks (SNNs) using surrogate gradient learning. The key technical contribution is a differentiable triangle-function interpolation with an annealing schedule that allows training real-valued delay parameters, which are rounded to integers at inference. The method is evaluated on three temporal processing benchmarks (SSC, PS-MNIST, SHD) using simple LIF neurons, achieving state-of-the-art results within the LIF-based model class on SSC and PS-MNIST, along with a detailed ablation study on SHD demonstrating that learned recurrent delays outperform learned feedforward delays in low-parameter regimes.

## Strengths

1. **Novel per-neuron recurrent delay learning with principled differentiable interpolation**: The paper introduces a clean formulation (Eqs. 9–13, Algorithm 1) for learning real-valued delays in recurrent SNN connections using triangle-function interpolation with σ annealing. This avoids predefining a maximum delay range, uses well-defined gradients throughout training, and is compatible with any spiking neuron model — a genuine technical advance over prior per-layer softmax-based approaches (Xu et al.) and EventProp-based methods (Mészáros et al.).

2. **Well-designed ablation study demonstrating the functional value of recurrent delays**: The SHD experiments (Figure 3, Table 2) are carefully executed with a clean train/validation split (noting the dataset's known methodological issues), 10 seeds, and systematic comparisons across model sizes from 2k–10k parameters. The finding that learned recurrent delays outperform learned feedforward delays in low-parameter regimes, with accuracy degrading less steeply as network size shrinks, provides concrete and credible evidence for the core thesis.

3. **Solid SSC results with proper statistical reporting**: On SSC, DelRec achieves 82.58±0.08% (3 seeds) using only LIF neurons, outperforming prior LIF-based methods. The error bars are tight. The paper honestly reports that the "recurrent delays only" variant (0.37M params, 82.58%) outperforms the combined recurrent+feedforward variant (0.55M params, 82.19%) — an interesting finding that the paper presents rather than hiding.

4. **First combination of feedforward and recurrent delay learning in a single SGL framework**: The paper demonstrates (Table 2, SHD) that jointly optimizing both feedforward delays (via DCLS) and recurrent delays (via DelRec) achieves 93.73±0.69% compared to 93.39±0.45% for recurrent-only delays, showing the two delay types are complementary — an architectural capability absent from prior work.

## Weaknesses

### Fatal
None.

### Major

1. **PS-MNIST result lacks statistical reliability**: The PS-MNIST accuracy of 96.21% is reported from a single seed, with no variance estimate. The margin over the previous best LIF-based method (ASRC-SNN, 95.77%) is only 0.44%. The paper's justification — "we only test one seed as all the previous state-of-the-art models on the dataset" (line 132) — perpetuates a known methodological weakness rather than addressing it. Since PS-MNIST is presented as one of two headline "SOTA" results, this single-seed evaluation significantly weakens that part of the paper's central claim. The authors should run at least 5 seeds before claiming a SOTA result on this benchmark.

### Minor

1. **Unqualified "SOTA" language in the abstract**: The abstract states that DelRec achieves "new state-of-the-art (SOTA) on two challenging temporal datasets" without qualification. Footnote 1 and the main text acknowledge that higher published numbers exist (Wang et al. at 83.69% on SSC; Chen et al. at 97.78% on PS-MNIST) but are excluded because they use substantially more complex neuron models. While the exclusion is defensible for the comparison table, the abstract's unqualified language gives the impression of absolute SOTA rather than SOTA among LIF-based methods. The conclusion makes a similar unqualified claim.

2. **Under-discussed finding that recurrent-only delays outperform combined delays on SSC**: Table 1 shows that the "only recurrent delays" variant (82.58%, 0.37M params) outperforms the "recurrent + feedforward delays" variant (82.19%, 0.55M params) on SSC. This result, which cuts against the narrative that combining both delay types is beneficial, is noted but not meaningfully analyzed.

3. **Delay initialization not reported in the main text**: The initial values of the learned delay parameters are not stated. Since initialization strongly influences optimization dynamics (a delay of 0 means default 1-step recurrence matching a vanilla RSNN; large initial delays would change the training dynamics substantially), this is an important hyperparameter that should be specified.

4. **σ annealing schedule underspecified**: The σ annealing schedule (initial value, decay rate, schedule type) is described only qualitatively ("decrease... throughout training down to 0"). Figure 2C shows σ=5 is used initially, but the precise schedule is not given.

5. **Computational overhead not discussed**: The scheduling matrix has dimension N × dim(Ẽ), which grows with the maximum delay. The paper does not analyze memory or runtime overhead relative to a vanilla RSNN.

### Trivial
None.

## Nice-to-Haves
- A direct controlled comparison between DelRec (per-neuron delays) and Xu et al.'s method (per-layer delays with softmax selection) on the same architecture, parameter count, and seeds would sharpen the technical contribution.
- Reporting the distribution of learned delay values for the SSC and PS-MNIST experiments would strengthen the claim that delays learn meaningful temporal structure rather than absorbing noise.

## Removed Points
These points were raised by the reviewers but removed from the main review for the following reasons:

- **Criticism about "first SGL-based" claim imprecision (Harsh Critic point #3)**: The critic argued that Xu et al. already learned recurrent delays with backpropagation, making the "first SGL-based" claim imprecise. However, Xu et al. learned a **single delay per layer** using softmax over a fixed candidate set, while DelRec learns **per-neuron axonal delays** using differentiable interpolation without a predefined range. These are meaningfully different in both granularity and mechanism. The paper's claim of being the first SGL method to train per-neuron delays in recurrent connections is accurate. **Removed as a misunderstanding of the paper's scope.**

- **Name typo "Hamouamri" vs "Hammouamri"**: This may be a parser formatting artifact; per hard rules on formatting artifacts, removed.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Run PS-MNIST over at least 5 seeds and report mean ± std to provide proper statistical support for the claimed SOTA result.
2. Qualify the SOTA claims in the abstract (e.g., "new state-of-the-art among LIF-based methods").
3. Discuss the under-performing combined-delays variant on SSC more thoroughly — why does adding feedforward delays hurt performance on this dataset?
4. Report delay initialization values and the full σ annealing schedule in the main text or a hyperparameter table.
5. Include a brief analysis of the computational overhead introduced by the scheduling matrix.

---

## Calibration

**Round 1 (Bracketing):** Searched for papers on "learning delays in spiking neural networks" across three bands: low (scores < 3.5), middle (3.5–7.5), and high (> 7.5). The most topically relevant anchors were:
- Delay Neural Networks (avg 4.50, Reject) — a weight-less delay-based SNN paper; clearly weaker than DelRec in method clarity and empirical rigor.
- Layer Synchronization in SNNs (avg 5.75, Reject) — an asynchronous SNN training paper; comparable scope but DelRec has a cleaner technical contribution.
- Kuramoto Oscillatory Neurons (avg 9.00, Accept) — strong but topically distant (oscillatory dynamics, not delays).

Initial bracket: **5.0–7.0**.

**Round 2 (Narrowing):** Searched inside (5.5, 7.5) for SNN temporal processing and delay learning papers. Key anchors read in full:
- DeepTAGE (avg 6.25, Accept, scores 5/6/6/8) — gradient enhancement for SNNs; similar quality level but DelRec's method is more novel, while DeepTAGE has broader-scale experiments (ImageNet).
- Temporal Flexibility / MTT (avg 6.20, Accept, scores 5/6/6/8/6) — multi-time-step training; comparable quality, DelRec has a cleaner contribution but more prominent single-seed weakness.
- ST-DANO (avg 5.75, Reject, scores 6/6/6/5) — neuron optimization for SNNs; DelRec is stronger in novelty and clarity.

**Final placement:** DelRec sits between the ~5.75 rejected papers and the ~6.2 accepted papers. Its core technical contribution (per-neuron recurrent delay learning) is stronger than most SNN method papers at this level, but the single-seed PS-MNIST result is a concrete empirical weakness that prevents it from reaching the 6.5+ range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>