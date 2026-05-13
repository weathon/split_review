# Decentralized Federated Learning Over Noisy Labels: A Majority Voting Method

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Contrary to centralized federated learning (CFL), decentralized federated learning (DFL) allows clients to cooperate in training their local models without relying on a central parameter server. As different clients have varying annotation skills and preferences, noisy labels are inevitable in decentralized data ownership. In centralized learning (CL) and CFL settings, learning from noisy labels has been extensively explored; however, such methods cannot be directly applied in DFL settings due to limited computational resources or privacy requirements. This paper introduces DFLMV \textit{(majority voting based decentralized federated learning)}, a general DFL framework for learning from noisy data without relying on any assumptions about local client noise models while maintaining data privacy for all clients. Specifically, (1) Clients first use traditional DFL to train their local models until they become stable. (2) Clients use each of their neighbors' models to make a prediction of every data point in their training datasets, then correct the labels based on majority voting. (3) Clients further fine-tune their models based on their updated training dataset. A theoretical analysis of DFLMV is also provided. Extensive experiments conducted on MNIST, Fashion-MNIST, CIFA-10, CIFAR-10N, CIFAR-100N, Clothing1M, and ANIMAL-10N validate the effectiveness of our proposed approach at various noise levels and different data settings in mitigating the adverse effects of noisy labels.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a decentralized federated learning algorithms to handle noisy training labels. The federated networks first perform decentralized training. Then each client makes predictions based on the majority voting from the models from its neighbours. The submissions tries to give some theoretical justifications of the proposed approach. Experiments show that the proposed algorithm improves model accuracy across various datasets, under non-IID settings and various noise conditions.

### Strengths
Handling noisy training data and understanding the generalization of robust learning algorithms (with distribution shifts) is an important problem.

The proposed method is relatively lightweight, communication efficient, and easy to implement.

Experiments consider various noisy ratios and settings.

### Weaknesses
It is not clear what implications Theorem 1 (the generalization result) have. In addition, it is modeling the gap between the population error under two distributions, not involving empirical error over the noisy dataset, making it not applicable to practical settings where we only have access to a finite set of samples. Consequently, Theorem 2 has similar issues.

Clients train on non-IID data, and it is not clear why assuming vote distributions are identical reasonable.

The proof of Theorem 3 is confusing. theta_1 (and theta_2) are the differences between the two probability distributions, but `difference’ is not defined. How does the submission mean by theta_1 is larger than theta_2?

Experiments use simple and similar datasets (despite including a set of image benchmarks). The non-IID dataset partition among clients is not natural partitions, and doesn’t fully reflect the real-world non-IIDness. 


Experiments don’t compare with algorithms that target at label noise, for instance, simple baselines such as applying state-of-the-art robust learning algorithms (against noisy labels) locally on each client during decentralized training.

### Questions
Please see 'weaknesses'.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces DFLMV, a decentralized federated learning (DFL) algorithm for training under noisy labels. DFLMV has in total three stages: (1) initial model training with traditional DFL, (2) label correction using a majority voting mechanism with peer models, and (3) fine-tuning models on the corrected data. This approach tackles the label noise issue without a centralized server and without the need for additional clean datasets. The authors provided theoretical guarantees on generalization error and error rate bounds for the majority voting mechanism. In addition, the authors conducted extensive experiments to demonstrate the accuracy improvements of DFLMV across several benchmark datasets.

### Strengths
- The idea of using peer model majority voting in the DFL setting for handling label noise is novel. 
- The paper provided clear explanations of the stages in DFLMV with the detailed theoretical analysis for each component of the algorithm.
- The evaluation of DFLMV is extensive where the authors considered different data distribution and label noise distribution. The results all demonstrated that the proposed method is effective.

### Weaknesses
Some details and ablation studies about the dataset partition are missing: how many clients are there for each dataset? For each client, how are the neighbors defined? How does the number of neighbors affect the utility of this approach? How many data points are needed for the initial staging to provide a reasonable model for relabeling? Furthermore, the paper lacks a discussion on the computational cost associated with the majority voting process, especially in scenarios with a large number of clients or neighbors. The communication overhead for exchanging model parameters among clients is also not discussed. It is unclear how the method scales with increasing numbers of clients and how the convergence rate is affected by the decentralized nature of the algorithm. Finally, the paper does not explore the sensitivity of the method to the choice of initial model parameters, which could significantly impact the performance of the label correction stage.

### Questions
- How robust is this approach considering malicious clients who might intentionally send manipulated model parameters to mess up the majority voting process?
- Have you considered other voting methods, e.g. weighted majority vote based on peer distance?

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
Noisy labels exist in widely used datasets, which can adversely affect model training. Existing methods aiming for learning with noisy labels mostly focus on centralized learning (CL) and centralized parameter server-based FL (CFL) settings, which cannot be efficiently employed in the decentralized federated learning (DFL) setting.
This paper then proposes a framework for learning with noisy labels in the DFL setting. The proposed framework is made up of three stages: typical DFL training, label correction which is based on majority voting, and extra fine-tuning.
The authors also provide a theoretical upper bound on the generalization error of any DFL algorithm using cross-entropy loss under arbitrary label noise, and an upper bound on the error rate of majority voting.
Experimental results further show the effectiveness of the proposed framework against noisy labels.

### Strengths
- The motivation is clear, and the paper is well-written.
- The proposed framework is simple yet effective, and it includes a theoretical analysis of performance bounds.
- Extensive experiments across various IID and non-IID data/noise settings demonstrate the effectiveness of the proposed framework.

### Weaknesses
 - The assumption that the distributions of the votes are identical seems too strong, particularly under non-IID settings which mostly cannot stand. The paper does not adequately address the implications of this assumption, especially given that the core motivation is to handle noisy labels in decentralized federated learning, where non-IID data is the norm. The theoretical analysis, while valuable, is limited by this assumption, making its practical relevance questionable.
- It is still not clear about the extra overhead. Regarding the claim "DFLMV does not introduce any extra communication overhead", stage 2 involves communication among clients, which would introduce extra communication overhead. Besides, stages 2 and 3 can be considered as the extra steps as stage 1 can be viewed as a whole typical DFL training (until it reaches a stable point), aside from the dimension of model parameters, then the extra overhead would be related to the number of iterations and local epochs in the later 2 stages. The paper lacks a detailed breakdown of the computational and communication costs associated with stages 2 and 3, making it difficult to assess the practical efficiency of the proposed framework. The $O(n)$ computational overhead mentioned is vague without specifying the constants involved and how it scales with the number of clients and the complexity of the models.

### Questions
- Regarding stage 2, can the authors please explain why not consider the aggregated model for label correction? Also, in this way, existing methods could be adopted in DFL as well, and the computational cost may vary.
- Can the authors please provide specific extra computational costs, at least for one setting?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper tackles the challenge of training machine learning models in decentralized environments with noisy label data. To address this, the paper proposes a majority voting-based algorithm called DFLMV (Decentralized Federated Learning Majority Voting), designed to enhance model quality in the presence of label noise without the need for a central server. DFLMV consists of three key stages:

**Initial Training Stage:** Each client performs traditional decentralized learning on its local dataset (an merging periodically with their neighbors) to train an initial model. After training for several epochs, each client reaches a « stable loss » value, at which point it moves to the label correction phase.

**Label Correction Stage:** Clients share model parameters with their neighbors, who then use these models to predict labels on their data. For each data point, the client assigns a new label based on majority voting among the predictions from its neighbors, thus correcting potentially noisy labels.

**Retraining Stage:** With updated labels, clients further fine-tune their local models on this improved dataset to enhance model accuracy and robustness.

The paper provides some theoretical analysis simplified results on the performance of DFLMV. It also compares DFLMV to PENS, another noisy label decentralized learning approach, by evaluating both methods across multiple datasets (e.g., MNIST, Fashion-MNIST, and CIFAR-10) under various levels of label noise and data heterogeneity.

### Strengths
The paper addresses a meaningful topic, and further exploration in this direction holds strong potential to benefit the research community. The core idea is clear and straightforward, which is an advantage. Furthermore, provided the results withstand scrutiny, it offers a practical and effective approach to improving the robustness of machine learning algorithms against label noise.

### Weaknesses
I found the paper challenging to follow, as aspects such as the organization, technical writing, clarity of results, and integration of related work could significantly benefit from improvements. Strengthening these areas would greatly enhance the paper’s overall clarity and impact. To be more precise I provide a specific list of concerns below.

## Quality of Technical Writing
In my view, the level of technical writing in this paper currently falls short of the standards expected for a top-tier conference like ICLR. Here are some specific points that I believe limit its clarity:

**Problem Presentation**: The problem setup presents an optimization problem in Equation (1) before defining the relevant notations. Generally, it would improve readability to first introduce the notations, clearly defining spaces and terms, and then present the optimization problem. 

**Unexplained Concepts and Notation**: Several concepts and notations are introduced without sufficient explanation. For example, symbols like $d_x$ and $d_y$ first appear in line 182 without clarification, similarly $f_k$ in line 193, and the term "non-colluding neighbors" in line 299. Although these may appear minor, they contribute to a challenging reading experience, especially in the preliminaries.

**Inconsistencies in Notations**: There are several inconsistencies in the notations, which make the paper harder to follow. Here is a non-exhaustive list:

   - The loss function is first introduced as $\mathcal{L}$ in Equation (1), then $\mathcal{L}_k$ in Equation (3), and switches back to $\mathcal{L}$ in Equation (4) before reverting to $\mathcal{L}_k$ in Equation (8).

   - The output space and corresponding vectors vary between $\mathbb{R}^{d_y}$ and {$1, \dots, C$}, leading to errors such as computing the one-hot encoding of a vector from $\mathbb{R}^{d_y}$ in line 191. This inconsistency also makes Theorem 1 difficult to interpret, as the left-hand side assumes vectors in $\mathbb{R}^{d_y}$ while the right-hand side assumes $Y$ is discrete.

   - Datasets are defined as sets of lowercase samples in Section 3, then as sets of uppercase random variables in Section 4.

   - Both $B$ and $n_{\text{peers}}$ appear to serve the same role, but they are used interchangeably throughout the paper.

## Presentation of the algorithms

The algorithm’s presentation lacks clarity and structure in the main paper. The analysis is intertwined with the algorithm's steps, making it difficult to follow. I would suggest dedicating one section solely to the algorithm's presentation and a separate section for the analysis to improve readability.

## Clarity and soundness of the results

Due to the clarity issues mentioned earlier, the presented results exhibit similar concerns on clarity. While I have reservations about their overall soundness, I believe that at least Theorem 1, as it currently stands, is factually incorrect. It appears that the paper attempts to adapt results from (Ke et al., 2023), but it overlooks key assumptions from the original work, particularly Assumption 5 and Assumption 6. As a result, the conclusions drawn in this paper cannot be valid, and consequently, the proof that follows the steps of (Ke et al., 2023) is also flawed. 

## Related work and comparison with existing solutions

The analysis of related work could be strengthened significantly. For instance, in line 125, the claim that decentralized (federated) learning was introduced by Lalitha et al. (2018) is misleading. The research on decentralized algorithms actually has a rich history (see e.g.,https://arxiv.org/pdf/2006.13838).

Additionally, I found the reference to (Yagli et al., 2020) regarding the definition of generalization somewhat confusing. After reviewing that reference, it does not appear to directly address the concept of noisy labels, and I was unable to locate a definition comparable to Equation (10). Could you provide a more appropriate reference for your definition of generalization error, or explain how you derive your definition from Yagli et al. (2020) if it is indeed relevant?

I also believe that the paper would benefit from a comparison with solutions that address stronger forms of corruption, such as Byzantine attacks in decentralized learning (see e.g., https://proceedings.mlr.press/v202/farhadkhani23a/farhadkhani23a.pdf). While I understand that your paper does not focus on these stronger attacks, exploring whether existing defenses in the literature could also apply to the seemingly simpler problem of noisy labels would be valuable. It’s possible that these methods may be less effective in terms of accuracy, but gaining insight on this would be beneficial before developing alternative approaches.

Finally, I would like to note that it appears the current paper is heavily inspired by (Ke et al., 2023), including similarities in notation and results. Given this, it seems somewhat unexpected that (Ke et al., 2023) is cited only once and solely in the appendix. A more thorough engagement with this source, discussing more explicitly how the submission builds upon or differs from Ke et al. (2023) (highlighting both similarities and key differences) could enhance the paper's depth and contextualization.

### Questions
Please comment on the above concerns

### Soundness
1

### Presentation
1

### Contribution
2
