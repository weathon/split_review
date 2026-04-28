# Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond

- Decision: Reject
- Avg Score: 5.33
- Scores: 3, 8, 5

## Abstract
\noindent
In this work, we introduce the Qwen-VL series, a set of large-scale vision-language models (LVLMs) designed to perceive and understand both texts and images.
Starting from the Qwen-LM as a foundation, we endow it with visual capacity by the meticulously designed \text{(i) visual receptor}, \text{(ii) input-output interface}, \text{(iii) 3-stage training pipeline}, and \text{(iv) multilingual multimodal cleaned corpus}.
Beyond the conventional image description and question-answering, we implement the grounding and text-reading ability of Qwen-VLs by aligning image-caption-box tuples.
The resulting models, including Qwen-VL and Qwen-VL-Chat, set new records for generalist models under similar model scales on a broad range of visual-centric benchmarks (\emph{e.g.}, image captioning, question answering, visual grounding) and different settings (\emph{e.g.}, zero-shot, few-shot).
Moreover, on real-world dialog benchmarks, our instruction-tuned Qwen-VL-Chat also demonstrates superiority compared to existing vision-language chatbots.
All models are public to facilitate future research.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes QWEN-VL, a series of large-scale vision-and-language models (LVLMs). Further details can be found in Strengths.

### Strengths
- S1: This is one of a few open-source models where the model weights are released (though I don’t think the data is; there is also some “in-house” data; see Table 2). This can benefit the research community; the claim is that while the performance of QWEN-VL is still behind private models, it excels in the open-source community, especially in terms of capabilities it supports (Figures 4-7).

- S2: The training pipeline (Figure 3) is sound and simple.

### Weaknesses
 - W1: Weak research significance and contributions. This work is a huge engineering effort and it is appreciated. However, research-wise, I am not convinced that it can provide any insights in terms of large-scale model training, architecture, or evaluation. The paper does not present any novel training techniques, architectural innovations, or evaluation methodologies that advance the field. The work seems to primarily focus on scaling existing methods, which, while valuable, does not constitute a significant research contribution. For example, the paper could have explored novel loss functions, attention mechanisms, or training strategies that could provide new insights into vision-language modeling. Without these, the research impact is limited.

- W2: Weak discussion of related work and clarity: To make W1 worse, the paper does not properly discuss the relevant work. If the paper would like to focus on the open-source aspect, I think it can expand this part much more heavily. What are the existing open-source LVLMs and what are “open” about them? What are the capabilities they support and so on? However, based on the current presentation this is unclear. The paper needs to provide a more comprehensive analysis of the current open-source landscape for LVLMs. This should include a detailed comparison of the architectures, training data, and supported tasks of existing models. The current discussion lacks depth and fails to highlight the unique contributions of this work in the context of existing open-source alternatives. For instance, the paper could have discussed the specific limitations of other open-source models and how QWEN-VL addresses these limitations.

### Questions
- Is the train-test overlap between benchmarks taken care of? Especially COCO-based datasets.

Please address the two points in my Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper showcase the qwen-vl as a versatile LMM, being able to perceive and understand both texts and images. The  qwen-vl series contains a multitask finetuned 7B model and a chatbox trained with interleaved data. The modeling is similar to flamingo but the trainable parts are different in different stage. The model achieves reasonable generalist scores.

### Strengths
(1) Very clear pretraining data size and mixture weights that helps the general audience get a sense of the pretraining distribution, though the paper uses some internal data, which is understandable

(2) good ablation study over different parts, window attention for highres

(3) good experiment setups that consider sufficient academic benchmarks, 

(4) well written and easy to follow

### Weaknesses
(1) seems missing generalist PaLI results. The PaLI-X authors also have multitask finetuned model for VQA and captioning mixtures separately.  

(2) missing the design / motivation or ablation of which part being trained during different stage. The stage 2 unfreezes ViT is for adapting to higher solution?

### Questions
Please comment on the weakness

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This model introduced a Vision Language Model QWEN-VL which is both pretrained and instruction finetuned. The model shows decent multimodal capability, especially in terms of bounding box reasoning. The model will be open sourced which will be helpful to the community.

### Strengths
- Open sourcing the model is going to help the research community
- The model shows decent multimodal capability, especially in terms of bounding box reasoning

### Weaknesses
My concerns are regarding the scientific and technical contributions from this paper.
- The claim in the related work section, "Despite achieving significant progress, previous vision-language models still have several limitations such as poor robustness in instruction following, limited generalization capabilities in unseen tasks, and a lack of in-context abilities." lacks justification. For example many models are not instruction-tuned (yet). That does not mean they have a fundamental difficulty in instruction following.
- There is limited innovation on the model architecture and training recipe. For example the use of interleaved data and multi-stage, multi-resolution training has been proposed in previous works. Also there is limited novelty in showing that supervised finetuning with interleaved chat data can lead to chatting capability.
- The ablation study is not written clearly (also see questions below)

### Questions
In the ablation study of Figure 7, which stage is that, lower-res or higher-res? If it is lower-res (224) stage it makes sense to use 256 tokens as the native number of patches is just (224/14)^2 = 256. If it is the higher-res (448) stage, then it is counterintuitive that using more tokens, i.e., 400, with more degrees of freedom, will lead to worse performance.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
