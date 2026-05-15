Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces SIM, a framework combining surface vision transformers (SiT) with tri-modal CLIP contrastive learning (audio, video, fMRI) to enable cross-subject and cross-stimulus decoding from 3-second clips of 7T fMRI data from the HCP movie-watching dataset. The core idea is that icosahedral patching of the cortical surface preserves spatial topography while the transformer captures long-range spatio-temporal dynamics. Three generalization scenarios are tested: new subjects (same movies), new movie scenes (same subjects), and both. The main results show high retrieval accuracy (76.8% top-1 for fMRI→video with hard-negative sampling), substantially outperforming Ridge regression baselines, with attention maps that align to known functional networks.

## Strengths

- **Demonstrated generalization to both unseen subjects and unseen movie stimuli**: The paper explicitly designs three generalization experiments and provides strong evidence (Table 1, Figure 5) that the SiT+CLIP framework achieves 76.8% top-1 accuracy for fMRI→video retrieval (hard-negative, new subjects), far exceeding the Ridge regression baseline (15.6%). Experiment 3 simultaneously tests generalization to new subjects AND new movie scenes, which is a meaningful advance over prior work that largely trains and tests within the same subjects.

- **Tri-modal CLIP alignment measurably improves decoding**: The paper introduces a tri-modal contrastive loss averaging six pairwise directional losses. Evidence that this joint training adds value: for fMRI→audio retrieval, tri-modal achieves 56.6% top-1 vs. 19.9% for bi-modal (fMRI, audio only); for fMRI→video, tri-modal (76.8%) outperforms bi-modal (64.7%). This is a genuine methodological contribution.

- **Surface vision transformer (SiT) with vsMAE pre-training provides a principled approach to cortical encoding**: The icosahedral patching preserves spatial autocorrelations across the cortical manifold, and the vsMAE self-supervision provides a pre-training task tailored to fMRI dynamics. The SiT-based model substantially outperforms Ridge regression even after MSMAll functional alignment, which is the standard inter-subject alignment method.

- **Interpretability analysis connects model representations to known neuroscience**: Attention maps projected back to the cortical surface are compared against Yeo networks, Margulies gradients, and the HCP multimodal parcellation, showing specialization into sensorimotor, visual, and auditory cortices.

## Weaknesses

### Fatal
None.

### Major

- **No comparison to alternative architectures under the same CLIP pipeline**: The paper's core architectural contribution is the SiT encoder, yet the only non-random baseline is Ridge regression (a linear method). Without comparing SiT against other reasonable neural backbones (e.g., a surface CNN, a 3D volumetric ViT, or even a shallow MLP on the same patched inputs) while keeping the CLIP alignment pipeline identical, it is impossible to determine whether the SiT architecture itself drives the gains or whether the CLIP alignment + vsMAE pre-training pipeline would work as well with a simpler encoder. The ablation experiments referenced in Table C.1 (appendix) compare SiT training strategies (frozen vs fine-tuned vs from scratch) but do not isolate the contribution of the SiT as an architecture. This undercuts the paper's central claim of a "surface vision transformer" contribution.

- **Reconstruction evaluation is anecdotal**: The video reconstruction (Figure 6) is trained on a single subject and tested on a single subject, with no quantitative metrics (FID, SSIM, or pixel accuracy). The paper acknowledges this limitation indirectly ("unable to effectively test whether the model would generalise to completely different movies"), but the framing of Figure 6 and its caption ("preserving most of the semantic information... generalise to new movie scenes and new subjects") overstates what can be concluded from N=1 qualitative examples. This section should be treated as illustrative rather than evidential.

### Minor

- **Within-split hemisphere independence inflates effective sample size**: The paper treats left and right hemispheres as independent samples, doubling the apparent training set (992 from 124 subjects × 4 sessions). Within the training split, multiple samples from the same subject are correlated (shared subject motion, anatomy, scanner effects), meaning the effective independent sample size is smaller than reported. The train/test split is clean (no subject appears in both), so the generalization claim for new subjects is not invalidated, but the reported confidence intervals on training performance may be anti-conservative.

- **Random baseline discrepancy unexplained**: The reported random baseline for fMRI→video top-1 is 3.7% with M=64 candidates. Expected accuracy under uniform random selection from 64 candidates is 1/64 ≈ 1.56%. This discrepancy is not explained in the paper. While the SiT results (64–77%) are far above either value and the Ridge baseline (15.6%) is the meaningful comparison, the numerical inconsistency is confusing and should be clarified.

- **No subject-level cross-validation for retrieval metrics**: Retrieval accuracy is reported across pooled query-clips rather than aggregated per test subject (e.g., compute top-1 per subject, then report mean ± std). Given the small number of test subjects (25), subject-level aggregation would be more statistically rigorous. The tight confidence intervals (±1–2%) may reflect within-subject correlations across multiple clips per subject rather than genuine precision.

- **The attention map correlation analysis lacks numerical detail**: The paper states that "Gradient 2 is the highest correlated with all attention heads" and mentions a correlation analysis against Margulies' gradient-based maps, but no correlation coefficients or statistical tests are reported in the main text (these may be in the supplementary). This reduces the strength of the interpretability claims.

### Trivial

- The choice of candidate pool sizes M=64 (video) and M=32 (audio) is provided with a brief justification ("audio samples being noisier") but would benefit from a sensitivity analysis showing how results vary with M.
- The cross-GPU batch aggregation for CLIP training (batch size 256) is mentioned but the mechanism (all-gather, etc.) is not described.

## Nice-to-Haves

- A comparison to recent inter-subject decoding methods (e.g., Thual et al. 2023, Scotti et al. 2024) would strengthen the positioning of the results.
- A sensitivity analysis of retrieval accuracy as a function of candidate pool size M would clarify whether the task becomes easier with smaller M and how robust the conclusions are.
- Subject-level blocked cross-validation for retrieval metrics would provide more reliable confidence intervals.
- Evaluating on entirely held-out movies (no clips from that movie in training) would be a stronger test of generalization than holding out only the second half of each movie.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Data splitting and independence violations inflate generalization claims [Structural]"** — The harsh critic claimed this is a fatal structural flaw that "cannot distinguish which factor drives retrieval success." This is an overstatement. The paper holds out test subjects entirely (no subject appears in both train and test). Experiment 3 tests on both new subjects AND new movies simultaneously. The hemisphere-as-independent-sample choice inflates the training count but does not cause train/test leakage. The model may learn less stimulus-pure patterns from correlated training samples, but the held-out subject evaluation still tests genuine generalization. Reduced to a minor weakness above.

2. **"Evaluation metric and negative sampling procedure raise doubts about reported accuracy"** — The harsh critic claims the 76.8% hard-negative result is "surprising given the low temporal resolution of fMRI" and the results are "unconvincing." This is a subjective opinion rather than a documented flaw — the paper reports the procedure transparently, and high accuracy on hard negatives from the same movie is a strong (not suspicious) result. The point about the random baseline discrepancy is retained as minor; the rest of this criticism is removed as speculative.

3. **Criticism of garbled text in vsMAE description** — This is a PDF parsing artifact, not an author error.

4. **Claim that the paper provides "no evidence" that SiT is responsible for gains** — The paper does reference ablation experiments in Table C.1 (appendix) and shows bi-modal vs tri-modal comparisons. The architectural comparison point is retained as a major weakness but reformulated precisely.

5. **"The limitations section does not address the fatal flaws in evaluation design"** — The paper's limitations section discusses scaling, subcortical omissions, temporal window constraints, and dataset limitations. The claimed "fatal flaws" do not exist as characterized.

## Novel Insights

The reviews surface an important tension: the paper makes a genuine architectural contribution (surface transformers for fMRI decoding) and provides the most comprehensive inter-subject generalization evaluation in this domain, yet the experimental design lacks the ablations needed to attribute performance specifically to the SiT. The harsh critic correctly identifies that without comparing SiT to simpler encoders under the same CLIP pipeline, the paper cannot rule out that its improvements come from the CLIP alignment + vsMAE pre-training framework rather than the surface transformer architecture. This is a common failure mode in multi-component ML systems and would be straightforward to address with additional experiments. Meanwhile, the tri-modal CLIP comparison (bi-modal vs. tri-modal) is a well-executed ablation that convincingly shows the value of the paper's second contribution.

## Suggestions

1. **Add an architectural ablation**: Train a version of the model that replaces the SiT encoder with a simpler alternative (e.g., average pooling of patched features + linear layer, or a surface CNN) while keeping the vsMAE pre-training and CLIP alignment pipeline identical. This is the single most important experiment needed to isolate the contribution of the SiT.

2. **Report subject-level retrieval metrics**: Aggregate top-1 accuracy per test subject and report mean ± std across subjects, rather than pooling all query-clips. This would produce more statistically rigorous confidence intervals and address concerns about within-subject correlations.

3. **Explain the random baseline computation**: Clarify how the 3.7% random top-1 for fMRI→video is obtained when M=64 (expected 1/64 ≈ 1.56%). If the procedure differs from the model evaluation, describe it explicitly.

4. **Provide quantitative reconstruction metrics**: Even a small-scale evaluation with FID or SSIM on a handful of subjects would substantially strengthen the reconstruction claims.

5. **Perform a sensitivity analysis over M**: Show how top-1/top-10 accuracy changes as the candidate pool size M varies (e.g., M=32, 64, 128, 256) to demonstrate that the retrieval performance is not artificially inflated by a small candidate pool.

## Score and Decision

The paper presents a technically interesting and largely sound pipeline for inter-subject multimodal fMRI decoding, with the strongest generalization evaluation in this space. The core claims (that the framework can decode stimuli from new subjects and new movies) are supported by the evidence, and the tri-modal CLIP ablation convincingly demonstrates the value of joint audio-video-fMRI alignment. The major weakness is the missing architectural ablation for the SiT component, which prevents full attribution of the gains to the surface transformer. This is addressable but should be fixed before publication.

Overall assessment: The paper makes a genuine contribution to the field and the main claims are supported, but a key ablation is missing. With the addition of this experiment, the paper would be solid.

**Score: 7.0** (Good paper, accept. A well-executed contribution with some weaknesses that should be addressed.)

Wait, let me reconsider the scoring guidelines more carefully. The score should reflect my assessment of the paper's quality after review.

The paper has a major weakness (missing SiT architectural ablation) but the core claims are supported by the available evidence. The tri-modal CLIP contribution is well-validated. The generalization to new subjects and new movies is demonstrated. The missing ablation doesn't invalidate the results but makes the central architectural claim less well-supported.

For a venue like NeurIPS/ICML, this would be a borderline paper. Let me score it 6.0 (weak accept / borderline) reflecting that the contribution is real but the key architectural ablation is missing.

Actually, let me re-read the instructions: "Score round to .5 or .0." and "If the FUNDAMENTAL ISSUES was triggered on top, rate the paper low accordingly."

I determined there are no fatal/fundamental issues. So the paper can be scored reasonably. Given the missing architectural ablation (major weakness), I think 6.0 is appropriate - borderline accept.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>## Summary

This paper introduces SIM, a framework that combines surface vision transformers (SiT) with tri-modal CLIP contrastive learning (audio, video, fMRI) to enable cross-subject and cross-stimulus decoding from 3-second clips of 7T fMRI data from the HCP movie-watching dataset. Three generalization scenarios are tested: new subjects, new movie scenes, and both simultaneously. The main results show high retrieval accuracy (76.8% top-1 for fMRI→video with hard-negative sampling), substantially outperforming Ridge regression baselines, with attention maps that align to known functional brain networks.

## Strengths

- **Demonstrated generalization to both unseen subjects and unseen movie stimuli**: The paper explicitly designs three generalization experiments and provides strong evidence (Table 1, Figure 5) that the SiT+CLIP framework achieves 76.8% top-1 accuracy for fMRI→video retrieval (hard-negative, new subjects), far exceeding the Ridge regression baseline (15.6%) and random (3.7%). Experiment 3 simultaneously tests generalization to new subjects AND new movie scenes, which is a meaningful advance over prior work that largely trains and tests within the same subjects. Two-sample t-tests (Ridge vs SiT) all yield p<0.001.

- **Tri-modal CLIP alignment measurably improves decoding over bi-modal**: The paper introduces a tri-modal contrastive loss averaging six pairwise directional losses. The evidence that joint training adds complementary information is clear: for fMRI→audio retrieval, tri-modal achieves 56.6% top-1 vs. 19.9% for bi-modal (fMRI, audio only); for fMRI→video, tri-modal (76.8%) outperforms bi-modal (64.7%). This is a genuine and well-validated methodological contribution beyond typical bi-modal (fMRI–video) alignments.

- **Surface vision transformer with vsMAE pre-training provides a principled cortical encoding approach**: The icosahedral patching preserves spatial autocorrelations across the cortical manifold, and the vsMAE self-supervision provides a pre-training task tailored to fMRI dynamics. The SiT model substantially outperforms Ridge regression even after MSMAll functional alignment (which already reduces inter-subject variability), demonstrating that the model captures functional dynamics beyond what linear alignment can provide.

- **Interpretability analysis connects model representations to established neuroscience**: Attention maps interpolated back to the cortical surface are compared against Yeo networks, Margulies gradients, and the HCP multimodal parcellation, revealing specialization into sensorimotor, visual, and auditory cortices. The finding that Gradient 2 (unimodal–transmodal axis) correlates highest with all attention heads provides a mechanistic link between model attention and known cortical organization.

## Weaknesses

### Fatal
None.

### Major

- **Missing architectural ablation for the SiT encoder**: The paper's core architectural contribution is the SiT, yet the only non-random baseline is Ridge regression (a linear method). The ablation experiments referenced in Table C.1 compare SiT training strategies (frozen vs fine-tuned vs from scratch), but there is no comparison to alternative neural architectures (e.g., a surface CNN, a 3D volumetric ViT, or even a shallow MLP on the same patched inputs) under the same vsMAE pre-training and CLIP alignment pipeline. Without this, it is impossible to determine whether the SiT architecture itself drives the gains or whether the CLIP alignment + vsMAE pre-training framework would work as well with a simpler encoder. This undercuts the paper's central claim that the surface transformer is responsible for the improvements.

- **Reconstruction evaluation is anecdotal, not evidential**: The video reconstruction (Figure 6) is trained on a single subject and tested on a single subject, with no quantitative metrics (FID, SSIM, or pixel accuracy) provided. The caption claims the reconstructions "generalise to new movie scenes and new subjects," but an N=1 qualitative demonstration cannot support this claim. While the paper acknowledges some limitations of the dataset for reconstruction, the framing significantly overstates the evidence. This section should be treated as illustrative rather than as evidence for generalization.

### Minor

- **Left/right hemispheres treated as independent samples inflates effective training size**: The paper explicitly states that fMRI from left and right hemispheres are treated as independent samples. With 124 training subjects × 2 hemispheres × 4 sessions = 992 training samples, the effective independent sample size is smaller because hemispheres and multiple sessions from the same subject are correlated. This does not invalidate the held-out subject generalization (no subject appears in both train and test), but the reported sample counts and confidence intervals may be anti-conservative.

- **Random baseline discrepancy unexplained**: The reported random top-1 accuracy for fMRI→video is 3.7% with M=64 candidates. Expected accuracy under uniform random selection from 64 candidates is 1/64 ≈ 1.56%. The paper does not explain this discrepancy. While the SiT results (64–77%) are far above either value and the Ridge baseline (15.6%) is the meaningful comparison, the inconsistency is confusing and should be clarified.

- **No subject-level aggregation for retrieval confidence intervals**: Retrieval accuracy is reported across pooled query-clips rather than aggregated per test subject (mean ± std across subjects). With only 25 test subjects producing multiple queries each, within-subject correlations could make the reported bootstrap-style confidence intervals (±1–2%) anti-conservative.

- **Attention map correlation analysis lacks numerical detail**: The paper states "Gradient 2 is the highest correlated with all attention heads" but reports no correlation coefficients or statistical tests in the main text. This weakens the interpretability claims.

### Trivial

- The choice of M=64 for video and M=32 for audio is justified briefly ("audio samples being noisier") but would benefit from a sensitivity analysis.
- The cross-GPU batch aggregation mechanism for CLIP training (batch size 256) is mentioned but the implementation (all-gather, etc.) is not described.

## Nice-to-Haves

- A comparison to recent inter-subject decoding methods (e.g., Thual et al. 2023, Scotti et al. 2024) would strengthen the positioning of the results.
- A sensitivity analysis of retrieval accuracy as a function of candidate pool size M would clarify the difficulty of the task.
- Evaluating on entirely held-out movies (zero clips from that movie in training) would be a stronger test than holding out only the second half of each movie.
- Reporting retrieval metrics per subject (mean ± std across subjects) rather than pooled across queries.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Data splitting inflates generalization claims"** — The harsh critic characterized this as a fatal structural flaw that "cannot distinguish which factor drives retrieval success." This overstates the problem. The paper holds test subjects completely out of training (no leakage between splits). Experiment 3 tests on both new subjects AND new movies. The hemisphere-as-independent-sample choice inflates training counts but does not cause train/test leakage. Reduced to a minor weakness above.

2. **"Evaluation metric raises doubts about reported accuracy"** — The harsh critic claims the 76.8% hard-negative result is "surprising" and "unconvincing" given fMRI temporal resolution. This is a subjective opinion, not a documented flaw. The paper is transparent about the evaluation procedure. The random baseline discrepancy point is retained as minor; the rest of this criticism is removed as speculative.

3. **Criticism of garbled text in vsMAE description** — This is a PDF parsing artifact, not an author error.

4. **"The limitations section does not address the fatal flaws"** — The paper's limitations section discusses scaling, subcortical omissions, and dataset constraints. The claimed "fatal flaws" do not exist as characterized.

5. **Missing appendix content** — References to Appendix Tables/Figures (C.1, C.5, C.9, etc.) are parser-stripped; these exist in the original submission.

## Novel Insights

The reviews surface an important tension that is common in multi-component ML pipelines: the paper makes a genuine architectural contribution (surface transformers for fMRI decoding) and provides the most comprehensive inter-subject generalization evaluation in this domain, yet the experimental design lacks the ablations needed to attribute performance specifically to the SiT architecture rather than to the vsMAE pre-training + CLIP alignment framework. The tri-modal vs. bi-modal ablation is convincing and well-executed for the alignment component, but the SiT itself is not compared against alternative encoders. Meanwhile, the hemisphere independence issue, while not fatal, highlights a broader methodological challenge in neuroimaging ML — the gap between biological sample size and the inflated sample counts from multi-session, multi-hemisphere designs, which the field would benefit from addressing more explicitly.

## Suggestions

1. **Add an architectural ablation**: Train a version that replaces the SiT encoder with a simpler alternative (e.g., average pooling of patched features + linear projection, or a surface CNN) while keeping the vsMAE pre-training and CLIP alignment pipeline identical. This is the single most important experiment needed to isolate the contribution of the SiT.

2. **Report subject-level retrieval metrics**: Aggregate top-1 accuracy per test subject (mean ± std across subjects) rather than pooling all query-clips, to produce more statistically rigorous confidence intervals.

3. **Explain the random baseline computation**: Clarify how the 3.7% random top-1 for fMRI→video is obtained when M=64 (expected 1/64 ≈ 1.56%). If the procedure differs from the model evaluation, describe it explicitly.

4. **Provide quantitative reconstruction metrics**: Even a small-scale evaluation with FID or SSIM on a handful of subjects would strengthen the reconstruction section.

5. **Perform a sensitivity analysis over candidate pool size M**: Show how top-1/top-10 accuracy changes as M varies (e.g., 32, 64, 128, 256) to demonstrate that retrieval performance is robust to the choice of candidate pool size.

## Score and Decision

The paper presents a technically interesting and largely sound pipeline with the most comprehensive inter-subject generalization evaluation in the fMRI decoding literature. The core claims (that the framework can decode stimuli from new subjects and new movies) are supported by the evidence, and the tri-modal CLIP ablation convincingly demonstrates the value of joint audio-video-fMRI alignment. The major weakness is the missing architectural ablation for the SiT component, which prevents full attribution of the gains to the surface transformer — this is addressable but should be fixed. The paper makes genuine contributions (surface-based encoding for inter-subject decoding, tri-modal contrastive alignment), and the evaluation design (three explicit generalization scenarios) is a methodological strength worth preserving.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>