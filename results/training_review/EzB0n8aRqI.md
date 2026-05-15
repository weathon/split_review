Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper formalizes open-set noise (where the true label belongs to an unknown class) within learning with noisy labels (LNL) by extending the noise transition matrix to account for outlier classes. It theoretically analyzes error-rate inflation under open-set vs. closed-set noise in two training regimes (fitted and overfitted), finding that open-set noise is less harmful to classification accuracy. Experiments on constructed datasets (CIFAR100-O, ImageNet-O) and entropy-based detection analysis support these claims while revealing that entropy is effective only for "easy" (not "hard") open-set noise.

## Strengths

- **Formal complete noise transition matrix (Definition 3.1).** Extends the standard noise transition matrix to explicitly model confusion from outlier classes (T_out) alongside inlier-class confusion (T_in). This is a clean conceptual advance over prior work (e.g., Xia et al. 2022) that collapsed all open-set noise into a single meta-class.

- **Clear two-case analysis (fitted vs. overfitted).** The paper correctly identifies that the impact of noise depends on whether the model fits the noisy distribution (frozen features + linear classifier) or memorizes labels (deep network trained from scratch). This dual perspective is pragmatically useful and clarifies why different noise types matter in different settings.

- **Theorem 3.7 and empirical validation.** The result that open-set noise causes less error-rate inflation than closed-set noise (under class-concentrated posteriors) is supported by experiments across two datasets (CIFAR100-O, ImageNet-O) and both training regimes (Figure 2a/b). While the theoretical assumption is strong, the empirical consistency strengthens the claim.

- **Identifies the "easy" vs. "hard" open-set noise distinction.** The paper shows experimentally that these two modes exhibit opposite accuracy trends under fitted vs. overfitted cases, and that entropy-based detection works for the former but not the latter (Figure 3). This is a practical finding with implications for sample-selection methods in LNL.

- **Proposes OOD detection as a complementary metric.** Figure 2c/d shows that open-set and closed-set noise affect OOD detection performance in opposite directions to classification accuracy, suggesting that accuracy alone is insufficient for evaluating models under open-set noise.

## Weaknesses

### Fatal

None. The paper's core theoretical and empirical claims are supported at a basic level, though the contributions are modest.

### Major

- **No LNL methods evaluated under open-set noise.** The only experiments (Figure 2) train standard classifiers directly on noisy labels with cross-entropy. The paper therefore cannot substantiate its motivating claim that "further investigation is needed" — we never see whether existing LNL methods (e.g., DivideMix, ELR, sample selection, robust losses, noise transition estimation) break or hold under open-set noise. This is the single largest gap: without any LNL baseline comparisons, the paper is an exploratory analysis rather than a complete study.

- **"Hard" vs. "easy" open-set noise is never formally defined.** The paper uses these terms throughout (Introduction, Section 3.3, Section 4, Section 5, Figure 2, Figure 3) but provides no operational definition — no semantic similarity threshold, no distributional divergence measure, no construction protocol that specifies how "hard" vs. "easy" outlier classes are selected. This makes the analysis ad hoc and unreproducible. The Experiments section says nothing about which classes were chosen as hard vs. easy or why.

- **WebVision open-set test set is introduced but never used.** The abstract and Introduction prominently claim its introduction as a contribution, yet the provided main text contains zero experiments using it. This is a significant mismatch between claimed and delivered contributions.

- **Entropy-based detection analysis is purely qualitative.** Figure 3 shows entropy histograms for different conditions, but the paper reports no quantitative detection metrics (AUC, F1, precision, recall) and provides no detection threshold. The conclusion that entropy is "effective only for easy open-set noise" is supported by visual inspection alone. A quantitative comparison against a baseline method (e.g., max softmax score) is needed.

- **CIFAR100-O and ImageNet-O construction details are absent from the main text.** The paper does not describe which classes were used as inlier vs. outlier, how noise ratios were controlled, or the construction protocol. Figure captions alone are insufficient; without these details the experiments cannot be reproduced or compared against.

### Minor

- **Theorem 3.7 relies on a very strong class-concentrated assumption (p_a → 1).** The paper acknowledges this but does not probe how quickly the result degrades as the assumption is relaxed. The theorem is nearly tautological under the assumption: if a sample is deterministically from one class, open-set noise dilutes probability to other inlier classes, while closed-set noise directly flips the max class. Experiments partially compensate, but an ablation on posterior entropy would strengthen the theoretical claim.

- **OOD detection findings are under-analyzed.** The paper notes that closed-set noise can improve OOD detection and open-set noise degrades it (Figure 2c/d), but this observation is limited to a single descriptive sentence. There is even a potential contradiction in the text — one sentence says open-set noise "degrades OOD detection" and the next says it "leads to steady improvement" — suggesting unclear writing. This non-obvious finding merits deeper investigation (e.g., why does closed-set noise improve OOD scores?).

- **No error bars or variance reported.** The two figures show point estimates without confidence intervals or standard deviations. Even for synthetic-data experiments with controlled noise, single-run results are insufficient to establish reliability.

- **The theoretical ∆E_x analysis assumes knowledge of the clean conditional distribution and noise transition matrix**, which are unavailable in practice. The practical applicability of the theoretical framework is therefore limited, and the paper does not address how practitioners could estimate these quantities.

### Trivial

- Some notation is unnecessarily heavy for simple concepts (e.g., the complete noise transition matrix is a natural block-matrix extension).

## Nice-to-Haves

- A table comparing accuracy and OOD detection for 2–3 representative LNL baselines (DivideMix, ELR, a sample-selection method) under open-set vs. closed-set noise would dramatically strengthen the paper.
- Reporting AUC for entropy-based open-set noise detection across conditions would turn a qualitative observation into a quantitative benchmark.
- An ablation on the class-concentrated assumption (e.g., using CIFAR-100 subsets with varying posterior entropy) would test whether Theorem 3.7's ordering holds as the assumption is relaxed.
- Explaining why closed-set noise improves OOD detection (Figure 2c/d) would be a genuinely novel contribution.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about missing VLM/SSL and robust loss experiments promised in the Introduction.** The Introduction lists these as bullet-point findings, but the main text received does not contain them. These could exist in a stripped appendix (the parser removed such sections from all papers). Per hard rules, this criticism is removed. *If these experiments are genuinely absent from the original submission, this would be a structural flaw; however, I cannot verify that from the extracted text alone.*

- **Criticism that the paper "does not propose a method."** This is a scope-creep criticism: the paper is framed as a theoretical/empirical analysis, not a method proposal. Judging it for lacking an algorithmic contribution is unreasonable given its stated goals.

- **Criticism that Theorem 3.7 is "unsurprising."** While the theorem's result may align with intuition, formalizing and empirically validating intuition has scientific value. The criticism is a matter of taste, not a concrete weakness.

- **Strength about "preliminary experiments with VLMs and SSL models."** This claimed strength references experiments not present in the main text. It is dropped because it conflicts with the verified weakness (lack of visible evidence) and is too speculative.

## Novel Insights

None beyond the paper's own contributions. The reviews identify gaps and missing analyses but do not surface any unrecognized pattern or insight about the paper's results that the authors themselves overlooked. The most interesting direction — why closed-set noise improves OOD detection — is noted by both the harsh critic and this review as an open question, not something the reviews close.

## Suggestions

1. **Add LNL baseline comparisons.** Even 2–3 representative methods (e.g., DivideMix, a sample-selection approach, a robust loss function) tested on CIFAR100-O would transform this from a preliminary exploration into a substantive empirical study.

2. **Formally define "easy" vs. "hard" open-set noise.** Provide a construction protocol (e.g., semantic similarity via WordNet hierarchy or embedding distance) and describe which classes were used for each category. Without this, the paper's central empirical distinction is not reproducible.

3. **Report quantitative detection metrics for entropy-based analysis.** AUC and precision-recall curves for distinguishing open-set from clean samples would replace visual histogram inspection with rigorous evidence.

4. **Use the WebVision open-set test set.** It is advertised as a contribution but absent from all experiments; including it would demonstrate real-world relevance.

5. **Add error bars or confidence intervals** to all experimental figures.

6. **Clarify the contradictory description of OOD detection results** (open-set noise both "degrades" and "improves" OOD performance in adjacent sentences — line 182 has a likely typo).

## Score and Decision

The paper makes modest but genuine contributions: a clean formalization of open-set noise in the noise transition matrix, a theoretical comparison with closed-set noise, and interesting preliminary findings about easy vs. hard open-set noise and entropy-based detection. However, the experimental validation is critically incomplete — no LNL baseline comparisons, no quantitative detection metrics, no operational definition of hard/easy noise, and unused claimed contributions (WebVision test set). These gaps prevent the paper from reaching the bar for a top-tier publication. It reads as a solid workshop paper or a starting point for a more complete study, but not as a finished archival paper.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>