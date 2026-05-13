Now I have a thorough understanding of the paper. Let me synthesize the review.

Key things I need to verify from the harsh critic:

1. **Abstract claims "improved performance" — is this overclaimed?** The abstract says "The HRR-based approach improved performance on the pre-training and fine tuning tasks compared to standard transformer embeddings." Let me check: 
- HRRBase is ~17% worse on pre-training MLM
- On mortality prediction, no significant improvements
- Disease prediction: HRRBase achieves significantly greater accuracy (p=0.033) and precision (p=0.023)
- HRRAdd and HRRCat improve pre-training by ~2%
- The conclusion uses "modestly outperformed"

The abstract claim IS overstated. HRRBase (the pure HRR method) degrades pre-training by 17%, and mortality prediction shows no significant improvement. The claim "improved performance" without qualification is misleading.

2. **ROOD experiment is under-described?** The paper says: "We constructed a really-out-of-distribution (ROOD) dataset from MIMIC-IV patients whose contexts contain at least one of 32 codes that were never used to train HRRBase and unstructured models. We found that HRRBase strongly outperforms unstructured for the disease prediction task on patients with only unseen codes (F1 Score 79.5 vs. 48.0)." This is indeed described in just one sentence with no details about the 32 codes' selection, test set size, number of trials, etc. This is a valid concern — it's a dramatic result with minimal methodology.

3. **Statistical testing validity with Shapiro-Wilk failures?** The paper reports Shapiro-Wilk failures for HRRBase precision and F1 (mortality) and HRRAdd accuracy (disease). The paper notes these violations but proceeds with parametric tests. However, on mortality prediction, no significant results were found anyway. On disease prediction, the significant results are for HRRBase accuracy and precision — the paper doesn't mention Shapiro-Wilk failures for these specific metrics on disease prediction. Let me re-check: "the Shapiro-Wilk test suggests normal distributions except for HRRAdd accuracy" for disease prediction. So the significant results for HRRBase (accuracy p=0.033, precision p=0.023) are for metrics where normality IS satisfied. The critic's concern about "significant results concentrated in metrics with distributional violations" seems partially incorrect for disease prediction. For mortality prediction, the normality violations are for HRRBase precision and F1, but no significant results were found for mortality anyway. So this is a minor concern at best.

4. **HRRAdd parameter count confound**: Valid. HRRAdd roughly doubles learnable parameters. The paper acknowledges this but doesn't provide a parameter-controlled baseline.

5. **671 excluded ICD codes**: Valid concern about systematic bias. 4.62% of codes excluded.

6. **Crosstalk noise from bundling**: This is a known HRR property. The paper doesn't discuss it but it's more of a nice-to-have analysis.

7. **HRRFreq only 1 trial**: Valid but minor concern.

8. **Disease prediction is coarse-grained (22 chapters)**: Valid concern — the task may not be sensitive to fine-grained ontological structure.

9. **Single annotator for cosine similarity**: Valid but this is a supplementary evaluation, not the core contribution. This is standard for case studies.

10. **Conclusion contradicts**: The conclusion says "modestly outperformed baseline models... for... mortality prediction F1" but the mortality prediction section says "No comparisons of mean metrics for HRR embeddings were significantly greater than the control." This is a valid contradiction.

Now evaluating the Strength Finder's output:
- ROOD experiment strength: Valid but weakened by the under-description
- Statistically validated semantic similarity: Valid for rare codes
- Efficient differentiable HRR computation: Valid and concrete
- Statistically significant fine-tuning improvements: True for disease prediction (accuracy, precision)
- Cross-dataset generalization: Valid (eICU transfer with p=0.046)
- t-SNE visualization: Valid qualitative evidence
- Cosine similarity case studies: Valid but limited (single annotator)
- Systematic exploration of configurations: Valid

Let me now synthesize.</think>Now I have a thorough understanding of the paper. Let me carefully synthesize the review, verifying each claimed weakness against the actual text.

## Summary

The paper introduces HRRBERT, a neuro-symbolic approach that encodes SNOMED CT medical ontology structure into BERT token embeddings using Holographic Reduced Representations (HRR). Atomic vectors for SNOMED CT terms, relationships, and description words are composed via HRR binding/bundling operations to form concept vectors for ICD diagnostic codes, and these structured embeddings replace standard random-initialization embeddings in a BERT model trained on clinical EHR sequences from MIMIC-IV. The authors provide an efficient FFT-based GPU implementation compatible with PyTorch autograd, and evaluate on MLM pre-training, mortality/disease prediction fine-tuning, and embedding quality analyses.

## Strengths

- **Efficient differentiable HRR computation**: The FFT-domain algorithm that computes the full HRR embedding matrix in ~80ms forward / ~550ms backward on a single RTX 3090 with ~3.5GB memory, compatible with standard PyTorch autograd, is a concrete engineering contribution enabling end-to-end learning through VSA operations at scale (Section 2.3).

- **Demonstrated mitigation of frequency bias**: The t-SNE visualization (Figure 2) clearly shows that unstructured embeddings cluster by code frequency, while HRRBase does not, providing compelling qualitative evidence that the ontological structure decomposes the frequency bias identified in prior work (Yu et al., 2023). The broader cosine similarity distributions for HRR configurations (Figure 3) and the Fisher's exact test on rare codes (p=2.44×10⁻⁸, Section 3.3) provide quantitative support, particularly for rare codes.

- **ROOD generalization to unseen codes**: The really-out-of-distribution experiment (Section 3.2) showing HRRBase achieving F1=79.5 vs. 48.0 for unstructured on disease prediction with unseen codes directly demonstrates the compositional advantage — rare/unseen codes share atomic elements with common ones, enabling meaningful representations absent training data. This is a strong evaluation design aligned with the paper's core motivation.

- **Cross-dataset transfer**: HRRBase achieves significantly greater mean accuracy (p=0.046) compared to unstructured embeddings when the MIMIC-IV fine-tuned mortality model is applied directly to the eICU dataset without further training (Section 3.2), suggesting ontology-enriched representations transfer better across institutions.

- **Systematic exploration of configurations**: The four HRR variants (HRRBase, HRRFreq, HRRAdd, HRRCat) alongside the unstructured baseline reveal meaningful trade-offs: HRRFreq recovers most of HRRBase's ~17% pre-training gap, confirming frequency information as the cause; HRRCat provides a parameter-fair hybrid configuration.

## Weaknesses

### Fatal
None.

### Major

- **Overstated abstract claims that do not match the experimental evidence**: The abstract states "The HRR-based approach improved performance on the pre-training and fine tuning tasks compared to standard transformer embeddings." This is misleading as a blanket claim: (1) HRRBase degrades pre-training MLM by ~17% relative to unstructured; (2) no mortality prediction metric shows statistically significant improvement for any HRR configuration; (3) on disease prediction, only HRRBase achieves significance on 2 of 4 metrics (accuracy p=0.033, precision p=0.023), with no other configuration significantly improving on any metric. The conclusion compounds this by claiming "modestly outperformed baseline models... for... mortality prediction F1," but the mortality section explicitly states "No comparisons of mean metrics for HRR embeddings were significantly greater than the control." The abstract should qualify which configurations and which metrics show improvement; the current framing implies broad, uniform improvement that the data do not support.

- **The ROOD experiment — potentially the paper's strongest result — is severely under-described**: The F1=79.5 vs. 48.0 advantage for HRRBase on disease prediction with unseen codes (Section 3.2) is a dramatic effect, but virtually no methodological detail is provided: how the 32 unseen codes were selected, the test set size for this sub-evaluation, whether this is averaged over multiple trials, or whether the result generalizes beyond a specific set of unseen codes. Without these details this result cannot be independently evaluated or reproduced, and it is too important a claim to leave as a single-sentence aside.

### Minor

- **HRRAdd confounds HRR structure with additional learnable parameters without a controlled baseline**: HRRAdd roughly doubles learnable parameters (22,725d atomic vectors + 25,493d learnable vectors) compared to unstructured (25,493d), yet is compared directly. The paper acknowledges this but does not provide a parameter-matched unstructured baseline (e.g., wider embeddings or an additional embedding table). While HRRCat offers a parameter-fair alternative, the lack of parameter control for HRRAdd means the ~2% pre-training improvement cannot be cleanly attributed to the HRR structure vs. additional capacity.

- **Disease prediction task is coarse-grained and may not fully test the method's advantage**: The task reduces all ICD codes to 22 binary disease chapter labels. Many ontologically distinct codes map to the same chapter, so this task may not be sensitive to the fine-grained ontological structure that HRR encodes. A finer-grained evaluation would more directly test whether the ontological structure yields benefits.

- **Single-annotator evaluation for cosine similarity study**: The Fisher's exact test (Section 3.3) relies on a single physician annotating 30 codes. While the result for rare codes is highly significant (p=2.44×10⁻⁸) and unlikely to be an artifact of a single rater, the common-code and all-code categories show no significance, which could reflect limited sample size or annotation bias rather than a true null effect.

### Trivial
None.

## Nice-to-Haves

- A parameter-controlled unstructured baseline (~47k learnable vectors) to fairly attribute HRRAdd's gains to structure vs. capacity.
- A per-frequency-band breakdown of MLM accuracy (e.g., quintiles) to directly quantify the rare-code advantage that is currently shown only through the ROOD experiment and qualitative figures.
- Multi-annotator evaluation or inter-rater reliability for the cosine similarity study to strengthen common-code claims.
- Analysis of relationship-count versus embedding quality to characterize crosstalk noise from bundling — a known HRR property.
- Analysis of whether the 671 excluded unmapped ICD codes are systematically rarer, which could bias rare-code evaluations.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Statistical testing validity compromised by violated normality assumptions**: The harsh critic claimed the reported p-values may be unreliable because Shapiro-Wilk tests fail for some metrics. However, the significant results on disease prediction are for HRRBase accuracy (p=0.033) and precision (p=0.023) — the paper states normality holds for these specific metrics (the violation is for HRRAdd accuracy). For mortality prediction, no significant results were found regardless. The normality violations therefore do not threaten the claimed significant results. Downgraded to a non-issue.

- **671 excluded codes may systematically bias rare-code evaluation**: While valid to flag, the exclusion affects only 4.62% of codes and 58 patients. The paper acknowledges this. Without evidence that the excluded codes are disproportionately rare, this remains speculative. Moved to Nice-to-Have.

- **HRRFreq only has 1 trial**: True but minor; HRRFreq is a supporting configuration (showing frequency info recovers performance) rather than a primary claimed contribution. Not substantively damaging.

- **Bundling crosstalk noise not discussed**: A valid theoretical concern but one inherent to all HRR/VSA work; not specific to this paper's methodology and the standard in the field. Moved to Nice-to-Have.

- **Criticisms about the introduction's framing of frequency bias being "indirect"**: The t-SNE and Fisher's exact test results directly demonstrate that HRR embeddings reduce frequency-driven organization and improve ontological similarity for rare codes. The paper does measure this, just with different tools than the critic expects.

- **Generic "this paper addressed an important problem" strengths**: Removed from the Strength Finder's list as too generic.

## Novel Insights

The ROOD result (F1=79.5 vs. 48.0) suggests that the compositional structure of HRR embeddings provides a fundamentally different kind of generalization than what standard embeddings can achieve: not merely better representation of rare codes, but viable prediction for codes that have *zero* training data. If confirmed with full methodological detail, this would be the clearest empirical demonstration that VSA compositional structure translates into practical out-of-distribution generalization in a large-scale NLP/medical setting — a result that goes beyond the typical VSA literature's toy-scale demonstrations.

## Suggestions

- Reword the abstract to qualify which configurations and metrics show improvement (e.g., "hybrid HRR configurations improved pre-training, while HRRBase significantly improved disease prediction accuracy and precision; pure HRR embeddings degraded pre-training performance").
- Expand the ROOD experiment description to include: selection criteria for the 32 unseen codes, test set size, number of trials, and results across multiple unseen-code sets if available.
- Add a parameter-matched unstructured baseline for the HRRAdd configuration to isolate the contribution of ontological structure versus parameter count.

## Score and Decision

**Originality**: The idea of encoding SNOMED CT into BERT embeddings via HRR with end-to-end differentiable computation is novel — this is, as claimed, the first application of HRR as structured transformer embeddings.

**Importance of research question**: Incorporating domain knowledge into EHR transformers and addressing frequency bias in medical code embeddings are important, practical problems.

**Claims well supported**: Partially. The qualitative/structural claims (reduced frequency bias, better ontological similarity for rare codes) are well-supported. The ROOD result is promising but under-described. The headline performance claims are overclaimed relative to evidence — the pure HRR method degrades pre-training and shows limited, fragmentary fine-tuning improvements on standard tasks.

**Soundness of experiments**: Reasonable design with multiple configurations, proper statistical testing (Dunnett's), and cross-dataset evaluation. The main gap is the under-described ROOD experiment and the parameter confound in HRRAdd.

**Clarity**: The paper is generally clear and well-structured, though the claims in the abstract and conclusion overstate the evidence.

**Value to community**: The efficient HRR implementation and the demonstration that compositional VSA structure can improve rare-code handling are of genuine value to the neuro-symbolic and medical AI communities.

The paper makes a real contribution at the intersection of VSA and medical NLP. However, the overclaimed abstract and under-described strongest result are significant issues that cannot be fully resolved in rebuttal (the ROOD methodology cannot be retroactively detailed). The core strengths — mitigating frequency bias, ROOD generalization, and the engineering contribution — are real but should be presented with the precision the data warrant.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>