---
job_id: f44a80c1-3797-443a-9f21-0bace955b385
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ppXAVexrAM.pdf
paper: ARSS: Taming Decoder-Only Autoregressive Visual Generation for View Synthesis From Single View
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies autoregressive generative modeling and representation learning for camera-conditioned novel view synthesis.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including abstract, introduction, related work, method, experiments, results, and discussion, and it presents a concrete method with nontrivial empirical evaluation. There are important weaknesses in formulation, clarity, and experimental support, but they do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other obvious manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes ARSS, a decoder-only autoregressive framework for novel view synthesis from a single image and a predefined camera trajectory. The method combines a causal video tokenizer, a camera autoencoder that converts Plücker raymaps into camera tokens used as 3D positional guidance, and a hybrid token-ordering strategy that randomly permutes tokens spatially while preserving temporal order. Experiments on RealEstate10K, ACID, and zero-shot DL3DV compare ARSS against diffusion-based and transformer-based baselines, with additional ablations on token permutation and tokenization strategy.

## Strengths
The paper explores an interesting direction, namely bringing decoder-only autoregressive modeling into camera-controlled novel view synthesis. That framing is meaningful, because the motivation around causal rollout and trajectory extension is reasonable for world-model-style settings, and the paper does articulate why a token-by-token model could be attractive compared with jointly denoising all views.

The system design is fairly coherent at a high level. The three modules, video tokenizer, camera-token conditioning, and temporally causal but spatially shuffled autoregressive decoding, fit together in a way that matches the stated goal. In particular, **Figure 2** is helpful in conveying the intended pipeline: it makes clear that the first view is treated as condition tokens, that camera tokens are interleaved with visual tokens, and that the transformer is trained on the ground-truth tokenized sequence. For a paper with several moving parts, this figure does useful explanatory work.

The use of a video tokenizer rather than per-frame image tokenization is a sensible design choice for sequence generation. The paper at least attempts to justify this empirically. In **Table 3**, replacing image VQ tokenization with the proposed video-tokenizer setup yields a large gain across PSNR/SSIM/LPIPS/FVD, especially the drop from 137.68 to 52.56 in FVD. Even if some details are missing, this table does support the narrower claim that temporally aware tokenization matters in this pipeline.

The ablation on token order is also directionally useful. **Table 2** and **Figure 7** together suggest that preserving temporal order while randomizing spatial order is better than either raster order or fully shuffled spatiotemporal order. That is a relevant result for the core architectural claim, not just an auxiliary tweak.

The qualitative results are reasonably broad. **Figures 3 and 4** include indoor, outdoor, and aerial examples, and the visual comparisons do suggest that ARSS can sometimes avoid the gross pose failures visible in some baselines while producing sharper results than the feed-forward transformer baseline. The zero-shot examples in **Figure 5** also indicate that the method is not totally brittle to synthetic or stylized inputs.

## Weaknesses
1. **The central novelty claim is overstated, and the paper does not position itself carefully enough against prior sequential/causal single-image view synthesis and transformer-based NVS.**  
   The paper repeatedly claims or strongly implies first-of-its-kind status, for example on **Page 2** and **Page 3** (“ARSS is the first...”, “To the best of our knowledge...”). That is a high bar, and the current related-work discussion is too narrow to support it. The paper discusses diffusion-based NVS, image AR generation, and video tokenization, but it does not adequately situate itself relative to earlier transformer-based single-image NVS or prior sequential long-horizon view/video generation from a single image. This matters because the claimed contribution is not merely “we got better numbers,” it is “we are opening a new formulation.” If the positioning is incomplete, the paper’s contribution looks more like a combination of existing ingredients, video tokenizer + camera encoder + random-order AR decoding, rather than a clearly differentiated conceptual advance.

2. **The mathematical specification of the core sequence construction is inconsistent and in places plainly broken.**  
   The most serious issue is in **Equation 6** on **Page 6**. The displayed sequence appears to list only \(\pi\) tokens, with repeated camera tokens and no visible \(x\) visual tokens in several places, even though the text says the sequence is interleaved camera and visual tokens. There are also repeated subscripts such as \(\pi_{11}^{P_1(1)}, \pi_{11}^{P_1(1)}\) and \(\pi_{2n}^{P_2(n)}, \pi_{2n}^{P_2(n)}\), which looks like either a typo or a deeper indexing confusion. If the intended sequence is something like
   \[
   \mathcal{S} = [\pi_{11}^{P_1(1)}, x_{11}^{P_1(1)}, \ldots, \pi_{ln}^{P_l(n)}, x_{ln}^{P_l(n)}],
   \]
   then the current equation should say that explicitly. As written, **Equation 6** does not define the actual transformer input sequence correctly, which is a major problem because the whole method hinges on that order.

3. **The training objective is underspecified to the point that reproduction is difficult, and the equations do not cleanly match the verbal description.**  
   **Equation 7** on **Page 6** is incomplete or malformed:
   \[
   \mathcal{L}=CE(f_{\theta}([\mathcal{S},[x_{21}^{P_{2}(1)},...,x_{ln}^{P_{l}(n)}]),
   \]
   It appears truncated, does not close properly, and never clearly states the prediction targets versus the shifted input sequence. In an autoregressive paper, this is not a cosmetic issue. The reader needs the exact training sequence, target sequence, whether camera tokens are predicted or only consumed as conditioning, whether the loss is applied only on visual-token positions, and whether the first frame’s visual tokens are excluded from prediction. A clean formulation would look more like
   \[
   \mathcal{L}
   = \sum_{t \in \mathcal{I}_{\text{visual target}}}
   CE\!\left(f_\theta(s_{<t}), x_t\right),
   \]
   with \(s_t\) explicitly defined as interleaved camera and visual tokens. Without that, the paper leaves too much implicit.

4. **Equation 8 is also ambiguous and does not rigorously define the conditional factorization.**  
   The notation
   \[
   p(x_{ij}^{P_i(j)}|\pi_{\le i,\le j}^{P_{\le i}(\le j)},x_{<i,<j}^{P_{<i}(<j)},[\pi_{11}^{P_1(1)},x_{11}^{P_1(1)},...])
   \]
   mixes sequence order, frame order, and permuted within-frame order in a way that is not mathematically well defined. For example, \(x_{<i,<j}\) is not meaningful once tokens are spatially permuted within each frame, because there is no natural two-dimensional partial order that corresponds to the actual one-dimensional decoding order. The paper should define a single flattened permutation index \(t\), or define \(P_i\) precisely and then use the rank induced by \(P_i\). Right now, the notation suggests more rigor than is actually present.

5. **The camera-token component is interesting, but its role is under-validated.**  
   The camera autoencoder is central to the paper’s story, yet there is no direct ablation removing camera tokens, replacing learned camera tokens with simpler positional/camera embeddings, or comparing against raw pose conditioning. The paper shows in **Figure 2** that camera tokens are inserted before visual tokens as “3D positional instruction,” but there is no experimental evidence isolating how much of the final performance actually comes from this choice. This is a significant omission because the paper argues that ordinary class-token conditioning is insufficient and that camera-aligned token-wise guidance is necessary. Without such ablations, that claim remains speculative.

6. **The quantitative results are mixed, and the paper’s verbal framing overstates them.**  
   The abstract says the method is “overall comparable to state-of-the-art,” but **Page 3** later says the method “out-performs current state-of-the-art methods.” **Table 1** supports the weaker statement, not the stronger one. On RealEstate10K and ACID, ARSS gets the best PSNR and LPIPS, but it is clearly worse than SEVA on SSIM and much worse on FID for ACID, 47.76 versus 33.16. On RealEstate10K the FID is also slightly worse than SEVA, 47.60 versus 46.98. So the picture is mixed, not dominant. This matters because the contribution case for a new AR paradigm depends on either clear empirical advantages or strong systems advantages such as causality/efficiency/reusability. The paper demonstrates neither convincingly enough.

7. **The baseline set is not fully convincing for the paper’s claims, and some comparisons feel uneven.**  
   The paper positions itself against diffusion-based NVS, feed-forward transformer NVS, and some generic video generation baselines, but the selection is not fully aligned with the claimed setting of single-image novel view synthesis with trajectory control. Some methods listed are more generic motion/video-control systems rather than the strongest camera-aware single-image NVS comparators for this exact problem. In addition, for several baselines the paper does not report zero-shot DL3DV results because of training overlap, which is fair, but it makes the headline zero-shot table less informative as a state-of-the-art comparison. The consequence is that the experimental section does not quite settle whether ARSS is genuinely competitive with the best alternatives in its most natural problem setting.

8. **The paper makes strong claims about autoregressive advantages, but provides almost no evidence on the key practical dimension of efficiency or controllable rollout.**  
   A major motivation on **Pages 1–2** is that AR models are better suited to strict causality, incremental extension, and reuse when the trajectory changes. Yet the experiments never measure inference time, memory, scaling with trajectory length, or any actual reuse scenario. This is a missed opportunity. If the method is not clearly better on standard image/video quality metrics than diffusion baselines, then the practical case for adoption should come from causal rollout benefits. Right now that argument is mostly rhetorical.

9. **The long-horizon error accumulation analysis is suggestive but not yet fully convincing.**  
   **Figure 6** is one of the more important figures in the paper because it supports the claim that ARSS accumulates less error over time. The trend lines do look favorable. However, the figure lacks uncertainty bands, sample counts, and enough setup detail to judge whether differences are statistically stable or dominated by a subset of scenes. Also, the paper states that ARSS has the “lowest LPIPS at every timestep” and “consistently highest or near-highest PSNR/SSIM,” but this is a strong summary from a small visual plot. Since this is one of the few places the paper directly addresses the long-horizon causal-generation motivation, the evidence should be stronger.

10. **Some qualitative evidence cuts both ways.**  
    The paper claims in **Figure 3** that ARSS generates “geometrically consistent and sharp views,” but even in the provided examples there are still visible softness and structural instability in some regions, especially around fine boundaries and repeated textures. **Figure 4** is more favorable, but it still shows only a limited set of selected examples. Since AR generation can suffer compounding errors, I would have liked more failure cases or denser trajectory visualizations. The qualitative section currently reads a bit too much like a curated best-case gallery.

11. **Presentation quality is below the standard expected for a paper whose main contribution is architectural/methodological.**  
    There are many language and notation issues: duplicated symbols in **Equation 5** where \(\bm d\) is defined twice, once as ray direction and then the text says “\(\bm d\) is the momentum term” though it should be \(\bm m\); malformed equations; repeated typos such as “purpose” instead of “propose,” “temporary” instead of “temporally,” “desnoising,” “perpetual loss” instead of “perceptual loss,” and inconsistent naming of datasets and methods. These are not fatal individually, but collectively they reduce trust in the precision of the technical presentation.

12. **The paper relies heavily on a strong external tokenizer backbone, but does not clarify how much of the gains come from that choice versus the proposed AR formulation.**  
    **Table 3** shows that the tokenizer matters enormously, which is useful, but it also weakens the attribution of performance gains to the main proposed method. If the largest quality jump comes from switching to VidTok-style causal video tokenization, then the paper needs stronger evidence that the decoder-only AR structure itself is doing more than riding on a high-quality representation. An ablation comparing a simpler conditional decoder on the same tokens, or an AR model without the proposed permutation/camera-token choices, would help separate these effects.

## Questions
1. Please provide a corrected and fully specified version of **Equations 6–8**. In particular, what is the exact flattened token sequence fed into the transformer, which positions are camera tokens versus visual tokens, and on which positions is cross-entropy applied? A precise formulation could substantially increase my confidence.

2. Can you add an ablation isolating the contribution of the camera tokens? For example, compare:  
   (a) no camera conditioning,  
   (b) global camera embedding only,  
   (c) simple per-token pose embedding,  
   (d) the proposed camera autoencoder tokens.  
   This would directly test the paper’s main argument that token-aligned 3D positional guidance is needed.

3. Since one of the main motivations is causal rollout and reuse along trajectories, can you report actual runtime and memory comparisons against representative diffusion baselines, ideally as a function of the number of generated frames? Without that, the practical advantage of the AR formulation remains under-supported.

4. For **Figure 6**, please clarify how the per-frame curves were computed: over how many scenes, with what trajectory length distribution, and whether confidence intervals can be added. If the trend is robust, stronger statistical reporting would materially strengthen the paper.

5. Can you better justify the baseline selection for single-image camera-controlled NVS, and explain whether stronger or more directly matched non-diffusion baselines were considered? This is important for assessing whether the comparison in **Table 1** really supports the claimed competitiveness.

6. Please clarify the first-frame handling in the tokenizer and training objective. On **Pages 4–5** the first frame is said to be independent and not temporally compressed, and also used as the conditional prefix. Are those visual tokens ever predicted during training, or are they always treated as observed context only?

7. The manuscript would benefit from a more restrained framing of the results in **Table 1**. If the authors can clearly articulate where ARSS is better, where it is worse, and why that tradeoff is worthwhile, that would improve the paper’s credibility.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are raised by the paper as presented. The work studies a standard generative vision task and does not appear to introduce new datasets, human-subject protocols, or especially sensitive deployment claims in the main paper.

## Soundness Rating
2: fair. The high-level idea is plausible and the experiments are nontrivial, but the core mathematical specification is incomplete/inconsistent, several central claims are under-ablated, and the evidence only partially supports the strongest claims.

## Presentation Rating
2: fair. The overall structure is understandable and some figures are useful, especially Figure 2, but the paper has substantial notation problems, malformed equations, and enough writing issues to hinder careful technical assessment.

## Contribution Rating
2: fair. There is a potentially interesting contribution in adapting decoder-only autoregressive generation to camera-controlled view synthesis, but the current positioning, empirical support, and method isolation do not yet establish a sufficiently strong contribution for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper has a real idea and some promising evidence, especially around using AR decoding for causal view rollout and the tokenizer/permutation ablations. However, the current submission falls short because the core formulation is not presented rigorously enough, the camera-token contribution is not isolated, and the experiments do not fully validate the practical advantages that motivate the method. With a cleaner mathematical specification, stronger ablations, and better support for the causality/efficiency claims, I could see this moving upward.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the main equations, tables, and figures, and the main reasons for my score are concrete issues in formulation and experimental support rather than vague lack-of-interest concerns.