---
job_id: ad74aff2-0f53-4871-b1e5-11e6ec790bfd
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 65Ai8mLfjI.pdf
paper: Rethinking Global Text Conditioning in Diffusion Transformers
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies generative models and conditioning mechanisms in diffusion transformers for image/video generation and editing.

## Minimum Quality
Pass ✅. The submission contains the expected components, including abstract, introduction, related work, methodology, experiments, quantitative/qualitative results, and conclusion; while I have substantive concerns about methodological clarity and experimental depth, these do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions targeting automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper revisits the role of pooled global text embeddings in diffusion transformers, arguing that while the pooled embedding often contributes little in standard use, it can still be useful as a test-time guidance signal. The authors propose modulation guidance, a training-free method that perturbs the global conditioning vector via positive and negative prompts, optionally with a layer-dependent dynamic schedule, and show improvements across text-to-image, text-to-video, and instruction-guided editing settings. The paper also studies models where CLIP-style pooled conditioning appears inactive, and proposes a lightweight way to reintroduce pooled conditioning into models that originally omit it.

## Strengths
The paper asks a timely and practically relevant question. Many recent diffusion transformers have moved toward attention-only conditioning, and the submission does a good job motivating why it is worth probing whether pooled global conditioning is actually useless, or merely underused.

The proposed intervention is simple and easy to understand. Equation (3) is a straightforward guidance rule in modulation space, and one appealing aspect is that it is inference-time only and computationally light because it perturbs a shared conditioning vector rather than repeatedly modifying large attention activations. This makes the idea practically attractive, especially for users of distilled or few-step models where standard CFG-style tricks are less natural.

The empirical scope is broad. The paper covers several text-to-image models with modulation conditioning, extends to CLIP-free models by adding a small MLP on top of pooled text embeddings, and also reports results for text-to-video and editing. Even if not every experiment is equally convincing, the breadth does help support the claim that the mechanism is broadly applicable.

The analysis in Section 4 is interesting and, at minimum, useful as a negative result. Table 1 on Page 3 is one of the more informative parts of the paper: for FLUX schnell, removing CLIP has almost no effect on long prompts, while removing T5 causes a large drop; for HiDream-Fast, removing CLIP has essentially no effect at all. That table supports the central claim that pooled CLIP conditioning is often weak or inactive in current models. Figure 1 complements this by showing that the DreamSim distance between outputs with and without CLIP shrinks as prompt length increases. This figure-table pairing is effective and is one of the stronger parts of the submission.

Some of the qualitative figures are genuinely helpful rather than decorative. Figure 2 illustrates that shifts in modulation space can induce semantically meaningful local and global changes, which is important for making the idea plausible. Figure 4 is also useful because it at least attempts to peek inside the model and connect guidance to altered token attention, rather than stopping at black-box outcome metrics.

There is a practical contribution in showing that CLIP can be reintroduced into models that originally lack pooled conditioning, with gains only appearing when that signal is used through modulation guidance. In Table 2, the COSMOS rows support this story reasonably well: "+CLIP" alone is flat or worse, while the subsequent guidance rows improve human preference and several automatic metrics. That is a nice empirical sanity check for the paper's central thesis.

Presentation is generally strong. The paper is well organized, the high-level idea is clear, and the figures are placed sensibly near the claims they support.

## Weaknesses
1. **The main method is simple, but the scientific account of why it should work is still too hand-wavy, and the paper occasionally overstates what has been established.**  
   Equation (3) on Page 4 defines the core method as
   \[
   \hat{\mathbf y}(\mathbf p,\mathbf p_+,\mathbf p_-,t)=\mathbf y(\mathbf p,t)+w\left(\mathbf y(\mathbf p_+,t)-\mathbf y(\mathbf p_-,t)\right).
   \]
   This is easy to implement, but the paper jumps quickly from this algebraic perturbation to claims about "guiding the model toward modes with more desirable properties" and accessing "interpretable directions" already embedded in the model. That is a much stronger claim than what the evidence really shows. As written, the method could simply be acting as a prompt-style bias injected through AdaLN-like conditioning, without implying any robust geometric structure of modulation space. Figure 2 shows two cherry-picked semantic edits, but this is not enough to support broader statements about interpretable directions. I would strongly suggest tempering those claims, or adding a more systematic analysis of linearity, consistency across seeds, and transferability of the same direction across prompts and models.

2. **The dynamic guidance mechanism is underdeveloped in the main paper, despite being presented as an important improvement.**  
   The paper says on Page 4 that “we consider the simplest variant present in Figure 3(b)” and that additional strategies are deferred to the appendix. But dynamic guidance is not a minor tweak here, it is central to the paper’s claim that modulation guidance can improve aesthetics without sacrificing prompt fidelity. Figure 3(a) indeed suggests a better PickScore-CLIP trade-off for dynamic versus constant guidance, and Figure 3(b) visualizes the chosen step function over layers, but the main paper does not define the full family of schedules clearly, does not justify why the layer index should matter mechanistically, and does not explain how the chosen starting layer \(i\) transfers across architectures of different depths. Since the method’s success depends substantially on this scheduling, the current main-paper treatment feels too shallow.

3. **Several important experimental choices are insufficiently specified, which hurts reproducibility and weakens confidence in the comparisons.**  
   This issue shows up repeatedly. In Section 6.1, human preference is measured on 128 PartiPrompts for general changes and 70 CompBench prompts for counting, but the paper does not clearly state whether prompts, seeds, and sampling hyperparameters are matched across all compared methods in every experiment. For the side-by-side win rates in Tables 2 and 3, there is no confidence interval, no annotator agreement statistic, and no explicit statistical test in the main paper, despite claims of statistically significant gains. Likewise, for the automatic metrics, the exact generation settings, number of seeds per prompt, and whether reported values are averaged across runs are unclear. With methods like this, small prompt- or seed-dependent swings are common, so these details matter.

4. **The empirical evidence focuses heavily on preference-style or proxy metrics, while prompt-faithfulness trade-offs are not examined rigorously enough.**  
   The paper repeatedly emphasizes improvements in aesthetics and complexity. But the obvious concern is that such guidance may simply steer the model toward a preferred visual style that partially overrides user intent. Figure 5 on Page 7 is a good example: the qualitative samples look more polished, but they also look pushed toward a common glossy aesthetic. Table 2 reports relevance win rates near 44 to 53 for several settings, which basically says text relevance is often unchanged or slightly worse. Yet the paper’s discussion is fairly gentle about this tension. Since the method is explicitly designed around prompts like “Ultra-detailed, photorealistic, cinematic” versus “Low-res, flat, cartoonish” in Table 5, the risk of style override is not incidental, it is the method. The evaluation should therefore include prompts whose intended output is simple, flat, sketch-like, diagrammatic, or otherwise anti-photorealistic, and test whether the guidance degrades compliance. Right now, the paper mostly demonstrates that adding beautifier-like directions makes images look better under aesthetics-oriented metrics, which is not the same as preserving prompt fidelity.

5. **Baseline coverage is decent but still not fully convincing for the paper’s strongest practical claims.**  
   The paper compares against Normalized Attention Guidance, LLM-enhanced prompts, and Concept Sliders in the appendix, which is useful. However, for the main paper’s headline message, stronger and more direct practical baselines should be front-and-center, not buried later. For example, when the method uses fixed positive/negative quality prompts, the most natural baseline is prompt engineering of comparable strength at equal token budget and equal number of text encoders, rather than only the relatively generic LLM-enhanced prompt baseline in Appendix E. Similarly, since the paper frames the approach as complementary to CFG, more main-paper comparisons to well-tuned CFG schedules would help establish that the gains are not largely recoverable through existing guidance tuning. Figure 15 in the appendix suggests complementarity, but the main paper gives this limited space.

6. **The treatment of models without pooled conditioning is interesting but methodologically thin in the main paper.**  
   On Page 5, the authors describe adding a small MLP on top of the pooled embedding and distilling against the original model while freezing the rest of the network. This is potentially a nice contribution, but several details are underspecified: the exact architecture and dimensionality of the MLP, where and how it is added to the timestep embedding, whether the added branch is normalized or scaled, what data distribution is used for the synthetic 500K samples, and how training hyperparameters were selected. More importantly, the setup where T5 receives an unconditional prompt and all text is forced through the pooled embedding is somewhat unusual. It makes sense as a probe, but it also changes the information pathway substantially, so it is not obvious that the resulting “+CLIP” rows isolate only the effect of reintroducing pooled conditioning in a clean way.

7. **The causal interpretation from attention visualizations is much too strong relative to the evidence shown.**  
   Figure 4 on Page 5 is suggestive, but attention visualizations are notoriously easy to over-interpret. The paper states that the model “focuses more on the desired features” and shifts attention toward more relevant tokens such as *hands* and *child*. Even if the plots are accurate, this only shows correlation between modulation guidance and changed attention weights, not that the changed attention is the mechanism producing better hands. The figure would be more compelling if paired with quantitative analysis over many prompts, layer-wise changes, and a control experiment showing that comparable output improvements are not accompanied by identical attention shifts under an unrelated intervention.

8. **The evidence for the claim that pooled CLIP is inactive on long prompts is narrower than the phrasing suggests.**  
   Section 4 studies FLUX schnell and HiDream-Fast, with short and long prompts from MJHQ. Table 1 and Figure 1 do support the claim for those settings, but the paper’s language sometimes reads more broadly, as if this is a general property of modern diffusion transformers. In reality, the evidence is from a small number of models and prompt sets, and one of the models shows a prompt-length-dependent effect rather than a universal null effect. This should be stated more cautiously. Also, Figure 1 appears to summarize prompt-length trends for one setup, but the exact sample count per length and the dispersion across seeds are not discussed in the main text, making the “fully resemble the initial ones” claim stronger than what the figure alone can support.

9. **Some result tables are harder to interpret than they should be because the evaluation target is not always aligned with the intervention.**  
   Table 4 on Page 9 reports VBench gains for video, with especially large improvement in dynamic degree for CausVid under modulation guidance. This is intriguing, but also raises a red flag: the same aesthetics-style prompt direction from text-to-image is reused for video, yet the standout gain is in dynamic degree rather than aesthetic quality. That is not impossible, but it is not explained convincingly. If the modulation direction primarily encodes a photorealistic/aesthetic prior, why does it so strongly improve motion dynamics after distillation? This deserves a deeper explanation or at least a more careful ablation. Otherwise, one worries that the method is altering the distribution in a way VBench happens to reward, without a stable semantic interpretation.

10. **There are a few exposition and notation issues around the conditioning formulation.**  
   In Equation (1) on Page 2,
   \[
   \mathbf y(\mathbf p,t)=\mathrm{MLP}(t,\mathrm{CLIP}(\mathbf p)), \qquad \mathbf s=[\mathrm{T5}(\mathbf p),\mathbf x],
   \]
   the notation conflates concatenation and conditioning somewhat loosely. It would help to define more precisely whether \(\mathrm{MLP}(t,\mathrm{CLIP}(\mathbf p))\) means concatenation of embeddings, addition after projection, or a more structured fusion. Similarly, Equation (2),
   \[
   \mathrm{Mod}(\mathbf s,\mathbf y)=\alpha_{\mathbf s}(\mathbf y)\cdot \mathbf s+\beta_{\mathbf s}(\mathbf y),
   \]
   uses \(\alpha_{\mathbf s}\) and \(\beta_{\mathbf s}\) in a way that suggests dependence on \(\mathbf s\), while the text says the coefficients are produced from the global conditioning vector \(\mathbf y\). If \(\alpha\) and \(\beta\) are functions of \(\mathbf y\) only, the notation should reflect that. These are not fatal errors, but in a paper centered on conditioning pathways, such notation should be tighter.

11. **The contribution is somewhat narrower than the framing suggests.**  
   The paper is not really “rethinking” global text conditioning in a comprehensive sense; it is showing that one can use pooled text embeddings as an extra guidance handle for quality/style steering. That is a useful finding, but it is more modest than the framing in the title and introduction. The strongest results are around aesthetics, complexity, and a few targeted attributes, not around improving core semantic alignment or offering a deeper new understanding of why pooled conditioning is retained in some architectures and dropped in others.

## Questions
1. The main practical concern is prompt override. Can the authors provide controlled experiments on prompts that explicitly request low-detail, flat, cartoon, schematic, or minimalist outputs, and show whether aesthetics/complexity modulation harms faithfulness there? A rebuttal with quantitative results on such adversarial prompt subsets would increase my confidence substantially.

2. For Table 2 and Table 3, please report confidence intervals or significance tests in the main paper, and clarify the exact number of raters, the aggregation rule, and inter-rater agreement. Right now the human evaluation methodology is too lightly specified relative to how much the claims rely on it.

3. Can the authors formalize the dynamic schedule more clearly? In particular, if the model has \(L\) layers and guidance is applied only after layer \(i\), what determines \(i\) across models of different depth? Is the schedule indexed in absolute layer number or normalized depth? This matters for portability.

4. For Equation (3), have the authors checked whether the direction
   \[
   \Delta \mathbf y = \mathbf y(\mathbf p_+,t)-\mathbf y(\mathbf p_-,t)
   \]
   is stable across timesteps \(t\) and prompts \(\mathbf p\)? If the semantic effect depends strongly on \(t\) or on the base prompt, the “direction” interpretation becomes weaker.

5. For the CLIP-free models, please clarify the exact architecture and training setup of the added MLP branch. What is the hidden size, activation, normalization, and injection point? Also, why is forcing T5 to unconditional prompts the right distillation design, rather than keeping the original text path and training the pooled branch to be additive?

6. In Figure 4, can the authors provide a broader quantitative analysis of attention redistribution across many samples and layers, rather than one exemplar plus grouped bars? Without this, the mechanistic claim remains suggestive but not very strong.

7. For the video results in Table 4, why does an aesthetics-oriented modulation direction produce the largest gain in dynamic degree? A more explicit hypothesis, or an ablation showing which component of the prompt pair is responsible, would help.

8. Since Table 1 suggests pooled CLIP matters more on short prompts for FLUX schnell, did the authors try conditioning the guidance strength \(w\) on prompt length or text-encoder entropy? That seems like a natural extension and could further support the core analysis.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper improves controllability and output quality of image and video generative models through a lightweight inference-time guidance mechanism. As with other methods that strengthen generative control, this could lower the barrier to producing deceptive or manipulative synthetic media at higher quality. The paper briefly acknowledges misuse risks in Appendix K, which is appropriate, and I do not see any immediate compliance or human-subject red flags beyond the standard risks associated with more capable media generation. I do not view this as a reason to reject the work, but it is worth flagging.

## Soundness Rating
3: good. The central empirical claims are mostly supported, and the method is technically straightforward, but several claims are framed more strongly than the evidence warrants, and key experimental details remain underspecified.

## Presentation Rating
3: good. The paper is generally well written and easy to follow, with useful figures and broad experimental coverage, though some notation and main-paper methodological details should be tightened.

## Contribution Rating
3: good. The contribution is useful and practically relevant, especially as a simple inference-time steering mechanism, but it is more modest and more heuristic than the framing sometimes suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
This is a useful and well-executed practical paper with a clear message, decent evidence, and broad applicability. My hesitation comes from the fact that the strongest claims about interpretability, mechanism, and generality are not fully nailed down, and the prompt-faithfulness trade-off needs more serious treatment. Still, the core idea is simple, actionable, and likely valuable to the community, so I lean positive.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. It is unlikely, but not impossible, that I missed some nuance in the conditioning details or related implementation choices.