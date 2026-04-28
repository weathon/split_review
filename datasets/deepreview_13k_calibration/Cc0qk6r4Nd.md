# Internal Cross-layer Gradients for Extending Homogeneity to Heterogeneity in Federated Learning

- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 8, 5, 8

## Abstract
Federated learning (FL) inevitably confronts the challenge of system heterogeneity in practical scenarios. To enhance the capabilities of most model-homogeneous FL methods in handling system heterogeneity, we propose a training scheme that can extend their capabilities to cope with this challenge.
In this paper, we commence our study with a detailed exploration of homogeneous and heterogeneous FL settings and discover three key observations: (1) a positive correlation between client performance and layer similarities, %across distinct client models, 
(2) higher similarities in the shallow layers in contrast to the deep layers, and (3) the smoother gradient distributions indicate the higher layer similarities.
Building upon these observations, we propose InCo Aggregation that leverages internal cross-layer gradients, a mixture of gradients from shallow and deep layers within a server model, to augment the similarity in the deep layers without requiring additional communication between clients. 
Furthermore, our methods can be tailored to accommodate model-homogeneous FL methods such as FedAvg, FedProx, FedNova, Scaffold, and MOON, to expand their capabilities to handle the system heterogeneity.
Copious experimental results validate the effectiveness of InCo Aggregation, spotlighting internal cross-layer gradients as a promising avenue to enhance the performance in heterogeneous FL.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors observe that layer similarities are related to accuracy for some FL models. They also observe that layer similarities are related to gradient distribution smoothness. Based on these observations, they modify the learning approach to increase similarities between shallow and deep layer gradients. This modification results in improved accuracy for a variety of FL methods and datasets. They also provide for layer splitting and other engineering necessities to evaluate their ideas, but I found the observations and modification above to be the most interesting and novel.

### Strengths
+ This is an interesting paper to read.

+ The paper combines experimental approaches to scientific discovery and system engineering to use these discoveries to produce improved accuracy.

+ The visualizations of findings and diagrams are clear.

+ The writing is well organized.

### Weaknesses
 - The reasons for the relationships observed by the authors are not well explained, although Section 5.4 makes a mostly unsuccessful attempt at doing so. The authors find that high-accuracy models tend to have particular properties and push the learning process to produce those properties without well explaining why the properties result in accuracy. They do, however, demonstrate that their approach works so it's a question of depth of understanding, not merit.

- Section 3.3 seems central to enabling improvement but it is relatively short, without much justification for design decisions. It states what is done but now why this is the most appropriate approach.

### Questions
1) Is there a fundamental justification for the form of expression 1, or might other expressions perform as well or better?

2) Why did you decide to simply constrain gopt from opposing g0 (with an inequality) instead of imposing a cost that increases with decreasing dot product?

3) What is the relationship between your findings and those regarding the contribution of residual connections in ResNets?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper highlights the positive correlation between client performances and layer similarities in a federated setting, specifically how similarities are higher in shallow layers of the network and steadily decrease as one gets to the deeper layers as well as how smoother gradient distributions correspond to higher layer similarities. 
Keeping these ideas in mind, the paper proposes InCo Aggregation, which leverages cross-layer gradient similarities to improve the similarity across clients in deeper layers, without the need for additional communication between clients.
Overall, InCo Aggregation is validated on both model-homogeneous and heterogeneous methods to highlight its impact in improving performances across the board.

### Strengths
- The observations on similarity at varying levels of deep networks across clients could potentially establish an observation mechanism for federated settings to analyze the impact of changes across multiple axes like data settings, model heterogeneity, etc.
- Figures 4 and 6 do a good job at conveying concepts surrounding various model splitting methods and gradient divergence, respectively.

### Weaknesses
 - "System level heterogeneity" is mentioned multiple times and is loosely defined through the early portion of the manuscript (Pg. 1, Paragraph 1). Over the course of reading the paper, one can figure out data and model heterogeneity are the relevant axes along which system level heterogeneity is defined. Defining these ideas earlier and more concisely would allow the reader to contextualize the problem domain and understand how the solution being proposed fits within its scope.
- While the paper discusses the relationship between gradient similarity and performance/accuracy, and gradient similarity with smoother gradients, the key justifications for choosing to use smoother gradients are (a)  lack of a shared database, (b) Features would increase communication overheads, and (c) correlation between similarity of gradients and smoothness. Are there stronger correlations between the level of similarity (actual value) to the peak density or other statistics of the gradients, such as variance, skewness, or kurtosis, that might provide a more robust justification for the method?
- There doesn't seem to be a an explicit definition of "deep" vs. "shallow" layers. Implicitly, within each stage there seem to be shallow and deep layers (Pg. 3, Cross-environment similarity). In general, there are certain experimental settings necessary to fully understand the figures plotted through the course of the manuscript that seem to be missing. For example, the specific layer indices or types being analyzed in the gradient distribution plots are not clearly stated, making it difficult to reproduce or fully interpret the results.
- Given the specific model heterogeneity settings under which InCo Aggregation is applicable, a discussion on how and where it isn't applicable (e.g., Complete model heterogeneity, where models are restricted to be within the same family of backbones) would be useful. This is particularly important for understanding the scope and limitations of the proposed method in practical federated learning scenarios, where diverse model architectures are common.

### Questions
- Could the authors define the notion of system level heterogeneity, using model and data heterogeneity, earlier and provide connection points to how the proposed method would address these issues. Having these points described earlier would allow the reader to grasp the importance of the observations described later on.
- Could the authors provide gradient plots like in Figs 2 and 3 for Stage 2's layers as well? Drawing a parallels to behavior across Stages would be helpful in establishing the consistency of the observations on smoother gradients and how they relate to similarity values.
- Could the authors provide an explicit definition of which layers can be considered deep vs.shallow? If the nomenclature implicitly defined in "Cross-environment Similarity" is to be maintained, could the authors provide an explanation of whether this pattern carries over to ViTs as well?
- Could the authors discuss further about similarity patterns in ViT's and how this impact the observations and InCo aggregation as a whole?
- Could the authors provide more detail explanations for the exact setups used to generate Fig. 1, 2, and 3?
- Could the authors provide more insight into how Fig. 3 would vary when tested across multiple trials? This could help remove the uncertainty caused by SGD noise.
- Could the authors provide the standard deviation values for InCo-based methods?
- Given the variation in performances in Table 3 and the original values cited under FedROLEX, ScaleFL, etc., could the authors provide a detailed breakdown of how the experimental settings differ from the original works?
- A discussion on how and where it isn't applicable (e.g., Complete model heterogeneity, where models are restricted to be within the same family of backbones or in cases where weight matrices do no align) is critical to understand and apply the proposed method.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tackles the challenge of heterogeneous models within federated learning, uncovering a notable pattern where shallow layers exhibit similar gradient distributions, in contrast to the disparate distributions in deeper layers. The authors further observed that higher gradient similarity corresponds to improved accuracy. Capitalizing on these insights, a novel aggregation method is proposed and substantiated through comprehensive experiments, demonstrating the efficacy of the proposed approach in navigating model heterogeneity.

### Strengths
1. The author presents intriguing findings regarding the relationship between layer similarity and model performance.
2. By refining the direction of deep layers, which exhibit lower gradient similarity compared to shallow layers, the author enhances model performance.
3. The proposed method demonstrates versatility, adaptable to various Federated Learning (FL) schemas.
4. The effectiveness of the proposed method is substantiated through extensive experimentation.

### Weaknesses
1. The utilization of a model with merely three convolutional layers is unconvincing; larger models should be employed in primary experiments to validate the findings. The analysis should include a more diverse set of architectures, and the use of a small model raises concerns about the generalizability of the observed gradient similarity patterns to more complex networks.
2. The manuscript could benefit from a more coherent narrative, including background on previous works, an introduction to the CAK similarity metric, and a discussion on why the proposed method outperforms state-of-the-art (SOTA) methods, especially in handling model heterogeneity. The lack of a clear problem definition and motivation makes it difficult to assess the novelty and significance of the proposed approach. The manuscript should also clarify how the proposed method addresses the specific challenges of model heterogeneity compared to existing methods.
3. Figure 6 lacks clarity; indicating the positions of client and global optima could elucidate the depicted concepts. The current visualization does not effectively communicate the optimization landscape and the impact of the proposed method on convergence. The figure should clearly show how the proposed method navigates the optimization space compared to standard federated learning approaches.
4. It is imperative to delineate the problem definition and notations before introducing the method, ensuring a logical flow and better comprehension. The current presentation makes it difficult to understand the scope and limitations of the proposed method. A clear problem statement is needed to establish the context for the proposed approach.
5. The manuscript does not adequately explain how cross-layer gradient adjustments ameliorate the effects of model heterogeneity. The mechanism by which these adjustments lead to improved performance is not clearly articulated, and the manuscript should provide a more detailed explanation of the underlying principles.

### Questions
1. I wonder if the proposed approach can be applied to complex models. 
2. I wonder how cross-layer gradient adjustments ameliorate the effects of model heterogeneity.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
this paper discover three interesting observations based on the exploration between homogeneous and heterogeneous FL settings. Then the authors propose InCo Aggregation methods, inpried by these observation and demonstrate the proposed method can be tailored to accommodate model-homogeneous FL methods and achieve better performance.

### Strengths
The paper is well-written and easily understandable, effectively communicating the research in a clear and coherent manner.

The discovered observations are interesting and valuable for future research, providing a foundation for further investigations and potential advancements in the field.

The experiments conducted in the paper are sufficient, with an appropriate and comprehensive setup that collects relevant data to support the claims and conclusions.

### Weaknesses
1. CKA is an important metric in this paper. The authors should explain it in more details.
2. Model splitting is proposed to facilitate model heterogeneity. What if the layer-wise gradient sizes of different models are not the same, how do you conduct cross-layer gradients mergence?

### Questions
1. where is CKA from in Fig. 1 (c). Is it the average value of all stages or deep/shallow stage?
2. Can you provide a more detailed comparison of InCo Aggregation with other state-of-the-art methods for handling system heterogeneity in FL? How does InCo Aggregation compare in terms of performance, communication overhead, and computational complexity?
3. The paper does not provide a detailed analysis of the computational and communication overhead of InCo Aggregation, which could be a significant factor in large-scale FL applications. This limits the practical applicability of the proposed approach.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
