# End-to-End Rule Induction from Raw Sequence Inputs

- Decision: Accept
- Scores: 8, 6, 5, 6

## Abstract
Rule learning-based models are widely used in highly interpretable scenarios due to their transparent structures. Inductive logic programming (ILP), a form of machine learning, induces rules from facts while maintaining interpretability. Differentiable ILP models enhance this process by leveraging neural networks to improve robustness and scalability. However, most differentiable ILP methods rely on symbolic datasets, facing challenges when learning directly from raw data. Specifically, they struggle with explicit label leakage: The inability to map continuous inputs to symbolic variables without explicit supervision of input feature labels. In this work, we address this issue by integrating a self-supervised differentiable clustering model with a novel differentiable ILP model, enabling rule learning from raw data without explicit label leakage. The learned rules effectively describe raw data through its features. We demonstrate that our method intuitively and precisely learns generalized rules from time series and image data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work introduces Neural Rule Learner (NeurRL), a system designed to learn interpretable rules from sequential data, such as from time-series sensor data (like spectrograms) and serialized higher-dimensional data (such as images).

The system uses symbolization functions to map raw data into a predetermined framework of pattern and region predicates, allowing discrete raw data sequences to be represented as logical atoms that can be used in rule learning. In the supplied reference implementation, patterns are learned automatically through a differentiable k-means clustering process, while regions are predefined subdivisions of the sequence. The combination of learned patterns and predefined regions allows the system to express discovered features as logical rules using this symbolic vocabulary.

The framework uses two types of symbolization functions: body symbolization functions that map discrete sequences to symbolic concepts, and head symbolization functions that map inputs to a set of atoms. The system avoids the "label leakage" problem by not requiring pre-trained neural networks to map raw inputs to symbolic labels. The entire pipeline is differentiable and can be trained end-to-end, learning directly from raw data without needing intermediate symbolic representations.

The implementation uses a deep rule-learning module with multiple dense layers, and rules are evaluated using precision and recall metrics. The reference implementation includes an autoencoder component for learning concentrated representations of subsequences.
Experimental validation was conducted on both time series data (UCR datasets) and image data (MNIST).  Learning on UCR data-subsets  highlights low-data or data-efficient learning methods. The reference implementation achieves comparable or better classification accuracy compared to baseline methods, and provides interpretable rules. The generated rules are human-readable and capture patterns in the data.

### Strengths
Originality: This provides a new and instructive implementation to address the raw-to-symbolic data problem, while avoiding the data leakage issue.

Quality and Clarity: The paper explains and illustrates the method in a clear and compelling way.

Significance:  This appears to be an important contribution to the problem of addressing the problem of learning symbolic rules about raw sequential data.

### Weaknesses
The approach may require significant data invariance (orientation of images, sampling regularity).  Many important datasets have these properties, although image data often does not.  See questions for further clarification.

As a demonstration of the advantage of this approach as an interpretable and explainable method, it would be helpful to have the interpretation of rules on each dataset from UCR discussed in more detail.  How interpretable are the rules in terms of the data patterns?  Are there particular datasets or data types for which rules emerge that provide insight or match intuition?

### Questions
Question:  Please clarify the generalizability of your approach.  Do you expect the rule learning method to be sensitive to data errors that arise naturally in real-world collection, such as uncalibrated sensors or aspect/focus variation in images, or frame rate in video?   Consider the following comment, if that helps clarify the objective of the request.

I am not familiar with the UCR datasets, and I don't think you provided a link, nor did the paper you cite have a currently valid link; I found data and descriptions here: https://www.cs.ucr.edu/~eamonn/time_series_data/.  Some datasets seem to have a small degree of possible coordinate sensitivity, such as the spectrogram data, while other would vary significantly with scale, placement of the signal within a collection window, and image orientation.  (This is also true of MNIST).  Please review the table below, and help me understand the sensitivity of your method to data collection errors.  This gets at the issue of generalizability / fragility of the method.  In the table, the first column has the dataset name, the second column records whether or not your method was the top score in your reported results, the third records a (possibly incorrect) sense of how sensitive the data collection is to getting all the coordinates right, and the fourth is an explanation of the assessment. 

| Dataset | NeurRL | Coordinate Sensitivity | Rationale for sensitivity assessment |
|---------|-------------|----------------------|-------------|
| Coffee | Top | Low | Based on spectrographic measurements which are inherently coordinate-independent. The frequency patterns would be consistent regardless of measurement setup, as long as calibration is maintained. |
| ECG | -- | Medium | While heart rhythms have characteristic shapes, the absolute voltage measurements depend on electrode placement. However, the relative patterns are fairly robust across different setups. |
| Gun Point | -- | High | Heavily dependent on camera angle, distance calibration, and the defined origin point for measuring hand position. The distinction between gun/no-gun relies on precise spatial coordinates. |
| ItalyPow.Dem | Top | Low | Power demand measurements are absolute values independent of coordinate systems. The readings represent actual power consumption regardless of measurement setup. |
| Lightning2 | -- | Low (?) | While electromagnetic measurements depend on sensor placement, the characteristic patterns of lightning types are relatively robust across different setups. |
| CBF | -- | Low | As a synthetic dataset designed to test pattern recognition, the shapes (Cylinder-Bell-Funnel) are meaningful in their relative values rather than absolute coordinates. |
| Face Four | Top | High | Face profile traces are highly dependent on camera angle, distance, and orientation. Changes in perspective would significantly alter the time series. |
| Lightning7 | Top | Low (?) | Similar to Lightning2, with moderate dependence on sensor placement but relatively robust patterns. |
| OSU Leaf | Top | High | Leaf contour measurements depend heavily on orientation, scale, and starting point of the trace. Different coordinate systems would produce very different time series. |
| Trace | -- | Low | As synthetic nuclear instrument data, the patterns represent relative changes that are meaningful independent of absolute coordinate systems. |
| WordsSyn | Top | High | Pen trajectories are highly dependent on writing orientation, scale, and starting position. The coordinate system directly affects the recorded patterns. |
| OliveOil | Top | Low | Spectroscopic measurements are independent of coordinate systems. The chemical signatures would be consistent across different spectrometers (after calibration). |
| StarLightCurves | Top | Low | Brightness measurements are relative values that remain meaningful regardless of the telescope's exact positioning (assuming proper astronomical calibration). |

Question 2:  Can you explain "leakage" more clearly?  The coordinate dependence an example above creates an implicit bias in the data, for instance limited field-of-view and imaging system orientation in MNIST and handwriting digitization; is this an example of "label leakage"?

### Soundness
3

### Presentation
4

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
The paper proposes a new differentiable Inductive Logic Programming framework where symbolic rules are learned via gradients from sequential data. To overcome the bottleneck of previous models that require pre-trained neural networks to perceive raw input, the authors propose Neural Rule Learner (NeurRL), which combines VAE and differentiable k-means to the differentiable rule learning approach. The resulting framework can learn classification rules that specify regions and corresponding patterns to be classified as positive. It is demonstrated in the experiments using simple datasets, including synthetic, UCR, and MNIST datasets.

### Strengths
This paper tackles an important topic in the field of differentiable ILP, specifically the need for pre-trained models to ground raw input into symbols for effective rule learning. The approach of combining differentiable k-means and VAE with gradient-based rule learners is noteworthy, even though the concept is relatively straightforward.

The manuscript is well-written, with a high-quality presentation overall. It clearly outlines the research question and effectively conveys its core idea.

This work is a valuable contribution to the neuro-symbolic research community, paving the way for developing more robust systems capable of learning with fewer priors on raw input.

### Weaknesses
My primary concern is that it remains unclear whether the main claim is adequately supported by the methods and experiments sections. The paper asserts:

> (Line 42-45) Learning logic programs from raw data is hindered by the label leakage problem common in neuro-symbolic research (Topan et al., 2021): This leakage occurs when labels of ground objects are introduced for inducing rules (Evans & Grefenstette, 2018; Shindo et al., 2023).

and

> (Line 82-85) In our work, we do not require a pre-trained large-scale neural network to map raw input data to symbolic labels or atoms. Instead, we design an end-to-end learning framework to derive rules directly from raw numeric data, such as sequence and image data.

If this claim holds, the proposed system should be trainable end-to-end, grounding symbols in meaningful ways such that rule learners can generate rules based on them. However, the paper does not make it clear how this grounding is accomplished.

Does NeurRL perform grounding on the obtained clusters? Can the rule learners manage rules involving multiple clusters by understanding the meaning of each cluster? If not, I am skeptical that the proposed framework fully addresses the bottleneck identified in the introduction, namely the reliance on perception models in prior rule learning frameworks like $\partial$ILP and $\alpha$ILP. The paper suggests that the clustering method assigns a symbol atom to each cluster, but it remains unclear how these abstract symbols are then utilized by the rule learner to form meaningful rules beyond simple conjunctions of cluster assignments. Without a clear mechanism for grounding these cluster-based symbols, the method's ability to generalize to more complex rule structures is questionable.

Without grounding, the method would be confined to the rule format (Eq. 5), as the system would lack the means to learn from non-grounded symbols, limiting its applicability to other domains.

While I appreciate the method's ability to learn from small datasets, it is unclear how it would scale to larger, more complex datasets. Given that neural models typically require large datasets, future development would benefit from the capacity to handle such data at scale to better integrate neural networks. It would be beneficial to provide runtime comparisons on different dataset sizes, or to discuss potential challenges and solutions for scaling the approach to larger datasets. How does the model's performance change with increasing dataset complexity and size? If scalability to large-scale data is an issue, this limitation should be discussed somewhere in the paper.

### Questions
Differentiable ILP frameworks ($\partial$ ILP and $\alpha$ ILP) typically suffer from their intense memory consumption due to the tensor encoding. Does NeurRL share the same problem? 

For other questions, please refer to the weakness section.

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
The paper proposes a supervised neurosymbolic model for time series data, structured as a cascade of three main building blocks. First, an autoencoder extracts an embedding representation from raw data. Next, a differentiable clustering module maps the embedding to a symbolic representation, followed by a fuzzy neural rule learner that maps the symbolic representation to the target. The overall training objective includes three loss functions, one for each building block: a reconstruction error for the autoencoder, a k-means objective for the differentiable clustering, and a supervised cross-entropy loss for the rule learner.
Training occurs in two stages, beginning with the pre-training of the autoencoder, followed by the fine-tuning of the entire model. Additionally, a post-hoc heuristic is introduced to extract rules in propositional logic form from the weights learned by the rule learner. Experiments are conducted on a series of small datasets from UCR, comparing the model to existing neural and kernel-based classification baselines for time series data, with results demonstrating superior predictive accuracy. Lastly, a qualitative experiment on MNIST data is provided.

### Strengths
1. The paper is overall clear **Clarity**. However the text should be polished to rewrite/rearrange words in some sentences and correct the several typos present throughout. Please refer the MINOR paragraph below for a non-exhaustive list.
2. The considered problem is relevant and timely **Relevance**.
3. Code is available, but no further check has been performed **Code availability**.

MINOR \
L.109 -> $\neg\alpha_2$ \
L.129 -> a substitution or an interpretation \
L.151 -> is ordered real-valued observations with the dimension one \
L.159 -> discrete -> discretize \
L.161 -> closest \
L.195-197 -> could you rephrase the sentence? \
L.273 -> the its \
L.325-327 -> could you rephrase the sentence? \
L.381 -> synthetic

### Weaknesses
1. The paper lacks adequate context within the existing neuro-symbolic learning literature, making its contribution appear incremental in terms of novelty **Quality**. For example, neuro-symbolic (NeSy) autoencoders have been previously explored (see [1,2]), and differentiable clustering has also been investigated (refer to [3,4]). Additionally, the rule learner shows a strong resemblance to $\delta$ILP. At a minimum, a discussion of related work should be included to clarify the paper's novelty and contribution. An experimental comparison with existing methods could also help demonstrate the advantages of the proposed approach. 
2. The paper lacks soundness due to several incorrect and overly ambitious claims that are not adequately supported **Soundness**. First, the paper states that this work is the first to enable joint training of the neural network and rule learner without pre-training. However, this claim is inaccurate, as the proposed training still requires a two-stage process. Additionally, contrary to what is mentioned, the work in [5] already achieves joint learning of a neural network and a rule learner. An experimental comparison on the datasets introduced in [5] would be valuable. Furthermore, the paper suggests that the proposed solution can uncover underlying rules without identifying conditions for failure. However, depending on the level of supervision and the complexity of the symbolic task, the neural learner may learn incorrect mappings from raw data to symbols. The work in [3,4] presents a basic sequential setting to analyze this issue, demonstrating that while representation learning (through differentiable clustering) is necessary to address the problem, it is not sufficient. Similar observations are subsequently reported in [6,7], where the authors label this issue as "reasoning shortcuts." 
3. There is very limited discussion about the details of the experimental methodology, raising serious concerns regarding reproducibility **Reproducibility**
4. Experiments are conducted on small datasets with relatively simple symbolic tasks **Quality**.  I encourage the authors to consider more traditional and more complex experimental settings for neuro-symbolic learning, including the arithmetic tasks on handwritten digits or the datasets in [5].

### Questions
In addition to discuss the above mentioned weaknesses, please find below some additional questions: 

1. The proposed solution introduces several hyperparameters, including parameters for data pre-processing (such as subsequence length and the number of temporal/spatial slots), fixed biases for the rule learner’s neurons, temperature parameters for the rule learner’s weights, and weights for the loss functions. How are these hyperparameters selected, and how sensitive is the model’s performance to their values? A sensitivity analysis could clarify this, and it should be feasible given the small size of the datasets. 
2. The post-hoc strategy achieves lower predictive accuracy compared to the full neural solution (see Table 1), with drops of up to 15 percentage points in some cases. This underscores the heuristic nature of the proposed strategy. Could you provide an explanation for this phenomenon? Additionally, what can be said about the faithfulness of the extracted rules in relation to the learned model’s weights? 
3. Why is neuro-symbolic learning necessary for the chosen MNIST task, and what is the rationale for this choice? The task could be solved by relying on superficial image cues (such as identifying regions that are either black or white), as illustrated by the qualitative demonstration in Figure 4, without needing to understand the underlying semantics of the digits. Therefore, a purely neural approach might suffice for this task. It would be interesting to assess the model’s capability to recognize digit classes within arithmetic tasks or, more broadly, in tasks defined by programs over integer sequences (e.g., sequences of even or odd numbers, counting). 
4. Are the codes learnable in the differentiable clustering layer and how do you ensure that meaningful clusters can be learnt, without experiencing any form of collapse? Please refer for instance to the work in [1].

**References**

[1] Sansone. The Triad Of Failure Modes and a Possible Way Out. In NeurIPS SSL Workshop 2023

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel differentiable Inductive Logic Programming model called NeurRL, aimed at solving the problem of learning symbolic rules from raw data. Unlike previous methods that rely on pre-trained neural networks to extract labels for symbolic learning, NeurRL combines a differentiable clustering module and a deep neural network learning module, enabling end-to-end rule learning from raw data such as time series and images without leaking label information.

### Strengths
1. The paper formally establishes the ILP learning task from raw data, utilizing the interpretation transition framework of ILP to guide the learning process.
2. Experimental results demonstrate that NeurRL shows a notable improvement over previous methods in terms of effectiveness.
3. The paper's overall presentation is clear, making the concepts and methodologies easy to follow.

### Weaknesses
1. The model has a large number of hyperparameters (especially the number of categories K, subsequence length l, and the number of regions P), which may negatively affect reproducibility and generalizability. The interdependence of these hyperparameters is also unclear; for example, the optimal subsequence length might vary significantly depending on the number of categories chosen. This lack of clarity makes it difficult to understand how to effectively tune the model for new datasets.
2. The experimental details are insufficient, lacking information on how hyperparameters were chosen and whether tuning was done separately for different experiments. Moreover, it is unclear if the results reported are the best performance or averaged. The absence of a clear hyperparameter selection strategy and the lack of statistical reporting (e.g., standard deviations) make it difficult to assess the robustness of the results.
3. The learned predicates lack high-level abstraction, instead offering post-hoc explanations for neighboring pixels. This limits the generalizability and interpretability of the induced rules. The rules seem to capture low-level spatial relationships rather than more abstract, semantically meaningful concepts, which is a significant limitation for real-world applications.
4. Although previous works did not formally define the task of extracting rules from raw data, some have achieved similar goals with comparable architectures (e.g., autoencoder + discriminator) [1, 2], or going further in technical sophistication [3]. This paper lacks a discussion of and comparison with such works. The absence of a thorough comparison with related methods makes it difficult to position the proposed approach within the broader landscape of explainable AI and rule learning.
5. The model does not consider translation invariance in the data, meaning some patterns should only need to be present rather than bound to a specific region. This limitation may hinder the model's performance in tasks where the position of the target is irrelevant. The reliance on fixed regions for pattern detection could lead to brittle rules that fail to generalize to slightly shifted instances of the same pattern.

### Questions
1. Is there a way to reduce the number of hyperparameters, such as determining the number of categories K adaptively during training? If this is not feasible, please at least provide guidance on how to select these hyperparameters and show how different choices impact the experimental results.
2. Please compare your work with more related studies (see Weakness 4)

### Soundness
3

### Presentation
3

### Contribution
3
