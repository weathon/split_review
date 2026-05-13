# Towards Meta-Pruning via Optimal Transport

- Decision: Accept
- Scores: 6, 8, 6, 8, 8

## Abstract
Structural pruning of neural networks conventionally relies on identifying and discarding less important neurons, a practice often resulting in significant accuracy loss that necessitates subsequent fine-tuning efforts. This paper introduces a novel approach named Intra-Fusion, challenging this prevailing pruning paradigm.
Unlike existing methods that focus on designing meaningful neuron importance metrics, Intra-Fusion redefines the overlying pruning procedure.
Through utilizing the concepts of model fusion and Optimal Transport, we leverage an agnostically given importance metric to arrive at a more effective sparse model representation.
Notably, our approach achieves substantial accuracy recovery without the need for resource-intensive fine-tuning, making it an efficient and promising tool for neural network compression.
Additionally, we explore how fusion can be added to the pruning process to significantly decrease the training time while maintaining competitive performance. We benchmark our results for various networks on commonly used datasets such as CIFAR-10, CIFAR-100, and ImageNet. More broadly, we hope that the proposed Intra-Fusion approach invigorates exploration into a fresh alternative to the predominant compression approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper focuses on the integration of pruning and fusion techniques in model compression. The authors introduce a novel approach called Intra-Fusion, which leverages Optimal Transport to inform the model compression process. Intra-Fusion aims to preserve the output of the original non-pruned model and recover accuracy without the need for fine-tuning or data. The paper also explores the application of fusion in factorizing and speeding up the training process of models that are pruned after training. Experimental results show that Intra-Fusion achieves consistent gains in test accuracy compared to conventional pruning methods.

### Strengths
1. Improved accuracy: The article demonstrates that Intra-Fusion can significantly enhance the accuracy of pruned models without relying on any additional data. By merging similar neurons, Intra-Fusion better preserves the output of the original non-pruned model, leading to superior performance.

2. Data-free pruning: Pruning neural networks usually results in immediate drops in accuracy, requiring extensive fine-tuning. However, the article argues that with Intra-Fusion, a significant amount of accuracy can be recovered without the need for any data points. This approach provides a more efficient and practical solution for model compression.

3. Factorizing model training: The article explores how fusion can be used to factorize and speed up the training process of models that are supposed to be pruned after training. By splitting the training dataset into subsets and training models concurrently, significant training time speedups can be achieved. This approach provides an alternative or enhancement to data parallelism during distributed model training.

### Weaknesses
1. This article has severe writing issues:
> + In the second paragraph of section 3.1, Figure 6 appears multiple times. I believe it should be Figure 1.
> + In Algorithm 1, $ neuron\ j \in layer \land i[j] \ge t$ represents a logical "AND" relationship, not a neuron.
> + The text contains many long and heavily clause-laden sentences, which pose a significant obstacle to understanding the article. I suggest avoiding such expressions as much as possible in academic papers, for example, in the sentence on the third line of Section 6.
> + The text description of Figure 7 has been truncated.

### Questions
1. What does "meta" manifest in?
2. In the fourth paragraph of the "Meta-Pruning Comparison" part in Section 3.1, it mentions "layer's cardinality." However, in the "Structured Pruning: Group-by-Group" part, it states, "The number of neuron pairings in a group we term 'group cardinality'." So, is 'cardinality' defined in the context of layers or groups?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a new model compression technique, IntraFusion, by combining pruning and merging (or fusion). The fusion part is based on Optimal Transport (OT). The main idea is to combine multiple independently trained neural networks. Empirical results suggest that IntraFusion performs better than the default pruning scheme, especially in the no finetuning ("data-free pruning") setting.

### Strengths
1. Most network pruning methods still rely on an excessive retraining process. This paper proposes a method to save the retraining, which potentially is of broad interest.

2. The proposed method uses OT to merge networks for model compression, unlike most of the conventional ways, which sounds novel to me.

3. The empirical results suggest the method is more effective than the default pruning scheme, especially without finetuning.

### Weaknesses
1. My biggest concern is about the empirical results.

1.1 Currently, it only compares with the default pruning for the main benchmark results (Tab. 1, Fig. 3 and 4). This looks quite limited to me. How is the method compared to other recent top-performing structured pruning methods like [*1 - *3]? It is highly advisable to add a set of comparisons with ResNet50 on ImageNet (as far as I know, this is the standard benchmark setup in a typical pruning paper). Specifically, the lack of comparison against methods that explicitly optimize for structured sparsity, such as those using group lasso or similar regularization techniques, makes it difficult to assess the true effectiveness of IntraFusion. The current comparisons only show an advantage over a basic pruning approach, not against state-of-the-art techniques.

1.2 Based on Tab. 1, after finetuning, the advantage of the proposed method seems quite marginal (the authors also agree that "*the gains might not seem as stark*"). Although the authors argue that "the focus of this paper is on data-free pruning", I do not think this is strong enough to justify the weak improvement, since  "data-free pruning" is barely practical at present. This means, when used in practice, the proposed method actually will not see much advantage against the default pruning scheme. The practical utility of a method that only shows a marginal improvement after fine-tuning, even if it excels in a data-free setting, is questionable. The paper needs to demonstrate a more substantial advantage in a practical scenario where fine-tuning is feasible.

2. Some minor issues:
* "Pruning techniques (LeCun et al., 1989) can broadly be classified into structured (Wang et al., 2019; Frantar & Alistarh, 2023)," -- The paper (Frantar & Alistarh, 2023) seems not to be structured pruning paper. It is unstructured.

### Questions
What is the training cost of the method compared to the default pruning scheme?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces 'Intra-Fusion', a novel approach that combines the concepts of pruning and fusion for compressing over-parameterized neural networks. While pruning is a well-established method for reducing the size of neural networks, fusion, which involves merging independently trained networks, has recently gained traction. The authors propose a method that leverages pruning criteria to inform the fusion process. This approach, irrespective of the specific neuron-importance metric used, can prune a significant number of parameters while maintaining accuracy levels comparable to standard pruning methods. Furthermore, the paper explores how fusion can enhance the pruning process, reducing training time without compromising performance. The results are benchmarked on popular datasets like CIFAR10, CIFAR100, and ImageNet.

### Strengths
1. The paper is well-organized and clearly written, which is easy to follow.
2. The problem studied in this paper is interesting and valuable.
3. The experimental verification is quite sufficient.

### Weaknesses
1. This paper presents extensive experiments across various settings. However, there are areas that could benefit from further exploration: It would be valuable to see comparative results with methods like the LOTTERY TICKET HYPOTHESIS [A]. How does the proposed approach stack up against such established techniques?
2. The FaP approach introduced in this paper seems to assume that the two models being fused have identical structures. It raises the question of how adaptable this method is. Can it handle fusions of models with different depths or even heterogeneous models, such as combining a CNN with a ViT[B]?

### Questions
Please see the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
I find this paper to be intriguing and appreciate its unique approach, diverging from traditional methods by employing optimal transport. The performance of this method appears promising, and I commend the authors for their work. I am inclined to give this paper a high rating and would recommend its acceptance.

### Strengths
I would like to express my sincere appreciation for the data-free setup presented in this paper; it is an aspect that I find to be incredibly valuable. The capability of the proposed method to effectively operate within a data-free setup is both intriguing and commendable.



I am genuinely intrigued by the concept of split-data training introduced in the paper. Its novelty, practicality, and engaging nature hold great potential to inspire and contribute significantly to the broader community.


The proposed method skillfully utilizes a modified version of OTFusion to integrate the discarded neurons into the "surviving" ones, a strategy I find to be quite thoughtful and well-reasoned.


A significant portion of the research in structured pruning has concentrated on creating more significant importance measures, denoted as i, while the overarching procedure outlined in Algorithm 1 has largely stayed consistent. Drawing inspiration from OTFusion, this paper endeavors to explore an innovative approach to the conventional pruning method. Rather than merely eliminating the less crucial pairings within a group, the authors thoughtfully utilize the calculated importance metrics to guide the fusion of these pairings, ultimately resulting in a reduced group cardinality. This nuanced method demonstrates a commendable attempt to enhance the efficiency of structured pruning.

The results showcased by the proposed method, particularly within the data-free setup, are indeed promising and show great potential. This outcome is both encouraging and exciting, and it highlights the method's effectiveness in challenging scenarios.


The results presented in Figure 6 appear to be promising and demonstrate the potential effectiveness of the approach being discussed.

### Weaknesses
I kindly draw your attention to pages 3 and 4, where multiple references to “Figure 6” appear. It is possible that these may be typographical errors, and you might be intending to refer to “Figure 1” instead.

It would be beneficial if the authors could extend their comparisons in the main text to include a wider range of prior works, in addition to the baseline they have already examined. This would provide a more comprehensive understanding of how the proposed method stands in relation to existing literature, and it would undoubtedly enrich the paper's overall context and value.

### Questions
See #Weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new intra-fusion approach, which tries to unify and bridge the paradigms of pruning and fusion. The proposed approach shows considerable gains with or without fine-tuning.

### Strengths
* The idea of unifying pruning and fusion into a principled approach is very interesting, and makes a lot of sense. 
* The argument that we should not just keep the most important nodes while discarding the others, but can actually restore information from all neurons to create more accurate compressed networks is novel. 
* The evaluation is comprehensive and interesting, while the analysis (Sec 5) demonstrates many interesting findings. 
* The discussion on applications beyond pruning, i.e., factorizing model training seems to be viable.

### Weaknesses
 * It is not clear to me why uniform distribution for both source and target is generally the most robust choice? (Sec 3.2.3)
* Is that possible to use existing pruning-at-initialization metrics, such as SynFlow or ZiCo, with the proposed Intra-Fusion?
* In the split-data approach, it is mentioned that if we train two individual models, the speed-up would (in theory) be 2x. Can you demonstrate this with some experimental results in practice?

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
