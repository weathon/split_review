Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes SIM, a framework that combines surface vision transformers (SiT) with tri-modal CLIP alignment (fMRI, video, audio) for decoding movie-watching stimuli from 7T fMRI data. The key contribution is demonstrating cross-subject and cross-stimulus generalisation: the model can retrieve which movie clip a person is watching using only their brain activity, even for subjects and movie clips never seen during training. The framework also produces interpretable attention maps that correlate with known functional brain networks, and enables video-frame reconstruction from fMRI of unseen subjects.

## Strengths

- **Generalisation to unseen subjects and novel movie clips**: The paper convincingly demonstrates cross-subject and cross-stimulus retrieval across three increasingly difficult experimental setups (Exp 1–3). Experiment 3 — the hardest setting where both subjects and movie clips are unseen — achieves 64.7% top-1 accuracy (hard-negative) for fMRI→video retrieval, a significant advance over prior decoding frameworks that operate within-subject. This is the paper's strongest contribution and is well-supported by the experimental design (Figure 2, Table 1, Figure 5).

- **Tri-modal CLIP alignment substantially improves decoding**: Adding audio to the fMRI↔video alignment raises top-1 hard-negative accuracy from 64.7% (fMRI, V) to 76.8% (fMRI, V, A) for fMRI→video, and from 19.9% to 56.6% for fMRI→audio (Table 1). This cleanly demonstrates that complementary audio information enriches the shared embedding space — a novel extension over prior bi-modal CLIP approaches.

- **Attention maps align with established functional neuroanatomy**: The paper projects self-attention weights back to the cortical surface and shows correspondence with known functional networks (Yeo networks, Glasser parcellation, Margulies gradients). This provides biological plausibility for what the model learns, going beyond pure retrieval metrics to offer mechanistic insight.

## Weaknesses

### Major

- **Video reconstruction results lack quantitative evaluation**: Figures 6, C.9, and C.10 show reconstructed frames qualitatively, and the paper claims they are "realistic, preserving most of the semantic information." No quantitative metrics (SSIM, LPIPS, CLIP similarity, or human rating) are reported. While reconstruction is a secondary contribution that borrows an existing pipeline (Ozcelik & VanRullen, 2023), the specific claim that the learned CLIP-aligned fMRI embeddings support semantic preservation across unseen subjects is an empirical one that requires quantitative backing. Without numbers, this section reads as a demonstration rather than a validated result.

### Minor

- **Ridge regression baseline is underspecified**: The paper states only that it "compare[s] against Ridge regression models, taking inspiration from Ozcelik & VanRullen (2023)" and that "all data has been MSMall (functionally) aligned across subjects." What input features the Ridge model uses is not stated — raw 40962-vertex surface data? PCA-reduced features? The same pre-processed data before SiT encoding? Given that this baseline is the only non-random comparator for the main retrieval results, specifying the exact architecture and input representation is necessary for reproducibility. (This does not threaten the core claim — the massive performance gap, Ridge 15.6% vs. SiT 64.7% in the hardest setup, makes it clear the SiT adds substantial value — but it should be fixed.)

- **Chance-level performance for hard-negative sampling not reported**: The paper reports random baseline as 3.7% for soft-negative sampling with M=64 candidates, but does not report chance for hard-negative sampling (where 63 negatives are drawn from the same movie, which shares similar semantic/visual content). While chance for M=64 uniform sampling is ~1.56%, the paper should explicitly state this and verify that the hard-negative task is distinguishable from chance given the reduced candidate pool per movie. Per-movie clip counts and a table of available candidates per movie would also help the reader assess feasibility.

- **Top-1 retrieval results (with CIs) for Experiments 2 and 3 are not displayed alongside top-10**: Figure 5 shows only top-10 accuracy with error bars for the soft-negative generalisation experiments. Top-1 results are provided for Experiment 1 in Table 1, but the reader cannot directly compare top-1 across all three experiments. These should be reported in the main text or supplement.

- **Attention map analysis lacks quantitative grounding**: The paper states that "a correlation analysis against Margulies' gradient-based maps shows that Gradient 2 is the highest correlated with all attention heads" and that attention heads "specialise in sensorimotor, visual, and auditory cortices," but no correlation coefficients, statistical tests, or quantitative overlap measures (e.g., Dice coefficients with Yeo networks) are reported. The qualitative figures are illustrative but the claims would be substantially strengthened by reporting actual numbers.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- **Additional spatial encoder baselines**: The ablation isolates SiT vs. Ridge, but adding a volumetric 3D CNN or a simple average of vertex-wise features (no spatial model) as additional baselines would more directly attribute performance differences to the SiT's specific spatial encoding mechanism.
- **Inter-subject correlation analysis**: Reporting the vertex-wise correlation across subjects for held-out clips (after MSMAll alignment) would help calibrate the upper bound of possible decoding performance and contextualise the results.
- **Distribution analysis of pre-trained encoders**: A brief discussion or embedding similarity analysis to check whether videoMAE and wav2vec encoders (pre-trained on datasets like HowTo100M) produce embeddings well-matched to Hollywood movie stimuli would address a reasonable concern.
- **Hemodynamic lag discussion**: A single 6s lag across all vertices is a simplification; acknowledging region-specific HRF variability would be helpful.

## Removed Points

- **Critic's claim that the Ridge baseline issue makes the central claim "unverifiable"**: This is overstatement. Ridge achieves 15.6% vs SiT's 64.7% in the hardest condition. Even without full specification of Ridge inputs, the performance gap is so large that the conclusion of SiT superiority holds. The critic's hypothetical that Ridge "might use the same pre-computed SiT features" is inconsistent with the observed performance and is not a realistic concern.
- **Criticism about frozen pre-trained encoder distribution mismatch being a weakness**: This is speculative and not grounded in evidence that the mismatch actually harms performance. The paper acknowledges dataset limitations in the discussion. Moved to Nice-to-Haves.
- **Call for more baselines (3D CNN, etc.)**: The paper's ablation is sufficient to support its claims. Additional baselines would strengthen but their absence is not a weakness. Moved to Nice-to-Haves.
- **Suggestion to compute inter-subject fMRI correlation to bound performance**: Interesting but not standard practice for decoding papers. Moved to Nice-to-Haves.
- **Strength Finder's generic strengths** (e.g., "addresses an important problem"): Removed for lacking specific content.

## Novel Insights

The most interesting observation from the review process is the tension between the paper's strongest result (76.8% top-1 hard-negative retrieval from fMRI of new subjects) and the limited diversity of the HCP movie stimuli (1–4.3 minute clips from Hollywood movies). If the model can indeed identify the exact 3-second clip from 63 within-movie distractors using only 3 seconds of fMRI from an *unseen subject*, then it is detecting remarkably fine-grained cortical signatures that survive functional alignment across individuals. This raises a question the field should investigate: what is the effective resolution of the shared functional topography after MSMAll alignment? If two different 3-second clips from the same movie produce distinguishable cortical activation patterns that generalise across subjects, the resolution of the common representational space may be considerably finer than typically assumed.

## Suggestions

1. **Specify the Ridge baseline**: State explicitly what input features it uses (e.g., "the same MSMAll-aligned 40962-vertex data, but with no spatial transformer encoding — a linear mapping from surface vertices to CLIP embedding space") and report its regularisation parameter.
2. **Add quantitative reconstruction metrics**: Report at least one automated metric (e.g., CLIP image similarity between original and reconstructed frame, or LPIPS) for the reconstruction experiments in Figures 6, C.9, C.10.
3. **Report hard-negative chance level**: State the theoretical and/or empirical top-1 chance for M=64 hard-negative sampling (given the candidate pool constraints).
4. **Add correlation coefficients for attention analysis**: Report numerical correlation values between attention maps and Margulies gradients, with statistical significance.

## Score and Decision

**Originality**: Strong — the integration of SiTs with tri-modal CLIP for cross-subject generalisation is novel. **Importance**: High — cross-subject decoding without per-subject dense recordings is an important open problem. **Claims**: Mostly well-supported, though the reconstruction claim needs quantitative backing. **Soundness**: The experimental design (three generalisation experiments, hard/soft-negative sampling, 95% CIs) is rigorous. **Clarity**: Generally clear, though the Ridge baseline description and attention analysis could be more precise. **Value**: The framework and findings are a meaningful contribution to the field of fMRI decoding and cortical functional topography modelling.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>