Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper extends the maximal update parameterization (μP) framework — previously limited to first-order optimizers — to second-order optimization methods K-FAC and Shampoo. The authors derive scaling rules for initialization, learning rates, and damping terms that ensure stable feature learning (Δh_l = Θ(1)) in the infinite-width limit. Key theoretical findings include: (1) K-FAC permits constant learning rates across widths while Shampoo requires width-dependent scaling, (2) the standard damping heuristic for K-FAC violates μP conditions at input/output layers and needs rescaling, and (3) zero initialization of the last layer creates an implicit bias toward the NNGP solution specific to K-FAC. Experiments across MLPs, CNNs, ResNets, and a CBOW model show that μP enables hyperparameter (learning rate and damping) transfer across widths and yields better performance than standard parameterization (SP) at large widths.

## Strengths

- **First principled extension of μP to second-order optimization.** Proposition 4-1 derives explicit scaling rules for initialization exponents b_l, learning-rate exponents c_l, and damping exponents d_X for both K-FAC and Shampoo, generalizing a previously first-order-only framework. The derivation follows the established one-step analysis methodology and makes concrete, testable predictions — notably that K-FAC and Shampoo require qualitatively different LR scaling.

- **Discovery of the NNGP bias specific to K-FAC under zero initialization.** Section 4-3 identifies and provides theoretical grounding for a phenomenon where K-FAC's one-step update from zero-initialized last-layer weights yields the NNGP solution, and that escaping this solution is harder with large batches. This is a genuinely novel finding specific to second-order optimization and is supported by initial experiments (Table 1, Figure 5).

- **Empirical validation of hyperparameter transfer across widths.** Figures 7-8 demonstrate that under μP, the optimal learning rate and damping remain constant as width increases across MLP, CNN, and ResNet architectures, while under SP they shift. This directly validates the practical benefit claimed by the theory — practitioners can tune on small models and deploy on larger ones.

- **Practical rescaling of K-FAC damping.** Equation (8) proposes a trace-based damping rescaling that fixes the failure of the standard heuristic at input/output layers, and Figure 1 (third column) confirms this rescaling yields width-independent feature learning.

## Weaknesses

### Fatal
None.

### Major

- **The distinctive Shampoo prediction (width-dependent LR) is never directly validated.** The theory predicts that Shampoo requires width-dependent learning rates (c_1 = -1/2, c_L = 1/2 for e=1/2) while K-FAC works with constant LRs (c_l = 0). Yet all Shampoo experiments (Table 1, Figure 4) only compare the full μP recipe against SP — the two differ in multiple exponents simultaneously. There is no experiment that fixes all other exponents to their μP values and varies the Shampoo LR exponent c to confirm that the predicted scaling is genuinely required. Since this qualitative difference between K-FAC and Shampoo is one of the paper's headline theoretical claims, the lack of targeted validation weakens the central narrative.

- **The paper claims "the accuracy can be consistently improved by μP" (line 439) but the Shampoo results on VGG19 show μP underperforming SP at widths 1 and 2** (SP 63.86 vs μP 63.58 at width 1; SP 70.55 vs μP 69.89 at width 2). While the table caption correctly qualifies the claim to "large widths," the main text overstates the pattern. More importantly, the paper does not analyze or comment on these negative results — whether they reflect noise, a finite-width effect that reverses at larger widths, or a systematic issue with Shampoo's μP at small widths. The overall trend is positive at large widths, but the inconsistency warrants discussion.

### Minor

- **The one-step derivation is not verified to be sufficient for multi-step training, and the paper does not test whether intermediate exponent values would also work.** The paper follows the original μP methodology (one-step analysis → full training recipe), but unlike the original μP work, the Tensor Program framework for multi-step analysis is not available for second-order methods (as the paper acknowledges in the conclusion). The experiments only compare μP vs SP — two discrete points in a multi-dimensional exponent space. A simple ablation on, say, an MLP with K-FAC that varies a single exponent (e.g., c_l for one layer) while holding others fixed would demonstrate the predicted values are not just sufficient but necessary. Without this, the derivation is validated only coarsely.

- **The NNGP bias finding lacks depth in empirical characterization.** The experiment uses a single architecture (3-layer CNN), one dataset (FashionMNIST, reduced to 1024 samples), and full-batch/large-batch training. The paper states the accuracy gap shrinks with smaller batch sizes but does not characterize where the transition occurs or whether practical batch sizes (256–4096) are affected. The chosen b_L=64 proxy for zero initialization is extreme, and the practical relevance for standard large-scale training remains speculative. As this is highlighted as a "novel implicit bias," a broader characterization would strengthen the claim.

- **The rescaled damping for K-FAC is shown to enable HP transfer, but it is not compared against well-tuned heuristic damping at each width for final accuracy.** The practical advantage claimed is transferability — which is validated — but it would strengthen the paper to show that the accuracy achieved with the transferred μP damping is competitive with width-specific tuning of the heuristic. Without this, a reader might wonder if the heuristic, if tuned per width, could match or exceed μP's accuracy even without transfer.

- **The paper does not discuss whether the "same-batch" assumption (gradient and preconditioners computed on identical samples) is critical or how stale preconditioners might affect the conclusions in practice.** This is acknowledged as a standard assumption but its robustness is not addressed.

### Trivial
None.

## Nice-to-Haves

- An ablation on an MLP with K-FAC or Shampoo varying one exponent (e.g., c_1) across a few integer values while holding others at μP values, confirming the predicted optimum.
- A dedicated Shampoo experiment showing that constant learning rates (c=0) cause feature decay or worse performance at large widths, directly validating the K-FAC vs Shampoo distinction.
- Testing the NNGP bias on a more realistic architecture/dataset and quantifying the accuracy penalty at standard batch sizes.
- Showing that the training dynamics (e.g., loss curves) across widths are nearly identical under μP with fixed HPs, not just that the optimal HP is constant.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Figure 4 caption's claim that μP 'consistently achieves higher accuracy' is undermined by VGG19 Shampoo width 2."** Removed: Figure 4's caption is about ResNet50 on ImageNet, not about VGG19. The critic conflates two separate experiments. The VGG19/Shampoo results are in Table 1, whose caption correctly qualifies the claim to "large widths."

- **"The valid damping condition is self-imposed and excludes other possibilities."** Removed: The paper explicitly acknowledges this (lines 224-225) and explains why other damping scalings reduce to first-order behavior. The critic restates what the paper already addresses.

- **"The one-step derivation does not guarantee conditions hold throughout training."** Downgraded from the critic's framing: The paper acknowledges this gap (line 515) and follows the same methodology as the original μP work. It is standard in the μP literature to use one-step analysis to derive scalings and validate empirically for t>1. This is a known limitation, not a flaw. The remaining valid kernel is captured in the Minor weakness about missing ablation.

- **"Could not verify Appendix content/derivations."** Removed per instructions: parser strips appendices; they exist in the original submission.

## Novel Insights

Beyond the paper's own contributions, the reviews collectively surface an interesting tension: the paper's theoretical framework makes a strong, testable prediction about a qualitative difference between K-FAC and Shampoo (constant vs width-dependent LR scaling), yet the experimental design never specifically targets this prediction. This creates a gap between the paper's strongest theoretical selling point and its empirical coverage. The broader lesson is that for theory papers making *comparative* predictions (method X requires Y while method Z does not), validation should target the predicted difference directly, not just verify that the full recipe works. A good-faith reader of this paper could accept that "μP helps second-order optimization" while remaining unsure about the specific mechanistic claim that distinguishes K-FAC from Shampoo.

## Suggestions

- Add a targeted Shampoo experiment (e.g., on an MLP or small CNN) that fixes all exponents to their μP values except c_1 (input LR exponent), varies it across values like -1, -1/2, 0, +1/2, and shows that the predicted c_1 = -1/2 gives the best scaling of Δh_l or most stable learning. This would directly validate the distinctive Shampoo prediction.
- Acknowledge and discuss the negative Shampoo results at small widths on VGG19 (Table 1), even if only to note they are finite-width effects that reverse at larger widths.
- Broaden the NNGP bias characterization with at least one additional architecture or realistic batch-size setting, or temper the claim to match the current evidence.
- For the damping claim, add a comparison showing test accuracy under transferred μP damping vs individually-tuned heuristic damping at each width.

## Score and Decision

The paper makes a genuine contribution by extending the μP framework to second-order optimization — a timely and practically relevant problem as second-order methods are applied to larger models. The theoretical derivation is principled and yields concrete, falsifiable predictions. The empirical work covers multiple architectures, datasets, and optimizers, and the HP transfer results are compelling for K-FAC. However, the paper's strongest comparative prediction (K-FAC vs Shampoo LR scaling) is not directly tested, and a few claims are slightly overbroad relative to the evidence. These issues are addressable and do not undermine the core contribution, but they limit the paper's conclusiveness in its current form.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>