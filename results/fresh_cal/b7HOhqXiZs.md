Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes DeMo (Decoupled Momentum Optimization), a distributed optimizer that avoids full gradient synchronization by using DCT-based compression of momentum states. Each accelerator maintains its own local momentum, extracts top-k DCT frequencies as "fast moving components," synchronizes only those compact representations across devices, and uses the averaged result for the parameter update step. The slow-moving residual components remain local and diverge across accelerators. Experiments on OLMo models (300M and 1B parameters) trained for 100B tokens show that DeMo achieves training loss and downstream task performance comparable to AdamW while reducing per-step communication by several orders of magnitude.

## Strengths

1. **Genuinely novel algorithmic idea.** Decoupling momentum by separating "fast" and "slow" components using DCT-based frequency extraction is a creative and non-obvious approach. The method is architecturally agnostic, parallelizable, and avoids the SVD bottlenecks of low-rank projection methods (Section 3.2.1). The fixed orthogonal basis of DCT means decoding requires no auxiliary information — a practical advantage.

2. **Dramatic communication reduction demonstrated empirically.** Table 1 reports per-GPU communication requirements showing DeMo uses orders of magnitude less bandwidth than AdamW (e.g., for the 1B model, ~0.5 MB vs ~4.7 GB per step according to the strength finder's reading of the table). At the same time, Figure 1 shows DeMo's training loss curve closely tracking the AdamW baseline, and the three downstream evaluation scores (HellaSwag, ARC-Easy, PiQA) in Table 1 are comparable or slightly better. This directly supports the paper's central claim that DeMo can match full-synchronization AdamW with drastically reduced communication.

3. **Minimal integration overhead.** Section 4 states that adapting the OLMo framework required only including the DeMo optimizer class and disabling gradient synchronization in PyTorch DDP. The paper releases code and configuration files, supporting reproducibility and practical adoption.

4. **Memory savings via signum variant.** The signum variant (Section 3.3) eliminates the second-moment optimizer state used by AdamW, providing additional memory advantages for large-model training on constrained hardware — and this variant is what the experiments actually use.

## Weaknesses

### Fatal

None.

### Major

1. **No comparison to any existing communication-efficient method.** The paper surveys three categories of prior work (Section 2: quantization/sparsification, low-rank projection, federated averaging) but does not benchmark DeMo against a single representative from any of these categories. The experiments only show that DeMo approaches full-communication AdamW performance. This leaves the reader unable to assess whether DeMo's approach is genuinely superior to simpler alternatives (e.g., quantized all-reduce, GaLore-style low-rank projection, or federated averaging with tuned synchronization period) for the same bandwidth budget. The paper's claim of being "better than sparsity" (Section 2.2) is stated without evidence. This is a significant evaluative gap because the practical value of DeMo depends not just on matching AdamW, but on being competitive with other compression strategies.

2. **Limited experimental scope undermines robustness of central claims.** The evidence is restricted to: (a) two model sizes (300M, 1B), (b) 100B tokens (~3% of the Dolma dataset — justified by compute constraints but acknowledged as limited), (c) a single architecture (decoder-only Transformer), (d) a single training run per configuration with no multiple seeds or statistical significance reported, and (e) only three downstream tasks (HellaSwag, ARC-Easy, PiQA). For a method whose core claim is matching or surpassing the dominant optimizer (AdamW), the evaluation is too thin to establish that DeMo's convergence properties hold reliably at full training scale or generalize across architectures. The paper states that the re-trained AdamW baseline had its "learning rate schedule adjusted accordingly" (line 153) but gives no specifics about the learning rate, schedule, or any hyperparameter tuning for DeMo itself — a detail gap that weakens the comparison.

3. **Motivating conjectures are stated but neither proven nor empirically validated.** The entire algorithm is motivated by three conjectures (3.1–3.3) about spatial auto-correlation, temporal variance, and long-term importance of slow components. The paper states it "will not formally prove any of these conjectures" (line 71) — which is fine for an empirical paper. However, it also claims these conjectures "show indications of validity based on empirical evidence" (line 61) yet provides zero diagnostic evidence to support them. No analysis of momentum's DCT spectrum during training, no visualization of energy concentration in few coefficients, no tracking of how fast/slow components evolve, and no ablation isolating the effect of the conjectured properties. Without any such validation, the reasoning connecting the conjectures to the algorithm's design remains largely intuition-based. This does not invalidate the empirical results, but it leaves the paper's intellectual framing significantly weaker than it could be.

### Minor

1. **Hyperparameter sensitivity is underexplored.** Only s=64 and s=128 chunk sizes are tested, and the k sweep uses a fixed s. No analysis of the effect of chunk overlap, the interaction between β (momentum decay) and s/k, or how to set these hyperparameters in practice. Learning rate sensitivity for DeMo is not reported at all — only β is specified (0.999), while the actual learning rate and schedule are absent.

2. **Synchronization description has a subtle ambiguity.** Section 3.2.2 describes "an all-gather on the last dimension of the extracted bins" and then "averaging the amplitude of any duplicate frequencies." Since different accelerators independently extract top-k frequencies, the index sets will differ across devices, and the all-gather operation on the k-dimension alone produces misaligned tensors. The paper does not specify how indices from different accelerators are aligned before averaging — e.g., whether the gathered pairs are unioned by (chunk_index, frequency_index) key. An implementation could infer the correct approach, but the description would benefit from explicit clarification.

3. **Terminological confusion between spatial and temporal "fast."** The paper refers to "fast moving components" in the spatial DCT sense (high spatial frequency) but Conjecture 3.2 discusses "low temporal variance" for these components. The mapping from spatial frequency in the momentum tensor to temporal dynamics over training steps is asserted but never explained or demonstrated. The terminology conflates two different notions of "fast," making the conceptual motivation harder to follow.

### Trivial

- The abstract claims DeMo "improves convergence compared to previous state of the art optimizers," but the experiments only compare to AdamW, not a broader set of optimizers. This overstatement should be scoped to "matches or surpasses AdamW."

## Nice-to-Haves

- Diagnostic plots of the momentum's DCT energy concentration during training, showing that the top-k coefficients capture most of the signal and that removing them from the local momentum has the intended effect. This would validate the conjectures and strengthen the paper's conceptual framing.
- A small-scale weak-scaling experiment (e.g., 8→64 GPUs) to show that DeMo's communication reduction remains beneficial as accelerator count grows.
- A brief comparison to one representative from each prior category (e.g., quantized all-reduce with 1-bit gradients, GaLore, or federated averaging) under matched bandwidth constraints.
- Training a smaller model (e.g., 125M) to convergence on C4 or a similarly standard dataset to show long-run stability.

## Removed Points

These points from the inputs were removed (with justification):

1. **"No concrete numbers provided in text for communication reduction"** (Harsh Critic). The critic claimed the reader must "infer from the Table (which is an image)," implying the numbers are absent. The specific numbers (e.g., 4719.2 MB vs 468.7 KB) are present in Table 1. The table is rendered as an image in the text extraction, but in the original submission PDF it is perfectly readable. This is a parser artifact, not a paper deficiency. Furthermore, both the abstract and conclusion state "several orders of magnitude" in running text, which captures the key claim.

2. **Criticism of the signum variant being "added as an afterthought"** (Harsh Critic, Section-by-Section Notes). Presenting the general algorithm first (Algorithm 1), then introducing the practical signum variant (Section 3.3), is a standard and reasonable expository structure. The variant is then used in experiments, as would be expected.

3. **Critique about low-rank projection claim being an overstatement** (Harsh Critic, Section 2.2). The paper says compression via low-rank projection "is better than sparsity and should be investigated further" — this is a mild qualitative statement about a trend, not a factual claim requiring proof. It does not substantively affect the paper's contributions.

4. **Criticism about 100B token training being "only 3%" of Dolma** (Harsh Critic). The paper explicitly acknowledges compute constraints (line 153). Training LLMs to full convergence on 3T tokens with 64 GPUs is cost-prohibitive. The 100B-token experiments are standard for a proof-of-concept paper and are not a flaw per se.

5. **Strength Finder strengths about "important problem" framing**. Dropped as generic/superficial; the concrete strengths above capture the paper's actual merit.

## Novel Insights

The strength finder and harsh critic, taken together, surface one genuinely novel observation that the paper itself does not fully articulate: DeMo treats inter-accelerator divergence of optimizer states as a *feature*, not a bug. Prior communication-efficient methods try to approximate the exact all-reduced gradient with less data (quantization, sparsification, low-rank projection). DeMo instead allows the slow-varying components of the momentum to permanently diverge across devices, synchronizing only the fast-varying components extracted by DCT. This is a fundamentally different strategy from prior work, and it is this decoupling — not better compression — that enables the extreme communication reduction. However, the paper's current evaluation does not isolate this decoupling effect from the DCT compression mechanism, so the insight remains an observation about potential rather than a demonstrated property. Future work could test this by comparing DeMo against a variant that compresses the full momentum via DCT (without decoupling), to quantify the relative benefit of allowing divergence.

## Suggestions

1. **Add at least one head-to-head comparison with a prior communication-efficient method** (e.g., quantized SGD at matched bandwidth, or GaLore). This is the single most important gap to fill: the paper currently shows DeMo ≈ AdamW but gives no evidence it is better than simpler alternatives at the same communication budget.

2. **Report the actual learning rate and schedule used for DeMo and the re-trained AdamW baseline.** Currently these are unspecified ("adjusted accordingly"), which impairs reproducibility and comparability.

3. **Include diagnostic validation of the three conjectures.** Even one figure showing DCT coefficient energy concentration in the momentum during training, and how the extracted components correlate with the full momentum, would dramatically strengthen the paper's conceptual foundation without requiring theoretical proofs.

4. **Run multiple seeds** for at least one configuration and report the range/standard deviation, to establish that DeMo's convergence parity is not a single-run artifact.

## Score and Decision

This paper proposes a genuinely novel idea — decoupling optimizer state synchronization via DCT-based frequency extraction — and demonstrates empirically that it can match AdamW performance on LLM pre-training while reducing per-step communication by orders of magnitude. The core contribution is significant and well-motivated. However, the experimental evaluation is too narrow in several respects (no comparison to any other communication-efficient method, limited model sizes and training duration, no statistical rigor, and no diagnostic validation of the motivating conjectures) to fully support the paper's claims at the level expected for a top venue. The paper would benefit from substantial strengthening but the direction is promising.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>