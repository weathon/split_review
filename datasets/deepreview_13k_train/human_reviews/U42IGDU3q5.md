# CIRQRS: Evaluating Query Relevance Score in Composed Image Retrieval

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Composed Image Retrieval (CIR) retrieves relevant images using a reference image and accompanying text that describes how the desired images differ from the reference. However, the commonly used evaluation metric Recall@k only checks if the target image is retrieved, without considering the relevance of other images to the query, potentially leading to user dissatisfaction. We introduce Composed Image Retrieval Query Relevance Score (CIRQRS), an evaluation metric that scores each retrieved image based on its relevance to the query, offering a comprehensive evaluation. CIRQRS is trained using a reward model objective to prefer highly relevant, positive images over less relevant, negative ones. We propose a strategy motivated by self-paced learning to dynamically adjust the negative set based on the relevance of each image by using CIRQRS's current training status. To validate CIRQRS's ability to measure relevance, we created the human-scored FashionIQ (HS-FashionIQ) dataset and compared it with scores from human evaluators. CIRQRS correlates with human scores 2.625 times better than Recall@k, highlighting its superior ability to capture relevance. Additionally, by ranking images based on their CIRQRS, we check if the target image appears in the top k. The results show that CIRQRS achieves state-of-the-art performance on two representative CIR datasets, CIRR and FashionIQ.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper is about CIRQRS (Composed Image Retrieval Query Relevance Score), a novel evaluation metric designed for Composed Image Retrieval (CIR) tasks, where users search for images based on a reference image and text query. The proposal is to use CIRQRS instead of the traditional Recall@k metric, which only checks if a target image is retrieved in the set of retrieved images. Since typically only one image is the target one, Recall@k can't evaluate if the other retrieved images may be still relevant to the composed query. CIRQRS, instead, assesses the relevance of each retrieved image to the query. The metric is trained using a reward model and a self-paced learning approach, where the negative set is dynamically adjusted based on relevance, to ensure it can rank images by query relevance accurately. The paper also introduces human-annotated data defining the HS-FashionIQ dataset, where CIRQRS is also validated and showing state-of-the-art performance, i.e. better correlation with human preferences over Recall@k. The method is also evaluated on the standard FashionIQ and CIRR datasets, demonstrating state-of-the-art performance.

### Strengths
- The paper is timely for the CIR community, I found the paper well structured and well written. 

- CIRQRS addresses a core limitation in current CIR evaluation metrics by focusing on user-perceived relevance rather than simply on retrieving a target image. Traditional metrics like Recall@k fail to account for how well the retrieved set of images matches the user’s desired attributes, often leading to retrievals that technically meet the query but don’t align with user intent.

- Experiments on the FashionIQ and CIRR datasets show clear state of the art performance.

- The creation of the HS-FashionIQ dataset is a valuable contribution to the CIR field.

### Weaknesses
 - The idea of proposing a metric based on a specific method to automatically evaluate images of the set is interesting, but it raises issues regarding alignment. Proposing CIRQRS as a primary CIR metric can be deceptive for future proposed methods, as is derived from a method that aims to align with user judgments but cannot perfectly capture user-defined relevance. This creates a risk that future CIR models, optimized based on CIRQRS, will only be partially aligned with actual user expectations. Specifically, this metric’s reliance on training data and model biases (in this case, the HS-FashionIQ dataset) introduces a limited view of “relevance” that might not generalize well across diverse retrieval contexts. Consequently, using CIRQRS as the evaluation standard could narrow the objective of future CIR models to a version of relevance that aligns more closely with CIRQRS’s training biases than with diverse user intent, specifically that of the ~2,7k valid queries. I understand the reason to evaluate the entire set instead of the single target image, but I do not see why this specific method should be better to be used as metric instead of any other existing state of the art CIR methods and check their correlation. Perhaps a better approach would be to treat CIRQRS as a methodological advancement—an effective way to improve the relevance evaluation capability of retrieval models—rather than promoting it as a general-purpose metric for CIR.

- The novelty of the self-paced learning strategy is limited to the application of the general strategy (like for instance in Jiang, Lu, et al. "Self-paced learning with diversity" Neurips 2014) to the method.

Typos
- page 6, FasionIQ should be FashionIQ.

### Questions
- I understand the reason to evaluate the entire set instead of the single target image, but I do not see why this specific method should be better to be used as metric instead of any other existing CIR methods. Perhaps a better approach would be to treat CIRQRS as a methodological advancement—an effective way to improve the relevance evaluation capability of retrieval models—rather than promoting it as a general-purpose metric for CIR. Can you compare CIRQRS with existing CIR methods as evaluation metrics, discussing their respective advantages and limitations?

- Are the HS-FashionIQ dataset and code of the method going to be released?

- Do you see potential mitigation strategies for these alignment concerns, such as methods to reduce bias in the training data or plans to validate CIRQRS across a more diverse range of retrieval contexts?

### Soundness
3

### Presentation
4

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
This paper introduces CIRQRS into the CIR task, providing a user-centric evaluation metric. The HS-FashionIQ dataset with human scores was created to validate CIRQRS. The paper proposes a new strategy to refine negative images during training and improve query-based image ranking. Experiments on the CIRR and FashionIQ datasets validate the effectiveness of the proposed method.

### Strengths
1 ) The paper is well-written and has a clear structure. It effectively presents a novel CIR evaluation metric. The appendix includes additional details on the new dataset. \
2 ) The proposed method achieves top-ranking results, placing first and second on the FashionIQ and CIRR datasets.

### Weaknesses
1 ) The paper does not sufficiently highlight the novelty and effectiveness of the proposed approach. The authors should explain more to clarify the method’s advancements beyond merely introducing a new loss function. 
2 ) Since the goal is to introduce a new evaluation metric for CIR, a more detailed review of its effectiveness is needed. For example, testing CIRQRS on other models could help show its efficiency. 
3 ) In Tables 2 and 3, the paper wants to demonstrate that CIRQRS is more effective than R@5, but the process by which these data were calculated should be clarified in greater detail. Since R@5 is an important point here, it would also help to show a comparison of R@5 results on the FashionIQ dataset as in Table 4 with other methods.

### Questions
The paper contains minor grammatical errors. For example, on page 2, line 85, "Additionally, when CIRQRS is higher on a set of retrieved images" should use "was" instead of "is," and "limitation" on line 95 should be "limitations."

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a new evaluation metric for Composed Image Retrieval (CIR) called CIRQRS (Composed Image Retrieval Query Relevance Score), aimed at overcoming limitations of the commonly used Recall@k metric. The authors offer a new dataset HS-FashionIQ, which scores different candidate groups of images of a few CIR models. The authors shows SoTA performance in most metrics of the CIRR and FashionIQ datasets.

### Strengths
- The idea of relevance score in image retrieval is good, especially human preference of retrieved results. 
- Authors show SoTA performance on the main CIR datasets
- Training procedure involving hard-negatives is shown in the paper, suggest a better training paradigm to CIR.

### Weaknesses
General:

- Line 037: The comment “CIR provides a more intuitive way to express search intent” - seems subjective. While CIR does enable a multimodal query format (image + text), which can simplify certain cases (e.g., describing a specific T-shirt design that may be hard to convey in words alone), using text as a query is often more intuitive for me (text-to-image retrieval task). I recommend rephrasing this sentence to clarify the intended advantage.
- Line 042: The example provided is helpful, but it would be especially beneficial to include the ground truth target image for clarity. This is important for readers who may not be familiar with the dataset.
- Related Work:  It would be more logical to introduce the “Vision-Language Foundation Model” paragraph first, as it provides the foundation for most CIR-related studies.
- Line 227: The claim that “as images with higher CIRQRS than the target are likely to be highly relevant after sufficient training” needs support. Consider using “Precision@K” labeling, accounting for false negatives (images that match but are not labeled as such). Otherwise, higher scores than the GT image could just be noise or indicate an imperfect model.
- Line 262 refers to Figure 5: This example is unclear. What distinguishes set A from set B? Why do the same images have different CIRQRS scores across sets? What is the GT image, and what do the User Preference symbols (v or x) mean? This example should clarify the annotation process (line 262), but it currently feels confusing.
- The scores CIRQRS-model outputs, to my understanding, are just similarity scores as any other casual CIR model produce. The authors shows SoTA performance, in some metric, with their different training procedure that considers “hard-negative” samples. The authors claim to introduce a new evaluation metric that “overcomes the limitation of Recall@k” (line 479), but in practice, all different model in the paper was evaluated using the Recall@K metric and not the new one.

Annotations: 
- I have a major concern about the annotation process. Image Retrieval (IR) datasets often include many “false-negative” examples—images labeled as “negative” by default but which humans would consider “positive.” Ideally, a human annotator would review the entire image corpus for each query to mark each image as positive or negative, but that’s impractical. While CIRQRS score annotations are valuable for the community, I worry they may still include “false-negatives,” where more positives are marked per sample. I suggest an extra step to label images in the candidate set as positive or negative, alongside CIRQRS score, to better distinguish true positives from “relevant but negative” images.

Evaluation:
 - Tables 4 and 5 compare different methods to the paper results (CIRQRS). As described in Sections 3 and 5, the authors leveraged the BLIP-2 foundation model for the the CIR task. Despite being trained differently, it is essential to present the BLIP-2 baseline performance on these datasets, compared to current CIRQRS. It will clarify from where the improvement in results comes from: theoretically, one may suspect that the BLIP-2 model (that shown to be a strong backbone) may outperform the CIRQRS baseline which maybe only decreases the result of its backbone. On the other hand, the CIRQRS baseline may improve BLIP-2 baseline in a large margin, due to a better training procedure. It is an essential comparison to make here, which is missing in the evaluation tables.

- Just to make it clear: does the authors method rely solely on the FashionIQ training set, or it also trained on HQ-FashionIQ?
* how beneficial would it be to train on both HQ-FashionIQ and FashionIQ? Since your method selects “hard negatives” using the scoring model (Sec 3.2), could adding HQ-FashionIQ data improve the Recall@K metrics?

Evaluation on HS-FASHIONIQ:

- In the paper, “CIRQRS” is referred as a score, metric and as a model/method (based on BLIP-2)..  Please clarify this usage in context or consider renaming (e.g., “CIRQRS-Model”). Specifically, in Sec 5.2, you compare Recall@K and CIRQRS metrics to human-preferences. What model was used for these results? What is the actual values of these numbers on this model, and how it changes across different models?
It is not fully clear to me.

Correlation with Human Score (Sec 5.2):

I’m not convinced this experiment is necessary. Different metrics assess different things: Recall@K measures how many GT targets appear in the top K, while human preference between two sets of results measures, indeed, human preference, and takes into account only top-k results. Imagine a bad CIR model that leaves all GT targets least in the results, but still top ranks “relevant” images based on shallow chartersitic such color - in this case, the Recall@K should be very low, while human preference will be high. It would be more “comparable” to conduct this experiment with Precision@K metric (but, it is not widely used as Recall@K).


I think the paper idea is good and important, but the flow is not entirely clear. The authors shall distinguish between method, metric and score, and provide more evidence for some claims. For example, since the CIRQRS metric presented as the main contribution in the paper, it is essential to include a substantial comparison of CIRQRS values across several CIR models. Without this, it is unlikely other CIR studies would adopt this metric, which would limit the paper’s impact.

### Questions
1. Eq. 1: “the inner product of the query and image embeddings” - I assume you mean “the inner product of the image embeddings of the query and the candidate image.” Is that correct?

### Soundness
2

### Presentation
2

### Contribution
2
