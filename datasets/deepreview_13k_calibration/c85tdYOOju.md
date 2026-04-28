# Decoupling Weighing and Selecting for Integrating Multiple Graph Pre-training Tasks

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 6, 5

## Abstract
\vspace{-1em}
Recent years have witnessed the great success of graph pre-training for graph representation learning. With hundreds of graph pre-training tasks proposed, integrating knowledge acquired from multiple pre-training tasks has become a popular research topic. In this paper, we identify two important collaborative processes for this topic: (1) \emph{select}: how to select an optimal task combination from a given task pool based on their compatibility, and (2) \emph{weigh}: how to weigh the selected tasks based on their importance. While there currently has been a lot of work focused on weighing, comparatively little effort has been devoted to selecting. This paper proposes a novel instance-level framework for integrating multiple graph pre-training tasks,
\textit{\underline{W}eigh \underline{A}nd \underline{S}elect} (WAS), where the two collaborative processes, \emph{weighing} and \emph{selecting}, are combined by decoupled siamese networks. Specifically, it first adaptively learns an optimal combination of tasks for each instance from a given task pool, based on which a customized instance-level task weighing strategy is learned. Extensive experiments on 16 graph datasets across node-level and graph-level downstream tasks have demonstrated that by combining a few simple but classical tasks, WAS can achieve comparable performance to other leading counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Since the roles of pre-training tasks vary with downstream tasks and different pre-training tasks may not be compatible, the authors point out that selecting and weighting tasks are key parts of the pre-training. Moreover, the existing methods that select tasks based on learned weights would confuse the roles of selection and weighting. To address these limitations, they propose WAS to decouple these two processes.

### Strengths
1. The proposed WAS decouples the selecting and weighting to avoid performance reduction caused by task conflicts. They calculate weights based on output distributions instead of losses to address the non-comparability between different loss functions.
2. The proposed method can automatically select the number and type of suitable pre-training tasks for different downstream instances.
3. The authors conduct extensive comparison experiments, and the proposed WAS performs better on both node-level and graph-level tasks. In addition, they visualized the evolution processes of selecting tasks and updating weights, which proves the decoupling of selection and importance weighting.

### Weaknesses
1. The authors should add more ablation experiments to demonstrate the effectiveness of the proposed model, such as the role of different updating methods in decoupling the selecting and weighting outputs, and the role of reweighting after selection. Specifically, it would be beneficial to see experiments that isolate the impact of momentum-based updates for selection versus gradient-based updates, and how this choice affects the decoupling of the selection and weighting mechanisms. Furthermore, the necessity of the reweighting step after selection should be more thoroughly investigated, perhaps by comparing performance with and without this step under various conditions, such as different numbers of selected tasks or varying weight distributions.
2. The comparison model in A5 needs more description to distinguish it from A1, such as whether Random-Select and ALL use learned weights. It is unclear whether the Random-Select method utilizes learned weights but randomly chooses the tasks, and whether the ALL method uses all tasks with their learned weights. A clearer description of how these methods utilize the learned weights is needed to fully understand the experimental results.

### Questions
Please refer to Weaknesses.

### Soundness
3 good

### Presentation
4 excellent

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
In recent times, graph pre-training for graph representation learning has gained prominence, with numerous pre-training tasks emerging. Integrating knowledge from various pre-training tasks is now a focal research area. Two critical collaborative processes for integration are: (1) selecting the best task combination considering their compatibility and (2) determining the importance of the chosen tasks. While much research has been on weighing tasks, selection has received lesser attention. This paper introduces a new instance-level framework named Weigh And Select (WAS) that merges both processes using decoupled Siamese networks. WAS adaptively determines the best task combination for individual instances, leading to a tailored instance-level task weighing strategy. Experiments across 16 graph datasets reveal WAS's efficacy, producing results comparable to top-performing methods by merging several basic tasks.

### Strengths
S1. The authors of the paper have done a good job in providing a compelling motivation for their research. Their thorough analysis of different pre-training tasks combined with a detailed examination of several datasets showcases their comprehensive approach. Furthermore, their assessment of task importance and compatibility provides valuable insights, shedding light on the central issue at hand.

S2. In terms of addressing the research concerns, the authors have carefully identified and highlighted them. These concerns have been formulated into four well-defined research questions that give readers a clear roadmap of the study's objectives. On a broader note, the manuscript is well-organized, with a structured flow that facilitates easy comprehension, making the writing lucid and clear to the audience.

S3. With respect to the empirical aspect of the study, the authors have presented an exhaustive set of experimental results. These results showcase outcomes that are indeed promising.

### Weaknesses
W1. The concept of instance is not well defined. Different pre-training tasks may have different definitions of instances fundamentally (eg. at a node-level, subgraph/graph-level, edge-level etc). Having a common and converged definition may not work well. Furthermore, downstream task could also have different definitions of instances.

W2. While 4 questions are clear in the identification of the 4 steps/issues to address, the solutions are quite standard. E.g. using Gumbel-Softmax sampling for Bernoulli distribution,  the weighting scheme and the Siamese network architecture are all well known tools.

W3. The compatibility issue, or interferences among tasks have been observed in previous work in other areas or problem settings [a,b,c]. Some discussion on this aspect, and its particular challenges in graph context, would further strengthen the motivation of the paper.

### Questions
Please see weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors have studied how to effectively integrate multiple graph pre-training tasks. They have identified two important collaborative processes, i.e., selecting and weighing.  They propose a new instance-level framework for integrating multiple graph pre-training tasks, named WAS (Weigh And Select), where the weighing and selecting processes are combined by decoupled siamese networks. Extensive experiments on 16 graph datasets have been performed to demonstrate the effectiveness of the proposed method.

### Strengths
1. In this paper, the authors introduce a new framework, namely WAS, for task selecting and importance weighing to integrate multiple graph pre-training tasks.

2. The authors show the limitations of existing weighing-only schemes and demonstrate the importance of task selecting process.

3. The authors have performed extensive experiments to demonstrate the effectiveness of the proposed method. 

4. This paper is clearly written and easy to follow.

### Weaknesses
1. In Table 1, 2, and 3, the authors do not compare the proposed WAS framework with existing frameworks that only focus on weighing (i.e., AutoSSL, ParetoGNN, AUX-TS, and AGSSL). However, in Table 4, WAS is compared with these methods. This makes the experimental settings not consistent.

2. The complexity of the proposed has not been studied. Although the proposed method can achieve some performance improvement, it may take more training/inference time, due to combining multiple pre-training tasks. The authors need to have some analysis about the complexity of the proposed method.

3. The authors also need to perform experiments to analyse how many tasks are selected for each instance on average.

### Questions
1. On average, how many tasks are usually selected for each instance?

2. From Figure 6(d), we can observe that the following 4 tasks have the largest weights, i.e, EP, AM, IG, and CP. How about we only use these 4 tasks and learning the their weights for prediction?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focus on multi-tasking graph pre-training and proposes a weighting and selecting network to model the compatibility and importance of tasks. The proposed WAS consists of knowledge extraction and transfer step, and it is powered by the decoupled siamese networks to assign weights to each teacher and do selection. Experiments are conducted on different benchmark datasets to showcase its effectiveness.

### Strengths
1. The paper is well-written and easy to follow.

2. The evaluation is conducted on both graph-level and instance-level tasks.

3. The idea on solving the compatibility issue of multiple tasks is new and insightful.

### Weaknesses
1. The motivation of focusing on graph-structured data is unclear.

2. Compared to the baseline methods for multi-task learning on instance-level, the improvement from WAS is marginal. On the largest graphs in the experiment (ogbn-arxiv), it achieves worse performance compared to baseline method.

3. Besides the empirical results, the theoretical analysis is still needed to answer why both selecting and weighing is needed,  and why there is compatibility issue (i.e., why some tasks shouldn't be selected).

### Questions
1. The proposed method does not treat graph-structured data specially, nor is it tailored for graph modeling. Why is it positioned for pre-training on graphs, instead of for general pre-training?

2. Any in-depth understanding of the relationship for the selected tasks? Are they independent?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
