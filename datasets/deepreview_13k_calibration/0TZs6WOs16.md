# Hyperbolic Embeddings in Sequential Self-Attention for Improved Next-Item Recommendations

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
In recent years, self-attentive sequential learning models have surpassed conventional collaborative filtering techniques in next-item recommendation tasks. However, Euclidean geometry utilized in these models may not be optimal for capturing a complex structure of the behavioral data. Building on recent advances in the application of hyperbolic geometry to collaborative filtering tasks, we propose a novel approach that leverages hyperbolic geometry in the sequential learning setting. Our approach involves transitioning the learned parameters to a Poincar\'e ball, which enables a linear predictor in a non-linear space. Our experimental results demonstrate that under certain conditions hyperbolic models may simultaneously improve recommendation quality and gain representational capacity. We identify several determining factors that affect the results, which include the ability of a loss function to preserve hyperbolic structure and the general compatibility of data with hyperbolic geometry. For the latter, we propose an empirical approach based on Gromov delta-hyperbolicity estimation that allows categorizing datasets as either compatible or not.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents an approach that leverages hyperbolic geometry for extending recommendation systems. The idea is that the hyperbolic layer will capture structural properties of the approach. The authors are based on one base model, SASRec, which they extend. They perform experiments on multiple datasets with mixed results.

### Strengths
The paper is generally well written which I greatly appreciate. It contains some interesting ideas of how to extend recommendation systems to take advantage of hyperbolic geometries. There is quite good coverage of related work even though I would like to see references from practical work. The authors could check recent papers in recommender systems from Pinterest, Airbnb, etc. where there are also real use-cases.

### Weaknesses
My first comment is that the originality of this work is quite limited as other works proposed hyperbolic recommenders. The addition of this paper is the extension of SASRec with a hyperbolic layer as stated at the last sentence Section 5. I am not sure how much originality is there.

As mentioned previously, it would be great if the authors could add some references from recent works of recommender systems on real use-cases just to contrast it with the current SOTA in real applications. Do we expect that such an approach would be viable or would give better online results in a real system?

In Section 3.2 authors mention that negative sampling is typically implemented using uniform sampling which is rarely the case for real use cases where one employs heuristics in order to sample hard negatives and learn more robust models.

I do not understand the statement "distributional properties of items based on the popularity hierarchy". What exactly someone would like to capture here? And why popularity cannot be captured with non-hyperbolic geometry?  I cannot see how this would help a recommendation system.

In the experimental part I would add the following baselines:
- Most popular
- Co-occurence baseline, where one would recommend the property that co-occurs more often with the last item in the sequence. This is often a very strong baseline.

Adding challenging datasets also would be great. In recent years many datasets have been released that can be used for sequential recommendation. For example:
- https://xmrec.github.io/wsdmcup/
- https://github.com/ExpediaGroup/pkdd22-challenge-expediagroup

Generally the results are no convincing/great. It seems in some cases there is some slight improvement (third digit). And the classification in good and bad datasets is arbitrary. What is the hypothesis that in one dataset of Amazon data the hyperbolic version is better and in another one (like Products) is not better? This seems random.

### Questions
Please see weaknesses section for the questions.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a hyperbolic architecture for sequential self-attention next-item recommendation applied to SASRec. Specifically, they replace the output prediction layer in SASRec with predictors in hyperbolic space. Besides, they adjust the machine precision setting to obtain a more accurate estimation of hyperbolic space curvature. Experimental results demonstrate that HSASRecCE can outperform SASRec with small embeddings.

### Strengths
1. The paper is the first work to extend the sequential self-attention next-item recommendation architecture by the hyperbolic prediction output layer.
2. The paper reveals that negative sampling harms the performance of hyperbolic models.
3. The paper adjusts the machine precision setting to obtain a more accurate estimation of hyperbolic space curvature, which can measure the hyperbolicity of a dataset and improve the performance of the hyperbolic model.

### Weaknesses
1. Limited novelty. The work simply replaces the output layer of SASRec with hyperbolic prediction layers. Besides, the used hyperbolic prediction layers(hyperbolic hyperplane and MLR) have been widely applied in other works. The contribution of this article needs to be re-condensed.
2. The paper measures the hyperbolicity of the dataset simply by δ-hyperbolicity but does not clarify the inherent hyperbolicity of the recommendation dataset. The utilization of hyperbolic space in this setting is questionable. 
3. The paper does not explain and analyze why negative sampling harms the performance of the hyperbolic model, which does not occur in the Euclidean model.
4. The paper does not optimize the model with the compatibility of data with hyperbolic space, though it tries to obtain a more accurate estimation of the curvature of hyperbolic space. The role of curvature is not fully used in the recommendation design.
5. The authors state to apply hyperbolic geometry in the sequence learning settings. However, the applicability of the proposed strategy to the state-of-the-art recommendation models is questionable.
6. The experimental results are not convincing. The comparison seems to focus on PureSVD-N and EASEr from 2019 (4 years ago). It is a bit misleading since many works have emerged in the past 4 years (see [1, 2] for example).

### Questions
Please refer to Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper extends SASRec [1] in hyperbolic space by adjusting the output prediction layer for next-item recommendation task. 

[1] Self-attentive sequential recommendation. ICDM 2018.
[2] HME: A Hyperbolic Metric Embedding Approach for Next-POI Recommendation. SIGIR 2020.

### Strengths
Strengths:

-	The approach is straightforward and well-explained
-	The writing is clear and on point
-	The authors conducted experiments on various datasets for benchmarking

### Weaknesses
Weaknesses:

- In my opinion, the contribution is marginal while the only change is the prediction layer (Eqn (6)). The modification, while seemingly straightforward, lacks a strong justification for its effectiveness beyond empirical results. A deeper theoretical analysis of why this specific change in the prediction layer leads to performance gains in hyperbolic space is needed. It's not clear if the observed improvements are due to the geometry itself or simply a better parameterization of the output layer.
- In Section 4.1, the authors mentioned that “we limit the allowed embedding size values to (32, 64, 128), while the Euclidean models explore higher values from (256, 512, 728)”. More deeper analyses would make the paper stronger. The rationale for limiting the embedding size in hyperbolic space is not sufficiently explored. It is unclear why a smaller embedding size is expected to be sufficient in hyperbolic space, and how this relates to the intrinsic dimensionality of the data. A more rigorous analysis of the impact of embedding size on model performance in both Euclidean and hyperbolic spaces is necessary.
- In Section 6.2, Table 1 shows that hyperbolic based solutions do not always show remarkable performance. It would be better if the authors also dive deeper into the details of the datasets / models, and evaluate about which scenarios can make hyperbolic based methods perform the best. The paper lacks a detailed analysis of the datasets where hyperbolic models underperform. It is crucial to understand the characteristics of these datasets that make them less suitable for hyperbolic embeddings. A more thorough investigation into the interplay between data properties and the effectiveness of hyperbolic models is needed, including a discussion of potential dataset biases or structural properties that might favor Euclidean spaces.
- Ablation studies should be further given. For example, can we generate visualization for user / item embeddings to observe the ‘before’ and ‘after’ changing the prediction layer? The absence of ablation studies, particularly regarding the impact of the modified prediction layer, limits the understanding of the model's behavior. Visualizations of user/item embeddings before and after the change could provide valuable insights into how the hyperbolic space is being utilized and whether the embeddings are capturing meaningful relationships. Without these studies, it is hard to isolate the effect of the proposed change.
- Missing citations / baselines such as [2]

### Questions
Please see my comments above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper makes the following main contributions:
- The paper proposes a new approach for the next-item recommendation that combines sequential self-attention with hyperbolic geometry. The base architecture is SASRec, with modifications only to the final prediction layer.

- The prediction layer is adapted to learn how to separate hyperplanes in the Poincaré ball, enabling a linear classifier in this non-linear hyperbolic space. This allows the model to leverage the benefits of hyperbolic geometry, like hierarchical representations and dimensionality reduction.

- An approach to estimate the hyperbolicity of datasets using Gromov delta-hyperbolicity is presented. Datasets are categorized as "good" or "bad" for hyperbolic modeling based on this.

### Strengths
The proposed approach is straightforward to implement, requiring only changes to the prediction layer of SASRec. This makes adoption more practical.

Analysis of dataset hyperbolicity provides insights into when these models can be expected to work well or not. The categorization into "good" vs "bad" datasets is useful.

### Weaknesses
There is no ablation study on the effects of different space curvature values. Varying the curvature and linking performance to estimated dataset hyperbolicity could provide better insights.

The negative sampling analysis seems incomplete. Different sampling strategies besides uniform should be evaluated before concluding their effects.

The approach for estimating dataset hyperbolicity lacks analysis of computational complexity and scalability. This could limit practical applications.

### Questions
Please solve the weakness listed above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
