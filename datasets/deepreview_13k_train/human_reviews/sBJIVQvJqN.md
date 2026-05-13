# Enhancing Vision-Language Model Pre-training with Image-text Pair Pruning Based on Word Frequency

- Decision: Reject
- Scores: 3, 8, 8, 3

## Abstract
We propose \textbf{W}ord-\textbf{F}requency-based Image-Text \textbf{P}air \textbf{P}runing (WFPP), a novel data pruning method that improves the efficiency of VLMs.
Unlike MetaCLIP, our method does not need metadata for pruning, but selects text-image pairs to prune based on the content of the text. Specifically, WFPP prunes text-image pairs containing high-frequency words across the entire training dataset. The effect of WFPP is to reduce the dominance of frequent words. The result a better balanced word-frequency distribution in the dataset, which is known to improve the training of word embedding models. After pre-training on the pruned subset, we fine-tuned the model on the entire dataset for one additional epoch to achieve better performance. Our experiments demonstrate that applying WFPP when training a CLIP model improves performance on a wide range of downstream tasks. WFPP also provides the advantage of speeding up pre-training by using fewer samples. Additionally, we analyze the training data before and after pruning to visualize how WFPP changes the balance of word frequencies. We hope our work encourages researchers to consider the distribution of words in the training data when pre-training VLMs, not limited to CLIP.
\keywords{Vision-Language Model  \and Multimodal Data \and Data Pruning.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces Word-Frequency-based Image-Text Pair Pruning (WFPP), a method to enhance the pretraining of Vision-Language Models (VLMs) by pruning the training dataset based on word frequency. The authors argue that reducing the dominance of high-frequency words leads to a better-balanced word-frequency distribution, which in turn improves the training of word embedding models. The experiments show that their approach, when applied to training a CLIP model, improves performance on various downstream tasks and speeds up pre-training by using fewer samples.

### Strengths
- The proposed method is simple yet effective, and the authors demonstrate its superiority on various benchmarks over other pruning methods for both pre-training and fine-tuning. 

- The paper is well-written, and the figures and tables are clear and support the narrative effectively.

### Weaknesses
 - The proposed method is verified on small scale dataset (CC3M and CC12M) with a large gap of accuracy against existsing methods (e.g., CLIP, MetaCLIP.) pretrained on larger scales (i.e., CommonCrawl 400M). For instance, the zero-shot classification accuracy on ImageNet 1K is around 35%+ for WFPP, but CLIP and MetaCLIP enjoys around 70%. Thus it may still remains unsure if WFPP can be extent to larger scales, expecially as a method to prune the large scale pre-training dataset.

- The probability to discard a sample decreases with the increasing length of input text, and this holds for both Equation 3 and Equation 4. This is intuitively unreasonable since longer input would be less likely to be discarded. The text length is set to 32 by default, but in practice the text lenght can vary a lot and more experiments w.r.t. the text length should be discussed.

### Questions
- The paper uses a straightforward approach to calculate word frequency, which is essential for the WFPP method. It would be beneficial if the authors could discuss the choice of this particular frequency calculation over other potential methods, such as term frequency-inverse document frequency (TF-IDF) or others.

- The threshold $t$ seems to be a critical hyper-parameter. The default value 1e-7 seems to be tricky. The authors should provide more details on how t was chosen and whether its value was tuned experimentally or derived theoretically. Additionally, discussing the sensitivity of the model's performance to changes in t would be insightful.

- It would be helpful to visualize the words filtered, and change of data category proportion before and after WFPP.

- How about the potential of WFPP on (vision-text) large language models?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper hypothesizes that a balanced word-frequency distribution in a dataset can improve the training efficiency of Visual Language Models (VLMs). Through extensive experiments, the authors demonstrate that their proposed method, Word-Frequency-based Image-Text Pair Pruning (WFPP), achieves better performance with a reduced training budget.

### Strengths
1. The approach is straightforward and constructive.
2. The authors conduct comprehensive experiments to validate WFPP’s effectiveness.
3. The analysis on text length normalization provides valuable insights.
4. The authors make all code and data publicly available, enhancing reproducibility.

### Weaknesses
1. The paper lacks theoretical analysis explaining why pruning based on word frequency is effective for image-text alignment.



### Questions
1. What does “w/o ft WFPP” mean in Figure 1?
2. Existing methods emphasize the importance of re-captioning. Would the proposed method be affected by re-captioning? What if, instead of deleting image-text pairs, we re-captioned the images?
3. WFPP uses word frequency as an indicator. Have the authors considered using alternative criteria, such as n-grams or token frequency?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Word-Frequency-based Image-Text Pair Pruning (WFPP), a novel approach designed to enhance the selection of image-text pairs for more effective CLIP pre-training.

### Strengths
1. The paper is clearly written and structured in a way that is easy to understand.

2. The experiments conducted on robustness classification tasks are thoroughly executed.

### Weaknesses
1. While CLIP is over three years old and attention has shifted to newer multimodal large language models (MLLMs), the impact of WFPP on larger models such as LLaVA remains under-explored.

2. MetaCLIP [1] has demonstrated impressive success in establishing a comprehensive pipeline for entire CLIP pre-training. However, the WFPP experiments are conducted using CC3M and CC12M datasets, which are significantly smaller than the 400M images used in the original CLIP training. This raises questions about the scalability and usefulness of WFPP when applied to larger datasets. The paper does not provide sufficient evidence that the observed gains on smaller datasets would translate to larger datasets, where the data distribution and scale are substantially different.

3. Although the authors claim that WFPP can enhance performance across a broad range of downstream tasks, the comparison baselines only include the original CLIP, which may not sufficiently demonstrate the method's relative effectiveness. The paper lacks comparisons against other improved CLIP pre-training methods, making it difficult to assess the true contribution of WFPP.

4. The proposed method employs techniques that are simple and already widely used in the NLP community. Therefore, more comprehensive experiments and detailed discussions are crucial to substantiate its uniqueness and effectiveness. The paper does not adequately explore the sensitivity of WFPP to different word frequency thresholds or provide a detailed analysis of the types of image-text pairs that are pruned.

### Questions
1. Is there any analysis or discussion in the paper that supports the effectiveness of WFPP when applied to much larger datasets, such as LAION?

2. It would be beneficial for the authors to compare WFPP with improved CLIP pre-training baselines, such as DeCLIP [2], FILIP [3], and UniCLIP [4], to better showcase the strengths of their approach.

3. Given that other works, such as TinyCLIP [5] and MoPE-CLIP [6], have achieved competitive performance by pruning and training CLIP models on datasets like CC12M or YFCC15M, a discussion and comparison with these studies would provide a more comprehensive view of WFPP's comparative advantages.

4. Numerous data processing techniques have been proposed to enhance CLIP pre-training, such as DataCompDR in MobileCLIP [7] and the OFA module in ALIP [8]. How does WFPP compare to these strategies in terms of improving pre-training performance?

[2] Supervision exists everywhere: A data-efficient contrastive language-image pre-training paradigm. ICLR 2022

[3] Filip: fine-grained interactive language-image pre-training. ICLR 2022

[4]  Uniclip: Unified framework for contrastive language-image pretraining. NeurIPS 2022

[5] Tinyclip: Clip distillation via affinity mimicking and weight inheritance. ICCV 2023

[6] Mope-clip: Structured pruning for efficient vision-language models with module-wise pruning error metric. CVPR 2024

[7] Mobileclip: Fast image-text models through multi-modal reinforced training. CVPR 2024

[8] Alip: Adaptive language-image pre-training with synthetic caption. ICCV 2023

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a data pruning method for CLIP that focuses on removing frequently occurring data samples. The experimental results show that the pruned model outperforms the original CLIP across several datasets and downstream tasks, indicating that eliminating high-frequency samples can enhance CLIP's training efficiency and performance.

### Strengths
Simplicity: The proposed approach is intuitive and easy to implement, which enhances its potential for broader application.

Performance Gains: The method consistently outperforms the original CLIP across most datasets, demonstrating that the removal of high-frequency samples leads to improved model performance.

### Weaknesses
Insufficient Coverage of Related Work: The paper lacks citations and discussions of key related works in data pruning. Crucial references such as [1-3] are missing. Including these would better position the contribution within the current research landscape.

Limited Baseline Comparisons: The experimental comparison is restricted to the CLIP and MetaCLIP, neglecting other state-of-the-art (SOTA) data pruning methods. A broader comparison with cutting-edge approaches would strengthen the evaluation and provide a more comprehensive assessment of the method's effectiveness. For example, methods that use gradient information or other sophisticated metrics for data selection should be considered as baselines.

Narrow Model Scope: The pruning method is evaluated only on CLIP, without experiments on other architectures such as BLIP or Llava, which are also highly relevant for vision-language and generative tasks. Additionally, the paper does not explore how the proposed method performs on more challenging vision-language tasks like VQA or image captioning. Expanding the experimental scope to include both different models and more challenging tasks would help to establish the method’s generalizability and effectiveness across diverse architectures and applications.

### Questions
Please see weakness.

### Soundness
3

### Presentation
2

### Contribution
2
