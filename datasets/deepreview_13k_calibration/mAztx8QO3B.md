# Coreset Selection via Reducible Loss in Continual Learning

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 5

## Abstract
A natural solution for rehearsal-based continual learning is to select a coreset as memory. A coreset serves as an informative summary of a large dataset, enabling a model trained solely on the coreset to achieve performance comparable to training on the full dataset. Previous bi-level coreset selection methods adjust sample weights or probabilities to minimize the outer loss, which is computed over the entire dataset. For non-representative samples like ambiguous or noisy samples, since these samples are not well learned even training model on the full dataset, loss of these samples in the outer loss are not worthy to be reduced. However, their high loss values may cause them to be selected in an attempt to minimize the outer loss, which may lead to suboptimal performance for models trained on the coreset. To address this issue, we first investigate how the performance of a trained model changes when a sample is added to the training dataset and approximate this performance gain using reducible loss. We then select samples with the highest performance gain in the coreset so that performance of model trained on coreset could be maximized. We show that samples with high performance gain are informative and representative. Furthermore, reducible loss requires only forward computation, making it significantly more efficient than previous methods. To better apply coreset selection in continual learning, we extend our method to address key challenges such as task interference, streaming data, and knowledge distillation. Experiments on data summarization and continual learning demonstrate the effectiveness and efficiency of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The work presents a concise way of preventing select noisy data into the coreset due to their high loss value. By using a holdout model as the baseline, it incrementally selects samples with high log prob loss. Which is mathematically shown by the authors that such samples are informative but not well represented yet in the coreset. The work shows improvements on various common continual learning datasets.

### Strengths
1. A detailed, structured, and rigorous paper with extensive derivations and experiments.
2. Conducts a variety of experiments, including those on standard continual learning datasets, more challenging ImageNet variants, training overhead, and extensive ablation studies.
3. Presents a clear and straightforward idea for selecting good samples to add to the coreset, supported by sound equations.

### Weaknesses
1. Not easy to understand at the first glance. It might be better to add some teaser figure.

2. The reliance on a holdout model, particularly its potential for poor performance on significantly different incoming tasks, raises concerns. If the holdout model, trained on initial data, struggles to provide meaningful loss values for later tasks due to a large domain shift, the core sample selection process could become ineffective. This could lead to the selection of uninformative samples or even the exclusion of crucial ones, hindering the overall performance of the continual learning system. The paper should address the potential limitations of the holdout model in such scenarios.

3. The distinction between equation 4 and equation 7, and the difference between \(\mathcal{S}\) and \(\mathcal{M}\) could be made clearer. While the equations themselves are similar, their application in different contexts (coreset selection vs. continual learning) needs more explicit explanation. The notation, while mathematically sound, could be more intuitively explained to enhance understanding.

### Questions
1. How do you train the holdout model? I believe it is trained only on the initial dataset, without any information about the incoming task. What if the holdout model is not good enough to calculate a meaningful loss for later tasks? For example, if the incoming task is very different from the previous one (a huge domain shift), the loss of holdout model might be poor for every input. In such a scenario, CSRL might not work.
2. What's the difference between eq.4 and eq.7? What's the difference between $\mathcal{S}$ and $\mathcal{M}$?

### Soundness
4

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
5

### Summary
This paper introduces a method for coreset selection using reducible loss to improve continual learning (CL) performance. Traditional experience replay-based CL methods face challenges when selecting representative samples from non-stationary data streams, often retaining ambiguous or noisy data that can degrade model performance. The proposed method uses reducible loss as a selection criterion, estimating each sample's performance gain to determine its representativeness and informativeness. This selection framework is computationally efficient, requiring only a forward computation without gradient backpropagation, thus avoiding the computational cost associated with implicit gradient methods. Additionally, the approach is extended to handle challenges in CL, including task interference and data streaming, demonstrating robustness against noisy data and effective scalability for large datasets like ImageNet. Experimental results show that this method consistently improves CL model accuracy and reduces forgetting when applied to various datasets.

### Strengths
This paper introduces a coreset selection method based on reducible loss for continual learning, aiming to improve model performance by selecting representative samples efficiently. By focusing on performance gain, this approach reduces computational demands and mitigates the impact of noisy data. It addresses key continual learning challenges, such as task interference and data streaming, making it particularly valuable for dynamic and large-scale applications.

### Weaknesses
The coreset selection method based on reducible loss presented in this paper shows promise for continual learning applications, but some of the design choices lack thorough validation, and certain aspects of the experimental comparisons and theoretical evidence could be more comprehensive.

Many coreset selection works in continual learning are not based on bi-level selection. Why does this work focus on bi-level optimization, what are the advantages?

The comparison experiment should involve some SOTAs which are not based on bi-level selection.

The tsne experiment cannot explain why the selected samples are representative and informative. And the tsne should be conducted on some works without bi-level selection strategy. If the visualization only shows the aggregation of the selected samples, then why not use a prototype-based method that selects samples near the class prototypes.

Some coreset selection methods such as [1,2,3] are all without bi-level strategy, are they also just heuristic? Also, they are SOTAs of coreset selection methods, maybe more comparison experiments are supposed to be conducted with them.

You claim that “samples with high performance gain are both representative and informative” in the abstruct, why works like [4,5] can not be considered as comparisons? They also make sample selections or updates based on the performance gain.

### Questions
1.	This paper builds upon the limitations identified in Greedy Coreset (NIPS 2020). However, given that four years have passed since its publication, does this work lack timeliness? Can its performance surpass current state-of-the-art methods?
2.	This paper uses a coreset-based replay method, so it should include more comparative experiments with other coreset selection approaches. The comparative experiments in this paper are insufficient.
3.	Since the paper mentions that reducible loss eliminates the need for backpropagation and reduces computational cost compared to traditional bi-level coreset selection strategies, an additional experiment should be included to validate this conclusion.
4.	Does training a holdout model using all the data contradict the continual learning (CL) setting?
5.	The paper mentions that “samples with high performance gain are both representative and informative.” Could the distribution of high-performance samples in feature space be provided as evidence for this claim?

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
5

### Summary
The authors focus on the coreset selection method used in continual learning scenario. They believe that the not well learned samples, like ambiguous and noise samples should not be included in the coreset. Therefore, a new method CSRL is designed with reducible loss to filter the not-well-learned samples during coreset selection. The experiments are conducted on MNIST, CIFAR-10, and CIFAR-100 with several earlier competitor methods.

### Strengths
1. I find the authors make great efforts in polishing this work. I found multiple supplementary explanations for the main text in the supplementary materials, which I believe is commendable and should be encouraged. 
2. The paper is well-organized and writing is almost clear.

### Weaknesses
About Method:

1. The proposed CSRL seems to be severely affected by the selection order and subset division way. If Algorithm 1 is correctly implemented, this means that the selected samples in the coreset will not be considered in the following selection process. Obviously, the gain score G of samples stored in the coreset will change as the model gradually learns from all subsets. The authors ignore this possibility, which may lead to the result that previously selected candidates are more likely to be stored in the coreset. In other words, the gain score may not be fair for all candidates.

2. The gain score G seems only to assess which samples are easier to learn fully, rather than which are more core. From the expressions in Equations (4) to (6), it is evident that the authors do not differentiate between difficult samples and noise when applying this gain score, instead treating both as noise. Clearly, difficult samples should also be treated appropriately during coreset selection.

3. I notice that the authors provide the results in Appendix H. However, I believe these results do not verify that CSRL is more reasonable and may even exacerbate the concerns I raised in W1. Since the overall difficulty level of the entire dataset is not provided, we cannot determine whether CSRL regulates the coreset selection more effectively. As I expressed in W1, the results can also be interpreted to mean that CSRL is severely affected by the selection order (which seems to be random) during application, leading to selection results that might also be random as the size of the coreset increases. This suggests that CSRL has less impact on regulating coreset selection. In contrast, the other competing method appears to perform better. Additionally, the authors claim that selecting fewer hard-to-learn samples will make a difference, which further confirms that hard samples are considered the same as noise samples.


About Experiments:

4. I noticed that the settings used by the authors are somewhat outdated. First, the largest network structure in this paper is only ResNet-18, and the authors further provide training and selecting time results based on this backbone to show the efficiency of their method. From both the performance and efficiency perspectives, I find this unconvincing. With such simple network structures, it is difficult to compare performance differences between new and old methods. Let alone that many recent state-of-the-art methods are not included in the main experimental results.

5. In terms of the experimental results, I find them unconvincing because the authors only adopt competitor methods from 3 and 5 years ago in all the experimental results presented in the main text. It becomes even more puzzling when I notice that the authors are aware of the latest state-of-the-art methods (e.g., BCSR, GCR) but only compare CSRL with them on one of the datasets used in BCSR in the appendix. Why are the latest state-of-the-art methods not compared under the same settings in this paper's main text? I believe that both the absence of state-of-the-art methods in the main text and the partial comparison results of these methods shown only in the appendix do not support the authors' claim that the proposed CSRL is state-of-the-art.

### Questions
Please see my questions in Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
