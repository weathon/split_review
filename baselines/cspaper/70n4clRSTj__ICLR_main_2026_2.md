---
job_id: 7729d409-4676-4ddb-beec-3faedced8083
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 70n4clRSTj.pdf
paper: Time Blindness: Why Video-Language Models Can’t See What Humans Can?
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as a benchmark and empirical study for video-language models, representation learning, and temporal reasoning in multimodal ML.

## Minimum Quality
Pass ✅. The submission contains the expected components for a benchmark paper, including abstract, introduction, related work, dataset/method description, experiments, quantitative results, and conclusion; while there are significant scientific weaknesses, they do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeted instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper introduces SpookyBench, a synthetic benchmark intended to isolate purely temporal understanding in video-language models by encoding content in motion patterns over noise-like frames, so that individual frames appear uninformative while humans can recover text, objects, or dynamic scenes from the temporal sequence. The authors evaluate a broad set of open and closed source video-language models and report a stark gap, namely near-perfect human accuracy versus 0% accuracy for all tested models, and argue that current architectures are strongly biased toward frame-level spatial processing.

## Strengths
The main strength is the clarity of the benchmark motivation. The paper is asking a focused and useful diagnostic question, namely whether current Video-VLMs can extract meaning when the signal lives almost entirely in temporal change rather than static appearance. That question is important, and the submission succeeds at making the failure mode easy to understand.

The empirical headline result is striking and easy to interpret. **Table 1** shows an unusually clean pattern across a wide range of model families and scales, from small open models to large commercial ones, with both direct prompting and CoT still yielding 0%. Even if one is skeptical about the breadth of the paper’s conclusions, the benchmark clearly identifies a regime in which current systems fail badly.

I also appreciated that the paper includes a human baseline rather than only model numbers. **Table 3** is valuable because it confirms that the task is not simply impossible or under-specified. The high human accuracy and perceptibility scores make the central point much more convincing than model-only failure would.

The benchmark construction is conceptually simple, which is actually a virtue for a diagnostic dataset. **Figure 2** does a good job illustrating the foreground/background opposing-motion idea and why the content is visible only during animation. Similarly, **Figure 3** is useful for showing the three categories of encoded content and gives the reader a concrete sense of what the benchmark instances represent.

The paper also makes some effort to probe alternative explanations. The FPS experiment in **Table 4** and **Table 5** is a reasonable sanity check against the claim that model failure is merely due to temporal downsampling. The fine-tuning experiment in Section 4.4 is another useful stress test, at least directionally.

Finally, the work is reproducibility-oriented in spirit. The generation process is simple enough that, if the promised release is complete, the community should be able to reproduce and extend this benchmark fairly easily.

## Weaknesses
1. **The paper overstates the scope of its conclusions relative to what the benchmark actually tests.**  
   The central rhetorical claim is that current models are fundamentally “time-blind” and “can’t see what humans can” (title, Abstract, Introduction, and Conclusion). But the actual benchmark in **Section 3** studies a very specific psychophysics-style regime: content revealed by coherent motion segregation in binary noise with highly synthetic rendering rules. Failing on this family of stimuli does show a serious blind spot, but it does not by itself justify the broader claim that current Video-VLMs cannot process temporal information in general. Many temporal tasks involve tracking, ordering, causality, event segmentation, or state transitions in natural videos, which are not equivalent to recovering a hidden shape from motion-defined noise. This matters because the paper repeatedly moves from “models fail on this benchmark” to “current architectures remain fundamentally time-blind” without enough evidential bridge. A better framing would be that SpookyBench exposes a specific and important missing capability, namely motion-based figure-ground segregation and temporal decoding under absent static cues.

2. **The benchmark is narrow, heavily synthetic, and not yet sufficient to support strong general claims about video understanding.**  
   The dataset has only **451 videos** in total, per **Section 3.3**, with a particularly small Dynamic Scenes subset of **57 videos**. That is modest for a benchmark paper aiming to make architectural claims about the field. The content generation process is highly stylized, with fixed binary noise, limited motion patterns, narrow speckle sizes, and a small set of encoding mechanisms from **Algorithms 1 and 2**. Because of this, the benchmark may be more diagnostic of one specific perceptual computation than of temporal reasoning broadly construed. The “essentially unlimited” argument on **Page 5** is not enough; what matters scientifically is the demonstrated diversity, difficulty control, and coverage of the released benchmark used in the paper. Right now, the paper would be stronger if it more carefully positioned SpookyBench as a stress test rather than as the first decisive benchmark of “pure temporal understanding.”

3. **Several experimental choices make the reported 0% results less informative than they initially appear.**  
   The paper reports exact-match accuracy with short text outputs in **Section 4.1**, and for objects/scenes allows a set of acceptable labels. However, the evaluation protocol remains under-specified in important ways. For example:
   - How were acceptable label sets \(Y_i\) constructed, and by whom?
   - Were responses normalized for case, plurality, punctuation, articles, or close synonyms beyond the listed examples?
   - How were multi-word outputs handled when the model described uncertainty or partial content?
   - For video models that “do not directly support video input,” what exact frame selection and ordering were used?
   
   When every model scores exactly 0%, even small evaluation mismatches can matter. This is especially important because the paper interprets 0% as categorical failure rather than extreme weakness. Without a more exhaustive description of decoding settings, frame budgets, temperatures, retries, response normalization, and API details, it is difficult to know whether all models were evaluated under comparably favorable conditions.

4. **The paper does not include even a minimal non-VLM computational baseline for the benchmark, which is a major omission for a benchmark paper.**  
   This is probably my biggest scientific concern. The paper argues that humans exploit temporal coherence and motion contrast, and then defines explicit metrics based on optical flow and motion boundaries in **Equations (1) to (4)**. The appendix also shows recovered masks and motion-boundary visualizations in **Figures 9, 10, and 11**. But the paper never tests a simple algorithmic baseline built from the same ingredients, such as:
   - optical flow + temporal averaging + contour extraction,
   - motion segmentation + OCR for text,
   - a 3D CNN or a small supervised classifier trained directly on the rendered sequences,
   - a handcrafted decoder matched to Algorithms 1 and 2.
   
   Without such baselines, it is hard to tell whether SpookyBench measures “temporal understanding” in a rich sense or whether it simply requires a low-level motion-segmentation operation missing from current VLM front ends. If a simple computer-vision pipeline solves a large fraction of the benchmark, the paper’s interpretation shifts considerably, from “models lack temporal reasoning” to “current VLM pipelines ignore a solvable low-level cue.” That distinction matters a lot.

5. **The fine-tuning evidence in Section 4.4 is too thin to support the architectural conclusion.**  
   The paper fine-tunes two models on 400 videos for 10 epochs and still reports 0%, then concludes this indicates a “fundamental architectural inability.” That is much too strong given the evidence presented. We are missing basic details: train/test split protocol, validation set, prompt templates used during training and testing, learning rate, batch size, number of trainable parameters, whether visual encoders were frozen, how video inputs were represented, and whether the token budget was sufficient for the full temporal signal. With only 451 total videos, there is also a serious risk that the fine-tuning setup is simply too data-poor and too brittle to meaningfully test learnability. A failed fine-tuning run is not the same as evidence of impossibility.

6. **The mathematical definitions of the SNR metrics are not rigorous enough, and some of the interpretations are shaky.**  
   The discussion in **Section 3.3.1** introduces four metrics in **Equations (1) to (4)**, but several quantities are ambiguous or insufficiently justified.
   - In **Equation (1)**, \(P_S = \mathbb{E}[\|\nabla \mathbf{F}\|^2]\) is called “motion boundary energy,” while \(P_N = \mathrm{Var}(I_0)\) is variance of a static frame. These are heterogeneous quantities with different semantics, and the rationale for taking their ratio as a standard SNR is not well established.
   - In **Equation (2)**, the objects \(B\) and \(N\) are not defined with enough precision to make the Fourier-domain operation reproducible. If \(B\) is “average motion boundary strength” and \(N\) is a static noise frame, then the numerator and denominator again live in rather different representational spaces.
   - In **Equation (3)**, \(C = e^{-\mathrm{Var}_\theta(\mathbf{F})}\cdot \mathbb{1}(\|\mathbf{F}\|>\tau)\) depends critically on the threshold \(\tau\), but \(\tau\) is never specified in the main paper. Since the benchmark’s conclusions partly rely on “high temporal coherence,” omission of \(\tau\) is not minor.
   - In **Equation (4)**, the mask \(M\) is “estimated from the motion boundaries,” yet the quality and procedure of this estimation are not described. This makes the reported motion contrast somewhat circular, because the same temporal structure is being used both to derive the mask and to evaluate the signal.
   
   More broadly, calling these quantities “SNR” may be rhetorically appealing, but it risks overstating their physical or statistical meaning. They look more like heuristic perceptual diagnostics than true signal-to-noise ratios. That is fine, but then the paper should say so more carefully.

7. **Some claims around the SNR analysis are internally inconsistent or at least poorly explained.**  
   On **Page 6**, the paper states that “text stimuli benefit from higher basic SNR ... explaining the observed performance gap,” but in the main results no model performs better on text than on anything else, since everything is 0%. So what exactly is the “observed performance gap” being explained there, human-vs-human category differences, human-vs-model differences, or text-vs-dynamic scenes? The argument is muddled. Similarly, **Figure 4** is presented as “analysis of effects of SNR on detecting words,” and the text says prompts performed best at 40% accuracy and that accuracy jumps to 85.7% above a threshold. This appears inconsistent with **Table 1**, where all model prompt settings are 0%. If **Figure 4** corresponds to human detection rather than model detection, that needs to be stated unambiguously in the main text. As written, this section is confusing and undercuts confidence in the presentation.

8. **The human evaluation is useful but scientifically light, and some details are missing for a strong human-vs-model claim.**  
   The paper uses only **six participants** in **Section 4.2**, all evaluating the full dataset. For a benchmark whose headline is a human-machine performance gap, that is a rather small and homogeneous sample. There is no discussion of participant demographics, visual acuity correction, display conditions, viewing distance, device consistency, or order/randomization effects. The perceptibility scores in **Table 3** are interesting, but there is no inter-rater agreement analysis and no uncertainty decomposition beyond mean ± std. This does not invalidate the result, but the human study is being asked to carry a lot of argumentative weight, and right now it is more a sanity check than a rigorous psychophysical experiment.

9. **The presentation has several quality-control issues, some of which interfere with interpretation.**  
   There are repeated reference/citation problems, visible formatting errors, and a few contradictory statements. Examples include the highly corrupted references on **Page 11**, inconsistent naming such as “Spooky-Bench” vs “SpookyBench” in **Table 2**, and awkward or incomplete prose in multiple places. The FPS experiment description is also inconsistent: **Page 8** says 120 videos, while the appendix on **Page 19** says 60 randomly sampled videos. That is not a cosmetic issue, because it directly affects the credibility of **Table 4** and **Table 5**. For a benchmark paper, details are the product. Right now, the paper needs a more careful pass.

10. **Figure usage is mixed, and one figure in particular exposes a gap between claim and evidence.**  
   **Figure 2** is genuinely helpful, because it concretely explains the core construction and makes the temporal-only nature of the stimulus intuitive. In contrast, **Figure 1** is more of a conceptual cartoon than evidence. It visually asserts a “coherence gap” between spatial and temporal features, but no experiment in the paper actually measures internal feature allocation or representation strength in those terms. Since the figure appears very early and anchors the main claim, it risks overselling what is empirically established. The appendix figures, especially **Figures 9 to 11**, are more scientifically useful because they show that motion-boundary computations can recover structure from the stimuli. But that usefulness also highlights the missing baseline issue discussed above.

11. **The benchmark positioning relative to prior temporal benchmarks is not sharp enough.**  
   The paper cites many temporal-reasoning datasets in **Section 2**, which is good, but the comparison remains mostly verbal. The paper says existing datasets allow spatial shortcuts and SpookyBench removes them entirely. That may be true, but the submission would be much stronger with a direct taxonomy: what exact temporal capability does SpookyBench isolate that TemporalBench, TVBench, VITATECS, VidHalluc, or SVBench do not? Right now the narrative is plausible, but still somewhat slogan-like. This matters because the paper’s originality lives primarily in benchmark design and problem formulation, not in a new algorithm.

## Questions
1. The biggest thing that would increase my confidence is a set of simple non-VLM computational baselines. Can the authors evaluate at least one motion-based decoder, for example optical flow + motion segmentation + OCR/classification, or a small 3D CNN trained directly on the rendered videos? If such baselines also fail, the claim of a genuinely hard temporal benchmark becomes stronger. If they succeed, the paper should revise its interpretation accordingly.

2. Please clarify the exact evaluation protocol in **Section 4.1**. How were acceptable labels \(Y_i\) constructed, how were outputs normalized, and what exact decoding / inference settings were used for each closed and open model? If there were any retries, temperature changes, frame count adjustments, or API-specific preprocessing, please specify them.

3. For models that do not support video input directly, what exact frame sampling strategy was used? Since the benchmark depends critically on temporal continuity, details such as number of frames, ordering, spacing, and whether repeated or uniformly sampled frames were sent matter a lot.

4. The fine-tuning claim in **Section 4.4** is currently too strong for the amount of detail provided. Please report the train/validation/test split, parameter-efficient vs full fine-tuning settings, frozen modules, learning rates, batch sizes, token/frame budgets, and whether the full temporal sequence was available during training and testing. I would also like to know whether training loss decreased at all.

5. Please clarify the inconsistency between **Page 8** and **Appendix D, Page 19** regarding whether the FPS study used 120 or 60 sampled videos. This needs to be corrected.

6. Please clarify **Figure 4** and the surrounding text on **Page 6**. Whose accuracy is being plotted there, humans or models? How does this relate to the 0% model accuracy in **Table 1**? As written, this section is confusing.

7. For **Equations (1) to (4)**, please specify all omitted hyperparameters and implementation choices, especially \(\tau\) in **Equation (3)**, the estimation procedure for \(M\) in **Equation (4)**, and the exact definitions of \(B\) and \(N\) in **Equation (2)**. I would also encourage the authors to rename these as perceptual diagnostics rather than formal SNRs unless there is a stronger justification.

8. Can the authors provide category-wise model outputs or confusion examples? Since **Table 1** compresses everything to 0%, seeing representative failure cases would help distinguish “random guessing,” “frame-based hallucination,” and “partial temporal sensitivity.”

9. The human study is helpful, but can the authors comment on display conditions and participant instructions in more detail? Given the visual nature of the stimuli, basic psychophysical controls matter.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The work appears to use synthetic data and a small voluntary human study with anonymized responses and stated consent. Based on the paper text, I do not see a substantive ethics issue that requires separate ethics review.

## Soundness Rating
2: fair. The benchmark idea is coherent and the central empirical observation is plausible, but several important methodological details are missing, the fine-tuning evidence is too weak for the architectural conclusion, and the paper lacks key computational baselines.

## Presentation Rating
2: fair. The core idea is understandable and some figures are effective, especially **Figure 2**, but the paper has notable clarity issues, inconsistencies across sections, and reference/formatting problems that interfere with careful assessment.

## Contribution Rating
2: fair. The paper identifies an interesting failure mode and the benchmark could be useful as a diagnostic tool, but the novelty is mostly in a narrow synthetic stress test, and the current evidence does not yet justify the broader conclusions claimed.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper exposes a sharp and interesting failure mode, and I do think the benchmark is worth discussing. However, the current version overclaims, lacks crucial non-VLM baselines, provides too-thin evidence for its architectural conclusions, and has enough presentation/methodological gaps that I do not think it clears the ICLR bar in its present form.

## Reviewer Confidence
4: confident. I am confident in the assessment and carefully checked the main empirical claims, tables, figures, and mathematical definitions, though some implementation details are missing from the paper and limit complete verification.