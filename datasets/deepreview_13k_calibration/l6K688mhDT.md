# Rethinking the Bias of Foundation Model under Long-tailed Distribution

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 6, 5

## Abstract
Long-tailed learning has garnered increasing attention due to its practical significance. Among the various approaches, the fine-tuning paradigm has gained considerable interest with the advent of foundation models. However, most existing methods primarily focus on leveraging knowledge from these models, overlooking the inherent biases introduced by the imbalanced training data they rely on. In this paper, we examine how such imbalances affect long-tailed downstream tasks. Specifically, we refer to the biases in foundation models and downstream tasks as parameter imbalance and data imbalance, respectively. Through fine-tuning, we observe that parameter imbalance plays a more critical role, while data imbalance can be mitigated using existing re-balancing strategies. Moreover, we find that parameter imbalance cannot be effectively addressed by current re-balancing techniques, such as adjusting the logits, during training, unlike data imbalance. To tackle both imbalances simultaneously, we constitute a causal structure graph and view the partial semantic factor as the confounder, which brings spurious correlations between input samples and labels. To resolve the negative effects of this, we propose a novel backdoor adjustment method that learns the true causal effect between input samples and labels, rather than merely fitting the correlations in the data. Experimental results validate the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the long-tail learning problem in foundation model fine-tuning from a novel perspective by considering both parameter imbalance (from pre-training) and data imbalance (from downstream tasks). The authors propose a causal inference framework to analyze these two types of imbalance and introduce a backdoor adjustment method to learn the true causal effects. Experiments conducted on three long-tailed datasets (ImageNet-LT, Places365-LT, iNaturalist2018) with various foundation models demonstrate the effectiveness of the proposed approach.

### Strengths
The paper presents a novel perspective on long-tail learning by considering the dual impact of pre-training and fine-tuning imbalance, which has been largely overlooked in previous work. The causal inference framework provides a principled way to analyze and address these challenges.

### Weaknesses
1. The definition and quantification of "parameter imbalance" lack rigorous theoretical justification. The causal relationship between pre-training data imbalance and parameter imbalance is not thoroughly explained. The selection of semantic factors as confounders needs stronger theoretical support. Specifically, the paper does not provide a clear mathematical definition of parameter imbalance, making it difficult to assess its impact. The connection between the distribution of pre-training data and the resulting parameter distribution is not formalized, and it's unclear how different pre-training datasets with varying imbalances would lead to different parameter imbalances. The choice of semantic factors as confounders is not well-justified; the paper needs to explain why these specific factors are the primary confounders and how they are identified and extracted from the model's parameters.

2. The claim that parameter imbalance has greater impact than data imbalance needs more empirical evidence. The current analysis relies on indirect observations and lacks a controlled experiment where the effects of both imbalances are isolated and compared. It is not clear how the authors disentangle the effects of data imbalance and parameter imbalance in their experiments. A more rigorous analysis is needed to support the claim that parameter imbalance is the dominant factor.

3. Incomplete ablation studies for key components and lack of analysis on computational overhead and efficiency. The paper does not provide a comprehensive ablation study to evaluate the contribution of each component of the proposed method. For example, the impact of the backdoor adjustment method needs to be analyzed in isolation. Furthermore, the paper lacks a detailed analysis of the computational cost of the proposed method, including the time and memory requirements, which is crucial for practical applications.

### Questions
1. How do you quantify parameter imbalance without access to the pre-training data? What metrics are used?

2. Can you provide theoretical justification for why semantic factors should be treated as confounders in the causal framework?

3. What is the computational overhead of the proposed method compared to standard fine-tuning?

4. How does the method perform when the degree of imbalance varies between pre-training and fine-tuning?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In the context of foundation model and PEFT, this paper defines two imbalance terms for long-tailed data, i.e., data-imbalance and parameter imbalance. The paper argues that only considering data imbalance is insufficient for PEFT on foundation models, and proposes an effective strategy to address the problem of parameter imbalance from a causal graph perspective. Numerical experiments have been conducted to support the arguments, and their proposed strategies.

The method's lack of efficiency is analyzed and discussed.

### Strengths
1. [Contribution] The proposed argument is important for the community, which is a generally existing problem while rarely mentioned. The propose of this problem is imperative.
2. [Soundness] The authors conduct a large number of experiments on SOTA models and popular long-tail datasets to demonstrate their arguments.
3. [Presentation] This paper is well organized. The step-by-step exploration of the problem provides an intriguing reading experience.

### Weaknesses
Although the introduced problem is important, the solution is kind of trivial. The simple combination of different models could partially resolve the problem, while each of the foundation models contains a large number of parameters, which is not applicable.

### Questions
1. In Fig. 3, how is the right picture plotted? How is the parameter imbalance computed for each sample?
2. In equation. 7, how is $P(Y=y|bc)$ implemented in your experiments. Do you run each model once and generate a $P(Y=y|bc)$? and how these models are jointly trained (or fine-tuned)?
3. In lines 184-195, it mentioned that "$P_P(Y)$ is inaccessible and we cannot use Eq. (1)". How is $P_P(Y)$  related to Eq. (1) where the symbol is not mentioned.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work considers the bias of foundation models when the data for fine-tuning suffers from class imbalance. They show that parameter imbalance is more dominant than data imbalance. Then, they propose a method based on an assumed causal graph and backdoor adjustment. Experiments show that the proposed method is effective.

### Strengths
- They made a clear observation from empirical results that parameter imbalance is more dominant than data imbalance.

- They show that previous methods such as GLA and re-balancing cannot resolve the parameter imbalance issue.

- The paper is well-written and easy to understand.

### Weaknesses
 - The argument that C is a confounder is confusing. The model will predict Y using the representation B, it is hard to believe there is a direct causal effect of C on Y. I would suggest the authors to show the direct causal effect or confounding bias with experiments.

- The proposed method utilized \textit{backdoor adjustment}, which is also used in some previous work in the literature of long tail classification such as [1]. The authors did not point out the difference.

### Questions
1. In Table 8, it seems that as M increases, performance improves. Do the authors think this trend can persist for larger values of M? Is there any theory or insight that can support this observed trend?

2. In Table 7, why can the proposed method also improve performance in D-Many? I suppose such methods would sacrifice the performance on D-Many for improvements on long tail classes.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper aims to solve the problem of long-tailed learning and illustrates the limitations of rebalancing methods due to biases in foundation models resulting from the imbalance in pre-training data. Based on a causal structure graph and back-door adjustment, the paper proposes a method to mitigate the spurious correlations introduced to the foundation model.

### Strengths
1. The paper identifies the importance of parameter imbalance and thoroughly analyzes the phenomenon with examples. It also highlights the limitations of logic adjustment-based methods in mitigating parameter imbalance.

2. The authors put significant effort into conducting thorough experiments.

### Weaknesses
1. The writing can be greatly improved. For example, the paper mentions Figures 2 and 3 in the introduction without further explaining what they mean. More explanation on figure 2 and 3 in the introduction or detailed caption for figures 2 and 3 would be preferred. Authors also refer to “D-many,” “D-Medium,” and “D-Few” without explicitly explaining what they are. Given the frequency of these terms, I would expect more details on what they means e.g., the definition and data processing etc.

2. Regarding the experimental results,  the improvement of the proposed method looks slightly marginal given that fine-tuning based method can also alleviate the bias. Maybe a side-by-side comparison of the improvement of the proposed method and fine-tuning based method would be beneficial. Moreoever, the results are mostly in tables, visual examples similar to those in Figure 4, that illustrate how the method reduces spurious correlations could be beneficial. To be more precise, what does the heatmap looks like after the application of the proposed method? Has the problem of partial semantic factor been alleviated from the visualization?

### Questions
1. Could you explain a bit more about the concept of partial semantic factor and the causal graph in Section 5.1? What is a data-balanced representation, and could you provide an example of  $C \rightarrow X$?

2. In Section 4.1, the authors claim that although the fine-tuning-based method is able to address parameter imbalance, bias still exists; the results shown in figure 3 for Places365 looks unreasonably bad and could you provide more details on this part of experiments?

### Soundness
2

### Presentation
1

### Contribution
2
