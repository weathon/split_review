# Trained Models Tell Us How to Make Them Robust to Spurious Correlation without Group Annotation

- Decision: Reject
- Scores: 5, 6, 5, 8

## Abstract
Classifiers trained with Empirical Risk Minimization (ERM) tend to rely on attributes that have high spurious correlation with the target. This can degrade the performance on underrepresented (or \textit{minority}) groups that lack these attributes, posing significant challenges for both out-of-distribution generalization and fairness objectives. Many studies aim to enhance robustness to spurious correlation, but they sometimes depend on group annotations for training. Additionally, a common limitation in previous research is the reliance on group-annotated validation datasets for model selection. This constrains their applicability in situations where the nature of the spurious correlation is not known, or when group labels for certain spurious attributes are not available. To enhance model robustness with minimal group annotation assumptions, we propose Environment-based Validation and Loss-based Sampling (EVaLS). It uses the losses from an ERM-trained model to construct a balanced dataset of high-loss and low-loss samples, mitigating group imbalance in data. This significantly enhances robustness to group shifts when equipped with a simple post-training last layer retraining. By using environment inference methods to create diverse environments with correlation shifts, EVaLS can potentially eliminate the need for group annotation in validation data. In this context, the worst environment accuracy acts as a reliable surrogate throughout the retraining process for tuning hyperparameters and finding a model that performs well across diverse group shifts. EVaLS effectively achieves group robustness, showing that group annotation is not necessary even for validation. It is a fast, straightforward, and effective approach that reaches near-optimal worst group accuracy without needing group annotations, marking a new chapter in the robustness of trained models against spurious correlation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper EVaLS, a method to improve model robustness against spurious correlations without requiring group annotations. EVaLS balances high- and low-loss samples from an ERM-trained model and applies a simple last-layer retraining (on a loss-based sampled dataset), thus enhancing group robustness. The approach also uses worst environment accuracy to for model selection. Experimental results on diverse dataset shows competitive performance to baseline methods.

### Strengths
1. The proposed approach EValS, using environment inference and Loss-based sampling, is novel and interesting. 
2. EValS has competitive performance with other methods across diverse datasets.

### Weaknesses
1. The assumption that "minority samples are more prevalent among high-loss samples, while majority samples dominate the low-loss category" is questionable. It is easy to construct distributions that does not satisfy this assumption. Specifically, if the spurious attribute is only weakly correlated with the target, or if the model learns a representation that is not strongly influenced by the spurious attribute, then the loss distribution may not clearly separate minority and majority groups. For example, consider a scenario where the spurious correlation is only present in a small subset of the majority group; in this case, the high-loss samples might be a mix of both majority and minority groups, thus invalidating the core assumption of the method.
2. The performance of EValS seems to rely on the EIIL to find the correct environment. However, how to find the environments may be a challenging problem itself. The method's reliance on a specific environment inference technique raises concerns about its generalizability and robustness. If the environment inference fails to capture meaningful variations, the subsequent loss-based sampling and retraining steps may not lead to improved robustness. Furthermore, the computational cost of environment inference also needs to be considered.
3. The peformance of EValS does not seem consistently better than other baseline methods across all datasets. It is not clear whether the better performance in specific dataset is by chance. The lack of consistent improvement across all datasets raises questions about the method's reliability and applicability in diverse scenarios. The performance variations might be due to dataset-specific characteristics or hyperparameter tuning, and it is not clear if the method is robust to these variations.

### Questions
See weakness above.

### Soundness
2

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
4

### Summary
Many studies that enhance robustness to spurious correlation require group annotations for training. This paper aims to enhance the robustness with minimal group annotation assumptions. Specifically, the losses from an ERM-trained model are used to construct a balanced dataset of high-loss and low-loss samples, mitigating group imbalance in data. Moreover, using environment inference methods to create diverse environments has been shown to potentially eliminate the need for group annotation in model selection. Experiments demonstrate the effectiveness of the proposed method.

### Strengths
- The paper is well-written and easy to follow.

- The paper proposes a practical method to mitigate the reliance on spurious correlations without any group annotations. 

- A new dataset is constructed that demonstrates the effectiveness of the proposed method in mitigating unknown shortcuts.

### Weaknesses
 - The proposed method is incremental and has limited technical contributions. Retraining the last-layer using group-balanced validation data to mitigate the reliance on spurious correlations has been used in [1,2]. Inferring environment is a direct follow-up of [3].

- The theoretical analysis does not really explain why loss-based sampling within a class can be used to create a group-balanced dataset. The analysis assumes that the losses on the majority and minority samples follow Gaussian distributions. Under this assumption, it is obvious that the loss-based sampling could create two group-balanced sets of data. However, whether this assumption holds in practice is questionable. Moreover, a previous study [2] has found that that model disagreement may effectively upsample worst-group data, or in other words, may create a more group-balanced dataset. Thus, the loss-based sampling may not be as effective as proved in the paper.

- The comparison in Table 1 isn't fair for some methods. EVaLS uses new data, i.e., a part of validation data, for retraining, while methods including GDRO + EIIL, JTT, and ERM do not have access to the new data. Moreover, the existing work [4] also propose a method that aims to mitigate spurious correlations without group annotations. It would be beneficial to compare with this method under the same setting. 

- There are some model selection methods that do not require group annotations, such as minimum class difference [4] and worst-class accuracy [5]. It would be helpful to analyze the effectiveness of the proposed worst environment accuracy in comparison with these techniques.

### Questions
- See the weaknesses.
- In Table 1, why the experiments on the CivilComments and MultiNLI datasets are out of the scope of the method?
- In L189, the authors mention that they randomly divide the validation set into $\mathcal{D}^{LL}$ and $\mathcal{D}^{MS}$. What if the random division results in a poor set of $\mathcal{D}^{MS}$ which does not have sufficient samples to represent a minority group of samples?

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
3

### Summary
This paper introduces a method called EVaLS, which trains a classifier that is robust to spurious correlations without requiring group labels. The method constructs a balanced dataset based on loss values and utilizes environments for hyperparameter tuning. Experiments on several datasets demonstrate the effectiveness of the proposed method.

### Strengths
The method of selecting high-loss and low-loss data proposed in this paper effectively mitigated the problem of group imbalance, with both experiments and theoretical analysis effectively validating this point.

### Weaknesses
 - The authors may need to provide a more detailed description of the advantages of loss-based sampling over other sampling methods. For instance, it would be beneficial to compare it specifically with methods like SELF, highlighting the unique benefits or efficiencies achieved by the proposed method. The current comparison lacks a detailed analysis of the specific mechanisms that make loss-based sampling superior, particularly in scenarios with varying degrees of class imbalance and spurious correlations.

- The authors' claim that their method 'completely eliminates the need for group annotations' as a primary contribution seems somewhat tenuous. The methodology presented in the paper can be categorized into two main components: Environment-based Validation (EV) and Loss-based Sampling (LS). Notably, LS appears to require group labels for hyperparameter tuning, while EV utilizes environment labels generated through Environment Inference for Invariant Learning (EIIL) as a stand-in for group labels. However, EIIL was originally proposed by Creager et al., 2021, and it was inherently designed to address scenarios where group labels are not available. Although Creager et al., 2021 used true group labels for model selection within GroupDRO in their experiments, it appears that environment labels could also be suitably employed for this step. The paper does not fully clarify the distinction between environments and groups, and how the method avoids using group information during hyperparameter selection for LS.

### Questions
- From lines 452-457, the authors state that annotation-free methods can mitigate the impact of both labeled and unlabeled shortcut features more effectively. However, EVaLS-GL, which utilizes group labels, achieved better results than EVaLS. Could the authors provide their insights on this phenomenon?
- 
In the experiments, the performance of EVaLS and EVaLS-GL varied, with each having its strengths and weaknesses. Could the authors discuss the advantages and disadvantages of using inferenced environments versus group labels based on these findings?

### Soundness
3

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
3

### Summary
This paper works in the sub-population shift setting, in which the data consists in samples of different groups that shares a property. The goal is to learn a model robust to sub-population shifts, such as class imbalance, attribute imbalance, and spurious correlations. They propose a method (EVaLS) that improves the robustness of models trained using ERM without using any group annotation data. The method is well motivated both empirically and theoretically, and they show that the model has competitive performance with and without using group annotation. Moreover, they show that EVaLS is robust to scenarios where there is an unknown spurious attribute in comparison to the state-of-the-art.

### Strengths
- Simple method, that works in multiple scenarios (with and without group annotations).  
- The method do not make strong assumptions about the trained model. The only requirement is a model trained by ERM (the training data or any other training information is not necessary), while the method acts in a post-training phase.  
- It shows competitive performance in comparison to the literature, while it has a less strict set of requirements in comparison to most of them.  
- EVaLS outperforms the DFR (one of the state-of-the-art models) in cases with multiple spurious attributes

### Weaknesses
 - Make a comparison of EVaLS with more methods (e.g. AFR, since it also doesn't depend on ERM training) in the multiple spurious attributes scenario.
- Have more evidence that EVaLS outperforms the DFR/other methods in cases with multiple spurious attributes (e.g. using more datasets). I believe that this is the strongest part of the results, and it is a clear advantage for EVaLS (besides cases in which group annotation is not available).



### Questions
Some questions:
1) Is it feasible to add AFR results to the multiple spurious attributes experiment?   
2) Is it feasible to add an extra dataset to the multiple spurious attributes experiment?

Adding these extra results will address the points mentioned in the weakness, showing stronger empirical evidence about EVaLS advantage in cases with multiple spurious attributes. 

Minor points:
- There are references to Figure 1 (Line 83) and Figure 3 (Lines 172-177) that come before Figure 2 and were a bit confusing to me while I was reading the paper for the first time. In my opinion, removing these references will improve the readability of the paper.  
- Figure 2 instead of figure 2 (Line 205).  
- Have the oracle results as a reference in Table 6 to follow Figure 4 (b).  
- Figure 4 (b) could include the standard deviation (such as in Table 6).  
- Sometimes you use sub-population (Line 131) or subpopulation (Line 139). Keep it consistent across the paper.

### Soundness
3

### Presentation
3

### Contribution
3
