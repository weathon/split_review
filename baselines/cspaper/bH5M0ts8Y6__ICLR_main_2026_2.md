---
job_id: 4a5a3dfe-9a66-4d88-94b6-26275eae45de
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: bH5M0ts8Y6.pdf
paper: VINCIE: Unlocking In-Context Image Editing From Video
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, centering on generative modeling, representation learning for vision, multimodal learning, and a new benchmark for in-context image editing.

## Minimum Quality
Pass ✅. The paper contains the expected components, including abstract, introduction, related work, methodology, experiments, quantitative and qualitative results, and conclusion; despite some clarity and evaluation issues, it presents a coherent technical contribution with substantial empirical evidence.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect any hidden instructions, suspicious prompt-injection content, or manipulative text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies whether an in-context image editing model can be learned purely from native video data, without using standalone image-editing pairs during pretraining. The authors propose a pipeline that converts videos into interleaved multimodal sequences of sampled frames, transition text, and segmentation masks, then train a DiT-based model with three proxy tasks, next-image prediction, current segmentation prediction, and next-segmentation prediction. The paper also introduces MSE-Bench, a 5-turn image editing benchmark, and reports strong multi-turn editing results together with qualitative demonstrations on composition, storytelling, and chain-of-editing.

## Strengths
1. The paper tackles a timely and meaningful problem. Learning in-context image editing from video, instead of relying entirely on curated before/after image pairs, is a sensible and important direction. The central idea, treating videos as naturally occurring edit trajectories, is compelling and reasonably well motivated in Sections 1 and 3.

2. The data construction pipeline is one of the stronger parts of the paper. **Figure 2** gives a concrete, easy-to-follow overview of how videos are transformed into training sessions with frames, transition text, and RoE masks. This figure materially helps the reader understand the full pipeline, especially the role of VLM annotation and GroundingDINO+SAM2 in turning native video transitions into editing supervision.

3. The model framing is coherent. The combination of next-image prediction with segmentation-related proxy tasks is a plausible way to force the model to represent both “what changes” and “where it changes.” **Figure 3** is effective in illustrating how NIP, CSP, and NSP are jointly embedded into a single multimodal diffusion-transformer training setup. Even though some objective details are underspecified, the overall design is conceptually clean.

4. The empirical results on multi-turn editing are strong enough to matter. In **Table 1**, the 7B + SFT model is competitive with or better than many open baselines on MagicBrush multi-turn metrics, especially on later turns where consistency degradation usually becomes severe. In **Table 2**, the gains on MSE-Bench are more notable: the proposed method substantially outperforms most academic baselines at turn-5, which is the regime where long-horizon consistency actually becomes hard.

5. The paper does a good job showing that context matters in this setting. **Table 4** is particularly useful because it isolates the benefit of adding context, dummy context, or turn history. This table is not flashy, but it is scientifically valuable because it supports the core thesis that multi-turn image editing is not just “single-turn editing repeated several times.”

6. The scalability story is convincing at a high level. **Figure 5** shows a fairly clear trend that later-turn success continues to improve with more video sessions, even when turn-1 begins to saturate. That is exactly the kind of result one would want if the paper’s main selling point is scalability through native video data.

7. Some qualitative analyses are genuinely informative rather than decorative. **Figure 6** supports the claim that in-context conditioning mitigates artifact accumulation compared with sequential single-turn editing, and **Figure 7** provides an intuitive example of why segmentation-first inference can reduce subject drift. These figures directly reinforce the paper’s mechanism-level claims, rather than merely showcasing cherry-picked pretty samples.

8. The proposed benchmark is potentially useful. A 5-turn benchmark with more realistic categories than MagicBrush is a welcome addition, and **Figure 4** usefully summarizes the category distribution of MSE-Bench.

## Weaknesses
1. The headline claim, “learned solely from videos,” is somewhat overstated relative to the actual supervision pipeline. The visual modality indeed comes from native videos, but the construction pipeline in **Section 3.1** and **Figure 2** depends heavily on external expert models, an in-house VLM for transition annotation, and GroundingDINO+SAM2 for region extraction. This matters because the paper rhetorically contrasts itself with prior editing-data curation pipelines, yet in practice it introduces another fairly heavyweight annotation stack. The distinction is still meaningful, but the paper should be more precise: this is not “raw videos in, model out,” it is “videos plus substantial machine-generated supervision.” That affects both the claimed simplicity and the true scalability bottleneck.

2. The mathematical formulation is too loose in several places, and the main training objective is underspecified. In **Equation (1)**, the paper writes
\[
\log p(S)=\sum_{i=1}^{M}\log p\!\left(I_i \mid I_0,\dots,T_{i-1},I_{i-1}\right),
\]
but this is not the actual optimized likelihood in the diffusion/flow-matching model. The text says the conditional is “modeled using flow-matching in latent space,” yet no explicit training loss is written. For a paper whose main contribution is a new multimodal training setup, I would expect at least a concrete objective of the form
\[
\mathcal{L}_{\text{FM}}=\mathbb{E}_{t,x_0,\epsilon}\big[\|v_\theta(x_t,c,t)-v^\star(x_t,x_0,t)\|_2^2\big],
\]
or the exact parameterization actually used. Likewise, **Equation (2)** is not a clean probabilistic factorization. It introduces dropout operators directly inside a log-probability expression,
\[
\log p(S)=\sum_{i=1}^{M}\log p(F_i\mid Rd(\cdot),Rd(\cdot),\dots),
\]
but does not define the sampling distribution of \(Rd\), whether dropout is independent across turns/modalities, or whether the expectation over dropout masks is part of the objective. This is not just a stylistic issue. Without a precise objective, it is difficult to reason about what is optimized, what ablations correspond to, and how much of the gains come from the task design versus regularization choices.

3. The notation around the sequence representation is inconsistent enough to create avoidable confusion. In **Section 3.1**, the interleaved sample is written as \((I_0,T_0,T_{m0},M_{00},T_{m1},M_{01},I_1,\ldots,I_K)\), while in **Section 3.2** the sequence is redefined as \(S=(I_0,T_0,\dots,T_{M-1},I_M)\) where \(I_i\) may represent either an image or a segmentation mask. This overloading of \(I_i\) for both images and masks blurs the modality boundaries exactly where the paper is trying to emphasize multimodal structure. In addition, the indexing changes from \(K\) to \(M\), and the special mask prompts \(T_{m0}, T_{m1}\) disappear into the abstraction. This matters because the paper’s novelty partly lies in interleaving modalities, yet the formal description of that interleaving is not stable enough for precise reproduction.

4. The ablation evidence for the three proxy tasks is useful but still not sufficiently disentangled. **Table 3** mixes training-time segmentation usage and inference-time chain-of-editing variants, making it hard to isolate the marginal effect of CSP vs NSP vs simply adding structured intermediate supervision. For example, the paper claims in Section 3.3 that the model jointly learns grounding, controllable generation, and multi-concept composition through random context compositions, but the main paper does not provide a clean ablation of NIP-only, NIP+CSP, NIP+NSP, and NIP+CSP+NSP under matched inference settings and training budget. This matters because the paper’s methodological contribution is not just “use video data,” it is also “use these three proxy tasks,” and the evidence for each task’s necessity is still partial.

5. The benchmark contribution is promising but not yet fully convincing as a community standard. MSE-Bench contains only 100 test instances in the main paper, and its evaluation relies primarily on GPT-4o judgments, as described in **Section 4.2** and Appendix C.6. I appreciate that the paper includes some human validation in the appendix, but in the main paper the benchmark is still relatively small and the evaluation protocol depends on a proprietary VLM judge. This matters because several claims in **Table 2** hinge on small differences among strong models, and judge sensitivity can meaningfully affect rankings in instruction-following tasks. A stronger benchmark section would have included either more examples, dual-annotator human evaluation in the main text, or at least a more careful discussion of evaluation noise and calibration.

6. The comparisons are a bit difficult to interpret because the training regimes are heterogeneous. In **Table 1** and **Table 2**, the paper compares against open and proprietary systems, some using full context and some not, while the proposed method is reported both before and after SFT. This is useful for breadth, but it also muddies the core claim. The fairest scientific question is whether video-derived pretraining alone provides a strong advantage, yet the strongest numbers rely on “Ours + SFT.” **Table 5** partly addresses this by comparing pairwise vs sequence vs sequence→pairwise, and that table is actually one of the most informative in the paper. I wish the paper leaned more on this controlled comparison and less on broad leaderboard-style comparison, because the latter makes it harder to isolate what is gained specifically from video sequence learning.

7. Some central claims are stronger than the provided evidence. For instance, the abstract and conclusion suggest “state-of-the-art results on two multi-turn image editing benchmarks,” but **Table 2** shows that the method still trails several proprietary models by a sizeable margin on MSE-Bench, and **Table 1** is more mixed depending on metric and whether SFT is included. Similarly, terms like “universal in-context editing and generation abilities” around **Figure 1** feel too ambitious for the current evidence, which is largely qualitative for composition, storytelling, and chain-of-editing. These capabilities are interesting, but they are not yet established with the same rigor as the multi-turn editing results.

8. Presentation quality is uneven. There are multiple wording issues and duplicated implementation details in **Section 4.1** on **Page 6**, including repeated sentences about collecting 10M sessions and repeated inference settings. There are also small inconsistencies like “Trun-3” in **Table 1**, mixed naming of OmniGen citations, and some awkward passages in **Section 4.4** around the description of Table 4. None of this is fatal, but for a paper with a complex multimodal pipeline, these lapses make an already dense manuscript harder to audit carefully.

9. The ethics section is brief relative to the scale and source of the training data. The appendix says the training videos come from “stock footage, films, documentaries, etc.” in **Appendix C.1**, but the main paper does not explain licensing, opt-out, or filtering beyond logos/borders/aesthetic estimation. For a web-scale video-derived dataset used to train an editing system with obvious misuse potential, that omission is important.

## Questions
1. Please clarify the exact training objective in mathematically explicit form. What is the precise flow-matching loss used for NIP, CSP, and NSP? How is the target velocity/noise defined, and how is the expectation over the random context-drop operator \(Rd\) implemented? A clean equation here would substantially improve confidence in the method.

2. Can the authors provide a more controlled ablation isolating the contribution of each proxy task under matched training budget and matched inference protocol, for example: NIP only, NIP+CSP, NIP+NSP, and NIP+CSP+NSP? Right now **Table 3** is suggestive, but not fully diagnostic.

3. In **Equation (2)** and **Section 4.1**, context dropout rates are given for current frame / current RoE / next RoE. Is dropout applied independently per turn and per modality token block, or per whole condition? Also, what context is guaranteed to remain for each task target \(F_i\)? This is important for reproducibility.

4. The benchmark would be more convincing with a stronger reliability story. Can the authors report, in the main rebuttal, judge agreement or variance estimates for GPT-4o evaluation on MSE-Bench, and ideally show whether the relative ranking among the main open models is stable under a small human-evaluated subset?

5. On **Table 5**, the “sequence” versus “pairwise” comparison is one of the most important results in the paper. Could the authors clarify whether these runs use the same total number of optimization steps, same model initialization, and same amount of image exposure? If yes, that should be emphasized more strongly because it isolates the benefit of video sequence data quite well.

6. The paper states that full attention and block-wise causal attention are both designed, but the main results overwhelmingly use the former, while Appendix **Table 10** suggests block-causal performs worse. What is the intended scientific takeaway here? Is block-causal primarily a future-looking engineering variant, or is there a setting where it is already competitive?

7. For the “learned solely from videos” framing, can the authors quantify the annotation cost and throughput of the VLM + GroundingDINO + SAM2 pipeline? It would help readers assess how scalable the approach is in practice, not just in principle.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper trains on large-scale video data and states in **Appendix C.1** that the source videos include stock footage, films, and documentaries. That raises legal and licensing questions that are not addressed in the main paper, especially around copyright, terms of use, and whether training data release is possible or appropriate. The method is also an image editing system designed to preserve identity and scene consistency across multiple turns, which has clear misuse potential for deceptive or manipulative media generation, as the authors themselves briefly acknowledge in the Ethics Statement on **Page 10**. Finally, privacy concerns arise if videos contain identifiable individuals and are mined into training sessions with fine-grained transition annotations and masks.

## Soundness Rating
3: good. The core methodology is plausible and the empirical evidence is substantial, but the mathematical specification of the objective and some ablations are not crisp enough for a higher score.

## Presentation Rating
2: fair. The paper is readable and the figures are often helpful, but the exposition has several notation inconsistencies, duplicated text, and some overclaiming that reduce clarity.

## Contribution Rating
3: good. The idea of learning in-context image editing from video-derived multimodal sequences is meaningful and the results are valuable to the community, even though some claims are broader than the current evidence supports.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a real contribution, especially in problem formulation, scalable video-derived supervision, and multi-turn editing results. I am positive overall, but only narrowly, because the objective is underspecified, the ablations do not fully isolate the proposed components, and the benchmark/evaluation setup still leaves some calibration questions.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I carefully checked the main technical formulation, figures, and tables, but some implementation specifics remain underspecified in the paper.