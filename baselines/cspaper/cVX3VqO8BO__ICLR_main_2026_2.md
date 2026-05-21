---
job_id: 4eeeb736-3073-42d5-b012-e5fd80744af1
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: cVX3VqO8BO.pdf
paper: UniHM: Unified Dexterous Hand Manipulation With Vision Language Model
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ The paper is clearly within ICLR scope, combining representation learning, generative modeling, vision-language-action modeling, and robotics/manipulation.

## Minimum Quality
Pass ✅ The submission contains the required scientific components, including abstract, introduction, related work, method, experiments, quantitative results, and conclusion. While there are notable clarity and evaluation issues, the paper presents a complete research contribution rather than an incomplete or obviously invalid submission.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes UniHM, a framework for language-conditioned dexterous hand manipulation that combines three main components: a morphology-agnostic VQ tokenizer shared across different hand embodiments, a vision-language model that predicts manipulation token sequences from RGB-D inputs and free-form instructions, and a physics-guided refinement stage for improving physical feasibility. The system is trained primarily from human-object interaction data retargeted to multiple robot hands, and is evaluated on DexYCB, OakInk, and a small set of real-world tasks.

## Strengths
The paper addresses a relevant and difficult problem, namely moving beyond static dexterous grasp prediction toward instruction-conditioned sequential dexterous manipulation. That problem framing is meaningful for the ICLR community, especially at the intersection of representation learning and robotics.

The overall system design is coherent. The three-stage pipeline in **Figure 2** is one of the clearer parts of the paper, and it helps explain how the proposed tokenizer, VLM, and physical refinement interact. In particular, the figure makes the intended modularity of the method easy to understand, namely, shared tokenization across hands, language-conditioned sequence generation, and post-hoc optimization for feasibility. I appreciated that the paper does not just claim “unified manipulation” at a high level, but actually provides a concrete architecture for it.

The morphology-agnostic tokenization idea is interesting. The formulation in **Equations (1) to (6)** gives a plausible way to map heterogeneous hand trajectories into a shared discrete code space while allowing hand-specific decoding. Even though I have concerns about how strongly the paper validates this claim, the representation-level idea itself is sensible and potentially useful.

The physical refinement component is better specified than many robotics papers of this type. **Equations (11) to (18)** provide an explicit energy with contact, generative, and temporal terms, and the Gauss-Newton update in **Equation (17)** is at least operationally clear. This is one of the more technically grounded parts of the paper.

The empirical results are generally strong. In **Table 1** and **Table 2**, the method improves substantially over the listed baselines on MPJPE, FOL, FPL, and FID, on both seen and unseen settings. On DexYCB, for example, the gain over MotionGPT3 in FPL is especially large, and the same pattern largely holds on OakInk. Even if some baseline choices are debatable, the reported margins are not tiny.

The ablation in **Table 4** is useful and supports that depth input, masked training, and physical refinement each matter. Among these, the “w/o Physical Refinement” row is particularly important because it suggests that the optimization stage contributes more than a cosmetic post-processing effect.

The paper also includes some real-world evidence. **Table 3** and **Figure 3** suggest the method can transfer beyond offline benchmark evaluation. Figure 3 is visually aligned with the paper’s central claim, namely, that the generated behaviors are not just static end poses but executable interaction sequences such as grab, open/close, and pull/push.

## Weaknesses
1. **The central “unified across morphologies” claim is under-validated in the main paper.**  
The paper repeatedly emphasizes cross-hand consistency and transfer, especially in **Section 3.2** and the contribution bullet “Morphology-Agnostic Codebook” on **Page 2**, but the main experimental section does not actually provide a direct quantitative evaluation of cross-morphology transfer. I see standard benchmark tables on DexYCB and OakInk, plus generic real-world success rates, but I do not see a controlled experiment of the form: train on a subset of hand embodiments, test on held-out embodiments, or translate the same token sequence across hands and measure fidelity/executability. This matters because the tokenizer is not a side detail, it is one of the paper’s headline contributions. Without an explicit cross-embodiment study in the main paper, the strongest claim of the method is supported more by architecture description than by evidence.

2. **The evaluation setup conflates the generator and the refinement module, making attribution difficult.**  
In **Section 4.3**, the authors state that prior baselines are post-processed with the proposed physics-guided refinement for fairness. That is understandable, but the presented results in **Table 1** and **Table 2** still mix two sources of gain: better sequence generation and stronger post-hoc optimization. The problem is that the paper’s own method also includes refinement, so the reader cannot cleanly assess how much of the improvement comes from the VLM/tokenizer versus the optimizer. The ablation in **Table 4** helps partially, but it is only for the proposed model on DexYCB, not a broader decomposition across methods and datasets. This matters scientifically because the paper claims advances in unified language-conditioned generation, but the reported benchmark lead may be substantially driven by the optimization back-end.

3. **Several experimental choices and baselines are not well matched to the task, weakening the novelty positioning.**  
The main baselines in **Table 1** and **Table 2**, namely TM2T, MDM, FlowMDM, and MotionGPT3, are primarily generic motion generation models rather than dexterous manipulation systems with explicit embodiment handling, contact modeling, or point-cloud conditioning. The paper mentions more directly related dexterous grasp/manipulation works in the related work section, but none appear in the main comparison tables. If the paper’s goal is unified dexterous manipulation under language guidance, then comparing mostly against general motion generators makes the empirical story look stronger than it may be. This matters because performance gains are easier to obtain when the baseline class is mismatched to the structure of the task.

4. **The method description around the VLM is underspecified at critical points.**  
In **Equation (9)**, the model is written as  
\[
\hat{Q}_{pos}=D_h(\mathrm{VLM}(E_j(Qpos_0), \mathcal{T}_{tar}, \mathcal{P}_{obj}, \mathcal{T})).
\]
But the paper does not clearly define the sequence prediction objective for the VLM itself. Is it next-token cross-entropy over code indices, masked token reconstruction, autoregressive decoding, or a mixture of these? **Equation (10)** defines a masking mechanism, but not the actual loss used to train the generator. Also, the notation alternates between hand poses, q-positions, tokens, and encoded chunks in a way that is hard to follow across **Sections 3.2 and 3.3**. This is not a minor exposition issue, because it makes reproduction and scientific interpretation much harder. If the central learner is a token-sequence model, the token-level training objective should be explicit.

5. **There are mathematical inconsistencies and sloppy notation in the refinement section and appendix, which reduce confidence.**  
The main text definition of the contact penalty in **Equation (12)** simplifies the outside case to \(\frac{\alpha}{\alpha} d^2 = d^2\), which makes the role of \(\alpha\) asymmetric and somewhat odd. More concerning, the appendix version in **Equation (B16)** appears malformed: the piecewise definition is broken across lines and does not match the cleaner expression in the main text. The paper then claims continuity, matched derivatives, and convexity in **Equation (B17)**, but given the malformed expression in (B16), the reader cannot really verify those claims from the appendix as written. Also, the Jacobian formula in **Equation (B19)** uses a denominator \(2\sqrt{f(d_i(q_t))}+\epsilon^2\), which looks unusual and is not justified. These are not fatal by themselves, but they matter because the optimization module is sold as one of the key technical contributions.

6. **The physical refinement objective is narrower than the prose claims.**  
The text in the ablation discussion on **Page 9** says the optimizer adjusts poses, contacts, and timing to reduce collisions and slips, enforce joint and torque limits, and improve stability. However, the actual main-text objective in **Equations (11) to (16)** contains contact distance, a generator prior, and first/second-order temporal smoothness. I do not see explicit friction-cone terms, torque constraints, collision penalties beyond fingertip-object signed distances, or object dynamics. The conclusion on **Page 10** does acknowledge simplified contact and friction modeling, but the main-body description is still more ambitious than the equations support. This matters because readers may overestimate the physical realism of the optimization based on the prose.

7. **The real-world evaluation is promising but too thin for the strength of the claims.**  
**Table 3** reports success rates on four task families, but key details are missing from the main paper: number of trials per task, object count per category, whether instructions were fixed or paraphrased, and how much manual engineering or failure recovery was involved. **Figure 3** gives qualitative examples and is visually appealing, but it is essentially a collage of successes. It does not show failure cases, comparative trajectories, or evidence that the language grounding rather than task-specific priors drives performance. Since the paper emphasizes “open-world tasks in real-world interactions” in **Figure 1** and the introduction, a more rigorous real-world section is needed.

8. **The “generalization without teleoperation” claim is somewhat overstated.**  
The title and abstract emphasize learning solely from human-object interaction data and eliminating massive teleoperation datasets. But the method still relies on retargeting those human sequences to robot hands, on object trajectories used during training, and at inference on a CLIPort-based planner plus object segmentation and point-cloud reconstruction. So the burden is shifted rather than removed. I do think the data source is different from conventional teleoperation, but the wording in the abstract and contributions on **Pages 1 to 2** is stronger than what the pipeline actually demonstrates.

9. **The diversity metric reveals a potentially uncomfortable trade-off that the paper does not analyze.**  
In **Table 1** and **Table 2**, the proposed method often has much lower Diversity than strong baselines, and also lower than ground truth by a substantial margin. For example, on DexYCB seen, the proposed method’s diversity is \(39.62\) versus GT \(125.53\), while MotionGPT3 reaches \(72.51\). On OakInk seen, the proposed method is \(165.47\) versus GT \(147.40\), but several other settings show large gaps. The text says “closer to the GT” is better, which is fair, but the paper never discusses whether the combination of codebook discretization, masked training, and refinement is collapsing the motion space toward safer but less expressive solutions. This matters because one of the motivations is open-vocabulary and compositional dexterous manipulation, which should ideally not come at the cost of severe mode reduction.

10. **Presentation quality is inconsistent and occasionally sloppy.**  
There are many grammatical issues, capitalization inconsistencies, and notation mismatches, for example “UNIFIED HAND-DEXTEROUSTOKENIZER” in the section heading on **Page 4**, inconsistent use of \(P_{\text{obj}}\) versus \(\mathcal{P}_{\text{obj}}\) in **Page 5**, and several awkward or exaggerated claims in **Section 4.3** such as “unequivocally affirm” and “cutting-edge.” These may sound cosmetic, but they affect trust, especially in a paper that already asks the reader to bridge many missing implementation details.

## Questions
1. The strongest contribution appears to be the shared tokenizer across hand morphologies. Can the authors provide a direct main-paper style experiment isolating cross-embodiment transfer, for example training on a subset of hands and testing on a held-out hand, or encoding with hand \(i\) and decoding with hand \(j\) using **Equation (6)**, with quantitative measures of reconstruction quality and execution success?

2. What exactly is the VLM training objective in **Section 3.3**? Please specify whether the model is trained with token-level cross-entropy, masked-token prediction, autoregressive next-token loss, or some hybrid objective, and write the corresponding loss explicitly. This would materially increase confidence in reproducibility.

3. For **Table 1** and **Table 2**, how much of the gain comes from the generator versus the refinement stage? A decomposition such as “raw generator output” and “after refinement” for both the proposed model and baselines would help determine whether the claimed contribution is mainly representational or mainly optimization-based.

4. The appendix expression **(B16)** looks inconsistent with the main-text **Equation (12)**. Can the authors clarify the exact form of \(f(d)\), and confirm the continuity and derivative calculations used to justify the Gauss-Newton procedure?

5. For the real-world results in **Table 3** and **Figure 3**, how many trials were run per task, how were seen/unseen objects defined, and were language instructions paraphrased or templated? A more detailed breakdown, including failures, would significantly strengthen the paper.

6. The diversity numbers in **Tables 1, 2, and 4** suggest a possible realism-versus-coverage trade-off. Do the authors observe that the physics refinement or discrete codebook compresses the motion distribution? A short analysis here could change my view of the method’s generative quality.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the paper itself. The work is a robotics manipulation system evaluated on standard datasets and controlled real-world tasks.

## Soundness Rating
2: fair, the paper has a plausible technical core and meaningful experiments, but several central claims are only partially supported and important parts of the method are underspecified or mathematically inconsistent.

## Presentation Rating
2: fair, the high-level idea is understandable, helped by **Figure 2**, but the paper has notable notation issues, missing training details, and multiple places where the prose overclaims relative to the equations.

## Contribution Rating
3: good, the problem is important and the combination of unified tokenization, language-conditioned sequence generation, and refinement is valuable to share, even though the empirical attribution and validation of the key claims are incomplete.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper tackles an important problem and presents a reasonably compelling integrated system with strong headline results, but the main claimed contribution, namely cross-morphology unification, is not validated as directly as it should be, and the methodological exposition needs tightening.

## Reviewer Confidence
4: confident, I am confident in my assessment, though not absolutely certain. It is unlikely, but not impossible, that I misunderstood some parts or missed some related work.