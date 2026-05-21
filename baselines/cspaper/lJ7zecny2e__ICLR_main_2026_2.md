---
job_id: 22027fdc-8298-4d7f-9a43-3e160b283b9c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: lJ7zecny2e.pdf
paper: Towards Faithful Reasoning in Remote Sensing: A Perceptually-Grounded GeoSpatial Chain-of-Thought for Vision-Language Models
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies vision-language modeling, multimodal reasoning, supervised fine-tuning, reinforcement learning, grounding, and benchmark/dataset construction for remote sensing.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments, quantitative and qualitative results, and conclusion; despite notable clarity issues and some underspecified methodological details, it presents a sufficiently complete ML contribution rather than a thin technical report.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-directed instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes Geo-CoT, a perceptually grounded chain-of-thought framework for remote sensing vision-language models, together with a large supervised dataset, Geo-CoT380k, and a two-stage training procedure consisting of supervised fine-tuning followed by GRPO. The resulting model, RSThinker, is evaluated on multiple remote sensing tasks including visual grounding, object counting, object detection, scene classification, captioning, and VQA, with the goal of improving both performance and the verifiability of intermediate reasoning.

## Strengths
The paper targets a real and important problem in remote sensing VLMs, namely that high-stakes geospatial predictions are often hard to verify when models operate as opaque image-to-text systems. Framing the contribution around perceptual grounding, rather than generic textual CoT, is a sensible direction for this domain.

The empirical scope is broad. The paper evaluates across several task families, and the gains are often large. In particular, **Table 4** shows a striking improvement on visual grounding, where RSThinker substantially outperforms both generic VLMs and remote sensing VLM baselines across in-domain and zero-shot settings. If these numbers hold under the same evaluation protocol, this is strong evidence that the proposed training recipe materially improves localization-heavy reasoning, which is the paper’s central claim.

The ablation in **Table 8** is also useful. It does not fully isolate all claims, but it does show that plain SFT helps a lot, CoT-style SFT helps more, and SFT with CoT plus GRPO tends to be strongest overall. That pattern is at least directionally consistent with the paper’s narrative that structure must be learned before RL can refine it.

The qualitative framing is effective in parts. **Figure 2** clearly communicates the intended division of labor between SFT and GRPO, and this helps the reader understand the method at a high level. I also appreciated that the paper includes a failure case in **Figure 7** rather than only cherry-picked successes. That figure makes a fair point: explicit grounding can make an error easier to audit, even when the answer is wrong.

The paper is ambitious in bringing together dataset construction, model alignment, and multi-task evaluation. Even if some pieces are adapted from existing VLM training practice, the overall packaging for remote sensing is reasonably coherent and practically relevant.

## Weaknesses
1. **The central claim is “faithful reasoning,” but the paper mostly demonstrates better task performance and more legible rationales, not faithfulness in a strong scientific sense.**  
   This is the biggest issue. Across the paper, “faithful,” “verifiable,” and “grounded” are used as if they are nearly interchangeable, but they are not. Producing a localized rationale is not the same as showing that the rationale causally supports the answer. The experimental section does not contain a dedicated faithfulness evaluation, such as perturbation tests, rationale-answer consistency checks, intervention studies, or human verification rates for the grounding trace.  
   This matters because the paper’s headline contribution is not just accuracy, it is the claim that RSThinker reasons more faithfully. **Figure 5** is presented as a faithful Planning-Grounding-Synthesis example, but it is still only a single model-generated explanation paired with a correct answer. A plausible trace can be post hoc. **Figure 7** actually hints at this problem: the reasoning chain remains “structurally sound” while the grounded evidence is wrong. That undermines the stronger rhetoric around faithfulness, and the paper should narrow the claim to “auditable grounded rationales” unless it can provide direct evidence for faithfulness.

2. **The contribution of perceptual grounding is not cleanly isolated from ordinary domain adaptation and task supervision.**  
   The strongest ablation, **Table 8**, compares base model, SFT without CoT, SFT with CoT, and then GRPO variants. This is helpful, but it still does not separate several confounded factors:  
   - more supervision versus different supervision format,  
   - remote-sensing-specific task tuning versus grounding-specific supervision,  
   - chain-of-thought structure versus explicit spatial evidence.  
   For example, “+SFT (w/o CoT)” versus “+SFT (w/ CoT)” suggests CoT helps, but I cannot tell whether the gain comes from step-by-step decomposition, from explicit box references, from longer targets, or simply from a higher-quality annotation distribution. Since the main conceptual pitch is perceptual grounding, a stronger ablation would compare text-only CoT against grounded CoT with matched training volume and tasks. Without that, the paper over-attributes the gains to the grounding principle itself.

3. **The GRPO formulation and reward design are underspecified, and in places mathematically inconsistent or at least sloppy enough to reduce confidence.**  
   The policy objective in **Equation (3)** is not written carefully. The token ratio is defined as  
   \[
   r_{t,i}(\theta)=\frac{\pi_\theta(o_{i,t}\mid q,o_{i,<t})}{\pi_{\theta_{\text{old}}}(o_{i,t}\mid q,o_{i,<t})},
   \]
   but the conditioning should include the image and presumably the question consistently, i.e. \((I,Q)\), not just \(q\). This looks minor, but in a multimodal paper the conditioning variables matter.  
   More importantly, the paper says GRPO refines “faithfulness via outcome-based reinforcement learning,” yet the rewards in **Table 3** are almost entirely final-answer rewards, such as IoU, mAP, MAE-derived counting reward, and caption metrics. These are task rewards, not rationale rewards. There is no term that directly rewards the correctness of the intermediate grounded trace. So the optimization target in Equation (3) is aligned to output quality, not faithfulness of the chain itself. That is a substantive mismatch between method and claim.  
   There is also insufficient detail on several implementation choices required to assess stability and fairness: group size \(k\), clipping parameter \(\epsilon\), KL coefficient \(\beta\), how partial correctness is operationalized for VQA/classification, how mAP reward is computed for free-form generative outputs in detection, and whether rewards are dense or sequence-terminal only. These omissions matter because small reward-design choices can dominate RL behavior in multimodal generation.

4. **The dataset construction pipeline is interesting, but its scientific reliability is not adequately audited in the main paper.**  
   Section 3.2 states that Geo-CoT380k is produced using GPT-4V under strict conditioning with bounding boxes, captions, and exemplars. That may reduce hallucination risk, but it does not guarantee quality. The paper does not provide a manual audit of rationale correctness, diversity, or error modes. Nor does it quantify how often generated rationales omit objects, inject unsupported statements, or simply paraphrase the provided answer and auxiliary signals.  
   This matters because the entire method depends on the SFT stage “instilling cognitive architecture” from these generated traces. If the traces are formulaic or weakly faithful, the model may learn a stylistic template rather than a genuine evidence-grounded reasoning policy. The authors briefly acknowledge possible stylistic bias in the conclusion, but that is too light relative to how central this dataset is.

5. **Some reported empirical results are unusually large relative to baselines, but the paper does not do enough in the main text to rule out evaluation or protocol mismatches.**  
   On several tasks, the gains are dramatic. For instance, in **Table 4**, RSThinker jumps to 93.1 @0.5 and 89.02 mIoU on DIOR-RSVG, far above all listed baselines. In **Figure 3** and Appendix **Table 10**, detection performance is also far ahead of existing VLM baselines. I am not saying the results are wrong, but when the margins are this large, the paper should proactively clarify whether all models were prompted identically, whether proprietary systems were allowed tool use, how outputs were parsed into boxes, and whether any task-specific post-processing was used for RSThinker but not for others.  
   The same concern appears in **Table 5**, where counting MAE drops sharply on HRRSD and NNPC-VHR. These gains may be real, but the paper needs more methodological transparency in the main text, because remote sensing tasks are extremely sensitive to prompting, resizing, tiling, and answer parsing. Right now, the numbers are impressive but a bit too convenient.

6. **Presentation quality is uneven, and there are many textual and formatting issues that obstruct technical confidence.**  
   This paper has stronger ideas than execution at the writing level. There are multiple malformed tags and corrupted outputs around **Pages 9–10**, such as repeated `<think>` / `<answer>` fragments and broken closing tags. Several qualitative traces contain clear wording errors, for example “Syndrome” in **Figure 5** where “Synthesis” is presumably intended, and “Hyathesis” in **Figure 6/7**. The captioning metric footer in **Table 7** says “B-4/MT/Cv: BLEU-4/METEOR/CIDEs,” which is clearly inconsistent. Appendix figures also contain answer-coordinate mismatches, for example in **Figure 8** the text discusses a dam but the reported answer appears to repeat the pond coordinates.  
   These are not just cosmetic nits. When a paper asks readers to trust a structured reasoning format and a multi-stage RL pipeline, sloppy formatting makes it harder to tell which parts were carefully validated and which were not.

7. **Several key methodological choices are deferred out of the main paper, leaving the main contribution under-specified.**  
   The paper repeatedly says critical details are in the appendix, including full benchmark details, training hyperparameters, prompt construction, and dataset pipeline details. For a method paper centered on a new training recipe, too much of the recipe is implicit in the main text. For example, object detection as autoregressive text generation is nontrivial, but the main paper never clearly specifies output serialization, box normalization convention, or how duplicate boxes are handled during evaluation. Similarly, the Geo-CoT format is described abstractly, but there is no concise formal schema in the main paper for what constitutes a valid grounded step.  
   This matters because the paper’s reproducibility and interpretability claims depend on exactly these design choices.

8. **The paper’s positioning against prior reasoning-with-RL work is somewhat overstated.**  
   The paper claims to be the first to propose such a framework for Earth Observation, but much of the training recipe, namely CoT-style SFT followed by GRPO-like RL, is now a broader pattern in multimodal reasoning. The domain adaptation to remote sensing may still be worthwhile, but the paper should be more precise about what is first: large-scale remote sensing grounded rationale data, the specific Planning-Grounding-Synthesis format, or the multi-task integration. As written, the novelty framing blurs domain novelty with methodological novelty.

## Questions
1. The main claim is improved faithfulness. Can the authors provide a direct faithfulness evaluation, not just task accuracy, for example: human verification of whether grounded steps actually support the answer, or intervention tests where removing cited evidence harms the answer more than removing uncited evidence? A response here could materially increase my confidence.

2. In **Equation (3)** and **Table 3**, what exactly is rewarded during GRPO: only final answer quality, or also format validity / grounding correctness? If only the final answer is rewarded, why is it appropriate to describe GRPO as refining “faithfulness” rather than simply task performance?

3. For the ablation in **Table 8**, can the authors disentangle text-only CoT from explicitly grounded CoT? A matched comparison between ungrounded CoT and grounded CoT would help isolate the specific value of perceptual grounding.

4. How were outputs parsed into boxes for visual grounding and detection for all compared models in **Table 4** and **Figure 3**? Were prompts standardized across baselines, and was any model-specific post-processing used? A precise answer is important given the very large margins.

5. What quality control was performed on Geo-CoT380k? Even a small manual audit table reporting rationale correctness, omission rate, and unsupported statement rate would strengthen the paper substantially.

6. Please clarify the missing RL details in the main paper: group size \(k\), clipping parameter \(\epsilon\), KL coefficient \(\beta\), reward normalization edge cases when \(\mathrm{std}(\mathcal{R}) \approx 0\), and how “partially correct” answers are defined for VQA/classification.

7. Can the authors confirm that no validation or test data were used in reward design, model selection, or prompt tuning for the reported evaluations? The paper does not raise a red flag here, but an explicit statement would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
N/A.

## Soundness Rating
3: good. The paper is technically plausible and supported by broad experiments, but the central “faithfulness” claim is only partially substantiated, and the GRPO/reward formulation is under-specified in important ways.

## Presentation Rating
2: fair. The paper is readable at a high level, and some figures such as **Figure 2** help, but numerous notation gaps, formatting issues, malformed qualitative outputs, and deferred implementation details weaken the presentation substantially.

## Contribution Rating
3: good. The combination of a remote-sensing grounded CoT dataset, a two-stage SFT+GRPO pipeline, and strong multi-task results is a meaningful contribution for the geospatial VLM community, even though the novelty is partly in domain adaptation and the faithfulness claim is stronger than the current evidence supports.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
The paper addresses an important problem, presents a reasonably coherent framework, and reports strong empirical gains across multiple remote sensing tasks. However, the paper oversells faithfulness relative to the evidence, under-specifies key parts of the RL and dataset pipeline, and needs cleaner ablations to isolate grounding from generic CoT/task tuning.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main technical and empirical claims carefully, though some implementation details are missing from the main paper and limit full verification.