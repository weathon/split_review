---
job_id: f5ba07d9-9f1a-4e05-91e9-f8cecd96a0ea
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Ry8jLSYIUG.pdf
paper: We Can Hide More Bits: The Unused Watermarking Capacity in Theory and in Practice
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining learning theory, optimization/representation-related ML systems, and empirical analysis of deep watermarking models for vision.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, related-work discussion, methodology/theory, experiments, quantitative results, and conclusion/discussion; while I have substantial concerns about rigor and positioning, these are review-level issues rather than desk-rejection issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, instructions targeting automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies the gap between theoretical and practical capacity in image watermarking. The main paper derives capacity bounds under a PSNR constraint and then extends the analysis heuristically to robustness against linear transformations such as crop-rescale, rotation, and a linearized JPEG operator. Empirically, the paper argues that current deep watermarking models underuse available capacity by showing failures of Video Seal in simplified settings, presenting simple linear and handcrafted constructions that achieve much higher payloads in PSNR-only setups, and introducing a scaled-up model, Chunky Seal, that increases robust payload from 256 to 1024 bits.

## Strengths
The paper asks a useful and timely question. A lot of watermarking work treats the current 100 to 256 bit regime as if it were close to saturation; this submission usefully challenges that assumption and tries to separate true fundamental limits from architectural/training bottlenecks.

The PSNR-only analysis in Sections 2.2 to 2.4 is the strongest part of the paper. Modeling images as lattice points in a cube and feasible watermarked outputs as integer points in an $\ell_2$ ball induced by Equation (1) is clean and easy to reason about. The transition across regimes in **Figure 3** is particularly helpful: it shows how Bounds 2, 3, 4, 6, 7, and 8 behave as PSNR changes, and it gives an intuitive sense that the gray-image and arbitrary-cover cases differ by at most about 1 bpp. Even if some approximations are loose, this part of the paper is conceptually coherent.

The simplified empirical setup in Section 3 is well chosen. Training Video Seal on a single gray image with only an MSE/PSNR constraint is a sharp sanity check, because it removes many confounders usually invoked to justify low capacity. **Figure 5** makes this point clearly: the left and center panels show that Video Seal saturates early and does not benefit much from larger spatial resolution, while the right panel shows a linear encoder/decoder succeeding at 1024 and 2048 bits. This is a strong and concrete experimental probe of architectural limitations.

There is a useful connection between visual evidence and numerical evidence. **Table 1** backs up the claims from Figure 5 with exact PSNR and bit-accuracy values, and the contrast is striking: Video Seal at $256\times256$ fails at 1024 bits with 89.63% bit accuracy at 40.10 dB, while the linear model reaches 100% at both 1024 and 2048 bits with 44.28 dB and 40.40 dB. That table is one of the most convincing pieces of the paper.

The paper also provides a practical, if brute-force, demonstration that higher robust capacity is achievable. **Table 3** shows that Chunky Seal reaches 1024 bits with overall bit accuracy 99.15% against Video Seal’s 99.31%, while keeping PSNR in roughly the same range. Even though the model is enormous, this still supports the paper’s central claim that current deep watermarking systems are not saturating capacity.

The discussion section is refreshingly honest that Chunky Seal is not itself a practical endpoint, and that the more important message is architectural underperformance. I appreciated that the authors do not oversell the scaled model as a deployable answer.

## Weaknesses
1. **The paper’s strongest claim rests on theory that is only rigorous in the easiest setting, while the more practically important robustness part is explicitly heuristic.**  
   The submission’s headline message is that practical watermarking is far below fundamental limits, including under robustness constraints. But in **Section 2.5** the paper repeatedly concedes that Bounds 10 to 12 are heuristics, not valid lower bounds and not valid upper bounds either. The appendix is even more explicit: **Figures 8 and 9** show cases where the singular-value-based heuristic can both under- and over-estimate true capacity due to quantization effects. This matters because the main practical conclusion, namely that robust watermarking should still allow around 0.5 bpp under severe crop-rescale or large capacities under LinJPEG, depends heavily on those heuristic estimates in **Figure 4**. Once those are admitted not to be bounds in either direction, the interpretation of Figure 4 shifts from “capacity remains large” to “one particular heuristic suggests capacity remains large.” That is a much weaker scientific statement.

2. **The terminology around “bounds” is too loose and occasionally misleading, especially once the paper moves beyond PSNR-only analysis.**  
   In the main text, the paper often presents a family of “bounds” together in one narrative, but some are exact counts, some are volume approximations, some are minima of other expressions, some are heuristics, and some are conservative lower bounds that the authors themselves call unrealistic. This creates a credibility problem. For example, **Bound 6** in Section 2.3.3 is justified empirically because it “closely tracks” Bound 5 in **Figure 3 left**, but that observation is only demonstrated at low-dimensional illustrative settings, not proved generally. Likewise, **Bound 13** is called an “actual lower bound” in Section 2.5, yet the main paper relies much more on the heuristic family because the lower bound is too conservative to support the intended narrative strongly. The paper would benefit from a much stricter separation between theorem-level claims, approximation-level claims, and intuition-level claims.

3. **Some mathematical steps and notational choices are sloppy enough to make careful verification unnecessarily difficult.**  
   There are several places where the exposition needs tightening. In **Section 2.5**, the transformation is written as $M \in \mathbb{R}^{c \times h \times c \times h}$, while elsewhere the linear operators act on flattened images in $\mathbb{R}^{cwh \times cwh}$; this is almost certainly a notational error, but it is precisely the kind of mismatch that hurts trust in a theory-heavy paper. In **Equation (6)**, the reduction factor $\xi_M=\prod_{\sigma_i>0}\min(\sigma_i,1)$ is presented as the key effect of quantization under linear transforms, but its derivation is heuristic and the example following **Equation (5)** is only an intuition, not a proof. In **Bound 12**, the formula as rendered is quite hard to parse, with inconsistent indexing and an expression for the box limits that appears typographically corrupted. In **Bound 13** on Page 30, the interval inside the product seems to read $\left[\frac{\beta_j}{\epsilon},\frac{\beta_j}{\epsilon}\right]$, which is almost surely missing the negative lower endpoint and would define a degenerate interval as written. These are not cosmetic nits in a paper whose value proposition leans heavily on theory.

4. **The empirical comparison is narrower than the paper’s rhetoric suggests.**  
   A recurring narrative is that “current models” underperform relative to theory, but the main body’s controlled experiments in Section 3 are effectively centered on one architecture family, Video Seal, plus a scaled-up version of it. The failure mode may well be real, but the paper does not establish that this is representative of modern watermarking architectures generally. This matters because the conclusion on Page 10 goes beyond “Video Seal is structurally limited” and suggests that modern methods broadly leave large capacity unused. The stronger that claim, the broader the empirical support should be.

5. **The single-gray-image setup is informative, but the paper overgeneralizes from it.**  
   The experiments in **Section 3.1 and 3.2** are a good sanity check, but they are also an extremely special case: one solid gray cover image, no augmentations, and often no perceptual constraints beyond MSE. The paper uses these experiments to dismiss explanations A, B, and C listed in Section 3, namely robustness, perceptual constraints, and data distribution. That leap is too aggressive. At best, the experiments show that these factors are not necessary to produce low-capacity behavior in one architecture. They do not establish that such factors are unimportant in realistic watermarking. The gap between “this simplified setup still fails” and “therefore these real-world complexities cannot explain the practical gap” is too large.

6. **The practical contribution, Chunky Seal, is somewhat undercut by scale and by mixed quality metrics.**  
   The main practical result in **Table 3** is a 4x capacity increase, which is meaningful. However, it comes with a roughly 90x larger embedder and 23x larger extractor. Moreover, the table shows a noticeable LPIPS degradation, from 0.0019 for Video Seal to 0.0085 for Chunky Seal, while several robustness metrics are slightly worse, especially rotation and JPEG. So the conclusion that Chunky Seal preserves quality and robustness “comparably” is directionally true but somewhat generous. The result is still interesting, but it looks more like a costly scale-up baseline than a compelling new Pareto frontier point. For a paper arguing that substantial headroom remains, this is acceptable; for a paper presenting Chunky Seal as evidence of practical progress, it is less persuasive.

7. **The literature positioning is incomplete for a paper making broad claims about capacity ceilings and current practice.**  
   The related-work discussion focuses mostly on classical information-theoretic analyses and a subset of deep watermarking systems. For a submission that repeatedly argues the field has plateaued around a few hundred bits and that much higher capacities are achievable in practice, the empirical positioning should be broader and more up to date, especially around recent high-capacity watermarking approaches and systems that specifically tackle geometric robustness. As written, the paper’s practical claims are more sweeping than its comparative empirical positioning.

8. **The dataset/distribution argument in Section 2.6 is too speculative to carry the conclusion assigned to it.**  
   The authors estimate the number of “possible covers” in a PSNR ball using capacity arguments from VQ-VAE/VQGAN-style latents and then conclude that data distribution has a negligible effect on watermarking capacity, reducing capacity by only about 0.05 bpp in a representative example. This is an interesting back-of-the-envelope argument, but it depends on very coarse upper-bounding logic and on a notion of perceptual distinctness that is not tied to blind watermark decoding errors in any formal way. The resulting conclusion that data distribution “cannot explain the low performance of current models” is therefore too strong.

9. **Several visual and quantitative elements support a weaker claim than the text asserts.**  
   **Figure 1** is effective as a motivating overview, but it visually compares a mixture of theory curves, heuristic robustness curves, and practical models on the same plot, which risks implying a stronger apples-to-apples comparison than is warranted. Similarly, **Figure 4** gives the impression of robust capacities remaining very high under crop-rescale, rotation, and LinJPEG, but given the status of Bounds 10 to 12, those curves should be interpreted much more cautiously. On the quantitative side, **Table 2** gives conservative capacities at PSNR 42 dB, and those values are indeed above current payloads, but the conservativeness varies wildly by transformation and dimension; the paper does not sufficiently discuss how loose these lower bounds may be in realistic image sizes.

10. **Presentation quality is uneven, especially in theory-heavy sections.**  
   The paper has a strong high-level story, but the execution is rough. Some equations are visibly mangled in the provided rendering, there are multiple notation inconsistencies, and the transition between main-text claims and appendix caveats is not always disciplined. This is particularly problematic because the paper’s contribution is not just empirical, it is partly theoretical; readers need confidence that the derivations are stated cleanly and precisely.

## Questions
1. The central practical argument relies on the claim that robustness-aware capacity remains far above current model performance. Since **Bounds 10 to 12** are acknowledged not to be valid lower or upper bounds, can the authors provide a clearer statement of exactly which claims in **Section 2.5 and Figure 4** should be interpreted as theorem-backed versus heuristic? A revised wording that sharply separates these categories would increase my confidence substantially.

2. Can the authors clarify the apparent notation and formula issues around **Section 2.5, Bound 12, and Bound 13**? In particular:
   - should the operator space be $\mathbb{R}^{cwh \times cwh}$ rather than $\mathbb{R}^{c \times h \times c \times h}$,
   - is the interval in **Bound 13** missing a negative lower endpoint,
   - and can the authors provide a cleaner, typeset version of **Bound 12** with unambiguous indexing?
   These are fixable issues, but they matter a lot for assessing the theory.

3. The simplified gray-image experiment is compelling, but it supports a narrower conclusion than the current prose states. Can the authors moderate or more carefully justify the jump from “Video Seal fails in a simplified setup” to “robustness/perceptual/data constraints do not explain the real-world gap”? For example, do the authors have any supporting experiment on nontrivial image distributions but still simplified losses, or on other architectures?

4. In **Table 3**, Chunky Seal improves capacity 4x but is vastly larger and somewhat worse in LPIPS and some robustness slices. Can the authors provide either a capacity-vs-compute or capacity-vs-parameter efficiency discussion, or at least a more explicit acknowledgement that this is a proof-of-feasibility scaling result rather than a practical Pareto improvement?

5. The conclusion that modern architectures fail to exploit image resolution is based largely on the comparison between the $256\times256$ and $32\times32$ Video Seal experiments in **Figure 5** and **Table 1**. Can the authors add analysis of where that bottleneck comes from architecturally, for example message broadcasting, receptive-field issues, decoder compression, or optimization pathologies? That would make the diagnosis more actionable.

6. For the handcrafted construction around **Equation (2)**, can the authors clarify exactly how decoding behaves under integer rounding and whether the construction assumes exact arithmetic and no clipping edge cases? A concise explicit encoder/decoder algorithm in the main text would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics review needed based on the content presented in the main paper.

## Soundness Rating
2: fair. The PSNR-only part is reasonably motivated and partially convincing, but several central practical claims rely on heuristic robustness analysis and the mathematical exposition contains enough ambiguities that I cannot rate soundness higher.

## Presentation Rating
2: fair. The high-level narrative is clear and some figures/tables are effective, but the theory sections suffer from notation issues, overloaded terminology around “bounds,” and formulas that are difficult to verify.

## Contribution Rating
2: fair. The paper asks an important question and offers an interesting challenge to prevailing assumptions, but the practical/theoretical support for the strongest claims is not yet strong enough for me to view this as a solid ICLR-level contribution in its current form.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has an interesting core idea, a useful PSNR-only sanity-check analysis, and some genuinely thought-provoking experiments, but the robustness theory is too heuristic, the claims are too broad relative to the evidence, and the presentation of the mathematics needs a substantial cleanup.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain; I carefully checked the main claims and equations, and my main uncertainty is how much weight to place on the heuristic robustness analysis versus the stronger PSNR-only part.