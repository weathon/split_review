## Summary

This paper proposes Progressive Visual Relationship Inference (PVRI), a scene graph generation method that augments standard relationship representations with fine-grained visual cues. The method has three components: (1) Known Cues Collection (KCC) — using an LLM to generate textual descriptions of visual cues and aligning them to image regions via CLIP cross-attention; (2) Unknown Cues Extraction (UCE) — learning latent part-based filters from object semantic features; and (3) Progressive Inference (PI) — refining predicate representations through a semantic hierarchy. Evaluated on Visual Genome and OpenImages V6.

## Strengths

- **Consistent gains on mean recall (mR@K) across all three SGG subtasks on VG**: PVRI reports 36.9/38.2 (PredCls), 18.7/20.6 (SGCls), and 15.4/17.2 (SGGen) on mR@50/100 (Section 4.2). Because VG is heavily long-tailed, mR@K is more reliable than R@K, and the method delivers its strongest results on this metric — directly supporting the claim that fine-grained cues help resolve rare and ambiguous predicates.

- **Novel use of LLM-generated fine-grained textual cues aligned to visual regions via CLIP cross-attention**: The KCC strategy (Section 3.3) goes beyond prior hierarchy-based approaches (Zhou et al. 2020, Zhang et al. 2024a) by having an LLM produce explicit descriptions of subtle visual distinctions (e.g., "upright leg" distinguishing "stand on" from "walk on"), then using both global cosine similarity and local convolutional cross-attention on CLIP patch embeddings to localize these cues in the image. This is a concrete and novel mechanism for injecting interpretable, fine-grained knowledge.

- **Ablation confirms both KCC and UCE contribute complementarily**: In Table 4, the complete model (17.2 mR@100 on SGGen) outperforms KCC-only (16.1) and UCE-only (14.4), and the combination also improves over each on Body/Tail predicate groups. This shows the two strategies address different aspects of cue extraction and are not redundant.

- **Stronger performance on tail predicates than ablations**: The complete model achieves 10.2% on tail predicates (Table 2), while KCC-only (9.7) and UCE-only (8.6) both fall short. This is significant because tail predicates are exactly where the paper's motivating problem (limited training examples, subtle differences) is most acute.

## Weaknesses

### Fatal

None.

### Major

- **Backbone confound makes comparisons to baselines uninterpretable**: PVRI uses CLIP ViT-B/16 as its visual backbone (line 234) — a large vision-language model pretrained on 400M image-text pairs. The baselines (IMP, MOTIFS, VCTree, BGNN, GPS-Net, etc.) all use standard detection backbones (ResNet-based Faster-RCNN). The paper never runs any baseline with the same CLIP backbone, nor does it ablate whether simply using CLIP features in a simpler method would achieve similar gains. Because CLIP provides substantially richer visual representations than ResNet, the reported improvements on R@K and mR@K cannot be confidently attributed to PVRI's proposed components (KCC, UCE, PI). The ablation (Table 4) helps internally but lacks a "CLIP backbone without any PVRI component" baseline, so the marginal contribution of KCC/UCE/PI over just using CLIP features is unclear.

- **Interpretability claimed but entirely unsubstantiated**: The paper identifies "lack of interpretability" as one of three core problems (lines 10, 27) and lists demonstrating "interpretability" as a main contribution (line 39: "demonstrate the effectiveness and interpretability of our method"). Yet the evaluation consists entirely of standard SGG metrics (R@K, mR@K, wmAP) — all of which measure prediction accuracy, not interpretability. There are zero qualitative examples, attention visualizations, cue analyses, human studies, or any evidence that PVRI makes relationship predictions more interpretable. If interpretability is claimed as a contribution, the paper must demonstrate it.

- **LLM-based cue generation is critically under-specified**: The KCC component, central to the method, provides: (a) no prompt templates, (b) no specification of which LLM was actually used in experiments (GPT-4 is mentioned only as an example in the introduction, line 29; the method section does not specify), (c) no examples of generated cue descriptions, (d) no validation or quality control of LLM outputs, and (e) no specification of how many cues per object category ($m_i$). The reader cannot reproduce, evaluate, or even understand what "visual cues" the model is actually using. This is a structural issue: the method's core data source is a black-box procedure with unstated inputs and no analysis.

- **Missing "neither KCC nor UCE" baseline in ablation**: The ablation (Table 4) evaluates KCC-only, UCE-only, and the full model — all of which use the CLIP backbone. There is no baseline that uses the CLIP backbone but discards both KCC and UCE (i.e., the basic two-stage SGG pipeline with CLIP features, without any cue mechanisms). Without this, the ablation cannot isolate whether the performance comes from PVRI's cue mechanisms or simply from using CLIP features in the inference pipeline.

### Minor

- **Factual error in contribution summary**: The contributions list (line 39) claims "we conduct experiments on four benchmark datasets." Only two datasets (Visual Genome, OpenImages V6) are ever mentioned, described, or evaluated. The abstract (line 19) and conclusion (line 279) correctly state two datasets. This is a verifiable factual inconsistency in a core claim.

- **UCE parameter $P$ never specified**: The paper generates "$P$ convolutional filters" (line 138) but never gives the value of $P$. The nature of these filters (spatial extent, how they act on patch embeddings) is also unclearly specified — they are described as $1\times1$ filters but their application mechanism is not fully detailed.

- **Missing hyperparameters**: Loss weights $\lambda_o$ and $\lambda_{pi}$ (line 216, though the subscript is printed as $\lambda_{rti}$) are never given numerical values. Hierarchy construction details (clustering algorithm, linkage criterion, distance threshold, number of layers) are not specified beyond "hierarchical clustering strategy" (line 151).

- **GloVe/CLIP embedding mismatch not justified**: The hierarchy clustering uses GloVe embeddings while node representations use CLIP embeddings (line 171). The paper does not justify this mismatch or analyze whether a consistent embedding source would change results.

### Trivial

None.

## Nice-to-Haves

- Providing the actual LLM prompts used and examples of generated cues for several object categories would substantially strengthen reproducibility.
- Reporting variance or confidence intervals for the key results would clarify whether reported gaps are meaningful.
- Qualitative analysis (attention maps from KCC, visualization of learned unknown cues) would support the method's motivation.
- Running at least one strong baseline (e.g., MOTIFS or BGNN) with CLIP ViT-B/16 features would isolate PVRI's contribution from the backbone advantage.

## Removed Points

These points were flagged for removal; treat them with caution:

1. **Garbled text in Section 3.1** (Harsh Critic): Lines 55-57 have incomplete/fragmented sentences ("please consult yourself", missing item 2 in enumerated list). Per policy, formatting/parser artifacts in the extracted text — which are consequences of PDF-to-text extraction, not author errors — are removed.

2. **Absent footnote content** (Harsh Critic mentions missing footnotes 2,3,4): These are stripping artifacts from PDF-to-text extraction; they exist in the original submission. Removed per policy.

3. **No statistical significance / variance reported** (Harsh Critic): Single-run evaluation without confidence intervals is standard practice in SGG. Moved to Nice-to-Have.

4. **Missing qualitative analysis of unknown cues** (Harsh Critic): Would strengthen the paper but is not a core flaw. Moved to Nice-to-Have.

5. **Strength Finder's generic strengths about "addressing important problem"**: Removed per policy to keep only concrete, evidence-grounded strengths.

6. **Formatting/style nitpicks about prose quality**: Removed per policy.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Control the backbone confound**: Re-run at least one strong baseline (e.g., MOTIFS or BGNN) with the same CLIP ViT-B/16 backbone. Add a "CLIP backbone without KCC/UCE/PI" ablation. Without this, the reported performance gains cannot be attributed to the proposed method.

2. **Provide LLM details**: Include prompt templates, the specific LLM used, examples of generated cues for several object categories, and an analysis of cue quality (e.g., human rating or ablation showing better cues improve performance).

3. **Support or retract the interpretability claim**: Either provide interpretability evidence (attention maps, cue visualizations, qualitative comparisons showing how PVRI explains its predictions) or remove the claim from the contributions.

4. **Fix the "four datasets" error**: Correct to "two datasets" to match the actual experiments.

5. **Specify missing parameters**: Report $P$, $\lambda_o$, $\lambda_{pi}$, and hierarchy construction details (clustering algorithm, linkage, threshold, number of layers).

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>