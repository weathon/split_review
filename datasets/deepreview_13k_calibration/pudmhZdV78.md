# In-context learning in presence of spurious correlations

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Large language models exhibit a remarkable capacity for in-context learning, where they learn to solve tasks given a few examples.
Recent work has shown that transformers can be trained to perform simple regression tasks in-context.
This work explores the possibility of training an in-context learner for classification tasks involving spurious features.
We find that the conventional approach of training in-context learners is susceptible to spurious features.
Moreover, when the meta-training dataset includes instances of only one task, the conventional approach leads to task memorization and fails to produce a model that leverages context for predictions.
Based on these observations, we propose a novel technique to train such a learner for a given classification task.
Remarkably, this in-context learner matches and sometimes outperforms strong methods like ERM and GroupDRO.
However, unlike these algorithms, it does not generalize well to other tasks.
We show that it is possible to obtain an in-context learner that generalizes to unseen tasks by training on a diverse dataset of synthetic in-context learning instances.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the problem of in-context learning in the presence of spurious correlations. The authors first examine the single-task setting and demonstrate that conventional approaches are vulnerable to spurious correlations. To address this issue, they propose several techniques to improve generalization in the presence of spurious correlations for in-context learning. However, they find that these methods do not generalize well to multiple tasks. Consequently, they develop additional techniques for training on diverse datasets and demonstrate the effectiveness of their method through experiments.

### Strengths
1. The paper addresses an important and interesting problem in in-context learning, as spurious correlations are a common issue in real-world scenarios.
The proposed method is generally sound and is validated by experimental results.

### Weaknesses
1. A major issue, although acknowledged in Section 5, is the requirement of spurious feature annotations. This is a strong assumption in practice and may significantly limit the applicability of the proposed method. The reliance on knowing *which* features are spurious is a substantial limitation, as this information is rarely available in real-world scenarios. The method's effectiveness hinges on this annotation, making it less practical for many applications where such annotations are not readily accessible or are costly to obtain. Furthermore, the paper does not adequately address how the method would perform with noisy or imperfect spurious feature annotations, which is a more realistic scenario.

2. In Section 2.2, an intuitive method would be to sample all in-context samples $x_i$ such that they all have a uniform group distribution. This could mitigate the issue of spurious correlations. Could the authors explain why they did not adopt this method? What are the experimental results of this approach?

3. The paper would benefit from more intuitive figures to explain the settings and proposed methods. Given the complexity of these settings, visual aids would help readers better understand them.

4. The authors construct a simulated dataset, Waterbird-Severe, to validate the effectiveness of their method. However, this dataset may not be realistic and contains a spurious correlation that is unrealistically strong. As a result, it would be more convincing if the authors conducted experiments on more realistic datasets. The artificial nature of the Waterbird-Severe dataset, with its exaggerated spurious correlation, raises concerns about the generalizability of the findings to real-world data. The paper lacks sufficient justification for the specific parameters used in generating this dataset and how they relate to real-world scenarios. The strong correlation might be an oversimplification, and the method's performance on this dataset might not be indicative of its performance on more complex, naturally occurring datasets.

### Questions
See the weakness part.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, authors explored the limit of current ICL framework by present more challenging setup in image classification with presence of spurious correlation in the features. They showed that existing approaches can lead to poor performance under distribution shift due to memorization issue. They proposed a new way of forming new ICL instances that can outperform baselines and mitigate this issue.

### Strengths
1. This paper proposes an interesting idea and the method is novel. 
2. Conducted analysis and experiments to demonstrate the idea and effectiveness.
3. Overall, the paper is well-written.

### Weaknesses
1. Impact of the paper is limited given current setup and experiments. 
2. Experiments are very limited and need more benchmarks to show this approach is generalizable to other cases.

### Questions
1. Some simulations and theoretical analysis or proof can make the paper stronger. 
2. It might worth to explore this idea with more benchmarks and experiments in visionLLM or LLM setup? ICL are frequently used in those models with prompts and I am curious if this method can improve the capability of ICL there, which can greatly enhance the impacts.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper explores the challenges and limitations of training large language models for in-context learning (ICL) on classification tasks that involve spurious features. The authors argue that conventional ICL approaches are susceptible to spurious correlations and can lead to task memorization rather than leveraging context for predictions. To address these issues, the paper proposes novel techniques for training ICL models that are more robust to spurious features and less prone to task memorization. The proposed methods involve permuting input embedding dimensions and constructing ICL instances with intermediate queries to simulate distribution shifts. The paper demonstrates that these techniques can lead to in-context learners that match or outperform established algorithms like ERM and GroupDRO on certain tasks. Furthermore, the authors show that by training on a diverse dataset of synthetic ICL instances, it is possible to obtain a more general-purpose in-context learner that can generalize to unseen tasks involving spurious features.

### Strengths
1. The paper introduces a new perspective on ICL by focusing on the impact of spurious correlations, which is an important yet underexplored area in the context of large language models.
2. The authors provide a thorough analysis of the problem, backed by empirical evidence from experiments on various datasets, including Waterbirds, CelebA, and iNaturalist.
3. The proposed method to mitigate task memorization and increase robustness to spurious features are innovative and show promising results in improving ICL, especially when the number of context examples is limited.
4. The paper not only focuses on in-context learning for a specific task but also addresses the generalization of the learned algorithm to unseen tasks, which is a critical aspect of real-world applicability.
5. The paper is well-organized, with a clear presentation of the problem, methodology, experiments, and results, making it easy to follow the authors' line of reasoning.

### Weaknesses
My primary concern with this paper lies in the limited support for the effectiveness of the proposed methods: "(a) passing example groups as input and (d) promoting learning of induction heads by occasionally querying past context examples."  The paper lacks a strong theoretical foundation for these methods, and the experimental validation is somewhat restricted.

Specifically, I have the following observations:

1. The experiments consider only a single model structure, depth, and width. The impact of these architectural hyperparameters on the effectiveness of the proposed methods remains unexplored.  Investigating different architectures could reveal whether the observed benefits are consistent across a wider range of models.

2. The experimental results are confined to three datasets: Waterbirds, CelebA, and iNaturalist. While these datasets are commonly employed in the Out-of-Distribution (OOD) generalization literature, they are relatively simple and may not fully capture the complexity of spurious correlations encountered in real-world applications. Evaluating the proposed methods on more diverse and challenging datasets would strengthen the claim of their effectiveness.

3. The paper does not address the possibility of data leakage, which could inadvertently inflate the reported performance.  A thorough analysis of potential data leakage sources and mitigation strategies is necessary to ensure the validity of the results.

### Questions
Could the authors provide a visual analysis to help readers intuitively understand the specific spurious features on which the existing methods and the proposed methods are effective or ineffective?

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
4

### Summary
This paper studies in-context learning image classfication tasks in presence of spurious correlations. The authors find that:
* permuting the image embeddings prevents transformers from memorizing the task and promotes in-context learning;
* inserting intermediate queries along with permuting embeddings enhences robustness to spurious correlations;
* using proceeding examples as queries improves the performance on both majority and minority groups; 
* passing group values to the context improves the performance on minority groups.

Except for Waterbirds dataset, these findings are also verified on (i) the Waterbirds-severe dataset where the spurious features are enhenced; (ii) a varying spurious correlations dataset adapted from iNaturalist. However, the transformer trained on dataset in (ii) fails to be robust against the spurious correlations in the dataset in (i).

### Strengths
This paper has a clear structure and interesting findings. I appreciate that authors also conduct experiments in the setting of different spurious correlations and test the trained model on unseen tasks.

### Weaknesses
1. Motivation for the proposed approach is unclear. I feel the effcacy of the proposed approach should be attributed to the fact that $q_i$ are sampled from the uniform group distribution and the autoregressive loss is only taken on these queries (Please correct me if I am wrong). This seems a bit werid to me -- under the spurious correlation setting, is it appropriate to assume that we have access to the uniform group distribution at the training stage? If one has access to the uniform group distribution data, why not simply use a training sequence consisting of these data as in-context examples?

2. Lacks of in-depth analysis and interpretation. For example, in section 2.4 the authors obtain interesting results by stwiching the evaluation data to (i) Waterbirds-severe; (ii) background prediction on Waterbirds; (iii) background prediction on Waterbirds with group-balanced context. There is one vague hypothesis saying the model learns to ignore the specific spurious feature in the pretrain data, which lacks further analysis and evidence. The trained model gets around 50% overall test accuracy and 9% worst-group accuracy on predicting the backgroud, which justifies your this hypothesis. However, the results on Waterbirds-severe and group-balanced Waterbirds seem to suggest the model still *in-context learns* to use the background feature. It feels to me the model learns some "biased initialization" (prefer to ignore specific feature) after pretraining on the spurious correlated data with the proposed approach, and then adjusts accroding to the in-context examples on top of this "biased initialization". Discussions along similar directions are lacked. Similar issues for the generality part in section 3. I feel more in-depth discussions would be beneficial.

3. Clarity issue: the paragraph "More concretely, ....." in section 3 is hard to parse. Would be helpful if there's an illustration for this data generating procedure. Also some other minor problems, please see questions.

### Questions
1. When producing Waterbirds-severe dataset, how is $\tilde s$ computed? Is it added before or after the permutation if using $+P$ technique.
2. For the $+I$ technique, is there any evidence that the performance gain is attributed to the forming of induction heads? This is not very obvious to me since the pair $(x_i,\tilde y_i)$ does not contribute to the loss function explicitly and the label of $q_{i-1}$ does not appear in the sequence. 
3. In the last paragraph, the authors claims the proposed approach does not require spurious feature annotations at inference time. Am I missing anything? I feel using $\tilde y$ to represent group ($+G$) technique requires the annotations at inference time since the inference sequence is also using the same form of $\tilde y_i$.
4. The questions in the weakness part.

### Soundness
3

### Presentation
2

### Contribution
2
