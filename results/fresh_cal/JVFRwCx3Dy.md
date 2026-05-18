Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper investigates the factors enabling in-context learning (ICL) in autoregressive models using a controlled image-classification setup with GPT-2. It argues that (1) exact conceptual repetitions (iCopy) in training sequences are a primary driver of ICL — more important than previously studied properties like burstiness or skewed distributions — and (2) the complexity of the in-weight learning (IWL) objective is crucial for stabilizing ICL and eliminating its transient behavior. The key empirical finding is that a single repetition of the query image in the context suffices for ICL to emerge, and combining repetitions with a sufficiently complex IWL objective (e.g., instance discrimination) yields non-transient ICL performance.

## Strengths

- **Repetitions alone suffice for ICL and dominate previously emphasized properties.** Section 4.1 and Figure 3 demonstrate that sequences with a single instance copy (iCopy, low burstiness) achieve similar peak ICL accuracy as high-burstiness sequences, while low-burstiness without repetition yields no ICL. Figure 3c further shows that repetitions with a uniform distribution outperform high-burstiness with a Zipfian distribution, directly disambiguating repetition from skewness as the primary causal factor.

- **Combining repetitions with a complex IWL objective produces non-transient ICL.** Section 4.2 and Figure 4a show that iCopy reduces ICL transiency compared to the burstiness-only baseline. Section 5 (Figure 7c) shows that an instance-discrimination IWL task paired with repetitions yields strong and stable ICL with no transiency — a result prior controlled studies could not achieve.

- **Systematic demonstration that IWL objective difficulty controls ICL emergence.** Section 5 provides four independent manipulations — increasing the number of classes, skewed distribution, label noise, and instance discrimination — all showing monotonic ICL improvement as the IWL task becomes harder. The cleanest experiments (number of classes in Figure 6a, skewed distribution in Figure 6b) establish a clear causal relationship without confounds.

- **Scales to realistic visual datasets where prior baselines fail.** Section 4.4 (Figure 4b) shows that the best iCopy+burstiness setup achieves strong 4-way-2-shot ICL on CIFAR-100, Caltech-101, and DTD, while the baseline (burstiness-only) shows no ICL on any of these datasets, supporting the generalizability of the findings beyond Omniglot.

- **Mechanistic link to induction heads.** Section 4.3 (Figure 5) demonstrates that in a minimal 3-layer, 1-head GPT-2, an induction circuit (label-image attention in L1, query-to-label attention in L2) forms only when trained with repetitions+burstiness; the burstiness-only baseline produces no such circuit and no ICL, linking the data property to a specific learned mechanism.

## Weaknesses

### Fatal

None.

### Major

- **The instance discrimination experiment confounds IWL difficulty with data mix, weakening the causal attribution.** In the instance discrimination experiment (Section 5, Figure 7c), the paper switches from a supervised setup (90% in-context + 10% standard sequences) to a self-supervised setup (100% in-context sequences). This changes both the learning objective *and* the data distribution simultaneously. The paper attributes the resulting strong, stable ICL to the "hard IWL task," but the data mix change is an equally plausible explanation — models trained exclusively on in-context sequences may trivially learn to use context because there is no competing IWL signal from standard sequences. The paper's central claim about the *balance* between look-up and IWL difficulty would benefit from an experiment where IWL difficulty is varied monotonically while keeping the data mix constant (which the number-of-classes and skewed-distribution experiments do, making them cleaner evidence).

### Minor

- **No quantitative metric for transiency.** The paper claims iCopy reduces ICL transiency (Section 4.2, Figure 4a) and that instance discrimination eliminates it (Figure 7c), but no quantitative transiency metric is defined (e.g., decay rate, area under the ICL curve after peak, time to drop below a threshold). The evidence is visual from training curves. Given the acknowledged variance across seeds (Section 6), a quantitative measure would substantially strengthen confidence in this claim.

- **Induction head analysis is qualitative/anecdotal.** The mechanistic analysis in Section 4.3 (Figure 5) is based on attention maps from a single evaluation example at a single training snapshot. While the simplified architecture (3-layer, 1-head) makes one-head-per-layer visualization informative, the paper would benefit from a quantitative induction head metric tracked over training (e.g., an induction score following Olsson et al. 2022) to substantiate the claim that repetitions drive induction head formation and that this formation correlates with ICL performance across conditions.

- **The gap between n-gram repetitions in text and image-label copies in the controlled setup is not fully bridged.** The paper's motivation (Figure 1) uses n-gram repetitions in pretraining corpora, but the controlled experiments use exact image-label pair copies. The paper notes that repetitions "could refer to n-gram repetitions in textual data or exact image copies" (abstract) and that iCopy "can be an exact copy or an augmented version" (Section 4), but does not test whether near-duplicates or augmented versions suffice. This limits the strength of the claimed connection to LLM pretraining.

- **The number-of-classes experiment (Figure 6a) does not specify whether total training samples or per-class samples are held constant.** This matters because increasing the number of classes while keeping total samples fixed reduces per-class samples (making IWL harder via data scarcity), while keeping per-class samples fixed increases total samples (introducing a confound). The paper should state which control was used. The skewed distribution experiment (Figure 6b) is cleaner in this regard, as it explicitly holds total samples constant.

- **Peak ICL accuracy values and variance are not reported for the main comparisons.** The paper states the iCopy and high-burstiness conditions achieve "similar ICL peak performance" (Section 4.1) but does not provide quantitative peak accuracy values, confidence intervals, or error bars for the curves in Figures 3, 4, and 6. Given the paper's own acknowledgment of sensitivity to initialization and seed variance (Section 6), this quantification would help the reader assess the reliability of the comparisons.

### Trivial

- The paper could briefly describe the image embedding method (e.g., linear projection or small CNN) used to map images into the GPT-2 token space, as this affects reproducibility.
- An ablation of the 90%/10% in-context/standard sequence mix ratio would be informative but is not necessary.

## Nice-to-Haves

- A factorial experiment that systematically varies look-up support (with/without iCopy) × IWL difficulty (e.g., 200 vs. 1600 classes) while controlling for all other factors would directly test the paper's central "balancing" hypothesis and cleanly separate the two factors.
- An ablation testing whether exact copies are necessary or whether augmented/near-duplicate versions suffice would clarify the mechanism and strengthen the connection to LLM pretraining where repetitions are rarely exact.
- A small-scale synthetic text experiment (e.g., n-gram copy tasks with token sequences) would demonstrate generalizability beyond the image classification domain.

## Removed Points

- **Label noise confound claim** (Harsh Critic's Critical Issue 2, part about label noise "incentivizing reliance on context"): The reviewer argued that corrupting labels in standard sequences "could directly incentivize reliance on context rather than simply making the IWL task harder." However, standard sequences (A-B-C-D-E-F-G-H) contain samples from different non-query classes with no repetition, so there is no relevant context to "look up" during standard-sequence training. The model cannot use context to overcome noisy labels in these sequences. The primary effect is making IWL harder by providing incorrect supervision — consistent with the paper's interpretation. This criticism is therefore based on a misunderstanding of the setup.

- **"The paper should be accepted if the authors can provide..."** — This is an overall assessment/qualification, not a weakness. The review should evaluate the paper as submitted.

- **"Critical architectural details missing from main text (appendix stripped)"** — Per the rules, appendix-stripping is a parser artifact; these details exist in the original submission.

- **Generic formatting/style nitpicks and reproducibility complaints about undisclosed hyperparameters** — Removed per rules.

## Novel Insights

The two reviews converge on the paper's core contributions but differ in severity assessment. The most interesting observation from synthesizing them is that the paper's main conceptual advance — that repetitions (a simple, specific mechanism) dominate burstiness and skewness (broader statistical properties) — is well-supported by the clean experiments in Section 4. However, the paper's secondary claim about the balancing of look-up and IWL difficulty is only partially evidenced because the most dramatic demonstration (instance discrimination eliminating transiency) changes multiple variables at once. This tension between a compelling conceptual framework and confounded experimental execution is the central unresolved issue. A clean 2×2 factorial experiment (look-up strength × IWL difficulty) would resolve it directly.

## Suggestions

1. **Define and report a quantitative transiency metric** (e.g., ICL accuracy at 1.5× the step where peak occurred, or area under the ICL curve after the peak) for all main experiments. This would convert the visual transiency claims into reproducible, comparable numbers.

2. **For the instance discrimination experiment**, either control the data mix (use the same 90/10 split with instance discrimination applied to the 90% in-context portion) or explicitly acknowledge the confound and present it as a combined intervention rather than isolated evidence for IWL difficulty.

3. **Report peak ICL accuracy values with error bars** over multiple seeds for the key comparisons (Figure 3a, 4b, 6a), especially since the paper acknowledges sensitivity to initialization.

4. **Clarify the control in the number-of-classes experiment**: state whether total training samples or per-class samples are held constant across the 200→1600 range.

5. **Strengthen the mechanistic analysis** by computing a quantitative induction-head score (e.g., the fraction of attention from query to correct label tokens) over training steps for each condition, rather than showing a single qualitative attention map.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>