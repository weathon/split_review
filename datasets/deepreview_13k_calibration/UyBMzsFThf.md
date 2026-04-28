# Finetuning CLIP to Reason about Pairwise Differences

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Vision-language models (VLMs) such as CLIP are trained via contrastive learning between text and image pairs, resulting in aligned image and text embeddings that are useful for many downstream tasks. A notable drawback of CLIP, however, is that the resulting embedding space seems to lack some of the structure of their purely text-based alternatives. For instance, while text embeddings have been long noted to satisfy \emph{analogies} in embedding space using vector arithmetic, CLIP has no such property. In this paper, we propose an approach to natively train CLIP in a contrastive manner to reason about differences in embedding space. 
We finetune CLIP so that the differences in image embedding space correspond to \emph{text descriptions of the image differences}, which we synthetically generate with large language models on image-caption paired datasets.  
We first demonstrate that our approach yields significantly improved capabilities in ranking images by a certain attribute (e.g., elephants are larger than cats), which is useful in retrieval or constructing attribute-based classifiers, and improved zeroshot classification performance on many downstream image classification tasks.
In addition, our approach enables a new mechanism for inference that we refer to as comparative prompting, where we leverage prior knowledge of text descriptions of differences between classes of interest, achieving even larger performance gains in classification. 
Finally, we illustrate that the resulting embeddings obey a larger degree of geometric properties in embedding space, such as in text-to-image generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method to train CLIP image/text encoders such that the difference between CLIP's image embeddings are aligned with the text descriptions of the image differences. The authors further show through empirical results that this results in better performance on difference-based classification while maintaining neutral performance on zero-shot prompting performance.

### Strengths
The strengths of the paper are as follows:

* The proposed method is simple and can be easily extended as a main objective during CLIP pretraining (not just as a finetuning objective).

* The proposed method shows significant improvement on tasks involving difference based classification.

### Weaknesses
The weaknesses of the paper are:

* The main contribution of the paper is limited. Finetuning CLIP on the proposed objective (aligning g(I_1 ) - g(I_2) with f(T_{1,2})) is a novel contribution, however in itself is not sufficient. Similarly, the empirical studies in this paper are not very impressive. While Table 1 results on difference-based classification are impressive, the rest of the results show very marginal improvements over the baselines.

* There seems to be lot of repetition in the form of summarizing the same set of results/observations over and again. The authors must reduce such repetition and include more details from the appendix, such as the training details.

### Questions
* In Sec 4.1, it is mentioned that the 1000 randomly sampled images were paired and a filtering was applied to remove poor quality generations -- are there any ablations without such a filtering? This is important in the context of scaling up this approach to millions of images where we might end up with lower quality generations, so learning how much lower quality generations impact the final performance could be a good indicator of the scalability of this approach.
* In L419, I think the authors meant to say "highly confused in Table 3" instead of "highly confused in Section 4.3".

### Soundness
2

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
The paper argues that the CLIP text embeddings do not exhibit the structure of purely text-based embeddings. Specifically, the difference between the CLIP text embeddings in the representation space does not encode the semantic difference between two captions in the raw space. To solve this problem, the authors propose to finetune the CLIP model on LLM-generated difference descriptions for the pair of image-text data sampled from a dataset. Post-training, the model can perform difference-based classification and zero-shot classification very well. In addition, the paper’s solution gives rise to the possibility of comparative prompting which can potentially improve the model classification on confused classes (e.g., crab and lobster), and embedding arithmetic with text-to-image generative models.

### Strengths
- The paper proposes an effective method to solve the highlighted problem. Specifically, the synthetic data generation using LLMs for any pair of images is reasonable. 
- The paper showcases the utility of their method using difference-based classification, zero-shot evaluation, and evaluating the quality of the learned method.

### Weaknesses
 - The paper lacks a good motivation on why CLIP models should exhibit the structure of purely-language based text embeddings. The CLIP pretraining never encourages such structure to emerge so it is not unusual to observe such behavior. In particular, the motivation never justifies why difference understanding is a desirable property.
- The paper’s problem does not seem relevant in the context of large multimodal models. Specifically, we have several models such as LLaVA, Qwen-VL that should be able to perform difference-based classification by design. In addition, we would not need to create difference descriptions during inference with these models. 
- The paper is quite detached from the prior work on difference based image captioning [1,2]. It is a well-studied field where the focus is on understanding the fine-grained differences between the two images. In reality, we would need PC-CLIP for such tasks more than difference-based classification. There is no evaluation on such tasks. 
- There is prior work that aims to address a similar problem [3,4]. The paper neither discusses nor compares with any of these methods. One of them is quite old, and warrants some level of comparison. 
- Comparative prompting is not well-grounded. Specifically, how will we know if the f_A is misaligned? Figure 3 expects that f_B is well-aligned but f_A is not, what happens if both f_A and f_B are misaligned? 
- In Table 2, we observe that comparative prompting leads to worse results than non-comparative prompting for CIFAR100, CUB, and almost similar results for SUN397. This suggests that this method may not be effective many times.
- Additionally, comparative prompting requires a user to create difference captions and tune the alpha hyperparameter. It is not clear whether such efforts are worth the gains on completely unseen tasks and scenarios in comparison to a CLIP model which does not require any of these.
- Zero-shot CLIP results are not provided for a more standard dataset such as ImageNet. A part of this is probably due to the cost involved in finding the confusion classes and creating difference prompts for them.
- Apart from zero-shot classification, CLIP model achieved high-level robustness to natural distribution shifts (ImageNetv2/R/A/S). It is unclear how PC-CLIP would perform in such cases. Additionally, there are no linear probing results to understand the quality of the learned vision embeddings.

### Questions
Mentioned in the weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents PC-CLIP, an approach to improve CLIP models' ability to reason about differences between images through fine-tuning CLIP with LLM-generated comparisons. The key idea is to align differences in CLIP's image embedding space with natural language descriptions of visual differences between image pairs generated by LLM. The authors demonstrate this enables new capabilities like difference-based classification while maintaining or improving standard zero-shot performance. They also introduce comparative prompting to leverage class-level differences during inference.

### Strengths
- New capabilities: The method enables valuable new capabilities like difference-based classification and comparative prompting while maintaining or improving CLIP's core zero-shot performance.

- Comprehensive empirical validation: The work provides extensive experimental validation across multiple tasks, datasets, and evaluation metrics, including classification, embedding analysis, and generation. The baselines are also very reasonable (fine-tune CLIP on the COCO original and rewrite captions).

### Weaknesses
 - Scaling up: The experiment focuses only on a single CLIP model size (ViT-L/14), it is unclear whether the approach still remains useful when the model is larger, and whether it is more or less useful.

- Limited improvements: While the method shows consistent improvements on standard classification tasks, many of the gains are relatively small (1-2% absolute improvement). It is unclear whether the cost is worth such small improvements.

- LLM dependency: The method's core dependency on LLM-generated comparisons introduces risks from hallucination and noise in the training signal, with limited analysis of how comparison quality impacts downstream performance or how to ensure robust comparison generation.

- What is the difference between Table 2 and Table 3? The numbers in Table 3 are much lower than in Table 2. Also, the PC-CLIP baseline numbers are much lower than CLIP (e.g., CUB 59.43 vs 52.57). Also, Table 3 is never referenced in the main text.

### Questions
- What is the difference between Table 2 and Table 3? The numbers in Table 3 are much lower than in Table 2. Also, the PC-CLIP baseline numbers are much lower than CLIP (e.g., CUB 59.43 vs 52.57). Also, Table 3 is never referenced in the main text.

Also see weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes PC-CLIP, a method to finetune vision-language models to better reason about pairwise differences between images by aligning embedding differences with LLM-generated descriptions of visual differences. The approach improves CLIP's performance on difference-based classification from almost random while maintaining zero-shot classification performance. The quality of the embeddings is also evaluated through text-to-image generation.

### Strengths
- The paper is well-structured and clearly written, explaining the methodology and results effectively. The experiments are comprehensive, and I also find the methodology for evaluating the quality of the embeddings through text-to-image generation very interesting and insightful.
- The method is novel, and the results of the difference-based classification look promising. The method gains significant performance from the almost random performance of vanilla CLIP. This capability can potentially benefit downstream models.

### Weaknesses
The method requires the LLM to generate the differences between two captions for both training and performing difference-based classification. However, the experiment only covers LLaMA2-13B-chat-hf as the LLM. I wonder if the authors have any insight into whether the training is based on LLaMA2 but the inference is using any smaller/larger models. Would the change in the distribution of the output impact the performance of the model?
- I'm curious if this approach could be combined with other CLIP improvement techniques. For example, NegCLIP [1] improves compositional reasoning by focusing more on the text encoder. This method feels like a nice complement to it.

### Questions
- The method requires the LLM to generate the differences between two captions for both training and performing difference-based classification. However, the experiment only covers LLaMA2-13B-chat-hf as the LLM. I wonder if the authors have any insight into whether the training is based on LLaMA2 but the inference is using any smaller/larger models. Would the change in the distribution of the output impact the performance of the model?
- I'm curious if this approach could be combined with other CLIP improvement techniques. For example, NegCLIP [1] improves compositional reasoning by focusing more on the text encoder. This method feels like a nice complement to it.

[1] When and Why Vision-Language Models Behave like Bags-Of-Words, and What to Do About It?, Yuksekgonul et al., 2023

### Soundness
3

### Presentation
4

### Contribution
3
