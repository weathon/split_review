# Revisiting Mode Connectivity in Neural Networks with Bezier Surface

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Understanding the loss landscapes of neural networks (NNs) is critical for optimizing model performance. Previous research has identified the phenomenon of mode connectivity on curves, where two well-trained NNs can be connected by a continuous path in parameter space where the path maintains nearly constant loss. In this work, we extend the concept of mode connectivity to explore connectivity on surfaces, significantly broadening its applicability and unlocking new opportunities. While initial attempts to connect models via linear surfaces in parameter space were unsuccessful, we propose a novel optimization technique that consistently discovers Bézier surfaces with low-loss and high-accuracy connecting multiple NNs in a nonlinear manner. We further demonstrate that even without optimization, mode connectivity exists in certain cases of Bézier surfaces, where the models are carefully selected and combined linearly. This approach provides a deeper and more comprehensive understanding of the loss landscape and offers a novel way to identify models with enhanced performance for model averaging and output ensembling. We demonstrate the effectiveness of our method on CIFAR-10, CIFAR-100, and Tiny-ImageNet datasets using VGG16, ResNet18, and ViT architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates connecting multiple models in parameter space through constructing appropriate surfaces. It is well-known that a simple linear hyperplane does not suffice and non-linear methods are needed. To that end, the authors propose using Bézier surfaces, where four points are used to represent the model parameters and nine other points in the parametrization are subsequently optimized such that uniformly sampled surface points also have low loss. The authors show that they can construct surfaces exhibit low loss everywhere, thus succesfully connecting multiple models with a single surface. They further show that the best point on the surface outperforms all the individual models and can thus be used to merge several models.

### Strengths
1. The paper is very well-written and clearly explains the problem as well as the techniques that aim to solve them. I like that the proposed method simply consisting of Bézier curves remains rather simple.
2. The experiments performed show quite convincingly that the proposed method succeeds in connecting multiple minima. The authors also investigate a variety of architectures, making the results stronger.

### Weaknesses
1. There seem to be quite a few related works missing that also explore the construction of surfaces to connect multiple minima [1, 2, 3, 4, 5]. The authors definitely need to add the listed papers to the related works and clearly articulate how theirs is different and what advantages it provides. 
2. For model merging, the authors do not seem to compare against any other method? It would be interesting to understand whether this technique allows one to leverage the diversity from all the points (that were obtained using different inits and shuffling). Standard merging always needs to be careful to end up in the same basin, and thus diversity of the points seems naturally reduced. Similarly for the output ensembling experiments, the obvious baseline of solely ensembling the four end points is missing. Does the surface really provide diversity beyond those four points? This is currently unclear with the provided experimental results.
3. I think taking the best performing point on the entire surface is (1) a bit an unfair comparison and (2) very expensive to do as a dense grid of models needs to be evaluated on the test set. I think it would be more appropriate and efficient to compare against some sort of “mean” value on the surface. Does a Bézier curve admit a natural “centroid”? If yes, how does that one perform compared to the individual models? 
4. Another related work for model merging is [6] which explored how a given ensemble can be constructed within the same convex region, and thus also allowing to average weights while still profiting from diversity. It would be interesting to understand which approach works better.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores extending the concept of "mode connectivity" in neural networks from one-dimensional paths to two-dimensional surfaces using Bézier surfaces. Traditionally, mode connectivity demonstrates that two trained models can be connected by a low-loss path in parameter space. Here, the authors introduce a novel method to connect multiple models on a smooth, low-loss surface, broadening the potential for optimization and generalization. They detail an algorithm that constructs and optimizes Bézier surfaces to maintain low loss and high accuracy across various architectures (VGG16, ResNet18, ViT) and datasets (CIFAR-10, CIFAR-100, Tiny-ImageNet). The study finds that nonlinear surfaces outperform simple linear interpolations, especially for model averaging and ensembling applications, ultimately enhancing performance in tasks like model merging and ensemble accuracy.

### Strengths
1. The paper is well-written and well-organized. It is easy to read.
2. The visualizations and plots are also very clear, facilitating the understanding.

### Weaknesses
1. **Premature Claim of "Low-Loss Curve" in Line 161 (Bottom of Page 3)**.
In line 161, the paper refers to a "low-loss curve" as if it were already established, though at this point, neither the method nor specific criteria for determining a "low-loss" property have been introduced. Could the authors clarify what they mean by "low-loss" here and either postpone this claim until it is better supported or define it explicitly at the outset? Additionally, grounding this concept with a preliminary explanation or notation would improve clarity.


2. **Rationale for Defining $q_{uv}$ in Equation 8 and Substitution with Uniform Distribution**.
The definition of $q_{uv}$​ in Equation 8 lacks an explanation of its theoretical motivation and why it can be replaced by a uniform distribution for practical purposes. What are the specific benefits of this choice, and how does this approximation impact the accuracy or reliability of the surface mode connectivity in experiments? A deeper rationale for this formulation would clarify its role in the model's performance.


3. **Lack of Distance Quantification Between Corner Control Points in Loss Landscape Visualizations**.
The visualizations of the loss landscapes do not quantify or highlight the parameter distances between corner points (control points). If these control points represent very similar models with minor parameter variations, the diversity of the parameter space explored may be limited, especially when these models are trained under comparable conditions. How would the approach fare with intentionally diverse model initializations, varying training settings, or other augmentations? Such differences could test the robustness of the surface connectivity under broader training conditions.

4. **Limited Impact of Experiments and Marginal Gaps in Results (e.g., Table 1)**.
The experimental evaluation relies primarily on relatively small datasets like CIFAR-10, CIFAR-100, and Tiny-ImageNet, which may limit the generalizability of the findings to larger, more complex datasets. Additionally, Table 1 shows only marginal improvements between the baseline and the model merging or ensembling results. Could the authors address how these findings might scale to larger datasets and discuss the significance of these marginal gaps, particularly given the computational overhead involved in the proposed approach? Expanding on the implications for practical, large-scale applications would enhance the impact of these results.

### Questions
1. **Ambiguity in the Central Question About "Both Low Loss and High Accuracy" (Line 195)**.
The central question on line 195 could benefit from greater specificity regarding "low loss" and "high accuracy." Are the authors referring to training loss and testing accuracy? Given the generalization gap, distinguishing training and testing here would provide meaningful context. If both metrics are from the same set (either training or testing), the statement may be redundant, as low loss often correlates with high accuracy on that set. Specifying if this is about generalization (low training loss translating to high testing accuracy) could substantiate the relevance of this question.

2. **Scalability Concerns for Optimization of Many Parameters (θ) in Equation 6**.
Equation 6 implies a potentially extensive optimization of numerous control points (θ values) across the Bézier surface. This approach seems computationally heavy, especially for large models with millions of parameters. Could the authors discuss the scalability of this optimization? Is there any strategy to reduce the computational load or parameterize this approach efficiently to make it viable for larger architectures?

3. **Justification for Selecting Models from Specific Epochs (Figure 6)**.
Figure 6 shows models chosen from epochs 220, 200, 180, and 160. However, it’s unclear why these specific epochs were selected or why only a single training trajectory was used. Would models from other epochs, or from different training trajectories, produce similar results? Providing a rationale for these choices or showing comparative results could help validate the generalizability of this selection process.

### Soundness
3

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
The paper explores the concept of mode connectivity in neural network loss landscapes, expanding it from traditional curve-based connections to surface-based connections. This approach offers a comprehensive way to merge models, enabling applications such as model averaging and output ensembling.

### Strengths
1.	Extending mode connectivity from curves to Bézier surfaces is a significant topic.
2.	The proposed method is sound.
3.	Writing is good to follow.
4.	The figure illustration is good in this paper

### Weaknesses
1.	Only evaluate the performance on small datasets. Large datasets like image-net should be included.
2.	Lack of theoretical analysis.

### Questions
See the above weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
