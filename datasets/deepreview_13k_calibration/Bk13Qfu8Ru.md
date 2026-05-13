# Severing Spurious Correlations with Data Pruning

- Decision: Accept
- Avg Score: 7.00
- Scores: 10, 5, 5, 8

## Abstract
Deep neural networks have been shown to learn and rely on spurious correlations present in the data that they are trained on. Reliance on such correlations can cause these networks to malfunction when deployed in the real world, where these correlations may no longer hold. To overcome the formation of such correlations, recent studies propose approaches that yield promising results. These works, however, study settings where the strength of the spurious signal is significantly greater than that of the core, invariant signal, making it easier to detect the presence of spurious features in individual training samples and allow for further processing. In this paper, we identify new settings where the strength of the spurious signal is relatively weaker, making it difficult to detect any spurious information while continuing to have catastrophic consequences. We also learn that spurious correlations are formed primarily due to only a handful of all the samples containing the spurious feature and develop a novel data pruning technique that identifies and prunes small subsets of the training data that contain these samples. Our proposed technique does not require information regarding the sample-wise presence or nature of spurious information, or human intervention. Finally, we show that such data pruning attains state-of-the-art performance on previously studied settings where spurious information is identifiable.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper aims to mitigate the problem of spurious correlations in deep learning models. Through a sequence of simulation experiments, they authors discover that a small subset of training data containing “hard” core features is primarily responsible for the model learning spurious correlations, even when the spurious signal is weak. The authors then demonstrate through subsequent experiments that pruning this subset of samples effectively severs the link between spurious and core features.

### Strengths
This work represents an example of my favorite kind of work. A very important and easy-to-understand problem (spurious correlations learned by models that affect their generalizability) and a very intuitive solution, once the authors explain and demonstrate it. I also felt the work was well written, guided the reader through the gaps in the literature, and step by step demonstrated the veracity of their arguments with simple and compelling experiments.

### Weaknesses
Inductive Solution
There I assume many types of spurious correlations can be learned by a model. For example, it is will documted that outliers can overinfluence functional estimation, and create spurious corrleations. The proposed solution addresses only a specific type of spurious correlation (i.e., roughly speaking, where a certain class has an over-representation of a given feature that its not truly indicative of the class label), which arises under the particular conditions the authors generate (i.e., "the spurious feature takes the form of a line running through the center of the images", "images of men with glasses", etc. ), given the distributional properties of the datasets considered, and given deep learning architectures (e.g., mostly ResNet) considered. Moreover, their solution relies heavily on specific empirical observations about how this particular type of spurious correlation manifests and is distributed, given the particular generation process followed. For instance, the authors observe that in their simulations "in settings where the strength of the spurious signal is not significantly greater than the strength of the invariant signal...samples containing spurious features are uniformly distributed across the training distribution...[and] the presence of spurious features does not have a significant impact on the training distribution...[therefore] samples containing hard core features that also contain the spurious feature are primary contributors to the formation of spurious correlations". They therefore, conclude that "to mitigate spurious correlations, one would only have to prune the hardest samples in the training set, as this subset of the data would contain samples with spurious features that have hard core features.” This reasoning appears to be purely inductive and raises questions about the generalizability of the observations and subsequent solution. Specifically, I'd assume that the observations about the distribution of spurious signals and sample difficulty will hold across other types of spurious correlations, which may behave differently under varying dataset characteristics or model architectures.

Theoretical Justification/Generality
Without a theoretical foundation supporting the general applicability of the inducitve observations, it remains unclear whether the observations that lead to solution are universal and/or if the prunning method can serve as a general approach to mitigating spurious correlations in models. Therefore, the paper could be significantly improve with a theoretical justifications for the generality of the inductive observation. For example, 1) is the particular type of spurious correlation the authors consider representative of all spurious correlations, 2) does the distributional uniformality of samples containing features with spurious correlation across the training samples generalize across types of spurious correlations, 3) is the pruning of this particular type of subset as a solution to (any type of) spurious correlations, and 4) are these justifications architecture/data dependent. 

Related, but unique, I think structuring the pruning solution as a formal model, statistical hypothesis test, etc. would strengthen the theoretical foundation of the proposed pruning technique, and again perhaps shed light on it's generality. A theoretical or statistical clarity on why the samples containing spurious correlation are distributed uniformaly (e.g., I wonder if this is a consequence of the inverse probability transform). A claim that spurious feature reliance experienceing polynomial growth with increasing sample difficulty, would be more trustworthy if supported by some theoretical formulation or model. 

Pruning Consequences
While the authors demonstrate that prunning a particular type of subset of data points will reduce spurious correlations, there is no discussion of what are the consequences. I am inclined to beleive that throwing out data is going to have some sort of negative consequence, and therefore it important to know what trade-off is being made. This will allow a better comparison to other methods that do not simply prune data as well as enable practitioners to understand/determine if the cost of pruning data is worth the benefit in removing spurious correlations.

### Questions
My question(s) would simply be can the authors provide theory, models, statistical justification etc. (or fairly robust/general empirics) to address the listed weaknesses?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper explores how deep neural networks often rely on spurious correlations present in training data, which can lead to performance drop under distributional shifts. The authors highlight a novel setting where spurious signals are weaker, making their identification challenging. They propose a new data pruning technique that selectively removes some training samples that contribute significantly to the formation of spurious correlations. This technique operates without requiring detailed information on the nature or presence of spurious features. The authors demonstrate that their approach achieves state-of-the-art performance on both standard and challenging benchmarks, including scenarios where spurious features are identifiable and unidentifiable.

### Strengths
1) The paper addresses a scenario where the strength of the spurious signal is relatively weaker and thus it is difficult to detect any spurious informationhat spurious signals compared to other works  where the strength of the spurious signal is significantly greater
than that of the core. 
2) The paper provides a thorough experimental design that spans both identifiable and unidentifiable spurious feature scenarios. The use of multiple datasets (e.g., CIFAR-10S, CelebA, Hard ImageNet, Waterbirds, MultiNLI) showcases the method's robustness.
3) The paper is well-organized, detailing the rationale behind the proposed method, experimental setup, and results.

### Weaknesses
1) The paper could explore more thoroughly the practicality of applying the proposed pruning method to large datasets. Specifically,even though the proposed method shows promise for datasets of moderate size, an assessment of its computational cost and efficiency on large and real world data would be beneficial. It would be useful to see a breakdown of the time and memory requirements for the pruning process itself, as well as the subsequent training on the pruned dataset, compared to standard training on the full dataset. This is particularly relevant given that the method relies on iterative sample difficulty estimation, which could become computationally expensive for very large datasets.
2) The approach relies on assessing sample difficulty as a proxy for contribution to spurious correlations. Clarifying the robustness of this metric under different training regimes (e.g., varied architectures or optimization strategies) could strengthen the generalizability of the findings. It is unclear how sensitive the sample difficulty scores are to changes in batch size, learning rate schedules, or the specific initialization of the neural network. A more detailed analysis of these factors is needed to ensure the reliability of the pruning method.
3) Although the paper discusses state-of-the-art methods, further comparative analysis with recently emerging pruning and robust training techniques that do not rely on explicit spurious feature identification would be helpful. Specifically, a comparison with methods that focus on data augmentation, gradient manipulation, or adversarial training could provide a more comprehensive understanding of the strengths and weaknesses of the proposed approach.

### Questions
1) How sensitive is the pruning method to changes in hyperparameters?
2) The robustness of sample difficulty estimation across different model architectures is not clear at the current version of the paper. Would it be possible to add some results or explanations for that?
3) Table 1 shows that some SOTa methods achieve better results. Could you please give some explanation on that? Also, 
4) could you please open source the code to enhance the reproducibility?
Suggestions for Improvement:
1) It would be helpful to include a section that discusses the potential negative impacts or limitations of the method, such as the risk of pruning samples that are informative but rare.
2)Extending the empirical analysis to more complex and real-world datasets with non-synthetic spurious correlations could further validate the applicability of the method.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper study the spurious feature associated with the trained model, focusing on how this correlation is formed during the training process and proposing a data pruning approach to mitigate spurious correlation. Specifically, the authors find that spurious correlation is caused by a few samples that are hard to learn and contains spurious features. As a result, this paper proposes to remove those data points from the training dataset to improve model performance.

### Strengths
1. The paper organization is clear and easy to follow.
2. The problem of identifying and mitigating spurious correlation is critial.
3. This paper considers a challenging scenario where spurious features have weak signals and therefore are difficult to be detected.

### Weaknesses
 **Major Concerns:**

1. Lack of rigorous formulation and solution. Throughout this paper, there is no single equation or definition that clearly states the problem and the proposed solution. Key concepts that heavily mentioned in the paper, such as spurious correlation, core/invariant features, simple/hard features, are not well-defined. For a more readable paper, the authors are encouraged to (1) state a self-contained problem with properly defined concepts (2) write a pesudocode for the proposed data pruning algorithm (3) disclose complete experimental details including but not limited to training/test dataset processing procedure, models, calculation of evaluation metric (which is not well-defined as well), and baseline methods.

2. Lack of clarity in findings. Most figures and tables are not self-explained and neither explained by their titles. As a result, it is confusing how do they support the claims in the main text. This problem is aggravated due to the previous point. For example, I did not understand the message in Figure 2, as concepts like "easy/hard" are undefined, and authors do not explain how they perform the experiments, e.g., how to add spurious features into the training data and how to calculate the misclassification rates. The authors should review all their findings and claims and rewrite their evidence to be more supportive and convincing.

### Questions
Please find in the weakness section above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper empirically investigates the phenomenon of spurious correlations being learned by deep learning models.

The authors are mainly interested in the setting where the spurious signals are "weak", in the sense that are not easy to be detected and removed.

In this setting, the authors propose a data pruning approach to limit the effects of the spurious correlations.

The method consists in looking at the (few) training points that are more difficult to classify during training. These points are most likely making the model overfit patterns that are not necessarily causal to the right label, and are therefore a major cause to the learning of spurious patterns. This is confirmed experimentally.

### Strengths
The paper is very well written, it is clear, the approach followed by the authors is logically sound, and I personally enjoyed reading it. While I am not certain that it is true that all previous work adresses cases where the spurious signal is stronger than the core features, the contribution seems indeed novel, and the results are reasonable and well explained.

The paper is on point. It proposes mainly one single method, and the writing is structured in a way that the reader can digest the phenomenology before being given the final algorithm / approach.

### Weaknesses
It is sometimes not obvious what the authors mean by "strong" or "weak". While providing precise definitions is beyond the purposes of this work, some examples during the introduction could facilitate the reading. For example, I was confused in the paragraph at line 201, where the strength of the signal is defined both in terms of the geometry of the pattern and it's frequency in the data. These two aspects are fundamentally different, and putting them altogether might not result in the best model to investigate this problem...

The reason behing I do not give a higher schore is that some of the results are not entirely surprising. The phenomenlogy described by Figure 2 is interesting, but at the same time - to my understanding - in line with what we expect from the influence of individual samples to the final parameters of the model (see, e.g., [1, 2]). Nevertheless, this might be a new perspective in the community of spurious features / correlations, and I therefore recommend acceptance.

There should be a typo in line 162 "as shown in..."

I am still confused about the setting used to obtain Figure 3. And what do the authors mean by "polynomial growth" in this case? What does it mean to "scale up the difficulty of the core features of the 100 saples"?

I am also confused by Section 6.3 - What do the authors mean by "group labels" in line 457? Can the authors provide a brief and self contained description of the point that wants to be raised in this section (while I believe this is not the central part of the work)?

### Questions
There should be a typo in line 162 "as shown in..."

I am still confused about the setting used to obtain Figure 3. And what do the authors mean by "polynomial growth" in this case? What does it mean to "scale up the difficulty of the core features of the 100 saples"?

I am also confused by Section 6.3 - What do the authors mean by "group labels" in line 457? Can the authors provide a brief and self contained description of the point that wants to be raised in this section (while I believe this is not the central part of the work)?

### Soundness
3

### Presentation
4

### Contribution
3
