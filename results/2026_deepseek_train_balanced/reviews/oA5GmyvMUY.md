Now let me produce the final consolidated review.

## Summary

The paper proposes a defense against label-flipping attacks in federated learning for autonomous vehicles, combining PCA dimensionality reduction with Multiclass SVM to detect malicious participants based on their model updates. The experiments use three physical SunFounder Picar vehicles and benchmark datasets (CIFAR-10, A2D2). However, the paper's central weakness is decisive: the proposed defense is never quantitatively evaluated. The Results section studies only the attack's impact, and the defense claims are entirely unsubstantiated.

## Strengths

- **Physical hardware deployment**: The experiments use three SunFounder Picar vehicles with an integrated camera and a custom 5K-image dataset (Section 3, line 29). Testing on physical hardware rather than pure simulation is a genuine positive differentiator from purely simulation-based FL defense work.

## Weaknesses

### Fatal

- **The defense mechanism is never quantitatively evaluated.** The Results section (Section 4, lines 184–190) exhaustively describes the attack's impact (source class recall loss, accuracy degradation across availability levels α) but contains zero quantitative data about the defense. The only mention of the defense is a single qualitative paragraph asserting that it "enables the detection" and leads to "no accuracy lost" (line 189). No detection rate, false-positive rate, accuracy-with-defense vs. without-defense comparison, or ablation is provided. The abstract claims the method "prevent[s] nearly 15% of accuracy drop" and achieves "reduction the attack success rate," but these specific numbers never appear in the body. A paper whose central contribution is a defense mechanism must present evidence that the defense works; this paper does not, rendering the core claim unsupported.

### Major

- **No comparison against existing defense baselines.** The related work (Section 2) discusses FoolsGold, kernel-density-based methods (Li et al., 2023b), output-layer inspection approaches (Jebreel et al.), and QPSO-based methods (Yamany et al., 2023), yet the experiments compare against none of them. Without baselines, there is no way to assess whether the proposed method improves upon, matches, or underperforms existing approaches.

- **Method description is too vague to be reproducible.** Several critical details are missing. (1) The "classes" in the Multiclass SVM are never defined — do they correspond to participants, to data labels, or to something else? The text says "differentiate the M class with the all the different training data" (line 79–80), which is ambiguous. (2) The Outlier Score formula (Eq. 3, line 82) uses $y_i$ and $\hat{y}_i$ without defining what these quantities refer to in the context of model-update analysis — the standard interpretation (predicted vs. true labels) would imply the server has ground-truth labels for participants' data, defeating FL's purpose. (3) Algorithm 3 describes operations such as "Test the w model and compute $\hat{y}_{i,k}^{L}$" (line 165) without specifying the testing procedure or what $\hat{y}_{i,k}^{L}$ represents. A reader cannot implement this method from the description.

### Minor

- **N=3 participants with one malicious is a trivial setup.** With only three participants and one adversarial, simple majority-based or distance-based filters would trivially identify the outlier. The paper acknowledges this as a limitation (lines 198–199), but it severely limits the generality of any conclusions that could be drawn even if the defense had been evaluated.

- **IID data only.** The experiments use only IID data distribution (line 34). Non-IID data is the standard stress test for FL robustness defenses, and its absence means a key practical challenge is unaddressed.

- **Incoherent example.** The paper illustrates the label-flipping attack with "red light → green light" in the context of CIFAR-10 (line 43). CIFAR-10 does not contain traffic-light classes (its classes are airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck), making this illustration nonsensical and suggesting confusion between the custom AV dataset and CIFAR-10.

- **Insufficient experimental repeats.** Line 184 states each condition is run only three times, which provides weak statistical reliability. (Line 43 claims 10 repeats — the paper is internally inconsistent on this point.)

### Trivial

- The related work discussion in Section 2 (lines 18–20) is overly broad and loosely connected to the label-flipping defense focus, spending substantial text on general FL applications in AVs that are not directly relevant.

## Nice-to-Haves

- A false-positive analysis would be important for a defense that claims to "never allow[] any updates from that participant" (line 189), as blocking honest participants with divergent data (common in non-IID settings) could degrade model quality. The absence of this analysis is a lost opportunity.

## Removed Points

- **"Algorithm 3 is garbled with '2210::'"**: This is a PDF parsing artifact, not an author error. Removed per formatting artifact rule. The underlying conceptual clarity issues are retained in Major.
- **Grammar/style criticisms**: Removed per instruction that these are parser artifacts, not author errors.
- **"No false-positive analysis"**: Moved to Nice-to-Haves since the defense wasn't evaluated at all — this is a missing analysis among many.
- **Strength about "lightweight defense relative to computational overhead"**: Removed because the defense is not evaluated, so computing a strength about its efficiency is premature and conflicts with the verified fatal weakness.
- **Strength about "systematic evaluation of attack impact"**: This evaluates the attack, not the defense. Since the paper claims a defense contribution, describing the attack well without evaluating the defense is not a genuine strength for the claimed contribution. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviewers' inputs converge on the fundamental observation that a defense paper must evaluate its defense, but this is a structural expectation rather than a novel insight.

## Suggestions

1. **Add a quantitative defense evaluation**: At minimum, a table comparing global model accuracy with and without the defense across multiple poisoning levels (e.g., 10%, 20%, 33% of participants malicious) and different α values. Report detection rate, false-positive rate, and accuracy over rounds.
2. **Compare against at least 2–3 baselines** from the related work (e.g., Krum, FoolsGold, or kernel-density filtering) on the same setup.
3. **Increase participant count** to at least 10–20 in simulation, even if physical hardware is limited to 3. Add non-IID data partitions.
4. **Clarify the method**: Define what $y_i$, $\hat{y}_i$, and the MCSVM classes represent concretely in the update-analysis setting; specify the detection threshold and how it is set.
5. **Resolve internal inconsistency**: Align the reported number of experimental repeats (3 vs. 10) and fix the CIFAR-10/traffic-light example.

## Score and Decision

**Score**: 2.0 — The paper's core claim (a defense against label-flipping) is entirely unsupported by evidence. The Results section does not evaluate the proposed defense. Even setting aside all other issues, this single fatal gap means the paper cannot be accepted in its current form. The physical hardware deployment and attack analysis are positives, but they do not rescue the absent defense evaluation.

**Decision**: Reject

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>