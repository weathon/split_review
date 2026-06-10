## Summary

This paper proposes ActionPiece, a method that applies byte-pair encoding (BPE) to action trajectories sampled by GFlowNet or RL policies, extracting frequently-occurring subsequences ("chunks") and adding them as macro-actions to the action space. The goal is to shorten effective trajectory length, improve credit assignment, and accelerate mode discovery. The method is evaluated on four environments (FractalGrid, bit sequences, graph generation, RNA binding) across GFlowNet, A2C, SAC, and random samplers.

## Strengths

- **ActionPiece consistently accelerates mode discovery for GFlowNets across all four tested environments** (Figure 3). On FractalGrid, chunking is particularly dramatic — atomic samplers get stuck in the first mode while chunked variants discover faraway modes. This directly supports the core thesis for GFlowNet samplers and is the paper's strongest empirical result.

- **Quantitative improvement in density estimation on graph generation** (Table 1). ActionPiece-Increment achieves an ELBO Gap of 0.25 (std 0.14) versus 0.72 (std 0.39) for the atomic baseline — a roughly 3× improvement. This is a clean, concrete measured benefit.

- **Demonstrated transferability of learned chunks** (Figure 6). Libraries of chunks learned on one RNA binding task (`L14_RNA1`) improve mode discovery when used to initialize samplers on two structurally related tasks (`L14_RNA2`, `L14_RNA3`), and GFlowNet-induced libraries outperform those from RL-based samplers. This goes beyond standard within-task evaluation in prior macro-action work.

- **Quantitative evidence that GFlowNet-learned chunks capture latent structure** (Table 2). GFlowNet-based samplers with ActionPiece-Increment achieve chunk occurrence mean ~1.11 and coverage mean ~0.69 on high-reward RNA sequences, far surpassing RL-based methods. The median coverage of 0.73 indicates most chunks appear in a majority of high-reward sequences.

- **Principled policy parametrization for nonstationary action spaces** (Section 4). The LSTM-based action encoder that produces embeddings for variable-length chunks and computes action logits via dot-product attention is a technically sound solution to an engineering challenge that naturally arises from the method.

## Weaknesses

### Major

1. **Claims are substantially broader than the evidence supports.** The abstract states the approach "demonstrates improved sample efficiency performance in discovering diverse high-reward objects, especially on harder exploration problems." Yet the paper's own presentation repeatedly qualifies the results: RL results are described as "mixed" (line 213); ActionPiece *hurts* mode discovery on RNA binding for A2C/SAC (line 213); ActionPiece-Increment *hurts* A2C on BitSequence (line 213); density estimation on the bit sequence task shows "chunking results in marginally worse performance" (line 266); the random sampler degrades on harder problems (line 213). The one consistently positive story is for GFlowNets. The paper would be substantially stronger if it reframed itself as a GFlowNet-specific technique and treated the mixed RL results as an informative finding (not a failure of generality) rather than claiming broad improvements to amortized samplers.

2. **No comparison against existing macro-action discovery methods.** The related work section (Section 2) discusses at least three prior approaches: n-gram-based macro-action composition (Dulac-Arnold et al., 2013), learning macro-actions as repeated/fixed-length subsequences (Durugkar et al., 2016), and evolutionary macro-action discovery (Chang et al., 2022). None are compared against. Without these baselines, the reader cannot assess whether ActionPiece is better, worse, or equivalent to prior techniques — only that it beats doing nothing in some settings. This substantially limits the paper's ability to claim a methodological advance.

3. **No ablation studies isolate what drives the improvements.** The method has several moving parts: BPE-based chunking, high-reward filtering threshold, the LSTM action encoder (which itself increases model capacity independently of chunking), chunking frequency, and the replay buffer. None are ablated. The most consequential missing control is: does the benefit come from the *content* of BPE-discovered chunks, or would *any* trajectory compression (e.g., random chunks of the same length distribution) produce similar gains? Without this, the paper's claims about BPE discovering "latent structure" are only weakly supported: the chunks are derived from high-reward trajectories, so they trivially appear in high-reward trajectories.

4. **The core technical contribution is thin for a top-tier venue.** The central algorithm is off-the-shelf BPE (1994) applied without modification. The paper's method section (Section 4) describes how to wire BPE into a training loop: sample, filter high-reward trajectories, run BPE, add tokens. No adaptation of BPE's mechanism, no theoretical grounding connecting frequency-based merging to useful MDP abstractions, and no analysis of whether BPE's text-compression inductive biases are appropriate for hierarchical action discovery. The paper is essentially an empirical demonstration that a standard tokenization algorithm helps GFlowNets when applied to their trajectories. For ICLR, this is a modest contribution that relies heavily on the strength of the empirical results, which (as noted above) are more mixed than the framing suggests.

### Minor

5. **"First demonstration of hierarchical planning in amortized sequential sampling" is overstated** (line 10). The related work section discusses extensive prior work on macro-actions and options in RL (Section 2), as well as library learning approaches like DreamCoder that learn hierarchical abstractions from sampled programs. The paper's contribution is incremental relative to this work, not a first demonstration. This framing should be recalibrated.

6. **Table 1 lacks uncertainty estimates for JSD and L1 distance.** The caption says standard deviation is reported in parentheses, but only the ELBO Gap column has std values. With only 3 seeds, this omission is notable. Relatedly, the ELBO Gap improvements (0.72→0.25) show overlapping standard deviations (0.39 vs 0.14), so statistical significance is unclear.

7. **No theoretical analysis of whether chunking preserves GFlowNet consistency.** Adding chunks changes the MDP (action space grows, trajectory lengths shrink). The paper does not analyze whether this preserves the detailed balance or trajectory balance constraints, or whether the nonstationary action space introduces bias into the GFlowNet training. This is not fatal — empirical validation can compensate — but it would strengthen the paper.

### Trivial

None.

## Nice-to-Haves

- An ablation with random chunks (matched length distribution) to isolate whether BPE's content matters or just trajectory compression helps.
- Qualitative examples of learned chunks (e.g., which nucleotide subsequences were learned in RNA binding) to make the "latent structure" claim concrete.
- A comparison that controls for the increased model capacity of the LSTM-based action encoder vs. a fixed-size action space policy.

## Removed Points

- **"ShortParse is undefined in the main paper":** Removed as factually incorrect. The paper defines ShortParse at line 166 as "a new fixed backward policy aimed at sampling the most compact backward trajectory in terms of the number of trajectory steps." Full implementation details are deferred to the appendix (per standard practice).
- **"Chunk execution detail relegated to a footnote":** Removed. The main text states "Whenever the abstracted action is chosen, its constituent actions are executed in order" — the footnote adds practical detail about masking, which is standard academic practice.
- **"BPE-on-modes baseline in Figure 5 is unfair":** Removed. The paper explicitly states this is a "minimum attainable shortest parse" serving as a lower bound, not a competitive baseline. The comparison is transparent about this distinction.
- **Pure formatting/style nitpicks and reproducibility concerns about cited references:** Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The core observation (BPE on sampled trajectories can help GFlowNet mode discovery) is what the paper demonstrates; the reviews do not add further synthetic insight.

## Suggestions

1. **Reframe the paper** to honestly acknowledge that the method primarily benefits GFlowNets, with RL results being mixed. Treat the RL failures as an informative finding about the interaction between exploration bias and chunk selection, not as a setback.

2. **Add comparisons against at least one prior macro-action method** (Dulac-Arnold's n-gram approach or Chang's evolutionary method). This is the single most important missing experiment for establishing the contribution's significance.

3. **Add an ablation with random chunks** as a control to isolate whether BPE's content matters or any trajectory compression helps. Also ablate the LSTM action encoder to separate the effect of increased model capacity from the effect of chunking.

4. **Report standard deviations for all metrics in Table 1** and consider increasing the number of seeds.

5. **Calibrate the "first demonstration" claim** (line 10) to acknowledge prior work on macro-actions and library learning in related settings.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>