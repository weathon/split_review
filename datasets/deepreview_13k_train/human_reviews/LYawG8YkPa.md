# LaMP: Language-Motion Pretraining for Motion Generation, Retrieval, and Captioning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Language plays a vital role in the realm of human motion.
Existing methods have largely depended on CLIP text embeddings for motion generation, yet they fall short in effectively aligning language and motion due to CLIP's pretraining on static image-text pairs.
This work introduces \textbf{LaMP}, a novel \textbf{La}nguage-\textbf{M}otion \textbf{P}retraining model, which transitions from a language-vision to a more suitable language-motion latent space. 
It addresses key limitations by generating motion-informative text embeddings, significantly enhancing the relevance and semantics of generated motion sequences. 
With LaMP, we advance three key tasks: text-to-motion generation, motion-text retrieval, and motion captioning through aligned language-motion representation learning.
For generation, we utilize LaMP to provide the text condition instead of CLIP, and an autoregressive masked prediction is designed to achieve mask modeling without rank collapse in transformers.
For retrieval, motion features from LaMP’s motion transformer interact with query tokens to retrieve text features from the text transformer, and vice versa.
For captioning, we finetune a large language model with the language-informative motion features to develop a strong motion captioning model.
In addition, we introduce the LaMP-BertScore metric to assess the alignment of generated motions with textual descriptions. 
Extensive experimental results on multiple datasets demonstrate substantial improvements over previous methods across all three tasks.
The code of our method will be made public.
{\let\thefootnote\relax\footnotetext{
$^*$Equal Contribution~~~
$^{\dagger}$Corresponding Author.
}
}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors point out that existing text-motion related methods largely depend on the CLIP text embeddings, yet will fall short in effectively aligning the language and motion features since CLIP is pretrained on static image-text pairs. The motion information and dynamic characteristics are overlooked. Thus, this work introduces LaMP, i.e., Language-Motion Pretraining model to generate motion-informative text embeddings, significantly enhance the relevance and semantics of generated motion sequences. With LaMP, text-to-motion generation, motion-text retrieval and motion captioning are advanced through aligned language-motion representation learning.

### Strengths
1. This work points out a significant problem for the current motion generative tasks, where the CLIP text embeddings are insufficient for motion generation;
2. The authors have conducted extensive experiments on text-to-motion generation, motion-text retrieval and motion captioning and show substantial improvements over baseline methods;
3. The paper writing is good and easy to follow.

### Weaknesses
1. CLIP is trained on large-scale image-text pair data, thus it can serve as a strong text feature extractor with strong generalization ability. However, it seems that LaMP is pretrained on a small text-motion dataset, thus the generalization ability of the LaMP features may be worse than CLIP’s. This ablation study should be provided to further verify the robustness and effectiveness of LaMP.
2. LaMP-BertScore is introduced as an evaluation metric to better measure the alignment between motion and text. However, since LaMP is trained on small-scale datasets, the metric may be not reliable and convincing. The reliability of this metric is questionable, especially when compared to established metrics that have been validated across diverse datasets. The potential for overfitting to the training data is a significant concern.
3. In current text-motion datasets such as HumanML3D and KIT-ML, the text descriptions are very simple and may include errors, such as left-right body part mistakes. How can LaMP handle these dataset problems to produce a good text-motion alignment model?
4. Some typos: L082, pertaining → pretraining, L096, 097, an LLM → a LLM.

### Questions
My main concern lie in that LaMP seems to be trained on small datasets, thus the generalization ability, the proposed BertScore may be not that reliable. Meanwhile, I also want to know how to deal with the simple text descriptions and errors for LaMP?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript presents LaMP which aims at improving the alignment of language and human motion. Unlike traditional methods relying on image-text models like CLIP, LaMP directly aligns language with motion data through a dedicated language-motion latent space. This approach enhances tasks such as text-to-motion generation, motion-text retrieval, and motion captioning. LaMP leverages a transformer-based framework with four key objectives, including contrastive learning and cross-modal generation, resulting in improved performance across various datasets. The model also introduces a new metric, LaMP-BertScore, to evaluate alignment quality between text and generated motions.

### Strengths
1. LaMP replaces traditional image-based text embeddings with motion-focused ones, effectively improving the semantic alignment between language and motion data.
2. The model successfully tackles three critical tasks—text-to-motion generation, motion-text retrieval, and motion captioning—demonstrating versatility and effectiveness across each task.
3. The introduction of LaMP-BertScore offers a valuable metric for assessing the quality of generated motions, particularly the semantic fidelity of textual descriptions. This enhances the evaluation process in the domain of motion generation

### Weaknesses
1. Comparison with DLP[1] on motion-to-text generation.
2. Failure cases. Please provide some failure cases for further analysis.
3. The details about the Text encoder-decoder. How about the reconstruction metrics on the KIT and HumanML3D datasets.

### Questions
Please see the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a language-motion pretraining approach which can address motion generation, retrieval, and caption problem. The proposed approach targets the problem of enhancing the relevancce and semantics of generated motion sequences. Experiments on multiple datasets have validated the effectiveness of the proposed approach. More specifically, the proposed approach has reasonable performance on the tasks of motion generation, retrieval, and caption.

### Strengths
1. The task of language-motion pretraining is of great importance to the community. 
2. The paper obtains reasonable performance on several benchmarks like HumanML3D, KIT-ML datasets with different evaluation tasks.

### Weaknesses
1. The novelty of the paper is not clear. As LLM model is already been utilized for the motion understanding and generation, for example, MotionGPT, what are the major contribution of the paper against the previous work based LLM?

2. The algorithm is based on BERT. How about the performance if the approach is based on a large LLM, for example, LLAMA-7B?

3. For the text caption, the approach attaches another pretrained LLM model (e.g., OPT-2.7B) to generate captions. This may be due to the limitations from the BERT model. It would be better if the motion caption generation can be integrated into one model. 

4. In the implementation details, what the CFG scale is set different for humanKL3D and KIT-ML datasets? (Also, what is the value for humanML3D dataset)

### Questions
Please address the questions raised in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces LaMP, a novel pretraining model that aligns language and motion to enhance the performance of multiple text-motion tasks including text-to-motion generation, motion-text retrieval, and motion captioning. The authors propose a new paradigm that transitions from language-vision to language-motion latent spaces, addressing the limitations of relying on CLIP for motion-related tasks. LaMP generates motion-informative text embeddings and utilizes an autoregressive masked prediction mechanism to improve the generation process. The paper reports substantial improvements over previous methods on multiple datasets and introduces a new metric, LaMP-BertScore, for assessing the alignment of generated motions with textual descriptions.

### Strengths
1. The paper is well-organized and easy to follow.
2. The authors have achieved a paradigm shift from language-vision alignment to language-motion alignment. Motivated by BLIP-2, they employ four text-motion tasks for joint pretraining, leading to a more enriched latent space that encapsulates rich motion dynamics information and informative embeddings for both motion and text.
3. Through extensive experiments, the authors showcase significant improvements over state-of-the-art methods across three key tasks. Notably, their proposed method exhibits substantial performance enhancements in human motion generation tasks on the HumanML3D and KIT-ML datasets compared to previous approaches.
4. The authors introduce the LaMP-BertScore metric as a novel evaluation measure to assess the quality of generated motions in relation to textual descriptions.

### Weaknesses
1. Some existing studies have also emphasized the downside of aligning static images and text in CLIP, and have suggested directly aligning motion and text in the latent space, as proposed in [1]. The authors should clarify the unique distinctiveness of their method compared to existing approaches. Specifically, the paper needs to articulate how its approach to aligning motion and text differs fundamentally from prior work that also moves beyond image-text alignment, particularly in terms of the specific architectural choices and training objectives that lead to improved performance. It is not sufficient to simply state that they align motion and text; the precise mechanism and its novelty need to be clearly delineated.

2. The authors should include a computational complexity comparison between their proposed method and previous works to provide insights into resource consumption. This comparison should not only focus on inference time but also detail the training costs, including the number of parameters and the computational resources required for pre-training. A comprehensive analysis of both training and inference costs is crucial for understanding the practical applicability of the proposed method, especially when compared to existing state-of-the-art approaches.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3
