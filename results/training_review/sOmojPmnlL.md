Now I have a thorough understanding of the paper and can verify each claim. Let me synthesize the final review.

## Summary

This paper proposes AnyExpress, a ReferenceNet-free audio-driven portrait animation framework. The key idea is replacing the heavyweight ReferenceNet with a weak Text-FaceID control mechanism (using IP-Adapter-Face) and fine-tuning only a lightweight Audio-Motion Adapter, enabling what the authors call "Freeform Portrait Animation" — generation with any face pose, animated backgrounds, and text-driven control. The paper also introduces Progressive Prefix Conditioning for long-video consistency and a two-stage training strategy to prevent motion module overfitting.

## Strengths

- **Well-motivated problem and clean design philosophy**: The paper identifies a genuine limitation of ReferenceNet-based methods — their strong control rigidly binds pose and background to the reference image, limiting flexibility and requiring costly retraining for new base models. Replacing this with a weak, modular control signal is a sensible and well-articulated design direction (Sec. 1, Fig. 1).

- **Qualitative results demonstrate genuinely new capabilities**: Figures 5, 6a, and 6b show portrait animations with substantially more diverse poses, dynamic backgrounds, and text-driven identity/background changes than typical ReferenceNet outputs. The ability to animate a text-to-image generated character (Fig. 6b, bottom row) is a qualitatively compelling demonstration of the plug-and-play claim.

- **Progressive Prefix Conditioning with anchor alignment is a practical contribution**: The ablation (Fig. 7a) clearly shows the failure modes of Progressive Fusion (inconsistencies across windows) and naive prefix conditioning (color drift), and demonstrates that the proposed method resolves these. This is a non-trivial engineering contribution for long-video consistency in a ReferenceNet-free setting.

- **Two-stage training strategy is well-motivated and empirically effective**: The ablation (Fig. 7b) shows that training only the audio module fails to align motion, while single-stage training causes identity overfitting. The two-stage approach addresses a real optimization challenge and the ablation convincingly demonstrates its benefit.

- **Modular design enabling integration with the broader ecosystem**: The adapter can work with any personalized T2I model (demonstrated with realistic and Asian-style models), IP-Adapter-Face for identity, and text prompts — all without retraining the base model. This is a practical advantage over tightly-coupled ReferenceNet methods.

## Weaknesses

### Fatal
None.

### Major

1. **The "7× reduction in trainable parameters" claim is unsubstantiated**: The abstract states "reducing the number of trainable parameters by 7 times" and the claim appears nowhere else in the paper with supporting numbers. Table 1 shows total parameters (0.9B vs. 1.1–1.4B for baselines), which is at most a 1.5× difference. The 7× claim apparently refers to trainable parameters during fine-tuning, but no actual trainable parameter counts are reported for AnyExpress or the baselines. Without this, a core claimed advantage is unverifiable.

2. **Uncontrolled quantitative comparison**: The quantitative evaluation (Table 2) compares AnyExpress (trained on 300 hours of curated video including HDTF) against baselines used off-the-shelf with their original training data. The paper does not specify whether the HDTF evaluation uses a held-out test set, raising concerns about training/evaluation overlap for at least one dataset. The baselines were trained on different, likely smaller datasets. This confounds method improvement with data advantage and invalidates the headline numerical comparisons.

3. **No quantitative evaluation for 2 of 3 claimed capabilities**: The paper defines "Freeform Portrait Animation" with three capabilities — any face pose, any animated context, any text control. Only "any face pose" receives quantitative evaluation (Table 2). Animated contexts and text-based control are shown only qualitatively (Fig. 6a, 6b). There are no user studies, no CLIP scores for text alignment, no background consistency metrics. The claims about these capabilities remain assertions supported only by examples.

4. **ΔP (Pose Diversity Score) conflates motion quantity with quality**: The metric measures head motion intensity where "higher is better," but jittery, unnatural head motion would score equally well. While the paper also reports DOVER for overall quality, the diversity claim rests partly on a metric that cannot distinguish natural expressiveness from artifacts. This weakens the support for the "more diverse" face pose claim.

### Minor

1. **The entropy analysis (Fig. 3) lacks methodological precision**: The paper does not specify how attention entropy is computed — what distribution it is calculated over (spatial positions, heads, or both), or whether "entropy difference" refers to the difference between weak and strong control or across timesteps. The description ("By examining the entropy difference across attention heads") is too vague to be reproducible. This weakens the theoretical motivation. However, the qualitative observation (weak control enabling more diverse outputs) is separately validated by the experiments.

2. **CLIP-I is imprecisely described**: The paper claims CLIP-I measures "structural similarity to ensure consistent facial features" (Sec. 4.1). CLIP image similarity measures semantic/visual similarity, not structural similarity in the SSIM sense. While CLIP-I is a commonly used metric, the terminology is misleading. FaceID Consistency (using a face recognition model) is the appropriate identity metric and is already reported, so this is a presentation issue rather than a methodological one.

3. **The evaluation does not specify the HDTF test split**: The paper states evaluation was "performed on the HDTF, CelebV datasets" without clarifying whether a standard held-out test set was used. Given HDTF videos are also used in training, this ambiguity matters for reproducibility.

### Trivial
- The "Proposition 3.2" framing (Sec. 3.2) is unusual for an empirical observation rather than a formal theorem. This is a minor presentation choice.
- Some references to supplementary figures ("Fig. 10" in Sec. 4.4 ablation) refer to content that may be in the appendix.

## Nice-to-Haves

- A controlled experiment training baselines on a subset of the same 300-hour data (or training AnyExpress on only HDTF) would substantially strengthen the quantitative comparison.
- Reporting actual trainable parameter counts explicitly (e.g., "Audio-Motion Adapter has X M trainable params vs. Y M for ReferenceNet + full UNet fine-tuning") would substantiate the efficiency claim.
- A user study for naturalness and identity preservation would be more convincing than automatic metrics, especially for the animated context and text control capabilities.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"CLIP-I is a clear misuse and padding with an irrelevant number"** *(Harsh Critic, Critical Issues 1)*: CLIP-I is a standard metric in image/video generation literature for measuring visual-semantic similarity between generated and reference images. While calling it "structural similarity" is imprecise, calling it "padding" or a "clear misuse" overstates the problem. FaceID Consistency is the primary identity metric in the paper; CLIP-I is a secondary, commonly-used metric.
- **"Sync-C and Sync-D model/audio source not specified"** *(Harsh Critic, Critical Issues 1)*: The paper cites Chung & Zisserman, 2017 — the standard SyncNet paper. The audio source is the driving audio used for generation. This reflects a reviewer knowledge gap.
- **"No evidence linking higher attention entropy to better generation quality"** *(Harsh Critic, Critical Issues 3)*: The paper uses entropy as a mechanistic explanation for *why* weak control enables more diverse outputs, not as a quality metric. Quality is evaluated separately through standard metrics (Table 2). The claim that this is "pseudo-evidence" is a strawman.
- **"Comparison is fundamentally unfair because baselines weren't designed for this task"** *(Harsh Critic, Critical Issues 1, partially)*: The paper explicitly states the comparison focuses on "Any Face Pose, where pose control is directly relevant" (Sec. 4.1). Evaluating whether existing methods fail at a new capability the proposed method enables is a standard and legitimate comparison strategy. The *data* confound (different training data) is a valid issue, but the *task* confound is not.
- **"Proposition 3.2 is entirely unproven"** *(Harsh Critic, Critical Issues 3)*: The proposition is an empirical claim that is tested through the experiments in Sec. 4. The "proposition" framing is unusual but the content is evaluated.
- **Strength Finder: "Comprehensive quantitative evaluation on multiple metrics across diverse conditions"**: This conflicts with the verified weakness that 2 of 3 claimed capabilities lack quantitative evaluation and the comparison is uncontrolled. Removed per instructions.
- **Strength Finder: "Dramatic reduction in trainable parameters: 7 times"**: This conflicts with the verified weakness that the 7× claim is unsubstantiated with concrete numbers. Removed per instructions.
- **Strength Finder summary paragraph** (overstates the conclusiveness of Table 2 given the uncontrolled comparison issues).

## Novel Insights

The reviews surface an interesting tension: the paper's core technical contribution is genuinely novel (removing ReferenceNet and using weak control for greater flexibility), but the evaluation framework designed to validate this contribution undermines itself by conflating multiple uncontrolled variables. The "less is more" argument (weaker control → greater generative freedom) is intuitively appealing and supported by the qualitative results, but the quantitative evidence is compromised by comparing against off-the-shelf baselines trained on different data for a task the paper itself defines. This suggests the community needs standardized evaluation protocols for "freeform" portrait animation tasks — perhaps building on existing benchmarks but with explicit pose-diversity metrics and controlled training conditions — before claims about surpassing ReferenceNet methods can be rigorously settled.

## Suggestions

1. **Substantiate the efficiency claim**: Report the exact number of trainable parameters for the Audio-Motion Adapter and the corresponding counts for full-UNet + ReferenceNet training in the baselines. A simple table with "Total Parameters" and "Trainable Parameters (for fine-tuning)" for each method would resolve this.
2. **Run a controlled experiment**: Either train AnyExpress on only the HDTF training set (42.58 hours) to match baseline data scale, or fine-tune baselines on the same 300-hour data. This would separate architectural advantage from data advantage.
3. **Provide quantitative evidence for animated contexts and text control**: At minimum, report CLIP-T score for text alignment and background motion diversity metrics. A user study (even small-scale) would strongly support the naturalness claim.
4. **Clarify the HDTF evaluation split**: Explicitly state whether the standard held-out test set was used or specify the split criteria.
5. **Add a failure case analysis**: Show cases where weak control causes identity drift or lip-sync degradation. This would strengthen credibility and help users understand limitations.
6. **Define the entropy computation precisely**: Provide the formula for attention entropy (e.g., \( H = -\sum p_i \log p_i \) over which dimension) in the main text or appendix.

## Score and Decision

This paper presents a well-motivated and architecturally clean solution to a real problem in audio-driven portrait animation. The qualitative results are impressive and demonstrate genuinely new capabilities (animated backgrounds, text-driven control, diverse poses from a single reference). The Progressive Prefix Conditioning and two-stage training are practical contributions validated by ablation.

However, the paper has significant gaps in experimental rigor: the headline "7×" parameter reduction is unsupported by concrete numbers, the quantitative comparison confounds method with data, and two of three claimed capabilities lack any quantitative evaluation. These issues are addressable but non-trivial.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>