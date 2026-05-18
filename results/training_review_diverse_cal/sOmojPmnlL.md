Now I have all the information I need. Let me compose the final consolidated review.

## Summary

The paper proposes AnyExpress, an audio-driven portrait animation framework that removes the standard ReferenceNet module used in prior methods, replacing it with a weaker Text-FaceID control mechanism and a lightweight Audio-Motion Adapter. This achieves a 7× reduction in trainable parameters and enables "Freeform Portrait Animation" with three claimed capabilities: any face pose, any animated context, and any text-based control. The paper also introduces Progressive Prefix Conditioning with anchor alignment for long-video temporal consistency.

## Strengths

- **ReferenceNet-free design is well-motivated and architecturally clean.** The entropy analysis in Figure 3 provides a quantitative justification for why strong ReferenceNet control constrains generation diversity, and the proposed weak Text-FaceID control is a sensible alternative. The modular Audio-Motion Adapter design (Section 3.4) cleanly separates motion dynamics from identity and pose, enabling plug-and-play integration with personalized T2I models without retraining.

- **Strong quantitative results on the Any Face Pose capability.** Table 2 shows AnyExpress achieves the best or second-best scores on Pose Diversity (ΔP), Sync-C/D, DOVER, FaceID Consistency, and CLIP-I against four baselines (AniPortrait, MegActor, EchoMimic, V-Express). The advantages on Pose Diversity and DOVER are particularly notable given the paper's stated goal of enabling more flexible generation.

- **Multiple well-designed ablation dimensions.** Figures 7 and 8 systematically ablate the Progressive Prefix Conditioning strategy, the two-stage training strategy, the number of trainable motion blocks, and the choice of identity controller (IP-Adapter-Face vs. ReferenceNet/Face-Adapter). While these are qualitative, they cover the key design choices and show clear visual degradation when the proposed configuration is altered.

- **First to define and demonstrate the Freeform Portrait Animation task.** The paper identifies a genuine limitation in current ReferenceNet-based methods and defines a new task formulation with practical relevance. The qualitative demonstrations (Figures 5, 6a, 6b) show capabilities—animated backgrounds and text-controlled identity/background—that existing methods cannot produce.

## Weaknesses

### Fatal
None.

### Major

1. **Two of three claimed capabilities lack quantitative or perceptual evaluation.** The paper defines Freeform Portrait Animation via three capabilities—any face pose, any animated context, any text control—but only the first is quantitatively evaluated (Table 2). Animated contexts (Section 4.3, Figure 6a) and text-based control (Section 4.3, Figure 6b) are supported only by qualitative examples. The paper acknowledges that no open-source baselines exist for text-controlled portrait animation, but this does not excuse the absence of absolute evaluation (e.g., CLIP text-image alignment for text prompts, background motion magnitude for animated contexts, or a user study). Without such evidence, the claim that AnyExpress *reliably delivers* on these capabilities is not convincingly supported.

2. **The "any face pose" quantitative evaluation is underspecified.** The paper does not describe how face pose was varied during the Table 2 evaluation. Section 3.4 mentions compatibility with pose control adapters (Zhang et al., 2023b; Mou et al., 2024), but the experimental setup (Section 4.1) does not state: which specific pose adapter was used (if any), how target poses were generated (e.g., random sampling, from a driving video, uniformly distributed angles), or what range of poses was tested. Since the baselines compared use different mechanisms for pose variation, the reader cannot determine whether AnyExpress's performance reflects the audio-motion adapter itself or properties of the external pose controller it was paired with.

### Minor

1. **Identity–flexibility trade-off is acknowledged but not analyzed.** In Table 2, V-Express achieves higher FaceID Consistency and CLIP-I scores than AnyExpress. The paper's argument is that weaker identity control buys greater flexibility—a plausible and potentially valuable trade-off—but it is not quantified. There is no scatter plot or Pareto analysis showing FaceID vs. Pose Diversity across methods, and no discussion of how much identity preservation is sacrificed for gains in flexibility. This makes it hard to assess whether the trade-off is favorable.

2. **Progressive Prefix Conditioning ablation is qualitative only.** The ablation in Figure 7a compares Progressive Fusion, prefix conditioning without anchor alignment, and the full method via side-by-side frames. While visually informative, a quantitative metric of temporal consistency (e.g., frame-wise LPIPS across window boundaries, color histogram variance) would strengthen the claim that anchor alignment reliably eliminates non-smooth transitions—especially since the paper identifies this as a key technical contribution.

3. **No parameter-count comparison table.** The abstract claims a 7× reduction in trainable parameters over ReferenceNet-based methods, but no table or figure breaks down the parameter counts. Given that parameter efficiency is stated as an advantage, a direct comparison (e.g., AnyExpress vs. EchoMimic or AniPortrait in terms of trainable parameters and GPU-hours) would meaningfully strengthen the paper.

4. **No discussion of limitations or failure cases.** The paper presents no cases where the method struggles—e.g., identity drift under extreme poses, text instruction failures, or lip-sync degradation with noisy audio. A brief limitations paragraph would improve credibility and guide future work.

### Trivial
None.

## Nice-to-Haves

- Report FID/FVD on a reconstruction-style subset (e.g., where the reference image pose is used as the target) to show the method does not catastrophically degrade standard metrics.
- Add a quantitative temporal consistency metric (e.g., inter-window LPIPS) to the Progressive Prefix Conditioning ablation.
- Include a scatter plot of FaceID vs. Pose Diversity to visualize the identity–flexibility trade-off.
- Conduct a small user study for text-driven animations and animated backgrounds to supplement qualitative results.

## Removed Points

- **"The two-stage training strategy ablation shows only one alternative (stage 1 only)."**—Factually incorrect. The paper (Figure 7b / lines 169–170) shows two alternatives: (1) no motion module fine-tuning, and (2) stage 1 only. The broader observation that these ablations are qualitative-only is retained in Minor Weaknesses.
- **"The claim of being 'the first to introduce this task' is overstated."**—The paper couches this as "to the best of our knowledge" (line 23), which is standard language. The claim is reasonable given the novel joint formulation of face pose + animated context + text control.
- **"Weak Control entropy analysis (Fig. 3) presentation is fragile / only two U-Net blocks."**—Showing shallow and deep U-Net blocks (3rd and 12th) is standard practice; two representative layers are sufficient to illustrate the trend. The analysis is conceptually sound and not "fragile."
- **"Missing appendix content."**—Parser artifacts; appendices exist in the original submission.
- **"Comparison on standard portrait animation metrics (FID/FVD)."**—The paper explicitly justifies why standard FID/FVD are not well-suited for the Freeform Portrait Animation setting (line 118). Moved to Nice-to-Haves.
- **Strength Finder point about "thorough ablation studies"**—The word "thorough" overstates what are qualitative ablations. Retained as a genuine but more modest strength.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation across the reviews is the tension between the paper's strong architectural motivation (the entropy analysis in Figure 3 provides a principled, quantitative reason why ReferenceNet constrains generation) and its underdeveloped evaluation of two of its three defining capabilities. The entropy analysis could itself be a starting point for a broader study of when "weak control" is beneficial versus detrimental in generative models—for instance, characterizing the Pareto frontier between control strength and output diversity across different tasks. The paper would benefit from making this perspective more explicit rather than treating the entropy analysis as a one-off justification.

## Suggestions

1. Add quantitative or perceptual evaluation for animated contexts (e.g., background optical flow magnitude vs. static-background baseline) and text control (e.g., CLIP text-image alignment scores between generated frames and text prompts). Even a small user study would significantly strengthen the claims.

2. Specify the pose variation protocol used in the Table 2 evaluation: which pose adapter, how target poses were generated, and the range of poses tested. This is essential for reproducibility and for interpreting whether the observed flexibility comes from the audio-motion adapter or the external pose controller.

3. Add a table comparing trainable parameter counts and training cost against representative ReferenceNet-based methods to support the 7× reduction claim.

4. Include a brief limitations section discussing failure cases (e.g., extreme poses, text control failures) to improve credibility.

## Score and Decision

**Overall assessment**: The paper makes a genuine architectural contribution—removing ReferenceNet from portrait animation via a lightweight Audio-Motion Adapter—and provides a well-motivated theoretical justification (entropy analysis) and strong results on the Any Face Pose capability. However, the evaluation is incomplete: two of the three task-defining capabilities lack quantitative support, and the main evaluation setup is underspecified. These gaps prevent the paper from fully substantiating its claims, though they are addressable. The core ideas are promising and the methodology is sound.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>