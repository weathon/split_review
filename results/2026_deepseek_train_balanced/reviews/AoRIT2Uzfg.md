Now I'll produce the final consolidated review.

## Summary

This paper proposes DRMGuard, the first defense against backdoor attacks for deep regression models (DRMs) in the image domain. The key insight is that backdoored DRMs exhibit a distinctive angle-concentration property in feature space (RAV ≪ 1), which the paper exploits to formulate a reverse-engineering optimization that avoids enumerating target vectors — impossible for continuous output spaces where classification-based defenses fail. The framework identifies backdoored DRMs and mitigates the backdoor via fine-tuning on reversed poisoned data. Evaluations span 4 datasets, 2 regression tasks, and 4 attack types.

## Strengths

- **Identifies and empirically validates a novel feature-space characteristic unique to backdoored DRMs**: The paper discovers that backdoored DRMs produce highly concentrated angle distributions between feature vectors and weight vectors (RAV < 0.1 across all 4 attacks × 2 datasets in Table 1), while benign DRMs do not. This is conceptually sound, grounded in the structural difference (no argmax in regression, so all neurons contribute to the output), and directly enables the feature-space regularization term that distinguishes the method from classification-domain defenses.

- **Formulates reverse engineering without class enumeration**: The paper correctly identifies that existing defenses like Neural Cleanse and FeatureRE cannot be directly applied to regression because the continuous output space makes class-by-class target enumeration impossible. The proposed variance-minimization objective (first term of Eq. 7) bypasses this limitation. The empirical gap is large: DRMGuard achieves ROC-AUC=1.000 across all attacks while NC (max 0.940) and FeatureRE (max 0.730) fall far short (Table III).

- **Ablation studies cleanly isolate the necessity of each component**: Table 7 shows that removing either FSRT or MTR collapses accuracy to 50% (all models classified as backdoored). This demonstrates that both the feature-space regularization term and the momentum reverse trigger are individually necessary, directly validating the paper's theoretical analysis.

- **Broad evaluation scope**: The paper evaluates on 4 datasets (MPIIFaceGaze, ColumbiaGaze, Biwi Kinect, Pandora), 2 distinct regression tasks (gaze estimation d=2, head pose estimation d=3), 4 attack types spanning input-independent (BadNets, Clean Label) and input-aware (IA, WaNet), and 4 adapted baselines — reasonable breadth for a first work in this undefended space.

## Weaknesses

### Fatal
None.

### Major

- **Critical component (MTR) is incompletely specified, harming reproducibility**: The momentum reverse trigger is stated to be essential — removing it collapses accuracy to 50% (Table 7, "w/o MTR"). Yet the paper never formalizes its mechanism. Line 189 provides only a high-level description ("assign different weights to different regions to balance the attention of the DRM on the image") and trails into a LaTeX comment describing gradient-based attention maps that is not part of the published text. The actual equation, how "momentum" is incorporated, and how the attention map modifies the optimization are all absent. A reader cannot reproduce DRMGuard, and the community cannot evaluate whether the success is driven by the optimization formulation or by unspecified engineering choices in MTR.

- **Adaptive attack evaluation does not support the claimed robustness**: The adaptive attack (Sec. 4.6) adds a term forcing RAV toward 1, but the resulting backdoor has AE=5.71 vs. WaNet's AE=1.51 — meaning the attack is substantially less effective at being a backdoor in the first place. The paper acknowledges this (line 434: "The AE of the adaptive attack is significantly higher than that of WaNet") but still concludes the defense is robust. A proper stress test would first ensure the backdoor achieves low AE (i.e., is an effective backdoor), *then* test evasion. The current setup conflates attack failure with defense success.

### Minor

- **Generator architecture $G_{\theta}$ is unspecified**: The paper states "We use a generative model $G_{\theta}$ to model $\mathcal{A}$" (line 90) but never specifies its architecture, parameter count, or training procedure. Since the capacity of $G_{\theta}$ directly determines what triggers can be reverse-engineered, this gap affects both reproducibility and interpretation of results.
- **No uncertainty quantification**: All results (including the perfect ROC-AUC of 1.000 in Table III) are reported without confidence intervals, standard deviations, or variance across runs. With only 10 benign + 10 backdoored models per condition, the statistical reliability of these point estimates is unknown. The ColumbiaGaze result (70% accuracy, 4 false positives, 2 false negatives) suggests the detection margin is not universally wide, yet this is averaged into "87.5%" without analysis of failure patterns.
- **Multiple-backdoor claim is unsubstantiated**: Line 280 states "the results show that our method is effective on identifying DRMs with multiple backdoors" without presenting any quantitative results, experimental setup, or analysis of what "multiple" means. This claim should be backed by evidence or removed.
- **Hyperparameter selection across tasks lacks justification**: $\lambda_1$ and $\lambda_2$ differ substantially between gaze estimation (20, 800) and head pose estimation (10, 100) with only "given task difference" as explanation (line 227). The ablation shows the method is sensitive to $\lambda_2$ (accuracy varies from 75% to 100%), yet no principled selection procedure is provided.

### Trivial
None.

## Nice-to-Haves

- Discussion of the ColumbiaGaze failure cases — are there systematic patterns (specific head poses, lighting conditions, subjects) that produce the 4 false positives and 2 false negatives?
- Reporting wall-clock time or optimization steps for the reverse engineering process to assess practical deployability.
- Clarification of how Neural Cleanse's outlier-detection heuristic (designed for discrete classes and their trigger magnitudes) was adapted to regression, beyond making $y_t$ an optimization variable.

## Removed Points

The following weaknesses from the input reviews were removed after verification:

- *"ROC-AUC of 1.000 is suspicious and likely an artifact of small sample size"* → **Downgraded from "critical" to Minor (above).** Perfect separation on 20 samples is not inherently suspicious — it simply means the perturbation metric cleanly separates the two groups. The genuine concern is lack of error bars and the ColumbiaGaze variability, which are already captured.
- *"Feature-space observation needs broader validation (only 2 datasets, 4 attacks)"* → **Removed.** Validated across 4 attacks × 2 datasets, which is reasonable first-work breadth. Suggesting more architectures/tasks as a weakness is scope creep.
- *"Baseline adaptation is described too briefly to be trustworthy"* → **Removed as standalone point.** The paper states the adaptation (making $y_t$ an optimization variable) clearly. The NC regression adaptation is genuinely nontrivial, but this is noted as a nice-to-have, not a flaw.
- *"Fine-tuning baseline deserves more discussion"* → **Removed.** DRMGuard's DAE (3.29) outperforms Fine-tuning (4.32). The comparison is adequate.
- *"Limitations section is one sentence"* → **Removed.** Short limitations sections are acceptable as long as the key limitation is identified. The paper correctly notes that a benign dataset is required.
- Various formatting nitpicks, speculative criticisms about missing appendix content, and claims about missing related works → **Removed per hard rules.**
- Strength Finder's generic/superficial strengths about "the problem being important" and the paper "addressing an important gap" → **Removed.** These add no specific information beyond what the paper itself states.

## Novel Insights

None beyond the paper's own contributions. The core insight — that backdoored DRMs exhibit angle concentration in feature space due to the absence of argmax, and that this can be exploited for defense — is already clearly stated in the paper.

## Suggestions

1. **Fully specify the MTR**: Provide the complete mathematical formulation — how the attention map is computed from input gradients, what "momentum" refers to (e.g., exponential moving average of attention maps across optimization steps), and how this modifies the optimization (element-wise weighting of the perturbation, the loss, or both).
2. **Construct a properly adaptive attack**: Start from a backdoor that achieves low AE comparable to WaNet's 1.51, then add the defense-aware penalty $L_{adp}$. If the penalty degrades AE, report this trade-off honestly; if AE can be maintained while raising RAV, report the resulting identification accuracy.
3. **Add statistical rigor**: Report mean and standard deviation (or confidence intervals) across multiple runs for all main results. For the ROC-AUC, also report the standard deviation.
4. **Specify the generator architecture** ($G_{\theta}$) in the main text or supplement — at minimum the architecture family, layer count, and parameter count.
5. **Substantiate or retract the multiple-backdoor claim** (line 280).

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>