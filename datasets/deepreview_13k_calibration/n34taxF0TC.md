# Shedding Light on Time Series Classification using Interpretability Gated Networks

- Decision: Accept
- Avg Score: 6.60
- Scores: 6, 5, 6, 8, 8

## Abstract
In time-series classification, interpretable models can bring additional insights but be outperformed by deep models since human-understandable features have limited expressivity and flexibility. In this work, we present InterpGN, a framework that integrates an interpretable model and a deep neural network. Within this framework, we introduce a novel gating function design based on the confidence of the interpretable expert, preserving interpretability for samples where interpretable features are significant while also identifying samples that require additional expertise. For the interpretable expert, we incorporate shapelets to effectively model shape-level features for time-series data. We introduce a variant of Shapelet Transforms to build logical predicates using shapelets. Our proposed model achieves comparable performance with state-of-the-art deep learning models while additionally providing interpretable classifiers for various benchmark datasets. We further show that our models improve on quantitative shapelet quality and interpretability metrics over existing shapelet-learning formulations. Finally, we demonstrate the capability of our models to provide interpretability in a real-world application using the MIMIC-III dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the Interpretability Gated Network (InterpGN), a time-series classification framework that implements interpretability with sufficient performance guarantees. InterpGN integrates a deep neural network and a concept-based shapelet bottleneck model (SBM) to model patterns for classification using interpretable shapelets (i.e., unique time-series subsequences). Here, linear classifiers are simple to interpret because the importance of each feature is directly reflected in the magnitude of its weight. By integrating predicates into a mixture of experts (MoE) framework, InterpGN uses a gating function to assign tasks based on the model's confidence.

### Strengths
1. The gated mechanism is novel. Such a gating function based on SBM's confidence level preserves interpretability for simple cases while calling on the DNN for complex samples.

2. The motivation for adding interpretability to time-series classification is compelling, specifically since the link between capturing temporal patterns and classification outcomes is often not intuitive.

3. New quantitative metrics are used to assess shapelet quality and interoperability, demonstrating improvements over existing models.

4. InterpGN achieves comparable or superior accuracy on benchmark datasets.

5. The manuscript is well-written, with a clear presentation of concepts and methodologies. Additionally, the authors effectively visualize the schematic concepts of the paper (Fig. 1, 2, and 4). These illustrations clearly present the core ideas.

### Weaknesses
1. Though interpretability is a primary focus, InterpGN reintroduces black-box elements due to the integration of DNN outputs. This can override shapelet-based explanations in challenging cases. The interpretability is particularly compromised when SBM fails to capture patterns adequately, and the model defaults to the DNN expert without sufficient transparency regarding how the shapelet information influences the final decision. Specifically, the gating mechanism, while novel, doesn't provide a clear understanding of how the DNN's decision is modulated by the shapelet-based model when the confidence is low. It's unclear if the DNN is learning to correct the SBM's mistakes or if it is simply bypassing the interpretable features altogether in these cases.

2. The authors claim that creating predicates using the RBF kernel allows for more flexible matching with the original time-series compared to the threshold distance-based shapelet approach. However, I'm not fully convinced that Fig. 3 effectively illustrates this intuition. In MTS classification, there could be relatively less important features (i.e., those that do not impact the classification results), so what's the justification for requiring a shapelet for every variable? This seems like an unnecessary constraint that could lead to overfitting or the learning of irrelevant shapelets, especially if the L1 regularization is not strong enough to prune these features effectively.

3. Interpretation of Fig. 6 may seem forced; the claim that the "OS" variable is steady appears subjective, as the left side actually seems steadier than the right side. The interpretation relies on a qualitative assessment of the time series, which is not robust. A more rigorous analysis, perhaps involving statistical measures of variability, would be necessary to support this claim.

4. I'm entirely persuaded of the usefulness of "global explanation." As the authors explain well, local explanation is valuable as a post-hoc method for identifying the shapelets that most influenced the classification outcome. However, compared to recent time-series classifications that achieve high performance, what is the necessity of a global explanation? Further intuition on this point would be helpful. It's not clear how a global explanation adds value beyond the local explanations, especially if the local explanations are already providing insights into the most influential shapelets for each instance.

5. The performance improvement in terms of average accuracy in Tab. 1 seems too small. Since InterpGN uses both FCN and SBM, i.e., more parameters, we expect the performance improvement to be significant. However, the improvement is only 0.6% in terms of average accuracy. The added complexity of the model should justify a more substantial improvement in performance, and the marginal increase raises concerns about the practical utility of the proposed approach.

### Questions
1. How do we get shapelets? Is it a learnable parameter?

2. Why is the length of the shapelet considered as in the paper? Why is the minimum length fixed at 3?

3. Can InterpGN be applied to other time-series applications? I'm really curious to see if InterpGN performs well in time-series anomaly detection (since it's a one-class classification) or some future prediction tasks.

4. Where and how were the hyperparameters introduced in Eq. (5) chosen?

5. Fig. 5 (c) is interesting, but I have a question: low $\eta$ (low transparency; low confidence of expert) data relies on the DNN output. However, line 388 states, 'Intuitively, predictions of opaque points are interpretable as they are based on SBM, while transparent points rely more on the DNN,' which is confusing.

6. Considering that the MIMIC-III in-hospital mortality dataset is imbalanced, how does InterpGN address potential issues in capturing representative shapelets for the minority class, and does it risk overfitting the majority class?

7. Why was an ablation study on the effect of L (length candidates of predicates)?

8. As the authors highlighted in the limitations section, a drawback of InterpGN is that its interpretability is somewhat rigid (e.g., sequences belonging to a certain class must have or must not have certain predicates). Given this, could InterpGN be utilized as a feature selection tool to enhance classification performance rather than the interpretability tool?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This article proposes Shapelet Bottleneck Model  (SBM) a framework for time-series classification that produces an interpretable model. This framework is based on the adaptation of an existing model (Learning Time-Series Shapelets, LTS). The main idea is to modify shapelet learning by introducing a Gaussian kernel to measure the distance between the time-series and the shapelet, as well as a cost function to ensure diversity among the learned shapelets and greater sparsity in the model's use of shapelets. The learned shapelets are then provided to a linear classifier. An analysis of the weights allows identifying the shapelets that are important for classification. The second contribution is the introduction of a Mixture-of-Experts model and a gating function to ensure good classification performance when the first model is insufficient. The approach is evaluated on 30 common datasets compared to state-of-the-art algorithms.

### Strengths
* The paper addresses an important topic regarding the explainability of classification in time series.
* The evaluations conducted are numerous and compared to a sufficient number of state-of-the-art algorithms.
* The experiments are well analyzed, and the qualitative analyses are welcome.

### Weaknesses
 * The state of the art is relatively brief, while there is a wealth of literature on the subject. However, the main works are well cited.
* The model section of the paper is relatively difficult to read. For SBM, even though it is an iteration of LTS, it would have been useful to say a few words about end-to-end gradient shapelet learning (at least a reference to the LTS paper in this section). Specifically, the description lacks detail on how the shapelets are actually optimized within the SBM framework. The paper mentions a Gaussian kernel, but it is unclear how this kernel is integrated into the loss function and how it affects the shapelet learning process. A more detailed explanation of the gradient flow with respect to the shapelet parameters would be beneficial.
* The Mixture-of-Experts (MoE) section is really hard to follow due to the very limited space given to it. Very few details are provided about this part. The description of the gating function is particularly vague. It is not clear how the sparsity of the SBM output is actually measured and used to weight the contribution of the DNN expert. The paper should provide a concrete mathematical formulation of the gating mechanism and explain how it is trained jointly with the other components of the model.
* The main contribution of the paper, given the stated objective — an interpretable time-series classification model — is the proposal of a Gaussian kernel distance rather than an Euclidean distance in the LTS approach, which seems rather modest. While the use of a Gaussian kernel might improve performance, the paper does not provide a strong justification for why this specific kernel is superior for interpretability compared to other distance metrics or kernel choices. The novelty of this contribution should be more clearly articulated.
* On the experimental side, given the similarity of the approach with LTS, why not use LTS as a baseline as well? The absence of a direct comparison with the original LTS method makes it difficult to assess the true impact of the proposed modifications. It is important to isolate the effect of the Gaussian kernel and the proposed training procedure by comparing against the original LTS implementation.
* Some results are unclear: what exactly do "Wins/Draws" and "Losses" mean in Table 1? What does the p-value refer to? The paper lacks a clear definition of these metrics, making it difficult to interpret the results. A more detailed explanation of the statistical tests used and the meaning of the reported values is necessary.
* Unless I am mistaken, there is no comparison with other interpretable methods for the interpretability results. The paper should include a comparison with other interpretable methods using quantitative metrics for interpretability, not just qualitative analysis. This would allow for a more objective assessment of the proposed method's interpretability.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Interpretability Gated Network InterpGN, a gated network that combines a DNN with a  Shapelet Bottleneck Model (SBM). This is a concept bottleneck model that makes predictions based on the presence or the absence of different shapelet.
 
# Method
### Shapelet-based TS Modeling
- a multivariate TS is modeled as independent univariate channels.
- they learn learn $K$ shapelets for each possible length $L$ and channel $M$ i.e each shapelet can be viewed as  $s_{k}^{m,l}$
- the paper introduces a distance metric $d_{i,k}^{m,l}$ between the shapelet $s_{k}^{m,l}$ and input $x_{i,t:t+l}^{m}$ which is the Euclidean distance between the two. 
- they also introduce Shapelet Transform on the distance to measure the likelihood that $s_{k}^{m,l}$  exists in $x_{i}^{m}$. This is defined as predicates $p_{i,k}^{m,l}$
###  Shapelet Bottleneck Model
- the predicates $p_{i}$ are fed into a linear layer to compute the outputs $r_{i,c}$ for each channel $c$
- the final loss is cross entropy loss between $(r_i,y_i)$, Shapelet diversity loss and  L1 regularization loss on classifier weight $\mathcal{L}_{\text{int}}$.
### InterpGN
- The paper introduces a DNN expert along with the SBM and a gated network that chooses to use either the SBM or the DNN.
- To choose whether to use the SBM or DNN, the paper proposed measuring the confidence of the SBM by measuring the diversity of $\hat{r_i}=\text{softmax}(r_i)$ they use a modified Gini Index that measures the diversity of variables in $\hat{r_i}$ which is given in equation 6  $\eta(x_i)$.
- The final output is a  hybrid between DNN output $z_i$ and the SBM output $r_i$ i.e $h_i = r_i . \eta(x_i) + z_i . (1-\eta(x_i))$
- The final loss is $\mathcal{L}_{\text{hybrid}}$ which is the weighted sum of SBM loss and the cross-entropy between $(h_i,y_i)$

# Experiments  
- **Classification** they evaluate the performance of InterpGN and SBN on 30 datasets from the UEA multivariate TS, overall InterpGN outperforms the baseline methods and SBM achieves comparable performance.
- **Interpretability** SBM offers global-level explanations by looking at weights of different shapelets in the linear layer for a given class. They also show that samples for InterpGN that rely most on DNN are usually on cluster boundaries, meaning InterpGN learns to use SBM for easier-to-classify samples while relying on the DNN to classify difficult boundary samples.
- **MIMIC-III dataset** The paper shows that InterpGN outperforms DNNs in terms of accuracy.

### Additional Metrics:
- **Interpretability metric** this measures the interpretability of SBM by measuring how sparse the weights of the linear model are.
**Shapelet quality metric** This measures how close the shapelets are to the actual time series.  

# Results and conclusions 
Through ablation studies, they found the following:

- Increasing the number of shapelets (K) in SBM enhances accuracy and shapelet quality by capturing more specific patterns; it reduces $\eta$ but seems to reduce sparsity, reducing overall interpretability. 
- The cosine decay schedule of loss weighting $\beta$ in InterpGN results in slightly worse accuracy but improves shapelet quality and interpretability by focusing SBM training on confidently predictable samples, though it reduces the utility rate $\eta$.
- Using RBF to get the predicate outperforms linear ones.
 -  The parameter  ϵ influences the steepness of RBF kernels, with larger  ϵ values improving shapelet quality but reducing accuracy significantly.
- There is an interpretability accuracy trade-off when increasing Weight regularization.
- Shapelet diversity regularization does not add any benefits.

### Strengths
## Originality -- High
-  The paper propose a shapelet bottleneck model (SBM) which is original extension to CBM for time series.
- The gating method used to decide between DNN and SBM in equations 6 and 7 original and quite smart to take into account how confident the SBM for gating.
- SBM offers several forms of interpretability that might be very useful for downstream applications.

## Quality -- High
- Strong empirical results and through experiments.
- Excellent ablation studies.

### Weaknesses
## Significance -- Low
- My main issue with the paper is that InterpGN is not interpretable at all. It makes sense that it will outperform regular DNNs because the prediction for a single sample comes from both SBM and DNN. This is unlike IME (Ismail et al., 2023), which also combines interpretable models with DNNs, but in IME case, it could still say there is a level of interpretability since for a single sample, only a single expert is used, but combining outputs from different models removes any forms of interpretability. So the paper up SBM was great, and it showed very useful interpretability forms, but InterpGN makes the model a black box again...

- There are also some justified choices, for example:

    -  Why have $\mathcal{L}_{\text{div}}$ while ablation studies show it didn't really help in any way?
     -  Why use $\eta$ as a gating function and not a linear model?

- The code was not provided to replicate the experiments.

## Clarity  -- Medium
- Please see the questions section

### Questions
- How are the shapelets learned? i.e., how do you get $s_{k}^{m,l}$? Are they randomly initialized for each channel and learned through back prob?
 
- Text is unclear in section 3; in the paper, lines 156-160, it is mentioned "Existing methods gain different levels of interpretability by inputting interpretable features (Zuo et al., 2023) into a simple model such as a linear layer (Ma et al., 2020; Qu et al., 2024)
or SVM (Li et al., 2021). However, such approaches usually fail to provide explanations of their  predictions based on distance features. For the interpretable expert, we build logical predicates using shapelets, and the classifier directly provides rule-like explanations." From this paragraph, one can assume that the classifier on top of the shapelets is not a linear classifier but something else. But in equation 3, it was mentioned that a linear classifier was used on top of the shapelets, so it is a bit confusing... 

- In figure Figure 5, what do different colors correspond to? Are they different classes?

- Typos:
    -  line 98 and line 285 interpretablity 
    -  line 437 intepretability 
    -  line 533 interoperable

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a self-explaining framework for time-series classification using shapelets as the form of explanations. While the concepts of CBM (Concept Bottleneck Models) and shapelets are not novel individually, successfully combining them into an end-to-end framework adds value. The overall model design is reasonable, though some details are questionable. The paper presents evaluation results showing similar or superior predictive performance but lacks sufficient experiments on explainability, even though explainability is its main selling point. I believe that the authors will address these shortcomings in the discussion period.

### Strengths
1. High predictive performance

2. The exploitation of shapelets as "concepts" of CBMs.

3. The proposed framework provides both local and global explanations.

4. The overall manuscript is clearly written.

### Weaknesses
1. In the worst case, the model can collapse (i.e., fail to find good shapelets), and $\eta$ appears to be always $0$ (e.g., Handwriting dataset in Figure 10). In this scenario, the model fully relies on the performance of unexplainable DNN module, while providing the explanation from SBM that does not affect the final model decision. Do you provide the value of $\eta$ in your explanation? Is there any design consideration to prevent such a collapse? Please see [1] and [2] for references explaining why it is problematic if there is another direct pathway from input to prediction.

2. The computational complexity of the shapelet diversity loss seems to be $K^2 \times M \times L$. This might incur a huge computational burden. While using a small K may reduce the complexity, this introduces another weakness.

3. A small number of shaplets (K) are used in the implementation, but this significantly limits the expressiveness of the model and may cause it to miss important features in practice. The experiments only consider $K=5$ and $K=10$; the authors should present more extensive result with larger values of $K$, such as $K=100$ or $K=1000$, if possible. 

4. This framework cannot capture the interaction between shapelets, since it uses a simple linear layer for the final prediction. However, the co-existence of relevant shapelets can meaningfully increase the model confidence in practice.

### Questions
**Related Work**

1. I recommend including a discussion about papers that propose CBM-like self-explaining frameworks that use logic rules (e.g., [2] and [3]).

**Method**

2. Why do you use Euclidean distance for measuring the "distance" between shapelets and inputs? In time-series data, two signals might look similar but have different offsets, leading to a large Euclidean distance. Did you also try cosine similarity or Pearson correlation?

3. The current model only considers the existence of the shapelet. However, isn't a shapelet that appears at the end of the input more important, considering the characteristics of time-series data? Is there any way to include the location of the shapelet in the explanation?

**Experiment**

4. An ablation study on the model components is needed. What is the performance of the DNN-only model and the SBM-only model?

5. The suggested interpretability metric using $w$ is unconvincing. The scale of the weights might change according to the training setup or dataset, and the thresholds are set empirically. Measuring the skewness of $w$ using the Gini index (which would be similar to $\eta$) would be more convincing.

6. While the sparsity of weight $w$ might increase interpretability, it is just one aspect. A more comprehensive evaluation of interpretability is needed, possibly through a user study.

7. In the XAI domain, "faithfulness" - the degree to which an explanation reflects the model's decision - is an important criterion for evaluating explanations. An evaluation of faithfulness is needed. It would be beneficial if the authors followed metrics from existing literature [4].

**Minor Questions**

8. Why do you refer to $p$ as a "predicate"? Typically, a predicate is a condition of a logic rule. It seems that $p$ is a value, not a condition or "predicate." Is this terminology commonly used in other papers?

9. Why do you consider SBM a "rule-like classifier"? I could not find a direct connection between SBM and a rule-like concept.

\
[3] Deep Neural Networks Constrained by Decision Rules (AAAI 2019)

[4] Towards Robust Interpretability with Self-Explaining Neural Networks (NeurIPS 2018)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces InterpGN, which stands for the interpretable time series classification framework, that brings together:
* A novel Shapelet Bottleneck Model (SBM) that explicitly uses shapelets as easily interpretable features
* A gating mechanism that determines the conditions under which interpretable predictions should be used and under which conditions deep neural network predictions should be used
* A Shapelet Transform variant for the construction of logical predicates
* Quantitative measures to assess interpretability and quality of shapelets

### Strengths
* Novel gating mechanism based on confidence of interpretable model
* Improved shapelet transform variant using RBF-based predicates
* Quantitative metrics for interpretability and shapelet quality
* Theoretically sound integration of physical constraints

* Clean separation between interpretable expert (SBM) and DNN
* Adaptive layer normalization for condition injection
* Unified masking strategy handling multiple tasks
* Flexible handling of varying input dimensions

* Local explanations: Sample-specific shapelet importance
* Global explanations: Rule-based class characteristics 
* Visual validation of learned patterns
* Quantitative interpretability metrics

### Weaknesses
 * High memory overhead O(T·l) w.r.t. very long sequences
* Limited to a fixed maximum number of channels (Kmax=40)
* Limited scalability analysis w.r.t very long sequences
* Linear classifier might be too simple, when relations are complex

* Limited analysis concerning failure cases
* Only one type of DNN expert (FCN only)
* Very restricted real-world applications (MIMIC-III only)
* Lacking comparison w.r.t. some very recent methods

* Some counterintuitive shapelet interpretations
* No formal evaluation of explanation quality
* Small number of studies regarding users and interpretability

* Lack of discussions on adversarial cases. Limitations regarding 
* Fixed shapelet lengths; single-stage training process; design of a simple gating mechanism
* Lack of realization based on physical constraints.

### Questions
* Why this form of gating function η(xi)? Were other confidence measures evaluated?
* How sensitive is the gating mechanism to noise in the interpretable expert's predictions? What if the expert is confidently wrong?
* What is the basis of using FCN as the DNN expert? Would other architectures like Transformers provide better results?
* How was the maximum channel number chosen as Kmax=40? What happens if this value is increased/decreased?
* Given a memory overhead of O(T·l), what is the practical sequence length limit? Will this ever change?
* What happens to performance as the number of variables, M, increases? What is computational complexity given M?
* How was the balance parameter β between interpretable and DNN experts determined? Is there a theoretical basis for its selection?
* Why were the particular shapelet lengths in L chosen? How sensitive is the model to these choices?
* How do you handle the case where important patterns occur at lengths not covered by the pre-specified shapelet lengths?
* A deeper comparison with post-hoc explanation methods is probably welcome. What exactly is the trade-off between the approach and methods like LIME?
* Have there been datasets on which InterpGN performed worse than others? What are the characteristics of such datasets?
* Maybe one can provide more detailed guidance on the hyperparameter choice for new datasets. How sensitive is this across different hyperparameters?
* How was the RBF kernel parameter ε chosen? What effect does that have on the quality of the shapelets?

### Soundness
3

### Presentation
3

### Contribution
3
