# NeurFlow: Interpreting Neural Networks through Critical Neuron Groups and Functional Interactions

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Understanding the inner workings of neural networks is essential for enhancing model performance and interpretability. Current research predominantly focuses on examining the connection between individual neurons and the model's final predictions, which suffers from challenges in interpreting the internal workings of the model, particularly when neurons encode multiple unrelated features. In this paper, we propose a novel framework that transitions the focus from analyzing individual neurons to investigating groups of neurons, shifting the emphasis from neuron-output relationships to the functional interactions between neurons. Our automated framework, NeurFlow, first identifies core neurons and clusters them into groups based on shared functional relationships, enabling a more coherent and interpretable view of the network’s internal processes. This approach facilitates the construction of a hierarchical circuit representing neuron interactions across layers, thus improving interpretability while reducing computational costs. Our extensive empirical studies validate the fidelity of our proposed NeurFlow. Additionally, we showcase its utility in practical applications such as image debugging and automatic concept labeling, thereby highlighting its potential to advance the field of neural network explainability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Summary:
The presented manuscript  proposes  the framework NeurFlow which offer interpretability to neural networks by focusing on groups of critical neurons. The framework tries to detect critical neurons and clusters them based on shared functionality, constructing a hierarchical circuit to model their interactions. The importance of the selected neurons is validated by comparing their impact on the model’s performance to random groups of neurons. Finally the manuscript also offers potential applications, e.g to debug model biases.

### Strengths
Strengths:
•	The identification of groups of critical neurons offers a way to tackle a node’s polysemantic behaviour.

•	The application of MLLMs to annotate group circuits is novel and original. This offers a nice way to explain a model’s decision.

•	The papers is very complete and self-contained. The proposed methodology is tested on different level as the authors don’t only look at the dependence of the model’s performance on the critical neurons, but also assess the optimality of their selection with the additional “Optimality of critical Neurons” experiment. Additionally the authors explore applications of their proposed approach.

### Weaknesses
Weaknesses:
•	The formal definition of a  group of critical neurons of is not obvious to me. Heuristically critical neurons are defined as neurons who, if knocked out, would result in a substantial change in performance. The formal definition however defines the critical neurons of neuron a as the group of neurons who, when knocked out, cause the neuron concept of neuron a ($\mathrm{V}^{\mathbb{S}}_a$) to be the most different from the original neuron concept ($\mathrm{V}_a$), as the cardinality of the intersection will then be small. This definition focuses on the change in the neuron's concept representation rather than the direct impact on the model's output, which is not immediately intuitive.

•	The description of the experiments are difficult to understand and it misses some important aspects to properly assess the results ( see questions below). The conclusion taken from these experiments are therefore not necessarily supported by the experiments. For example, the optimality experiment lacks confidence intervals, making it hard to assess the significance of the results. The masking/retaining experiments also lack clarity on how the random neurons are selected, specifically if the number of random neurons per layer is equivalent to the number of critical neurons at that layer.



### Questions
Questions:
1)	How dependent are the results on the choice of the hyperparameter k in the neuron concept $\mathrm{V}_a$ ? 
2)	In the “neuron clustering algorithm based on the semantic groups”, is the concept of the neuron $s_i$, namely $\mathrm{V}_{s_i}$ a subset of the parent neuron’s concept $\mathrm{V}_a$? Intuitively, if the neurons are indeed critical for neuron a this should be the case correct? From Algorithm 3 in supplemental material it seems that the neuron concept $\mathrm{V}__{s_i}$ is identified independently of the parent’s concept. 
3)	In the experiment to detect the optimality of the critical neurons the authors mention: “For each setting we randomly select 50 target neurons (denoted by a_i) from 10 distinct classes”. Does this mean the authors select in total 500 (50 x 10 neurons) or are 5 neuron selected per class ?
4)	In the experiments leading to Figure 4: Could the authors please indicate the confidence intervals as the results are averages over different selections of random groups of neurons ? It would be interesting to see the spread of the loss to note if some random groups of neurons reach near optimality. 
5)	The weight $W(G_i,G_j)$ in Equation 5 seems to be unnormalized with respect to the number of neurons in $\mathbb{S_i}$ and $\mathbb{S_j}$. Doesn’t this make it difficult to interpret these weights over different groups of neurons?
6)	How are the random neurons selected in the masking/retaining experiment? Are the number of random neurons per layer selected in an equivalent amount as the number of critical neurons at that layer? Or is only the total number of random neurons matched to the cardinality of the set $\mathbb{S}_a$ ?
7)	The behaviour of the critical nodes in the multi-layer retaining experiment does not  seem to support the interpretation of critical nodes, as the performance significantly decreases (or fluctuates) with increasing layers.

Additional comments
Line 056: “there” -> “their”
Line 181: “our” -> “out”
Line 250: “its all” should be replaced with “all its”
Line 311: There seems to be a word missing from this sentence to make it coherent.
Figure 4: The current choice of color & marker shape is not very intuitive to grasp the message of the figure. Using a consistent colour for critical/random and varying the marker between different values of $\tau$ might make interpreting the figure more easy.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper argues that it is most useful to analyze neural networks through the lens of groups of neurons rather than individual neurons. It describes an algorithm for constructing such groups, which can be used to construct hypertrees of which neuron groups are involved in each class prediction. The algorithm works by creating a dataset of visual features (which I believe are different crops of different dataset classes), then for each neuron constructing the "neuron concept", which is the top K visual features that the neuron activates. The algorithm then looks for the critical input neurons to each neuron, which is defined as ones which would change the neuron concept if removed. (This is actually done via an importance score, since calculating this fully in set form would be too computationally costly). Then, one can construct a hypertree of neurons involved in predicting a class, based on finding the critical neurons of the final logit and then on downwards.

### Strengths
- This paper engages with the problem of neuron analysis in a way that seems to pragmatically balance between the purist but unscalable approach of individual neurons, and the combinatoric explosion of looking at every possible circuit 
- The paper did rigorous analysis of both the correctness and the usefulness for interpretability of the neurons they find, as well as calling out explicit useful applications

### Weaknesses
The paper defines a lot of terms (critical neuron group, neuron concept, neuron circuit/hypertree, visual feature) that are in colloquial language somewhat similar, and I think it could have benefitted from a glossary figure that explicitly defines all of these with reference to one another, so that a reader can flip to it if needed. I was unclear on how the semantic grouping vector was calculated, and which feature maps were explicitly within each visual feature. Are visual features individual images? Images of a class? Some subset of images within a class? I was unclear on this, and it made it harder to understand the rest of the paper. The description of visual features as "partitioning [a dataset] into smaller features of various sizes" is vague and does not clearly convey that the process involves cropping image patches. This lack of clarity makes it difficult to understand the construction of the visual feature dataset and how it relates to the original image data.

### Questions
- I was unclear on how the semantic grouping vector was calculated, and which feature maps were explicitly within each visual feature
- Are visual features individual images? Images of a class? Some subset of images within a class? I was unclear on this, and it made it harder to understand the rest of the paper

### Soundness
3

### Presentation
2

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
The paper proposes NeuroFlow, a framework designed to identify the set of connected neurons (i.e., circuit) that most strongly influence the predictions of a target class. The framework begins by clustering neurons based on their semantics and then reconstructs the circuit through interactions between clusters across the network structure. The framework's main steps are as follows:

1. For a given neuron at layer L, the critical neurons for its output at layer L-1 are identified. These critical neurons are the ones whose removal causes the highest change in the top-k patches associated with the target neuron. This set is approximated by an algorithm that sums attributions (calculated using Integrated Gradients) for the identified top-k patches.
2. The Top-k patches activated by the neuron are clustered into semantic groups using agglomerative clustering, where each cluster represents a semantic concept captured by the neuron.
3. The algorithm calculates the contribution of each critical neuron in the preceding layer to each semantic group identified in the previous step.
4. Semantic groups from the entire layer are clustered based on their similarity, and neurons that share at least one clustered semantic group are clustered together.
5. A multimodal LLM labels the clustered semantic groups
6. The concept circuit is generated using the connections and the attributions of the critical neurons within each semantic group.

The proposed framework is evaluated by assessing (1) the approximation accuracy of the heuristic used to compute critical neurons, (2) the impact of critical neurons with respect to a random baseline, and (3) the correlation between attribution scores and accuracy loss when neurons are removed. The paper also demonstrates an application of NeuroFlow to the problem of bias detection.

### Strengths
- The paper is well structured, clear, and quite easy to follow (with some caveats noted in the weaknesses section) 
- The polysemantic nature of neurons is often overlooked in the current literature, particularly in works focused on circuits. The paper's attention to this topic, even if only partially addressed (see weaknesses), is highly relevant and of interest to the ICLR community.
- Some of the characteristics of the frameworks are both novel and promising. In particular, step (3), the possibility for a neuron to be “active” in multiple clusters, and the connections between semantic groups are a clever way to deal with polysemantic neurons. 
- The integration of previously explored directions into a unified framework offers a fresh perspective on the topic.

### Weaknesses
The main weakness of the paper regards the evaluation and supporting experiments. There is a mismatch between the strong claims and the evidence provided. The current evaluation adequately validates the framework’s design choices. However, it does not place the work in the broader context of the ongoing research on this topic. Given substantial improvements in this direction, I would be willing to increase the score.

In more detail, several steps of the framework have been explored in prior literature, albeit sometimes with different objectives. Analyzing the connections between the outcomes of these steps and findings from other approaches would greatly strengthen the paper. Below are some specific examples of this point.
- Step 1 identifies critical neurons. The way in which they are identified (in relation to the top-k patches) seems novel to me. However, the concept of critical neurons for a particular prediction or a class has already been studied in the literature. For example, authors of [1]  identify class-specific critical neurons. They found that a small subset of neurons, when removed, leads to significant shifts in prediction. Similarly,  (Vu et al., 2022) explore related concepts.  How do the findings in these papers relate to those in this work? Is there an overlap between their critical neurons and those identified here? If not, what could explain the differences?
- The paper claims to “demonstrate that for a particular task, only a subset of neurons—referred to as critical neurons—have a substantial influence on the model’s performance”.  However, the experiments only show that, on average (but not always), the identified critical neurons have a greater impact than randomly selected neurons. This mismatch should be addressed either by providing additional experiments that prove that no other neurons outside the critical impact the class or by lowering the claim.
- A large body of literature explores the extraction of circuits (like the ones cited in the paper). Although the circuits’ structures may differ, it would be valuable to compare their components. Do they share the same neurons? What important features are missing in prior approaches that the proposed framework captures? This would help clarify the unique contributions of this work.
- The point raised by the authors about “groups of neurons within each layer also collectively encode the same concept” is quite well known. On this topic, a highly related work is [2], which identifies collaborative neurons responsible for the recognition of a concept. Similarly to the previous points, it would be great to see a comparison in terms of finding between this paper and the cited related work.


Other weaknesses that didn’t impact my current score:
- Polysemantic behavior is not limited to the highest activations. Several previous works indicate that neurons can recognize concepts at the lowest activations or across a range of activations [3,4,5]. However, the current framework relies upon and analyzes only the highest activations to compute the “visual features”. Therefore it is not guaranteed that the critical neurons extracted are the only ones contributing to the recognition of those concepts. Note that some alternative approaches [1,  (Vu et al., 2022)] for computing critical neurons are immune to this problem. Given the emphasis on polysemantic behavior, I encourage the authors to acknowledge this aspect as a limitation, a future direction, or to provide a more generalized formulation of the framework applicable to a broader range of settings.
- Some terminology in Section 3.2 could be confusing for practitioners unfamiliar with the domain. Specifically, terms like "neuron concept," "top-kkk patches visual features," and "top-kkk patches" may cause confusion. For example, definition 1 defines the set of top-k patches as the “neuron concept”. That name implies that these patches represent a single concept, whereas, in later sections, they denote a set of visual features (or concepts) recognized by the neuron. Based on the equation and the paper's narrative,"top-k patches" would be a better term here.  The words “visual features” and patches are used interchangeably throughout the text, even if they are not exactly the same. Traditionally, “visual features” refer to the semantic: the same visual feature can be captured by several patches, so there could be five patches that identify one visual feature. For clarity, I suggest using "patches" where possible and reserving "visual features" for references to their semantic meanings. For instance, lines 201-205 would be clearer if the first and last occurrences of "visual features" were replaced with "patches."

### Questions
Please check the weaknesses section. Several parts include direct or indirect questions for the authors and I would appreciate their answer and clarification.

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel framework, NeurFlow, to enhance the interpretability of deep neural networks (DNNs) by focusing on critical neuron groups and their interactions, while existing works focus more on interpreting individual neurons. The framework proposes constructing hierarchical circuits encapsulating critical neuron interactions across layers, providing a more holistic view of model decision-making.

The proposed method can be summarized in the following steps.
(1) Identifies critical neurons 
(2) Clusters these neurons into groups
(3) Investigate the functions and interactions of these groups.

### Strengths
• The paper introduces a novel way to identify semantic groups by leveraging clustering. By clustering neuron responses into semantic groups, the proposed method can interpret the target model with more specified concepts.

• Interesting applications of the proposed method with easily understandable figures.

•  The paper is well-written and easy to understand, except for a few parts.

### Weaknesses
Although the paper showed novelty and interesting results, I still have some concerns about this paper.

Major remarks

1. Existing works like [1*] and [2*] investigate neuron groups as fundamental units for explaining the internal workings of deep neural networks. Especially, [1*] proposes a similar idea of identifying critical neurons from different layers with importance scores derived from integrated gradients, which should be compared. Also, what are the major strengths of this paper regarding [1*] and [2*]?

2. This paper aims to enhance the interpretability of deep neural networks (DNNs). However, the proposed method only evaluated on CNNs (ResNet and GoogLeNet). Does the proposed method also work in other architectures like ViTs?

Minor remarks

1. How many random crop patches are needed to guarantee the stable performance of NeurFlow?

2. Various ways of determining the importance score should be evaluated (i.e., various approximations of Shapley value)

3. Existing works like [3*] identify neuron responses with highly activating crop and original images. It also investigates basic groups of neurons for decision-making, which should be referred to in the paper.

4. In Figure 6, why do some layers(i.e., 2,3,4 in resnet and 3b, 4b, 4d in googlenet) have low correlations compared to the previous and subsequent layers? Can you share some insights regarding this result?

5. Shouldn't it be "knocking out these neurons" In line 181?

### Questions
Please address or explain the remarks in the above Paper's Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2
