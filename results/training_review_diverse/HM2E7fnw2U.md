Now I have all the information needed. Let me produce the consolidated final review.

## Summary

This paper proposes an architectural bias for variational sequential disentanglement: conditioning the static posterior on a single sample (an anchor) and subtracting the resulting static code from the LSTM hidden states in the dynamic path. This approach mitigates mode collapse without requiring mutual information loss terms or dimensionality constraints. The method is evaluated on video (Sprites, MUG) and time series (PhysioNet, Air Quality, ETTh1) benchmarks, showing state-of-the-art results on MUG generation metrics and on PhysioNet mortality prediction, supported by thorough ablation studies.

## Strengths

- **Simple, well-motivated architectural bias that effectively mitigates mode collapse without auxiliary losses.** Conditioning the static factor on a single sample and subtracting its code from the dynamic path hidden states (Eq. 8) directly enforces the static/dynamic separation. The ablation (Tab. 4) confirms the subtraction is crucial: removing it drops MUG accuracy by ~10% and degrades time-series prediction. This validates the core design choice empirically without requiring MI penalty terms, which the paper correctly identifies as difficult to tune and domain-dependent.

- **State-of-the-art results on multiple challenging benchmarks with fewer hyperparameters.** On MUG video, the method achieves 87.53% accuracy, IS=5.598, H(y|x)=0.049 (Tab. 1), outperforming prior works including SPYL and C-DSVAE. On PhysioNet mortality prediction, it achieves AUROC=86.3 and AUPRC=52.1 (Tab. 2), surpassing all baselines including raw features. These results are obtained with only two hyperparameters (α, β), compared to the three MI penalties in competing approaches.

- **Thorough ablation and robustness analysis.** Tab. 4 systematically ablates both the subtraction module and the additional static reconstruction loss across MUG, PhysioNet, and ETTh1. The same table also tests robustness to anchor index (first, middle, last sample), showing near-identical performance regardless of choice — directly addressing the natural concern about dependence on x₁.

- **Qualitative analyses provide insight into what the model learns.** t-SNE visualizations (Fig. 2) show clean separation between static and dynamic codes, with static factors forming subject-identity clusters without supervision. The swap experiment (Fig. 3) successfully transfers expressions between subjects. The honest failure-case analysis on MUG (Fig. 4) identifies the specific confusion (fear vs. surprise) and provides a plausible explanation, adding credibility.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The main paper claims state-of-the-art audio results but presents no audio evidence in the body.** The abstract, introduction, and conclusion claim state-of-the-art results on audio (Timit). Section 5.1 mentions Timit as a dataset, but no audio results — not a single table, figure, or numeric value — appear anywhere in the main paper's experimental sections (5.2–5.4). While the audio results presumably reside in the appendix (which the parser strips), the main paper should stand on its own for this claimed modality. The paper does not even reference a specific appendix table summarizing audio results. This is an organizational weakness that undermines one of the stated claims of modality-independence. The remainder of the paper's evidence (video + time series) is already strong, so this does not threaten the core contribution, but it should be fixed.

- **No direct quantitative measure of mode collapse beyond downstream proxies.** The paper defines mode collapse as "dynamic vectors encode static and dynamic information, leading to a non-meaningful static component" and uses downstream task performance and qualitative t-SNE separation as proxies. A more direct measure — e.g., estimated mutual information I_q(s; d_t) between static and dynamic codes, or the variance of static codes across sequences with identical dynamics — would more directly substantiate the central claim. The ablation study already provides strong indirect evidence (removing the subtraction causes clear collapse), so this is not a fatal gap, but it would make the comparison to MI-based competitors (e.g., C-DSVAE, SPYL) cleaner.

- **The subtraction mechanism's effect is empirically validated but not analyzed.** The paper subtracts \tilde{s} from \tilde{h}_t at each time step (Eq. 8) and the ablation proves this helps. However, there is no analysis of *why* it works — e.g., whether the subtraction actually reduces correlation between \tilde{s} and the LSTM hidden states, or the extent to which \tilde{s} and \tilde{h}_t share feature content. The paper would be stronger with even a small-scale diagnostic (correlation before/after subtraction, or a linear probe predicting static attributes from d_t). The core idea remains sound without this, but the architectural insight feels less grounded as a result.

### Trivial

- The confusion matrix caption in Fig. 4 refers to "the characters series on the left" but the paper body describes it as facial expressions (MUG dataset). This is a minor inconsistency in the figure description.

## Nice-to-Haves

- **Computational comparison:** The paper highlights fewer hyperparameters as an advantage but does not report training time or parameter counts versus baselines. Reporting wall-clock time or model size would strengthen the practicality argument.
- **Dynamic representation quality evaluation:** The evaluation focuses on static disentanglement and downstream prediction. A quantitative measure of dynamic code quality (e.g., motion prediction accuracy on Sprites, or forecasting of dynamic attributes) would round out the evaluation of what the dynamic codes capture.
- **Statistical significance:** Results are reported as means (with standard deviations in the appendix). For small-margin improvements (e.g., Sprites IS values in Tab. 1 that are nearly identical across methods), noting significance would clarify which differences are meaningful.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the subtraction description is "underspecified" about whether it happens at every step or only initially.** The paper's Eq. 8 reads "h_t := \tilde{h}_t - \tilde{s}, t=2,…,T," which clearly specifies subtraction at each time step. The LSTM's internal recurrence (\tilde{h}_{t-1} → \tilde{h}_t) is unaffected — the subtraction is a post-processing step on the output hidden state. This is a misreading by the reviewer.
- **Criticism about missing related works.** Per the meta-reviewer protocol, we cannot verify which related works are or are not cited without external sources.
- **Pure formatting/style nitpicks about the paper presentation.**
- **Criticism questioning whether cited models/references exist.** All cited models, datasets, and benchmarks are assumed to exist as of the review date.

## Novel Insights

None beyond the paper's own contributions. The reviews do not identify a novel perspective on the method that the authors themselves did not articulate. The strongest observation from the reviews is that the subtraction mechanism (Eq. 8) is empirically crucial but the paper does not probe *how* it achieves its effect — this is a gap the authors could address with correlation or probing analyses, but it does not reveal a new insight about the method.

## Suggestions

- Move a summary of the audio results (Timit) from the appendix into the main paper body. At minimum, reference the specific appendix table with key numbers (e.g., "See Tab. A.5 for audio results") and report the headline metric in a sentence. This is essential to make the claimed modality-independence verifiable in the main text.
- Add a diagnostic experiment directly measuring the separation between static and dynamic codes — e.g., mutual information I_q(s; d_t) estimates, or the ability of a linear probe to predict static attributes from d_t — on at least one dataset. This would directly substantiate the mode-collapse mitigation claim.
- Include training time or parameter count comparisons to support the claim of practical efficiency.

## Score and Decision

**Originality:** The architectural bias (conditioning s on a single sample + subtraction) is novel within the sequential disentanglement literature, which has primarily relied on loss-term interventions. The connection to architectural biases in other domains (CNNs, attention) is well-drawn.

**Importance of question:** Mode collapse in sequential disentanglement is a well-recognized problem. The paper addresses it with a simple, practical solution that avoids hyperparameter-heavy MI objectives.

**Claims supported:** The core claim (architectural bias mitigates mode collapse without MI terms) is well-supported on video and time series. The claim of audio results is not supported in the main paper body.

**Soundness of experiments:** Generally sound. Standard benchmarks, appropriate baselines, thorough ablation. Minor gaps: no direct mode-collapse metric, no statistical significance.

**Clarity of writing:** Clear and well-structured. The method is explained with equations and a figure. Some figures are only described via captions (parser artifact).

**Value to community:** The method is simple, effective, and easy to implement. It offers a practical alternative to MI-based approaches. The honest failure-case analysis is a model for rigorous evaluation.

The paper has no fatal or major weaknesses. The most significant issue (missing audio results in the main body) is an organizational fix, not a scientific flaw. The paper makes a clear contribution with strong empirical support on video and time series. The remaining weaknesses (no direct MI measure, no subtraction analysis) are minor and do not threaten the core claims.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>