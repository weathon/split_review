Now I have a thorough understanding of the paper and can produce the final consolidated review.

---

## Summary

FedOD introduces the first federated learning system for classical (non-neural) outlier detection algorithms. It decomposes OD algorithms into shared basic operators (convex, non-convex, and simple), approximates each operator with a neural network, and trains those networks via FedAvg using local loss functions that require no cross-agent data sharing. The paper evaluates five diverse OD algorithms (kNN, LOF, PCA, CBLOF, iForest) across 21+ datasets, reporting less than 5% ROC-AUC difference from the ground truth (centralized) baseline and up to 11× error reduction over running OD independently per agent.

## Strengths

- **First FL system for classical OD algorithms.** The paper directly addresses a well-known limitation: classical OD algorithms (distance-based, density-based, tree-based) involve inter-sample data dependencies that make them incompatible with existing FL frameworks. FedOD's neural approximation approach fills this gap in a principled way (Abstract, Section 1, Section 7).

- **Well-designed operator decomposition framework.** The paper systematically decomposes 20+ OD algorithms into a small set of recurring basic operators categorized by convexity (convex, non-convex, simple). This decomposition is demonstrated concretely for kNN, ABOD, and LOF (Figures 1, 3, 4) and enables reuse: each operator's neural approximator is designed once.

- **Strong empirical accuracy.** Across five diverse OD algorithms and 21+ datasets, FedOD achieves less than 5% ROC-AUC difference from the ground truth (centralized execution), outperforming the direct (per-agent) baseline by up to 11× on kNN (Section 5.2, Appx. Table C3). These results hold across distance-based (kNN), density-based (LOF), linear (PCA), clustering-based (CBLOF), and tree-based (iForest) methods.

- **Empirical robustness to model architecture choices.** Ablation studies show performance variance under 3% across different hidden-layer sizes and depths (Section 5.4.1, Figure 6). The paper also compares MLP vs. Transformer backbones, finding MLP simpler, faster, and often more accurate (Section 5.4.2).

- **Practical efficiency gains.** FedOD delivers up to 10× inference speed-up on larger datasets for CBLOF and iForest (Section 5.3, Figure 5) and provides anytime inference capability (Section 4.3).

## Weaknesses

### Fatal
None.

### Major

- **Missing critical FL experimental details.** The paper does not specify the number of agents (K), the data partitioning strategy (i.i.d. vs. non-i.i.d.), or the number of communication rounds (T) used in the experiments. For a paper whose core claim is enabling global OD under FL, these parameters are essential: the results are substantially easier to achieve under i.i.d. partitioning where each agent's local distribution approximates the global one, and harder under non-i.i.d. partitioning where outlier prevalence varies across agents. Without this information, the reader cannot assess whether the reported 5% gap to ground truth reflects genuine cross-agent learning or favorable experimental conditions.

- **No communication cost analysis.** Communication efficiency is a standard evaluation dimension for FL systems. The paper provides no discussion of the number of rounds needed for convergence, per-round communication volume, or how these scale with the number of agents. This is a significant omission for a system that claims to enable FL-based OD.

### Minor

- **No theoretical analysis of the approximation gap.** The paper relies on the Universal Approximation Theorem to justify neural approximation but provides no analysis of when or why local loss functions suffice to recover the global operator's output. The core conceptual challenge—that an operator like kNN on the global dataset depends on cross-agent pairwise distances, yet the neural network only sees local distances during training—is addressed solely through empirical validation. While the empirical evidence is reasonably strong (<5% gap), a theoretical characterization of the approximation error would significantly strengthen the contribution, especially for cases where data distributions across agents are highly heterogeneous.

- **Limited empirical breadth relative to claimed scope.** The paper claims support for "over 20 popular classical OD algorithms" but experimentally validates only five. While the decomposition framework (Figure 4) plausibly generalizes, and the reviewer notes this is acceptable for a system paper, the gap between claimed and demonstrated scope remains notable.

### Trivial
- Minor inconsistency: the abstract states "more than 30 benchmark and synthetic datasets" while Section 5.1 mentions "over 21 real-world OD datasets" (synthetic datasets are presumably in the stripped appendix).

## Nice-to-Haves
- An experiment explicitly varying the number of agents K (e.g., 2, 5, 10, 20) to show how performance degrades with increased fragmentation.
- Evaluation under controlled non-i.i.d. partitions (e.g., one agent contains all outliers, another contains none) to stress-test the cross-agent dependency claim.
- Reporting communication rounds needed for convergence and total communication volume.

## Removed Points
These points were flagged by reviewers but are removed with justification:
- **"Method not reproducible because local loss functions aren't specified"** — The paper states "We design a local loss function For each supported operator in FEDOD" (line 145). The detailed loss functions are in Appendix B, which was stripped by the parser but exists in the original submission. Per policy, criticisms of missing appendix content are removed.
- **"Claim of 'first FL system for diverse OD algorithms' is misleading"** — The paper is transparent about using neural approximation to bridge classical OD with FL. The contribution is clearly scoped; this is a semantic nitpick.
- **"Anytime inference is not novel"** — This is a stated practical advantage, not a core claim of novelty.
- **"10× speed-up is just replacing classical with NN"** — That is precisely the paper's design; it is not a weakness.
- **"Convexity discussion is unused"** — The paper uses convexity to explain the empirical observation that PCA (convex) shows lower performance variance than LOF/iForest (non-convex) in Section 5.2.
- **"Only tests 5 of 20+ algorithms"** — The reviewer themselves notes "That is acceptable for a system paper." The decomposition framework (Figure 4) shows all supported algorithms follow the same pattern.

## Novel Insights

The harsh reviewer's core conceptual objection—that neural networks trained on local data cannot capture cross-agent dependencies because the local loss only sees local pairwise distances—is the most interesting tension in the paper. The paper resolves this tension empirically (the 5% gap to ground truth) but never theoretically, which means the method's applicability to highly heterogeneous FL settings remains an open question. The strength finder correctly identifies that the empirical results are the single most important piece of evidence. A genuinely novel insight would require understanding why FedAvg is able to align the neural approximators across agents such that the central model produces global-like outputs despite each copy training on only a subset of the data—but neither the paper nor the reviews provide this analysis.

## Suggestions

1. **Specify the FL setup explicitly** in a revision: number of agents K, data partitioning strategy (i.i.d. vs. skewed), number of communication rounds T, and the convergence criterion. This is the single most impactful improvement the authors can make.
2. **Add at least one non-i.i.d. experiment** where outlier prevalence varies across agents (e.g., Dirichlet-based partition by label). This would directly address the most serious concern about whether the method works when local data does not resemble the global distribution.
3. **Include a communication cost analysis**: report the total communication volume and number of rounds needed for convergence, which are standard metrics in the FL literature.
4. **Provide a brief intuitive argument** or simple bound for why the local loss + FedAvg combination can approximate global operator behavior, even if a formal proof is not feasible.

## Score and Decision

**Originality**: 4/5 — The neural approximation approach for classical OD under FL is novel.  
**Importance**: 4/5 — Privacy-preserving OD is practically important and the paper addresses a genuine gap.  
**Claims support**: 3/5 — Empirical support is strong, but missing FL experimental details weaken the core claim.  
**Soundness**: 3/5 — Approach is sound in principle, but incomplete experimental specification limits interpretability.  
**Clarity**: 3/5 — The main ideas are clear, but critical experimental parameters are absent.  
**Value**: 3.5/5 — Valuable contribution with potential, but needs stronger experimental validation to be fully convincing.

The paper proposes a genuinely novel approach to a well-motivated problem and provides reasonably strong empirical evidence. The main weakness is not a flaw in the method itself but incomplete specification of the FL experimental setup. These issues are addressable in revision.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>