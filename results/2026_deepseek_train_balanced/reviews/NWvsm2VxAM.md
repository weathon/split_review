## Summary

ID-Booth proposes a fine-tuning framework for diffusion models that replaces the standard identity-similarity objective in PortraitBooth with a triplet identity objective (ℒ_TID), using prior preservation images as negatives to reduce overfitting on spurious facial attributes. Evaluated on SD-2.1 and SD-XL with two prompt complexity levels using the Tufts Face Database (105 subjects), the method shows improved diversity over PortraitBooth while maintaining identity consistency. CosFace models trained on ID-Booth-generated data outperform models trained on the original real TFD dataset across five verification benchmarks.

## Strengths

1. **Triplet objective demonstrably preserves diversity where PortraitBooth loses it.** Section 4.1 (lines 140–145) shows that PortraitBooth achieves "drastically worse recall with complex prompts on the FFHQ dataset than DreamBooth," while ID-Booth "does not display the same issues... achieving notably higher recall scores, more similar to DreamBooth." This directly validates the paper's central claim that the triplet formulation avoids overfitting on expression/pose that plagues PortraitBooth's ℒ_ID.

2. **Downstream face recognition evaluation validates practical utility.** Table 3 (lines 164–167) reports that CosFace models trained on ID-Booth-generated data achieve the highest average verification accuracy across all five benchmarks (LFW, CALFW, CPLFW, CFP-FP, AgeDB-30). The direct comparison against models trained on the real TFD dataset provides the strongest evidence for the method's practical value for privacy-preserving face recognition.

3. **Best intra-identity consistency and inter-identity separability among synthetic samples.** Section 4.2 (line 151) reports that "ID-Booth achieves the highest consistency among generated samples of the same identity and the largest separability between synthetic samples of different identities," supported by verification metrics in Table 2 and distribution plots in Figure 3.

4. **Systematic evaluation across two diffusion models and two prompt complexity levels.** The full factorial design (SD-2.1 vs SD-XL × Base vs Complex prompts) in Section 4 strengthens generality. Results are reported separately for all four combinations in Tables 1–3, showing the advantage is consistent across architectures and prompt settings.

5. **Principled mechanistic reasoning for why the triplet fix works.** Section 3.3 (line 94) identifies that ℒ_ID "can lead to overfitting on facial characteristics that might leak into the training identity embeddings, e.g. the expression or pose of subjects." Section 3.4 (line 109) then explains that the triplet formulation "reduces the risk of overfitting on unintentional characteristics of training identities as they are also present in negative examples." This reasoning is precise, testable, and goes beyond a black-box claim of improvement.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Claim scope slightly exceeds evidence on the real-data comparison.** The abstract states that ID-Booth enables training models that "outperform even real-world datasets of a similar scale gathered with suitable consent." This claim is supported only against the Tufts Face Database (TFD), a single dataset of 105 subjects captured in a constrained laboratory setting. While the comparison with TFD is meaningful (it is the source of training data for fine-tuning and the paper's scope is small consented datasets), the abstract's phrasing could be read as a broader claim about any similarly-sized real dataset. The paper would benefit from explicitly noting that this comparison is against one specific dataset whose constrained-laboratory collection limits its utility for in-the-wild recognition, rather than a general claim.

2. **No ablation or sensitivity analysis of the triplet margin m.** The margin in ℒ_TID (Equation 7, line 106) is defined as a "non-negative margin" but no ablation study is provided showing how varying m affects the diversity-consistency trade-off. Since the advantage over PortraitBooth is attributed to the triplet formulation rather than the simpler ℒ_ID, the reader cannot assess whether the reported improvements are robust across margin choices or contingent on a specific tuned value. This is the most significant evidential gap.

3. **Identity consistency evaluation partially relies on the same model architecture used in training.** The triplet objective (line 124) computes ArcFace features, and the consistency/separability evaluation in Table 2 and Figure 3 also uses ArcFace features (line 126). This creates modest circularity—the method optimizes ArcFace similarity, then ArcFace-based metrics show improvement. The downstream evaluation with a different architecture (CosFace, Table 3) partly addresses this, but the paper's central consistency claims rest mainly on ArcFace-vs-ArcFace evaluation. Reporting consistency using a different face recognition backbone would strengthen the evidence.

4. **No error bars or significance tests for key results in Tables 2 and 3.** While CR-FIQA is reported with mean±std in Table 1, the core identity consistency metrics (Table 2) and downstream recognition accuracies (Table 3) lack measures of variance. With only 105 identities and 21 images per identity, results could be sensitive to the specific identity set or random seeds. Reporting over multiple seeds or bootstrapping would substantially increase confidence.

### Trivial

1. **Imprecise characterization of conditioning-based approaches in Related Work.** Section 2 states that these methods "did not consider identity during training," but Arc2Face explicitly conditions on ArcFace features—a clear form of identity consideration. This overstatement is minor and does not affect the paper's core contribution.

## Nice-to-Haves

- An ablation study over the margin parameter m (at least 3 values) to demonstrate robustness of the improvements.
- A direct Pareto-style visualization of the diversity vs. consistency trade-off, with DreamBooth, PortraitBooth, and ID-Booth as points, to directly support the paper's central claim about improving rather than sliding along this trade-off.
- A brief analysis of what the prior preservation images contain and why they serve as appropriate negatives (e.g., similarity distributions between negatives and positives).
- A discussion of the computational cost of per-identity fine-tuning at scale, and a qualitative comparison with conditioning-based alternatives (IP-Adapter, InstantID, Arc2Face) that avoid per-identity fine-tuning and have a fundamentally different cost profile.

## Removed Points

These points were raised by reviewers but are removed per the filtering guidelines. Treat with caution if referenced.

- **Harsh Critic Point 1 (comparison "constructed to inflate" significance):** The critic claimed the comparison against TFD was designed to inflate the contribution. However, the paper's claim is explicitly about "similar scale" and compares against the same dataset used for fine-tuning—a meaningful and honestly-framed comparison for the paper's stated scope (generating synthetic data from small consented datasets). The paper does not claim to replace datasets like CASIA-WebFace. Removed as an overreading of the paper.

- **Harsh Critic Point about margin value "never stated":** The paper delegates detailed hyperparameters to the supplementary material (line 124: "Additional implementation details... are available in the supplementary material"). The parser strips supplementary content, so the margin value may be specified there. Removed per hard rule about penalizing absent appendix content.

- **Harsh Critic Point about "21 images per identity" being unnecessarily restrictive:** The 21 images per identity × 105 identities ≈ 2,205 images closely matches TFD's 2,213 images, creating a fair scale-matched comparison. This is intentional experimental design, not a limitation. Removed.

- **Harsh Critic Point about training steps/learning rate not in main text:** Delegated to supplementary material. Removed per hard rule.

- **Strength Finder: generic/delusional/superficial strengths filtered.** General observations about "the problem being important" or unsubstantiated praise removed.

- **Harsh Critic Point about no comparison with conditioning-based approaches:** Rephrased from a weakness to a nice-to-have, since the paper explicitly scopes itself as a fine-tuning approach and the comparison set (DreamBooth, PortraitBooth) is appropriate. Conditioning approaches have a fundamentally different cost profile and are acknowledged in Related Work.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations sharpen the paper's limitations (partial circularity in evaluation, missing ablation of the margin) but do not reveal new insights beyond what the paper itself provides.

## Suggestions

1. Add an ablation study over the margin parameter m (at least three values, e.g., 0.1, 0.3, 0.5) to demonstrate robustness of the reported improvements.
2. Report variance (e.g., over multiple seeds or bootstrapping over identities) for the key results in Tables 2 and 3.
3. Explicitly acknowledge in the conclusion that the "outperform real-world datasets" claim is supported against TFD specifically, and note the constrained-laboratory nature of that dataset.
4. Add one additional identity consistency evaluation using a different face recognition backbone (e.g., a pretrained CosFace or MagFace model) to break the partial ArcFace circularity.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>