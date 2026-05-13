# Is Large-scale Pretraining the Secret to Good Domain Generalization?

- Decision: Accept
- Scores: 6, 5, 8, 6

## Abstract
Multi-Source Domain Generalization (DG) is the task of training on multiple source domains and achieving high classification performance on unseen target domains. Recent methods combine robust features from web-scale pretrained backbones with new features learned from source data, and this has dramatically improved benchmark results. However, it remains unclear if DG finetuning methods are becoming better over time, or if improved benchmark performance is simply an artifact of stronger pre-training.  Prior studies have shown that perceptual similarity to pre-training data correlates with zero-shot performance, but we find the effect limited in the DG setting. Instead, we posit that  having perceptually similar data in pretraining is not enough; and that it is how well these data were learned that determines performance. This leads us to introduce the Alignment Hypothesis, which states that the final DG performance will  be high if and only if alignment of image and class label text embeddings is high. Our experiments confirm the Alignment Hypothesis is true, and we use it as an analysis tool of existing DG methods evaluated on DomainBed datasets by splitting evaluation data into In-pretraining (IP) and Out-of-pretraining (OOP). We show that all evaluated DG methods struggle on DomainBed-OOP, while recent methods excel on DomainBed-IP. Put together, our findings highlight the need for DG methods which can generalize beyond pretraining alignment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper analyzes the reliance of DG works on pre-training particularly in the context of CLIP.  The authors propose the Alignment hypothesis which states that pre-trained alignment between image and class embeddings is helpful for domain generalization performance prediction even after a model is finetuned on source domains. For evaluation, the authors utilize a two-step method. First, they cleaned the data. Images with AlignmentScore < 0.15 are discarded. Similarly, high AlignmentScore (>0.4) is usually for samples that have label text in the image. Second, In-pretraining and Out-of-pretraining are determined based on a scoring threshold of 0.21, based on the authors' observations about the data.

### Strengths
The paper is well-written and generally easy to follow.

This paper presents some interesting insights: 

  1. Relation of low AlignmentScore and presence of label noise in the domain generalization datasets.

  2. "We find that all methods, including those considered state-of-the-art, perform poorly on OOP data" which seems to suggest that DG methods do not learn anything beyond what has already been learned by CLIP during pre-training. This also aligns with some of the previous findings. 

  3. Model parameter averaging boosting performance. 

  4. The fact that a high score indicates text in the image, which is not a significant part of the data (0.00-0.15% across the dataset).

### Weaknesses
IP/OOP method of splitting data seems to be a bit circular. Some of the results are a bit difficult to interpret. For instance, Table 2 seems to represent the correlation of final performance and prediction with IP/OOP splits but presentations make it hard to understand. Further concerns are mentioned in the questions.

- IP/OOP splitting by using CLIP AlignmentScore does not make sense. The CLIP model is first used to calculate to split the data and then to predict the score. Is not it circular?

- One assumption behind this work is that simple alignment between image and label embeddings is sufficient to measure the presence of data in pre-training. What is the justification for this assumption? If a model has learned well, it should have high similarity for examples that are not part of training data but are in the training distribution.


- The authors state the following in the abstract: "Not just the presence of data in pre-training but how well is it learned", however, this part is not reflected later in the paper. How does IP/OOP reflect this?

### Questions
- IP/OOP splitting by using CLIP AlignmentScore does not make sense. The CLIP model is first used to calculate to split the data and then to predict the score. Is not it circular?

- One assumption behind this work is that simple alignment between image and label embeddings is sufficient to measure the presence of data in pre-training. What is the justification for this assumption? If a model has learned well, it should have high similarity for examples that are not part of training data but are in the training distribution.


- The authors state the following in the abstract: "Not just the presence of data in pre-training but how well is it learned", however, this part is not reflected later in the paper. How does IP/OOP reflect this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a hypothesis stating that if the test images and their corresponding text labels (e.g., "A photo of a {cls}") are already well-aligned in the embedding space before fine-tuning, the model's domain generalization (DG) performance will be high after fine-tuning.

Using an alignment score, the target dataset is divided into two parts: in-distribution (IP) and out-of-distribution (OOP). The experiments show that DG methods perform well on high-alignment samples (DomainBed-IP) after fine-tuning but poorly on low-alignment samples (DomainBed-OOP). This suggests that current DG methods rely heavily on pre-trained features.

### Strengths
I appreciate that the authors consider the impact of pre-training weights in the current DG evaluation protocol.

I also value their effort to remove noisy data labels in standard DG benchmarks.

This paper presents a comprehensive set of experiments.

### Weaknesses
 **Weaknesses**

- Since the goal of CLIP's contrastive loss is to maximize the similarity between the ground truth text label embedding and image embedding, it's unsurprising that the alignment score (measured as similarity to the ground truth text embedding) correlates with final performance after fine-tuning. Additionally, the alignment score applies only to vision-language models, not to pure vision models, which is a limitation that should be mentioned in the paper.

- When comparing the predictive power of the Alignment and Image Similarity Hypotheses for downstream tasks, it would be helpful to provide quantitative metrics showing how strongly each hypothesis correlates with performance. It would be beneficial to see not just a correlation, but also a comparison of the slopes of the performance vs. alignment/similarity score, to understand if the alignment score is indeed a better predictor of performance.

- In line 177, is there a typo where “before” should be “after” in “The cosine similarity between image and ground truth text-label embeddings before pre-training”? Also, just to confirm, are the alignment scores and similarity scores shown in Figure 2 calculated from the CLIP model immediately after pre-training on LAION, but before fine-tuning on the downstream DG benchmark?

- I wonder if using a Perceptual Similarity Score with a well-chosen threshold could similarly divide the data into high-similarity samples (DomainBed-IP) and low-similarity samples (DomainBed-OOP). Would the same experimental results hold—that DG methods perform well on DomainBed-IP but struggle on DomainBed-OOP after fine-tuning? Specifically, what is the sensitivity of the results to the choice of threshold for the Perceptual Similarity Score, and how does the performance difference between IP and OOP vary as this threshold changes?

- Based on experiments showing that DG methods perform well on high-alignment samples (DomainBed-IP) but struggle on low-alignment data (DomainBed-OOP), the paper concludes that current DG methods rely on pre-trained features. While this is a useful insight, the conclusion is somewhat unsurprising, as it’s well-known that downstream task performance heavily depends on the diversity of the pre-trained dataset, whether in-distribution or out-of-distribution. For those interested in accurately measuring a DG method’s generalization performance, [1] suggests a new evaluation protocol isolating pre-training's impact. Alternatively, pre-training on a larger and more diverse dataset is likely the best approach for those focused on improving downstream generalization.

### Questions
I have several questions regarding the significance of the proposed Perceptual Similarity Score and the conclusions of this paper. Please see the details above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper critically investigates the successes of recent DG methods that rely on pre-trained backbones, such as CLIP, with a focus on answering an important question: whether those successes are due to the effect of pre-training or to the algorithmic details of DG methods. To this end, the authors first consider the recently proposed image-similarity hypothesis, which posits that if the pre-training data contains images that are perceptually similar to the target data, then the zero-shot performance will be higher. However, the authors find that this does not fully explain the phenomenon and instead introduce the alignment hypothesis. They posit that if the alignment between image embeddings and text labels is high, with respect to the cosine similarity score defined in CLIP models, these alignment scores serve as a better indicator of generalization. They perform this analysis before fine-tuning and after fine-tuning, thus disentangling the effects of pre-training. Given this observation, they create a new benchmark that splits domain bed datasets into in-pretraining (IP) and out-of-pretraining (OOP) splits. 

They then train a large number of DG algorithms from the domain bed framework and observe that most methods actually perform better in the IP condition and perform poorly on the OOP condition, where the performance gap between DG and oracle is quite high. They propose to release these datasets to provide the community with a new benchmark that encourages algorithmic innovations to improve generalization, rather than just using a more powerful backbone.

### Strengths
The paper is well-written and considers an important question of understanding the importance of pre-training backbones in modern DG approaches. Creating a new benchmark is an important contribution.

### Weaknesses
The paper could be improved, especially in Section 3. The methods for identifying image similarity scores and alignment scores need clearer explanations instead of the brief sentences currently provided. Specifically, the computation of the perceptual similarity score, which appears to rely on some form of feature extraction and comparison, lacks detail. It is unclear what specific features are used and how the comparison is performed beyond a general notion of perceptual similarity. Similarly, the alignment score, based on cosine similarity, would benefit from a more detailed explanation of how the image and text embeddings are obtained and how the cosine similarity is calculated for each image-label pair. I suggest including an algorithmic table, as this is a key contribution.

While I appreciate the current contribution, it seems limited since it only considers one variant of the DG problem. The community has explored a broader range of generalization tasks  including sub-population shifts. It will be important to discuss how this work fits into those contexts as well. For example, the paper does not address how the proposed analysis would apply to scenarios where the domain shift is not solely due to pre-training data but also due to other factors such as spurious correlations within the source domains. Additionally, the current alignment score relies solely on cosine similarity loss. I believe it should also take into account the uncertainties exhibited by the model, which would help in making a better split. This consideration is important because it would factor in the calibration of the pre-trained models, which the current approach does not address. A model might have high cosine similarity for a wrong class, but a low confidence, which is not captured by the current approach.

Finally, it is not very clear to me whether combining both image similarity and alignment scores would provide a better indicator or does alignment score already take that into account. It is also unclear if the alignment score is robust to the choice of text prompts used for calculating the text embeddings. Also, I would recommend the authors toning down the statements like "DG has been solved with datasets like PACS etc". May be the takeaway that authors want to communicate is that some datasets should be dropped from future DG research and I think that is a better way to put it than the current style. As a community, DG needs new evaluation benchmarks that go beyond the now simple datasets and the excellent performance on these are hardly surprising given they have common categories that a pre-trained model would have been trained on.

Typos:

In the section 3.1, the equation of  perceptual similarity score is missing $\langle$.

Line 368, it should be ``between IP and OOP`` instead of  ``between OP and OOP``

### Questions
Please see weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors investigate the relationship between certain aspects of pre-training and domain generalization (DG). They observe that high DG performance is achieved only when there is strong alignment between image and class label text embeddings. Based on this finding and evaluations on splits with lower alignment, they conclude that current DG methods predominantly rely on pre-trained features and struggle to learn novel, generalizable features from source domains.

### Strengths
1. The observation that alignment in pre-training between image and text embeddings significantly correlates to domain generalization (DG) performance is a valuable contribution. 
2. The paper’s approach of dividing DomainBed datasets into In-Pretraining (IP) and Out-of-Pretraining (OOP) splits provides a novel lens for evaluating DG methods. This split reveals that while many models perform well on IP data, they struggle with OOP data, indicating that these models are not fully generalizing beyond pre-trained features.

### Weaknesses
Although the central idea of the work is interesting, I have several concerns with the work as follows:
1. **CNN Evaluations**: It would be valuable to experiment with pre-trained CNNs and CNNs trained from scratch using some of the DG methods, then evaluate them on their corresponding IP/OOP splits. Do differences in IP/OOP performance persist when training CNNs from scratch as compared to adapting a pre-trained CNN? And therefore does a freshly trained CNN learn more generalizable features than a pre-trained one? Specifically, it is unclear if the observed reliance on pre-training is specific to the CLIP architecture, or if it is a more general phenomenon. The paper should explore this by comparing the performance of CNNs trained from scratch to those fine-tuned from pre-trained weights, using the same DG methods and IP/OOP splits. This would help determine if the reliance on pre-training is an architectural artifact or a fundamental limitation of current DG methods.

2. **Zero-Shot Classification**: To better assess how pre-training alignment influences DG performance, it would also be helpful to conduct zero-shot evaluations on both the IP and OOP test sets of DomainBed using the same backbone as the DG methods. This could open up various observations, such as the proportion of zero-shot classified points in each split and the number of points that shifted from correct to incorrect (or vice versa) after DG. What additional insights about alignment and generalization could zero-shot evaluation on IP and OOP data reveal? For instance, are there cases where fine-tuning degrades performance compared to zero-shot, and how does this vary across IP and OOP splits? A detailed analysis of the confusion matrices between zero-shot and fine-tuned predictions would provide a more granular view of how DG methods are modifying the pre-trained representations.

3. **Revisiting the Image Similarity Hypothesis**: The image similarity hypothesis addresses the link between zero-shot generalization and similarity to the pre-training dataset but may not directly translate to DG. An analogous approach for DG might involve examining the perceptual similarity score between the target domain's evaluation set and the source domains' training set to see if it correlates with performance. Does this modified similarity hypothesis hold when applied to DG settings? Specifically, the paper should investigate if the perceptual similarity between source and target domain samples correlates with the performance of DG methods on those samples. This would help determine if the performance of DG methods is driven by the similarity between source and target domains, or if it is primarily determined by the pre-training alignment.

4. **Clarifying Key Takeaways**: While the paper presents some interesting insights, the main takeaways risk being obscured by details. A dedicated discussion section could enhance clarity by addressing questions such as (but not limited to): What insights from prior work connect pre-training with DG? What are the primary takeaways of this study, and how do they interrelate, and how would you contextualize with findings from prior work?

### Questions
Although the central idea of the work is interesting, I have several concerns with the work as follows:
1. **CNN Evaluations**: It would be valuable to experiment with pre-trained CNNs and CNNs trained from scratch using some of the DG methods, then evaluate them on their corresponding IP/OOP splits. Do differences in IP/OOP performance persist when training CNNs from scratch as compared to adapting a pre-trained CNN? And therefore does a freshly trained CNN learn more generalizable features than a pre-trained one?

2. **Zero-Shot Classification**: To better assess how pre-training alignment influences DG performance, it would also be helpful to conduct zero-shot evaluations on both the IP and OOP test sets of DomainBed using the same backbone as the DG methods. This could open up various observations, such as the proportion of zero-shot classified points in each split and the number of points that shifted from correct to incorrect (or vice versa) after DG. What additional insights about alignment and generalization could zero-shot evaluation on IP and OOP data reveal?

3. **Revisiting the Image Similarity Hypothesis**: The image similarity hypothesis addresses the link between zero-shot generalization and similarity to the pre-training dataset but may not directly translate to DG. An analogous approach for DG might involve examining the perceptual similarity score between the target domain's evaluation set and the source domains' training set to see if it correlates with performance. Does this modified similarity hypothesis hold when applied to DG settings?

4. **Clarifying Key Takeaways**: While the paper presents some interesting insights, the main takeaways risk being obscured by details. A dedicated discussion section could enhance clarity by addressing questions such as (but not limited to): What insights from prior work connect pre-training with DG? What are the primary takeaways of this study, and how do they interrelate, and how would you contextualize with findings from prior work?

I am willing to adjust my score if these concerns are addressed adequately.

### Soundness
2

### Presentation
2

### Contribution
3
