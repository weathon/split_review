---
job_id: c6493e49-afb0-4f8b-989b-8697ac4410e2
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ZNAY3ivd62.pdf
paper: GUI-Spotlight: Adaptive Iterative Focus Refinement for Enhanced GUI Visual Grounding
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, sitting at the intersection of multimodal representation learning, reinforcement learning, visual grounding, and agentic tool use for GUI understanding.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including abstract, introduction, related work, method, experiments/results, and conclusion, and it presents a concrete method with quantitative evaluation and ablations; while I have several substantive concerns, they do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other obvious manipulation attempts in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes GUI-Spotlight, a GUI visual grounding system that augments a multimodal LLM with three visual tools, `crop`, `extract`, and `find_color`, and trains it to iteratively refine its focus over a screen until it predicts a final coordinate. The method uses a three-stage pipeline, supervised warm-up followed by two reinforcement learning stages based on a modified GSPO objective with an auxiliary cross-entropy term intended to stabilize multi-turn tool use. Experiments on ScreenSpot-Pro, UI-Vision, and OSWorld-G show gains over the underlying 7B backbones, especially for the UI-TARS-1.5-7B initialization, and the paper also includes ablations on RL variants and reward design.

## Strengths
1. **The paper tackles a real bottleneck in GUI agents, namely precise visual grounding on high-resolution cluttered interfaces.** This is a practically important problem, and the paper is not merely reporting another tiny benchmark gain on an easy dataset. The emphasis on pointer-level grounding and failure modes of one-shot grounding is well motivated in Section 1.

2. **The method is conceptually simple and easy to understand.** The overall interaction loop in **Algorithm 1** is straightforward, and **Figure 1** helps considerably here. In particular, Figure 1 makes the intended behavior of the system concrete: the model first acts on the full screenshot, then appends cropped views to the dialogue history, and only stops once it has enough localized evidence. This visualization is much more persuasive than a purely textual description and makes the proposed “iterative spotlight” idea easy to follow.

3. **The empirical gains over the paper’s own backbones are meaningful.** On **Table 3**, the UI-TARS-initialized variant improves from the reported UI-TARS-1.5-7B baseline of 38.7 to 52.8 on ScreenSpot-Pro, which is a substantial jump. Likewise, in **Table 5**, the same initialization improves from 61.9 to 62.7 on OSWorld-G, which is smaller but still shows that the method does not collapse outside the main benchmark. Even the Qwen-initialized version shows consistent improvement relative to its raw base on ScreenSpot-Pro and OSWorld-G.

4. **The paper does more than just present headline benchmark numbers; it provides ablations on algorithmic design choices.** The RL-selection discussion in Section 4.1, especially the comparison in **Figure 3**, is useful. The right panel is particularly informative because it supports a central training claim: vanilla GRPO/GSPO variants become unstable, whereas the added positive-example cross-entropy term appears to prevent the late-stage collapse. This is one of the stronger parts of the paper.

5. **The staged training narrative is reasonably coherent.** The progression shown in **Figure 2** aligns with the stated training pipeline: Stage 1 gives an under-aligned but tool-capable model, Stage 2 produces the largest jump, and Stage 3 provides an additional boost. The figure is simple, but it does support the claim that each stage has a distinct role rather than the whole system depending on one opaque training cocktail.

6. **The paper highlights data efficiency as a practical angle, and the main benchmark table supports that claim to some extent.** In **Table 3**, the best reported GUI-Spotlight model uses 18.5K training samples and still exceeds several 7B baselines trained with much larger datasets. Even if the exact fairness of these comparisons deserves scrutiny, the result is still interesting enough to warrant attention.

## Weaknesses
1. **The paper’s novelty claim is weaker than the writing suggests, because the core idea is largely iterative region refinement with a small set of hand-designed tools.** The method combines an existing MLLM backbone, standard image subregion operations, and policy optimization to learn tool usage. That can still be a useful contribution, but the paper often frames the method as if the main conceptual leap were the “think-with-image spotlighting” paradigm itself. From the main paper alone, what feels genuinely new is not the idea of iterative narrowing, but the particular packaging of three tools plus a modified GSPO training recipe. This matters because the contribution rating should depend on whether this is a substantial methodological advance or a well-engineered composition of known ingredients.

2. **The method is under-positioned against relevant alternatives that are very close in spirit, especially training-free or lightly trained iterative zoom/refinement baselines.** Section 5.4 compares against two internal baselines, but those are relatively weak controls: one is a multi-turn conversational inference baseline, and the other is repeated single-turn recropping around the model’s own prediction. Those are useful, but they do not fully answer the main scientific question, namely whether the gains come from the proposed RL-trained tool policy rather than from iterative zooming itself. This gap matters because the paper’s central claim is about the value of learning adaptive multi-tool refinement. Without stronger direct comparison to competitive iterative-focus alternatives, it is hard to know whether the proposed training complexity is really justified.

3. **The empirical story is uneven across benchmarks, and the paper somewhat overstates generality.** On **Table 3**, the UI-TARS-based variant is strong at 52.8, but the Qwen-initialized variant only reaches 38.7, which is a very large gap. On **Table 4**, the Qwen-initialized variant reaches only 8.3 average on UI-Vision, actually far below the UI-TARS-based version at 23.4 and still not especially convincing as a robust general method. Even within the same method family, the behavior appears highly backbone-dependent. That weakens the broader claim in Section 5.1 that the RL objective and multi-tool coordination “transfer beyond UI-specialized backbones” in a robust way. The transfer exists in a narrow relative-to-base sense, but absolute performance remains poor for the non-UI backbone on UI-Vision.

4. **The evaluation on UI-Vision and OSWorld-G is not strong enough to substantiate the paper’s broader significance claims.** The main benchmark is clearly ScreenSpot-Pro, and there the result is solid. But on **Table 4**, the best model is still below the 7B UI-Venus-Ground baseline, 23.4 vs. 26.5, and far from the stronger larger models. On **Table 5**, the best GUI-Spotlight score, 62.7, is competitive with UI-TARS-1.5-7B at 61.9 but clearly below GTA1-7B at 67.7 and UI-Venus-Ground-72B at 70.4. So the cross-benchmark evidence is more “sometimes helpful” than “consistently strong.” This matters because the paper’s framing is broad, but the strongest support is concentrated on a single benchmark.

5. **Several parts of the mathematical formulation are underspecified or not fully convincing, especially around the RL objective and stability claims.** In Section 3.2.2, the modified objective
   \[
   \mathcal{J}_{\text{Ours}}(\theta)= \mathbb{E}\left[\frac{1}{G}\sum_{i=1}^{G}\min\left(s_i(\theta)\widehat{A}_i,\ \mathrm{clip}(s_i(\theta),1-\varepsilon,1+\varepsilon)\widehat{A}_i\right)\right]+\lambda \mathcal{J}'(\theta)
   \]
   is presented as the key technical improvement, but important details are missing from the main paper. For example:
   - It is not fully specified whether the expectation is optimized with the usual sign convention for gradient ascent or implemented as a minimization objective in practice.
   - The sequence-level ratio
     \[
     s_i(\theta)=\exp\left(\frac{1}{|y_i|}\sum_{t=1}^{|y_i|}\log \frac{\pi_{\theta}(y_{i,t}\mid x,y_{i,<t})}{\pi_{\theta_{\text{old}}}(y_{i,t}\mid x,y_{i,<t})}\right)
     \]
     uses an average log-ratio before exponentiation, effectively a geometric mean token ratio, which is not the standard PPO token-level importance ratio. That may be inherited from GSPO, but the paper does not explain why this is appropriate specifically for long, multi-turn tool trajectories, nor what failure modes it avoids or introduces.
   - The auxiliary term \(\mathcal{J}'(\theta)\) is said to be computed on outputs that are both format-valid and result-correct, but “result-correct” is itself a composite notion in this environment. Is a trajectory correct only if the final answer lands in \(B^\star\), or also if intermediate tool use is semantically appropriate? That distinction matters because the positive-example loss can easily bias the model toward shallow local formats rather than better exploration.
   - The paper attributes stability improvements to this term, but the evidence is empirical only. That is acceptable, yet the text on Pages 4-5 sounds closer to a causal optimization diagnosis than the main paper rigorously supports.

6. **The reward design has hidden assumptions and possible failure modes that are not discussed.** In **Table 2**, \(r_2\) rewards crop IoU with the ground-truth box, \(r_3\) gives extract a reward of 1 if the quadrant fully contains \(B^\star\), and \(r_4\) rewards whether a 200×200 color-match window covers \(B^\star\). This creates a training setup in which intermediate tool calls have access to supervision signals that may not align with how the final system is supposed to reason. A crop that barely overlaps the target can still get positive signal through IoU, while extract receives an all-or-nothing criterion based on full containment. The paper does not analyze whether these reward choices induce overly conservative crops, degenerate repeated containment strategies, or benchmark-specific heuristics. The right panel of **Figure 4** shows sensitivity to the Crop/Extract reward ratio, which is actually evidence that the behavior is fragile to reward shaping rather than obviously robust.

7. **The tool design itself is somewhat ad hoc, and the paper does not justify why these three tools are the right abstraction.** Table 1 defines `extract` as a quarter crop based on coarse position, `find_color` as sliding 10×10 patches with stride 10 and then centering a \(w/s \times w/s\) window, and `crop` as a rectangular crop with some edge-case adjustments. This is a very handcrafted action space. Why quarter crops rather than learned scales? Why a fixed 10-pixel stride for color search? Why is the `find_color` reward tied to a 200×200 window in Table 2 while Table 1 describes a centered \(w/s \times w/s\) crop? The relation between the tool implementation and reward computation is not fully clear. This matters because the reported performance may depend heavily on these implementation details, yet they are treated as if they were natural primitives.

8. **The data construction and filtering pipeline raises concerns about evaluation bias and reproducibility.** On Pages 3-4, the authors collect high-resolution samples and then use Qwen2.5-VL-72B to score instruction quality, bounding-box accuracy, and consistency. This means a powerful external MLLM is used as both a quality controller and, indirectly, a data curator. That can produce cleaner data, but it also injects another model’s preferences into the training set. The paper does not analyze whether the retained examples become skewed toward easy, text-heavy, or model-legible interfaces. Since only about 50% of UGround is retained, the filtering is quite aggressive, and the resulting training distribution may differ materially from the original one. That matters for scientific interpretation of the data-efficiency claim in **Table 3**, because “18.5K curated samples” is not comparable to arbitrary 18.5K raw samples.

9. **The exposition has multiple clarity and notation issues that reduce confidence in technical precision.** A few examples:
   - In **Algorithm 1**, line 8 says `Tool(i, args)` although the text above describes the model output as `Action(i, Tool, args)`. This is minor, but symptomatic.
   - Algorithm 1, line 12 returns `None` after the loop body, but the indentation in the pseudo-code makes it ambiguous whether this return happens after the first non-stop action or after the entire loop ends. The intended semantics are obvious from the prose, but the algorithm as printed is sloppy.
   - On Page 5, the bucketing notation for Stage 3 is not presented cleanly. The notation \(\hat S_t \subseteq S_t, |\hat S_t| = n_{\min}\) is fine, but the subsequent definition of \(C_b\) is awkwardly formatted and not well integrated with the earlier explanation of \(\mathcal{J}'(\theta)\).
   - Table 2 uses a mix of prose and formulas that is grammatically rough enough to force the reader to infer meaning, for example “1 if the final answer the predicted coordination \((\hat x,\hat y)\) lies inside the \(B^\star\).” Presentation issues alone are not fatal, but here they interact with already-complex training claims.

10. **The figures are informative but also reveal limitations that the paper does not fully confront.** **Figure 3 (left)** shows that many RL tweaks have only small differences in final accuracy, except the final variant with tool-filtered positives. That suggests the method’s performance may hinge more on preventing syntax collapse than on genuinely better policy learning. **Figure 4 (left)** shows sparse and dense answer rewards converging to quite similar ranges, with the margin labeled as “diminishing marginal gains”; this makes the reward-design contribution look narrower than the prose suggests. **Figure 5** is also a bit too coarse: it reports three bars, 7.6, 47.6, and 52.8, but it does not reveal how many steps each method uses, what the stopping conditions are, or whether the baseline iterative methods are compute-matched. Since the whole paper argues for adaptive multi-step reasoning, that missing control matters a lot.

11. **The paper’s “sample efficiency” claim is directionally interesting but not fully apples-to-apples.** In **Table 3**, the model is compared against systems trained on much larger corpora, which sounds impressive. But the compared methods often differ not just in sample count, but also in data source, pretraining, synthetic generation pipeline, backbone initialization, and task formulation. In other words, the table shows that the proposed fine-tuning recipe can add value with relatively little additional data, not necessarily that the overall method is intrinsically more sample-efficient in a controlled sense. The current wording occasionally blurs that distinction.

12. **The paper could do a better job separating tool-use capability from underlying backbone strength.** The strongest model is initialized from UI-TARS-1.5-7B, which is already a strong GUI-specialized base. The Qwen-initialized version is much weaker on the harder benchmarks. This pattern suggests that GUI-Spotlight may function primarily as a refinement layer on top of already-strong GUI priors rather than a generally powerful grounding framework. That is still useful, but the paper should state it more directly.

## Questions
1. **Can the authors provide a more controlled comparison against stronger iterative-focus baselines?** The baselines in Section 5.4 are a start, but I would like to see either a compute-matched test-time zoom baseline with adaptive stopping or a stronger fixed-policy region-refinement baseline using the same backbone and the same number of image crops. This would directly test whether RL-learned tool policies add value beyond iterative recropping itself.

2. **Please clarify the exact optimization objective and implementation details for Section 3.2.2.** Is \(\mathcal{J}_{\text{Ours}}\) maximized directly, or do you optimize its negative? How exactly is the expectation estimated in practice with grouped rollouts? A short derivation or pseudo-code for how \(s_i(\theta)\), \(\widehat A_i\), and \(\mathcal{J}'(\theta)\) are combined during one update would improve confidence substantially.

3. **What precisely qualifies a sample as “result-correct” for the mask \(C_b\) in \(\mathcal{J}'(\theta)\)?** Is correctness based only on the final answer coordinate falling inside \(B^\star\), or do intermediate tool choices matter? If only the final answer matters, have you observed the model learning poor but lucky trajectories that are then reinforced by the auxiliary term?

4. **Can you report tool usage statistics and failure breakdowns?** For example, average number of tool calls, frequency of each tool, percentage of trajectories ending with malformed outputs before/after Stage 2, and accuracy as a function of number of steps. This would help interpret **Figure 5** and make the “adaptive iterative focus” claim more concrete.

5. **How sensitive are results to the handcrafted tool parameters?** I would specifically like to know about the stride in `find_color`, the crop size used after color matching, and the quarter-crop design of `extract`. An ablation on these parameters would help determine whether the gains are robust or dependent on brittle engineering choices.

6. **Could the authors clarify the relationship between the tool implementation in Table 1 and the reward in Table 2 for `find_color`?** Table 1 describes a centered \(w/s \times w/s\) window, while Table 2 refers to a fixed \(200 \times 200\) window. Are these the same in practice for the benchmark resolution, or is the reward computed with a different crop definition than the actual tool output?

7. **For the data filtering pipeline, can the authors quantify the distribution shift induced by filtering?** In particular, what kinds of examples are disproportionately removed by IQ, BA, and CON? If the retained subset is biased toward cleaner textual elements, that would affect how strongly one can interpret the sample-efficiency claims.

8. **Please add variance or repeated-run statistics for the headline results if available.** The training curves in **Figures 2-4** suggest nontrivial stochasticity, so reporting mean and standard deviation over multiple seeds, at least for the main ScreenSpot-Pro result, would increase confidence.

## Flag For Ethics Review
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The ethics statement on **Page 10** is too brief for the actual data collection and application setting.

1. **Legal / compliance concerns.** In **Appendix A.4**, the paper describes automated crawling of high-traffic websites such as google.com, youtube.com, facebook.com, instagram.com, reddit.com, x.com, amazon.com, netflix.com, and others, followed by screenshot capture and element extraction. That raises at least terms-of-service, copyright, and dataset redistribution questions. The paper says the data will be released after publication, but it does not discuss permissions, licensing, or redistribution constraints for screenshots of commercial websites and their UI elements.

2. **Potentially harmful applications.** A method that improves precise GUI grounding can be used for benign automation, but it can also lower the barrier for scalable interaction with third-party interfaces, including automating actions on websites and desktop environments in ways the platform operator may not intend. The paper does not need an alarmist treatment, but the current statement that the work does not introduce foreseeable risks is too dismissive.

## Soundness Rating
2: fair. The empirical results are interesting and the method appears to work, but the central claims are only partially supported due to limited baseline positioning, under-specified optimization details, and some overreach in the interpretation of generality and sample efficiency.

## Presentation Rating
2: fair. The core idea is understandable and several figures are helpful, but the paper has enough notation issues, pseudo-code ambiguities, and rough phrasing that the presentation falls short of what I would expect for a strong ICLR paper.

## Contribution Rating
2: fair. There is a useful engineering contribution here, especially the combination of iterative tool use with RL stabilization, but the conceptual advance over existing iterative refinement and region-focusing approaches feels moderate rather than strong.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper addresses an important problem and contains some solid empirical work, especially the RL ablations and the strong ScreenSpot-Pro result for the UI-TARS-based model. However, the novelty is more incremental than the framing suggests, the method is insufficiently positioned against stronger iterative-refinement alternatives, and the technical presentation leaves too many ambiguities around the optimization and reward design for me to support acceptance confidently.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main methodological and experimental details carefully, though I cannot fully verify all implementation-specific aspects from the main paper alone.