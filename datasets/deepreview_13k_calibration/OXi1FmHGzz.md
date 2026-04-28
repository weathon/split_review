# Vertical Federated Learning with Missing Features During Training and Inference

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Vertical federated learning trains models from feature-partitioned datasets across multiple clients, who collaborate without sharing their local data. Standard approaches assume that all feature partitions are available during both training and inference. Yet, in practice, this assumption rarely holds, as for many samples only a subset of the clients observe their partition. However, not utilizing incomplete samples during training harms generalization, and not supporting them during inference limits the utility of the model. Moreover, if any client leaves the federation after training, its partition becomes unavailable, rendering the learned model unusable. Missing feature blocks are therefore a key challenge limiting the applicability of vertical federated learning in real-world scenarios. To address this, we propose \texttt{LASER-VFL}, a vertical federated learning method for efficient training and inference of split neural network-based models that is capable of handling arbitrary sets of partitions. Our approach is simple yet effective, relying on the strategic sharing of model parameters and on task-sampling to train a family of predictors. We show that \texttt{LASER-VFL} achieves a $\mathcal{O}(\sfrac{1}{\sqrt{T}})$ convergence rate for nonconvex objectives in general, $\mathcal{O}(\sfrac{1}{T})$ for sufficiently large batch sizes, and linear convergence under the Polyak-{\L}ojasiewicz inequality. Numerical experiments show improved performance of \texttt{LASER-VFL} over the baselines. Remarkably, this is the case even in the absence of missing features. For example, for CIFAR-100, we see an improvement in accuracy of $21.4\%$ when each of four feature blocks is observed with a probability of 0.5 and of $12.2\%$  when all features are observed.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies vertical FL with missing features. The authors propose a new vertical FL method named **LASER-VFL** for efficient training and inference of split neural network-based models. This method relies on the strategic sharing of model parameters and on task-sampling to train a family of predictors. The authors also provide convergence rates for **LASER-VFL** under different objective functions.

### Strengths
1. This paper proposes a new algorithm to address the missing features in vertical FL.

2. Valid convergence analysis and experiments are provided.

### Weaknesses
1. The notations are too complex, which is not friendly for readers. The authors should try to simplify notations.

2. I'm not an expert in vertical FL, so I'm confused about the **key idea** presented on page 4.  So it will be better to add workflow diagrams to explain the method.

3. The experiments are conducted on the data with synthetic missing features. It would be more convincing to show results on real-world vertical FL data with missing features.

### Questions
1. What do hyperparameters refer to in vertical FL? Is it the optimization parameters such as learning rate or some specific parameter in vertical FL?

2. Does the proposed algorithm allow multiple local updates in each machine like traditional FL?

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
This paper focuses on vertical federated learning (VFL), where data is partitioned by features rather than by samples. In this setting, each client possesses only a subset of the features for a specific sample. The paper addresses the challenge of missing features in the dataset and the heterogeneous availability of clients during the federation. Standard VFL approaches cannot handle these challenges, as it assumes that all features are available during both training and inference. To tackle these issues, this work proposes LASER-VFL, which relies on strategic sharing of model parameters and task sampling to train a family of predictors, allowing training and inference using any and all available blocks of features, leading to full utilization of the data. The paper provides theoretical guarantees for non-convex objectives and demonstrates empirical results on four different datasets, showing good performance.

### Strengths
The authors propose an approach for VFL that enables both training and inference using all available blocks of features.

The authors provide theoretical guarantees for convergence under L-smoothness, unbiasedness, and bounded variance assumptions. 

The authors conduct empirical evaluations of the proposed methods over 4 datasets, showing good performance.

### Weaknesses
For VFL models, the authors mention that split neural networks are often considered and explains that they seek to find multiple parameters for each block and for a fusion model. Then mentions that they aim to solve (1) which requires all the blocks, which contradicts the paper objective seeking VFL with missing blocks. The authors should be clear from the early stage whether they aim to solve (1), or other works aimed to solve (1). 

The authors mentions that LASER-VFL enables both training and inference
using all available blocks of features. However, in Figure 1 (b) (our method), shows that samples 4, 6, and 7, which has missing blocks, are only used for training (and not for testing), which is not clear why.

The authors go through some previous works very briefly in the introduction without going into details of their approaches and mention that these previous works add training stages and modules, making them more complex. While related work was provided later this paragraph seemed both redundant and unclear. 

The authors mentioned some works that dealt with missing features. Then surprisingly claim that to the best of their knowledge, LASER-VFL is the first method to enables both training and inference using any and all available blocks of features. (line 108: We propose LASER-VFL (Leveraging All Samples Efficiently for Real-world VFL), a novel method that enables both training and inference using any and all available blocks of features. To the best of our knowledge, this is the first method to achieve this.)

Citations should be \citep when discussing some paper (not the authors). For example in line 144 it should be in (Feng & Yu 2020; Kang et al. 2022a) not in Feng & Yu (2020); Kang et al. (2022a).

In VFL problems what cases would really requires more than a few clients to collaborate? In the empirical setting the authors considered 4 clients. If we have a few companies, why not simply do a combinatorial approach? For such few client cases, say 2 or 3, the authors could show the optimal performance of training the 2^k-1 models as an optimal target against the proposed solution. 

The authors introduce a lot of notations, which should be minimized to the least possible to make it easier to follow. (While the authors clearly mentions that the notation in (3) differs slightly from (1) and (2), this still should be avoided as much as possible). 

While the authors mention several methods that dealt with missing blocks, most of these approaches were not considered in the empirical evaluation. Being more complex and requiring multiple stages or modules should not be a reason to skip the comparison. It could be that these added stages or complexities lead to better accuracy and/or better efficiency in terms of rounds to accuracy. 

Giving uniform weights in the aggregation of the feature representations of different blocks of features for the different clients (Eq. (4)) would alter the performance compared to other concatenation methods. Averaging and sum can cancel some information which can be a drawback compared to concatenation methods.

While the authors claim that the method is suitable for a growing number of clients, avoiding the exponential growth in computation and memory. Empirical results should be provided to deal with more than 4 clients to see that the method indeed can achieve good performance. For example, would be nice to show for 8 and/or 16 clients. 

The theory shows convergence in the non-convex setting, under L-smoothness and other assumptions, which is appreciated. However, such results do not reveal the optimality of the method.

### Questions
How would the performance of the aggregation mechanism differ when using weighted averaging rather than simple averaging? What if some clients have more powerful feature blocks? Giving uniform weights would alter the performance compared to other concatenation methods.

How would the performance be with even larger number of clients?

For small number of clients, the combinatorial approach becomes feasible, how does the combinatorial approach (which can be considered as an upper bound) differ from the proposed method?

How does the method perform against the other discussed related works which does solve the same problem but may have different training stages/modules?

How would the results be in a convex setting? Where does it converge? Does it guarantee optimal performance of VFL with missing clients?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to handle missing features in VFL during both training and testing by sharing model parameters and sampling different configurations to approximate the exponential number of possible predictors (with different possible non-missing features).
The intuition is that entirely local models are robust to missing features but poor predictors while global models are stronger predictors but not robust missing features.
The paper proposes to train a set of models for all possible subsets of missing features by sharing model parameters and sampling different missingness patterns, called "tasks" in this paper, during training time.
The sampled tasks are weighted to approximate the loss function of all missing value patterns using Monte Carlo sampling of the tasks.
The paper provides theoretic results on convergence and empirically demonstrates their method compared to several baseline methods.

### Strengths
- The paper proposes a Monte-Carlo approach with weighting to train a split-NN architecture to be robust to missing features during training and inference. The method is relatively simple and avoids complex hyperparameters or multi-stage configurations.

- The paper provides theoretic convergence results on their proposed method.

- The empirical results show significant improvement over baselines methods used in the paper when there is missingness at inference time.

### Weaknesses
------ After reading author response ------
While I still have some concerns, the author response helped reduce them. Thus, I've increased my score by 1.
------ Original -------
- Either the setting is a small number of clients (say 4 as used in the experiments) and then it might be feasible to actually just train all possible models---this calls into question the motivation for learning "an exponential number of models" since there are only 24 models. Or, the setting is a large number of clients (say 10-100) and then finding large batches of samples such that the missing values are the same would result in either small or biased batches---which would violate assumption 2. Thus, the motivation of the paper or the requirement for large unbiased batches seem to be at odds with each other. 

- The assumption of unbiased batches would require the missingness to be Missing Completely at Random (MCAR) to ensure that the batches are unbiased. This seems unlikely to hold in real-world applications.

- The paper seems to overclaim a bit on the novelty or significance of the model sharing aspect. The model sharing aspect is a common approach in GNNs or other modern networks such as attention-based architectures, yet these do not claim significant novelty in terms of sharing model parameters across nodes.

- The paper lacks an empirical comparison to the method proposed in Ganguli et al. [2023] that can handle inference time faults. This seems to be a closely related method. They use dropout (like your task sampling), gossiping (like the ensemble-based baseline), and replication of the fusion/predictor (as you do as well).

[Ganguli et al., 2023] Ganguli, S., Zhou, Z., Brinton, C. G., & Inouye, D. I. (2023). Fault Tolerant Serverless VFL Over Dynamic Device Environment. arXiv preprint arXiv:2312.16638.

### Questions
- How does this paper compare to the methods proposed in Ganguli et al., [2023]? They seem to be doing something very similar including the dropout mechanism during training. Perhaps, the authors missed this very related work.

- The model architecture resembles a single-layer GNN with summation aggregation. Each client has it's own fusion predictor. Is this correct or am I missing something?

- While the weighting method for learning an "exponential number of models" is interesting, it is perhaps a bit misleading to argue for the "compactness" of learning an exponential number of models. Simple dropout could also learn "an exponential number of models" but it is difficult to argue that these models would be anywhere near the naive solution of actually directly training an exponential number of models.

- There are other types of parametric aggregation methods that can handle arbitrary sizes. For example, an attention-based aggregation or similar is a parametric aggregation method but can handle arbitrary length inputs.

- The notation is a bit overwhelming and needs to be simplified and clarified. In Eq 5 alone, there are 4 different uses of the $\mathcal{L}$ with different subscripts.

- Choosing a mini-batch with the same missing features in a real-world VFL scenario would introduce bias in the training batch since it is unlikely for the missing features to be missing completely at random (MCAR). Rather, different groups of samples will likely have similar missing features. Can you explain how your method would handle this? This seems to be a severe limitation as the exact missingness pattern is unlikely to happen often unless the number of clients is very small.

- Related to above, it seems that this biasedness in mini-batches would cause Assumption 2 in your theory to be violated. Thus, it is unclear if your theory is reasonable for the practical algorithm and real-world situation.

- Relatedly, how do you handle the fact that there might be missingness patterns that are far more common than others? 

- Does this assume that all clients participate during the training process (i.e., no client leaves even temporarily)? It seems that this requires all clients to be available during training (even if they do not participate in the training round).

- How are the baseline methods trained when there is missingness at test time? Are the batches with high missingness simply thrown out? It seems there are some simple baselines to adapt standard VFL by simply imputing zeros at train and test time or something like that. Stronger baselines with some naive adaptations like this for missing values would be helpful.  Currently, it seems that standard VFL is unfairly penalized.

- Do your experiments assume missingness completely at random (MCAR)? I'm guessing they do but wanted to double check. This would align with your theory.

- What happens if you do not weight things but just use simple dropout when sampling your missing features?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The author(s) proposed LASER-VFL to handle the missing feature challenge arising from the vertical federated learning problem. By transforming the objective into a finite sum problem, LASER-VFL can handle missing features (clients) via the task sampling technique, which is similar to client dropout. LASER-VFL is backed with theoretical analysis and some simple numerical experiments.

### Strengths
- The writing is clear in general;
- The paper is well-motivated, the missing feature during training and inference is a crucial problem in vertical federated learning from a practical perspective.
- The proposed method is simple and easy to understand.

### Weaknesses
 - The experiment section is rather weak:
    - Experiments details are missing, for example, the train/test split of dataset, the neural network architecture being used, the hyper-parameter tunning...
    - A baseline is missing, the naïve method described in section 2 (train exponentially many predictors).
    - The number of clients is set to 4 for all experiments, how does the result change when we increase the number of clients? If there are 4 clients, then it is not really computational prohibitive to train exponentially many predictors.
- Notations are quite heavy in line 293-342.
- The theoretical analysis assumes features are missed uniform randomly, which simplifies the problem significantly. By this assumption and transforming the objective into a finite sum problem, the author(s) could directly use classic convergence analysis of SGD without much technical modification. Therefore, the theoretical novelty is kind of limited.
- Minor: missing reference at line 855.

### Questions
By transforming the objective into a finite sum problem, is the convergence analysis almost the same as the classic convergence analysis of SGD?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on vertical federated learning. More specifically, the authors present a framework called LASER-VFL, which is more robust in handling missing features and any arbitrary combination of partitions. They provide a convergence rate analysis along with  experimental results.

### Strengths
I really enjoyed reading this paper. The presentation is good and easy to follow, and the experimental results are very convincing. More specifically:
- The paper addresses missing features problem, which is an important area of study in VFL.
- The proposed idea is simple yet effective. The authors create a fusion of arbitrary combinations of predictors on each client, allowing them to leverage all available features. To avoid sharing an exponential number of predictors, they propose a strategy in which only K predictors and K fusion models need to be shared. 
- They demonstrate improved performance compared to the existing works.

### Weaknesses
 - While the authors present related works, it is difficult to identify which components of the proposed framework are novel when reading Sections 2 and 3. I encourage the authors to provide a more detailed comparison with existing VFL approaches that address missing features.
- The results are convincing, especially given that they cover different levels of missing features. However, only two VFL methods are used for comparison. The authors are encouraged to include additional comparisons to better highlight the work's significance in the field of VFL.

### Questions
- Why are there K fusion models?  Is it because each client needs a specialized fusion model for its own task?
- Could the authors elaborate on line 2 in Algorithm 1 (Client K sample the same mini-batch .... via a shared seed)? What is the impact of this shared seed, and why is the same mini-batch important?
- Could the authors elaborate on how domain shift is addressed? Or how would the framework generalize if there were a significant level of domain shift across clients?
- Does the proposed framework have specific requirements for the fusion model and projectors? Also, what is the architecture of the fusion model and predictors in Section 5?

### Soundness
2

### Presentation
3

### Contribution
3
