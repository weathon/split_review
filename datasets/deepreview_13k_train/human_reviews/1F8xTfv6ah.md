# Advancing Out-of-Distribution Detection via Local Neuroplasticity

- Decision: Accept
- Scores: 5, 5, 6, 5

## Abstract
In the domain of machine learning, the assumption that training and test data share the same distribution is often violated in real-world scenarios, requiring effective out-of-distribution (OOD) detection. 
This paper presents a novel OOD detection method that leverages the unique local neuroplasticity property of Kolmogorov-Arnold Networks (KANs). 
Unlike traditional multilayer perceptrons, KANs exhibit local plasticity, allowing them to preserve learned information while adapting to new tasks. 
Our method compares the activation patterns of a trained KAN against its untrained counterpart to detect OOD samples. 
We validate our approach on benchmarks from image and medical domains, demonstrating superior performance and robustness compared to state-of-the-art techniques. 
These results underscore the potential of KANs in enhancing the reliability of machine learning systems in diverse environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a new out-of-distribution (OOD) detection method leveraging Kolmogorov-Arnold Networks (KANs), which utilize “local neuroplasticity” to differentiate in-distribution (InD) data from OOD data via comparing the activation patterns of a trained KAN against an untrained counterpart. KANs stand out due to their spline-based architecture, which preserve specific network regions during training, aiding in the OOD detection.

### Strengths
The described method is clearly defined and is easy to reproduce.

The method is validated across image and tabular medical data benchmarks, demonstrating improved performance and robustness compared to other state-of-the-art OOD detectors. 

The findings highlight KANs' potential in enhancing model reliability across diverse environments by maintaining high detection accuracy, even with a relatively small training dataset.

The results (although not on all datasets) look promising in terms of different OOD detection accuracy especially for the case of low number of training samples.

### Weaknesses
Despite the clarity, some steps of the approach implementation look like ad-hoc tricks for improving the method’s performance without developing a deep intuition why a particular step is better than alternatives (please, see questions below for details).

The fact that not all datasets (leaderboards) from the OpenOOD were used for testing the approach, along with the obtained not perfect results on CIFAR-100, suggest that the datasets were selected manually. The authors need to prove absence of any selection bias. 

I am strongly concerned about the scalability of the proposed method, which requires splitting the training dataset into a number of subsets and fitting a model per a subset (see comments below).

The method resembles feature-preprocessor (backbone-dependent), being not applicable to the case where a good feature extractor is not known.

### Questions
Questions and suggestions:

Major: 
Testing of approach on other large-scale datasets would be beneficial, consider other leaderboards from openOOD like ImageNet-200, 1K.
The choice of the K-means clustering approach looks quite arbitrary for initial data splitting. Why not use other clustering approaches like DBScan, Spectral, Agglomerative or even Gausian mixture? I believe, K-means choice should be justified here.

One can assume a dataset with a lot of natural clusters (like ImageNet-1K) will require a lot of time for training KANs. Show that the approach is actually scalable, robust, and not computationally burdensome in case of a large number of clusters.

The robustness of clustering approach is not evident for the case of regression task due to the poor internal separability of data clusters. I suggest adding one example of OOD detection where the training dataset is directly related to the regression task. 

The method looks strongly backbone dependent and may be poorly working for the plethora of practical tasks where the good backbone feature extractor is not known. Is it possible to exemplify the method robustness for the case of the absence of backbone preprocessor? 
Probably, some classic ML tabular datasets (e.g. from sklearn) could be useful here.

“Importantly, our experiments show that the previous methods suffer from a non-optimal InD dataset size” - this statement requires more experimental support. Currently, the method superiority was shown only for the CIFAR-10 dataset. 

Minor:
Line 183 (figure caption): “- “(e) InD score S(x)∀x ∈ [−1,1] “ - why the InD score can take negative values? The original formula (5) contains absolute value operation brackets. Is this the typo? 

Line 187: “A simple, yet effective approach is to split the dataset based on class labels.”  - It is not obvious how to train KANs in case of such splitting. One can imagine a situation where positive class is OOD for a KAN trained on samples of negative class, and the maximization scoring procedure identifies positive class as an OOD. This point should be clarified or rephrased.

I’m interested if the method will be robust for the case of NaN-enriched data samples? It is not a request for an additional analysis but rather an interesting point for the discussion of method limitations.

### Soundness
3

### Presentation
3

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
This paper introduces a novel OOD detection method that leverages the unique local neuroplasticity of Kolmogorov-Arnold Networks (KANs). By comparing the activation patterns of a trained KAN against its untrained counterpart, the method identifies OOD samples across diverse benchmarks, including computer vision and tabular medical data. Experimental results demonstrate that the KAN-based approach outperforms existing methods and shows resilience to variations in in-distribution dataset sizes. This robust, adaptable approach makes KANs a promising tool for enhancing the reliability of ML systems.

### Strengths
1. It introduces an innovative approach to OOD detection, offering fresh ideas and a unique viewpoint that advances the current understanding of OOD detection techniques.
2. The paper effectively harness the neuroplasticity characteristic of KANs, ensuring that learning new tasks only affects the network regions activated by the training data, effective motivation for OOD detection.
3. The paper includes thorough experiments on standard benchmarks.

### Weaknesses
1. While the core idea is clear, the method appears loosely structured. Specifically, the role of multiplying location-specific information with regions activated by InD samples to achieve the delta function (used in the score function) is unclear (e.g., Eqn 5). Additionally, no study is provided to analyze these aspects, leaving parts of the methodology unexplored. The lack of clarity extends to how the location-specific information is derived and why this particular formulation is chosen over other potential alternatives. A more detailed explanation of the mathematical underpinnings and the rationale behind the design choices is needed to fully grasp the method's mechanics.
2. The paper does not present or discuss the generalization performance of models when KANs are incorporated into the training scheme. It remains unclear how the use of KANs as a post-hoc processor impacts the overall performance and robustness of the system, particularly in scenarios where the backbone model might be sensitive to changes in feature representation. The absence of experiments exploring the end-to-end training with KANs limits the understanding of the method's practical applicability and potential drawbacks.
3. Results on CIFAR-100 indicate minimal advantage over existing methods, as the improvements in detection performance appear statistically insignificant. The reported gains are marginal, raising concerns about the practical significance of the proposed approach on complex datasets. A more rigorous statistical analysis, including confidence intervals and effect sizes, is needed to substantiate the claims of superior performance.
4. Including a discussion on the computational cost of the proposed method would strengthen the paper. Given that the approach involves dividing the dataset into different groups, insights into computational efficiency would enhance understanding of the method’s practicality. The analysis should include not only the inference time but also the time required for the setup, including feature extraction, partitioning, and KAN training. This is crucial for assessing the scalability and feasibility of the method in real-world applications.

### Questions
Please answer the points raised in the questions.

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
4

### Summary
Authors utilize Kolmogorov Arnold Networks (KAN) for out of
distribution detection. The main idea is to leverage the fact that KAN
uses BSplines as non-linear functions. Feature values that appear
within InD, if they are concentrated in certain part of the feature
space - which is $\mathbb{R}$ in this case, will only modify certain
BSpline coefficients. In this scenario when a feature value that is
different than the InD comes, the BSpline coefficients at those
locations will not have been modified during training. Hence, the
difference in activation between trained and untrained network will be
low. Experiments with benchmark datasets and comparisons with large
set of alternatives are presented.

### Strengths
+ The topic is very relevant.
+ The idea is novel and quite intuitive.
+ The results are motivating. Even though this is not the best
  performing all around, it is one of the top algorithms.
+ Authors do a great job explaining the method as well as motivating
  the approach.
+ Large set of experiments.

### Weaknesses
 - The model - due to KANs - is heavily univariate. While authors do
  dataset partitioning to alleviate the problem, I do not see how they
  can actually do so. Unsupervised combinations of features are
  mentioned, however, their applicability also raises questions. Specifically, the method relies on partitioning the data, but it's unclear how the KANs handle complex, non-linear relationships between features within each partition. The assumption that marginal distributions within a partition are sufficient seems overly simplistic, especially when dealing with high-dimensional data where feature interactions are often crucial for OOD detection.
- Partitioning the dataset requires having multiple trained models,
  which limits the applicability of the approach for large scale
  problems. The computational cost of training and maintaining multiple KAN models, each on a different partition, is a significant drawback. This approach does not scale well to datasets with a large number of features or a high degree of complexity, where the number of partitions might need to be very high. This also raises questions about the memory footprint of such an approach.
- KANs are interesting but most recent work do not use these
  networks. This naturally limits the applicability of the approach. The choice of KANs, while novel, introduces a potential barrier to adoption. The lack of widespread use and established best practices for KANs means that the method might be harder to implement and integrate into existing workflows compared to methods based on more established architectures. The reliance on a relatively niche architecture also makes it difficult to leverage existing tools and libraries, potentially increasing the implementation overhead.

### Questions
- It is not clear how different KAN$_i$'s are trained. It would be
  good to explain this a bit more in depth.
- Authors state that the method can be seamlessly integrated with any
  pre-trained model. I do not really understand this. Doesn't one need
  to use KAN model for this?
- How are the pre-trained backbones used for KAN? Does one use the
  features extracted from these networks and build classifiers and
  regressors with KAN architecture?
- Authors state that hyperparameters are tuned using a validation
  set. How much do the trained hyperparameters generalize to OOD types
  unseen in the validation set?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose to use Kolmogorov-Arnold Networks (KAN) for out-of-distribution detection. The key advantage of KANs is their plasticity which results in avoiding catastrophic forgetting. The authors show that this property can be leveraged to detect OOD samples. 

The method demonstrates good performance on small datasets, but the proposed method does not properly address the shortcomings of the KAN architecture, and the method was not validated in terms of scalability to realistic problems. Overall I rate weak reject.

### Strengths
- Originality: Given that KANs are a novel type of architecture the research is a very current  
- The method is evaluated on image and tabular data, demonstrating feasibility across different domains. 
- Performance: The performance on the benchmarks is convincing and demonstrates superiority over a vast set of previous methods 
- Exhaustive experimentation on toy datasets including multiple important ablations that erase questions (such as stochasticity)

### Weaknesses
Major:
- Scalability: No experiments demonstrate the method's scalability to larger images or real-world problems. The experiments are limited to small datasets such as CIFAR and toy tabular data. The method needs to be tested on larger, more complex datasets such as ImageNet or real-world anomaly detection benchmarks like MVTech to properly assess its applicability.
- Insufficient capturing of joint distribution: I believe the partitioning problem of KANs is very severe. While the problem is mentioned I believe it is not properly addressed. Essentially, by partitioning the dataset you are just scaling the problem down to subclasses. What if the l-shaped differences, that you mention in Table 2, appear on an intra-class level instead of a class level? While this may work for toy data if the data is sufficiently separable using k-means or class labels directly, I doubt it will work for more difficult problems such as MVTech. The method does not explain how the partitioning of the data affects the final OOD detection performance. The method should investigate the effect of different partitioning strategies, and how the choice of partitioning impacts the ability to capture the underlying data distribution.
- The influence of Model capacity is unclear: KANs are known for their improvements in lack of catastrophic forgetting. How does the model size influence this. Additionally, if KANs treat features individually, the difficulty of the problem and the necessary capacity of the method scales drastically with the image size. The paper does not provide a clear analysis of how the grid size of the KAN affects the performance. It is also unclear how the method scales with the dimensionality of the input feature space. A detailed analysis of the model capacity and its relationship to the performance is needed.

### Questions
Line 43 has wrong citation 

You mention that the hyperpareter search can be quite challenging. How did you decide for the parameter space especially regarding number of epochs, learning rate, partitionings?

### Soundness
3

### Presentation
3

### Contribution
2
