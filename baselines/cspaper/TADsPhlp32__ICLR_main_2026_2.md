---
job_id: 2a5f4657-7780-420f-8bf0-1529bcc85343
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: TADsPhlp32.pdf
paper: Structural Semantic Features for Improved AI-Generated Fake Image Detection
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within representation learning / computer vision for AI-generated image detection, which fits ICLR’s scope on learned representations and ML applications in vision.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments, results, and conclusion, and it presents a coherent empirical study, even though there are notable concerns about novelty, methodological detail, and evaluation rigor that affect the recommendation rather than triggering desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes adding a structural feature stream to the AIDE fake-image detector. The added features are derived from a recursive cuboidal partitioning procedure that greedily splits an image to maximize reduction in within-segment sum of squared errors, then encodes the cumulative sequence of split gains and concatenates it with AIDE’s existing patchwise and semantic features. Empirically, the paper reports improved mean accuracy over AIDE on GenImage, competitive but mostly weaker performance on AIGCDetect, and second-best performance on Chameleon.

## Strengths
The main practical strength is that the method is simple and modular. As shown in **Figure 2** on Page 4, the proposed branch is attached to a frozen AIDE backbone and only adds a structural feature extractor plus a small projection layer before the final MLP head. This makes the idea easy to understand and potentially easy to retrofit into an existing detector without full end-to-end retraining.

The paper addresses a real weakness of many AIGC detectors, namely the tension between low-level forensic cues and high-level semantics. The authors try to inject a third source of information, structural organization, and that design choice is at least conceptually well motivated by the examples discussed in the introduction and qualitative section.

The empirical results on **Table 1** (GenImage, Page 7) are genuinely strong relative to the reported baselines. The gain over AIDE in mean accuracy, from 86.88 to 89.56, is not tiny, and the improvements are spread across several generators, especially **GLIDE** (+3.36), **VQDM** (+4.83), and **BigGAN** (+6.75). Even if one debates whether this constitutes a major advance, it does suggest that the added feature branch captures some useful signal beyond AIDE’s existing features.

I also appreciated that the paper does not pretend the method helps everywhere. The discussion in Section 4.8 acknowledges that the extra feature stream can degrade performance on some subsets, which is more honest than the usual “wins on everything” narrative.

The qualitative examples in **Figure 1** and **Figure 3** are useful for intuition. **Figure 1** gives a concrete failure case of AIDE and suggests that the partitioning can isolate suspicious local regions around facial structure. **Figure 3** further shows multiple examples where prediction confidence flips from incorrect to correct. These figures do not prove the mechanism, but they at least make the intended use case visually understandable.

## Weaknesses
1. **The technical contribution feels narrow and closer to feature grafting than a substantial methodological advance.**  
   At a high level, the paper takes an existing detector, **AIDE**, keeps its backbone frozen, computes a hand-designed structural descriptor via recursive SSE-based partitioning, projects it with one FC layer, and concatenates it before classification, see **Section 3.3** and **Figure 2**. That is a reasonable engineering modification, but the paper overstates it as a major new detection framework. The core algorithmic ingredient, cuboidal partitioning, is explicitly borrowed from prior work in image analysis, and the integration strategy is simply concatenation plus retraining the classifier head. For ICLR main track, that raises the bar on either deeper analysis, stronger evidence that this specific structural signal is fundamentally new for the task, or more convincing mechanistic understanding. As written, the work reads as “AIDE + one additional handcrafted feature family.”

2. **The method description is underspecified in important ways, especially around the actual feature construction and computational procedure.**  
   This is not a cosmetic issue, because the entire paper hinges on the structural vector defined in **Equations (1), (2), and (3)** on Pages 4 to 5. Several details are missing:
   - The paper says \(p_i\) is the pixel feature vector, “e.g., RGB values” in **Equation (1)**, which implies the exact feature representation is not fixed. Is the method using raw RGB, another color space, CLIP features, or something else? This directly affects the computed SSE and therefore the partition tree.
   - The paper says the algorithm finds the “optimal axis-parallel cut” maximizing gain in **Section 3.2**, but does not specify the search space. Is every pixel row/column considered as a candidate split? Are there minimum segment size constraints? How are ties broken?
   - The phrase “always selecting the sub-segment that offers the greatest potential gain for the next split” is too vague. Potential gain according to which candidate cut, recomputed globally over all current leaves, or based on stale values from previous iterations?
   - The paper sets \(N=1024\), but does not clarify what happens when the image resolution or stopping criteria make this impossible or unstable, or whether all images are resized to a common size before partitioning.
   
   These omissions matter because they prevent exact reproduction from the main paper and also make it hard to judge whether the improvements come from a robust structural descriptor or from implementation choices hidden behind the summary.

3. **The mathematics are intuitive but not carefully formulated, and the notation in Equation (3) is sloppy enough to create ambiguity.**  
   In **Equation (3)** on Page 5, the paper defines
   \[
   \hat g_i = \frac{1}{e_I}\sum_{j=1}^{i}\hat g_j, \quad 1 \le i \le N.
   \]
   This is mathematically awkward because \(\hat g_i\) is used both as the ordered gain at split \(i\) and as the normalized cumulative feature at index \(i\). The notation overload is avoidable and should be fixed. For example, if the ordered raw gains are \(g^{\downarrow}_j\), then the cumulative normalized feature should be something like
   \[
   f_i = \frac{1}{e_I}\sum_{j=1}^{i} g^{\downarrow}_j.
   \]
   Relatedly, the paper never proves or even states basic properties of this feature. Since \(g = e_S - (e_{S_1}+e_{S_2})\), one expects \(g \ge 0\) for mean-based SSE partitioning, and cumulative sums normalized by \(e_I\) should satisfy \(0 \le f_i \le 1\) if the tree is well-defined. Those properties would help readers understand what the feature encodes and how to interpret the 1024-dimensional curve. Instead, the formulation stays informal at exactly the point where precision would matter most.

4. **The empirical comparison protocol is not fully convincing because the paper mixes in numbers from prior papers rather than clearly establishing a uniform re-evaluation.**  
   In **Section 4.1** on Page 5 and the start of Page 6, the authors state that “the specific baselines used vary by benchmark, as we rely on the comparison results published in the original papers.” This is a serious weakness. Once a new method is built on top of AIDE and compared against many detectors, the natural expectation is a controlled benchmark where preprocessing, splits, and evaluation conditions are harmonized as much as possible. Pulling baseline numbers from different papers often introduces hidden confounders: different image resizing, different thresholds, different training durations, and different implementation choices. The paper may be following common practice, but it still weakens the evidential value of claims like “new state-of-the-art.”

5. **The results are mixed in a way that the paper does not analyze deeply enough, especially on AIGCDetect and Chameleon.**  
   The narrative emphasizes success, but **Table 2** on Page 8 tells a more complicated story. According to the table, the proposed method is not second-best mean accuracy on AIGCDetect, it is actually below AIDE and PatchCraft in the reported means: AIDE is 97.05, PatchCraft is 98.43, and Ours is 95.58. This directly conflicts with the text in **Section 4.5**, which says “Our model achieves a mean accuracy of \(91.85\%\), which is the second-best overall.” That is not a small typo, it is a major inconsistency between the prose and the table. Either the table, the mean, or the textual interpretation is wrong.
   
   Even setting the inconsistency aside, the method loses noticeably to AIDE on many columns in **Table 2**, including one of the two StyleGAN columns, CnVbGAN, StoGAN2, Adide, MediPentary, both Stable Diffusion columns, VQDM, Wukong, DALLE2, and SOTA. This is far from a clean win. On **Table 3** (Chameleon, Page 8), the method is better than AIDE for ProGAN training but worse for SD v1.4 training. Again, the message is “competitive,” not “robustly superior.” The paper should spend much more effort characterizing when structural features help and when they hurt.

6. **There is no ablation that isolates the actual source of improvement.**  
   This is the biggest empirical omission. Since the main contribution is one added feature stream, I expected at least:
   - A comparison between raw cumulative gain vector vs. projected vector after the FC + GELU step.
   - Sensitivity to the number of structural points \(N\), especially since \(N=1024\) appears arbitrary.
   - Variants using different pixel representations in **Equation (1)**.
   - Training only the new structural branch and a linear probe vs. the current MLP retraining.
   - A comparison against simpler spatial partition baselines, such as fixed-grid statistics or quadtree-like splits without gain optimization.
   
   Without these, it is hard to know whether the success comes from hierarchical structure specifically, from just adding another moderately informative descriptor, or from optimization luck in retraining the final classifier.

7. **The qualitative evidence is suggestive but not rigorous enough to support the mechanistic claims.**  
   **Figure 1** is visually appealing, but it is still a single cherry-picked example, and the highlighted regions are not quantitatively validated. The paper says the method “isolated” the ear and hair-like structure as suspicious regions, yet the actual model is not trained with segmentation or localization supervision. The figure therefore risks overstating interpretability. Likewise, **Figure 3** only shows examples where AIDE failed and the proposed method succeeded. It would be much more informative to also show failure cases where the structural branch hurts performance, especially since **Section 4.8** admits such degradation exists. As presented, the qualitative section is one-sided.

8. **The paper’s presentation has multiple clarity and consistency problems that undermine trust.**  
   A few examples:
   - **Section 4.5** reports a mean of \(91.85\%\) on AIGCDetect, while **Table 2** reports 95.58 for Ours. That discrepancy is too large to ignore.
   - The method names and dataset columns in **Table 2** appear inconsistent or possibly erroneous, for example duplicate “StyleGAN” columns, unusual names like “Adide” and “MediPentary,” and a “SOTA” column that is not explained in the surrounding text. If these correspond to benchmark-specific generator names, they still need clarification.
   - In **Section 3.2**, “cuboidal partitioning” is borrowed terminology, but for 2D images the paper should explain whether this is effectively rectangular splitting in the image plane, otherwise readers are left guessing.
   - The paper repeatedly claims “state-of-the-art” in contexts where the supporting comparisons are not uniformly re-run and, in the AIGCDetect case, not even clearly better than the strongest listed baseline.
   
   None of these issues alone is fatal, but together they make the paper feel under-polished for a top venue.

9. **The freezing strategy in Section 3.3 is not justified, and it potentially biases the comparison in both directions.**  
   The authors freeze the pre-trained Patchwise and Semantic encoders and train only the final discriminator together with the structural module. That is computationally efficient, but there is no evidence that this is the right integration regime. If AIDE was originally tuned end-to-end or with a different classifier setup, retraining only the head may either underuse or overstate the value of the new branch. A fairer story would compare at least two regimes: frozen AIDE + new branch, and joint finetuning with careful regularization. Without that, the chosen setup feels convenient rather than justified.

10. **The paper does not do enough to position itself against other ways of adding complementary cues to fake-image detectors.**  
   The related work surveys many detectors, but the experimental story mostly reduces to comparing against published leaderboard numbers. Since the whole point is that structural cues complement spectral and semantic cues, the paper should more explicitly differentiate itself from other multi-cue fusion approaches and feature-engineering strategies, both conceptually and empirically. Right now, the reader is left with a broad claim that “structure helps,” but not a sharp understanding of why this specific structural formulation is preferable to other ways of injecting spatial organization.

## Questions
1. In **Equation (1)**, what exactly is the pixel feature vector \(p_i\) used in all experiments? Is it raw RGB, grayscale, another color space, or something else? Please state this explicitly, since it materially changes the partition tree and the resulting gain vector.

2. Please clarify the full splitting algorithm behind **Section 3.2**. For each current segment, do you evaluate all horizontal and vertical cut positions? Is there a minimum segment size? How are ties handled? When you say the next split is chosen by “greatest potential gain,” is this computed globally over all current leaves at every step?

3. Can you provide a corrected and unambiguous definition for **Equation (3)**? As written, \(\hat g_i\) denotes both the ordered gain and the cumulative normalized feature, which is confusing. Also, are the resulting features guaranteed to satisfy \(0 \le f_i \le 1\)?

4. The text in **Section 4.5** says the AIGCDetect mean is \(91.85\%\) and second-best overall, but **Table 2** reports 95.58 for Ours and even higher numbers for AIDE and PatchCraft. Which numbers are correct? This inconsistency needs to be resolved.

5. Please provide an ablation isolating the value of the structural branch: AIDE alone, structural features alone, AIDE + structural features without FC/GELU, and sensitivity to \(N\). This would substantially increase confidence that the observed gains come from the proposed mechanism rather than from adding generic extra features.

6. Since **Table 2** and **Table 3** show several regressions relative to AIDE, can you characterize the failure cases more systematically? For example, what image types or generator families produce negative transfer from the structural branch?

7. In **Figure 1**, the localized suspicious regions are visually highlighted. Are these regions directly derived from the high-gain partitions, and if so, can you quantify localization consistency over a set of examples rather than only presenting one case?

8. Did you re-run AIDE under your exact training protocol, or are some baseline numbers copied from prior papers while your own method is evaluated under a separate setup? A precise statement of what was reimplemented and what was inherited from published tables would improve fairness and reproducibility.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper is about detecting AI-generated fake images, which is socially useful, but it also sits in an adversarial domain. Better detectors can inform more evasive generators, and claims of robustness/generalization may be overinterpreted in deployment settings. This is not a reason to reject on its own, but the paper would benefit from a short discussion of deployment limitations, possible attacker adaptation, and the risk of presenting benchmark gains as real-world forensic reliability.

## Soundness Rating
2: fair. The core idea is plausible and the experiments suggest some signal, but the technical specification is incomplete, there is a significant inconsistency between the AIGCDetect text and **Table 2**, and the evaluation lacks key ablations and controlled comparison details.

## Presentation Rating
2: fair. The paper is readable at a high level, and **Figure 2** helps convey the architecture, but there are multiple presentation problems, including ambiguous notation in **Equation (3)**, underexplained tables, and a serious mismatch between textual claims and reported results.

## Contribution Rating
1: poor. The paper offers an incremental extension of AIDE via an added handcrafted structural descriptor and does not provide enough methodological depth, ablation, or analysis to justify a stronger contribution assessment.

## Overall Rating
2: Reject, not good enough. The idea is sensible and the GenImage result is promising, but the paper currently falls short of ICLR standards due to limited methodological novelty, underspecified feature construction, missing ablations, inconsistent reporting around AIGCDetect, and only mixed evidence of robust superiority over the underlying AIDE baseline.

## Reviewer Confidence
4: confident. I am confident in the main concerns, especially regarding the methodological incrementalism, the mathematical/specification gaps in **Equations (1)-(3)**, and the inconsistencies between the text and the reported tables, though I cannot fully verify implementation-level details from the paper alone.