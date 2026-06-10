## Summary

CLIP-DETR proposes a training-only framework that integrates CLIP visual-linguistic knowledge into DETR-based object detectors via two modules: AlignNet, which performs contrastive alignment between encoder features and CLIP text+scale features, and DynQL, which trains the decoder with multiple sets of GT-informed queries at varying noise levels. Both modules are removed at inference, preserving the baseline model's computational efficiency. The paper reports 3.9% and 5.1% mAP gains over Deformable-DETR on COCO with ResNet-50 and CLIP backbones, respectively, and demonstrates modest improvements on open-vocabulary detection tasks.

## Strengths

1. **Substantial mAP gains over strong non-CLIP baselines**: The method achieves a 3.9% mAP improvement over Deformable-DETR with ResNet-50 and 5.1% with a CLIP image encoder backbone on COCO (Section 4.1, line 175). These are non-trivial improvements over a well-established DETR baseline.

2. **Demonstrated generalization to unseen categories in open-vocabulary detection**: CLIP-DETR improves OV-DETR by 1.4% AP50 on novel categories and CORA variants by 1.7% and 0.8% on novel categories on OV-COCO (Section 4.2, line 183). This directly supports the claim that CLIP integration aids unseen-category recognition.

3. **Inference-time efficiency is preserved**: Both modules are only applied during training and removed at inference, so "CLIP-DETR maintains the same inference-time computational efficiency as the baseline DETR architecture" (Figure 1 caption, line 19). This is a practical advantage with a verifiable design property.

4. **Ablation rigorously isolates scale from location and yields a non-obvious finding**: Table 5 (lines 199–206) compares label-only, label+full-box [cx,cy,w,h], and label+scale-only [w,h]. The scale-only variant outperforms the full-box variant, with a cogent explanation (translation invariance making absolute [cx,cy] unsuitable for feature refinement). This goes beyond a typical ablation by identifying *why* one choice is better.

5. **Ablation on DynQL noise configurations provides actionable guidance**: Tables 6 and 7 (line 207) explore noise distributions and number of query sets, finding that a uniform noise range (0.1–0.9) with 5 sets is optimal. This gives concrete design guidance to future practitioners.

6. **Clean feature extraction using GT boxes rather than noisy proposals**: Unlike RegionCLIP and prior region-based methods, AlignNet pools features using GT bounding boxes from hierarchical feature levels (Section 3.2, Eq. 1, lines 67–73), avoiding noise from inaccurate proposals.

## Weaknesses

### Fatal
None.

### Major

1. **The evaluation does not disentangle the contribution of CLIP's pretrained knowledge from the contribution of the specific AlignNet/DynQL design.** The headline results (Table 1, Table 2) compare CLIP-DETR against Deformable-DETR, DINO, and Co-DETR — none of which use CLIP. The reported gains (3.9%–5.1%) could be driven largely by the mere presence of CLIP's powerful representations in the training pipeline, with little evidence that AlignNet's *specific* contrastive design or DynQL's *specific* query noise scheme is superior to simpler alternatives (e.g., appending CLIP text embeddings to encoder features as an auxiliary loss, or adding a basic contrastive loss without scale information). The ablation in Table 4 shows that both modules contribute individually, but it does not compare against a "naive CLIP injection" baseline that uses CLIP in a simpler way. The open-vocabulary experiments (Table 3) provide partial support by showing gains on top of already-CLIP-aware methods (CORA, OV-DETR), but these gains are modest (1.4–1.7 AP50 on novel categories) and their statistical significance is unclear. Without a controlled comparison against a simpler CLIP-augmented baseline, the core claim — that the *specific* AlignNet/DynQL design is the source of the improvements — is not fully supported by the evidence.

### Minor

2. **Insufficient analysis of how DynQL's GT-informed training transfers to inference.** DynQL constructs query content from the ground-truth label (via CLIP text embedding) and GT object scale, and query positions from GT boxes with noise. Both modules are removed at inference. While the self-attention masking (lines 134–135) prevents direct information leakage, the cross-attention parameters are shared between conventional and DynQuery processing, meaning the decoder's cross-attention weights are shaped by queries initialized close to GT. The paper does not analyze whether these learned cross-attention patterns generalize to the fully uninformed queries used at inference (e.g., by comparing conventional query accuracy during training with and without DynQL, or analyzing cross-attention map differences). The empirical result that the full system works is suggestive but does not address *how* or *why* the transfer succeeds.

3. **The use of text-derived features (`z_attr`) as decoder query content is a notable design choice without sufficient justification.** Conventional DETR queries are learned embeddings or spatial anchors. DynQL's content queries are derived from a CLIP text embedding (concatenated with scale [w,h]) — a representation from a different modality. The paper does not discuss or analyze the modality mismatch, whether the decoder learns to "translate" this representation, or how DynQuery features evolve across decoder layers relative to conventional queries. An analysis of query feature space dynamics would strengthen the contribution.

4. **No training cost or variance statistics are reported.** DynQL adds S×N additional queries per training step (with S=5, N=batch instances), which likely increases training memory and time. No measurements are provided. Additionally, no confidence intervals or run-to-run variance are reported for any result, which is especially relevant for the open-vocabulary experiments where improvements are modest (1.4–1.7 AP50).

### Trivial
None.

## Nice-to-Haves

- **Report training cost**: Memory and wall-clock time comparisons with and without DynQL, since adding 5×N queries per training step has non-trivial overhead.
- **Add a "naive CLIP injection" control**: A simple baseline where CLIP text embeddings are concatenated to encoder features or used as an auxiliary contrastive loss (without AlignNet's specific design) would directly address the attribution gap in the evaluation.
- **Provide run-to-run variance**: Especially for the open-vocabulary results where gains are small; at least 3 seeds would clarify reliability.
- **Discuss limitations / failure cases**: The paper currently lacks any discussion of when the approach might fail (e.g., noisy annotations, small objects, CLIP's known biases for certain categories).

## Removed Points

These points were flagged by reviewers but removed during consolidation for the reasons stated:

- *"Tables are embedded as images — numerical data inaccessible"*: Removed as a parser artifact. The original submission has proper tables; the extracted text is a formatting casualty. The textual descriptions of results (lines 175, 183) are sufficient to verify the paper's claims.
- *"Ambiguity about what 'the baseline' refers to"*: Removed — the paper clearly states (line 159) that Deformable-DETR is the foundational detector and all models are built upon it, making the baseline unambiguous.
- *"Self-attention masking description is ambiguous"*: Removed — the description (lines 134–135) is clear: each DynQuery set interacts with its own set and conventional queries, while conventional queries are isolated from DynQuery sets.
- *"Criticism about missing comparisons against RegionCLIP/CLIPSelf"*: Partially removed. The paper scopes itself to DETR-based detectors; RegionCLIP and CLIPSelf are not DETR-based. However, the broader point about needing a CLIP-aware DETR baseline is retained in the major weakness.

## Novel Insights

Both reviewers correctly identify the core tension in this paper: the method claims credit for a specific architectural design (AlignNet's contrastive framework + DynQL's noise-varied queries) but the evaluation primarily demonstrates that *some* form of CLIP integration improves detection over non-CLIP baselines. The ablations are well-designed and show that both modules contribute, but they stop short of comparing against a simpler CLIP injection — the minimal experiment that would settle whether the design details matter or whether any reasonable CLIP infusion would yield similar gains. This is a recurring methodological challenge in literature that proposes complex pipelines for leveraging pretrained models: the burden of proof should fall on showing that the *specific* mechanism, not just the presence of the pretrained model, drives the improvement. The paper's open-vocabulary experiments (building on already-CLIP-aware CORA/OV-DETR) partially mitigate this, but the modest gains and lack of variance estimates limit their conclusiveness. The ablation on scale vs. full-box alignment (Table 5) is a genuine methodological insight that stands independently.

## Suggestions

1. **Add a baseline that injects CLIP into DETR via the simplest reasonable mechanism** (e.g., add a contrastive loss between encoder features and CLIP text embeddings without the scale component, without AlignNet's full design, and without DynQL). If CLIP-DETR meaningfully outperforms this, the case for the specific design is made; if it does not, the paper's contribution is undercut. This single experiment would resolve the most serious ambiguity.

2. **Empirically analyze DynQL's effect on inference-time decoder behavior**: Compare conventional query prediction quality layer-by-layer with and without DynQL training, or visualize cross-attention maps to show that the shared cross-attention weights learned with GT-informed queries transfer effectively to conventional queries.

3. **Provide an analysis of query feature space dynamics**: Measure the distance between DynQuery features and conventional query features at each decoder layer to illuminate whether text-derived query content is being "translated" into a compatible visual feature space.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>