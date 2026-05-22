Here is the consolidated review.

## Summary

This paper introduces TNT, a two-stage training paradigm for deep memory modules (e.g., Titans) that aims to decouple training efficiency from inference performance. Stage 1 uses a hierarchical memory architecture: a global module processes large chunks (C_G=2048) for long-range context, while multiple parallel local memory modules handle fine-grained details. The key innovation is a periodic reset of local memory states to a learned initial state every S_L tokens, which breaks sequential dependencies and enables context parallelism for non-linear RNNs. Stage 2 is a brief fine-tuning phase that adapts local memory modules to smaller chunk sizes (down to 1) for inference accuracy. Experiments on 150M-parameter models trained on 10B tokens show up to 17.37× training speedup over the strongest Titans baseline while matching or improving perplexity and commonsense reasoning accuracy.

## Strengths

- **Periodic reset mechanism enables genuine context parallelism for non-linear deep memory modules.** Equation (6) defines a learnable initial state W_init that resets local memory every S_L tokens, breaking the sequential dependency that previously prevented parallel computation. This is a technically sound solution to a well-identified problem (parallelizing non-linear recurrences) and is clearly the paper's most original contribution. Figure 4 demonstrates linear runtime scaling with sequence length, and at 32K tokens, TNT (C_L=128) runs at ~550ms vs FlashAttention's ~1000ms — strong evidence that the parallelism translates to real wall-clock gains.

- **17.37× training speedup with simultaneous quality improvements over the strongest Titans baseline.** Table 1 shows TNT C_L={64} reaching target loss 3.20 in 1.12 hours vs Titans C=8 in 19.48 hours. Table 2 shows TNT Stage 1 achieving 23.13 avg PPL and 41.0% commonsense accuracy, outperforming Titans C=8 (25.07 PPL, 39.0%) and vanilla Transformer (23.58 PPL, 38.3%). These are meaningful empirical gains for this model family.

- **Q-K Projection ablation provides clear evidence of its importance.** Table 3 shows removing the projection degrades PPL from 21.04 to 22.01 (≈1 point) and accuracy from 40.6% to 36.4%. This gives empirical support to the claimed domain-mismatch problem, regardless of whether the exact mathematical formulation is a proper projection.

- **Stage 2 fine-tuning improves over Stage 1 with only ~5% additional compute.** The best Stage 2 configuration (C_L={2,4,8,16}) achieves 23.09 avg PPL vs Stage 1 best of 23.13, with accuracy improving from 40.6% to 40.9%. The compute overhead is reported as minimal, which makes the two-stage framing practically useful.

## Weaknesses

### Major

- **The "decoupling" claim is oversold relative to the evidence.** The paper's central narrative is that Stage 1 uses large chunks for efficiency and Stage 2 adapts to small chunks for accuracy. However, the Stage 1 models already use multi-resolution local memories with small chunks (down to size 4 or 8). The improvement from Stage 2 is marginal (best Stage 1: 23.13 PPL → best Stage 2: 23.09 PPL). We never see a model pre-trained with a single large local chunk (e.g., 256) and then fine-tuned to small chunks to demonstrate a dramatic recovery. The two-stage framework is legitimate, but the "decoupling" claim would be more convincing with a cleaner separation: a Stage 1 that truly avoids small chunks entirely, followed by a Stage 2 that shows large recovery. As presented, Stage 2's gains could be partially attributed to simply having more training compute or a better multi-resolution configuration rather than adaptation per se.

- **The Q-K Projection formula (Eq. 7) is not a proper orthogonal projection as claimed.** The paper states it "project[s] the query q_t onto the subspace spanned by previously observed keys." The formula ∑_{τ} (k_τ k_τ^T / ‖k_τ‖²) q_t computes the sum of individual rank-1 projections onto each key. This equals the true orthogonal projection onto the subspace only if the keys are orthogonal. The paper notes that keys are often L2-normalized (unit norm), but this does not imply orthogonality. The true projection would be K(K^T K)^{-1} K^T, which requires matrix inversion. This is a clear mathematical imprecision in a core technical claim. The empirical ablation shows the mechanism helps, and the approximation may work well in practice, but the paper should characterize what Eq. 7 actually computes, rather than presenting it as a subspace projection.

- **The abstract claims evaluation on "Titans and TTT models," but TNT is only instantiated on Titans in the experiments.** The abstract states: "Evaluated on Titans and TTT models, TNT achieves a substantial acceleration." However, Section 5 clarifies "we instantiate it with a strong deep memory model, Titans" — TTT is included only as a baseline, not as an architecture that TNT was applied to. This is a factual overstatement in the abstract that should be corrected.

### Minor

- **Stage 2 fine-tuning protocol is underspecified.** The paper describes it as "a brief fine-tuning phase" and "a small number of steps" but does not state the number of steps, learning rate schedule, or which Stage 1 checkpoint each Stage 2 configuration is fine-tuned from. The mapping between Stage 1 configurations (C_L={8}, {8,16}, {4,8,16}, {4,8,16,32}) and Stage 2 configurations ({1}, {2,4}, {2,4,8}, {2,4,8,16}) is not explicitly stated. While this does not invalidate the results, it impairs reproducibility.

- **Baseline comparisons do not include the strongest efficient architectures.** The paper includes DeltaNet and GatedDeltaNet from the linear RNN family, but does not compare against Mamba-2, H3, or Hyena — architectures that also achieve efficient long-context processing. Given the paper's framing as advancing "expressive RNNs" as an alternative paradigm, situating TNT against these methods would strengthen the contextualization. Adding them is feasible since they operate at similar model scales.

- **The "domain mismatch" motivation for Q-K Projection lacks theoretical characterization.** The paper asserts that retrieval queries lie outside the key distribution on which the memory was trained, but provides no analysis or evidence of this distributional difference. The ablation shows the projection helps, but the underlying claim about domain shift remains untested (e.g., measuring distributional divergence between keys and queries in the trained model).

### Trivial

- The paper defines the function ξ(i, j) := i − (i mod j) as "the beginning of the chunk containing index i for chunk size j." In Eq. 7, the sum runs from ξ(t, C_L) to t, which is correct for a running sum. However, the Q-K projection uses keys from the current local chunk only — the paper should clarify whether this is a design choice (projecting only onto recent keys) versus the subspace of all past keys.

## Nice-to-Haves

- A cleaner decoupling experiment: pre-train a TNT model with a single large local chunk (e.g., C_L=128 or 256, no multi-resolution), then Stage 2 fine-tune to C_L'={1,2,4,8} and show large perplexity recovery. This would directly support the central claim.
- Runtime comparison against a Titans model with chunk size matched to TNT's global chunk (e.g., C=2048) to more cleanly isolate the benefit of the hierarchical design over simply scaling the chunk size in the standard model.
- Analysis of the computational overhead of the Q-K Projection (d×d matrix per local memory per head) in terms of both memory and FLOPs.

## Removed Points

The following points from the reviews were removed with justification:
- **"Central claim is entirely unsupported"** (Harsh Critic): Overstated. The paper does show Stage 2 improving over Stage 1, and the two-stage framing is coherent. The critic's claim that Stage 2 models "are not fine-tuned from Stage 1 models" is unsupported — the paper explicitly says they are. Removed as a strawman.
- **"Hierarchical memory not compared against simpler alternatives"** (Harsh Critic): The requested baseline (Titans with chunk 2048) would trivially confirm what Figure 2 already shows — Titans with large chunks has poor perplexity. The paper's comparison against Titans with various chunk sizes is sufficient to show TNT's advantage. Removed as demanding a point already addressed.
- **"Runtime measurements suspect"** (Harsh Critic): The paper provides detailed methodology (TPUv4 pod, batch size 0.5M tokens, sequence length varied). TNT beating FlashAttention at 32K is notable but the paper acknowledges lacking custom kernels and doesn't oversell this result. Removed as speculative without evidence of measurement error.
- **"Model scale too small"** (Harsh Critic): 150M parameters / 10B tokens is the standard scale in this subfield (matching the Titans, TTT, DeltaNet papers themselves). Not a valid weakness for papers in this line of work.
- **"Q-K Projection ablation confounded"** (Harsh Critic): Pure speculation without evidence. The ablation cleanly isolates the projection. Removed.
- **Generic/pseudoscience strengths from Strength Finder** (e.g., "addressed an important problem", "promising paradigm"): Removed as generic. Kept only concrete, evidence-grounded strengths.

## Novel Insights

The most interesting aspect of this work that the reviews surface but the paper does not fully develop is the tension between the "batch-parallel" framing and the actual architectural design. The periodic reset makes local memory modules stateless across shards, which is what enables parallelism — but it also makes them local in a very strong sense (no information flows between shards). The global memory compensates, but it operates at a coarse chunk size (2048). This creates an asymmetric architecture where fine-grained temporal dependencies are captured by independent local modules that do not communicate. An unasked question is whether this design limits the model's ability to learn cross-shard patterns at fine granularity — and whether the multi-resolution approach (multiple local modules at different chunk sizes) is what actually compensates for this limitation rather than the two-stage training. The paper's ablation (Table 3) shows that adding more local modules improves performance, which is consistent with this interpretation. A deeper analysis of when and why the reset hurts (and how global memory compensates) would be a valuable follow-up.

## Suggestions

1. Clarify the mathematical status of Eq. 7: either characterize it as an approximation to the subspace projection and discuss the conditions under which it is exact (e.g., orthogonal keys), or rename it to avoid overclaiming.
2. Add explicit mapping between Stage 1 and Stage 2 configurations in Table 2 (which checkpoint was fine-tuned into which Stage 2 model), along with fine-tuning hyperparameters (steps, LR).
3. Include a cleaner decoupling experiment with a single-large-chunk Stage 1 pre-training followed by Stage 2 fine-tuning, even if at a slightly smaller scale, to directly support the core narrative.
4. Correct the abstract to state that TNT was evaluated on the Titans architecture (not both Titans and TTT).
5. Consider adding Mamba-2 as a baseline to better contextualize TNT's quality-efficiency trade-off against the broader efficient architecture landscape.

## Score and Decision

**Round 1 bracket:** Based on calibration search, low-band (avg 2.0–3.0) contained papers with fundamental flaws or very weak contributions; mid-band (avg 5.75–6.25) contained solid method papers with clear contributions but some limitations (EM-LLM 5.75, MELODI 6.25, HOMER 6.25); high-band (avg 8.0+) contained outstanding contributions with stronger evaluation and theoretical grounding. Initial bracket: 5.0–7.0.

**Round 2 narrowing:** Within the 5.0–7.0 bracket, I examined Ultra-Sparse Memory Network (6.00, accepted) and AutoChunk (6.33, accepted). UltraMem (6.00) had a novel memory architecture with thorough experiments but suffered from readability issues and missing baselines — TNT is comparable in contribution depth with cleaner presentation. AutoChunk (6.33) solved a well-defined compilation problem with a formal optimization framework — TNT's contribution is more heuristic but addresses a harder architectural constraint (non-linear recurrence). Compared to MELODI (6.25), TNT has comparable experimental breadth but weaker theoretical grounding for one of its mechanisms (Q-K projection). The paper sits at the lower end of this range due to: (a) the Q-K projection mathematical imprecision, (b) the oversold decoupling claim, and (c) underspecified Stage 2 protocol. 

**Final score: 6.0.** The periodic reset mechanism is a genuine contribution to parallelizing non-linear RNN training, and the speedup results are convincing. However, the paper overstates the two-stage decoupling and contains a mathematical imprecision in its core Q-K projection formula. These issues can be addressed in revision.

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EukID7GvBy | 3.00 | 1 (low) | Weak paper about gradual fine-tuning; TNT is substantially stronger. |
| 4ymHtDAlBv | 2.33 | 1 (low) | Simple RNN variant for classification; TNT is far more novel and rigorous. |
| 2DD4AXOAZ8 | 2.00 | 1 (low) | MixAttention paper with limited experiments; TNT has stronger evaluation. |
| fDZumshwym | 5.75 | 1 (mid) | Dataset condensation paper with hierarchical features; different domain. |
| BI2int5SAC | 5.75 | 1 (mid) | EM-LLM episodic memory for LLMs; TNT has stronger methodological contribution but similar scale concerns. |
| TvGPP8i18S | 6.25 | 1 (mid) | MELODI hierarchical memory compression; TNT comparable in depth but with different strengths. |
| ulaUJFd96G | 6.25 | 1 (mid) | HOMER context merging; TNT has stronger architectural innovation. |
| OujTnpmAZG | 5.50 | 2 | Spiking neuron parallelization; different domain and lower quality. |
| FhbZ1PQCaG | 5.75 | 2 | Decision Transformers with internal memory; TNT is stronger. |
| 7iuFxx9Ccx | 6.00 | 2 | Test-time training with slimmable networks; different focus. |
| 4wk2eOKGvh | 6.50 | 2 | Test-time ensemble adaptation; cleaner evaluation but narrower contribution. |
| GQGNLEHmdl | 6.33 | 2 | AutoChunk compiler for memory-efficient inference; stronger formalization. |
| zjeHLSiNv1 | 6.00 | 2 | UltraMem sparse memory network; comparable contribution depth and quality. |
| E4Fk3YuG56 | 8.50 | 1 (high) | Cut Cross-Entropy loss optimization; stronger theoretical contribution and broader impact. |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>