# Is self-supervision enough for training sentence embeddings?

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
In NLP, sentence embeddings are crucial for many tasks such as information retrieval, classification, clustering, or visualizing collections of texts. Currently, top-performing sentence embeddings are derived from pre-trained language models that undergo extensive supervised fine-tuning. This contrasts with computer vision, where self-supervised training has demonstrated remarkable success. Here we show that self-supervision alone can produce high-quality sentence embeddings, albeit slightly below those from state-of-the-art supervised models. We systematically compare several existing augmentation strategies for positive pair generation in contrastive learning and show that text crops strongly outperform popular dropout-based augmentation. Using text crops, well-performing embeddings can be obtained even when training from scratch without using pre-trained model weights, or when training a bare token embedding layer without any transformer architecture. Overall, we show that self-supervised learning allows rapid training of text embeddings of a given dataset.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates the potential of self-supervised learning (SSL) for generating high-quality sentence embeddings without relying on large, supervised datasets. The authors evaluate various SSL techniques, particularly focusing on text crops as a data augmentation strategy, and find it outperforms traditional dropout-based methods. Their findings suggest that SSL alone can yield competitive embeddings, with performance close to supervised models, and highlight that most improvements stem from generic sentence adaptation rather than domain adaptation. They also emphasize that embeddings can perform well even when trained from scratch or with minimal architecture.

### Strengths
- The paper compares multiple self-supervised learning approaches for sentence embeddings, providing insights into the effectiveness of different data augmentation strategies, especially text crops.

- It demonstrates that SSL can achieve sentence embedding quality close to supervised models, suggesting potential for relying more on SSL instead of supervised fine-tuning on large datasets.

### Weaknesses
 - The paper lacks originality, as most of its observations are already well-known in the research community. Self-supervised learning (SSL) has long been applied for training embeddings, and data augmentation techniques like text cropping and dropout are established as beneficial. The paper does not introduce new techniques or offer novel insights in this area.

- The study does not compare with current state-of-the-art models, such as BAAI's BGE models or commercial models (such as OpenAI and Voyage AI). Although it’s true that these models may be trained on different data, this lack of such results weakens the paper’s contribution. Its conclusions would be far more convincing if the proposed model was trained on the same or similar data as state-of-the-art models. 

- Additionally, the evaluation is limited, omitting several popular benchmarks; for instance, many datasets from the MTEB benchmark are not included in the analysis.

### Questions
N/A

### Soundness
2

### Presentation
2

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
This paper proposes fine-tuning sentence embeddings on consecutive text crops sampled from a dataset to improve embedding performance on that same dataset. The fine-tuning objective is InfoNCE with cosine as the similarity metric.  The evaluation is done on MTEB clustering tasks, recast as knn accuracy. The results indicate that, for a particular type of model (MPNet), text crops work much better than alternative strategies, such as dropout augmentation. The approach does not perform as well as SBERT. Further analysis leads to claims of generalization and looks at the performance at different layers.

### Strengths
1. Well written and easy to follow.
2. Thorough analysis and sound experiments.
3. Sufficient substance, including detailed appendix.

### Weaknesses
1. Overclaiming in the central claim: The title is honestly just completely wrong — the work is not about whether SSL is “enough” for training sentence embeddings. The work, if I put it bluntly, proposes a tried and trusted method in machine learning: tuning on the test set. Please correct me if I’m wrong, but the approach fine-tunes on the same dataset that it is evaluated on, using essentially the same objective, so it is no surprise that the method outperforms its (weak) baseline. I suspect that alternative approaches (eg finetuning pretrained BERT NSP/MLM-style on the same dataset) would also see gains. The authors argue that given that “SSL does not have access to class labels”, there are no “overfitting issues” — this is misguided: the central claim is directly related to “having access” to the test set. It would be really worrying if this method did not see improved performance. Why not do K-fold cross-validation to show that the approach holds up generally, with confidence bounds that show that differences in performance are statistically significant?

2. Lack of performance: Despite tuning on the test set, the approach does not outperform SBERT. What is the value of applying this method if I could simply apply SBERT? If the approach really works, couldn’t we apply it to SBERT to get SOTA? That would be valuable to practitioners. Similarly, you could evaluate whether downstream performance (eg in a RAG pipeline) improves if you adapt the embeddings to the domain.

3. Overclaiming in adjacent claims: The first sentence of the discussion “We showed that self-supervised fine-tuning on a minimal amount of data can lead to large improvements in sentence embedding quality” should be rewritten to “We showed that self-supervised fine-tuning on a given dataset improves sentence embedding quality on that dataset”. It is a much narrower claim. It is important to be precise. In l.375-77 “We conclude that the majority of the improvement was due to generic sentence-level adaptation, while domain adaptation had a smaller effect” — it’s still a similar domain, scientific literature clustering? This claim is much too strong. Related to the first point above, if you want to make this claim, you need to provide much more and much stricter evidence.


Minor:
- The correct citations for sentence representations/embeddings would be “SkipThought” (Kiros et al; 2015) and “Distributed Representations of Sentences” (Hill et al; 2016), definitely not Reimers et al.

### Questions
1. Why train using cosine but evaluate using Euclidean?
2. How was the learning rate chosen? Wouldn’t it be better to tune with a range of learning rates and pick the average (or best if you had a validation set)? How do I know that your dropout results are not poor simply because you selected your learning rate based on what worked best for cropping?
3. “It is unclear how their [SSL approaches] compares between each other and to the SOTA” (l. 43) — what is unclear and why? It’s phrased in a way where it needs a better explanation, and it’s not actually something you are really examining in this paper?
4. Why was MPNet chosen as the model to do the experiments with? No justification is given. I’d think it would make the paper stronger if you can show the same results for different models.
5. Specifically, how does this method perform when you apply it to SBERT rather than MPNet? If it improves SBERT, then this could be a valuable contribution?
6. What happens in section 4.1 when you use something like CCNews (or something even more out-of-domain) rather than PubMed?

### Soundness
2

### Presentation
4

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
This paper investigates whether self-supervised learning (i.e., using the domain corpus only) alone can produce high-quality sentence embeddings without extensive supervised fine-tuning (i.e., using a sentence pair dataset).
The authors re-explore the effectiveness of cropping-based augmentation for contrastive learning, demonstrating that this approach performs better than traditional dropout-based augmentation, SimCSE.
The paper shows that sentence embeddings can achieve comparable performance with supervised fine-tuning in some embedding tasks.
Key contributions include a systematic comparison of augmentation strategies and evidence that self-supervision can suffice for strong sentence representations.
This work challenges the need for supervised data in sentence embedding and offers insights for more efficient embedding training.

### Strengths
The paper demonstrates that self-supervised learning alone can produce high-quality sentence embeddings, reducing dependence on supervised data.

It systematically compares augmentation techniques, highlighting the effectiveness of cropping-based augmentation over traditional dropout methods used in SimCSE.

### Weaknesses
The research question "Is self-supervision enough for training sentence embeddings?" is not convincingly answered. While there are various experimental results in the paper, the insights derived from them seem somewhat lacking in coherence and strength with respect to the research question.

While the paper provides experimental findings, it lacks deep discussions or analyses about why it happens. For example, although the experimental results about the superior performance of cropping are somehow different from the conclusion in the SimCSE paper [Gao et al. 2021], there is no discussion or investigation about the reason. Gao et al. [2021] show that SimCSE is better than cropping and the next sentence pairing [Logeswaran and Lee, 2018].

>Note that we purposefully used the entire dataset first for self-supervised training and later for supervised evaluation. As SSL does not have access to class labels, this does not present overfitting issues.  For supervised evaluation, we used a 9:1 train/test split (using only labeled data).

Did the self-supervised training use test-split data too? If yes, the setting is a little tricky, and "As SSL does not have access to class labels, this does not present overfitting issues" is misleading. Even without access to the class labels, it should be a dataset leakage or a transductive learning setting.

>our own results showed that STS performance does not correlate with nearest-neighbor quality

Where is the result?


Does this self-supervised contrastive approach have any limitations? For example, is there any task where self-supervised contrastive learning may underperform supervised learning in MTEB or other tasks using embeddings?


Pre-training (e.g., language modeling) is also self-supervised learning. The title is misleading because it is ambiguous. Please consider different titles or wording to clarify it.

### Questions
>Note that we purposefully used the entire dataset first for self-supervised training and later for supervised evaluation. As SSL does not have access to class labels, this does not present overfitting issues.  For supervised evaluation, we used a 9:1 train/test split (using only labeled data).

Did the self-supervised training use test-split data too? If yes, the setting is a little tricky, and "As SSL does not have access to class labels, this does not present overfitting issues" is misleading. Even without access to the class labels, it should be a dataset leakage or a transductive learning setting.


>our own results showed that STS performance does not correlate with nearest-neighbor quality

Where is the result?


Does this self-supervised contrastive approach have any limitations? For example, is there any task where self-supervised contrastive learning may underperform supervised learning in MTEB or other tasks using embeddings?


Pre-training (e.g., language modeling) is also self-supervised learning. The title is misleading because it is ambiguous. Please consider different titles or wording to clarify it.

### Soundness
2

### Presentation
2

### Contribution
2
