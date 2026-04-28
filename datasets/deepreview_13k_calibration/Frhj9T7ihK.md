# All Models are Biased, Some are More Transparent about it: Fully Interpretable and Adjustable Model for Mental Disorder Diagnosis

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 1, 3, 5

## Abstract
Recent advances in machine learning have enabled AI applications in mental disorder diagnosis, but many methods remain black-box or rely on post-hoc explanations which are not straightforward or actionable for mental health practitioners. Meanwhile, interpretable methods, such as k-nearest neighbors (k-NN) classification, struggle with complex or high-dimensional data. A network-based k-NN model (NN-kNN) combines the interpretability with the predictive power of neural networks. The model prediction can be fully explained in terms of activated features and neighboring cases.  We experimented with the model to predict the risks of depression and interviewed practitioners. The feedback of the practitioners emphasized the model's adaptability, integration of clinical expertise, and transparency in the diagnostic process, highlighting its potential to ethically improve the diagnostic precision and confidence of the practitioner.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this work, the authors study the interpretability and adaptability of neural network-based model NN-KNN. Because each parameter in the model has some semantic meaning, and the network relies on simple operations, it is interpretable. They then conduct a qualitative study about the utility of this model in mental disorder diagnosis.

### Strengths
- Paper is well-written and easy to follow
- The authors carry out a detailed qualitative study about how clinicians and experts could utilize such a model for diagnosis of a mental disorder

### Weaknesses
 - The sample size for training the model seems relatively small (117 cases), which might make the model less reliable. Additionally, the performance of the model is low. It does seem like there are larger datasets with similar questionnaire-based case-level answers and scores (for example, the DAIC WOZ dataset with PHQ scores/sub-component scores)
- It is not clear how the much the simplifying assumption of a global feature weighting (which makes the model interpretable) impacts performance
- The questions in the questionnaire seems particularly focused on the tunable weights component of the model, not the broader interpretability and trust
- The study might have been stronger if the authors compared with another potentially non-interpretable but simple model (like a decision tree or logistic regression model, all of which adjust their weights/structure during training)

### Questions
- Can authors clarify the impact of the global feature weighting assumption on performance?
- Can authors justify the use of a relatively small dataset in their study?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper discusses the problem of interpretability and explainability with AI, and studies the use of a neural network-based k-nearest-neighbor algorithm (NN-kNN) for diagnosis of mental illnesses and for interpretability and explainability through conducting a qualitative study.

### Strengths
The paper does address an important area of interest in psychiatry and AI. XAI is something that interests both mental health professionals and AI experts. With the paper studying NN-kNN, it does further contribute to the discussion of XAI and use of deep learning and machine learning in psychology and psychiatry. It also illustrates the use of a deep learning/machine learning model (NN-kNN) in diagnosing mental disorders, which is a very good contribution as it shows the use of a newly created AI model in psychiatry.

### Weaknesses
There are many significant issues with both the presentation and the soundness of the paper. There is also a concern tied to the soundness, which can impact the contribution of the paper. 

In terms of presentation, the paper was confusing to follow. This is due to the way that the paper is organized and the writing. I will mention only a handful of issues that contributed to the confusion. The paper would have been better organized if the authors swapped Section 2 and Section 3. That is, talk about the related work first, then talk about the model that the authors used. Additionally, it is very unclear why the authors went with NN-kNN instead of other interpretable machine learning algorithms. Also, not only does the title of the paper not make sense, but it doesn’t connect to the paper at all. More details on this will be provided in the next paragraph on soundness. Another thing is that since NN-kNN is considered both a NN and a kNN, the authors should include literature on the use and studies of kNN for mental illness diagnoses in the related work section. Doing so would help with understanding what work has been done for kNN and why kNN model would be suitable for mental illness diagnosis. One other thing is that the paper could use another round of proof reading. There are sentences that are written incorrectly. For example, it’s supposed to be “then invited practitioners to adjust the parameters based on their clinical judgements for depression” and not “then invited practitioners to adjust the parameters based on their clinician judgements for depression”. Lastly, in the introduction of the paper it says that they will conclude with discussions and future directions, but in the conclusion only one point is made about future directions and the things mentioned in the discussion are confusing. For example, in the conclusion it states, “We propose NN-kNN for mental disorder diagnosis not as a solution to the inherent challenges of diagnosis, nor solely for its predictive accuracy”. This is very confusing as the sections before that says otherwise. From what I understand, the sections before say that NN-kNN is a solution for mental disorder diagnosis because of its adjustability, interpretability, and explainability. I think the authors meant “We propose NN-kNN for mental disorder diagnosis as a solution to the inherent challenges of diagnosis, nor solely for its predictive accuracy”, but I can be wrong. 

In terms of soundness, the paper has several serious issues that need to be addressed before it can be published anywhere. I can’t mention all of them as that would make this review very, very long. Instead, I will just mention and detail two severe issues. One severe issue is the paper claims that “all models, including NN-kNN, are biased because they are at most as effective as the data they are trained on”. While this is true, the paper doesn’t adequately support the claim with any sort of evidence or anything. The paper only covers one model, and even for that the focus wasn’t on the biasness associated with the model, it was on its interpretability and explainability. In addition, there isn’t any discussion or anything about models being bias in the paper. It’s just mentioned once in the title and then once in the conclusion, which is a major problem. Not only does it make the paper confusing, but it also impacts the objective and cogency of the paper. This claim also raises a concern, which will be mentioned in the final part of this review. Because of the lack of coverage and studying conducted on the biasness of models, the title doesn’t make any sense. I would suggest removing “ALL MODELS ARE BIASED, SOME ARE MORE TRANSPARENT ABOUT IT” from the title and the parts of the paper that mentions biasness of models. 

Another severe issue with the paper comes from the claim the authors make in introduction, which is that the paper “introduces a novel approach to human-machine interaction drawing on insights and methodology from both AI and psychology”. This novel approach from what I understand is supposed to be the XAI approach. The paper itself doesn’t discuss the XAI approach at all. Instead, the paper presents an XAI model, shows its application in mental health, and shows its interpretability and explainability through a qualitative study. XAI approaches and XAI models are two different things. To help understand what I mean from this, I’ll use an existing XAI study. In the paper “Explainable AI meets Healthcare: A Study on Heart Disease Dataset” (URL to article: https://arxiv.org/abs/2011.03195), the authors do something similar to what the authors of the paper being reviewed are trying to do but for a AI model focusing on heart disease instead of mental illnesses. In that paper, they clearly state the types of AI models (XGBoost), and XAI approaches (contrastive explanation methods, example-based techniques, etc.) they will use in their study, and then discuss them accordingly. Going back to the paper being reviewed – the paper states the AI model used, but doesn’t state, explain or detail the XAI approach used. Consequently, the paper does not introduce a novel approach to human-machine interaction like the paper claims it does. Based on the qualitative study findings, it could be that the XAI approach that the authors are talking about is: 1) present the model to the clinicians; 2) let the clinicians adjust the parameters based on their clinical judgements for the mental disorder; 3) conduct a qualitative study with using the interpretative phenomenological analysis (IPA) approach. If that is the case, then it goes back to the presentation issues, which is that the way that the paper is written is in a way that does not make that clear. To make this clear, not only does the wording and structure of the paper need to be changed, but the paper should also include a part/section that covers the name of the XAI approach, an explanation, and enough details for others to be able to clearly understand and use the approach. 

The final part of this review is on a noteworthy concern with the paper. The concern is that if the paper is on how all models are biased and that some are more transparent about it than others like the title of the paper and the conclusion say it is, then that would make contribution of the paper worthless. It is already known within the AI, computer science, engineering, statistics, etc. communities that all AI models are biased because they are at most as effective as the data they are trained on, and that all AI models are not equally transparent about it. To prevent the paper from losing its value, I would recommend to the authors to not focus on that at all and instead focus on either NN-kNN being used as an AI algorithm suitable for mental illness diagnosis or the approach to human-machine interaction/XAI approach that they were trying to present.

### Questions
What's the exact objective of the paper? Is it to introduce a new XAI approach? To introduce a new AI model that explainable and can be used for mental disorder diagnosis? Or to show that all models are biased and that some models are more transparent about it than others?

Based on the information you provided, do you think that your study is easily reproducible? That is, do you think others will be able to easily conduct the experiment and get the same or similar results as your study did?

For suggestions on how to improve the paper, please see the weakness section.

### Soundness
2

### Presentation
1

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes to use a neural network based k-nearest-neighbor algorithm (NN-kNN), i.e., a k-nearest neighbor algorithm, that can explain each model decision with activated cases, and each activated case can be attributed to its feature distances with the query. 
As said by the authors "This study focuses on the interpretability and adaptability of NN-kNN to aid practitioners in mental disorder diagnosis."

Thus the main issue with the paper is that, even if very interesting as results, it only consists on the usage of NN-k-NN on a case study with interviews with prectitioners related to the interpretability. As a consequence, I do belive that ICLR is not the right venue for this contribution as it lacks of methodological novelty.

### Strengths
interesting as results

### Weaknesses
 The paper proposes to use a neural network based k-nearest-neighbor algorithm (NN-kNN), i.e., a k-nearest neighbor algorithm, that can explain each model decision with activated cases, and each activated case can be attributed to its feature distances with the query. 
As said by the authors "This study focuses on the interpretability and adaptability of NN-kNN to aid practitioners in mental disorder diagnosis."

Thus the main issue with the paper is that, even if very interesting as results, it only consists on the usage of NN-k-NN on a case study with interviews with prectitioners related to the interpretability. As a consequence, I do belive that ICLR is not the right venue for this contribution as it lacks of methodological novelty.

### Questions
Any novel contribution with the exception of the specific application?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the reader to the problem of black box models for mental-health issues, which medical professionals cannot use well because they do not offer the explainability of their decisions, with post-hoc methods not being able to fully explain how the decision of a model was made. To solve this they propose the use of a recent method NN-kNN. They use the model to qualitatively show how the experience of the medical practitioners’ changes by using this model and offer insight into the clinicians’ experience.

### Strengths
- Real-world applications of XAI are a very important and current topic.
- I really appreciate the evaluation on users that are a decent representation of the end-user of such an approach! This is severely lacking in XAI at this moment. Even with the compromises that have to be made

### Weaknesses
1. Since the NN-kNN model has already been quantitatively assessed by related work, the main contribution of the paper is the qualitative study.

2. The interpretation of the study’s results does not align with the results. The model’s strengths, specifically how each parameter of the model can help the practitioners in explaining the relevance of features to depression, seem to justify the use of the model in general. The general opinion is that the model can be useful in some specific cases however they would not generally trust it, specifically because while it is explainable, changing the parameters seems to help sometimes and is counterproductive other times.

3. It seems like changing the model’s weights to align more with clinicians’ beliefs confirms the clinicians’ bias even more (this issue is also raised by Dr. Yong). While your study provides novel results, the conclusions you draw are showing support of the model even though the corresponding clinician’s opinions mostly do not confirm that. You should be more critical of the model’s ability in helping a clinician. It seems like you agree with this in the first paragraph of the conclusion, however this is not visible from section 5 and from the last paragraph of the conclusion, where you again show strong support for the use of the model.

4. We have to at least acknowledge two limitations of the study methodology in the context XAI.
- There is more and more evidence that participants perception of how a XAI method helps is not really that correlated with actual performance. A good starting point: Amarasinghe et al.: "On the importance of application-grounded experimental design..."; Bucinca et al: "Proxy tasks and subjective measures...".
- Without a placebo or baseline method, we can't really know if the proposed method performs well because of the mere addition of some XAI method or if it performs better than any of the methods criticised in the paper. A good starting point: Eiband et al.. The impact of placebic explanations on trust in intelligent systems.

Therefore, a placebo (or at least some baseline) quantitative study with some real-world performance metric would be the next step.

Minor comments:
- A period is missing at the end of the sentence on line 197.
- The sentence in line 251 “The original dataset is …” could be rewritten. 
- Line 299: Space is missing after “:”.
- In line 422, and the whole section, the use “our” model is misleading, because the model was not created by the authors but was only evaluated.

### Questions
- The details of the study protocol are vaguely described in different parts of the paper or missing (How were they recruited? Demographics or any other meta-data?). I would prefer if the study was described in one place and in enough detail so it is reasonable to claim that it can be reproduced. Even if it all ends up in the Appendix.

### Soundness
2

### Presentation
3

### Contribution
2
