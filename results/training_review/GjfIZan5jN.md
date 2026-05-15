Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper investigates whether classifiability-oriented pre-trained visual representations can simultaneously achieve high interpretability and high classifiability. To quantify interpretability, the authors propose the Inherent Interpretability Score (IIS), which measures how much task-relevant semantic information is preserved when representations are projected onto a sparse concept space. Across extensive experiments on multiple architectures (ResNet, ViT, ConvNeXt, Swin) and datasets (ImageNet, CUB-200, CIFAR-10/100), the paper reports a positive correlation between IIS and classification accuracy, contrary to the widely assumed trade-off. It further demonstrates two applications: improving classifiability via an IIS-regularized fine-tuning objective, and producing interpretable (concept-based) predictions from high-accuracy representations.

---

## Strengths

- **Novel, well-defined metric for semantic information preservation during concept-based interpretation.** The IIS (Section 2.3) is clearly motivated: it quantifies how much classification accuracy is retained when predictions are made using sparse concept projections rather than original representations. The area-under-the-curve aggregation over sparsity ratios avoids commitment to a single sparsity level, making the metric broadly applicable. This is a clean operationalization of information loss in interpretation.

- **Extensive empirical investigation across diverse architectures, datasets, and concept libraries.** The paper evaluates 13+ pre-trained models (ResNet-18/34/50/101/152, ViT-B/L, ConvNeXt-T/S/B/L, Swin-T/S/B), four concept library types (Prototype, Cluster, End2End, Text), and four datasets. Figures 3 and 4 show that the positive correlation between IIS and accuracy is remarkably consistent across all settings. This breadth rules out the possibility that the finding is an artifact of a particular model family or concept construction method.

- **The positive correlation contradicts a widely held assumption.** Prior work (e.g., Mori & Uchihira, 2019; Zarlenga et al., 2022; Dombrowski et al., 2023) has argued for an inherent conflict between interpretability and classifiability in interpretability-oriented models. This paper provides robust evidence that for classifiability-oriented *pre-trained* representations specifically, the opposite relationship holds, offering a constructive perspective for the field.

- **Demonstration of concrete downstream utility.** Applying IIS-guided fine-tuning (Section 4.1) yields measurable accuracy improvements across multiple backbones. The interpretable prediction setting (Section 4.2) shows that concept-based predictions from high-accuracy pre-trained representations can substantially outperform interpretability-oriented methods that train from scratch, while requiring far fewer trainable parameters (linear head only).

---

## Weaknesses

### Fatal
None.

### Major

- **The IIS metric's validity as a measure of "interpretability" is not externally validated.** The paper defines interpretability as the ability to preserve task-relevant semantics in interpretations, and operationalizes it as accuracy retention under concept sparsification. However, no evidence is provided that higher IIS correlates with human judgment of interpretability, with established interpretability metrics (faithfulness, completeness, concept alignment scores such as TCAV), or with any downstream measure of explanation quality. The paper's central claim—"interpretability and classifiability are positively correlated"—therefore rests entirely on an unvalidated proxy. This gap is significant because it conflates *information preservation* (which IIS measures) with *human interpretability* (which involves cognitive factors like clarity, trust, and comprehensibility that IIS does not directly address). The correlation between IIS and accuracy may be an interesting finding about semantic alignment, but the paper's terminology overreaches.

- **The positive correlation may be partially confounded by the evaluation design.** Concept libraries are constructed from the same datasets (ImageNet, CUB-200, CIFAR-10/100) on which classification accuracy is measured. Representations that are more accurate on a dataset will naturally align better with concepts derived from that dataset—this inflates the correlation trivially. The paper partially mitigates this by testing four different concept library types (including visual prototypes and clusters that differ from the textual GPT-derived concepts), and the consistency across all four strengthens the case. However, the paper does not test whether the correlation holds when concept libraries are drawn from *completely different* data distributions or orthogonal semantic spaces, which would be a stronger test. Additionally, the IIS computation uses ARR (accuracy retention rate), whose denominator is the representation's own accuracy. When accuracy is low, even a modest absolute interpretation accuracy produces a high ARR, which can artificially inflate IIS for low-accuracy models and steepen the observed correlation. The paper does not analyze or correct for this mathematical coupling.

- **The claim of "mutual promotion" between interpretability and classifiability is not fully supported by the evidence.**  
  *Section 4.1 (improving classifiability via IIS maximization):* The fine-tuning objective jointly optimizes both the original accuracy and the IIS-constrained accuracy. Observing that both metrics increase during training (Figure 8) is largely circular—it shows that the optimization works, not that improving interpretability *causes* improved classifiability. The accuracy gains could equally stem from the regularization effect of the low-rank subspace constraint or from additional training, independent of interpretability.  
  *Section 4.2 (interpretable predictions):* The comparison against interpretability-oriented methods (Tables 4, 5) is asymmetric: the paper uses a frozen, high-capacity pre-trained backbone and trains only a linear head, while the baselines train full models from scratch. Achieving higher accuracy under this setup is expected and does not demonstrate that the resulting concept-based explanations are more interpretable to humans. The paper is transparent about this asymmetry (line 193), but it limits what the comparison can conclude.

### Minor

- **No statistical significance, error bars, or variance reported.** All results (Figures 3–7, Tables 1–5) are presented as single-point estimates. Without multiple seeds, bootstrapped confidence intervals, or standard deviations, it is impossible to judge whether the reported accuracy improvements (or the observed correlation strength) are reliable or within the noise of the measurement.

- **The ARR denominator coupling is not disentangled.** As noted above, ARR = Acc(interpretations) / Acc(representations). This means that when the denominator is low, even a low interpretation accuracy yields a moderate ARR. The paper does not control for this coupling (e.g., by using a held-out accuracy estimate or by showing that the correlation holds when controlling for denominator effects). The analysis of early training phases (Figure 5) illustrates the problem: the paper acknowledges that "both interpretations and representations have similarly low accuracy" (line 123), producing high early IIS as an artifact, but then claims this "does not affect the application of IIS" without justification.

- **The concept library construction is underspecified in several respects.** (a) For visual concepts, the paper does not describe how patches/segments are selected from images, nor the resolution or stride. (b) For textual concepts, the GPT-3 prompts are not provided, making it impossible to reproduce or assess the prompt sensitivity of the resulting concepts. (c) The number of sparsity ratios sampled for IIS computation and their distribution are not reported (line 92 merely says "select multiple sparsity ratios"). (d) The linear classifier \(g_{cls}\) (Equation 5) is trained on interpretations derived from the same dataset \(\mathcal{D}\), raising the risk of overfitting to the concept projection subspace; no cross-validation or held-out data is described.

- **The sparsification function (Equation 4) is described as "zeroing out" elements but actually performs soft thresholding that modifies retained values, not just removes them.** The text says "zero out s×100% elements" (line 58), but the formulation \( \mathbf{x}_i^{\mathcal{C},s} = \mathbf{x}_i^{\mathcal{C}} \max(|\mathbf{x}_i^{\mathcal{C}}| - \tau, 0) \) continuously shrinks the magnitudes of all retained concepts rather than leaving them unchanged. This affects the ARR computation in a way that is not discussed. A hard thresholding baseline would clarify whether IIS is sensitive to this choice.

### Trivial

- The hyperparameter analysis (Tables 2, 3) reports optimal values \(M=200\) and \(s=0.1\) but does not specify which model these ablations were run on, limiting generalizability.
- The statement that "the interpretation of representations... cannot be employed as human-understandable interpretations due to human cognitive limitations" (line 56) would benefit from a citation or elaboration.

---

## Nice-to-Haves

- **Human evaluation study** testing whether higher-IIS representations actually produce explanations that humans find clearer, more trustworthy, or more useful for task performance. This is the single most impactful addition.
- **Out-of-distribution test:** computing IIS using concept libraries from a different dataset than the one on which accuracy is measured (e.g., CIFAR-100 concepts for ImageNet models) to decouple the correlation from dataset-specific concept alignment.
- **Comparison against existing interpretability metrics** (faithfulness, completeness, TCAV sensitivity) to position IIS within the broader landscape and validate that it captures a distinct or complementary notion of interpretability.
- **Multiple training seeds** for the fine-tuning experiments (Table 1) with reported mean ± std.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- The harsh critic's claim that accuracy gains are "0.0x% to 0.3% absolute" cannot be verified from the available text (Table 1 is an embedded image). The criticism about missing statistical significance is retained in Minor.
- Criticism about missing related works (TCAV, concept bottleneck models) — removed per the meta-review guideline against demanding specific missing citations.
- Several formatting/style nitpicks (e.g., about presentation) — removed per guidelines.
- The critic's claim that the pre-training process artifact "is not evidence of interpretability" — the paper explicitly acknowledges this artifact (line 123) and does not present it as evidence, so the criticism misreads the paper.
- The strength finder's claim about specific numerical gains (ResNet-50: 76.16%→79.46%, ViT-B: 81.07%→83.23%) — these numbers appear in an embedded table image and cannot be verified from the text; the general claim of improvement is retained in Strengths.

---

## Novel Insights

The reviews collectively surface a tension that the paper does not fully resolve: "interpretability" is used to mean two different things. The paper operationalizes it as *semantic information preservation* (how much task-relevant signal survives concept projection and sparsification), which is a necessary condition for good explanations but not a sufficient one. The positive correlation between this property and classifiability is a clean and well-supported empirical finding. However, the broader interpretability-classifiability debate in the literature concerns human-centric notions of interpretability (comprehensibility, trust, sparsity that aligns with human reasoning). By conflating these two meanings, the paper makes a stronger claim than its evidence supports. The most productive direction would be to either (a) rebrand IIS as a measure of "concept-aligned information retention" or "interpretation faithfulness" rather than "interpretability," matching the evidence more precisely, or (b) add external validation linking IIS to human judgment, thereby bridging the gap between the operational definition and the claimed concept.

---

## Suggestions

1. **External validation of IIS.** Conduct a human evaluation or correlate IIS with established interpretability metrics (faithfulness, completeness, TCAV sensitivity). This is the single most important step to strengthen the paper's central claim.
2. **Disentangle the ARR denominator coupling.** Show that the IIS–accuracy correlation is not a mathematical artifact by computing IIS with a fixed reference accuracy or by demonstrating that the correlation persists when controlling for denominator effects.
3. **Report error bars and statistical significance.** Add multiple seeds (at least 3) for the fine-tuning experiments and bootstrapped confidence intervals for IIS estimates.
4. **Provide concept library details.** Release the GPT-3 prompts, patch extraction parameters, and the set of sparsity ratios used for IIS computation to enable reproducibility.
5. **Clarify the claim scope.** Consider either (a) qualifying the use of "interpretability" throughout to "interpretation faithfulness" or "semantic information preservation," or (b) adding the external validation needed to substantiate the stronger claim.
6. **Add an out-of-distribution concept library experiment.** Compute IIS using concept libraries from a different dataset to test whether the correlation reflects genuine semantic alignment or simply same-dataset confounding.

---

## Score and Decision

The paper presents a cleanly defined metric and a remarkably consistent empirical finding across many architectures and datasets. The positive correlation between IIS and classifiability is a genuine contribution that should inform future work on representation learning and concept-based interpretability. However, the paper's critical weakness is the gap between what IIS measures (semantic information preservation under concept projection) and the paper's claim about "interpretability" writ large. Without external validation or more precise framing, the core conclusion overreaches the evidence. The applications, while interesting, do not fully resolve this gap. The paper is a solid contribution that would benefit significantly from the suggested revisions, but in its current form the central claim is insufficiently supported.

**MY FINAL SCORE: <pineapple>6.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**