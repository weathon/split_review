- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 6, 5, 1
Now I have all the information needed. Let me compile the final consolidated review.

## Summary

This paper proposes an architectural bias for unsupervised sequential disentanglement: the static posterior is conditioned on a single sequence element (e.g., the first frame), and the resulting static code is subtracted from LSTM hidden states that produce the dynamic factors. This design mitigates mode collapse without mutual-information loss terms or dynamic-dimension restrictions, reducing the objective to a standard β-VAE with only two hyperparameters (α, β). The method is evaluated across video (Sprites, MUG), time series (PhysioNet, ETTh1, Air Quality), and audio (Timit), achieving state-of-the-art results on multiple benchmarks.

## Strengths

- **Architectural bias eliminates mutual-information loss terms and reduces hyperparameters.** The posterior design (Eq. 4: conditioning static on a single element; Eq. 8: subtracting the static code from LSTM hidden states) removes the need for the three MI penalties used in prior work (Bai et al., 2021) and avoids constraining dynamic dimension (Li & Mandt, 2018). The objective has only two hyperparameters (α, β) as described in Section 4.

- **State-of-the-art quantitative results across multiple modalities.** On MUG video dataset, the model achieves 87.53% accuracy, IS=5.598, and H(y|x)=0.049, outperforming all prior methods (Table 1). On PhysioNet mortality prediction and ETTh1 forecasting, it surpasses every baseline including raw-feature training (Table 2). On Air Quality classification, it exceeds prior methods (Table 3).

- **Robustness to the choice of anchor sample is empirically validated.** Ablation experiments (Table 4, bottom) show that conditioning the static posterior on the first, middle, or last sample yields similar performance across PhysioNet, ETTh1, and MUG tasks. This directly addresses a natural concern about the single-sample assumption.

- **Failure-case analysis adds evaluation depth.** The paper provides a confusion matrix for MUG (Fig. 4) identifying systematic confusion between fear and surprise, explains this via visual similarity, and discusses implications for hierarchical disentanglement. This honest characterization strengthens the empirical contribution.

- **Simpler training objective than state-of-the-art alternatives.** Compared to methods balancing multiple MI loss terms (Bai et al., 2021) or requiring careful tuning of dynamic dimension (Li & Mandt, 2018), the proposed model uses only two hyperparameters, no contrastive estimation, and no domain-dependent data augmentation.

## Weaknesses

### Fatal

None.

### Major

None. The verified weaknesses are significant enough to warrant attention but do not threaten the paper's core claims.

### Minor

- **The subtraction mechanism is empirically validated but not analyzed mechanistically.** The paper shows that removing subtraction ("no sub") degrades performance (Table 4), but does not interrogate *what* the subtraction accomplishes. For example: does it remove all static-feature components from the dynamics, or also remove dynamic features correlated with the static code? Do s̃ and h̃_t (MLP output vs. LSTM hidden state) lie in a compatible representational space for subtraction? An analysis measuring residual static information in the dynamic codes (e.g., via a linear probe predicting a static attribute from d_t) would strengthen the claim that the architecture *mechanistically* prevents mode collapse rather than merely improving numbers through a heuristic.

- **No sensitivity analysis for the α hyperparameter.** The reconstruction loss (Eq. 5) weights x₁ separately with α, and the paper states "we typically obtain better results in practice when α≠1" without showing how α affects disentanglement quality or reconstruction fidelity. Since α directly controls how much information about x₁ must be captured by the static code s (because d₁=0), the trade-off deserves a sensitivity plot or at least an ablation across values.

- **Quantitative swap metrics are not reported.** The swap experiment on MUG (Fig. 3) is shown only qualitatively. Prior work in this area (C-DSVAE, SPYL) typically reports a quantitative metric (e.g., accuracy of a classifier on swapped sequences). Adding this would make the comparison fairer and more complete.

- **Baseline tuning fairness on time series tasks warrants more clarity.** The margin of improvement on time series tasks (Tables 2, 3) is large. The paper states "for a fair comparison, we use the same encoder and decoder modules for all baseline methods," but does not describe the hyperparameter tuning protocol (e.g., budget, range searched) for baselines versus the proposed method. Since baselines with multiple MI loss terms may require more careful tuning, reporting the tuning procedure would make the comparison more convincing. This is a concern about presentation completeness rather than a suspicion of foul play.

- **Failure modes of the single-sample assumption are not explored.** While the paper acknowledges this as a limitation and tests robustness to index choice, it does not probe scenarios where the anchor sample might be a poor representative (e.g., corrupted first frame, occlusion, noise). The claim that static features are "recoverable from a single sample" is treated as an inductive bias; discussing when it might break would improve the paper's rigor.

### Trivial

- None.

## Nice-to-Haves

- Provide a direct measurement of how much static information remains in dynamic codes after subtraction (e.g., train a linear classifier to predict subject identity from d_t with vs. without the subtraction module).
- Show a sensitivity plot of α across a range of values on at least one dataset to illustrate the trade-off in static/dynamic separation.
- Report a quantitative swap metric (e.g., expression classification accuracy on swapped sequences) to complement the qualitative examples in Fig. 3.
- Test the single-sample assumption on frames with synthetic corruptions (e.g., masking the first frame's informative region) to characterize failure boundaries.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Missing audio results in main text"** — Removed per hard rule: audio results and the Timit evaluation exist in the appendix (which the parser strips). The main paper lists Timit in the experimental setup (Section 5.1) and the conclusion references audio evaluation. The results are part of the original submission.
- **"No statistical significance reported / standard deviations"** — Removed per hard rule: the paper states "Results with standard deviation appear in Tab. 9" (line 155, referring to an appendix table stripped by the parser).
- **"No analysis of latent dimensionality sensitivity"** — Removed per hard rule: architectural details and hyperparameter choices (including latent dimensions) are described in the appendix (App. A.3, A.4), which was stripped.
- **"The paper does not present quantitative results for audio"** — Same as above; audio results are in the appendix.
- **Missing related works** — Per instructions, I cannot verify the existence of missing citations and should not mention them.
- **Formatting or style nitpicks** — None present in the inputs; any such issues would be parser artifacts.

## Novel Insights

The reviews surface an interesting tension: the paper's central idea—using an architectural bias (subtraction) rather than a loss-based penalty to enforce disentanglement—is praised as elegant and practical, yet the mechanism by which subtraction achieves this remains a "black box" even after reading the paper and ablations. The empirical evidence is strong (ablation shows subtraction matters), but the community would benefit from understanding *why* subtractive coupling works better than, say, concatenating s as additional input to the dynamic encoder. The merged perspective reveals that the paper's key innovation (architectural bias over loss terms) is simultaneously its greatest strength (simplicity, fewer hyperparameters) and its most under-analyzed component (no mechanistic analysis of the subtraction). This gap is real but does not invalidate the contribution—it points to a natural next step for follow-up work.

## Suggestions

1. Add a short analysis probing the subtraction mechanism: measure the mutual information I_q(s; d_{1:T}) with and without the subtraction module, or train a linear probe to predict a static attribute from the dynamic codes. This would directly address the most substantive gap in the current manuscript.
2. Include a sensitivity plot for α (e.g., on the MUG or PhysioNet dataset) showing how accuracy or disentanglement metrics vary as α ranges from 0.1 to 10.
3. Add a quantitative swap metric (accuracy of a pre-trained classifier on swapped sequences) to the video experiments, consistent with prior work.
4. Clarify the hyperparameter tuning protocol for baselines on time series tasks: how many configurations were searched per method, and what were the final settings? This would preempt concerns about unequal optimization effort.
