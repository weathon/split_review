## Summary
This paper identifies a phenomenon called "model collapse" in Deep CCA methods, where performance drops drastically as training proceeds. It proposes NR-DCCA, a noise regularization approach that constrains neural networks to be Correlation Invariant (CIP) — i.e., the correlation between data and random noise should be approximately invariant under the encoder transformation. Theoretical analysis shows CIP is equivalent to full-rank weight matrices for linear/square transformations. Experiments on synthetic datasets with controllable common rates and three real-world datasets show NR-DCCA achieves stable, competitive performance. A synthetic data generation framework is also introduced.

## Strengths
- **Identification and empirical characterization of model collapse in DCCA**: The paper provides the first systematic study of this phenomenon. Figure 1 shows eigenvalue decay of weight matrices at epochs 100 vs. 1200, and Figure 5a shows performance trajectories on synthetic data, both demonstrating that DCCA-based methods suffer from performance degradation over training while NR-DCCA is stable.

- **Synthetic data generation framework with controllable common rate**: The construction of multi-view synthetic datasets (Section 6.1, Definition 1) where the overlap of features from a "God Embedding" is parameterized by a common rate is a principled and reusable benchmark. It allows systematic testing of MVRL methods across different levels of view correlation.

- **NR-DCCA achieves stable and competitive performance on both synthetic and real-world data**: On synthetic data across common rates (Figure 5a), NR-DCCA avoids the collapse seen in DCCA/DCCAE/DCCA_PRIVATE and retains stable accuracy. On real-world datasets (PolyMnist, CUB, Caltech — Figure 6), NR-DCCA achieves competitive or best F1 scores, demonstrating practical utility.

- **Theoretical link between CIP and full-rank matrices is rigorously established for the linear case**: Theorem 1 proves that CIP (correlation invariance w.r.t. noise) ⟺ full-rank square matrix W_k. Theorem 2 connects full-rank weights to low reconstruction/denoising loss. These results provide clear theoretical intuition, even if their scope is limited (see Weaknesses).

## Weaknesses
### Fatal
None.

### Major
- **Theory-practice gap: Theorem 1 is proven for a single square linear matrix, but the method uses deep nonlinear encoders.** Theorem 1 (line 228) explicitly assumes "W_k is a square matrix" and concerns a single linear transformation. The method, however, applies the NR loss to the output of a deep, nonlinear encoder \(f_k\) (MLP with ReLU). The paper states "By forcing \(f_k\) to possess CIP and thus mimicking the behavior of Linear CCA, the NR approach constrains the weight matrices to be full-rank" (line 232), but this reasoning is intuitive/heuristic, not a proof. No argument is given that CIP for a deep nonlinear network implies full-rank weight matrices in every layer, nor under what conditions a nonlinear function inherits CIP from its components. This is not fatal — the method can stand on empirical validation — but the theoretical framing overreaches by presenting the theorem as a justification for the deep method without bridging this gap.

- **Model collapse is not empirically demonstrated on real-world datasets.** The paper defines model collapse as "performance of DCCA-based methods will drop drastically when training proceeds" (line 26), a temporal phenomenon. On synthetic data, this is shown via training trajectories (Figure 5a). However, on real-world data (Figure 6), only **final** F1 scores are reported — no performance-vs-epoch plots. The paper then states "DCCA-based methods exhibit varying degrees of collapse on various datasets" (line 376) based on this figure. A bar chart of final performance cannot distinguish between a method that collapsed during training and one that was simply poor from the start. This weakens the evidential link between the claimed phenomenon and the real-world experiments.

- **Claimed generalizability to DGCCA is experimentally unsupported.** The abstract (line 7), introduction, and conclusions (line 392) state that the NR approach "can also be generalized to other DCCA-based methods such as DGCCA." Yet no experiment with NR-DGCCA (or any DCCA variant other than NR-DCCA) is reported. If the method is presented as a pluggable module, at least one demonstration on another DCCA variant is needed to substantiate this claim.

### Minor
- **Hyperparameter \(\alpha\) is not reported.** The NR loss weight \(\alpha\) is introduced (line 209-211) but its value across experiments is not stated. This makes the results harder to reproduce and leaves the sensitivity of the method to this parameter unclear. An ablation would strengthen the paper.

- **No comparison against explicit rank-promoting regularizers.** The paper hypothesizes that low-rank weight matrices cause collapse but does not compare against standard regularizers that directly penalize low rank (e.g., weight decay, orthogonality regularization). This is acknowledged as future work (line 395), but including at least one such comparison would strengthen the claim that CIP-based regularization is specifically effective rather than generic regularization helping.

- **Figure 5a caption and x-axis ambiguity.** The caption reads "performance across synthetic datasets in different training epochs," which suggests the x-axis is epochs. However, the figure filename ("Syn_rate") and the surrounding text's focus on common rates may create ambiguity. The paper should explicitly label the x-axis in the caption or text.

### Trivial
- Line 362: "mean value pf Reconstruction" contains a typo ("pf" → "of").

## Suggestions
1. **Reframe the theoretical contribution** as providing *motivation and intuition* for why CIP should prevent collapse, rather than presenting it as a proof that applies directly to deep nonlinear networks. Alternatively, discuss conditions under which the linear result extends (e.g., injective activations, residual connections).
2. **Add training trajectory plots** on at least one real-world dataset (e.g., PolyMnist-5views) showing F1/R² vs. epoch for DCCA, DCCAE, DCCA_PRIVATE, and NR-DCCA.
3. **Run NR-DGCCA** on synthetic data for one common rate and one real dataset to support the generalizability claim.
4. **Report \(\alpha\) values** used in all experiments and ideally include a sensitivity analysis.
5. **Clarify Figure 5a's x-axis** in the caption (explicitly state "Epoch" or "Common Rate").
6. **Fix the typo** on line 362.

## Score and Decision

The paper makes a genuine contribution by identifying the model collapse problem in DCCA and proposing a simple, empirically effective solution (NR-DCCA). The synthetic benchmark is a useful auxiliary contribution. However, the theoretical analysis is decoupled from the actual method (proven for linear/square but applied to deep/nonlinear), the central phenomenon is not demonstrated on real-world data with temporal plots, and the generalizability claim is unsupported by experiments. These are significant gaps but all can be addressed with additional experiments and a reframed theoretical discussion. The core method is sound and shown to work well empirically.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
