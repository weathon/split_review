- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
I now have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes Gradient Storm, an extension of the Sleeper Agent backdoor attack that uses a multi-round optimization procedure (parameter R) combined with multiple optimization cycles (parameter S) to embed several distinct backdoor triggers—each with its own source-target pair and trigger type—into a single model simultaneously. The paper claims two contributions: (1) "stronger noisy gradients" achieved by distributing perturbations across multiple rounds targeting different parameter-space regions, and (2) a framework for multi-trigger, multi-target attacks. Experiments are conducted on CIFAR-10 and GTSRB using ResNet-18 and other architectures.

## Strengths

- **Demonstration of concurrent multi-trigger, multi-target attacks with distinct trigger types**: Section 4.4 (Tables 5 and 6) shows that Gradient Storm can embed two or three different backdoors (patch, blended patch, sinusoidal signal) simultaneously, each with a different source–target pair, in a single model. The paper reports high per-trigger attack success rates alongside preserved benign accuracy (~93–94%). This goes beyond single-trigger methods and demonstrates feasibility of the multi-trigger setting.

- **Broad defense evaluation**: Section 4.2 evaluates Gradient Storm against eight different defense mechanisms (Spectral Signatures, Activation Clustering, DeepKNN, Gradient Shaping, ABL, DP-InstaHide, I-BAU, MOTH), which is more comprehensive than what is typically reported for a single backdoor attack.

- **Black-box transferability demonstration**: Section 4.3 (Table 4) shows that poisons crafted using a ResNet-18 surrogate transfer to VGG-16, DenseNet-121, MobileNet-V2, and GoogLeNet with high ASR (≥95%), and that benign accuracy remains close to the clean baseline.

- **Competitive single-trigger performance**: Tables 1 and 2 compare Gradient Storm against several established single-trigger attacks (Blended, Label-Consistent, Refool, HTBA, Sleeper Agent) on CIFAR-10 and GTSRB, showing ASR at or above the level of baselines.

## Weaknesses

### Fatal
None.

### Major

- **No comparison to existing multi-trigger baselines (core evidential gap)**: The paper's central claim is that Gradient Storm enables effective multi-trigger attacks. However, Section 4.4 (the only multi-trigger evaluation) reports results for two and three simultaneous attacks **without comparing to any baseline whatsoever**. The paper itself cites existing multi-trigger methods in the related work (Gong et al. 2021, Xue et al. 2024, Wang et al. 2024) and describes them. Since there is no comparison—not even to a naive combination of independently-run Sleeper Agent attacks for each trigger, each with its own poison budget—the reader cannot assess whether Gradient Storm offers any advantage over prior work. This gap directly undermines the paper's second claimed contribution.

- **The "expanded parameter space coverage" mechanism is not empirically validated**: The paper's title and framing assert that dividing optimization into multiple rounds (R) causes poisons to target different regions of parameter space, producing "stronger" attacks. However:
  - No ablation study varies R; only R=2 is tested (Section 4.1).
  - No measurement or analysis shows that perturbations actually target different "regions" of parameter space.
  - The algorithm (Algorithm 1) is structurally similar to Sleeper Agent's iterative retraining (the paper states that Sleeper Agent already "distribute[s] the optimization process evenly across four retraining periods"), so what distinguishes the two is unclear and unvalidated.
  - The claimed mechanism therefore rests entirely on intuition, without supporting evidence.

- **Defense evaluation does not support the robustness claim without comparison**: The paper states that Gradient Storm shows "strong resilience against a range of poisoning defense mechanisms" (conclusion). However, Table 3 only reports Gradient Storm's ASR after each defense—it does not compare to any other attack's resilience under the same defenses. Without knowing whether a baseline attack (e.g., Sleeper Agent, Blended) would degrade more or less under the same defenses, the numbers in Table 3 are uninterpretable as evidence of relative robustness. Some defenses listed (e.g., Spectral Signatures, I-BAU) appear to substantially degrade ASR based on the reviewer reports, which further underscores the need for a comparative baseline.

### Minor

- **Multi-trigger experiments lack per-trigger single-attack baselines**: In the multi-trigger setting (Tables 5, 6), we do not see the ASR for each trigger when embedded alone under the same poison budget. Without this, it is unclear whether adding multiple triggers degrades individual trigger effectiveness, or whether one trigger dominates the others.

- **Modest single-trigger improvement over Sleeper Agent**: The claimed single-trigger improvement (contribution 1) appears marginal based on reviewer assessments, and no statistical significance testing is reported. While the multi-round procedure is a plausible extension, the evidence that it yields meaningfully "stronger" attacks is thin.

- **No variance or confidence intervals reported**: The single-trigger comparisons (Tables 1, 2) and multi-trigger results (Tables 5, 6) do not report variance across multiple runs, making it impossible to assess whether observed differences are meaningful or due to chance.

### Trivial
None.

## Nice-to-Haves

- Compare against a naive multi-trigger baseline: running Sleeper Agent (or any gradient-matching attack) independently for each trigger with its own poison budget, then testing all triggers on a single model.
- Compare against cited multi-trigger methods (Gong et al. 2021, Xue et al. 2024) under the same experimental conditions.
- Provide an ablation study varying R to validate the parameter-space coverage claim.
- Include the defense ASR of at least one competing attack (e.g., Sleeper Agent) in Table 3.
- Provide single-trigger baselines alongside multi-trigger results to assess interference.

## Removed Points

These points were flagged for removal; treat them with caution:

- **Criticism about garbled/corrupted text in equations (e.g., "sauncdh")**: This is a PDF-to-text parser artifact, not a paper author issue. The original submission does not have this problem. → **Removed per rule about parser errors.**

- **Criticism about missing appendix or proofs**: The parser strips appendices from all papers, so any claim about missing appendix content is based on incomplete information. → **Removed per rule about missing appendix.**

- **Criticism about "threshold T with no guidance on its setting"**: The paper specifies T=0.006 in Section 4.1, so the threshold is documented for the experimental setting. While general guidance could be helpful, this is a weak criticism. → **Moved here.**

- **Generic formatting/style nitpicks (e.g., "poorly formatted equations")**: Parser artifacts, not author errors. → **Removed.**

## Novel Insights

None beyond the paper's own contributions. The reviewers' main insight is that a paper claiming a multi-trigger attack framework must evaluate it against existing multi-trigger methods—otherwise the claimed contribution is unsubstantiated regardless of how clean the within-method results look.

## Suggestions

1. **Add multi-trigger baselines**: For Section 4.4, compare against (a) running Sleeper Agent independently for each trigger and combining the poisoned datasets, and (b) at least one existing multi-trigger method (e.g., Gong et al. 2021's neuron-specific approach). Report per-trigger ASR and benign accuracy for each.

2. **Provide an ablation on R**: Vary the number of rounds (e.g., R=1, 2, 4) while controlling for total retraining epochs and poison budget. Show that multi-round optimization yields higher ASR or different gradient orientations, directly testing the parameter-space coverage claim.

3. **Add defense comparisons**: Include ASR for at least one competing attack (e.g., Sleeper Agent) in the defense evaluation table to establish relative robustness.

4. **Report variance**: Run experiments multiple times with different random seeds and report standard deviations or confidence intervals.

5. **Tighten claims**: The conclusion claims "exceeding 90% in both single-trigger and multi-trigger scenarios." Verify that all individual per-trigger ASR values in Tables 5 and 6 meet this threshold. If some fall below, adjust the claim to match the evidence.
