# YouCLIP: Advancing Multilingual Cross-Modal Learning with Efficient Training.

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
Since the advent of vision-language pretraining, the CLIP model has become a foundational model for many downstream tasks. However, most of the advanced CLIP models available today are trained primarily on English, making them poorly suited for other languages. This limits accessibility for countries where other languages are dominant. Given that training CLIP models requires vast amounts of GPU resources and data, which most countries lack due to the absence of companies on the scale of Google or OpenAI, this paper proposes an efficient and straightforward three-stage fine-tuning method, which allows for the conversion of the most powerful English CLIP model into models for other languages. 
In these three stages of training, the first stage focuses on aligning the embedding layer, followed by token fusion in the second stage, and finally contrastive learning fine-tuning in the third stage.
Meanwhile, to improve data quality, we propose a translation filtering model to filter the data.
In this work, we target Chinese as the language of interest and name the resulting model YouCLIP, which is currently the most powerful Chinese CLIP model, significantly outperforming previous models across all Chinese benchmarks. For example, YouCLIP improves the text-to-image Recall@1 score on the COCO-CN dataset from 63.4 to 73.1. Additionally, YouCLIP retains strong English capabilities, achieving a Top-1 accuracy of 76.9 on ImageNet. Despite these impressive results, YouCLIP requires the least amount of training resources compared to other Chinese CLIP models. All models and code for YouCLIP will be open-sourced.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method to adapt the English-Image CLIP model to a Chinese-English-Image model by just training a new language encoder without modifying the Image encoder, with a very little loss on English-Image tasks.  The proposed method use a very limited training resources compared with existing Chinese-Image models which are training from scratch with Chinese-Image datasets.   The resulting model YouCLIP creates new SoTAs in almost all Chinese-Image understanding benchmarks.

The method has three steps, while in step one only the embedings of the new language encoder are trained and in the step 2 and 3 both the embeddings and the half of the transformer layers of the language encoder are trained.  In step 2, the language encoder are trained with Chinese-English aligned data and in the step 3, the Chinese encoder are trained with Chinese-Image or English-Image data randomly. 

The English-Chinese-Image data are construsted by translating the English captions into Chinese in an English-Image dataset.  The translation is conducted with a strong LLM QWEN 1.5.  A translation filtering network is proposed is designed to filter out low quality translations.

### Strengths
The paper is clearly written and the experiments have well demonstrate the effectiveness of the proposed method.
The paper creates a new SoTA for Chinese version of CLIP by adapting the English CLIP with the help of an LLM: QWEN 1.5.
The proposed method includes three steps is introduced in details.  Compare with the previous work which training the model from the scratch, this method requires much less computing resources.

### Weaknesses
I wonder the high performance of YouCLIP not only comes from the proposed methods, but also heavily depends on the translation system.  The paper uses QWEN 1.5 for the translation from English to Chinese, which is much larger than CLIP itself.  So the claim that the proposed requires the least amount of training resources is not really true: it uses an existing LLM which is trained with huge amount of resouces which is much larger than the training of a Chinese CLIP.

The effect of the translation system to produce the triple data should be analysed.  Although the paper analyses the effect of the AFN to the final performance, it is not enough.

More details of the AFN also should be provided.

I further suggest the auther to add a pipeline system as the baseline, which first translation Chinese captions into English with the same translation system, than use the original CLIP system with the English captions and the image.  I am curious if YouCLIP can outperform this pipeline system.

### Questions
See weaknesses above.

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
4

### Summary
This paper tackles a problem of adapting the existing CLIP model that is trained in English into another language such as Chinese. The authors proposed a three-stage training method: 1) the first stage focusing on the embedding layer alignment, 2) token fusion and 3) contrastive learning fine-tuning. Experimental results show effectiveness of the proposed approach, significantly outperforming previous models across all Chinese benchmarks.

### Strengths
- Experimental results are technically sound

### Weaknesses
- some experimental settings and/or results are unclear; what about applying the proposed approach into other languages? robustness? Have you ever tried few-shot experiments related to Tables 2 and 3?

### Questions
- Figure 1 (Left) needs a scale or values for the results of "Wukong" and "CN-CLIP"
- Tab.2 -> Table 2 for better readability, as I don't see any space issues in the current manuscript
- OpenCLIP's result on ImageNet (EN) might be missing in Table 3?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a framework to train a non-English CLIP model from English CLIP model. The authors propose three stages of training: 1) Embedding layer alignment; 2) the first half of the Chinese encoder's parameters training; 3)Aligning Chinese encoder with image encoder. The paper instroduces a Translation Filtering Network to filter out the low-quality translated data.

### Strengths
The paper presents a knowledge distillation framework for non-English CLIP model training, allowing for the conversion of the English CLIP model into models for other languages. The method is easy to understand and the research question is interesting.

### Weaknesses
The motivation of the paper is to improve the performance of CLIP models for multiple languages and the title contains "multilingual". However, the model only supports two languages. It is unclear how the model performs on other languages.

The technical novelty is limited. It is common to align different languages by training the embedding layer and using non-English image-text pairs to align the non-English text encoder and image encoder.

The design of the method is relatively arbitrary. For example, the paper assumes the primary difference of text encoders lies in the embedding layer. However, the embedding layer is trained in stage 1 while the first half of the text encoder are trained  in stage 2. 

The model requires a large amount of data, at the billion level, and lacks a detailed comparison with other methods in terms of computational overhead.

### Questions
1. The paper uses the qwen 1.5 models to translate English data to Chinese. How about the performance on the low-resource non-English languages?

2. Can you provide more detailed ablation studies comparing different architectural choices? 

3. What about the performance when the model is a multilingual model that supports multiple languages?

### Soundness
2

### Presentation
2

### Contribution
2
