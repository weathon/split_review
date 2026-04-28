# Debiasing Attention Mechanism in Transformer without Demographics

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Although transformers demonstrate impressive capabilities in a variety of tasks, the fairness issue remains a significant concern when deploying these models. Existing works to address fairness issues in transformers require sensitive labels (such as age, gender, etc.), which can raise privacy concerns or violate legal regulations. An alternative way is through fairness without demographics. However, existing works that improve Rawlsian Max-Min fairness may impose overly restrictive constraints. Other methods that use auxiliary networks could be parameter inefficient. In this paper, we present a new approach to debiasing transformers by leveraging their inherent structure.  By reconsidering the roles of important components (queries, keys, and values) in the attention mechanism, we introduce a simple yet effective debiasing strategy from two perspectives: 1) Grounded in theoretical analysis, we normalize and apply absolute value operations to queries and keys to minimize the bias in attention weight allocation; 2) We reduce the bias within values through local alignment via contrastive learning. Throughout the entire process, our approach does not require any sensitive labels. Furthermore, to enhance memory efficiency in the training phase, we propose a strategy that debias only the last encoder to improve fairness in pre-trained models. We conduct experiments in computer vision and natural language processing tasks and show that our method is comparable and even outperforms the state-of-the-art method with substantially lower energy consumption.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
**Rebuttal Update** After reading the author's rebuttal, I improved my score from a 5 to a 6. However, I would like to see the writing and clarity improve for a final paper if accepted. Specifically, the introduction and use of notation needs cleaning, as well as the motivations in the introduction. I would also like a bit more explanation of the contrastive learning method and its motivations in the context of the whole work.

In this paper, the authors propose a new method for debiasing the attention mechanism to achieve fairness without prior subgroup definitions. Their method consists of two components. First, they normalize the token embeddings in their Query and Key matrices and absolute value them to bound the attention weight difference across sensitive attributes. Second, they use a contrastive loss to encourage the embeddings of samples from the same class to be similar to each other, encouraging equal representation across sensitive attributes while maintaining performance. Then, the authors provide extensive empirical evaluation of their fairness method across two vision and two language tasks.

### Strengths
This paper builds on a wide literature of debiasing methods, and does a great job of synthesizing methods from fairness aware transformers with methods in fairness without demographics. Furthermore, the method is straightforward and the first part can be applied easily to any attention mechanism, whereas the second requires a small amount of fine tuning of a nonlinear head. The entire system can be applied out of the box to existing models with little or no training. Another thing I really liked about the paper is the green analysis of the power consumption of the method. I think this is a great step forward for researchers in the field.

### Weaknesses
One weakness of the paper is the motivation. While debiasing models / fairness is generally a strong motivation, the authors do not explain in much detail why it is important to debias attention mechanisms. Instead, most of the introduction feels like a "related works" section, where the main motivation of the paper is the failings of previous methods. I would like to see a better written introduction that explains why the failings of previous methods are bad or costly, and why a new method is needed. 

Other parts of the paper are not very clear as well. What motivates the fairness optimization problem (2)? Why do we care about attention weight values when in fairness we traditionally care about outcomes? While having the same activations results in the same outputs of course, it seems to me to be extreme to limit the expressivity of the model across sensitive attributes.

Furthermore, the notation in the paper is pretty messy and unclear. In section 3.1, in the first paragraph the vectors $\textbf{q}, \textbf{k}$ are not introduced as slices of the $Q$ and $K$ matrices. Also the relationship between the dataset $\mathcal{D}$ and how it is inputted into the attention mechanism/transformer model is not mentioned at all (it just jumps straight from dataset notation to attention notation with no connection between the two). In Section 3.2 near the end, what is $q_{cls}$?

I would like to see a better figure explaining the pipeline or mathematical equation of the entire model. $g$ is only mentioned before eqn. (7), but not ever shown visually, this makes it very unclear as to how to implement the second modification and is a bit misleading as we require an additional layer to train to align the model. 

Finally, I would like to see an ablation study of the two mechanisms to compare which one impacts fairness more.

### Questions
What is the practical/fairness motivation behind the fairness optimization problem, and the motivation behind debiasing attention as a whole? 

Also, it seems as though instead of using subgroup attributes in the contrastive loss, you use classes. However, what happens if each class is dominated by a single sensitive group attribute? For example, if class 1 is all male and class 2 is all female, then requiring all class 1 (male) representations to be similar with each other and different than class 2 (female) will actually cause more disparity by pushing the representations away from each other. Don't we have to assume sensitive groups are balanced within classes?

Finally, just as a curiosity, won't normalizing reduce the expressivity of the model? I would love to see the distribution of attention weights before and after normalizing, as well as before and after absolute valuing (as well as an ablation study of the two steps).

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work focuses on the attention mechanism to debias the transformers without assuming access to the sensitive attribute information. For this, two steps have been performed. First, they propose a weight relocation mechanism by normalizing (subtracting mean and dividing by standard deviation) and taking the absolute value of query ank key vectors in the attention module. 
A theoretical insight is also provided to show that this bounds the discrepancy for various sensitive attributes. 
Then, a nonlinear mapping is applied on tokens with higher attention values to map them to a latent representation $v \rightarrow z$. Then, supervised contrastive learning is applied to the latent representation to make sure that the embedding for the samples from the same class has core similarity.

### Strengths
The paper is generally written well and easy to follow, even though some parts are missing (will discuss later).

The idea of focusing on the attention module and debiasing the transformer without assuming access to the sensitive attributes is really interesting. 

As this approach is not computationally intensive (based on the experimental results provided in section 4) and is not making significant changes to the architecture, it can be easily added during training to most of the transformer-based structures and improve fairness.

### Weaknesses
This paper has some weaknesses and I believe addressing these weaknesses can improve the quality of the paper:

1. Intuitively I understand that as the attention mechanism shows the importance of different patches during training/ inference, it can have a large impact on introducing bias. However, authors need to justify in a more systematic way, why using only the attention mechanism is powerful enough to debias a transformer structure. As an example, an analysis in a controlled setup (when we have access to sensitive attributes) can be provided to show that the attention module is the one that mostly affects the bias, or similar experiments to justify this. Specifically, a sensitivity analysis could be performed where the attention weights are perturbed and the resulting change in bias is measured. This would provide a more concrete justification for focusing solely on the attention mechanism.

2. Similarly, authors need to justify why the optimization objective in Eqn. (2) (minimizing the disparity in attention weights) can be a good approximation to the fairness metrics? I believe there should be an approximation error as instead of considering the output, we are just considering the attention weights. A detailed analysis is required to justify this alternative definition. It would be beneficial to see a formal derivation or empirical evidence demonstrating the correlation between minimizing attention weight disparity and improving fairness metrics like demographic parity or equal opportunity. The authors should also discuss the limitations of this approximation and under what conditions it might fail.

3. The statistics of the $q$ and $k$ are estimated during training and then used as an estimation during inference. Authors should provide more details on the accuracy of this choice, as the distribution shift during training and inference might affect both fairness and classifier performance. The paper lacks a discussion on how the running mean and standard deviation are updated during training and how sensitive the method is to the choice of the update rate. Furthermore, the authors should provide an analysis of the potential impact of distribution shift between training and inference on the estimated statistics and the overall performance of the debiasing method.

4. In section 3.4., more details are required regarding debiasing the pre-trained network by inserting the encoder layer. This part was not clear to me. Specifically, the authors should clarify how the inserted encoder layer is initialized and trained, and how it interacts with the pre-trained weights. The paper should also discuss the potential impact of this insertion on the overall architecture and performance.

5. The experimental results are not convincing enough as a very limited number of combinations for label $y$ and sensitive attributes $A$ are used. 
- Authors should provide various combinations to show the generalizability of the results. 
- In addition, for different datasets, different combinations are used which may give a bad impression of cherry picking.
- On average, the proposed method is not better than previous approaches and the main benefit is less compute. I wonder wether this approach can be combined with previous methods to give better performance in terms of reducing bias and preventing the degradation in the classifier accuracy?

small typo in Figure 1: dotted line $\rightarrow$ solid line

### Questions
please refer to weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method to address fairness issues in vision transformers and natural language processing transformers without requiring access to sensitive demographic attributes during training. The key contributions are:

- They identify two sources of bias in transformers: misallocation of attention weights and bias in value vector representations. 

- To address attention weight bias, they normalize and take the absolute value of query and key vectors before computing attention. This is motivated by theoretical analysis showing it reduces disparity in attention weights between groups.

- For value vector bias, they use a supervised contrastive loss on the core value vectors to encourage consistency between groups. 

- The method is evaluated on vision and NLP tasks, showing improved fairness metrics compared to prior work without demographics. It also enables efficiently debiasing pretrained models by only retraining the last encoder layer.

- Overall, the method provides a simple and effective way to improve transformer fairness without needing sensitive attributes, auxiliary networks, or restrictive constraints. The ablation studies demonstrate tradeoffs between fairness and accuracy.

### Strengths
- The paper tackles an important problem - improving fairness in transformers without needing sensitive attributes. This is challenging but highly relevant given privacy regulations. 

- The approach of debiasing attention weights and value vectors specifically is novel. Prior work either operates on the full representations or relies on adversarial training, which can be unstable. Deconstructing the transformer in this way is creative.

- The method is simple, leveraging existing operations like normalization and contrastive loss. Avoiding complex auxiliary networks is a plus for efficiency.

- Results on vision and NLP datasets demonstrate improved fairness over prior art like DRO and knowledge distillation. The method also enables efficient debiasing of pretrained models.

- Theoretical analysis provides justification for the attention weight debiasing, and empirically shows the approach achieves near optimal fairness-accuracy tradeoffs.

### Weaknesses
 - For NLP, the scheme of picking top value vectors may be less effective for long sequences. Dynamic selection based on attention may work better.

- The last layer retraining is convenient but provides no guarantees. Analyzing how bias propagates through the full network could further improve this.

- The contrastive loss operates locally on values. Extending the alignment more globally could potentially improve fairness further without sacrificing accuracy.

- No rigorous ablation study is provided to analyze the individual effects of the attention and value debiasing components. Their relative contributions are unclear.

### Questions
see weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper aims at the fairness issue when deploying models. This paper presents an approach to debiasing transformers using their inherent structure. The authors propose some methods to handle the queries, keys and values to reduce the bias. Also, the memory efficiency in the training phase is enhanced.

### Strengths
1. The overall writing is clear. 
2. The problem of fairness issue when deploying models is important.

### Weaknesses
The biggest problem is the experiment settings and results.

1. In the experiment tables, which method belongs to "Fairness without Demographics", which method requires Demographics?
2. The proposed method cannot beat SOTA methods. For example, in Table 2, the proposed method is worse than LfF on EOp dataset. In Table 4, the proposed method is worse than JTT method on EOp and EOd dataset.
3. Following problem 2, the authors may claim that they have much less energy consumption. However, the comparison is not straightforward. The authors need to show one of the two results to claim this point: 1) same energy consumption and higher accuracy; 2) same accuracy and less energy consumption. If the authors can show these results compared to LfF on EOp dataset, and JTT method on EOp and EOd dataset. I will raise my score.
4. Energy consumption is not a stable indicator when comparing the models. The hardware may have big influence. I would recommend to use FLOPs to compare these methods.

### Questions
see weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
