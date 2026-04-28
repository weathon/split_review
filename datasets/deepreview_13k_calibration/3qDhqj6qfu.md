# TabKANet: Tabular Data Modeling with Kolmogorov-Arnold Network and Transformer

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
Tabular data is the most common type of data in real-life scenarios. In this study, we propose the TabKANet model for tabular data modeling, which targets the bottlenecks in learning from numerical content. We constructed a Kolmogorov-Arnold Network (KAN) based Numerical Embedding Module and unified numerical and categorical features encoding within a Transformer architecture. TabKANet has demonstrated stable and significantly superior performance compared to Neural Networks (NNs) across multiple public datasets in binary classification, multi-class classification, and regression tasks. Its performance is comparable to or surpasses that of  Gradient Boosted Decision Tree models (GBDTs).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a discriminative model for tabular data that is distinct from previous models in that it uses a KAN for embedding numeric features rather than linear or MLP layers. Its performance is compared to a selection of GBDT and NN tabular models. In the experiment settings evaluated, TabKANet consistently outperforms the other NN models but is mostly outperformed by the GBDT models.

### Strengths
- Exploring the potential uses of KANs in tabular modelling is a relevant current topic.
- The model shows some promise in outperforming other NN models.
- Code is provided to reproduce some of the results.

### Weaknesses
On the whole, I think paper has a poor contribution due to issues with the evaluations and a lack of depth in justifying the proposed modelling choices. The overall novelty of the method is limited, being a relatively simple combination of existing modelling components (KANs, batch normalization, and transformers), and I don't think the rest of the paper has the depth or soundness to make up for that.

- No hyperparameter tuning is done for baseline models. This is especially problematic for GBDT models, which require hyperparameter tuning for a practical comparison. This is out of line with prior research (e.g., see Gorishniy et al. 2021) and severely limits the utility of the comparison with GBDTs. The authors fix hyperparameters across all datasets, which is not standard practice for GBDT models, and makes the comparison unfair. A proper comparison would require a hyperparameter search for each dataset, as is standard in the field.

- The NN models being compared to are not state-of-the-art, so the comparison to them does not indicate much about the paper's contribution. I would have at least liked to have seen TabR and TabPFN included, and other recent models that are widely used as baselines such as FT-Transformer and MLP-PLR would have been welcome.

- The discussion of why KANs should be used in this area is lacking in depth. The paper doesn't provide theoretical or empirical insights into how they would be useful for tabular data in particular. Instead, there are just vague references to their flexibility. Ablations are also not provided to compare the contribution of the KAN part alone versus other encoders. The paper needs to provide a more detailed justification for the use of KANs, including theoretical properties that make them suitable for this task, and empirical evidence of their effectiveness compared to other encoders.

- Using batch normalization instead of layer normalization is a fairly trivial tuning choice, and the discussion on page 5 is unclear and does not provide significant technical insights to justify treating it as an important decision. The paper presents this as a key decision, but the justification is weak and lacks technical depth. The ablation study in section 4.7 does not provide sufficient evidence to support the claim that batch normalization is crucial for performance.

- Parts of the paper contain misleading claims:
	- The introduction indicates that existing attempts to use transformers in tabular modelling are using them to encode categorical variables, when in fact there's a much wider variety of transformer models for tabular data (some of which are given in the Related Work). In general, the proposed model is not contextualized with respect to the entire range of existing tabular transformer models.
	- The introduction also claims that the proposed model achieved "identical performance" to GBDTs on almost all datasets - the performance was not identical, and was lower on average in most cases (evaluation issues notwithstanding).
	- "Current scientific research has not yet proposed a simple, stable, and universal numerical embedding module" - this is a very strong claim that is not justified. MLPs, linear layers, and piecewise linear encodings arguably satisfy these criteria just as well as the proposed solution.

### Questions
- What about KANs makes them a compelling choice for this application in particular: encoding numeric tabular data to pass into a downstream transformer? E.g., what theoretical properties are especially relevant for this application? Why not use them in other parts of the model?

- Did you evaluate other numeric encoders within the same framework as your model, such as linear, MLP, and/or piecewise linear encoders?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a model for tabular data based on the Transformer architecture, similar to TabTransformer, but including a KAN layer for encoding continuous features. The model is evaluated on binary and multi-class classification tasks as well as regression and is found to outperform deep learning baselines and in some cases GBRT models.

### Strengths
The paper discusses encoding of continuous values for tabular classification. This is a hot topic, and the combination with the recently proposed KAN architecture is timely.
The model is evaluated on a wide variety of tasks and the datasets are discussed in detail.

### Weaknesses
 # Main concern
Given that the novelty of the method is relatively small, the empirical evaluation of the method is critically important. However I have several concerns regarding this:
a) It's unclear how the datasets for evaluation were selected. There is many established benchmark suites, such as the AutoML benchmark, TabZilla, OpenML-CC18 and the Grinsztajn collection. Not adhering to a standard benchmark suite allows for cherry-picking of dataset.

b) Since the emphasis of the paper is on the encoding of continuous features, I think FTTransformer, and Gorishniy et al:  On Embeddings for Numerical Features in Tabular Deep Learning are critical baselines to compare against.

c) Some important ablations are missing; in particular, what happens if the KAN layer gets replaced by simple input scaling? This seems to be different form TabTransformer, which skips the transformer entirely for continuous data. Also, Table8 shows a big improvement between the LN and BN versions. An obvious comparison here would be to TabTransformer with BN.

d) The paper doesn't describe how hyper-parameters for the methods were tuned.

e) Some deep baselines are missing. While it's not reasonable to compare against all publications, I would suggest comparing against TabR and TabPFN (even when subsampled to a maximum of 3000 samples, TabPFN performance is still strong, see McElfresh.

I think the clarity of the paper could also be improved, and the novelty of the KAN is overstated, in particular wrt existing neural networks and "On Embeddings for Numerical Features".

# Other Concerns
## Overselling KAN
The paper states in several places that KANs are more powerful than MLPs; however, that is not strictly the case. A KAN can easily be represented with an MLP by constraining the MLP structure and potentially changing the activation function. For example a KAN with piecewise linear splines with r pieces is equivalent to an MLP with ReLU activations where each node is replaced by a small neural network with r nodes.  This view calls into question claims like line 63 "This feature offers neural networks
 more flexible performance compared to Multilayer Perceptron" and Line 115 "rigidity in MLP".
Also, neural networks with spline activation functions have long been studied, and it's unclear what (if any) novelty can be attributed to KANs.

## Minor suggestions
Line 028 "ordered different features" is hard to read and not very clear.

Line 028: add citations for most commonly used and oldest business data format. I am not convinced by these claims. A lot of data is actually in spreadsheets and relational databases, neither of which are tabular data in the sense of the standard ML datasets. NoSQL data is also extremely common.

Line 036: Citing Hollman for the prevalence of GRBT is strange, since TabPFN is a deep model that clearly outperforms GRBT.

Line 043: None of the three arguments for neural networks seems sound, and I am a firm believer in using neural networks on tabular data. 1) is vague, 2) it is unclear what is meant by scalability and how it relates to multimodality 3) unsupervised schemes exist for tree-based models, though they are not as common.

Line 070: It's unclear what is meant by "business structure framework"

Line 215 1): It's unclear wrt to what baselines you are discussing improvements. Both LN and BN are common in transformer models. Is this wrt KAN or wrt TabTransformer?

Line 218 3): This is just concatenating features, right?

Figure 2: The meaning of d is unclear, it seems to be embedding size. However, it's unclear why the output would be reshaped to (m+n) * d? Is this just to input into the MLP? Also, the figure shows multiple rows in input and output, but the model operates on one row at a time, right?

Line 223: It's unclear what's meant by "subconscious best solution".

Line 377: "predict auc scores" I think you mean predict the target and compute AUC scores?

## Typos

Line 027 "The tabular" -> "a tabular"

Line 030 "medicineI" ->"medicine"

Line 053 "they have used Transformers" -> Transformers have been used.

Figure 1: "Nurmerical" -> "Numerical"

Line 212: Numercal -> "Numerical"

Acknowledgements contain author instructions.

### Questions
* How were the datasets for the evaluation selected?
* How where hyper-parameters tuned for all models?
* How well does the model perform when removing the KAN layer?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces TabKANet, a model that integrates Kolmogorov-Arnold Network (KAN) and Transformer architectures to improve the handling of structured tabular data. The authors demonstrate that TabKANet outperforms selected deep learning baselines in various tasks. However, its performance gains over decision tree-based ensemble methods, such as Gradient Boosted Decision Trees, are minimal.

### Strengths
- The paper addressing an important issue of the structured tabular learning 
- Authors utilize various tabular datasets from different domains

### Weaknesses
 - The explanation of KAN and the model’s overall structure is brief and lacks clarity. The paper’s organization could be improved to aid readers in understanding the background and methodology.

- The proposed method, TabKANet, offers only marginal improvements over existing models on key metrics for several datasets. For instance, on 2 out of 6 datasets, the AUC improvement compared to CatBoost is very small, with a difference of only **0.003**. This casts doubt on the claim from the abstract that *"Its performance is comparable to or surpasses that of Gradient Boosted Decision Tree models (GBDTs)."* Overall, such minor performance gains may not justify the added complexity of the approach.

- The paper omits several recently proposed methods for deep tabular learning, such as TabPFN, GANDALF,  DeepTLF, and more in [1]. Including these baselines would provide a more comprehensive comparison and better contextualize the performance of TabKANet. 

- The evaluation of TabKANet could be strengthened by using widely recognized benchmarks, such as Tabzilla, which is well-accepted by the community and would provide a more robust assessment of the model's effectiveness.

### Questions
- General question. Why are numerical and categorical data processed separately? Would it make sense to explore a combined representation that integrates both types of features?

- Line 221: The statement *"Firstly, normalization for numerical items is crucial, which is essential to avoid gradient explosion, especially with real-world data."* raises a question: Why not simply normalize the numerical data before feeding it to the neural network? Using batch normalization introduces additional learnable parameters and can significantly affect training, as the normalization depends on batch size. Although this question is somewhat addressed later (Line 238), it introduces another point of confusion: *"Repeatedly pairing numerical normalization results and category features will bring additional training data."* This may be more accurately described as data augmentation rather than additional data, which could be explored through an ablation study.

- Line 223: Could you clarify the phrase *"This is a subconscious best solution"*? The entire sentence is somewhat confusing and may need rephrasing for clarity.

- Line 255: The sentence about data splitting is unclear. Did you apply cross-validation, or was the data split into three groups: training, testing, and validation?

- Tables 2 and 3: What is the motivation for separating the neural network and machine learning baselines? A unified comparison would improve clarity.

Minor Comments

- In the motivation, you mention that self-supervised learning is a major strength of deep learning approaches. How could TabKANet be adapted for use in self-supervised settings?

- Section 3: The statement "As mentioned in Sec. 2.1, GBDTs outperform NNs in table modeling tasks because of the skewed or heavy-tailed features in table information" reads as a hypothesis rather than a definitive fact. Could this be clarified?

- Line 267: *"MLP is a traditional deep learning model consisting of multiple layers of neurons."* How are you defining a "traditional" deep learning model here? A more specific description might be helpful.

### Soundness
2

### Presentation
2

### Contribution
2
