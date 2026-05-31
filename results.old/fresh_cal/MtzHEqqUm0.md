Good, I've verified all claims against the paper. Let me now produce the consolidated review.

## Summary

This paper re-evaluates two long-tailed regularization methods (contrastive loss from Makansi et al. 2021 and PLM reweighting from Kozerawski et al. 2022) by applying them to Trajectron++, a probabilistic trajectory predictor with associated likelihoods, whereas prior work only tested these methods on non-probabilistic models. The authors evaluate on both pedestrian and vehicle classes of the NuScenes dataset using KDE-NLL and most-likely FDE metrics. The central finding is agent-dependent: both methods improve long-tail performance for pedestrians, but neither reliably improves (and PLM reweighting sometimes degrades) long-tail KDE performance for vehicles — a finding that differs from the original papers' claims.

## Strengths

- **First application to a probabilistic predictor.** The paper correctly identifies that prior long-tail regularization work (Makansi et al., Kozerawski et al.) was evaluated only on non-probabilistic models (EWTA) using minADE/minFDE metrics. Applying these methods to Trajectron++, which outputs a full distribution with likelihoods, enables evaluation with the KDE-NLL metric that assesses the whole predicted distribution rather than just the best trajectory (§3.2, lines 59–69). This is a genuine methodological gap that the paper addresses.

- **Evaluation across both agent types reveals agent-dependent results.** The original papers evaluated on only one agent class. By reporting results for both pedestrians and vehicles in NuScenes (Tables 1–4), the paper shows that the methods' effectiveness does not transfer uniformly — a non-trivial empirical finding that would not have been surfaced otherwise.

- **Negative finding for vehicles is the paper's most valuable contribution.** The demonstration that neither contrastive loss nor PLM reweighting reliably improves long-tail KDE for vehicles, and that PLM reweighting even degrades performance (Table 4, §4.2.2, lines 162–165), contradicts the implicit generality of the original claims. This negative result is actionable for the community.

- **Use of KDE-NLL for distributional evaluation.** The paper adopts the KDE metric from Salzmann et al. (2021) instead of relying solely on point-based metrics (§4.1, lines 105–107), providing a more principled assessment of the predicted distribution quality.

## Weaknesses

### Fatal
None.

### Major

- **Ablation study is announced but never presented.** Line 91 states: "we also perform an ablation study to see how applying more or less regularization might affect the model." No results from this study appear anywhere in the paper. This is a significant omission because the regularization methods (contrastive loss and PLM reweighting) were originally tuned for a non-probabilistic EWTA baseline. Without any exploration of how regularization strength interacts with the CVAE's ELBO objective, the reader cannot assess whether the reported comparisons reflect a genuine property of the methods or suboptimal hyperparameter choices. This directly weakens confidence in the core empirical claims.

### Minor

- **Loss integration details are insufficient for reproducibility.** The paper states that contrastive loss is applied to the CVAE's feature embedding "before the decoder" (line 80) and that it uses default parameters from Makansi et al. (2021), but it never specifies how the contrastive loss is combined with the CVAE's ELBO objective (e.g., additive weighting coefficient). For PLM, the description says "adding the PLM regularization function... to the individual loss of each example" (line 89), but in Kozerawski et al. the PLM is a *transformation* of the per-example loss, not an additive term. Whether these are additive regularizers or loss transformations matters for reproducibility. The paper should provide the exact training objective equation.

- **No statistical reliability measures.** All results are reported from a single run with no variance, confidence intervals, or multiple seeds. Given that long-tail evaluation splits the test set into percentiles (95th, 98th, 99th), the effective sample sizes for extreme-tail metrics are small, making single-run results potentially fragile. Even reporting mean over 3 seeds would substantially strengthen the evidence.

- **Vehicle failure analysis lacks supporting quantitative evidence.** The paper attributes PLM reweighting's poor vehicle KDE performance to predicting a "mean" long-tail trajectory (line 162–163), which is a plausible inference from the combination of good most-likely FDE and bad KDE. However, this remains speculation without direct diversity metrics (e.g., average pairwise distance among top-k predictions, mode count, entropy of the predicted distribution). The qualitative examples (Figure 3) show only single cases. Computing such metrics is straightforward from existing model outputs and would strengthen the contribution.

- **"In many cases" in qualitative evaluation is unsubstantiated.** Line 171 states that in "many cases" the contrastive model's predictions had higher variance, without providing any quantitative measure of how many cases or how much higher. This weakens the qualitative analysis.

- **minFDE not reported for direct comparison with original works.** The paper justifies replacing minFDE with most-likely FDE (lines 131, 160), which is a reasonable choice for evaluating the most-probable prediction. However, the paper also states that "the good results of Makansi et al. (2021) and Kozerawski et al. (2022) persist" (line 143) without ever reporting the metric (minFDE) on which those original results were defined. Reporting minFDE alongside the chosen metrics would provide a cleaner link to prior work and allow readers to directly assess whether claimed improvements transfer.

### Trivial

- **CVaR/percentile imprecision.** The paper states (line 114) that percentile error is "equivalent to measuring the CVaR." The p-th percentile of errors is Value at Risk (VaR), not CVaR (which is the conditional expectation above the threshold). This is a minor technical inaccuracy that does not affect the results.

## Nice-to-Haves

- Include the announced ablation study results (a sweep over the key regularization strength parameters) to calibrate trust in the reported comparisons.
- Compute and report minFDE from the available 20 trajectory samples alongside the current metrics to enable direct comparison with the original papers.
- Add diversity metrics (e.g., average pairwise distance among predicted modes) to substantiate the "mean trajectory" explanation for vehicles.
- Run the methods on the original EWTA baseline under the same experimental conditions to isolate the effect of the base predictor from the effect of regularization, strengthening the claim that results differ from prior work.

## Removed Points

- **Tables as images making results unverifiable.** This is a PDF parsing artifact — the original submission contains proper tables. Removed per rule: parser errors are not author errors.
- **Abstract overselling KDE focus.** The paper reports both most-likely FDE and KDE, and the abstract specifies "comparing them on the KDE metric" as a focus — it does not claim exclusivity. Removed as a nitpick.
- **Underspecified "first to report both classes" claim.** The paper explicitly clarifies the scope of its claim (same framework, same metrics). Removed as not a genuine weakness.
- **Missing EWTA baseline comparison for isolation.** Scope creep — the paper's contribution is evaluating on a probabilistic predictor, not isolating base-predictor effects. Demoted to nice-to-have.
- **Missing related works.** Rule prohibits mentioning missing related works without external verification. Removed (no such criticism appears in inputs, noted for completeness).

## Novel Insights

The harsh critic's most insightful observation is that the vehicle failure analysis, while directionally correct, could be significantly strengthened by converting its plausible inference (good most-likely FDE + bad KDE → mode collapse) into a quantitative finding with diversity metrics. This would elevate the paper's central negative result from a descriptive observation ("neither method works for vehicles") to an actionable diagnostic ("the methods induce mode collapse in the vehicle regime because..."). Neither reviewer surfaced the deeper question of whether the CVAE's latent space interacts differently with the contrastive loss for vehicles vs. pedestrians — this remains an underexplored angle in the paper itself. The merged review also surfaces that the paper's strongest contribution (the surprising agent-dependent result) is also its weakest-supported claim, due to the missing ablation study and lack of statistical rigor.

## Suggestions

- **Present the ablation study results.** This is the single most impactful fix. Even a simple sweep over the regularization weight (e.g., λ for contrastive loss) would show whether the default parameters from the EWTA regime are reasonable for Trajectron++ or whether the results are parameter-dependent.
- **Compute minFDE from the existing 20 trajectory samples.** This is trivial (the paper already generates 20 samples per example) and would permit direct comparison with the original papers' numbers, making the claim that "results persist" or "differ" verifiable rather than asserted.
- **Report variance or multiple seeds.** At minimum, mean and standard deviation over 3 random seeds for at least the key tables (Tables 2 and 4) would greatly improve confidence, especially for the extreme-tail percentile splits where sample sizes are small.
- **Add diversity metrics for the vehicle analysis.** Compute average pairwise distance among top-k predicted trajectories or distribution entropy to quantitatively support the hypothesized mode collapse in PLM reweighting for vehicles.

## Score and Decision

This paper tackles a well-motivated and genuinely underexplored question. The main empirical finding — that long-tail regularization methods transfer to probabilistic predictors only for pedestrians, not vehicles — is interesting and potentially useful. However, the missing ablation study (announced but absent) is a significant gap that undermines confidence in the core comparison: without knowing whether the default parameters from a non-probabilistic training regime are appropriate for a CVAE, the reader cannot tell whether the observed differences reflect genuine transfer properties or hyperparameter mismatch. The lack of any statistical reliability measures (single seed, no variance) further weakens the evidence. These are fixable issues, but as submitted, the empirical support for the central claims is incomplete.

**Originality:** Moderate — applying existing methods to a new predictor type. **Importance of question:** Good — understanding when long-tail methods transfer is practically relevant. **Support for claims:** Below average — the missing ablation study and lack of statistical rigor are real gaps. **Soundness of experiments:** Moderate — methodology is generally sound but lacks verification steps. **Clarity:** Good — the paper is well-written and clearly motivated. **Value to community:** Moderate — the negative result for vehicles is the most valuable finding, but its presentation needs strengthening.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>