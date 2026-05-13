# Early Fusion Helps Vision Language Action Models Generalize Better

- Decision: Reject
- Scores: 6, 3, 1

## Abstract
Recent advances in Vision-Language-Action (VLA) models can enable robots to perform a wide range of tasks based on language or goal-based instructions. These VLA models typically encode text and images into disjoint tokens, generating actions that align with the given instructions. This requires the VLA models to simultaneously perform vision-language understanding and precise closed-loop control, resulting in significant challenges for them to generalize to new environments. However, contrastive pre-trained VLMs, such as CLIP, already possess vision-language alignment capabilities, which are underutilized by current VLA models. In this paper, we propose Early Fusion VLA (EF-VLA), a novel VLA architecture that exploits CLIP’s vision-language understanding by performing early fusion, extracting fine-grained vision-language tokens relevant to the task instructions before passing them to the transformer policy. EF-VLA keeps the
VLM frozen, allowing it to effectively perform unseen tasks without requiring fine-tuning, which often reduces generalization capabilities. Simulation and real-world experiments suggest that EF-VLA outperforms state-of-the-art VLA models on diverse tasks, with significant generalization capabilities in unseen environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper argues against fine-tuning the vision encoder in manipulation policy learning, proposing instead a straightforward yet effective feature fusion method to leverage features extracted by frozen CLIP. This approach preserves the rich alignment capabilities of Vision-Language Models (VLMs) and enables the model to generalize effectively to new environments without extensive vision encoder fine-tuning.

### Strengths
- Clear Motivation and Novel Insight: The paper is well-motivated and clearly written, with a compelling argument for early fusion to decouple the vision-language alignment learning from the manipulation control learning. This insight into separating the two learning tasks highlights a thoughtful approach to using pre-trained VLMs in robotics.
- Simplicity and Effectiveness: A simple fusion method is proposed and the experiments show that it is effective in improving the performance of manipulation policy learning.

### Weaknesses
The depiction in Figure 3 is somewhat confusing. The figure seems intended to represent the calculation of image-attended text features through an analogy to the attention mechanism using the CLIP score. However, with attention equations presented on the same page, it is unclear if the query, key, and value refer to the same elements discussed in the figure. A clearer distinction or separate notation could help alleviate this confusion.

One major weakness is the lack of experimental justification for the fusion method's design choices. While ablation studies demonstrate optimal performance for the current configuration, they do not provide enough insight into *why* the proposed method is effective or how it might inspire further exploration of fusion methods. For instance, the paper does not explore simpler fusion methods like a concatenation or a simple linear layer, nor does it provide a rationale for the specific hyperparameter choices in the cross-attention pooling. This lack of exploration limits the understanding of the proposed method's effectiveness and its potential for broader applicability.

All reviewers, including myself, expressed concerns about the method's scope being limited to CLIP. The proposed method, based on ClearCLIP and tailored for CLIP, may not generalize to other models like SigLIP. The paper does not provide sufficient evidence or discussion on how the proposed fusion method might be adapted or perform with other VLMs that have different architectures and pre-training objectives. This raises concerns about the method's generalizability and impact beyond the specific context of CLIP.

### Questions
- Choice of CLIP Over Other VLMs: Although the paper mentions other Vision-Language Pretrained models like BLIP in lines 122 - 127, it only discusses why fine-tuning CLIP and modifying CLIP is not desirable and does not provide a detailed rationale for not using other VLPs. Beyond CLIP, models such as ALIGN, BEiT, and CoCa offer potentially richer language capabilities. Could the authors elaborate on why they chose to modify CLIP over these alternatives and discuss whether these models might offer additional benefits in manipulation policy learning?
- What is the learnable "cross-attention pooling" in line 225?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel approach, Early Fusion VLA (EF-VLA), which leverages the CLIP model’s capabilities in image-text alignment through early fusion of vision-language (VL) features. EF-VLA differentiates itself by extracting fine-grained VL features early in the process, prior to inputting them into a transformer-based policy network. These fused features are concatenated with attention-pooled text features and embodiment features, forming a comprehensive multi-modal state representation. This representation is subsequently fed into a causal transformer policy for fine-grained action generation. The authors evaluate EF-VLA's performance on a diverse set of tasks within both the LIBERO simulation environment and real-world scenarios. Results demonstrate EF-VLA’s superior performance over several baseline approaches.

### Strengths
1. The paper is well-structured and easy to follow. 

2. The experimental setup is thorough and convincingly demonstrates the effectiveness of EF-VLA. The inclusion of real-world robotic experiments, alongside evaluations on the LIBERO platform, strengthens the validity of the results and highlights the method's practical applicability.

### Weaknesses
1. **Potentially Misleading Title and Incomplete Exploration of Early Fusion**: While the title suggests an exploration of “early fusion,” the fusion approach presented here uses attention at the final layer of the vision encoder before passing features to the downstream transformer-based policy. This choice, although earlier than fusing everything solely within the transformer-based policy, falls short of a deeper fusion study that examines the benefits and trade-offs of fusing features at even shallower layers of the vision encoder. Specifically, the paper does not explore how performance might change if fusion occurred at intermediate layers of the vision encoder, potentially missing opportunities for more effective feature integration. Additionally, while the proposed early fusion method generalizes well to LIBERO and real-world tasks, a broader exploration of early fusion designs across diverse model settings, such as OpenVLA, would strengthen claims about generalizability. The current approach risks being a specific case study rather than a generalizable method.

2. **Missing Ablations on Key Design Choices**: The study lacks critical ablations that could clarify the choices made in EF-VLA’s architecture. For instance, although the authors introduce a learnable pooled text embedding \(f'_l\) in the state representation, there is no equivalent learnable visual embedding (\(f'_v\)) included, and the rationale for this asymmetry remains unexplored. This raises questions about whether the lack of a learnable visual embedding is a principled design choice or an oversight. Additionally, in the LF-VLA configuration, it is unclear why visual and textual tokens are processed through an attention pooling layer to produce final tokens, rather than directly using classification tokens from each encoder, which would be a more straightforward approach. This design choice needs further justification, as using the CLS token is a common practice in transformer models. These omissions leave gaps in understanding the impact of design decisions on model performance.

### Questions
Listed in the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes "Early Fusion VLA" (EF-VLA) to address token fusion from different modalities in a modern vision-language-action model, i.e., a policy network that takes vision-language inputs and predicts robot actions. EF-VLA is motivated by 1. leveraging existing vision-language alignment in pre-trained models (like CLIP) instead of re-learning it at the policy learning stage (late fusion), and 2. providing fine-grained visual features for policy learning. The proposed EF-VLA uses CLIP as the vision encoder and follows the ClearCLIP way to use per-patch features for language alignment. The author evaluates EF-VLA only in a simulated environment and compares it against OCTO and OpenVLA in real-world experiments. The results show that EF-VLA improves.

### Strengths
- Studying early or late fusion is meaningful for robot learning use case. 

- Real-world experiments are highly appreciated.

### Weaknesses
 - The authors claim that VLMs and VLA models using similar architectures are in the late-fusion style (L142-144). However, I hold a different opinion. Let's take examples of LLaVA and OpenVLA. In LLaVA, the visual encoder is CLIP. The visual tokens are generated by CLIP, mapped to language space, and processed by the LLM part. The LLM part is visually very large, for example, 8B, 34B, and even 72B / 110B (recent LLaVA-NeXT). Comparing the LLM parameters to CLIP parameters (~300M for CLIP-ViT-L), the visual tokens still go through many more parameters than the encoder part. OpenVLA uses DINOv2 and SigLIP plus a Llama-7B backbone, in a similar way that many more parameters are used for modality fusion. Therefore, I don't believe it's true that many existing VLMs and VLA models are late-fusion. 

- The presentation is extremely unclear. See some clarification questions below.
  * L176 Eq. (2) What are $X_{res}$ and $X_{attn}$? They are not defined.

  * Is Eq. (1) overloaded in L175 and L212? Also, the equation in L212 does seem to be standard (more like pseudo-code)

  * As this paper follows ClearCLIP, it seems that this paper is directly taking Eq. (1)-(3) from the original ClearCLIP paper, but poorly explains the meaning.

  * What's the cosine similarity in Figure 3? I can not find anything in the main text that describes it.

- What's the reason for using final LN for text features but post-attention LN for visual features? The choice needs justification. Following this, what's the meaning of another L2 normalization descript in L207? Are they referring to the same operation?

- One of the main motivations is to provide dense visual features to policy learning (L84-86). However, the aligned vision-language tokens $f_{vl}$ are further compressed into one token. The compression is done by cross-attention pooling using the original text feature. So 
  1. Why do we need to do the first per-patch alignment and then compress it again? Can't we directly do the final pooling?

  2. The author needs to justify why a single token can provide dense visual features to the policy learning framework, with only light-weight learnable parameters in between (L227)

  3. The cross-attention pooling is not described (L227)

- The real-world evaluation tasks are all pick-and-place tasks. This is a very limited setting. And I'm concerned that the advantage of this model only preserves this limited task scope, which is unfair to other VLA models like OCTO and OpenVLA. 

- Significant architectural difference between EF-VLA and baselines. The policy part of EF-VLA is trained from scratch from my understanding. However, authors use it to compare against fine-tuned OCTO and OpenVLA models. This does not make sense since the model sizes could significantly affect the result given the relatively small amount of real-world data, compared to the large pre-trained set that OCTO and OpenVLA used. EF-VLA's policy head only contains 4 Attention blocks, each with 8 attention heads and the latent dimension is 512. This is much smaller than OCTO and OpenVLA. Another point is that EF-VLA takes inputs from multiple steps (and also outputs multiple steps) but the others don't. The performance gain could come from this aspect but the author didn't experiment thoroughly. The better way to study early fusion is by modifying the original OCTO and OpenVLA and re-training them. I understand the potential effort on it, but there is no other way to clearly justify early fusion is better and generally applicable.

- The proposed particular method highly depends on CLIP. The problem is how this approach can be generalized to other vision models and whether other vision encoders will show similar early-fusion benefits. In its current form, the approach is highly limited by CLIP. The authors are highly encouraged to explore how other pre-trained vision encoders for general purposes or specifically for robot learning will fit in this paradigm. Also, studying the way of mixing two visual representations like in OpenVLA is interesting.

- The technical contribution is minor considering the existing ClearCLIP. 

- Other baselines are not evaluated in simulated environments. Only one simulated environment is used.

### Questions
Please find them in the weaknesses part.

### Soundness
1

### Presentation
2

### Contribution
1
