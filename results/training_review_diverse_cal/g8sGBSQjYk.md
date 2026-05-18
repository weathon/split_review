Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper extends the maximal update parameterization (μP) framework to second-order optimization methods, specifically K-FAC and Shampoo. It derives scaling rules for initialization, learning rates, and damping terms that ensure feature learning in the infinite-width limit, provides a trace-based damping rescaling for K-FAC, identifies an implicit bias of K-FAC toward the NNGP solution under zero initialization, and empirically validates that the proposed parameterization enables hyperparameter transfer across widths and consistent "wider is better" performance.

## Strengths

1. **Novel derivation of μP for second-order methods.** The paper is the first to extend μP — previously limited to SGD, Adam, and entry-wise optimizers — to K-FAC and Shampoo. Proposition 4.1 and Table 1 provide explicit, grounded scaling rules for initialization (b_l), learning rates (c_l), and damping exponents that ensure feature learning in the infinite-width limit. The derivation is anchored in the push-through identity, which reduces width-dependent preconditioners to width-independent expressions.

2. **Identification of width-independent learning rates for K-FAC.** A key finding is that K-FAC under μP requires constant learning rates across widths (c_l=0 for hidden layers), unlike SGD (c_l=0 for hidden layers but c_1=-1, c_L=1) and Shampoo (c depends on width). This is theoretically derived from the push-through analysis and empirically confirmed across MLPs, CNNs, and ResNets (Figures 3–5), where optimal learning rates remain fixed across widths under μP while they shift under standard parameterization.

3. **Proposed rescaled damping for K-FAC.** The paper identifies that existing K-FAC damping heuristics satisfy μP conditions in hidden layers but fail in input/output layers, causing updates to decay with width. The proposed trace-based rescaling (Equation 7) resolves this, satisfying valid damping scaling universally, and is shown experimentally (Figures 1, 5) to enable damping transfer across widths.

4. **Empirical validation across multiple architectures, datasets, and methods.** The paper demonstrates hyperparameter transfer and "wider is better" consistently across MLPs, CNNs, VGG19, ResNet18, ResNet50, CBOW, on CIFAR-10, CIFAR-100, FashionMNIST, WikiText-2, and ImageNet, using both K-FAC and Shampoo. Table 3 shows μP outperforming SP at large widths across architectures; Figures 3–5 show learning rate and damping transfer.

## Weaknesses

### Major

None that threaten the paper's core claims. The theoretical derivations are sound for the one-step setting, and the empirical validation is extensive.

### Minor

1. **One-step-to-multi-step theoretical gap is acknowledged but the paper overstates its guarantee.** The μP conditions are derived from a one-step analysis of the second-order update. The paper claims (line 222) that "this is the same as in the original work on μP where the one-step update determines the μP for the whole (inductive) t-step updates." However, the original μP work relied on the Tensor Program to formally extend the one-step result to the full training trajectory, and the paper itself notes (line 515) that "Tensor Program... is currently not applicable to the second-order parameterization." The sentence at line 222 gives the impression of a theoretical guarantee that has not been established for second-order methods. The empirical validation partially fills this gap, but the paper should more carefully distinguish what is proven (one-step) vs. empirically observed (multi-step). This does not undermine the practical value of the scaling rules, but the framing should be more precise.

2. **The implicit NNGP bias claim is partially supported but the evidence is indirect.** The paper mathematically shows (Equations 18–19) that a single K-FAC update with zero-initialized last layer yields the NNGP solution. However, the claim that K-FAC with large b_L "converges to" and "does not deviate from" this solution during multi-step training is supported only by accuracy degradation (Table 2, Figure 2), not by direct measurement. The paper does not report the NNGP predictor's test accuracy on the same task, nor does it measure the distance (e.g., parameter distance, output distance) between the trained model and the NNGP solution over time. The observation is suggestive and interesting, and the mathematical derivation of the one-step result is sound, but the multi-step "implicit bias" claim would be substantially strengthened by a more direct comparison. The paper should either provide such evidence or frame the claim more cautiously (e.g., "suggestive of an implicit bias").

3. **The fixed learning rate used in Table 3 (VGG19/ResNet experiments) is not sufficiently specified.** The caption states "The learning rate is set slightly small to enlarge the effect of infinite width" (line 421) without stating the specific value or tuning strategy. While the paper provides other experiments (e.g., Figure on ResNet50/ImageNet) showing robustness across learning rates, the lack of specificity here is a reproducibility concern. The description is too vague to allow reproduction or to assess whether the comparison between SP and μP is made at a fair operating point for both parameterizations. The paper also mixes framing: the caption claims μP achieves "higher accuracy" but the setup (deliberately small LR) is designed to demonstrate a *robustness* advantage (SP degrades, μP does not), not necessarily optimal accuracy for either. Clarification is needed.

### Trivial

- **SGD as e=0 case in Table 1:** Including SGD (e=0) as a special case of the preconditioner exponent framework is natural and demonstrates unification, but the paper does not explicitly explain this connection. A brief justification would help readers.
- **Push-through identity derivation sketch:** The derivation from the first to second line of Equation (4) uses the push-through identity to eliminate width-dependent matrices, but the intermediate steps involving δ, χ, and the mapping to the resulting conditions are not explained in the main text. The paper calls this a "rough sketch" and defers to the appendix, which is acceptable for a conference paper within page limits, but the main text could be slightly more self-contained.
- **Choice of trace for damping rescaling:** The paper proposes trace-based damping (Equation 7) but does not discuss why the trace is the appropriate statistic versus alternatives (e.g., maximum eigenvalue). The choice is reasonable and computationally convenient, but a brief justification would help.

## Nice-to-Haves

- Directly compute the NNGP predictor's test accuracy for the architectures/datasets used in Section 4.3 and show that K-FAC with b_L=64 converges to it, or measure the distance to the NNGP solution over training. This would elevate the implicit bias finding from suggestive to well-supported.
- Provide explicit theoretical intuition for why the preconditioner scaling should remain width-consistent across steps (e.g., why the preconditioner update is lower-order in width), or clearly delineate what is proven vs. empirically observed.
- Discuss potential modifications needed for attention layers in Transformers, since K-FAC's preconditioner structure differs for attention.

## Removed Points

- **Criticism about "missing appendix, missing proofs" (harsh critic's general concern):** The parser strips these sections; they exist in the original submission. Removed per instructions.
- **Criticism about "dataset availability/reproducibility due to unreleased models":** All models, benchmarks, and datasets referenced are cited and exist. Removed per hard rules.
- **Claims of missing related work:** Removed per instructions — this would require external verification.
- **Generic formatting/style nitpicks:** Removed per instructions.
- **Criticism about Figure 2 being "only for a specific dataset and architecture":** This is true of all empirical results. A single demonstration of the curvature order stability is sufficient as a sanity check. Removed as an unreasonable demand.
- **Complaint about CNNs being "empirically validated but not derived":** The paper honestly acknowledges this limitation. This is a reasonable scope note, not a weakness. Removed.
- **Suggestion to "discuss relationship to lazy regime parameterization":** The paper references this and states lazy regime parameterization is discussed in an appendix section. Removed as already addressed.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface a genuinely novel insight that the authors themselves have not already articulated. The interaction between the one-step derivation and the difficulty of applying Tensor Programs to second-order methods is the main unresolved theoretical question, and the paper already acknowledges this in its conclusion.

## Suggestions

1. **Sharpen the multi-step framing in Section 4.1.** Replace the sentence "This is the same as in the original work on μP where the one-step update determines the μP for the whole (inductive) t-step updates" with a more precise statement: "The μP conditions are derived from a one-step analysis following the original μP approach. While the original work formally extended this to the full trajectory via Tensor Programs, that tool is not currently applicable to second-order methods (see Section 6). We empirically validate that the scaling rules remain effective throughout training in Section 5."
2. **Strengthen the NNGP bias experiment (Section 4.3).** Compute the NNGP predictor's test accuracy for the same architecture and dataset, and either (a) show that K-FAC with b_L=64 achieves similar accuracy, or (b) measure and report the distance (e.g., MSE in output space) between the trained model and the NNGP solution over training steps. If this is computationally prohibitive, reframe the claim as "suggestive of an implicit bias" rather than a validated finding.
3. **Clarify the experimental protocol for Table 3.** State the specific learning rate value used for each architecture, how it was selected, and whether it was tuned on the narrow model. If the intent is to demonstrate robustness rather than optimal performance, state this explicitly.
4. **Add a brief explanation of why SGD appears as e=0 in Table 1** — i.e., that e=0 corresponds to no preconditioning, recovering a first-order gradient update, and that the resulting (b,c) values match known μP for SGD.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>