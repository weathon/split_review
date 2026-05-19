- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have all the information needed. Let me produce the final consolidated review.

## Summary
This paper introduces SIM, a framework combining surface vision transformers (SiT) with tri-modal CLIP contrastive alignment (fMRI, video, audio) for cross-subject decoding of movie-watching stimuli from 7T fMRI. The model is pre-trained with a video surface masked autoencoder (vsMAE) and then aligned to videoMAE and wav2vec embeddings via CLIP, enabling retrieval and reconstruction of visual/auditory stimuli from cortical activity. The key claimed advance is generalization to subjects and movie clips unseen during training, validated on the HCP 7T movie-watching dataset (N=174).

## Strengths
1. **Strong quantitative results for cross-subject decoding with seen movies (Experiment 1).** Table 1 reports 76.8% top-1 accuracy for fMRI→video retrieval (tri-modal) on new subjects viewing movies seen during training — a substantial improvement over the Ridge regression baseline (15.6%) and random chance (3.7%). The tri-modal CLIP alignment also demonstrably outperforms bimodal variants (76.8% vs. 64.7% for fMRI→V), showing that audio-video joint encoding provides complementary information for brain decoding.

2. **Interpretable attention maps aligning with known functional networks.** The paper visualizes self-attention heads from the SiT encoder and shows they specialize into sensorimotor, visual, and auditory cortices, with correlation to Margulies' gradient maps. This provides neurobiological validity for the model's internal representations and is a meaningful departure from black-box decoding approaches (Section 5, Figure 4).

3. **Reconstruction generalizes to unseen subjects and movie scenes.** Using the trained CLIP embeddings, the model reconstructs video frames from fMRI of unseen subjects and clips, preserving semantic content (Figure 6). This extends the framework beyond retrieval into generative decoding, demonstrated for both seen and unseen movies.

4. **Well-designed experimental setup isolating generalization factors.** The paper defines three explicit experiments (new subjects only, new stimuli only, both) with separate train/test splits and both soft- and hard-negative sampling (Figure 2, Table 1, Figure 5). This systematic evaluation provides a clear picture of where generalization does and does not hold.

## Weaknesses

### Fatal
None.

### Major

1. **Experiment 3 results — the paper's headline claim — are not presented with the same quantitative rigor as Experiment 1 in the main text.** The abstract and introduction foreground generalization to both new subjects and new movies (Experiment 3), yet Table 1 — the main results table — reports only Experiment 1 (new subjects, seen movies). Experiment 3 results are relegated to Figure 5, whose caption states "Results (in %) with μ and 95% conf. interval" but does not specify whether the y-axis is top-1, top-5, or another metric. Hard-negative results for Experiment 3 are not presented in the main text at all. The paper references supplementary Tables C.1–C.3 and Figure C.5 for these, but the main text does not give the reader any clear numeric top-1/top-10 values for the setting that defines the paper's core contribution. This makes it impossible to evaluate from the main paper alone how much generalization the model achieves in the hardest condition.

2. **Only one non-trivial baseline (Ridge regression); no comparison against any other deep learning architecture.** The paper compares only against Ridge regression on MSMAll-aligned vertex values. This conflates two potential sources of improvement: (a) using a powerful non-linear transformer with contrastive CLIP learning, and (b) the specific surface-patching mechanism of the SiT. Without an ablation replacing the SiT encoder with a volumetric ViT, a surface CNN (e.g., BrainSurfCNN), or even a simple MLP on the same features, the evidence does not isolate what the surface-specific design contributes. The paper cites Dahan et al. (2022, 2024) showing SiT outperforms surface CNNs on phenotyping tasks, but decoding retrieval is a different setting that warrants a direct baseline.

### Minor

3. **No explicit control for low-level visual feature confounds in the retrieval evaluation.** The 76.8% top-1 accuracy for fMRI→video is strikingly high (5× the Ridge baseline). While hard-negative sampling (negatives from the same movie) partially mitigates semantic confounds, the paper does not show that the model fails on scrambled stimuli, temporally mismatched clips, or other controls for low-level features (e.g., luminance, motion energy, scene cuts) that might be predictable from cortical activity.

4. **Self-attention correlation analysis lacks statistical rigor.** The paper states that "Gradient 2 is the highest correlated with all attention heads" but does not report actual correlation coefficients, confidence intervals, or whether comparisons survive multiple-comparison correction across heads. This weakens an otherwise interesting interpretability analysis.

5. **Reconstruction results are presented without quantitative metrics.** Figure 6 shows reconstruction examples but provides no quantitative evaluation (e.g., SSIM, LPIPS, classification accuracy of reconstructed frames). Given that the reconstruction pipeline follows Ozcelik & VanRullen (2023), using comparable metrics would allow direct benchmarking.

6. **Subject-level variance is not reported.** Results are averaged across test subjects, but for a cross-subject method, knowing whether performance is consistent or driven by particular subjects would be valuable.

7. **Uneven test-set sizes across modalities are explained only vaguely.** Video retrieval uses M=64 clips while audio uses M=32, explained as "audio samples being noisier." This makes cross-modality comparisons of top-K accuracy difficult since chance levels differ.

### Trivial
- The forward-looking claim about "Digital Twins" (Abstract, Introduction) is a rhetorical leap beyond what the paper demonstrates — the model does not adapt to individual subjects' idiosyncratic functional topographies.

## Nice-to-Haves
- Reporting the actual correlation coefficients with confidence intervals for the self-attention vs. Margulies gradient analysis.
- Including per-subject accuracy distributions to show whether the average performance is consistent or driven by outliers.
- Quantitative reconstruction metrics (SSIM, LPIPS) to enable direct comparison with prior work.
- Clarifying which training regime (frozen vsMAE, fine-tuned, or from scratch) was used for the main results in Table 1 — this is referenced to Table C.1 in the appendix but would strengthen the main text.

## Removed Points
These points were raised by reviewers but are excluded for the following reasons:
- **Garbled text in vsMAE description**: Parser artifact, not an author error. Per instructions, formatting artifacts from PDF extraction are removed.
- **Missing architectural details (hidden dim, dropout rate, layer count)**: Per instructions, nitpicks about undisclosed hyperparameters and trivial implementation details are removed.
- **Data/code placeholder URLs**: Placeholder URLs are standard for anonymized submissions; these will be populated upon publication.
- **The "ill-posed" claim about hyperalignment requires justification**: This is a brief rhetorical framing point that does not affect the paper's claims or results; insufficiently substantive for a weakness.
- **Missing related works**: Per instructions, the reviewer cannot verify missing citations without external sources.
- **6s temporal lag not justified**: The paper cites "Huth et al." for this choice — standard practice.
- **Criticism about MSMAll alignment reducing novelty of inter-subject contribution**: The paper openly states it uses MSMAll; this is part of the pipeline, not a hidden confound.

## Novel Insights
None beyond the paper's own contributions. The reviewers identify gaps in evidence presentation (Experiment 3 quantification, lack of architectural baselines) but do not surface unexpected findings or new connections not present in the paper.

## Suggestions
1. Move Exp 3 top-1/top-10 results (for both soft- and hard-negative sampling) with confidence intervals into the main Table 1 or a companion table, so the paper's headline claim is supported by the same level of quantitative evidence as Exp 1.
2. Add at least one architectural ablation — e.g., replace the SiT encoder with a volumetric ViT of comparable capacity or a surface MLP, keeping the CLIP training pipeline fixed — to isolate the contribution of the surface-patching mechanism from the general power of transformers + contrastive learning.
3. Include a control experiment showing that retrieval accuracy drops to near-chance when stimuli are temporally scrambled or when low-level features are permuted, to rule out confounds.
4. Report per-subject accuracy variability alongside averaged metrics.
5. Specify the top-K metric used in Figure 5's y-axis in the caption or text.
