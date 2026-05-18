Now I'll produce the final consolidated review.

## Summary
The paper proposes In-Context Risk Minimization (ICRM), which reformulates domain generalization as a next-token prediction problem. Given a stream of unlabeled test examples from the same environment, ICRM uses a transformer (GPT-2) to autoregressively predict labels for each test input, conditioning on previously seen unlabeled examples as context. The paper provides theoretical analysis showing that ICRM "zooms-in" on the environment-specific risk minimizer as context grows, and empirically demonstrates consistent improvements over ERM, ARM, and TENT across four benchmarks (FEMNIST, Rotated MNIST, WILDS Camelyon17, Tiny ImageNet-C), with gains of up to 8.5 percentage points in average accuracy and up to 11.6 points in worst-case accuracy.

## Strengths

1. **Consistent and substantial empirical outperformance across multiple benchmarks.** Table 1 shows ICRM beats ERM, ARM, and TENT in both average and worst-case OOD accuracy on all four datasets once context samples are available (≥25). On FEMNIST with 100 context samples, ICRM achieves 87.8% average accuracy vs. ERM's 79.3% and ARM's 84.6%. Gains on Camelyon17 are particularly striking: ICRM at 0 context achieves 92.0% vs. ERM's 68.6%.

2. **Clean architecture ablations that isolate the in-context mechanism.** Table 4 compares ICRM against ERM⁺ and ARM⁺ (same GPT-2 backbone but without in-context conditioning or with simple concatenation). ICRM dramatically outperforms both (e.g., on Tiny ImageNet-C: ICRM 38.3% vs. ARM⁺ 5.5% and ERM⁺ 29.7% at 0 context), showing that the gains come from the in-context design, not merely from a more powerful backbone.

3. **Environment-specific context matters.** Table 3 compares ICRM (context from same test environment) with ICRM-Mix (context sampled i.i.d. from all training environments). On FEMNIST and Rotated MNIST, ICRM consistently outperforms ICRM-Mix (e.g., FEMNIST 87.8% vs. 80.9% at 100 context), confirming that the method exploits environment structure rather than relying solely on a large pool of examples.

4. **Novel conceptual bridge between DG and ICL.** The paper argues convincingly that coarse environment indices are limiting and that richer context descriptions (unlabeled test examples as they arrive) enable more nuanced adaptation. The "zoom-out" proposition (Prop. 1) formally connects ICRM to ERM at zero context, providing a clean continuum from no-context to full-context behavior.

5. **Principled theoretical baseline.** Proposition 1 (Zoom-out) shows that without context, ICRM behaves exactly as the global ERM predictor. This establishes a theoretical consistency property and provides a clean interpretation of improvements as attributable to context length.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical guarantees assume away the central difficulty.** Theorem 1 (Full iid zoom-in) assumes an "amortization function" b(X, C_t) that converges almost surely to the environment-specific parameters θ^E_X. This essentially assumes that the unlabeled test data can fully recover the environment-conditional distribution—precisely the condition under which test-time adaptation would work perfectly. Theorem 3 (OOD zoom-in) assumes Gaussian latent variables with identity mixing and that test environments fall in Voronoi cells of training environments. These assumptions are so strong that the theory provides little practical guidance for when ICRM will succeed or fail on real benchmarks. The paper does not connect these assumptions to the experimental settings.

2. **The 0-context performance gap is unexplained and potentially confounds the analysis.** ICRM at 0 context sometimes dramatically exceeds ERM (92.0% vs. 68.6% on Camelyon17, 38.3% vs. 31.8% on Tiny ImageNet-C). The paper attributes this to "the training regimen... enabling the model to identify contextual images relevant to the current query, resulting in a better featurizer" (lines 428-431). However, no analysis is provided to support this explanation. If ICRM without any test context already substantially outperforms ERM, the training procedure itself (autoregressive prediction on training sequences) may be providing a benefit independent of the claimed in-context zoom-in mechanism. This confounding effect is not disentangled—e.g., by training ICRM but providing random/mismatched context at test time to see if the benefit persists.

### Minor

1. **Framing as "domain generalization" is imprecise.** The method requires access to unlabeled test examples during inference, making it a test-time adaptation (TTA) method rather than a standard DG method where the model is fixed at test time. While the paper is transparent about the test protocol and appropriately compares against TTA methods (ARM, TENT), the title and abstract claim to address "out-of-distribution performance" without clearly flagging this assumption. The paper would benefit from explicitly stating in the abstract: "We assume access to a stream of unlabeled test examples from the same environment."

2. **Incomplete baseline coverage.** Several relevant TTA methods are absent: TTT (Test-Time Training), MEMO, SHOT, and self-supervised adaptation approaches that also use unlabeled test data. Given the computational cost of ICRM (GPT-2 on image sequences), it is important to show that the improvement stems from the autoregressive conditioning specifically, not just from having a more compute-intensive backbone. The architecture ablations (ERM⁺, ARM⁺) partially address this, but comparing against a transformer that encodes the test context as a set (permutation-invariant, like a Set Transformer) would better isolate the contribution of the autoregressive ordering.

3. **The invariance claim rests on a toy example that is explicitly disconnected from the actual method.** The paper claims ICRM "discovers invariances" by extending the feature space, but the only supporting example (Section 5) provides environment means μ^e₂ as additional features explicitly ("instead of requiring the algorithm to learn such representation from general-form sequential context," line 334). The actual method must learn the relevant amortization from raw context images. No empirical demonstration shows that ICRM's learned representations are invariant in any meaningful sense.

4. **Insufficient positioning relative to ICL-for-meta-learning prior work.** The idea of using transformers to process test examples and make predictions conditioned on them is well explored in Neural Processes (Garnelo et al., 2018), in-context few-shot classification (Chen et al., 2022), and broader ICL literature. The paper should more clearly distinguish its contribution—e.g., by arguing that DG poses unique challenges (distribution shift across multiple training environments) that make ICRM different from standard few-shot ICL.

5. **No discussion of computational cost or practical limitations.** Using GPT-2 for image classification with sequences of up to 100 images is far more expensive than ARM or TENT. The paper should report inference time, model size, and discuss practical trade-offs. Additionally, the assumption that test examples arrive in order and can be processed autoregressively may not hold in many real applications (e.g., medical diagnosis on individual patients).

### Trivial
None.

## Nice-to-Haves
- A quantitative analysis of how prediction accuracy evolves with context size per test instance (not just aggregated across the test set).
- A comparison against a transformer encoder that processes the test context as a set (permutation invariant) to test whether autoregressive ordering specifically matters.
- An experiment providing random/mismatched context at test time to disentangle "learning to use context" from "learning better features from the sequence training objective."

## Removed Points
These points were flagged for removal and should be treated with caution:

- **"0-context results are inconsistent with the theory"** (from Harsh Critic #1): The paper explicitly addresses this (lines 428-431), attributing the benefit to the training regimen producing a better featurizer. While the explanation could be stronger, the criticism that this is "inconsistent with the framing" ignores the paper's own discussion.

- **"Missing related works"**: Removed per instructions (not verifiable without external sources).

- **"Missing appendix/experimental setup details"**: The paper references the appendix (\Cref{sec: experimental setup}, \Cref{sec: thms_proofs}) for these details; the parser strips appendix sections.

- **Strength Finder's generic strengths about "important problem"**: Removed as generic/superficial (e.g., "this paper addressed an important problem").

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Reposition the contribution as a test-time adaptation method** in the abstract and introduction, explicitly stating the assumption of accessible unlabeled test streams. This would eliminate the framing disconnect with standard DG and make the contribution clearer.

2. **Analyze the 0-context performance gap** by comparing ICRM trained with the sequence objective but evaluated with mismatched/random context or without any context from the test environment. This would disentangle the training procedure benefit from the in-context zoom-in benefit.

3. **Sharpen the theoretical analysis** to bound error after finite context in terms of the diversity of training environments, rather than relying on asymptotic convergence under strong assumptions. This would better connect theory to the experiments.

4. **Add a Permutation-Invariant Context baseline** (e.g., Set Transformer encoding the context as a set) to test whether the autoregressive ordering specifically contributes to ICRM's gains.

## Score and Decision

### Calibration Anchors

**High-scoring anchors (avg ≥ 6):**
- **yOhNLIqTEF** (avg 6.67, Accept) — "Generalization of Transformers with In-Context Learning": Empirical study of ICL generalization boundaries. The current paper has stronger theoretical framing and comparable experiments, but weaker positioning relative to prior work.
- **aKJr5NnN8U** (avg 6.50, Accept) — "Toward Understanding In-context vs. In-weight Learning": Theory-driven paper on ICL emergence. Current paper has stronger empirical DG results but weaker theory.
- **YPIA7bgd5y** (avg 6.50, Accept) — "In-Context Learning Learns Label Relationships": Analysis of ICL mechanisms. Current paper has a more applied contribution but less mechanistic insight.
- **gK1rl98VRp** (avg 6.00, Accept) — "Towards Auto-Regressive Next-Token Prediction: In-context Learning Emerges from Generalization": PAC-Bayesian theory for ICL. Current paper has stronger empirical validation across DG benchmarks.
- **5sU32OCxgZ** (avg 6.00, Accept) — "TTVD: Test-Time Adaptation Based on Voronoi Diagram": TTA method. Current paper has comparable empirical strength with a broader conceptual contribution linking DG and ICL.

**Medium-scoring anchors (avg 4-6):**
- **pudmhZdV78** (avg 5.25, Reject) — "In-context learning in presence of spurious correlations": Narrower scope, weaker experiments. Current paper is stronger in both breadth and depth.
- **iLUcsecZJp** (avg 5.75, Accept) — "ICL Models with Typical Meta-Learners": Theoretical comparison. Current paper has stronger empirical contribution.
- **q1UyoY3MgJ** (avg 6.00, Accept) — "Rethinking Invariance in In-context Learning": Method for permutation-invariant ICL. Current paper has a different focus (DG) with comparable quality.

**Low-scoring anchors (avg ≤ 3):**
- **ZbOSRZ0JXH** (avg 3.00, Reject) — "Data-free OOD Generalization via Extrapolation": Weak experiments, unrealistic assumptions. Current paper is substantially stronger.
- **EVg9lwHFJs** (avg 3.00, Reject) — "Fine-Grained Emotion Recognition with ICL": Narrow task, weak results. Current paper is substantially stronger.

Compared against these anchors, the paper sits in the 5.5–6.5 band. It has a novel conceptual contribution, strong empirical results, and clean ablations, but is held back by over-strong theoretical assumptions, an imprecise DG framing, and incomplete baseline coverage. It is stronger than the ~5.25 papers and comparable to the ~6.0-6.5 accepted papers.

**MY FINAL SCORE:** <score>6.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>