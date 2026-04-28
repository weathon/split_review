# LVP: Language-guide Visual Projector for Efficient Multimodal LLM

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Visual projector plays a crucial role in bridging the visual model and the large language model (LLM) in modern multimodal LLM. 
Typically, MLLMs utilize a simple MLP to preserve all visual tokens, causing a heavy computational burden and redundant visual tokens.
Some recent works adopt either a resampler or an adaptive pooling to reduce the visual tokens. However, they only reduce the visual tokens based on the image feature,
leading to the feature misalignment between visual tokens and text tokens. In this paper, we present a novel Language-guidance Visual Projector (LVP), where the text 
feature serves as a guide to selecting the important visual tokens. Specially, we first adopt a lightweight text encoder to extract the text feature. Then, a lightweight
cross-modal feature enhancement module is proposed to enhance the cross-modal feature alignment. Finally, we select the important visual tokens according to the feature similarity between visual tokens and text tokens and apply
a deformable attention module to integrate the visual features from the visual encoder into the selected visual tokens. We further propose a multi-level language-guidance visual projector, which selects the visual tokens from different stages of the visual encoder.
Extensive experiments demonstrate that our LVP compresses the visual tokens by 75\%~95\% while achieving competitive even better performance across diverse benchmarks with a significant efficiency advantage. For instance, LLaVA1.5-LVP with Qwen2.5-7B
obtains 72.4\% accuracy on VQA$^\text{T}$, realizing the state-of-the-art result. The code and the model will be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper discusses advances in multimodal large language modeling by presenting a novel language-guided visual projector (LVP).The LVP utilizes textual features to guide the selection of visual tokens, which enhances the consistency between visual and textual data and improves computational efficiency. It employs a cross-modal feature enhancement module and a multi-level approach to capture fine-grained features, reducing the number of visual markers while maintaining performance. Experiments show that LVP achieves state-of-the-art results using fewer visual markers, demonstrating its effectiveness in multimodal tasks. Its main contributions include the innovative use of linguistic knowledge to optimize visual marker selection and improve multimodal learning.

### Strengths
1) The paper introduces a new approach to align visual and text tokens by using language features to guide the selection of essential visual tokens, which is novel in reducing token input for LLMs.
2) LVP improves the alignment between text and visual features with a cross-modal enhancement module, facilitating better integration of multimodal data.
3) By reducing visual tokens to 25% of the original input, LVP maintains high performance while enhancing computational efficiency in text generation tasks.
4) The multi-level projector design captures both detailed and global visual features, enhancing the system’s versatility and adaptability across different tasks.

### Weaknesses
1) The generalization of the method mentioned in the paper in the scenario of multi-round conversations with multi-modal large models is yet to be proved.
2) The structure proposed in the paper is similar to the one mentioned in paper LXMERT: Learning Cross-Modality Encoder Representations from Transformers, with an additional step of visual token selection.

### Questions
1) It is suggested to add relevant experiments to show that LVP still has excellent performance in the scenario of multi-round conversations with large multimodal models;
2) Specify the innovativeness of the structure, and make a distinction and appropriate citation from the more popular structures previously developed.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work introduces a language-guided visual projector for multimodal large language models (MLLMs).  LVP first proposes a lightweight text encoder to extract text features, followed by the introduction of a cross-modal feature enhancement module and a multi-level language-guidance feature selection module to generate compressed tokens. Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
1. The performance is impressive compared to existing methods.
2. The research focus is both interesting and effective.

### Weaknesses
1. The presentation of this paper is similar to that of TokenPacker.
2. In lines 245-251 on page 5, the feature injection using enriched features through cross-attention shares a similar idea with Mini-Genimi and TokenPacker, although you employ deformable attention in this work.
3. Minor issue: In Table 1, line 344, the value 53.9 should be in bold with the best performance, instead of 53.5.

### Questions
Considering the impressive performance, will the code be released publicly to facilitate reproduction of the results?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Emergency review for Submission #6390

This paper presents the Language-guide Visual Projector (LVP) for multimodal Large Language Models (MLLMs). Existing visual projectors in MLLMs have issues like heavy computational burden or feature misalignment. LVP uses text features to guide the selection of important visual tokens, with a lightweight text encoder, a cross-modal feature enhancement module, and a deformable attention module. In addition, the authors propose a multi-level language-guide visual projector to generate the visual tokens from different stages of the encoder. Experiments show that LVP compresses visual tokens by 75% - 95% and achieves good performance across various MLLM benchmarks.

### Strengths
The advantages of the submission are obvious:

S1. The research on reducing tokens is quite useful. The methodology of the submission is also technically sound.

S2. The performance of the proposed is very good. It beats a lot of baselines. The MME score is also very high.

S3. This paper is also well-written and is easy-to-follow.

S4. According to the visualization, the performance of author's method is also sound.

### Weaknesses
There are three weaknesses from my point of view.

W1. Compared with image tasks, the research on video tasks can better highlight the authors' motivation. We know, there is a lot of redundant information in video. Therefore, I suggest the authors extend their paper to video tasks as in VideoLLaMA and LLaVA-OV.

W2. I suggest the authors present TPS in Tab.1 and Tab.2.

W3. As a submission to ICLR, the paper should have some discussions on the representations of the visual token. Some related experiments need to be conducted.

### Questions
I have some questions.

Q1. Why the datasets evaluated in Tab.1 are not in line with those of Tab.2? Can you report them in total?

Q2. What is the influence of your method applied to video tasks?

Q3. The idea of using text features has already been discussed in InstructBLIP. What are the advantages of your technique compared with InstructBLIP?

Q4. How $N_q$ influence the last model performance?

Q5. Why deformable attention is utilized. How about a regular self-attention?

Q6. Is it possible to quantitatively or qualitatively analyze the representation of tokens input to LLM?

Q7. The visual feature encoder and LLM used by the author are relatively outdated. I know this is for a fair comparison. I want to know how good the performance would be if you consider SigLIP and QWEN2.5 and develop a version under the high-resolution setting.

Justification on rating:

I think the proposed method is useful. I have no firm reasons to reject this paper. I will stick to a positive one if all my concerns are addressed.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a visual projector called LVP, designed to compress visual tokens for efficient multimodal
large language models (LLMs).  LVP is a language-guided visual projector in which text features serve as a guide for 
selecting important visual tokens based on feature similarity. Extensive experiments are conducted to validate the performance of LVP.

### Strengths
1. The text-guided selection for visual token compression presents a novel approach to the task.
2. Compared to previous token compression methods, LVP achieves state-of-the-art performance 
under identical experimental conditions.

### Weaknesses
1. The overall discourse of this paper closely resembles the previous research on TokenPacker, 
particularly in the second and third paragraphs of the Introduction, the first and second paragraphs 
of the Related Work section, and the descriptions of the datasets and main comparison results in the Experiments section. 
This version of the paper requires substantial revisions to eliminate textual repetition.

2. In Figure 2, the visual attention map should indicate which layer in the LLM it corresponds to.

3. In the high-resolution experiments, this paper adopts the same dynamic image slicing method proposed in TokenPacker-HD with resolutions of 1088x1088 and 1344x1344. If this is the case, it should be clarified.



### Questions
I noticed that in Table 3, the performance of 64 tokens (9x compression ratio) utilizing multi-level features achieves comparable results to that of the MLP with 576 tokens, which is impressive. 

I am concerned whether the code will be made publicly available to facilitate better reproduction of results. 
I encourage the authors to release the code to benefit the field.

#####Post-rebuttal#####

After reviewing the feedback and comments from other reviewers, I have decided to lower my scores for the following reasons: 

1. The presentation of this paper largely borrows from the previous paper, TokenPacker, which the authors have acknowledged. Although revisions have been made, many details still exists. It is unacceptable for an academic paper. Additionally, the overall presentation is rough, particularly for figures. I think  this paper is  not adequately prepared for publication.

2. The novelty of this work is limited, despite achieving better performance. The core contribution is  a combination of language-guided methods derived from Grounding DINO  and TokenPacker.  This issue has also been pointed out by Reviewer Note R.

### Soundness
3

### Presentation
2

### Contribution
2
