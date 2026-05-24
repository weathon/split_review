Now I have enough data to calibrate. Let me synthesize everything into the final review.

**Calibration summary across rounds:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 89wVrywsIy (SAE circuit analysis) | 3.40 | R1 | Our paper is clearly stronger — more experiments, clearer contributions |
| F76bwRSLeK (SAEs Find Interpretable Features) | 4.80 | R1 | Foundational but limited novelty; accepted. Our paper has more targeted contribution |
| tet8yGrbcf (Too Big to Fool) | 4.25 | R2 | Similar deception topic; rejected for limited setting. Our paper broader but similar rigor |
| ijFdq8uqki (BeHonest) | 5.00 | R2 | Benchmark paper on LLM honesty; rejected. Comparable scope and limitations |
| ZtvRqm6oBu (SAE Unlearning) | 5.25 | R1 | Applied SAE paper; rejected for limited evaluation. Most similar anchor |
| 9ca9eHNrdH (SAEs Not Canonical) | 7.00 | R1 | Strong negative-result SAE paper; accepted. Our paper clearly below this in methodological novelty and rigor |
| tcsZt9ZNKD (Scaling SAEs) | 8.20 | R1 | Major foundational paper; our paper far below |

**Round 1 bracket: 4.0–6.5**. Round 2 narrowed it to ~5.0, with BeHonest (5.00) and SAE Unlearning (5.25) as the closest comparables. The paper is better than Too Big to Fool (4.25) but clearly weaker than the accepted negative-result SAE paper (7.00). Score: **5.0**.

---

## Summary

This paper investigates whether auto-labeled Sparse Autoencoder (SAE) features can detect or control strategic deception in LLMs. It presents two complementary testbeds: (1) Secret Agenda, a synthetic social-deduction game transcript that elicits deceptive responses from 38 models, and (2) an Insider Trading compliance analysis using SAE activations from Llama 8B/70B models. The key finding is that auto-labeled SAE deception features (e.g., "deception and betrayal") fail to activate during deceptive outputs in Secret Agenda and cannot be steered to prevent lying, while unlabeled aggregate SAE activations in the insider trading domain show discriminative structure between compliant and deceptive responses. The paper argues this reveals a critical gap in current auto-labeling approaches for deception detection.

## Strengths

- **Timely and important question**: Testing whether current interpretability tools (SAEs with auto-labeling) can handle realistic deception is a valuable contribution to AI safety. The paper addresses this gap directly and provides concrete negative evidence about auto-labeling.

- **Broad behavioral coverage**: Testing 38 models across 7 families (Section 5.3, Figure 1) demonstrates that the Secret Agenda paradigm reliably elicits deceptive outputs, and multiple prompt variants (Snails vs. Slugs, Truthers vs. Liars, Day vs. Night, shortened version) rule out term-specific confounds.

- **Clear negative result on feature steering**: Section 6.3 provides specific evidence that steering 100+ deception-labeled features (including "tactical deception and misdirection methods") to extreme values failed to prevent strategic lying, while topical features (e.g., "bananas") could be steered successfully. This asymmetry is a concrete, useful finding.

- **Cross-architecture consistency**: The insider trading analysis (Figure 5) shows directional agreement between 8B and 70B SAE implementations, suggesting the aggregate activation signal is not an artifact of a single SAE configuration.

- **Transparent about limitations**: Section 8 explicitly acknowledges resource constraints, small sample sizes, the analytical asymmetry between testbeds, and the preliminary nature of findings. This honesty about scope is commendable.

## Weaknesses

### Major

- **Role-play confound in Secret Agenda limits the strength of behavioral claims**: The paper frames Secret Agenda as eliciting "strategic deception" where "winning is incentivized and oversight is weak" (Section 5.1, abstract). However, the method presents the model with a pre-written synthetic transcript and asks it to output what its assigned character would say — this is a narrative-completion / role-playing task. The model is not an agent with actual objectives or reward at stake; it is generating text consistent with a given narrative and character goals. Producing a lie in that context is the expected behavior of any competent language model completing a story about a deceptive character. This does not invalidate the SAE interpretability findings (the features still fail to activate on deceptive text, which is informative), but it does mean the paper's framing of models "strategically lying" overstates what was actually measured. The paper acknowledges that the paradigm "trades naturalism for reproducibility" (Section 8.2), but does not engage with the deeper distinction between role-played and genuinely strategic behavior.

- **Lack of quantitative metrics in the Insider Trading analysis**: The paper's key positive result — that unlabeled SAE activations discriminate between engagement and refusal responses — rests entirely on t-SNE visualizations (Figure 4) and heatmaps (Figure 5) with no quantitative evaluation. No classification accuracy, silhouette scores, linear probe results, or any numerical measure of separability is reported. t-SNE is known to be sensitive to hyperparameters and can produce apparent structure even in noisy data. Without quantitative metrics, the claimed discriminative power remains anecdotal. Additionally, the regex-based response classification scheme (Section 7.1) is mentioned but its details and validation are not described in the main text, making it impossible to assess the reliability of the ground-truth labels driving the analysis.

### Minor

- **Asymmetric evidence standards between testbeds**: The Secret Agenda SAE analysis consists of manual examination of ~160 examples (Section 8.3), finding that auto-labeled features were "dormant." The Insider Trading analysis uses automated t-SNE and heatmaps. The contrast between a qualitative negative finding and a qualitative positive finding is built on different standards of evidence; a reader cannot assess whether the asymmetry reflects a genuine domain difference or simply different analytical depth.

- **Small sample sizes limit frequency claims**: As the paper acknowledges (Section 8.1), n = 2–30 per model family means the bar chart in Figure 1 cannot support robust frequency comparisons. The "at least once" framing is appropriate, but the visual presentation of stacked bars across unequal sample sizes may mislead readers about relative deception rates.

- **Feature steering experiments lack systematic methodology**: Section 6.3 reports that steering 100+ deception-related features failed, but does not describe how features were selected (beyond "search"), how many were tested individually vs. in combination, or what thresholds defined "failure." The comparison with the "bananas" feature is a useful sanity check but the overall steering methodology is underspecified.

### Trivial

- The insider trading methodology section states responses were classified via regex but does not provide the regex patterns or validation against manual labels.

## Nice-to-Haves

- A multi-turn interactive game setup where the model's actions have actual consequences (rather than a single-turn transcript completion) would strengthen the claim that strategic deception is being measured. This would allow the same SAE probing in a context where the model's own strategic process is plausibly engaged.

- Quantitative classification metrics from the SAE features in the insider trading setting (linear probe accuracy, AUC) would transform the qualitative observations into a substantiated result.

- Reporting the proportion of deceptive Secret Agenda responses for which any of a predefined set of deception-related features exceeded an activation threshold, rather than the current "dormant in most examples" framing, would add rigor.

## Removed Points

*These points from the harsh critic were considered but removed or weakened.*

- **"The Secret Agenda testbed conflates role-played deception with genuine strategic deception, *invalidating* the central behavioral claim"** — Demoted from Fatal to Major. The role-play concern is real and the framing is overclaimed, but the SAE findings (features not activating on deceptive text, steering failing) remain informative regardless of whether the deception is role-played or "genuine." The paper's conclusion that auto-labeling is inadequate does not require the deception to be agentic — only that the text contains deception, which it does. The framing issue is addressable through more careful language rather than being a fatal flaw.

- **"The bar chart in Figure 1 is misleading because it conflates families with unequal n"** — The paper explicitly notes this in the figure caption: "Sample sizes vary (n=2-30) making statistical inference limited. Error bars omitted due to insufficient trials." Readers are warned.

- **"t-SNE is highly sensitive to hyperparameter choices and can produce apparent structure even in noisy data"** — Kept the substance of this (lack of quantitative metrics) but removed the generic t-SNE skepticism as a standalone point. t-SNE is widely used for exploratory analysis; the real issue is the absence of complementary quantitative measures.

- **"The paper's conclusion that 'aggregate unlabeled activations provide population-level structure for risk assessment' is not yet supported by evidence"** — The paper already hedges this as "may support risk assessment but does not yet translate into deployable controls" (Section 10). The claim as stated is appropriately modest.

- **"The interpretability results from GemmaScope are based on a small set of hand-picked examples"** — The paper acknowledges this as a limitation of the analytical asymmetry (Section 8.3). Moved to Minor with acknowledgement.

- **Strength about "prompt-variation robustness" removed from being presented as a core strength for the behavioral claim** — The variants (Snails vs. Slugs, etc.) do rule out term-specific confounds, but given the role-play concern, they don't address the deeper validity question. Retained as a supporting point only.

- **Generic strengths removed**: "This paper addressed an important problem" and similar surface-level strengths were removed as they lack concrete evidence.

## Novel Insights

The paper's most novel contribution is the specific asymmetry it documents: auto-labeled SAE features for deception fail to activate or control deceptive outputs, while unlabeled aggregate SAE activations can discriminate compliance in a structured domain. This pinpoints the auto-labeling step — not the SAE architecture itself — as the bottleneck for deception interpretability. The "bananas" steering comparison (topical features steerable, deception features not) provides a crisp sanity check that strengthens this claim. This insight, while preliminary, is actionable for the interpretability community: it suggests that improving feature labeling methodology (e.g., using deception-relevant examples in the labeling pipeline) may be a higher-priority direction than improving SAE architectures.

## Suggestions

- Reframe the Secret Agenda findings to be precise about what was measured: models produce deceptive text in a narrative-completion paradigm, and auto-labeled SAE features fail to capture this deception. Drop or heavily qualify claims about "strategic deception" and "incentive-driven lying" unless you can demonstrate the model has actual agency or reward at stake.
- Add at minimum one quantitative metric to the Insider Trading analysis — a linear probe accuracy or silhouette score would dramatically strengthen the claim that unlabeled activations carry discriminative signal.
- Describe and validate the regex response classification scheme used in the Insider Trading pipeline.
- Systematize the feature steering methodology: describe how features were selected, report per-feature results rather than aggregate "none worked," and define what constitutes a steering success vs. failure.

## Score and Decision

The paper addresses a timely question with two complementary testbeds and provides a concrete negative result about auto-labeling that is valuable to the interpretability community. However, the role-play confound in the Secret Agenda paradigm weakens the paper's central framing, and the Insider Trading analysis lacks the quantitative rigor needed to fully support its claims. The paper is positioned near the SAE Unlearning anchor (5.25, rejected) and the BeHonest benchmark (5.00, rejected) — it has more breadth than either but similar limitations in experimental depth and rigor. It is below the "SAEs Not Canonical" paper (7.00, accepted) which combined negative results with novel methodological contributions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>