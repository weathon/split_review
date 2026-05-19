Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper formalizes the problem of active continual learning (ACL)—integrating active learning (AL) into continual learning (CL) scenarios—and conducts a systematic empirical study across three CL scenarios (domain-IL, class-IL, task-IL) and two modalities (image, text). The main contributions are: (1) a formal ACL framework with a warm-started proxy model, (2) the finding that ACL with limited labelled data can match full-data CL in domain-IL, (3) the "forgetting-learning profile" diagnostic that reveals a gap in class-IL (no studied method occupies the ideal low-forgetting + quick-learning quadrant), and (4) actionable guidelines for pairing AL and CL algorithms.

---

## Strengths

1. **Formal ACL problem definition.** Section 2.3 (Algorithm 1) provides a precise algorithmic formulation of ACL, including the warm-started proxy model and iterative AL rounds within each CL task. This goes beyond prior work that assumes independent annotation and gives a clear framework for studying the AL–CL interplay.

2. **Empirical finding: ACL with limited data matches full-data CL in domain-IL.** Figure 2 and the accompanying text show that ACL methods using only 10–30% of labelled data can surpass standard CL methods trained on the full dataset in the domain-IL scenario (P-MNIST, ASC). This is a non-obvious and practically relevant result.

3. **Forgetting-learning profile as a diagnostic tool.** The 2-D visualization (forgetting rate vs. learning curve area) introduced in Section 2.3 and shown in Figures 7/8 is a useful analytical lens. It reveals that in class-IL, methods cluster into two non-ideal regions—quick learners with high forgetting (Ft, EWC) and slow learners with low forgetting (ER)—with no method occupying the ideal quadrant. This cleanly identifies a specific gap in current ACL methods.

4. **Sequential vs. independent labelling comparison.** Table `tab:ind-ret` and the discussion in Section 3.1 provide a nuanced finding: sequential labelling yields quicker learners but higher forgetting, and its benefits depend on the CL scenario (beneficial in domain-IL, detrimental in class-IL). This is a concrete, evidence-based contribution.

5. **Algorithm selection guidelines.** The paper distills its empirical results into actionable recommendations: experience replay (ER) is the best CL method across scenarios; uncertainty-based AL works best in domain-IL; diversity-based AL (kMeans) is more suitable for class-IL due to poor calibration. These are supported by the experiment tables.

6. **Broad experimental coverage.** The study spans three CL scenarios (domain-, class-, task-IL) and two modalities (image: P-MNIST, S-MNIST, S-CIFAR10; text: ASC, 20News), with multiple AL and CL algorithms. This systematic coverage strengthens the generalizability of the findings.

---

## Weaknesses

### Fatal
None.

### Major

1. **Factual error in the contributions summary (line 31).** The paper's own list of contributions states that the forgetting-learning profile reveals clusters of *"slow learners with high forgetting rates and quick learners with low forgetting rates."* However, the actual results reported in Section 3.2 (line 157) for class-IL—the main scenario where the gap is identified—describe *"quick learners with high forgetting (Ft and EWC)"* and *"slow learners with low forgetting (ER)."* These are the opposite diagonal: the contributions list describes the ideal/bad diagonal (quick+low, slow+high), while the actual finding is the other diagonal (quick+high, slow+low). This is a real inconsistency in the paper's self-summary that must be corrected. It does not invalidate the core empirical finding (the class-IL gap is still clearly described in Section 3.2), but it makes the paper's introductory summary unreliable.

### Minor

2. **No variance shown on forgetting-learning profile plots.** Figures 7 and 8 (referenced as `\Cref{fig:forgetting-learning-profile}` and `\Cref{fig:forgetting-learning-profile-cv}`) plot each ACL method as a single point. The paper reports averages over 6 runs with different task orders and seeds (line 122), but the figures show no error bars, confidence ellipses, or standard deviations. The central claim that methods group into "distinct regions" would be stronger if the reader could assess whether these clusters are statistically separable, especially given that some points appear close to quadrant boundaries. (Note: standard deviations for accuracy tables are reported in the appendix; the issue is specific to these profile plots.)

3. **Key comparative claims lack formal statistical support.** The paper makes actionable recommendations such as "uncertainty-based AL methods perform best in domain-IL" and "diversity-based AL is more suitable for class-IL" (line 33). While the underlying accuracy tables are in the appendix, the main text presents only relative accuracy figures (Figures 3, 4) without significance tests or confidence intervals. Given that many differences are small (2–5%), a reader cannot assess whether these patterns are reliable or seed-dependent. Adding paired significance tests or explicitly noting which differences are robust would strengthen the guidelines.

4. **Normalized forgetting analysis limited to one simple dataset.** The analysis of normalized forgetting ratio vs. annotation budget (Figure `fig:nfr-mnist`, line 164) is only shown for S-MNIST. The paper itself acknowledges that S-MNIST is simple enough that nearly all methods achieve near-perfect accuracy. The claim that BADGE "consistently scores lower forgetting rates" (line 164) may not generalize to harder datasets like S-CIFAR10. This limitation should be acknowledged or the analysis extended.

5. **Annotation budget differences and dataset comparability not discussed.** The annotation budget varies across datasets (10% for P-MNIST/S-MNIST, 25% for S-CIFAR10, 30% for ASC, 20% for 20News) as noted on lines 121–122. Higher budgets make ACL closer to supervised CL, so the apparent advantage of ACL in domain-IL over class-IL may partly reflect budget differences. The paper does not discuss this confound.

### Trivial

6. **Formatting: the `\textsc{Ft}` command on line 129 has an anomalous closing parenthesis** (`\textsc{Ft)}` instead of `\textsc{Ft}`)—a likely parser artifact, but worth noting for the final version.

---

## Nice-to-Haves

- **Add error bars/confidence ellipses** to the forgetting-learning profile plots to visually assess cluster separability.
- **Include a random-subsample baseline** for the ACL vs. full-data CL comparison: comparing ACL to CL on a random subsample of the full data at the same budget would isolate the benefit of AL-driven selection beyond data quantity.
- **Discuss computational cost.** ACL requires repeated AL querying and proxy model retraining within each task. A brief note on runtime or query budget would help practitioners evaluate the method.
- **Extend normalized-forgetting analysis** to at least one harder dataset (e.g., S-CIFAR10) to test generalizability.

---

## Removed Points

These points were flagged in the source reviews but are removed or demoted for the reasons stated:

- **"The abstract misrepresents the paper's own findings" (Harsh Critic).** The actual error is in the **contributions list** (line 31), *not* in the abstract (lines 3–12). The abstract correctly describes only a "gap" without specifying region labels. The error itself is real and retained as Major weakness 1 above; the misattributed location is corrected. *(Partially kept, corrected.)*

- **"The forgetting-learning profile is more an analytical visualization than a proposed method" (Harsh Critic).** This is a semantic quibble that does not affect the paper's actual contribution. The profile is indeed a diagnostic tool, which is appropriately described. *(Removed — not a genuine weakness.)*

- **"Absolute accuracy numbers relegated to appendix" (Harsh Critic).** The paper explicitly directs readers to appendix tables (lines 129, 132) and notes standard deviations are provided there. This is a format choice, not a flaw. *(Removed — reasonable formatting decision.)*

- **"Proxy model interaction is a known challenge not deeply discussed" (Harsh Critic).** The paper acknowledges this design choice (lines 86–87) and contrasts it with independent AL. Deeper analysis would be nice but is not required for the paper's empirical scope. *(Demoted to Nice-to-Have.)*

- **"The profile is mostly useful for diagnosing deficits" (Harsh Critic).** This is a true statement but not a weakness—identifying a gap is the entire purpose of the analysis. *(Removed — not a weakness.)*

- **Strength Finder strengths about importance of the problem/generic praise.** Any generic or superficial-sounding strength language from the Strength Finder was assessed and the specific, evidence-grounded strengths were retained in the Strengths section above. No strength was removed from the final list, but generic framing was compressed.

---

## Novel Insights

The most interesting insight that emerges from examining these reviews together is the tension between the paper's ambitious self-summary (which overstates or even inverts the observed clustering pattern) and the actual nuanced finding that the class-IL gap is the *absence* of ideal methods rather than the presence of a specific configuration. The harsh critic correctly identifies this self-contradiction. Meanwhile, the strength finder correctly identifies the substantive contributions. The critical meta-observation is that the paper's actual empirical results are stronger and more honest than its contribution list suggests—the class-IL gap is a genuine negative result worth reporting, but the contribution list tries to frame it as a positive "discovery of two regions" and gets the direction wrong. The paper would be improved by embracing the negative-result framing more directly rather than over-interpreting the pattern.

---

## Suggestions

1. **Fix the factual error in contribution item 3 (line 31).** Replace "slow learners with high forgetting rates and quick learners with low forgetting rates" with the correct observation: methods cluster as *quick learners with high forgetting* and *slow learners with low forgetting* in class-IL. Or, more precisely, state that no method occupies the ideal region.
2. **Add standard deviation ellipses** (or at least note the range across runs) to the forgetting-learning profile figures to give readers a sense of cluster separability.
3. **Add a brief note** about the annotation budget confound (higher budgets make ACL closer to supervised CL) to qualify cross-dataset comparisons.
4. **Explicitly note** which of the guideline-level findings are robust across all datasets vs. tentative based on limited evidence (e.g., the BADGE forgetting finding is only on S-MNIST).
5. **Consider adding** a random-subsample-at-same-budget baseline to isolate the AL selection benefit.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>