Now I have thoroughly read the paper. Let me synthesize my review.

## Summary

ALBAR proposes an adversarial training framework for mitigating both foreground and background biases in video action recognition, using entropy maximization and gradient penalty losses on static (motionless) clips through a single 3D encoder—eliminating the need for attribute labels or a separate 2D critic model. The method achieves over 12% improvement in contrasted accuracy on HMDB51 and also identifies and corrects a background leakage flaw in the existing UCF101 SCUBA/SCUFO evaluation protocol.

## Strengths

- **Identifies a genuine evaluation confound in the UCF101 bias protocol** (Section 4.2, Figure 2): The paper convincingly demonstrates that bounding-box masks used in the prior UCF101 protocol allow background information to leak into foreground evaluation, and proposes tighter segmentation masks via SAMTrack. This is a substantive methodological correction.

- **Strong quantitative improvements**: The >12% improvement in contrasted accuracy on HMDB51 (53.02% vs. prior best) is a significant margin, and the method achieves state-of-the-art on multiple SCUBA/SCUFO variants. Composing ALBAR with StillMix further pushes this to 53.68%.

- **End-to-end design without attribute labels or external critics**: Unlike prior methods requiring scene/object classifiers (ARAS) or salient frame detectors (StillMix), ALBAR operates within a single 3D encoder, improving scalability and practical applicability (Section 1, Sections 3.3–3.4).

- **Informative ablation study** (Table 3): Shows that adversarial loss alone degenerates into label-flipping (row b), entropy alone is insufficient (row c), and each component complements the others (row h), providing clear design rationale.

- **Composability with augmentation methods**: The combination with StillMix pushing contrasted accuracy to 53.68% demonstrates complementary behavior between adversarial and augmentation-based debiasing.

## Weaknesses

### Fatal

None.

### Major

- **Partial alignment between training objective and evaluation metric weakens the headline SCUFO claim**: The entropy maximization loss (Eq. 3) directly trains the model to produce uniform class probabilities on static clips. The SCUFO component of contrasted accuracy measures whether static clips yield inaccurate predictions—precisely the behavior the loss enforces. This means a significant portion of the 12% contrasted accuracy improvement is mechanically explained by the training objective rather than demonstrating that the model learned genuinely "robust motion features." A model that simply detects the absence of motion and suppresses predictions would score well on SCUFO without being debiased. However, this concern does **not** invalidate the entire paper: improvements on SCUBA (motion clips with replaced backgrounds), ARAS rare-scene evaluation, and downstream tasks provide independent evidence. The concern specifically weakens the SCUFO-portion of contrasted accuracy as an independent validation of debiasing. The paper would be substantially strengthened by additional evidence that the model relies on motion features rather than a motion-activation gate—e.g., evaluation on clips where motion cues conflict with foreground appearance cues, or representational analysis (t-SNE, CCA) showing feature-level changes.

- **Limited evidence of foreground debiasing beyond static-clip uniformity**: The paper frames foreground debiasing (reducing reliance on appearance cues like clothing) as a key contribution. However, the primary evidence for foreground debiasing is the SCUFO metric, which measures behavior on motionless clips—a scenario directly targeted by the training loss. The Confl-FG evaluation partially addresses this by inserting conflicting foregrounds into motion clips, but does not create direct motion-vs.-foreground conflicts where an actor's appearance suggests one action while the motion indicates another. Without such evaluation, the claim of foreground debiasing remains partially unverified beyond "the model outputs uniform predictions on static inputs."

### Minor

- **Missing comparison with conceptually similar adversarial debiasing methods**: The paper explicitly positions itself as improving upon the 2D-critic paradigm (citing Bahng et al. / ReBias), but does not compare against ReBias or LfF experimentally on the same benchmarks. While these methods were designed for image classification rather than video, an experimental comparison would strengthen the argument that the single-encoder formulation is superior.

- **The "no static information is useful" assumption acknowledged in Limitations is restrictive**: The paper concedes this assumption (Section on Limitations), and actions where static context is genuinely disambiguating (e.g., "diving" in a pool vs. "falling") may suffer. No per-class analysis is provided to quantify this cost, which would help assess practical utility.

- **Downstream task gains are modest and lack statistical significance testing**: UCF_Crime AUC improves ~1% and THUMOS14 mAP improves 1–3 percentage points (Table 5). Without standard deviations or significance tests across the 3 runs, it is unclear whether these improvements exceed normal variance.

- **The ablation in Table 3 reveals that adversarial loss alone causes label flipping** (predicting the wrong class with high confidence), indicating the model's representations still encode strong static correlations. The paper discusses this but does not provide representational analysis (e.g., feature visualizations before/after debiasing) to verify whether the combined losses actually change learned features rather than just remapping outputs.

### Trivial

None.

## Nice-to-Haves

- Evaluation on clips with direct motion-vs.-foreground conflict (e.g., an actor in a soccer uniform throwing a frisbee) to more robustly test foreground debiasing.
- Representational analysis (t-SNE/CCA) comparing features before and after debiasing to verify feature-level change rather than output-level suppression.
- A controlled "motion-gate" baseline that explicitly detects absence of motion and suppresses predictions, to verify that ALBAR achieves more than this trivial strategy.
- Per-class breakdown of debiasing effects to identify actions where the method helps vs. hurts.

## Removed Points

- **Claims about absent comparisons with LfF/ReBias being essential**: Downgraded from major to minor. While desirable, ReBias and LfF are image-classification methods not designed for video action recognition benchmarks, making direct comparison require non-trivial adaptation. This is a nice-to-have rather than a critical gap.

- **SAMTrack segmentation quality concerns**: The paper states each video is "manually checked for accurate segmentation." While quantifying failure rates would strengthen the protocol, the manual checking provides reasonable quality assurance. This is a minor methodological detail, not a weakness.

- **IID accuracy degradation concern**: The 73.08% vs. 73.52% difference is negligible (0.44%), and the paper reports averages over 3 runs. This is not a meaningful degradation warranting separate analysis.

- **Statistical significance of downstream gains as a major weakness**: Downgraded. While confidence intervals would be informative, single-run evaluation without standard deviations is standard practice in this community. The consistent improvements across multiple tasks provide some robustness.

- **Claims that the paper cannot claim foreground debiasing at all**: Overstated. While the SCUFO-based evidence is partially circular, SCUBA (background-swapped clips with motion), Confl-FG, ARAS, and downstream evaluations provide independent evidence of debiasing. The concern is that *foreground* debiasing specifically is less well-validated, not that all debiasing claims are unfounded.

## Novel Insights

The identification of the background leakage in the UCF101 protocol via bounding-box masks is a genuine and non-obvious contribution—the kind of evaluation hygiene fix that improves the entire field's measurement. The label-flipping degenerate solution uncovered in the ablation (Table 3, row b) is also noteworthy: it reveals that adversarial debiasing alone doesn't simply remove static dependence but can invert it, and the entropy maximization loss is specifically needed to prevent this pathology. This interaction is a design insight for future adversarial debiasing methods.

## Suggestions

- Add a simple "motion gate" baseline: a model that explicitly detects motion magnitude and outputs uniform predictions when motion is near-zero, while using a standard classifier otherwise. If ALBAR significantly outperforms this baseline on SCUBA and downstream tasks, it would directly address the motion-gate concern.
- Report per-class or per-category debiasing analysis to identify action types where the method provides the most and least benefit, particularly to assess the cost of the "no static information useful" assumption.
- Provide t-SNE or similar visualizations of encoder representations before and after debiasing to verify genuine feature-level changes.

## Score and Decision

The paper makes real contributions: a genuine evaluation protocol fix, strong performance improvements, a clean method, and good ablations. The partial alignment between the entropy loss and the SCUFO evaluation metric is a substantive concern that weakens the SCUFO component of contrasted accuracy as independent validation, but independent evidence from SCUBA, ARAS, and downstream tasks partially mitigates this. The lack of foreground-motion conflict evaluation leaves foreground debiasing claims less well-supported than background debiasing claims. These are significant but not fatal weaknesses. The paper is above the acceptance threshold.

**Originality**: The single-encoder adversarial formulation is a meaningful departure from prior 2D-critic approaches, and the UCF101 protocol fix is a non-obvious contribution.

**Importance**: Foreground bias in action recognition is an understudied and societally relevant problem.

**Claims support**: Partially well-supported; the SCUBA and downstream evidence is strong, but SCUFO-based claims are partially circular.

**Experiments**: Comprehensive across multiple benchmarks, protocols, and ablations, with one notable gap ( foreground-motion conflict tests).

**Clarity**: Well-written and clearly organized.

**Value**: The UCF101 protocol fix alone is a service to the community, and the method advances the state-of-the-art.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>