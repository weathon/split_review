# From Data to Model: Anomaly Detection of 3D GPR Data in CuDeRes Model Space

- Decision: Reject
- Scores: 5, 3, 6, 5

## Abstract
Ground Penetrating Radar (GPR) offers in-depth subterranean insights, yet subsurface anomaly detection in GPR data remains challenging due to limited training data, typically confined to some normal data samples free from any subsurface structures or anomalies, and the variability of subsurface conditions. In response, this paper introduces practical and accurate subsurface anomaly detection within the Cubic Decay Reservoir Network (CuDeRes) model space. Our approach employs commonly available normal GPR data, segmented into blocks. Each data block is independently fitted using the introduced CuDeRes, which incorporates three reservoirs with spatial decay to adequately capture the data-inherent multi-directional dynamics, resulting in a compact fitted readout model. Representing each data block with the fitted model, together with the distance measurement between models, the original GPR data blocks are mapped into the CuDeRes model space, and the fitted models are collected into a "Model Depot". For subsequent anomaly detection in newly collected GPR data, the same segmentation and CuDeRes fitting approaches are applied, where the data blocks are represented by fitted models for comparative assessment against the model depot. Anomalies are detected through model dissimilarities, and subsequently clustered within the CuDeRes model space, allowing us to accurately identify the data blocks with potential subsurface anomalies and ascertain their anomaly types. Experiments on real-world GPR data demonstrate the practical effectiveness of our approach, notably using only limited normal data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a framework for anomaly detection in 3D Ground Penetrating Radar (GPR) data using the Cubic Decay Reservoir Network (CuDeRes). CuDeRes fits 3D GPR data segments into model representations, which are stored in a "Model Depot" as references for normal data patterns. The approach detects anomalies by comparing new data representations with stored models, leveraging multi-directional spatial decay to capture subsurface dynamics. Experiments demonstrate the model’s effectiveness in identifying subsurface anomalies, achieving an F1-score of 91.9% and surpassing baseline methods.

### Strengths
1. **Efficient Use of Limited Normal Data**: The framework relies on a small amount of normal data, making it feasible for real-world applications where labeled anomaly data is scarce.

2. **Novel Application of Multi-Directional Reservoirs**: By incorporating three reservoirs with spatial decay, the CuDeRes architecture effectively captures multi-directional dynamics, essential for processing complex 3D GPR data.

3. **Practical Relevance for Subsurface Anomaly Detection**: This model has clear potential applications in structural health monitoring, especially for roads and urban infrastructure.

4. **Comprehensive Experimental Validation**: The model is rigorously tested across various anomaly types and compared to multiple baseline models, demonstrating both its classification and clustering performance.

### Weaknesses
1. **Robustness in Anomaly Typing**: The clustering step for anomaly type identification is not extensively evaluated. The paper would benefit from additional metrics or case studies demonstrating the accuracy and practical impact of identifying specific anomaly types. Specifically, the paper lacks a detailed analysis of the confusion matrix for the clustering results, making it difficult to assess the model's ability to differentiate between similar anomaly types. For example, it would be beneficial to see how often the model confuses a small void with a region of material looseness, as these could have similar signatures in GPR data. Furthermore, the paper does not explore the impact of different clustering algorithms on the results, which could reveal whether the observed performance is specific to the chosen method or a more general property of the model's representations.

2. **Scalability**: The approach’s scalability to larger datasets or real-time applications is not well-explored. Given the model's complexity, its feasibility in high-throughput scenarios is uncertain. The paper does not provide a clear analysis of the computational cost associated with fitting the CuDeRes model to each data block. This is particularly important because the model involves multiple reservoirs and spatial decay calculations, which could become computationally expensive for large 3D GPR datasets. Furthermore, the paper does not discuss memory requirements, which could be a limiting factor for processing large volumes of data.

3. **Distance Metric**: The paper uses the p-norm distance for model comparisons without exploring alternative metrics or adaptive methods. This approach may limit its effectiveness in distinguishing anomalies with subtle variations from normal models. The choice of p-norm distance is not well-justified, and the paper does not explore whether other distance metrics, such as cosine similarity or Mahalanobis distance, might be more appropriate for comparing the model representations. The p-norm distance may not capture the complex relationships between different model parameters, and an adaptive distance metric that learns the importance of different features could potentially improve anomaly detection performance.

4. **Manual Parameter Tuning**: The CuDeRes model performance depends on manually set parameters (e.g., reservoir size, spatial decay rate) without clear guidelines on optimal selection. This could limit the method's applicability to other data sources or detection tasks without significant retraining or adjustment. The paper lacks a systematic study of how the model's performance varies with different parameter settings. This makes it difficult to determine the optimal parameter values for new datasets or different anomaly detection tasks. The absence of a clear methodology for parameter selection could hinder the practical application of the model in real-world scenarios.

### Questions
1. **Scalability and Computational Efficiency**: Given the complex nature of fitting CuDeRes on each GPR data block, what is the computational cost for large-scale data processing? Has the model been tested in a real-time setting, and if so, how does it perform?

2. **Robustness**: How accurate is the clustering in differentiating between types of anomalies? Are there specific situations where the model fails to distinguish between similar anomaly types, such as looseness versus cavities?

3. **Distance Measures**: Why was p-norm distance selected as the primary comparison metric? Would a learned distance metric improve the model's sensitivity to different anomaly patterns without impacting generalizability?

4. **Parameter Sensitivity**: The paper lacks an in-depth analysis of how CuDeRes's performance is affected by parameter variations. Have the authors considered any methods for dynamic parameter tuning, or is the current approach limited to the manually selected parameters?

5. **Ablation Study**:  Given the complexity of the CuDeRes model, why did the authors not conduct an ablation study to examine the contributions of individual components? For instance, how does the model perform without the spatial decay mechanism or when using single-direction fitting instead of multi-directional fitting? Additionally, would testing alternative distance metrics or varying reservoir sizes provide insights into which design choices are most critical for effective anomaly detection?

### Soundness
3

### Presentation
3

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
The paper addresses the problem of anomaly detection in images,
esp. for multichannel ground penetrating radar images (called
3d-GPR). The authors propose to characterize such an image by
the parameters of a ridge regression that aims to reconstruction
a blurred version from a pixel and its three left, upper and behind
neighbors. In an experiment on a GPR dataset with several classes,
they show that their method outperforms other methods
for image anomaly detection.

### Strengths
- s1. interesting data modality: 3d GPR data.
- s2. interesting progressive blurring operation: project each pixel
  to a combination of already blurred neighbors. 
- s3. well written.

### Weaknesses
 - w1. irreproducible: experiments on a single, non-public dataset.
- w2. major baselines missing in the experiments, e.g. Liu et al. 2024
  and Zhou et al. 2024.
- w3. simple ablations missing, e.g., blurring pixels based on their
  neighbors' observed intensities.

The paper addresses an interesting, not so heavily researched
data modality: ground penetrating radar images. It makes some
interesting, specific proposals. But currently I see three major
issues:

w1. irreproducible: experiments on a single, non-public dataset.
- Without showing a performance against other methods on a
  public dataset, it will be very difficult for other researchers
  to compare against the proposed method. It also is more
  or less impossible to assess the quality of the method.
- The authors also do not release any code to make such a
  reproduction easier.

w2. major baselines missing in the experiments, e.g. Liu et al. 2024
  and Zhou et al. 2024.
- The authors mention these two papers in their related work
  as being close and GPR-specifc. Can you compare agains them?

w3. simple ablations missing, e.g., blurring pixels based on their
  neighbors' observed intensities.
- Your method is specific in the sense that your blurring operation
  in eq. 1 blurs progressively: the value of the next pixel depends
  on the already blurred values of previous pixels. This leads to
  a very deep architecture. Can you compare on a simple setup
  where you blur on just the observed values of the neighbors?
- You fix theta to 1 and test only against theta = 0 ("w/o E").
  Can you run a full parameter sensitivity analysis for theta?

There also are some smaller issues that the authors could
look into:
- i1. Your model does not depend on x_a, y_b and z_c, but just
  on x_{a+1}-x_a (in eq. 3). You could simplify your representation
  by just using indices a, b, c and say what scaling factors you
  use in eq. 3.
  - Can you specify what these 3 numbers,  x_2-x_1, y_2-y_1 and z_2-z_1
    are in your experiment? 
  - line 417 you say the "width" of a block is 2.5m. Earlier you said
    your third channel is the antenna channel (e.g., fig. 2). Can you clarify?
- i2. line 293 you characterize the task as "next point prediction".
  But in your case u(x_a, y_b, z_c) is one of the inputs. So would
  it not be more appropriate to call it a reconstruction (from a
  blurred input)?
- i3. line 330 "\mu(x) denotes the probability density over the input
  domain" one easily could read as if you mean the ground truth
  distribution of the GPR images. But then you clarify to assume
  a uniform distribution.
- i4. The conditions on the random parameters W^x, W^y, W^z
  are formulated only vaguely as "satisfy the Echo State Property"
  (line 269). This could be made self-contained.

### Questions
- q1. Can you demonstrate your method on any public datasets,
  preferably some used already for anomaly detection for images?
- q2. How does your method compare against the methods from
  Liu et al. 2024 and Zhou et al. 2024 mentioned in your related work?
- q3. If in your blurring operation (eq. 1), you blur not based on the already
  blurred values of the neighbors, h*, but on the observed values
  (u(x_{a-1}, y_b, z_c), u(x_a, y_{b-1}, z_c), u(x_a, y_b, z_{c-1})),
  does this (way less deep, simpler) model work as well?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a novel method, called cubic decay reservoir network, for anomaly detection within 3D Ground Penetrating Radar data.

### Strengths
The method seems interesting and the paper is well written with comprehensive experiments that demonstrate the relevance of the proposed approach.

### Weaknesses
The proposed method is motivated by the objective of diminishing the computational demands, as opposed the 3D-CNNs necessitating considerable computational resources. However, not much is said on the computational complexity of the proposed method, and the authors need to provide results on the comparative analysis. Specifically, the paper lacks a detailed analysis of the time complexity, measured in terms of floating-point operations (FLOPs) or actual run-time, for both the training and inference phases. Furthermore, the memory footprint of the proposed method, particularly during the reservoir construction and readout phases, is not discussed, which is crucial for assessing its suitability for resource-constrained environments. A comparison with the computational cost of 3D-CNNs, even if only on a theoretical level, would greatly strengthen the paper's claims regarding efficiency.

### Questions
What about the computational complexity ?

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
4

### Summary
This is paper about GPR anomaly detection. GPR signals are noisy and there lacks negative training data in some cases. So the paper proposed a method that is trained on normal data to construct a learning in the model space called LMS. Each direction of GPR measurements, i.e., x, y, z corresponds to one type of model in the LMS. After training, the method is tested on normal and abnormal GPR signals and showed better performance than other methods. Contributions include the introduction of Cubic Decay Reservoir Network (CuDeRes) and better performance in testing.

### Strengths
Strengths include the introduction of CuDeRes to model normal GPR data and better performance in testing and comparisons versus Patchcore-3D, STEAL, 3D VAE, and MemAE, as well as the capability to tell apart different types of buried objects such as manholes and pipes by either K-Means, Agglomerative clustering, or Fuzzy C-Means.

### Weaknesses
While CuDeRes model had better performance, it seems the novelty of this model is not particularly high. The example GPR signals as shown in the paper appear to have quite distinct presentation from the normal case and from each other, thus it seems the problem is not very challenging for a deep learning model to detect. 
There lacks detailed description about the GPR data, adding to the difficulty to understand the paper. For example, the specific GPR device used, the frequency of the signal, the soil type, and the depth of the measurements are not mentioned. This makes it difficult to assess the generalizability of the proposed method. Furthermore, the paper does not specify the units of the GPR data, which is crucial for interpreting the results. 
In some places, the writing is a little bit difficult to follow and there are typos. For example, "U is a specific data blocks", should be "block".

### Questions
In modeling the three directions of GPR signals, it is understandable that there could be signal decay along the in-depth direction of the signal to the soil (the z direction according to Figure 4), but it is not clear why there should be signal decay along the other two directions. And even if so, why the decay coefficient theta is the same over all three directions in equation 3?
If seems there is a segmentation step as alluded in equation 10, how is segmentation done?
As the GPR moves down the track, is there any overlap in the data block in the method? 
It is not clear why equation 15 equals to zero? Does it mean W_1^out and W_2^out is everywhere equal? If so, why? If not so, then can authors elaborate why equation 15 is zero?
It seems that each direction in 3D is modeled separately and has their own model reservoir, if that is so, what happens in testing if at location, the GPR data is a good fit, for example, for x-, y- and z-direction models but these "good" models are not from the same data point in the training process, rather the fitted x-, y- and z-direction models were from different data points in the training set. Will that cause a problem for the whole method to process?

### Soundness
2

### Presentation
2

### Contribution
2
