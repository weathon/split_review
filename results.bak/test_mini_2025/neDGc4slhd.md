Now I have a solid calibration sense. Let me write the final review.

## Summary

This paper applies topological data analysis (TDA) — specifically persistent homology and Betti curve similarity — to compare the functional graphs of four CNN architectures (LeNet-extended, AlexNet, VGG-16, ResNet-18) trained on 30 disjoint 10-class subsets of ImageNet. Neuron activations are reduced via k-means++ to 1000 cluster representatives, a correlation-based distance metric is used to construct finite metric spaces, and the resulting Betti curves are compared across epochs and datasets using the infinity-norm similarity. The paper presents qualitative evidence that Betti curve similarity can distinguish architectures and track representation changes during training.

## Strengths

1. **Concrete example where TDA reveals information that accuracy does not**: Section 3.2 shows that for subset 27, models ResNet-18, VGG-16, and AlexNet have high pairwise Betti curve similarity while their test accuracies are all distinct (Figures 8–9), and the extended LeNet model differs from all three in the topological space. The paper correctly notes that "accuracy…would not readily reveal this difference" — providing evidence that the method captures something beyond standard performance metrics.

2. **Clear formal framework linking DNN functional graphs to persistent homology**: The paper defines functional graphs as finite metric spaces using a correlation-based distance (Equation 1), constructs the Vietoris–Rips filtration, and derives Betti curve similarity via the infinity norm (Equation 7). This provides a self-contained theoretical foundation.

3. **Reproducibility-oriented experimental design**: The study trains four architectures on 30 disjoint ImageNet subsets across 60 epochs with seven checkpoints. Implementation details (random seed 1234, hardware, hyperparameters, GitHub repository) are provided in Sections 2.1–2.2, enabling full reproduction.

## Weaknesses

### Fatal
None.

### Major

1. **Unvalidated k-means++ reduction undermines confidence in the entire topological analysis.** The paper reduces neuron activations to 1000 cluster representatives using k-means++ and then computes persistent homology on this reduced set. The paper itself states that "silhouette scores for the clusters…show that the clusters were poorly separated" (Section 2.3). No experiment — even on a toy scale where exact PH computation on the full activation set is feasible — validates that the persistent homology of the reduced set approximates that of the original activation space. The justification (citing Corneanu et al., 2019, for the claim that local structure is less important) is asserted, not demonstrated. Since every Betti curve and every similarity score derived from it depends on this reduction being topologically faithful, the lack of validation is a significant gap. This is not fatal — validation on a smaller network could address it — but as the paper stands, the core empirical chain is on uncertain ground.

2. **No baseline comparisons to simpler representation similarity measures.** The paper positions Betti curve similarity as a tool for comparing DNNs, yet does not compare against any alternative method such as CKA (Kornblith et al., 2019), SVCCA (Raghu et al., 2017), or even average pairwise correlation of activation vectors. Without baselines, it is impossible to assess whether the TDA machinery adds meaningful information beyond what simpler methods already provide. TDA is computationally expensive (66 minutes per experiment); the paper needs to justify this cost by showing that it reveals patterns that cheaper methods miss.

3. **Results are purely qualitative with no statistical support.** The paper makes claims like "temporal similarity is quite low at the beginning of training and then typically increases" and "for certain models and subsets, the similarity was quite low," but provides no confidence intervals, error bars, statistical tests, or effect sizes. Only 2 of the 30 subsets (subsets 11 and 27) are discussed in detail, and the selection appears anecdotal. For an empirical study whose stated goal is to show that Betti curve similarity "can be a useful tool," the evidence is too thin and informal to support the conclusion.

### Minor

4. **Connection between Betti curve similarity and actual network behavior is not established.** The paper describes Betti curve similarity as a "companion to accuracy" that could "provide a more nuanced understanding," yet no correlation is computed between the similarity values and any performance metric (accuracy, loss, generalization gap). The discussion of subset 11 notes a 5% accuracy gap between ResNet-18 and VGG-16, but this single anecdote does not constitute evidence that the topological measure tracks functionally meaningful properties of networks.

5. **Identical hyperparameters across all architectures may confound architectural comparison.** All four models are trained with the same learning rate (0.001), weight decay (0.0005), optimizer (Adam), and training duration (60 epochs). While this removes hyperparameter tuning as a confound, it may systematically under- or over-regularize some architectures relative to their typical configuration. If some models are undertrained, observed topological differences may partly reflect suboptimal training rather than inherent architectural divergence. This is a common concern in comparative studies and is manageable with proper caveats, but the paper does not discuss it.

### Trivial
None.

## Nice-to-Haves
- A small-scale validation experiment (e.g., a small MLP on a simple dataset where the full activation set is small enough for exact PH) comparing Betti curves from full and k-means-reduced activation sets.
- Correlation analysis between pairwise Betti curve similarity and pairwise test accuracy difference across the 30 subsets.
- Filtration parameters (epsilon range, number of steps) used for the Vietoris–Rips complex could be explicitly stated.
- A specific downstream application (e.g., detecting representation shift during training) with quantitative comparison to a simpler baseline.

## Removed Points
These points were flagged by the Harsh Critic but are removed or demoted for the reasons below.

- **"The Betti curve similarity is a very minor change"**: This is a judgment about novelty framing, not a concrete weakness. The paper is presented as an empirical study applying an existing summary statistic, which is an honest framing.
- **"Figure 4 is confusing / caption mismatch"**: The image descriptions in the parsed PDF are auto-generated and may not accurately reflect the actual figure content. Without seeing the original figure, this cannot be verified as a real error.
- **"No reproducibility details for the TDA pipeline (filtration parameters)"**: The appendix (where such details typically reside) was stripped by the PDF parser; these details likely exist in the original submission.
- **"The exposition of PH is textbook material"**: Standard context-setting for papers introducing TDA tools to a new domain.
- **"No treatment of high-dimensional activations"**: The paper clearly explains (Section 2.3) that activations are stored in an M×N array where M = number of test images and N = number of neuron activations; k-means++ clusters the N activations into 1000 groups. This is adequately described.
- **"The claim about first-time use of Betti curve similarity for DNNs"**: Whether this is true is a factual claim that cannot be verified without complete literature knowledge. The paper should be evaluated on the method and evidence, not on priority claims.

Strength Finder points removed:
- **"Spearman correlation choice is a strength"**: This is a standard, sensible design choice, not an exceptional strength worth highlighting.
- **"Large-scale, reproducible experimental design"** (in the general sense): The praise for scale is somewhat inflated — 30 subsets of 10 classes each is moderate, not large-scale.

## Novel Insights

The Harsh Critic and Strength Finder largely agree on the paper's core issues (unvalidated reduction, missing baselines, qualitative-only results) but differ in severity assessment. The Critic correctly identifies that the k-means++ reduction with poor silhouette scores is the paper's most vulnerable point — this resonates because the paper itself flags the poor separation without seeming to recognize how much damage it does to its own case. An interesting observation that neither reviewer explicitly captures: the paper's best evidence (subset 27, where Betti similarity groups models differently from accuracy) is actually the one result least damaged by the k-means concern, because it is a within-reduction comparison — if the reduction systematically distorts topology, the distortion would apply similarly across models, so relative comparisons between models on the same subset could still be meaningful. The more problematic claims are the temporal ones (e.g., "convergence towards the same global structure"), where absolute changes in Betti curves over training epochs could easily be artifacts of how k-means++ behaves differently on early versus late activation distributions.

## Suggestions

1. **Validate the k-means reduction.** Select a small network where the full activation set is small enough for exact PH computation. Compare Betti curves from full and reduced sets to establish that the reduction preserves relative topological structure across models and epochs. Even a single small-scale validation would substantially strengthen the paper.

2. **Add baseline comparisons.** Compute CKA, cosine similarity between mean activations, or SVCCA on the same data and show whether Betti curve similarity provides information these measures do not. This is essential for establishing the value proposition of TDA.

3. **Replace qualitative descriptions with quantitative evidence.** Report means and variances of similarity scores across the 30 subsets. Compute the correlation between pairwise Betti curve similarity and pairwise accuracy difference. A permutation test for whether cross-architecture similarities are systematically lower than within-architecture similarities would add rigor.

4. **Reposition the paper as a preliminary investigation.** The current framing ("can be a useful tool") overclaims given the evidence. A more accurate framing would acknowledge the unvalidated reduction and present the results as suggestive patterns that warrant further investigation with proper controls.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| xA25Ib7H8U (Ricci flows, continuous-depth networks) | 2.33 | 1 | Weaker — speculative theory without working experiments |
| 7pIxS9m283 (WISE-GNN) | 3.00 | 1 | Weaker — limited empirical scope |
| A9yKCUQNnc (Low-dim representation & generalization) | 3.00 | 1 | Similar weakness profile but different subfield |
| G2Lnqs4eMJ (NN approximation) | 2.50 | 1 | Weaker — purely theoretical with thin contribution |
| **NiCSyYOfex** (Node-Level Topological Rep. Learning) | 5.33 | 1 | **Stronger** — clearer contribution, more rigorous experiments |
| **QMQBza9BCx** (PH for high-dim data via spectral methods) | 4.50 | 1,2 | **Somewhat stronger** — has methodological gap (outlier problem) but clearer novel contribution |
| **RKXcTwWqVa** (ECLayer) | 5.20 | 1,2 | **Stronger** — more extensive experiments, clear utility |
| **sq5gkjC9jv** (Topological Expressive Power of ReLU NNs) | 5.67 | 1,2 | **Stronger** — substantive theoretical results |
| EzjsoomYEb (Topological Blindspots) | 8.00 | 1 | Much stronger — rigorous theoretical analysis |
| dLrhRIMVmB (TDA on noisy quantum computers) | 8.00 | 1 | Much stronger — complete, validated pipeline |
| **FE7PY7e4tr** (NN Expressive Power via Manifold Topology) | 5.25 | 2 | **Stronger** — meaningful theoretical bound with experiments |
| **L7gyAKWpiM** (Theoretical Study of NN Expressive Power) | 5.80 | 2 | **Stronger** — sound theoretical framework |
| X6y5CC44HM (MANTRA) | 5.75 | 2 | Stronger — large-scale benchmark contribution |

**Round-1 bracket:** The paper clearly sits above the 2–3 anchors (which have fundamentally broken or near-broken contributions) and clearly below the 5+ anchors (which have clearer contributions, more rigorous evaluation, or substantive theoretical results). Initial bracket: 3.5–5.0.

**Round-2 narrowing:** Inspecting the mid-range anchors (QMQBza9BCx at 4.50, RKXcTwWqVa at 5.20, FE7PY7e4tr at 5.25) shows these papers all have identifiable weaknesses but also possess either a clear novel contribution (spectral distances for PH, ECLayer architecture, network size bounds) or more rigorous experiments. Our paper is weaker on both counts: the contribution is essentially "applying an existing tool to a new domain" and the empirical validation is thin. The paper is closer to the 3.5–4.0 end of the initial bracket. The closest comparator is QMQBza9BCx (4.50) — both have a significant methodological concern — but that paper has a stronger novelty claim (novel distance measures + closed-form expression) and more thorough experiments. Our paper trails it.

**Final score:** The paper has a clear framework, reasonable scope, and one genuinely interesting observation (subset 27), but the unvalidated k-means reduction, absence of baseline comparisons, and purely qualitative evidence are significant limitations that prevent it from competing with papers in the 4.5+ range. It is above a flat reject (2–3) because the pipeline is sound in principle and the code/data are available for extension, but it is well below the acceptance threshold for ICLR.

**MY FINAL SCORE:** 4.0
**MY FINAL DECISION:** Reject