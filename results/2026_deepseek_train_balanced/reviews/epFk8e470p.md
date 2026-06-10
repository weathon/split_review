## Summary

This paper investigates how humans and deep networks use body vs. background information for action recognition. It finds that a standard ResNet-50 trained on full video frames performs at chance (20%) on body-only stimuli, while humans remain highly accurate (94%). The paper proposes a two-stream architecture (DomainNet) with separate body and background streams and per-stream losses, which raises body-only accuracy to 62.5% and reproduces the human-like ordinal pattern (body > background accuracy). Human behavioral data (N=28) from the HAA500 dataset is also reported.

## Strengths

- **Baseline failure is cleanly quantified:** ResNet-50 achieves chance-level (20%) on body-only stimuli versus 57% on original and 40% on background-only (Section 4.3, line 109). This is a concrete, reproducible finding about a specific failure mode of standard supervised action recognition.

- **DomainNet yields a 42.5 percentage-point improvement on body-only stimuli** (from 20% to 62.5%, Section 4.4, line 116) — a large effect that directly supports the practical value of separate-stream processing.

- **Stimulus construction is methodical:** Body masks were summed across all frames of each video and dilated before inpainting, ensuring the inpainted region does not change frame-to-frame and contains no silhouette outline that could convey pose information (Section 3.1, line 39).

- **Parameter-count concern is partially addressed:** DomainNet:frames (two ResNet-50 streams) outperforms Baseline:frames+flow (also two ResNet-50 streams), ruling out the simplest "more parameters → better performance" explanation (Section 5, line 140).

- **Code and data are provided** at an anonymized link (Section 6, line 155).

## Weaknesses

### Fatal

None.

### Major

1. **Training data and loss function confound between Baseline and DomainNet.** The Baseline is trained only on ORIG frames with a single cross-entropy loss. DomainNet is trained on body-only AND background-only frames (two input versions) with three separate loss terms (L_body, L_background, L_combined). The paper attributes performance gains to "brain-inspired architecture" (lines 129, 140), but the architecture is confounded with (a) 2× training data variety and (b) multi-task supervision. The parameter-count control (DomainNet:frames vs. Baseline:frames+flow) does not isolate the architectural contribution because the training inputs and loss functions still differ. Without a control that disentangles the effect of the separate-stream design from the effect of richer training data and loss signals, the paper cannot support its central claim that the architecture itself drives improvement. This is a structural limitation in the experimental design.

2. **Critical missing methodological detail: how does DomainNet process ORIG frames at test time?** The paper specifies that DomainNet receives "body-only frames and background-only frames respectively" as input during training (Section 3.2, line 46). It then reports DomainNet accuracy "when tested using frames showing both the body and the background ('ORIG')" (Section 4.4, line 116). The paper never states how a two-stream model trained on isolated inputs handles a full ORIG frame at test time. Possible approaches (e.g., segmenting the ORIG frame at test time and feeding each stream its respective input; feeding the ORIG frame directly to both streams; using only the combined output) would produce very different results. This omission makes the ORIG accuracy numbers for DomainNet uninterpretable without consulting the code, which undermines a key comparison in the paper.

### Minor

3. **"More human-like pattern" claim lacks quantitative support.** The paper asserts that DomainNet's performance pattern "matches more closely the pattern of accuracy observed in human participants" (Section 5, line 129). The evidence presented is the ordinal property that both humans and DomainNet show body > background accuracy, while Baseline shows the reverse. No quantitative measure of pattern similarity is reported — no correlation of per-category accuracies, no cosine similarity between accuracy vectors, no statistical test. The ordinal observation is meaningful but too coarse to carry the weight the paper places on it, especially given the large absolute accuracy gap between humans and DomainNet.

4. **Fixed block order confounds condition with practice effects in the human experiment.** Background-only blocks were always presented first, body-only second, ORIG third (Section 3.4.2, line 78). The rationale (avoiding carryover from ORIG) is legitimate, but this fixed order means practice effects and task familiarization are confounded with condition. Body-only accuracy (94%) could be inflated relative to background-only (76%) simply because participants had more experience with the task by the second block. The large effect size makes it unlikely that practice alone explains the 18-point gap, but the confound is real and should be acknowledged as a limitation.

5. **No variance or confidence intervals for model accuracies.** All model results (Sections 4.3–4.4) are reported as single point estimates. It is impossible to assess whether modest differences (e.g., the 2.5% gain on background-only, or the 3.75% drop when adding flow to DomainNet on background-only) are reliable across training runs.

6. **Unexplained accuracy decrease when adding optical flow to DomainNet for background-only stimuli.** DomainNet:frames+flow achieves 38.75% on background-only, a 3.75% decrease from the frames-only version (42.5%). The paper notes this as "somewhat surprising" (Section 4.4, line 118) but offers no analysis or hypothesis.

### Trivial

7. **Citation error:** YOLO v8 is cited as (Redmon et al., 2015), which is the original YOLO paper, not YOLO v8 (Section 3.1, line 39).

## Nice-to-Haves

- A control experiment where a single-stream ResNet-50 is trained on all three input versions (ORIG, body-only, background-only) with a comparable multi-objective loss to isolate the effect of the separate-stream architecture.
- Counterbalanced or between-subjects block ordering in the human experiment.
- Quantitative pattern-similarity metrics (e.g., Spearman correlation of per-category accuracies between humans and each model, with confidence intervals).
- Ablation of the three loss terms (e.g., L_combined only, or L_body+L_background only) to understand each term's contribution.
- Testing additional backbone architectures beyond ResNet-50 to establish generality across network designs.

## Removed Points

*Points below are flagged for removal; treat them with caution.*

- **Category selection as "cherry-picking" (Harsh Critic Point 2):** The paper's stated rationale — selecting the 50 most accurate categories for Baseline to ensure failures are not category-specific — is a reasonable methodological choice. The claim that selected categories have the "most diagnostic backgrounds" is speculative and unsupported by evidence in the paper. REMOVED as speculative.
- **"Dropout relationship is tenuous" (Section-by-section notes):** The paper's discussion of Dropout is coherent on its own terms (different sub-networks vs. fixed streams, redundancy reduction). Not a genuine weakness.
- **"No justification for summation fusion":** A design choice; not a weakness unless shown to be inferior.
- **"Speculative evolutionary claims in Discussion":** The Discussion does make broad claims about brain organization, but this is standard scope for a discussion section that frames broader implications. The core empirical results are what determine paper quality.
- **Strength Finder Point 3 ("design minimizes order effects"):** The paper's design has a fixed block order which confounds practice effects — calling this a strength is incorrect. REMOVED.
- **Generic/superficial strengths (e.g., "addresses an important problem"):** REMOVED per filtering rules.

## Novel Insights

None beyond the paper's own contributions. Both reviews converge on the core empirical findings but offer standard methodological critiques (confounds, missing controls, thin quantitative support) rather than generating new insights about the paper's content.

## Suggestions

1. **Clarify test-time ORIG handling:** State explicitly how DomainNet processes ORIG frames — this is essential for interpreting the main results.
2. **Add the critical control:** Train a single-stream model on all three input versions with comparable losses. If it matches DomainNet, reframe the contribution around training strategy; if it falls short, the architectural claim gains real support.
3. **Report variance:** Use multiple random seeds and report means with standard deviations or confidence intervals.
4. **Add pattern-similarity metrics:** Compute per-category accuracy correlations between humans and each model, with statistical testing.
5. **Acknowledge block-order confound explicitly** and discuss its likely magnitude and direction.
6. **Temper Discussion claims:** The evidence from one ResNet-50 variant on one dataset does not support an "alternative account" of ventral temporal cortex organization. Scope the neuroscientific claims to match the empirical basis.

---

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>