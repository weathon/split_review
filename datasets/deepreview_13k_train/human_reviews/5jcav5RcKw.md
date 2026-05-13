# Jointly Training Large Autoregressive Multimodal Models

- Decision: Accept
- Scores: 5, 6, 5, 6

## Abstract
In recent years, advances in the large-scale pretraining of language and text-to-image models have revolutionized the field of machine learning. Yet, integrating these two modalities into a single, robust model capable of generating seamless multimodal outputs remains a significant challenge. To address this gap, we present the Joint Autoregressive Mixture (JAM) framework, a modular approach that systematically fuses existing text and image generation models. We also introduce a specialized, data-efficient instruction-tuning strategy, tailored for mixed-modal generation tasks. Our final instruct-tuned model demonstrates unparalleled performance in generating high-quality multimodal outputs and represents the first model explicitly designed for this purpose.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
JAM, novel methodologies for combining pretrained autoregressive image2text and text2image models, demonstrates remarkable new abilitys to generate interleaved image-text sequence.

### Strengths
This work proposes a novel approach to bridge two separate image2text and text2image models into a new unified model that can generate both image and text.

The resulting model demonstrates remarkable ability on generating interleaved image-text sequence under adequate qualitative evaluation compared with GILL.

### Weaknesses
 **Method is restricted.**
1. The method is not general and nearly impossible for the community to follow. Because your method requires two identical image2text and text2image models, but nearly all available image-to-text and text-to-image models are of different architectures. This severely limits the applicability and reproducibility of the proposed approach. The requirement of identical architectures for both models is a significant constraint, given the diversity of existing models, making it difficult to leverage pre-trained models and hindering adoption by the broader research community.
2. Thus, the only way for the community to test your method's effectiveness is to first pretraining two **identical** separate models. I think this is rather inefficient and prohibitive. The computational cost and time required to pre-train two large models from scratch, just to test this method, is a major barrier to entry for most researchers. This is a significant practical drawback that needs to be addressed.

**Experiments seem too casual.**
1. Your paper focuses on multimodal models that generate both images and texts, but how can the performance of pure language tasks be your main table and experiments? **This table even becomes the most adequate part of your experiments**. This is not aligned with your motivation and focus. The emphasis on language-only tasks, like perplexity on text datasets, does not adequately demonstrate the model's core multimodal capabilities. It seems like the authors are prioritizing a metric that is easy to compute, rather than a metric that truly reflects the model's ability to generate interleaved image-text sequences.
2. Experiments about multimodal ability are too casual and not taken seriously. Your all multimodal experiments, except for the qualitative cases, are Table 2-5 on Page 7. Among them, three are ablation and Table 2 is your main table for multimodal performance. However, Table 2 uses MS-COCO as dataset and PPL as metric, which rarely serves as a **main** evaluation of multimodal ability. The baselines also lack a lot. The experiment quantity and quality is too bad to be a ICLR submission. Using PPL on MS-COCO as a primary metric for multimodal performance is insufficient and does not capture the complexities of interleaved image-text generation. It is a weak proxy for evaluating the model's ability to produce coherent and meaningful multimodal sequences. The lack of comparison with other strong baselines further weakens the experimental results.

**Inadequate literature review.**

Your focus and motivation is to develop a multimodal model able to generate both image and text outputs. The field has witnessed an emergence of such kind of models. To name a few, Emu [1], SEED-LLaMA [2,3] and DreamLLM [3], etc. Among them, SEED-LLaMA [2,3] and DreamLLM [3] are recent work and can be arguably ignored, but Emu [1] is released even earlier than the blog of CM3Leon, the work you heavily follow. However, your literature review and discussion totally ignore such multimodal unified modeling work that generate both image and text, which I think are **the most closely related to your work** and should not be ignored. The omission of relevant works, particularly Emu [1], which directly addresses the generation of both image and text outputs, is a significant oversight. The lack of discussion regarding these related approaches leaves a gap in the paper's contextualization and analysis of its own contributions.

### Questions
My rating is 4. But as only 3 and 5 are available, I choose 5 for the novelty in combining two separate models to empower better multimodal capability. But this work have too many deficiencies too.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors work on combining two pre-trained autoregressive models to form a new decoder armed with multimodal generation capability. More specifically, the authors combined text-to-image decoder and text decoder, and formed a decoder that can seamlessly generate text+image.

### Strengths
To the best of my knowledge, this work is, if not the earliest one, among the pioneering works that explore fusing two decoder-only models of different modality into one, to enable seamless image+text generation. Previous works have considered merging the token spaces from different modalities, and use single decoder to enable generating both modalities (like AudioPaLM); However, the idea of fusing two decoders, and arm the new decoder with the capability of generating high-quality multimodal output is new. 

As a pioneering exploration, the authors explored three different approaches to fuse two decoders, and all the three methods all seem to be successful. The authors also conduct ablation studies to better understand the three approaches they have proposed. Empirically, the authors show the feasibility of fusing two decoders from multiple modalities.

The authors collect a small and curated mixed-modal dataset for the purpose of multimodal conversational instruction tuning, and also confirmed that training with interleaved image-text data is beneficial.

### Weaknesses
On Reasoning/Understanding: 

One weak point is that JAM models (both JAM-Uniform, Width or Cross) are all much weaker compared to LLaMA and GPT-3, while LLaMA is even smaller in terms of model size compared to JAM-Width and JAM-Cross. This is acceptable as this work is not focusing on reasoning and understanding.

On Scaling up: 

Compared to GPT-3, the JAM model is still pretty small. Scaling up the model size could potentially help with the performance in terms of common sense reasoning and also generation. 

Single image generation:

 Interleaved generation is one innovation of this work. By reading the decoding strategies, it seems that one single image will be sampled if <break> token is detected, and then the model will continue text generation unless the <eos> token is sampled. By looking at all the samples provided, it seems that this is the case.One possibility is that there could be multiple text requests to generate multiple images at once.

### Questions
Did authors compare their decoding strategy with contrastive decoding and clip-reranking, in terms of both efficiency and performance?

Can users control alpha_c, tao and other critical hyper-parameters during decoding? So the tool can be more balanced in generating text+image, or more leaning towards text or image generation.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors study three ways in which a pre-trained text-only decoder LLM $\mathcal{T}\_{llm}$ and a text-image LLM (trained on VQ-VAE tokens) $\mathcal{T}\_{img}$ with the same architecture can be merged as a multi-modal LLM capable of interleaved text-image generation called Joint Autoregressive Mixture (JAM). The three ways of combining the two models are: 1. **Model Merging** in which the weights $\theta\_{llm}$ of $\mathcal{T}\_{llm}$ and the weights $\theta\_{img}$ of $\mathcal{T}\_{img}$ are averaged as initialization weights $\theta\_{avg} = 1/2 \theta\_{llm} + 1/2 \theta\_{img}$ for a model of the same parameter size (7B in the paper) (JAM-Uniform) 2. **Width Concatenation** in which the weight matrices are concatenated to form matrices of double size (per matrix dimension), both copying and averaging (JAM-Width) 3. **Cross Model Fusion** in which both  $\mathcal{T}\_{llm}$ and $\mathcal{T}\_{img}$ are augmented with cross-attention layers that permit a bi-directional flow of information, generalizing the Flamingo model (JAM-Cross). In each way, the authors train the resulting JAM model using the CM3 loss and perform instruction tuning using a small curated dataset of examples (following the LIMA paper).

### Strengths
- The idea of bi-directional cross-attention layers between two generative backbones is an elegant approach for performing model merging. Indeed, the authors obtained SOTA results with JAM-Cross on MS-COCO (147.6 PPL), also showcasing the positive influence of the pre-trained joint text decoder.
- Comparing the three ways of performing model merging while demonstrating the superiority of JAM-Cross between the three sheds light on what is the best way of performing such an operation.

### Weaknesses
### weaknesses:
 - While the experimental section is fair, pointing to a new state-of-the-art over CM3leon, the improvement is only 1.4 PPL points with an increase of the model size of more than double (19B vs 7B of CM3leon) and increased training time. The authors suggest that minimal performance degradation post-merging should be studied in the evaluation part. While I agree minimal degradation is a necessary condition, it is not sufficient: given that the final model performs the same tasks as CM3leon, improving only 1.4 PPL points does not justify the necessity of jointly training with a text LLM. Specifically, the authors should consider evaluating the model on tasks that specifically require interleaved text-image generation to show the unique benefits of their approach. Furthermore, a more thorough ablation study is needed to isolate the impact of the joint training with the text LLM, compared to simply increasing the model size or training time of the original CM3leon model.

- The paper does not adequately address the potential for catastrophic forgetting during the merging process. When merging two models, there's a risk that the resulting model will lose some of the capabilities of the original models. The authors should provide a more detailed analysis of the performance of the merged model on tasks that the original models were trained on, to ensure that no significant capabilities have been lost.

### Questions
- Shouldnt we have $\mathbf{H}\_{llm,l}$ and $\mathbf{H}\_{img,l}$ in Eq. 4 instead of $\mathbf{H}\_{llm,l}$ and $\mathbf{H}\_{llm,l}$?
- "We prevent the objective from masking across the modality `<break>` tokens.": Does the CM3 objective relocate masks at the end of each modality or at the end of the total document?
- What is $q$ in “The retriever takes an input query x and returns a relevance score $r(q, m)$”, the authors intended the $x$ variable?
- “We leverage our text-to-image backbone’s modifications introduced in Yu et al. (2023).” What does this phrase mean in the paragraph?
- “The two embeddings are then averaged to form the documents’ vector representation”: if a document contains multiple text and images, shouldn't it have more than two embeddings?
- "We prioritize the diversity of the sampled documents by skipping candidates with a score r(q, m) ≤ 0.9.”. Reading the original paper, the candidates with a score higher than 0.9 are dropped, not the opposite as here.
- “we is data efficient we train”, bad phrasing.
- In classifier-free guidance, $t_x$ refers to the tokens generated before the image token to be sampled?
- I don't understand if the final text-to

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the Joint Autoregressive Mixture (JAM) framework, aimed at integrating large-scale pre-trained text and image models to generate cohesive multimodal outputs. Leveraging the architectural compatibility of autoregressive text-to-image models with Large Language Models (LLMs), the authors propose a systematic approach to model fusion and joint training. The JAM framework exhibits superior performance in generating high-quality multimodal outputs, integrating text and images seamlessly, and represents a significant step towards advanced multimodal conversational systems.

### Strengths
- The authors have proposed novel methods for combining pretrained AR models.
- This represents a great contribution towards building multi-modal conversation agents.
- The specialized instruction-tuning strategy demonstrates efficiency and effectiveness.
- The results shown are noticeably better.

### Weaknesses
 - PPL is not defined anywhere in the draft.
- Retrieval augmented presentation, the last section of page 4, can be improved. a small schema can be helpful.
- Instruction tuning lacks enough details. For example, in the introduction, the efficiency for even 1% of original pretraining data is stated but not mentioned anywhere else in the draft.
- Why does LLaMA have blanks in Table 1?
- Is Table 1 suggesting that 7B LlaMa is better than all the proposed JAM models in reasoning?
- Can we have the baseline results in Table 2 for the Wikipedia dataset as well?

### Questions
- Why does LLaMA have blanks in Table 1?
- Is Table 1 suggesting that 7B LlaMa is better than all the proposed JAM models in reasoning?
- Can we have the baseline results in Table 2 for the Wikipedia dataset as well?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
4 excellent
