# Gaze-Regularized Attention for Human Action Prediction

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
Eye gaze, encompassing fixations and saccades, offers valuable insights into human intentions and future actions. This study presents a novel approach to enhancing Vision Language Models (VLMs) for human action prediction by integrating eye gaze data into egocentric video analysis. Existing methods for action anticipation in egocentric videos often rely solely on visual data, potentially missing critical information provided by eye gaze. To address this limitation, we propose a unique gaze-augmented framework that integrates eye gaze directly into the VLM architecture and training process. By generating gaze heatmaps from eye gaze coordinates, our model dynamically focuses on regions highlighted by gaze patterns. Additionally, a gaze-regularization mechanism ensures the model maintains attention on gaze-allocated areas, thereby improving prediction accuracy and robustness. Our approach significantly enhances the model's ability to generate precise and detailed predictions of future actions. Compared to baseline models without leveraging gaze data, our method achieves a nearly 13\% improvement in the semantic score of predictions. This substantial improvement underscores the effectiveness and novelty of integrating eye gaze with a gaze-regularized attention mechanism in VLMs for action anticipation. Moreover, our work demonstrates that incorporating eye gaze through this gaze-augmented framework can significantly boost the predictive capabilities of VLMs, enhancing their potential in applications that require accurate human action prediction.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new framework that incorporates human eye gaze into the VLM training process for the task of fine-grained human action prediction. Compared to the VLM baseline (Flamingo) that is trained without any gaze information, the proposed approach achieves better performance. The dataset used for experiments is constructed using a subset of the Ego4D dataset.

### Strengths
The problem that is addressed in the paper (fine-grained action prediction in egocentric video) is well motivated and is an important problem that has great potential for various practical use cases.

The paper provides detailed descriptions of the dataset creation process and other details around the experimentation. This is is helpful for better understanding and reproducibility.

### Weaknesses
 * Other baselines for fair comparison
There is only one baseline that is considered in the paper, which is a plain VLM model fine-tuned on the language and image without gaze. Since gaze itself is additional information that contains rich information about person's intention on its own, simply providing this info into the existing VLM pipeline would also increase the performance, even without the proposed gaze-regularized attention architecture.
In order to better evaluate the true value of the proposed method and to separate out the improvements coming from having access to additional information, additional baselines would be valuable. For example, if we simply provide gaze-overlaid images to base VLM, fine-tune and evaluate on them, how much would that help?

* Sensitivity to missing data
In real use case scenarios, gaze data can be frequently missing from the gaze tracker or have no gaze information at all. What is the impact of such cases on the model performance? Can an off-the-shelf saliency model be used in the absence of actual gaze? or would it be causing more harm than good if gaze data is missing? How big would be the gap if so?

* Generalizability
The whole idea in the paper is only validated using a single dataset, which is Ego4D, and even then it is a subset of it and small scale. Is the method generalizable to other scenarios? or is it optimized for only this use case? It needs to be evaluated on other scenarios/datasets.

### Questions
See above.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a gaze-guided vision-language model (VLM) for fine-grained human action prediction. The authors leverage the gaze data present in the data set Ego4D as input signal to create gaze-augmented images and feed them into a vision transformer (ViT). The resulting tokens are used as queries in an attention block, where similarly processed tokens of RGB images are used as keys and values. The attention block is regularized to align the transformer’s attention with the human gaze heatmaps through Kullback-Leibler divergence. The authors compare their model to a baseline model without gaze guidance and achieve a ~13% improvement in performance.

### Strengths
The paper is well written and presents good experiments and ablation studies to validate their method. The method is described clearly and reproducibility will be ensured by providing the relevant code. In general, action prediction is a valuable task for human-machine interaction, which the authors present as their motivation.

### Weaknesses
- The significance of the method for the ICLR community remains unclear, as the topic mainly belongs to the field of human-computer interaction (HCI) and does not incorporate any representation learning, which is clear as no ICLR papers are used as reference. Hence, it might make sense to redirect this paper to a more HCI specific conference. 

- Guiding a model’s attention with eye gaze is not novel (Min & Corso, 2020; Awale & Sarikaya, 2022) +  [N1, N2, N3] and usually includes a gaze prediction model instead of requiring gaze at inference time. This key limitation of the method has been described as a feature, because “eye-gaze can be easily obtained and should be used as a direct signal” (L1.41), which remains questionable.

- The authors only compare their method to a simpler baseline model instead of other methods described in the literature, e.g. (Min & Corso, 2020).

- Several key references are missing, e.g. vision transformer [N4], similarly for ChatGPT, GPT-V4, and ShareCaptioner. In general, I would suggest adopting a more comprehensive citation style and finding references for claims, such as “VLMs have the potential to facilitate human-machine interaction” (L.40) or “[these scores] are widely employed to assess text similarity” (L.410).

- Abbreviations are not used consistently, i.e. vision transformer (ViT) is almost always written in full, same as vision-language model (VLM).

### Questions
Based on the ablation studies it remains unclear why the use of gaze overlaid images (G) as queries in the attention block is important. The attention-guidance through KL divergence seems to be the main reason for the performance increase, as performance drops even below baseline performance if lambda is set to 0 (Table 2). Therefore, I would suggest performing a more detailed analysis and potentially removing this additional input step, which in turn would make it easier to remove the need for eye gaze signals at inference time. 

Since delta is set to 200 ms and the eye gaze is sampled at 30 fps, the maximum number of gaze points considered in one prediction is 6 (and this is most likely during a saccade). Further, the images considered as input are downsampled to 1 fps. I believe it would be interesting to evaluate whether increasing the amount of gaze points (delta) up to the 30 points corresponding to one image frame, can increase the performance of the model. Additionally, it would be interesting to see how the data is distributed, i.e. how many gaze points are within the selected distance discrepancy threshold (eta) and why delta has been selected to be 200ms.

### Soundness
3

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
3

### Summary
The paper presents an innovative approach that utilizes gaze as an attention map to guide visual features within a Vision Language Model (VLM) for human action prediction in an egocentric context. In this method, gaze data collected across a sequence of frames is aggregated into a gaze heatmap. This heatmap is divided into patches, with a probability distribution defined over each patch to reflect the gaze intensity. The heatmap is overlaid on the original RGB images, which are then processed by a Vision Transformer (ViT) to generate gaze-aligned features.

In the attention mechanism, these gaze features serve as queries, while the RGB image features extracted by the ViT act as keys and values. The model predicts attention weights by aligning the queries with these keys and values, facilitating attention guided by gaze patterns. To encourage alignment, a Kullback-Leibler Divergence (KLD) loss is applied, ensuring that the VLM’s attention distribution closely matches the gaze-derived distribution. This setup allows the model to dynamically focus on regions of visual significance while incorporating human gaze cues, which enhances the interpretability and relevance of its predictions for egocentric action anticipation.

### Strengths
The authors present a straightforward yet effective way to integrate gaze data into a Vision Language Model (VLM), guiding the model's attention to human gaze-directed areas. By aligning machine attention with human perceptual cues, the approach enhances the model’s understanding of intent and supports more accurate action prediction, especially in dynamic, egocentric scenarios.
Their results indicate a substantial improvement over the baseline model lacking gaze-based guidance, with a notable 13% increase in accuracy. The paper also includes a thorough experimental comparison with the baseline model and an ablation study exploring various methods of incorporating gaze as an attention mechanism.
One particularly impressive aspect of the approach is the use of gaze features, rather than relying solely on heatmaps. By optimizing the attention distribution to reflect gaze patterns, the model effectively benefits from human guidance in identifying critical visual areas. This method, while relatively simple, proves both intuitive and powerful in enhancing action anticipation accuracy.

### Weaknesses
While the paper is well-written and demonstrates clear improvements over a basic VLM baseline, I find the experimental section overly focused on their proposed approach without sufficient comparisons to existing non-gaze-based methods on the Ego4D dataset. For a more comprehensive evaluation, it would have been beneficial to see comparisons with alternative models that perform action prediction on Ego4D using methods other than gaze. Examples such as PALM: Predicting Actions through Language Models and MMG-Ego4D: Multi-Modal Generalization in Egocentric Action Recognition could provide useful context, though they are just suggestions. Such comparisons would show how the proposed approach stands relative to state-of-the-art action prediction methods in similar settings rather than only against a weaker baseline. The argument that fine-grained action recognition makes comparisons with methods focusing on coarse-grained predictions unsuitable is not convincing, as fine-grained predictions should still contain information relevant to coarse-grained tasks, allowing for meaningful comparisons. Additionally, I see potential in the gaze embedding component as a general enhancement for VLMs, which could be more compelling if evaluated across a range of tasks or compared with other gaze-based approaches. For instance, examining how the model compares to Voila-A: Aligning Vision-Language Models with User's Gaze Attention could offer insights into its performance in similar gaze-enhanced VLM setups. Considering that gaze data collection requires specialized equipment, it would strengthen the argument if the authors could demonstrate that gaze embeddings lead to clear accuracy gains over non-gaze-based methods. Testing with other vision-language models, such as LXMERT, could showcase the potential generalizability and robustness of the gaze embedding across models.

Minor Suggestions: Adding a grid overlay to Figure 3 would help clarify the construction of patches for the reader, improving the paper’s visual clarity in illustrating the method.

### Questions
1- Equation 4 Clarification: The author points out that the denominator refers to all pixels in the image rather than just those in the patch. This choice may impact how attention weights are normalized across different regions and could benefit from further explanation. Why does the model use global pixel summation instead of patch-specific summation? Additional clarification on this point would be helpful.

2- Gaze-Overlaid Image Processing: The statement, "We adopt a methodology similar to that used for RGB images to process gaze-overlaid images with a Vision Transformer (ViT) for feature extraction," is confusing. The authors did not explain what exactly was used for RGB images. A more detailed description of what is meant by "similar to that used for RGB images" would enhance clarity.

3- Study of Temporal Variations: Given the paper's proposal to use gaze-guided features for action prediction, a deeper analysis of how the model performs over varying input and prediction times would be valuable. I think including results form Table 8 and 9 from supp material into the main paper could strengthen the paper further.

4- Model Speed and Real-Time Performance: Since action prediction in an egocentric setting often requires near real-time responses, it would be useful to provide details on the model's runtime. An analysis of inference speed, particularly for real-time applications, would strengthen the model's practical applicability.

5- Construction of Gaze Feature Images: More information on how gaze feature images are constructed is essential for reproducibility. Exploring alternative ways of generating these features could offer insights into the method's sensitivity to gaze representation. Additionally, a study on the distribution of the Gaussian overlay on gaze data could provide insights into how different spatial representations impact model performance. Testing variations, such as adjusting the Gaussian’s spread or opacity, could highlight the robustness of the gaze feature representation

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This study introduces a novel approach to improving VLMs for human action prediction by integrating eye gaze data into egocentric video analysis. The method involves generating gaze heatmaps from eye gaze coordinates and dynamically focusing the model's attention on regions highlighted by gaze patterns. A gaze-regularization mechanism ensures the model maintains attention on gaze-allocated areas, enhancing prediction accuracy. The approach achieved a nearly 13% improvement in the semantic score compared to baseline models (i.e. no gaze), demonstrating the effectiveness of incorporating gaze data into VLMs for action anticipation.

### Strengths
- The ablation study is adequate, with a lot of experiments.

### Weaknesses
Title, intro & Abstract:
•	I believe the title (as well as the intro) of the paper is misleading. If the task at hand to improve VLM performance on action prediction/anticipation than VLM should exist in the title. Otherwise, it reads like an action recognition work. 
•	Also, the term "prediction" seems to be replaced with "anticipation."  
•	The task is not "action" based as the output is a description (like a caption). I do not see any parser that takes the final description and receives the actions, the output description has multiple actions while the original GT has a single action and noun.
•	The first sentence of the related work section is also inaccurate: “Action prediction and activity forecasting tasks both aim to anticipate future human actions.” The term "forecasting" implies that future actions are known at the time of prediction. The anticipation definition provided by Ego4D indicates that future frames are unavailable during prediction. In prediction, future frames are processed to predict actions, object interaction locations, etc. The second sentence improves upon the first but uses the vague phrase "longer time." I recommend adopting the Ego4D definition, as the method was evaluated based on this benchmark.

Related work:
•	If the task is to improve VLMs for action prediction, then why there is no section discussing VLMs in this line?
•	Several works are cited as Arxiv, despite being accepted in different venues. The references in the related work section should be updated accordingly. This is crucial for ensuring comparisons with state-of-the-art (SOTA) methods, which is completely missing in this study.
•	It appears the authors have overlooked the winners of the Ego4D anticipation task from the past few years.
•	The statement, “However, in our study, we use eye gaze data as a direct signal for human action anticipation, building a gaze-regularized attention mechanism,” suggests that the authors have not considered the foundational works by James Rehg and his group, who have demonstrated that gaze signals can significantly enhance action anticipation and prediction in egocentric videos. It would be beneficial to review the ETRA conference and GAZE workshops. Relevant examples include:
[A] Ozdel et al. Gaze-Guided Graph Neural Network for Action Anticipation Conditioned on Intention
[B] Fathi et al. Learning to Recognize Daily Actions Using Gaze
[C] Ozdel et al. Gaze-Guided Graph Neural Network for Action Anticipation Conditioned on Intention
[D] Zhang et al. Can Gaze Inform Egocentric Action Recognition?
•	On the other hand, I do not see any advantage of using the gaze signal which exists as a modality in the proposed method (also in test time) while several methods can predict the gaze and actions simultaneously and use the gaze to improve the action prediction. It would be great if the authors clarify this.

Annotation and Dataset Concerns:
•	It is crucial to note that since the proposed method relies on gaze signals as a modality—differing from other studies performs action prediction/anticipation—the dataset split utilized is significantly smaller. Limiting experiments to one dataset, which is substantially smaller than the most recent action prediction SOTA, poses a disadvantage. A more realistic approach would involve using a gaze target detector and incorporating its output, as in real-life applications, gaze location will not be provided as ground truth.
•	How did you evaluate the text descriptions manually for such a large number of images? What was the duration of the evaluation process? How many individuals assessed each image, and what was the consensus among them? Are there any statistics available regarding this consensus?

Method:
•	The "GAZE-REGULARIZED ATTENTION BLOCK" bears a strong resemblance to the work of [E], which uses object embeddings instead of gaze, nevertheless, its technical novelty is unclear.
[E] Thakur et al., Leveraging Next-Active Objects for Context-Aware Anticipation in Egocentric Videos, WACV 2024.
•	The evaluation metrics employed diverge significantly from those suggested by Ego4D. The task encompasses more than mere action recognition and should not be cast to captioning or if it is captioning then why mentioning the action recognition in the title and related work and thought the paper?

Evaluation:
•	Ablation study is adequate.
•	Comparisons with SOTA are missing. What about using different large models? Why only flamingo?
•	The task defined by Ego4D where the noun, action, and time of contact are to be predicted, was significantly changed. Consequently, comparisons with other methods are harder. However, the current results are not justifying the performance of the proposed method is significant or not as it is just ablated but not compared with other approaches. The results demonstrate that gaze matters, however, this is something we already know from the literature.

Overall & justification of the score:
HCI and computer vision studies have repeatedly shown that gaze is an important indicator of both current and future actions. This study presents similar findings. However, the method of incorporating the gaze signal is not novel even if it might be the first time for a VLM case while it was not tested on several ones, but flamingo was used. 
The limitations of the approach were not discussed. Additionally, both the ground truth and predictions were generated by VLM, which raises concerns. The findings are unsurprising, and the technical novelty is unclear. There are no comparisons with other papers using Ego4D, which may be due to significant changes in the ground truth. However, it seems possible to inject VLM into other methods and perform a comparison. This possibility was never been discussed.

### Questions
- Why did you change the definition of the existing action prediction (and/or anticipation) task, which is well described in Ego4D? The GT has been significantly changed and the produced output is also very different, what are the advantages of them wrt to Ego4D's SOTAs' implementation? And do you think what you perform in the paper is action recognition?
- What is the advantage of using the gaze signal directly? Would not it be better to regress the gaze simultaneously?
- What are the limitations of your work?

### Soundness
2

### Presentation
2

### Contribution
1
