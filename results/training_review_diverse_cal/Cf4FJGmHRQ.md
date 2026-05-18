Now I have all the information needed to produce a consolidated review. Let me write it.

## Summary

PAC-FNO proposes a Fourier Neural Operator architecture for recognizing low-quality images (low-resolution and/or naturally degraded). It makes two architectural changes to prior FNOs: (1) removing the low-pass filter to retain high-frequency information (AC-FNO block), and (2) stacking blocks in parallel rather than serially. A two-stage training procedure is also proposed. The method is evaluated across 4 backbone architectures and 7 datasets, showing strong improvements over prior FNO variants, super-resolution models, and resizing baselines — especially at very low resolutions (e.g., 28×28, 32×32) on fine-grained datasets.

## Strengths

- **Novel AC-FNO block removes the low-pass filter to retain high-frequency information, which proves critical for fine-grained classification.** The paper argues that prior FNOs discard high-frequency components via an ideal low-pass filter (§3), harming generalization. Table 2 shows that on Oxford-IIIT Pets at 28×28, PAC-FNO achieves 73.4% top-1 accuracy, dramatically outperforming vanilla FNO (19.1%), UNO (11.1%), and A-FNO (27.0%), as well as super-resolution baselines like DRPN (41.5%). The stark gap at low resolutions on fine-grained tasks directly validates the advantage of using all frequency components.

- **Parallel configuration of AC-FNO blocks increases capacity and resilience to input variations.** Unlike prior serial FNOs, PAC-FNO stacks AC-FNO blocks in parallel (§3.2). Figure 3 (ablation) shows that with the same total number of blocks, the parallel configuration consistently outperforms serial across all resolutions on both ImageNet-1k and ImageNet-C/P (Fog). At 224 target resolution with fog, parallel suffers only 22.9% degradation versus 39.3% for serial — a direct demonstration that parallel structure improves resilience.

- **Comprehensive evaluation across diverse backbones, datasets, and degradation types.** PAC-FNO is tested with four backbone architectures (ResNet-18, Inception-V3, ViT-B16, ConvNeXt-Tiny) across seven benchmarks including ImageNet, four fine-grained datasets, and ImageNet-C/P corruptions (Tables 1–3). The consistent superiority over resizing, fine-tuning, super-resolution, and other FNO baselines demonstrates the method's generalizability.

- **Small parameter overhead.** PAC-FNO adds only 1–13% of the backbone's parameters (§3.3), making it practical to attach to existing pre-trained models without substantial computational cost.

- **Generalization to unseen resolutions confirms the neural operator advantage.** Table 4 shows that models trained on only two resolutions ({32,224}) or four resolutions ({32,64,128,224}) still produce meaningful accuracy at intermediate, unseen resolutions (e.g., 48, 96, 160), validating the frequency-domain design goal of handling arbitrary resolutions without re-training.

## Weaknesses

### Fatal

None.

### Major

1. **The contribution of the all-component design (removing the low-pass filter) is not isolated from the parallel structure.** The paper makes two architectural changes: (i) removing the low-pass filter from the FNO block (AC-FNO), and (ii) stacking blocks in parallel. The ablation in Figure 4 tests parallel vs. serial while keeping the AC-FNO block constant, and the main comparisons (Tables 1–3) compare PAC-FNO (parallel + all-component) against FNO/UNO/A-FNO (serial + low-pass filter). **No experiment fixes the parallel structure and varies only whether the low-pass filter is applied.** Without this, it is impossible to tell whether the gains come from removing the filter, adopting parallelism, or their interaction. Since removing the low-pass filter is presented as the paper's primary architectural insight (§3: "We argue that the low pass filter removes useful information"), leaving it confounded with the parallel structure is a significant methodological gap. The authors should compare parallel-FNO (with filter) vs. parallel-AC-FNO (without filter) holding the parallel configuration fixed.

2. **Only 4 of the 19 corruptions from ImageNet-C/P are reported, with no justification for the selection.** Table 3 shows results for fog, brightness, spatter, and saturate. The paper states (§4.2) that "ImageNet-C/P has 19 noises that can be used to test resilience against image quality degradation" but gives no reason why these four were selected and the other 15 omitted. Given the large variability across corruption types (noise vs. blur vs. weather vs. digital), showing only a subset raises concerns about cherry-picking. The claim that PAC-FNO is "more resilient to input changes regardless of resolution than other baseline methods" (§4.2) cannot be properly evaluated without results across all corruptions or, at minimum, a principled justification for the selection. The authors should either report all 19 corruptions or clearly define the selection criterion (e.g., "one from each category").

### Minor

1. **The "up to 77.1%" improvement stated in the abstract is untraceable.** No percentage improvement of 77.1% appears in any table or figure in the paper. The only "77.1" in the main text is the top-1 accuracy of FNO (77.1) at resolution 112 for ViT-B16 (Table 1), which is not an improvement percentage. The closest computable relative improvement is 76.9% (PAC-FNO 73.4 vs. DRPN 41.5 on Oxford-IIIT Pets at 28×28), but this is not what the abstract states. All numeric claims in the abstract should be directly traceable to specific experiments with explicit definitions (absolute accuracy gain, relative accuracy gain, etc.).

2. **The relative accuracy metric is defined but never used.** Section 4 defines relative accuracy as "the ratio of a model's accuracy in low quality to that in the original resolution" and states it "enables us to compare the effectiveness of methods across different datasets and models." However, all tables report only top-1 accuracy. The metric should either be reported in tables or its omission justified.

3. **The computational cost claim ("1–13% of backbone parameters") is vague.** The specific PAC-FNO configuration (n, m), backbone, and dataset corresponding to 1% vs. 13% are not given. FLOPs or inference-time comparison with other FNO variants would substantially strengthen the paper's claims about efficiency.

4. **A potential data quality issue in Table 2 (Food-101).** The DRPN row shows 59.5 at resolution 112 for Food-101, while adjacent entries (Resize: 88.1, Fine-tune: 88.3, DRLN: 86.8, FNO: 88.2) are all ~86–89. This value appears anomalously low. The authors should verify this entry, as it may affect the comparison.

5. **The two-stage training algorithm's "well harmonized" criterion is not operationalized.** The paper defines it as performance "similar to that of a pre-trained model at the target resolution" (§3.3) but does not specify the convergence criterion (e.g., within X% of baseline accuracy, after Y epochs of no improvement). While the ablation (Figure 5) demonstrates the algorithm's benefit, the lack of an explicit stopping condition makes the procedure difficult to reproduce precisely.

### Trivial

- None beyond the minor issues above.

## Nice-to-Haves

- An evaluation where PAC-FNO is attached to a frozen pre-trained backbone (only the module is trained) would directly test the claim that PAC-FNO is "ready to work with existing image recognition models" without modifying the downstream model's weights.
- The sensitivity study (Figure 5) finds that for ResNet-18 on ImageNet-1k, the optimal PAC-FNO has n=1, m=2 (only 2 parallel blocks), while the parallel vs. serial ablation (Figure 4) used 8 total blocks. Discussing why more blocks do not further improve performance and whether the optimal configuration varies across backbones/datasets would strengthen the paper.

## Removed Points

- **Two-stage training algorithm novelty criticism** (from Harsh Critic #4): The reviewer claimed the two-stage algorithm's novelty is unclear and its necessity is not argued. However, the paper explicitly motivates it (§3.3: "the pre-trained backbone model may not be able to fully understand the hidden space created by the PAC-FNO"), and the ablation (Figure 5) demonstrates its effectiveness. The contribution framing is proportionate — it is presented as a training procedure rather than a major architectural innovation. This is a reasonable training strategy adapted to the setting, not a claimed breakthrough. Moving to Removed Points as the paper's own framing is appropriate and the criticism overstates the novelty claim.

## Novel Insights

The most effective cross-check between the reviews is the conflict between the claimed strength of the all-component design (Strength Finder points to the Pets 28×28 result as validation) and the missing isolation experiment (Harsh Critic notes the confound). Both are correct: the PAC-FNO result is impressive, but without a parallel-FNO-with-filter baseline, one cannot determine whether the improvement comes from removing the low-pass filter or from the parallel structure. The parallel vs. serial ablation (Figure 4) shows that parallel helps when the all-component block is held constant, but the reverse ablation (fix parallel, vary filter) is absent. This means the most novel claim — that removing the low-pass filter is beneficial — is currently the least supported.

## Suggestions

1. Add the missing ablation: fix the parallel structure (e.g., n=1, m=2 or n=1, m=4) and compare two variants — one using a standard FNO block (with low-pass filter) and one using the proposed AC-FNO block (without filter). Report this on at least ImageNet-1k and one fine-grained dataset.
2. Report results on all 19 ImageNet-C/P corruptions (at minimum as an average or table in the appendix/supplement), or clearly justify the selection criterion for the 4 reported corruptions. If space is a concern, provide category-wise averages (noise, blur, weather, digital) in addition to individual results.
3. Trace the 77.1% abstract claim to a specific table cell with a clear definition of how the improvement is computed (absolute vs. relative, which baseline, which resolution/dataset).
4. Report relative accuracy in at least one table or explicitly state why it was omitted.
5. Specify the convergence criterion for the "well harmonized" condition in the two-stage algorithm.
6. Verify the Food-101 DRPN entry at resolution 112 and correct if erroneous.

## Score and Decision

The paper tackles an important real-world problem and proposes an intuitive, well-motivated architecture (PAC-FNO) with strong empirical results across multiple backbones and datasets. The consistency of the gains — especially the dramatic improvements at very low resolutions on fine-grained tasks — suggests the approach has genuine merit. However, two structural issues prevent full confidence in the contribution: the core claim about the all-component design is confounded with the parallel structure, and the evaluation on input variations covers only 4 of 19 corruptions without justification. These are fixable with additional experiments, but as submitted the evidence is incomplete. The paper makes a solid contribution that would be strengthened by addressing the missing ablation and broadening the robustness evaluation.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>