Now I have sufficient calibration data. Let me produce the final consolidated review.

**Round-1 Bracket**: Based on comparisons with anchors from all three bands, the paper sits between 5.5 and 7.0.

**Round-2 Narrowing**: The paper is well above the 4.50 "Mimetic Initialization" paper (similar thesis but much broader/cleaner execution), comparable to the 6.00 "SSM Bottlenecks" paper and the 6.33 "Zoology" paper, and below the 8.00 "Never Train from Scratch" paper (which validates on real benchmarks). The most calibrated landing is 6.5.

---

## Summary

This paper empirically compares Transformers and modern state-space models (Mamba, Hyena, Mamba2, DeltaNet) on two synthetic benchmarks—multi-query associative recall (MQAR) and copying—using ~3,000 runs and ~20,000 GPU hours. The central finding is that SSMs succeed only within an extremely narrow learning rate window, while Transformers are robust across ~2 orders of magnitude, suggesting that prior expressivity comparisons between these architectures may be confounded by optimization instability rather than fundamental capacity limitations. The paper also documents opposing scaling behaviors (width benefits SSMs, depth benefits Transformers), identifies the 1D convolution as the driver of 1-layer Mamba's expressivity via symmetric ablations, and shows that DeltaNet achieves Transformer-like LR robustness.

## Strengths

1. **Optimization instability as a confounder in prior expressivity claims.** Figure 1 convincingly shows Mamba and Hyena achieve high accuracy only within a narrow LR window (~1e−4 for Mamba, ~0.001 for Hyena), while Attention succeeds across ~2 orders of magnitude. The dashed lines marking the LR grid from Arora et al. (2023) fall *outside* these windows, providing concrete evidence that prior negative results for SSMs on MQAR may reflect training brittleness rather than inexpressivity.

2. **Refutation of the "hidden dimension ≈ sequence length" memory bottleneck with proper tuning.** Figure 2 shows that with a finer LR grid (solid orange), Mamba solves MQAR at sequence length 512 with hidden dimension as small as 64—directly contradicting the prior claim (Arora et al., 2023; Jelassi et al., 2024) that recurrent models require hidden size to grow linearly with sequence length. The same models using prior work's default LRs drop to near zero.

3. **Symmetric ablation isolating the 1D convolution as the source of Mamba's single-layer expressivity.** Table 2 reports that removing conv1d from 1-layer Mamba drops accuracy from 99% to 2%, while adding a convolution before the QKV projections in a 1-layer Transformer raises accuracy from 2% to 99%. This cleanly demonstrates the two architectures are mechanically equivalent without this component.

4. **Clean width-versus-depth scaling asymmetry on the copy task.** Table 1 shows a 12-layer Mamba (width 1024, 80M params) scores 0%, a 24-layer Mamba (width 1024, 150M params) scores only 16%, but a 12-layer Mamba with increased width (1408, 150M params) scores 100%—matching the Transformer at 150M params. This provides parametric evidence that scaling SSMs in width rather than depth is necessary to unlock their performance.

5. **Identification of a stable SSM variant and a causal hypothesis for instability.** Figure 7 shows DeltaNet maintains ~0.9 accuracy across LRs from 1e−5 to 0.3 (dim 64), while Mamba and Mamba2 only peak at a single LR. The paper ties this to DeltaNet's Householder-based mixing (off-diagonal terms do not vanish), contrasting with Mamba/Mamba2's A_k decay rate that induces vanishing gradients.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Framing tension between the strong thesis and the paper's own nuanced evidence.** The paper states at line 39: "Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics." Yet the paper's own evidence shows genuine expressivity differences: 1-layer Transformers fundamentally cannot solve MQAR regardless of tuning (Section 4), and at equal width/depth on the copy task (12L/1024), Mamba gets 0% while Attention gets 100% (Table 1). Line 31 more cautiously notes "while fundamental expressivity issues exist between such model classes." The moderate version from the abstract—"a crucial differentiator lies not just in their expressivity but in their fundamental learnability properties"—is well-supported and should be used consistently. The stronger version at line 39 overreaches relative to the evidence.

2. **The induction head interpretation in Section 6 is speculative and lacks mechanistic evidence.** The paper claims a loss bump in 1-layer Transformers "resembles the formation of an induction head circuit" and that the model "attempts to form induction heads." Induction heads are defined (and known from prior work) as a *two-layer* circuit. The paper acknowledges this but still asserts the parallel. No attention pattern analysis, probing, or circuit analysis is provided; the bump could result from other optimization phenomena (saddle point escape, changes in gradient flow, feature learning phases). The paper does hedge with "resembles" and "hypothesize," but the discussion is the weakest part of the paper and should be either removed or substantially caveated.

3. **The DeltaNet analysis is too limited for the claimed conclusions.** Figure 7 tests only up to model dimension 256 (due to implementation constraints) and only on MQAR, not the copy task where the main findings were validated. The claim that "Transformer-level robustness is only achieved by DeltaNet" would require broader evaluation, especially at larger scales and on the second task.

4. **The width-preference claim is framed as causal without direct evidence.** The paper states "brittle optimization has a direct impact on scaling, causing SSMs to favor width over depth" (abstract). An alternative explanation consistent with the data is that SSMs have a genuine representational bottleneck through their finite hidden state (which the paper itself acknowledges at line 144: "a larger hidden dimension facilitates less aggressive compression"). Width-preference and optimization instability could be co-occurring phenomena both driven by the recurrent structure rather than one causing the other.

5. **No direct measurement of gradient dynamics.** The paper invokes vanishing gradients as the hypothesized cause of LR sensitivity (citing Pascanu et al., 2013; Zuchet & Orvieto, 2024) but does not measure gradient norms, loss landscape curvature, or any direct optimization diagnostics. This limits the mechanistic depth of the observational findings. Direct gradient measurements would substantially strengthen the narrative connecting LR sensitivity to the classical RNN training difficulties.

### Trivial
- Table 1 does not include a Transformer at equal parameter count to the Mamba 12L/1408 configuration (both 150M params). Showing a Transformer at 12L/1408 achieving 100% would symmetrically reinforce the width-scaling point.

## Nice-to-Haves
- Testing whether the core findings (narrow LR windows, scaling behavior) transfer even to a small language modeling task (e.g., perplexity on WikiText-103 with varying LRs) would substantially increase the weight of the paper's claims. The paper acknowledges this limitation, but it remains the most important one.
- Measuring gradient norms or spectral properties of the loss landscape to directly connect the observed LR sensitivity to vanishing/exploding gradient mechanisms.
- Testing whether the LR sensitivity is affected by optimizer hyperparameters beyond LR (Adam betas, weight decay, schedule).

## Removed Points
- *Criticism about SSM background section being "thin"* — Removed. Appropriate level of detail for a 9-page empirical paper's background; the paper cites Mamba/S4 papers for full details.
- *Criticism about not testing narrow + deep Mamba on copy task* — Removed as factually incorrect. Table 1 tests 24L/1024 (16% accuracy).
- *Criticism questioning whether Arora et al.'s grid was appropriate for their setting* — This is a speculation by the critic, not a verifiable weakness in the paper.
- *Generic strengths from Strength Finder about "important problem" and similar platitudes* — Removed as insufficiently concrete.

## Novel Insights

None substantially beyond the paper's own contributions. The observation that DeltaNet's Householder-based mixing avoids the vanishing-gradient issue is the closest to a novel insight that synthesizes across the reviewed findings.

## Suggestions
1. Harmonize the thesis statement: use the moderate version ("learnability is a crucial differentiator alongside expressivity") consistently and remove or soften the stronger claim at line 39.
2. Either remove the induction head speculation about 1-layer models or provide mechanistic evidence (attention pattern analysis, probing).
3. Expand the DeltaNet evaluation to the copy task and larger dimensions to support the "Transformer-level robustness" claim.
4. Consider adding gradient norm measurements to connect the LR sensitivity observation to the hypothesized vanishing/exploding gradient mechanism.

## Calibration Anchors

### Round 1 (Bracketing)
| Path | Avg Score | Comparison |
|------|-----------|------------|
| It4KL6XnPq (3.00) | 3.00 | Weaker paper on memory for RL; current paper is clearly stronger |
| NSBP7HzA5Z (3.00) | 3.00 | Inductive bias for transformers; current paper is much stronger |
| iVy7aRMb0K (4.50) | 4.50 | "Mimetic Init" — most directly related thesis; current paper is broader and cleaner |
| QFgbJOYJSE (5.75) | 5.75 | Theoretical SSM-Transformer comparison; current paper is stronger empirically |
| pymXpl4qvi (6.00) | 6.00 | SSM recency bias & over-smoothing; similar quality, comparable experimental rigor |
| b5lXUwZiD3 (5.25) | 5.25 | Transformer limits on HMMs; current paper is stronger |
| PdaPky8MUn (8.00) | 8.00 | "Never Train from Scratch" — strong paper on fair SSM-Transformer comparison with real benchmarks; current paper lacks real-task validation |
| GRMfXcAAFh (8.00) | 8.00 | New SSM model (LinOSS); current paper is weaker due to lack of proposed method |
| Tzh6xAJSll (7.60) | 7.60 | Scaling laws for associative memories; current paper is less theoretically deep |
| STUGfUz8ob (7.60) | 7.60 | Transformer reasoning on abstract symbols; theoretical focus, less directly comparable |

### Round 2 (Narrowing)
| Path | Avg Score | Comparison |
|------|-----------|------------|
| EGjvMcKrrl (6.00) | 6.00 | SSM generalization bounds; theory-practice gap, current paper has cleaner execution |
| LNYL96VIsD (4.75) | 4.75 | Large LR training instability generally; current paper is more focused and compelling |
| BwG8hwohU4 (5.33) | 5.33 | SSM stable reparameterization; current paper is stronger empirically |
| TBJCtWTvXJ (6.20) | 6.20 | Optimizer for training stability (SignSGD); different topic, less relevant |
| LY3ukUANko (6.33) | 6.33 | "Zoology" — the paper directly criticized by current work; has real LM validation; comparable quality |
| hwSmPOAmhk (7.33) | 7.33 | Factual recall in Transformers via associative memories; stronger theoretical depth |
| IiagjrJNwF (6.25) | 6.25 | Memory Mosaics architecture; different contribution type |
| KC58bVmxyN (6.75) | 6.75 | Cognitive model for relational structures; different topic |

**Initial bracket**: (5.5, 7.0). **Narrowing**: Paper is well above 4.50-5.33 anchors, comparable to 6.00-6.33 anchors, below 7.33-8.00 anchors. **Final score**: 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>