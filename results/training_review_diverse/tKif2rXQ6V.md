Now I have all the evidence needed. Let me synthesize the review.

## Summary

This paper introduces SteBen, a large-scale benchmark for the Steiner Tree Problem (STP) containing 1.28 million optimally solved instances across four graph models (ER, WS, RR, Grid) with node sizes ranging from 10 to 1000. The benchmark supports both supervised and reinforcement learning paradigms, and the paper implements and evaluates four classes of NCO methods (autoregressive/non-autoregressive × SL/RL) adapted for STP, along with classical baselines (SCIP-Jack, 2-approximation). The paper claims that NCO solvers trained on SteBen generalize to real-world instances without fine-tuning.

## Strengths

- **Large-scale, diverse dataset filling a clear gap.** SteBen provides 1.28M optimally solved STP instances across four distinct graph models with node sizes 10–1000, whereas existing STP benchmarks like SteinLib offer only a few dozen instances per scenario (Sections 1, 4.1). This scale enables training of neural models that were previously infeasible for STP.

- **First systematic comparison of NCO paradigms on STP.** The paper implements four distinct methodological classes (autoregressive SL, non-autoregressive SL, autoregressive RL, non-autoregressive RL) adapted for STP, including modifications to PtrNet (level-order traversal, distance-based priority, GNN embeddings), DIFUSCO (edge feature initialization), and DIMES (embedding/decoding) (Section 4.2). This establishes a structured baseline for future NCO research on STP.

- **Insightful analysis of STP's unique structural properties.** Figure 1 and the accompanying discussion (Section 3.2) illustrate how small perturbations in STP cause large changes in optimal solution structure, contrasting with TSP and motivating why dedicated STP benchmarks and methods are needed.

- **Identification of the tail-recursive property mismatch.** The paper explains that STP lacks the tail-recursive property of routing problems, which prevents direct application of recent SOTA autoregressive SL methods like LEHD and BQ-NCO (Section 4.2). This is a novel, problem-specific insight that guides future method design for STP.

- **Sample efficiency analysis.** The Discussion (Section 6, Figure 2) analyzes how supervised methods degrade with reduced training samples, showing that DIFUSCO is more robust under limited data but has a steeper relative decline from peak performance compared to PtrNet. This offers actionable guidance for researchers working under data constraints.

## Weaknesses

### Fatal
None.

### Major
None. The core contribution — the SteBen dataset itself — is described in sufficient detail to be assessable. The most severe concerns raised by reviewers are attributable to parser-induced extraction failures rather than genuine omissions by the authors.

### Minor
- **Edge cost distribution parameters unspecified.** Algorithm 1 and the description (Section 4.1) reference a truncated Gaussian \(\mathcal{N}(\mu,\sigma^2)\) for edge costs with truncation \([1, 2^{16}]\), but never specify the values of \(\mu\) and \(\sigma\). While reasonable values could be inferred, these should be explicitly stated for full reproducibility.

- **Real-world instance generalization claim lacks documentation in visible text.** The abstract and contributions list state that "NCO solvers trained on SteBen generalize well to real-world instances without additional fine-tuning." However, no description of the real-world instances (source, size, characteristics, or results) appears in the visible portions of the paper. If this information resides in the (parser-stripped) Results section, it should additionally be present in the dataset description or experimental setup.

- **Baseline adaptations described without validation.** The modifications to PtrNet, DIFUSCO, and DIMES (Section 4.2) are described at a reasonable conceptual level, but no ablation or analysis is provided to isolate the effect of each modification. For a benchmark paper, the baselines serve as reference points rather than novel contributions, so this is not fatal — but a brief validation (e.g., showing that the adapted versions outperform naive baselines) would strengthen confidence in the comparisons.

### Trivial
- Section 3.1 contains a paragraph (lines 80–81) that restates the motivation for datasets almost verbatim from the introduction. This redundancy does not affect soundness but indicates hurried writing.

## Nice-to-Haves
- Provide per-graph-type and per-node-size breakdowns of test instances.
- Include a brief ablation or sanity check for the baseline adaptations (e.g., comparing adapted PtrNet against a version without GNN embeddings or level-order traversal).
- Document the source and characteristics of the real-world instances used in the generalization experiment, even if briefly.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Entire Section 5.2 (Results) described as missing.** The section header exists at line 166; the content (tables, figures) was stripped by the PDF-to-text parser. The Discussion section references Table 1 and Figure 2, confirming that results were present in the original submission. This is a parser extraction failure, not a paper flaw.
- **Criticism about the 1.28M / 1M / 280K split relationship.** The paper clearly states "1 million training set and a 280,000 validation set" (1M + 280K = 1.28M), with test instances (10,000 + 500) being separate. The reviewer's arithmetic was incorrect.
- **"Excluding improvement methods is not justified."** The paper explicitly states (Section 1) that the benchmark focuses on constructive solvers "given the importance of generating solutions efficiently with minimal prior knowledge," which is a reasonable scope choice for a benchmark paper.
- **Complaint about "Cherrypick" decoding being referenced without explanation.** The method is cited to Yan et al. (2021), which is standard practice; full re-description of a cited method is not required.
- **Request for hyperparameters and training details.** The paper provides the hardware setup (8×3090 GPUs), dataset splits, evaluation protocol (greedy + 32 samples), and metrics. Specific hyperparameters are standard implementation details typically documented in released code, not essential for assessing the benchmark contribution.
- **"Level-order representation not uniquely defined for weighted graphs."** The paper describes a concrete adaptation (level-order tree traversal, distance-based priority, GNN embeddings). The representation is well-defined in the context of the authors' decoding procedure; the reviewer's objection is speculative without evidence of a concrete flaw.
- **Generic/gap-filling strengths from the strength finder:** None of the strengths were generic — all had specific supporting evidence from the paper.

## Novel Insights

The most notable insight that emerges across the reviews (beyond the paper's own contributions) is that the structural complexity of STP — specifically the non-tail-recursive solution space and the sensitivity to small perturbations — creates a fundamentally different learning landscape from routing problems like TSP. This suggests that NCO methods designed for routing problems may not transfer well to STP, and that the field may need problem-specific architectural innovations rather than generic adaptations. The sample efficiency analysis further suggests that in STP, the choice of learning paradigm (SL vs. RL) has different implications under data scarcity than in routing problems, where SL methods typically dominate when sufficient data is available.

## Suggestions
1. Add explicit values for \(\mu\) and \(\sigma\) in Algorithm 1 and the dataset description (Section 4.1).
2. Provide a brief characterization of the real-world instances — even two sentences about their source, size range, and number — in the Experimental Setup (Section 5.1) to support the generalization claim.
3. Add a short paragraph or table footnote validating the baseline adaptations, e.g., comparing the adapted PtrNet against a simpler decoder without level-order traversal on a small subset of instances.
4. Include a breakdown of test instances per graph type and node size to improve reproducibility.

## Score and Decision

The paper is a benchmark/dataset contribution, and the core deliverable — 1.28M instances across diverse graph models and sizes with optimal solutions — is well-described and fills a genuine gap in the NCO-for-STP literature. The visible weaknesses (unspecified distribution parameters, undocumented real-world instances, unvalidated baseline adaptations) are non-fatal documentation issues that can be addressed in a revision. The parser-stripped results section is not a genuine paper flaw. The taxonomy of NCO methods and the analysis of STP's structural properties add value beyond the dataset itself.

**Score:** 6.5 — A solid benchmark paper with a clear contribution. The dataset fills a real gap, the taxonomy is sensible, and the analysis is insightful. The documentation omissions are real but addressable.

**Decision:** Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>