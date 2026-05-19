Now I have a thorough understanding of the paper and all reviewer claims. Let me synthesize the final consolidated review.

---

## Summary

This paper reanalyzes neural recordings from mouse piriform cortex during an odor discrimination task with prolonged overtraining (18 extra days after behavioral saturation). The authors provide evidence that target vs. nontarget odor representations continue to separate during overtraining (Figure 2), that the margin of a linear SVM trained on these representations increases (Figure 4), and that decoding accuracy improves (Figure 1, right). They build a synthetic MLP model that recapitulates these qualitative patterns and use a hinge-loss ablation to attribute the effect to late-time margin maximization. A separate theoretical section derives how this feature-learning framework can explain the classic overtraining reversal effect in animal learning.

## Strengths

- **Direct neural evidence of continued representation separation during behavioral plateau.** Figure 2 shows that the average dot product (interpreted as representational similarity) between target and nontarget population responses decreases from the first to the last day of overtraining, while behavior in Figure 1 (left) is at ceiling throughout. The effect is present in all 4 animals. Figure 4 further shows that the margin of a max-margin SVM trained on PPC representations increases steadily across days of overtraining. These two observations constitute the paper's primary empirical contribution and are genuinely novel — they provide a neural-level window into hidden learning that parallels the "grokking" phenomenon in deep learning.

- **Causal mechanistic probe through model ablation.** The synthetic MLP (Section 4.1) shows that the same qualitative pattern — training loss plateaus while test loss continues to drop, margin increases, and representations separate — can arise from a simple architecture. The hinge-loss ablation is a clean causal test: replacing cross-entropy (which drives late-time margin maximization) with hinge loss (which stops providing loss gradients once margin ≥ C) eliminates the late-time test loss improvements, directly supporting the claim that margin maximization drives the effect in the model.

- **Fine-grained tracking of feature learning via the Fisher discriminant.** Figure 6 tracks the Fisher discriminant between target and probe classes over training, showing that signal-to-noise increases monotonically during overtraining and that probe trials are learned in order of increasing overlap with the target. This provides a principled metric connecting the neural separation to improved decoding performance and adds detail to the "hidden progress" narrative.

## Weaknesses

### Fatal
None.

### Major

1. **Unaddressed confound: whether the same nontarget stimuli are compared across days.**  
   The paper does not state whether the exact same nontarget odors are presented on each day of overtraining vs. sampled from a larger pool. The setup description says the mice discriminate "one target odor from hundreds of nontarget odors" with "around N≈200 trials per day." If the nontarget set changes across days, then the increasing margin and class separation could partly reflect a shift toward an easier stimulus distribution rather than progressive refinement of representations of a fixed set of items. This is the most serious weakness because the paper's central claim is that *the same* trained items become better separated over time. The trends are visually consistent across all 4 mice, which mitigates (but does not eliminate) this concern. The authors must either clarify from the original data source that the same nontarget stimuli appear across days, or re-run the analysis on a fixed subset of trials.

2. **The synthetic model is not quantitatively validated against the neural data.**  
   The model uses n=10, k=100 (vs. n=3, k=13 in the real task), a different architecture (one-hidden-layer MLP vs. piriform cortex), and is trained on a much larger stimulus space. The paper offers no quantitative match to the neural data — no comparison of time constants, no fitting of margin growth rates, no test of whether the model's representational similarity trajectories resemble those in Figures 2–4. The hinge-loss ablation demonstrates that margin maximization *can* drive the effect in the model, but it does not establish that margin maximization *does* drive it in cortex. The model is illustrative but does not constrain the hypothesis against alternatives (e.g., slow Hebbian plasticity, gain adaptation, unsupervised consolidation).

### Minor

1. **Core trends lack statistical significance testing.**  
   Figures 2, 4, and the right panel of Figure 1 show trends across days with standard-error bands, but no formal significance test is reported (e.g., slope across days ≠ 0 in a mixed-effects model, permutation test for monotonicity, or comparison between first and last day accounting for individual variability). With only 4 mice and ~15 neurons each, it matters whether the trends are statistically reliable across animals or dominated by one subject. The visual consistency across all 4 mice is encouraging, but formal testing would substantially strengthen confidence.

2. **The overtraining reversal section (Section 4.2) is a disconnected theoretical add-on.**  
   The linear-network model of reversal learning is mathematically derived and simulated, but it is not tested against the neural data (the mice in Berners-Lee et al. were not studied in a reversal paradigm) nor grounded in known features of olfactory cortex. The section is presented as a core contribution ("We use our insight to suggest a new, fine-grained and neural explanation for the overtraining reversal effect"), but the link to the paper's empirical evidence is absent. If retained, it should be clearly labeled as a prediction for future work. Its removal would not weaken the paper's primary thesis.

3. **PCA visualizations (Figure 3) have limited interpretability.**  
   The PCs are recomputed independently for each session, so axis orientations and scales differ between the first and last day. The paper presents these as a "qualitative view," but the visual claim of "more separated" representations cannot be reliably assessed from these panels. This does not undermine the quantitative evidence in Figures 2 and 4, but the qualitative framing is overclaimed.

### Trivial
- None beyond the items already listed.

## Nice-to-Haves

- Report neuron counts per day and check robustness of trends to subsampling, since the margin and decoding analyses may be sensitive to the small and potentially variable number of recorded neurons (~15).
- Clarify the margin normalization procedure ("normalize margins for each mice") — how exactly was this done, and does the trend hold without normalization?
- Consider adding cosine similarity or cross-validated distance as an alternative to dot product for representational similarity, to decouple magnitude from direction. (The current use of z-scored dot product is defensible but could be justified more explicitly.)

## Removed Points

*These points were raised in the reviews but are excluded from the main weaknesses for the reasons stated.*

- **"Dot product conflates magnitude and direction; use correlation instead."** The paper states it uses Z-scored firing rates and computes the average dot product. For Z-scored data, dot product is proportional to correlation/cosine similarity, so this is not a genuine issue.
- **"Margin normalization not explained."** The paper states: "We normalize margins for each mice so data are comparable across mice." This brief explanation is adequate for the setting.
- **"The paper does not report how many neurons were recorded per mouse and per session beyond 'around 15.'"** The paper reports "around D≈15 neurons" and "around 15-20 days for each of 4 mice." More detail would be helpful but is not a weakness — this is standard reporting for a reanalysis.
- **"Choice of model parameters (n=10, k=100) not justified."** The paper explains that the parameters were increased to allow for probe trials with varying overlap. This is a reasonable design choice for the model's purpose.
- **Generic "weakness" about missing significance tests for the Fisher discriminant.** This duplicates the Minor weakness already listed above about overall lack of statistical testing.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that meaningfully reframes or extends what the paper itself argues.

## Suggestions

1. **Clarify the stimulus-set issue.** State explicitly whether the same nontarget odors appear on each day of overtraining. If the data allow, repeat the margin and representational-separation analyses on a fixed subset of trials that appear consistently across days.
2. **Add significance tests.** Report at minimum a permutation test or linear mixed-effects model testing whether the slope of the margin/representational similarity vs. days of overtraining is significantly different from zero across animals.
3. **Re-frame the reversal section.** Either present it as a forward-looking prediction for future experiments (removing it from the list of central contributions), or ground it in the available data.
4. **Tone down the PCA claims.** Acknowledge explicitly that the PCA axes are recomputed each session, so the visual comparison is illustrative only.

## Score and Decision

The paper tackles a timely and interesting question — whether sensory representations continue to evolve after behavior plateaus, analogous to grokking in deep learning. The reanalysis of existing neural data provides suggestive evidence, and the synthetic model offers a plausible mechanistic account. However, the empirical core has two significant gaps: (1) the unaddressed confound of whether the same stimuli are compared across days, which could affect the interpretation of the margin and separation trends, and (2) the lack of quantitative validation connecting the model to the neural data. The trends are visually consistent across all 4 mice, which prevents the first issue from being fatal, but the paper would be substantially strengthened by addressing both. With these revisions, the paper would make a valuable contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>