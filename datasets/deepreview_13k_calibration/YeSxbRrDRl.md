# Dist Loss: Enhancing Regression in Few-Shot Region through Distribution Distance Constraint

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Imbalanced data distributions are prevalent in real-world scenarios, posing significant challenges in both imbalanced classification and imbalanced regression tasks. They often cause deep learning models to overfit in areas of high sample density (many-shot regions) while underperforming in areas of low sample density (few-shot regions). This characteristic restricts the utility of deep learning models in various sectors, notably healthcare, where areas with few-shot data hold greater clinical relevance. While recent studies have shown the benefits of incorporating distribution information in imbalanced classification tasks, such strategies are rarely explored in imbalanced regression. In this paper, we address this issue by introducing a novel loss function, termed Dist Loss, designed to minimize the distribution distance between the model's predictions and the target labels in a differentiable manner, effectively integrating distribution information into model training. Dist Loss enables deep learning models to regularize their output distribution during training, effectively enhancing their focus on few-shot regions. We have conducted extensive experiments across three datasets spanning computer vision and healthcare: IMDB-WIKI-DIR, AgeDB-DIR, and ECG-Ka-DIR. The results demonstrate that Dist Loss effectively mitigates the negative impact of imbalanced data distribution on model performance, achieving state-of-the-art results in sparse data regions. Furthermore, Dist Loss is easy to integrate, complementing existing methods. Our code will be made publicly available following the review process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles the issue of imbalanced regression, which often results in poor performance in regions with few samples, by proposing a new loss function termed Dist Loss. Dist Loss is designed to reduce the distribution gap between model predictions and actual labels, thereby promoting closer alignment with the target distribution, particularly in sparse data regions. The approach has shown enhanced performance in few-shot scenarios across several datasets, such as IMDB-WIKI-DIR, AgeDB-DIR, and ECG-Ka-DIR, and complements existing techniques well. Through extensive experimentation, Dist Loss demonstrates state-of-the-art accuracy for rare instances, highlighting its relevance for critical fields like healthcare.

### Strengths
1. The paper introduces Dist Loss, a new loss function specifically designed to tackle the problem of imbalanced regression, improving model performance in low-sample regions.

2. Dist Loss is easy to incorporate with current techniques and enhances their performance in few-shot areas, making it a practical addition to existing approaches.

3. The proposed method is evaluated on different datasets.

### Weaknesses
1. According to the problem setting, the distribution has been discretized using fixed bin size, which can also be adapted into classification setting if one have a look at Figure 1. However the authors claimed in section 2.2 that the methods developed for imbalanced image classification can not be well adapted into imbalanced regression task. From my point of view, if bin is chosen then classification based method can also be used in regression task. More explanation should be provided by the authors.


2. The performance gain of the proposed loss function is not promising compared with Balanced MSE in Table I. It even underperforms BalancedMSE on IMDB/WIKI/DIR dataset using GM metric.

3. The authors are also suggested to compare with some other existing related works, e.g., a.

In a and b, the task is evaluated in four different settings, which are all, many, medium, few, which is also mentioned by the authors. However it seems in the provided Tables there are only results for few shot regions. I find the original different shot settings more convincing since it can showcase the generalizability of the proposed loss function among different shot settings.

Another question, why the reported performance of ConR is different compared with the performance reported by their paper for AgeDB DIR dataset? Did the authors follow the same experimental setting as introduced in ConR and other existing works?

a. Wang, Z., & Wang, H. (2024). Variational imbalanced regression: Fair uncertainty quantification via probabilistic smoothing. Advances in Neural Information Processing Systems, 36.

b. Keramati, M., Meng, L., & Evans, R. D. (2023). Conr: Contrastive regularizer for deep imbalanced regression. ICLR 2024.

4. In Table 3, it seems that balanced MSE is better than the proposed Dist Loss regarding the training time consumption. The benefits from the training efficiency pespective is now well highlighted.


5. I have some concerns with Table 4. From the paper of ConR as mentioned in b, LDS with ConR can achieve better performance on AgeDB DIR dataset, with 9.62 for MAE and 6.87 for AgeDB DIR when we considering the few shot setting. The authors are suggested to compare with all other existing works in Table 4.

### Questions
1. In Section 2.2, the authors claim that imbalanced image classification methods cannot be well adapted for imbalanced regression. However, with the chosen discretized distribution using fixed bin sizes, wouldn't classification-based methods be applicable? Could the authors elaborate on why classification-based methods might not work well in this setting and clarify the limitations or challenges?

2. The proposed loss function does not show a strong performance improvement over Balanced MSE, as shown in Table I, and it even underperforms Balanced MSE on the IMDB/WIKI/DIR dataset using the GM metric. Can the authors explain why the proposed loss function struggles to outperform Balanced MSE in these cases and discuss any specific scenarios where it demonstrates advantages?

3.Could the authors compare their method with other existing works, such as Wang & Wang (2024) and Keramati et al. (2023)? These works evaluate the task across different settings (all, many, medium, few), which seems like a more convincing framework to assess generalizability. Why did the authors choose not to include similar shot-based evaluations? Would this additional analysis provide deeper insights into the model’s robustness?


4.The performance of ConR reported in the paper differs from what is reported in the original ConR paper for the AgeDB DIR dataset. Did the authors follow the same experimental settings as in these related works? If there were any differences in the setup, could they clarify these and explain how they might impact the results?

5.Table 3 shows that Balanced MSE is more efficient in terms of training time compared to the proposed Dist Loss. Could the authors discuss the trade-offs between training time efficiency and performance gain? Given the additional time cost, what are the practical advantages of using Dist Loss?
Performance on AgeDB DIR Dataset in Few-Shot Settings:

6. According to Keramati et al. (2023), ConR combined with LDS achieved better results on the AgeDB DIR dataset in the few-shot setting (MAE of 9.62 and 6.87). Why does the proposed method seem to underperform compared to this? Did the authors consider integrating ConR or LDS in their approach to enhance few-shot performance, and if not, what were the reasons?

### Soundness
3

### Presentation
3

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
The paper addresses the challenge of imbalanced data distributions in regression tasks, especially the difficulty deep learning models face in accurately predicting few-shot settings. The authors introduce a new loss function, called Dist Loss, designed to align the distribution of model predictions with the label distribution using kernel density estimation and pseudo-predictions. The authors also contribute a differentiable relaxation for their loss function to make the model end-to-end training. The paper conducts experiments on the regression of three datasets, compares with five related works, and has demonstrated significant improvements.

### Strengths
The paper has the following strengths:

(i) The problem of imbalanced regression tasks is important to study but less well investigated in related works. The authors contributed a new loss function to train the model and showed good results compared to other baselines in two aspects: using the new loss function integrated into the baseline and combining the existing training loss with their proposed one. The running time is as fast as the mean squared error and significantly faster than other baselines. 

(ii) The idea of using a pseudo-label to define the distance between prediction and label distribution is interesting. Also, the authors applied different sorting techniques to make their Dist Loss ($L(S_P, S_L)$) trainable.

### Weaknesses
While the paper achieved good results, its presentation lacks details and information to help the reviewer understand core ideas and how the method efficiently addresses imbalanced problems in regression tasks.

(i) In Figure 2, what is the role of **"Labels"** and **"Predictions"** terms (inside **Dist loss calculation**) while the Loss function already received **Pseudo-labels** and **Sorted Prediction**?

(ii) In Section 3.2.1, authors jumped into detail about how they compute pseudo-labels and pseudo-predictions but they have not addressed two key questions:
+ Why do we need to compute "pseudo-here"? How is it important to deal with the imbalanced dataset?
+ Section 3.2.1 is based on the Empirical label distribution (KDE), but no details about KDE are discussed (either background and how it is used), which makes the readers unable to follow the details later. For e.g., is the KDE step applied at a batch size level or at the whole training dataset?

Another unclear problem is the standard regression formulation, which transforms continuous label space Y into discretized B bins (**Section 3.1**). How is the standard learning scheme trained with these discretized labels?

(iii) The descriptions in Equation (1) and (2) and the definition of $N_{L'}$ are also hard to imagine without a figure to illustrate core ideas beyond.

Overall, the paper's methodology section is not well presented, with information presented sporadically, and does not address core concerns about imbalanced settings.

### Questions
The reviewer has the following questions:


(a) can you explain how the KDE is used in your formulation? What is input data? Do we need to use it in the testing part or only in the training steps?

(b) can you explain why the pseudo-label is important to overcome imbalances in regression?

(c) The ablation study in Table 4 is difficult to capture. In particular, the authors mentioned, *"We demonstrate the effects of using different functions, considering the probability-based inversely weighed MAE and MSE losses."* There are two questions here. First, what is *probability-based inversely* (INV) ? and why $INV - L_1$ or $ INV - L_2$ shows benefit of your proposed one?

(d) because dist_loss works with discrete values in sorted orders, how can you make the training process stable and avoid exploding gradients given large values from the loss function?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes a new approach, called Dist Loss, for imbalanced deep regression. Specifically, the method generates pseudo-labels taking into consideration label distribution information, and at the same time generates pseudo-predictions. The paper is novel and well-written, but has a number of issues and can be strengthened.

### Strengths
The paper proposes an interesting and concise idea by generating pseudo-labels and pseudo-predictions for imbalanced deep regression. The paper is clearly written with elucidatory illustrations for easier understanding.

### Weaknesses
All datasets are image datasets and all models are ResNet-like models. The method has not been evaluated on more datasets like text data or tabular data.

The experiment setting may not be representative enough. For all three real-world datasets, their imbalance rates are fixed. However, the input data could be manually tweaked to generate datasets covering a wider range of imbalance rates, and to investigate the algorithm's performance in scenarios from mildly to extremely heavy-tailed distributions.

There is no theoretical analysis of the algorithm.

### Questions
In Figure 2, what is the exact form of the loss function L(.)? This is not clear from both the figure and the main text. Specifically, in Figure 2, for the two sequences [1, 3, 3, 4, 4, 4, 6] and [1, 2, 2, 3, 5, 6, 7], how is the loss computed?

The first step of the algorithm is discretization which maps the continuous label space Y into B bins. In such a way, the regression problem is transformed into a classification problem. Could you also show classification metrics such as overall accuracy and few-shot accuracy, along with the regression metrics, so that we have a more thorough understanding of the result? Again, what are the correlation metrics (Pearson's or Spearman's) of the results? Could you please also present some actual-by-predicted correlation plots of the prediction?

How did you determine the number of bins B?

### Soundness
3

### Presentation
3

### Contribution
3
