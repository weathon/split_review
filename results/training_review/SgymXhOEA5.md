Now I have a thorough understanding of the paper and the reviewer claims. Let me construct the final review.

## Summary

This paper provides an empirical investigation of camera bias in person re-identification (ReID) models, focusing on the previously overlooked scenario of **unseen domains**. The authors show that camera bias becomes more pronounced under distribution shift, and that camera-specific feature normalization (per-camera centering and scaling of embedding vectors at test time) is broadly effective across 14 model variants. They provide a mechanistic explanation: only a small fraction of feature dimensions are camera-sensitive, and features shift consistently in those dimensions under camera changes. The paper further extends the normalization framework to fine-grained bias factors (image properties, body angle) and identifies camera bias as a critical problem in unsupervised ReID, proposing simple training modifications (debiased pseudo labeling + discarding single-camera clusters) that yield large gains (e.g., 19.3 mAP on MSMT17 for CC).

## Strengths

- **First systematic study of camera bias on unseen domains.** While prior work focused on bias within the training domain, this paper measures camera bias (via NMI) across multiple datasets and demonstrates that even camera-aware and domain-generalizable models exhibit large bias on unseen data (Table 1). This establishes a previously overlooked problem and is well-supported by data.

- **Mechanistic understanding of why normalization debiases.** Section 4.2 shows that only a small fraction of feature dimensions are camera-sensitive (Figure 2a), features move consistently in those dimensions under camera changes (Figure 2b), and centering just the top-50 sensitive dimensions achieves roughly half the total performance gain (Figure 2c). This goes beyond the heuristic use of normalization in prior work and provides actionable insight.

- **Comprehensive generalizability across models and backbones.** Table 3 reports consistent improvements from normalization on 14 model variants (supervised, unsupervised, camera-aware, domain-generalizable, ResNet, ViT) on unseen domains, with mAP gains of 3–10 points, demonstrating the method is not tied to a specific architecture or training scheme.

- **Extension of normalization to fine-grained bias factors.** Section 4.3 shows that group-specific normalization for low-level image properties (brightness, sharpness, area) and body angle also reduces bias, and combining property groups with camera labels (e.g., area+camera) can outperform camera-only normalization. This reveals that camera bias is not monolithic.

- **Practical training strategies for unsupervised ReID with large gains.** Toy experiments (Figure 6) clearly demonstrate the detrimental effect of camera-biased pseudo labels. The simple strategies (debiased pseudo labeling + discarding single-camera clusters) improve CC by 19.3 mAP on MSMT17 (Table 6), with ablation in Figure 7 isolating each component's contribution.

## Weaknesses

### Fatal
None.

### Major
None. No weakness identified rises to the level of fundamentally undermining the paper's core claims or results.

### Minor

- **Transductive nature of the normalization protocol is not discussed.** The paper computes per-camera statistics from the entire test set (Section 4.1) but does not clarify whether gallery and query splits are separated. In standard ReID evaluation, using query images to compute normalization statistics could leak information. While Figure 5 shows that as few as 25 samples per camera suffice, making gallery-only statistics feasible, the paper should explicitly state the protocol used and discuss whether the method remains valid under strict query-unknown settings. This affects reproducibility but not the validity of the empirical findings.

- **Dimension-sensitivity analysis is limited to one model and one dataset.** Section 4.2's analysis of which feature dimensions are camera-sensitive is performed only on TransReID-SSL trained on MSMT17, evaluated on CUHK03-NP. While the general effectiveness of normalization is validated across many models (Table 3), the specific mechanistic claim that "the sensitivity of each dimension is quite different" as a general property of ReID models would be strengthened by replication on at least one additional model architecture.

- **The paper does not discuss why domain-generalized methods (ISR, PAT) still benefit from normalization.** Table 3 shows clear gains for these methods, which are explicitly designed for robustness to domain shifts. The paper merely notes they are domain-generalized without analyzing whether the residual bias stems from incomplete camera-invariance or from the normalization correcting other dataset-specific shifts. A brief discussion would strengthen the analysis.

- **Abstract slightly overstates applicability to detailed bias factors.** The abstract states normalization "can be applied to detailed bias factors such as low-level image properties and body angle." While technically true, applying normalization to these factors requires property/angle labels that are not available in standard ReID benchmarks. The paper's Section 4.3 is transparently framed as analysis (not a deployable method), and the conclusion appropriately calls for "further research." The abstract could better signal this distinction between analysis and practical deployment.

### Trivial

- The toy experiment (Section 5.2) uses 7500 samples from 500 identities. The paper is transparent about this setup, and the conclusions are consistent with the full-scale results, so this is not a substantive weakness — the toy experiments are designed for controlled analysis, not for benchmarking.

## Nice-to-Haves

- A direct comparison of the USL training strategies (debiased pseudo labeling + discarding single-camera clusters) against simply applying test-time camera-specific normalization to the baseline USL models at evaluation time. The paper's own data (Table 3, seen domain rows) already suggests the training strategies provide substantially larger gains than test-time normalization alone on the seen domain, but making this explicit would cleanly isolate the benefits of the training pipeline modifications.

- Comparing camera-specific normalization to alternative test-time debiasing approaches (e.g., camera-subspace removal via PCA, camera-conditional whitening, or a learned camera-adversarial projection). The paper already compares to global ZCA whitening (Table 4), but a broader comparison would strengthen the claim that simple centering is a competitive approach. However, this is a nice-to-have, not a core gap, given the paper's primarily analytical contribution.

- Reporting published results alongside reproduced baselines for USL methods (CC, PPLR) in Table 6 to rule out the possibility that the reproduced baseline is low.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic's Critical Issue 1 (Missing comparison to alternative test-time debiasing)** — Removed/Weakened. The paper's contribution is primarily analytical: understanding *why* normalization works and demonstrating its broad applicability, not proposing a new SOTA method. The paper already compares to ZCA whitening (Table 4), which is a related approach involving covariance correction. Requesting comparisons to PCA, adversarial removal, or camera-conditional batch normalization as competitors is scope creep for an empirical analysis paper. The paper's claim is that normalization is *effective*, not that it is the *best possible* debiasing method.

- **Harsh Critic's Critical Issue 3 (USL strategies vs test-time normalization on baselines)** — Removed/Weakened. The paper's own data implicitly addresses this. Table 3 shows that test-time normalization gives only "slight improvement" (gray background) on the seen domain for USL models, while the training strategies give 19.3 mAP improvement on MSMT17 (Table 6). These techniques address different settings (training modification vs. test-time postprocessing) and the data already shows the training strategies provide substantially different and larger benefits. An explicit comparison would be nice-to-have but is not a missing critical experiment.

- **Harsh Critic's Critical Issue 4 (Detailed bias factors framed as practical method)** — Removed/Weakened. Section 4.3 is explicitly titled "ANALYSIS ON DETAILED BIAS FACTORS" and the conclusion frames this as "highlighting the need for further research." The paper is transparent that these experiments require labels not typically available at test time. The abstract's phrasing ("can be applied to") is technically accurate; this is a minor presentation nuance, not a substantive flaw.

- **Criticism about InfoMAP clustering not being justified** — Removed. NMI with InfoMAP clustering is a standard approach for measuring cluster agreement in the literature. Different clustering algorithms would change absolute NMI values but are unlikely to change the relative ordering across models/datasets that supports the paper's main conclusions.

- **Criticism about toy example scale (7500 samples, 500 identities)** — Removed. Toy experiments are designed for controlled analysis, not benchmarking. The paper is transparent about the setup and the conclusions are validated on full-scale datasets.

- **Criticism about missing related works** — Removed per instructions (cannot verify existence of missing references).

## Novel Insights

Beyond the paper's own contributions, the key insight emerging from this set of reviews is that the paper's main strength is its **scope and structure as a systematic empirical study** rather than as a novel algorithmic contribution. The finding that camera bias persists even in domain-generalized models (which are explicitly designed for robustness) is itself a noteworthy result that challenges assumptions in the ReID community. The dimension-sensitivity analysis (Figure 2) is particularly valuable because it provides a mechanistic explanation for why a simple operation works, rather than just reporting that it works — this is the kind of analysis that enables principled future method design. The USL results (19.3 mAP gain) also make a clean empirical point: camera bias in pseudo labels is not a minor nuisance but a primary bottleneck for unsupervised ReID, and simple fixes targeted at this bottleneck yield disproportionate gains.

## Suggestions

1. **Clarify the evaluation protocol for normalization.** Explicitly state whether per-camera statistics are computed from gallery-only, query-only, or the full test set. If full-test-set statistics were used, include an ablation comparing gallery-only vs. full-set to quantify any transductive bias and clarify the practical protocol for deployment.

2. **Replicate the dimension-sensitivity analysis on at least one additional model** (e.g., a ResNet-based model) to confirm the claim is not architecture-specific.

3. **Add a brief discussion of why domain-generalized methods (ISR, PAT) still benefit from normalization.** Even a paragraph speculating on the residual bias source would strengthen the paper's analytical depth.

4. **Tone down the abstract's "can be applied to detailed bias factors"** or add a caveat that property/angle labels are required, to better align with the paper's actual experimental scope.

5. **Add a simple comparison table or paragraph** that explicitly contrasts the gains from test-time normalization vs. the training strategies for USL on the seen domain, to cleanly separate the contributions of the two techniques.

## Score and Decision

This paper makes solid empirical contributions: it identifies a real and overlooked problem (camera bias on unseen domains), provides mechanistic understanding of why a simple fix works, and demonstrates large practical gains in unsupervised ReID. The experimental scope (14 models, multiple datasets, both analysis and application components) is impressive. The weaknesses identified are minor and addressable — none threaten the core claims. The paper would benefit from clarifying the evaluation protocol, slightly expanding the analysis breadth, and more carefully distinguishing analysis from deployment claims in presentation. The core scientific contribution is sound and valuable.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>