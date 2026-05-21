---
job_id: 6e126512-2165-4627-b2e6-11b87ffd50d0
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: k6nTUFoqeT.pdf
paper: FASTER: Toward Efficient Autoregressive Vision Language Action Modeling via Neural Action Tokenization
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on representation learning, generative/autoregressive modeling, multimodal learning, and robotics/VLA policies.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, method, experiments, quantitative results, and conclusion; it presents a nontrivial methodological contribution with substantial empirical evaluation, despite several clarity and rigor issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, instructions targeting automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes FASTer, a framework for efficient autoregressive vision-language-action modeling that combines a learned action tokenizer, FASTerVQ, with a block-wise autoregressive policy, FASTerVLA. The tokenizer represents action chunks through a structured residual vector quantization pipeline, while the policy introduces block-wise decoding and a lightweight action expert to reduce inference cost and improve control performance. Experiments span multiple simulated and real-world benchmarks, with comparisons on reconstruction quality, compression, inference speed, and policy success rates.

## Strengths
The paper tackles a real bottleneck in autoregressive VLAs, namely the tension between action-token fidelity and decoding efficiency. This is a worthwhile problem, and the paper presents a reasonably coherent end-to-end answer rather than only a tokenizer or only a policy-side speedup.

The tokenizer design is thoughtfully motivated. The patchification scheme and RVQ-based structured latent space in **Figure 2** make the core intuition quite clear: actions are treated as a 2D object over horizon and action dimensions, then compressed with residual quantization in a coarse-to-fine way. That representation choice is sensible for robot actions, where temporal redundancy and per-dimension heterogeneity are both important.

The empirical scope is strong. The paper evaluates across multiple embodiments, multiple datasets, simulation and real robots, and different VLM backbones. Even if some experimental choices could be better justified, this breadth is a genuine strength and makes the work more useful to the community than a narrow benchmark win.

The main benchmark results are impressive. In **Table 1**, FASTer improves over several strong baselines on both LIBERO and Simpler-Bridge, and the gains are not tiny. In particular, the average on LIBERO improves over both $\pi_0$ and $\pi_{0.1}$, while the Simpler-Bridge average is substantially above prior AR baselines and also above the diffusion/flow-style methods listed there. This gives the paper real empirical weight.

The efficiency story is also supported with concrete measurements. **Table 2** is helpful because it breaks down where runtime goes instead of only reporting a single end-to-end number. The observation that encoder cost dominates while BAR mainly reduces decoding overhead is useful and more honest than pretending all latency comes from token generation. The comparison in the text and **Table 5** also supports the claim that FASTer is especially helpful when token counts would otherwise become very large.

The tokenizer analysis is more thorough than usual for robotics papers. **Figure 5** and **Figure 6** aim to show the trade-off between compression and reconstruction rather than reporting only downstream task success. That is the right axis of analysis for this problem, and it strengthens the case that the tokenizer is not just an incidental engineering detail.

The cross-backbone results are interesting. **Figure 7** suggests that the learned tokenizer transfers across VLM backbones and that much of the gain comes from FASTerVQ itself, not only from BAR. If this holds robustly, that is a useful systems contribution for the VLA community.

## Weaknesses
1. **The paper combines several nontrivial components, but the main paper does not cleanly isolate which component is responsible for which gain.**  
The full system includes non-uniform patchification, a transformer-convolution hybrid tokenizer, RVQ, DCT-domain loss, spacing augmentation, a lightweight action expert, block-wise decoding, and a specific codebook-first decoding order. This is a lot. The main paper claims that FASTerVQ and FASTerVLA each contribute distinct benefits, but the causal attribution is still muddy in the main text. For example, in **Figure 7**, the text says most of the gain comes from the neural VQ tokenizer and BAR adds a smaller gain, but the main paper does not provide a sufficiently systematic decomposition across all settings. The more detailed ablations are pushed largely to the appendix, and some important decisions, such as the DCT loss and the codebook-first decoding order in **Figure 3(b)**, are not directly ablated in the main paper. This matters because a complex stack can look stronger than it really is if the key gain comes from one or two ingredients while the rest mainly add engineering burden.

2. **The mathematical formulation of the tokenizer objective is incomplete and somewhat inconsistent with standard RVQ/VQ training.**  
In **Equation (1)**, the loss includes reconstruction and one commitment-style term, $\lambda \|z-\mathrm{sg}(z_q)\|_2^2$, but there is no explicit codebook loss term of the usual VQ-VAE form, e.g. $\|\mathrm{sg}(z)-z_q\|_2^2$, because the authors instead say the codebooks are updated using EMA. That can be fine, but then the paper should say much more clearly which parts receive gradients, what the EMA update equations are, and how this interacts with residual quantizers and dead-code reinitialization. As written, **Equation (1)** underspecifies the actual training dynamics. Also, the text says the reconstruction is on the patchified action $\mathbf{a}_{t:t+H}^P$, but **Equation (1)** is written using $\mathbf{a}_{t:t+H}$ without the patch superscript, which creates avoidable ambiguity about whether the loss is applied before or after unpatchifying. This is not a fatal error, but it weakens technical clarity right at the core objective.

3. **The BAR objective in Equation (3) is intuitive, but the paper glosses over a nontrivial train-test mismatch.**  
In **Equation (3)**, tokens within a block are predicted conditioned only on previous blocks, not on earlier tokens in the same block. Then the model uses a modified attention mask allowing intra-block attention, and the text says training still uses teacher forcing. These details need a sharper formulation. If intra-block tokens attend to each other during training, then the conditional factorization written in **Equation (3)** is not the usual causal one. If instead the block is jointly predicted from a repeated $\langle \mathrm{BoBlk} \rangle$ token, then the exact input-output alignment and loss indexing should be specified more rigorously. The description around **Figure 3(c)** and the paragraph introducing block masks gives the high-level idea, but not enough detail to verify that the stated objective and the implemented mask are actually consistent. Since BAR is one of the main claimed contributions, this should be tighter.

4. **The novelty relative to recent action-tokenization work is somewhat overstated in places.**  
The paper makes a strong case that existing tokenizers do not satisfy the desired combination of compactness, fidelity, 2D structure, and flexibility, but the actual methodological ingredients are mostly a careful assembly of known ideas: patchification, transformer+conv autoencoding, residual vector quantization, frequency-domain reconstruction loss, and block-wise decoding. I am not saying the paper is derivative, because the combination is well targeted to VLA, but the prose occasionally reads as if the conceptual leap is larger than what is supported. The contribution is strongest as a well-engineered and well-evaluated system for this setting, less as a fundamentally new modeling principle.

5. **Some central empirical claims are supported primarily by custom metrics or by appendix-only evidence, and the main paper does not always give enough calibration.**  
The introduction of VRR in **Equation (4)** is reasonable, but the metric is also somewhat custom and threshold-dependent. The paper argues that $\sigma$ values correspond to meaningful physical tolerances, but those tolerances are not calibrated in the main paper with downstream sensitivity curves or per-task execution analyses. **Figure 5** looks favorable for FASTer, but without stronger linkage from VRR to task success in the main text, this metric remains only partially convincing. Likewise, several claims about generalization across embodiments and action representations rely on **Figure 8** and appendix figures/tables rather than a more comprehensive main-paper quantitative breakdown.

6. **Baseline fairness is not fully transparent, especially where pretraining sources and tokenizer data differ.**  
The paper says in **Section 4.1** that models are initialized from large-scale robotics-pretrained checkpoints, often from $\pi_0$-FAST, but also notes separate settings for Bridge and Droid. Meanwhile, **Table 3** in the appendix shows multiple data mixtures for different FASTerVQ variants. This creates some uncertainty about apples-to-apples comparison. For example, when tokenizer scaling is discussed in **Figure 5**, the comparisons mix different data budgets and different data mixtures. The paper argues that FASTer still wins under smaller or equal budgets, which may be true, but the main paper presentation is not clean enough to make that conclusion easy to audit.

7. **The reported efficiency gains are real, but the practical narrative is a bit selective.**  
The paper emphasizes faster inference, and **Table 2** is useful, but it also shows that the biggest runtime component is observation encoding, not action decoding. In the whole-body setting, the text admits that FASTerVLA and $\pi_0$ have similar runtimes, around $230$ ms. That is important. The stronger claim, then, is not simply “autoregressive VLA becomes fast,” but “the tokenizer prevents AR decoding from becoming catastrophically slow as token count grows.” That is still valuable, but narrower than some headline language suggests.

8. **Presentation quality is mixed, with multiple notational and editorial issues that matter more than they should in a technical paper.**  
There are several awkward phrases and inconsistencies, for example “share structured action expert” on **Page 3**, “follows most VLM structure” on **Page 5**, and symbol inconsistencies across the method section. In **Table 4**, one column is labeled $C_b$ although the method mainly discusses $C_h$ and $C_a$, which is confusing. Some sections reference tables that are only in the appendix or cite “Table 6” in the main paper without much context. These are fixable, but the current draft still feels rough in places.

9. **The codebook-usage analysis is suggestive but not yet fully persuasive as a mechanistic explanation.**  
The paper argues that balanced code utilization leads to stronger performance, using **Table 8** and the discussion in Section 4.3. The statistics are interesting, especially the jump to 100% usage and higher normalized entropy for FASTerVQ, but the causal claim is still loose. High utilization can reflect better expressiveness, but it can also reflect different dataset mixture, codebook size, quantization regularization, or action normalization choices. The paper presents this as an explanation for generalization gains, but it currently reads more as a correlation than a demonstrated mechanism.

10. **The main paper under-discusses failure modes and robustness limits.**  
The experiments emphasize average success and OOD drops, such as in **Figure 9** and **Figure 10**, but there is little qualitative analysis of where FASTer still fails, which tasks are brittle, or whether BAR introduces characteristic failure patterns. Given the paper’s focus on efficient discrete action generation, some discussion of failure cases would help readers understand when the method should or should not be trusted.

## Questions
1. For **Equation (1)**, can the authors explicitly write the full training/update rule for the RVQ tokenizer, including how EMA codebook updates are performed at each residual stage, and clarify whether the reconstruction losses are applied on patchified actions, unpatchified actions, or both? A more precise formulation would increase my confidence in the method section.

2. For **Equation (3)** and **Figure 3(c)**, can the authors describe the exact training-time inputs and attention mask for block-wise decoding? In particular, do tokens inside a block attend to gold tokens from the same block during teacher forcing, or are they predicted jointly from a replicated control token without intra-block teacher forcing? This is important for understanding whether the factorization in Eq. (3) matches the implementation.

3. Can the authors provide a clearer main-paper ablation, not only appendix material, that isolates the contribution of:  
   (i) the DCT loss,  
   (ii) the non-uniform action patchifier,  
   (iii) the action expert, and  
   (iv) the codebook-first decoding order shown in **Figure 3(b)**?  
   Right now, the decomposition of gains is still too implicit.

4. How sensitive are the results to the VRR threshold $\sigma$ in **Equation (4)**, and can the authors better connect VRR to downstream control success? A simple plot relating tokenizer VRR to policy success across several tokenizers/settings would make the metric much more convincing.

5. In **Table 1**, FASTer improves substantially on Simpler-Bridge over prior methods. Can the authors clarify whether all compared methods use matched pretraining data, action representations, and evaluation protocols, especially for the zero-shot settings? A concise fairness statement in the main paper would help.

6. **Table 2** suggests the encoder is the main runtime bottleneck in some settings. Do the authors expect further BAR improvements to matter in practice unless visual encoding is also optimized? It would help to frame more precisely when FASTer’s speed benefits are most consequential.

7. Could the authors include a short discussion of failure cases, especially for the OOD experiments in **Figure 9** and **Figure 10**? Even one figure or paragraph identifying recurrent failure patterns would improve the scientific value.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper is about robotic manipulation policies that can generalize across embodiments and tasks. While this is standard robotics research and I do not see an immediate ethics red flag in the experimental protocol itself, more capable and transferable robot control policies can also be deployed in safety-critical or misuse-prone settings. The ethics statement on **Page 11** is quite minimal and mostly says there are no direct concerns. I do not think this should block publication, but the paper would benefit from a more realistic discussion of deployment risks, especially since the method emphasizes transfer across platforms and efficient inference.

## Soundness Rating
3: good. The paper is technically plausible and supported by broad experiments, but some central methodological details, especially around the tokenizer loss/update rules and BAR factorization, are not specified tightly enough for a higher score.

## Presentation Rating
3: good. The paper is generally understandable and the figures are useful, but the notation and exposition need cleanup, and several important details are either ambiguous or deferred.

## Contribution Rating
3: good. This is a meaningful systems contribution to efficient autoregressive VLA design with solid empirical value, though the conceptual novelty is more in the integration and execution than in a fundamentally new principle.

## Overall Rating
8: Accept, good paper (poster). Despite several technical clarity issues and a somewhat overpacked design, the paper addresses an important problem, presents a credible and practically useful approach, and backs it with unusually broad empirical evidence. I would recommend acceptance, though I would like to see the method section and ablation story tightened.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the relevant VLA/action-tokenization literature, though some implementation details in the paper are underspecified enough that I cannot fully verify every mathematical claim from the main text alone.