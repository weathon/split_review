# Towards Realistic Mechanisms That Incentivize Federated Participation and Contribution

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Edge device participation in federating learning~(FL) is typically studied through the lens of device-server communication (\textit{e.g.,} device dropout) and assumes an undying desire from edge devices to participate in FL.
As a result, current FL frameworks are flawed when implemented in realistic settings, with many encountering the free-rider dilemma.
In a step to push FL towards realistic settings, we propose \realfm: the first federated mechanism that (1) realistically models device utility, (2) incentivizes data contribution and device participation, (3) provably removes the free-rider dilemma, and (4) relaxes assumptions on data homogeneity and data sharing.
Compared to previous FL mechanisms, \realfm allows for a non-linear relationship between model accuracy and utility, which improves the utility gained by the server and participating devices.
On real-world data, \realfm improves device and server utility, as well as data contribution, \textit{by over $3$ and $4$ magnitudes} respectively compared to baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces incentive mechanisms in federated learning (FL).

### Strengths
REALFM incentivizes edge devices to participate in federated learning by offering accuracy-based and monetary rewards proportional to each device's data contribution. This mechanism enables the central server to attain better model performance by motivating devices to contribute more data than they would on their own.

### Weaknesses
The paper lacks a detailed discussion on the computational overhead of implementing REALFM, especially given the added accuracy-shaping and monetary reward calculations. Including complexity analysis would help readers understand potential trade-offs.

The paper could be enhanced if  it could further exploring the impact of varying device capabilities (e.g., computational power, storage) on REALFM’s effectiveness and scalability.

A discussion on privacy-preserving mechanisms to protect device-specific information in the proposed setups would enhance the paper’s relevance to practical federated applications.

Given that contract-based FL mechanisms (e.g., using registration fees to penalize free-riders) are common in the literature, adding a comparative analysis with these mechanisms would offer a more rounded assessment of REALFM’s advantages and limitations.

### Questions
The paper lacks a detailed discussion on the computational overhead of implementing REALFM, especially given the added accuracy-shaping and monetary reward calculations. Including complexity analysis would help readers understand potential trade-offs.

The paper could be enhanced if  it could further exploring the impact of varying device capabilities (e.g., computational power, storage) on REALFM’s effectiveness and scalability.

A discussion on privacy-preserving mechanisms to protect device-specific information in the proposed setups would enhance the paper’s relevance to practical federated applications.

Given that contract-based FL mechanisms (e.g., using registration fees to penalize free-riders) are common in the literature, adding a comparative analysis with these mechanisms would offer a more rounded assessment of REALFM’s advantages and limitations.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes REALFM, a federated learning mechanism designed to incentivize edge device participation and data contribution by modeling device utility and removing the free-rider dilemma under non-i.i.d distributions. It introduces non-linear reward structures to enhance both device and server utility in federated settings with heterogeneous data. The proposed approach shows significant improvements in device contributions and model accuracy compared to existing mechanisms.

### Strengths
-The paper provides a solid theoretical framework, supported by rigorous proofs and analyses
- The paper is well-organized, with clear definitions and explanations that make the methods and results easy to follow.

### Weaknesses
 - The paper focuses on non-i.i.d case but uses "data heterogeneity" for so long before being precise, which can be misleading for the reader. Moreover, assumptions and mechanisms would struggle in highly variable data distributions: The accuracy shaping mechanism assumes that central server updates generally benefit all participants, which would not be the case for label or covariate shift. Specifically, the assumption that server updates universally improve model accuracy across all clients is a strong one, and the paper does not adequately address scenarios where updates might degrade performance for certain clients due to label or covariate shift. This is a critical oversight, as real-world federated datasets often exhibit such complex non-i.i.d characteristics, making the proposed approach less robust than claimed.
- REALFM introduces a complex reward and incentive mechanism that may be challenging to implement in "real-world" federated learning systems. The added layers of utility modeling and accuracy shaping might make it difficult to scale across diverse device types and operational environments. Additionally, the "real" part might be an overestimation. The computational overhead of calculating individual rewards based on non-linear utility functions and accuracy shaping is not negligible, and the paper lacks a detailed analysis of the computational cost and scalability of the proposed mechanism, especially when dealing with a large number of heterogeneous edge devices. This raises concerns about the practical applicability of the approach in resource-constrained environments.
- It is unclear what kind of "realistic" scenarios can benefit from such incentive scheme. The paper does not provide a compelling justification for the need for such a complex incentive mechanism in real-world applications. The examples provided are not sufficiently detailed to demonstrate the practical relevance and benefits of the proposed approach. The paper needs to provide more concrete examples of real-world scenarios where the proposed incentive mechanism is necessary and beneficial, and it should also discuss the potential limitations and challenges of applying the approach in these scenarios.
- The figures could have better readability by adding more information about the datasets

### Questions
- Please explain why "for example, accuracy improvement from 48% to 49% should be rewarded much differently than 98% to 99%" 
- Please explain how the proposed approach can be extended to covariate and concept shift.
- How is the proposed approach handling clients with minority data? The approach aims to punish free-riders but it might mistakenly punish minority clients, in particular by offering a noisy model
- Please add the dataset name and dirichlet parameter to the figures to improve readability.
- What kind of "real" applications would require this incentive scheme?

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
The paper introduces an incentive mechanism for federated learning, addressing key issues like the free-rider problem and the lack of realistic incentives. The approach is well-motivated, theoretically solid, and supported by experiments demonstrating improvements over existing methods. However, some areas, such as more comprehensive literature reviews in related work, practical implementation details, and additional ablation studies, could further strengthen the work.

### Strengths
1. Well-written: The paper is clear and well-structured.
2. Solid Theoretical Analysis: The theoretical analysis and proofs are strong and well-supported.

### Weaknesses
1.	Free-rider problem has been widely studied in FL settings, such as [1], and literature in its related works. In addition, previous studies of mechanisms for FL-related scenarios, such as crowdsourcing, can be suitable and easily adapted to FL settings.
2.	Achieving the goals of this paper seems to require knowledge of the data amount on each device. However, in the context of privacy-preserving machine learning, is it essential for FL clients to disclose their data sizes? This raises the question of whether the proposed approach truly aligns with the notion of “REALISTIC MECHANISMS” as suggested in the title.
3.	Including well-organized source code for the experiments would enhance the paper's reproducibility and allow reviewers to verify specific details.

### Questions
1. Are some ablation studies missing, such as examining performance under different client numbers or aggregation algorithms? （A mini Question)

### Soundness
3

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
3

### Summary
This work proposes a federated learning mechanism to incentivize data contribution and device participation. Building on the work of [1], this paper further allows more realistic settings such as non-linear mapping between utility and model accuracy, non-iid local data distribution (to some extent), preventing data sharing, and modeling of server utility.

### Strengths
- The mapping from the model accuracy to utility is non-linear, which renders it more realistic.

- Server utility is explicitly modeled, which has not been widely explored in previous research.

### Weaknesses
 - In calculating server accuracy, it’s unclear why Assumption 3 holds, especially if local accuracies vary significantly across devices. The assumption that the server's accuracy is a simple aggregate of local accuracies does not account for the complexities of non-IID data distributions and varying device capabilities, which could lead to a biased server model.

- The study aims to address a cross-device setup; however, the experiments involve only 16 devices, which somewhat limits the persuasiveness of the empirical results. The limited number of devices does not adequately represent the scale and heterogeneity of real-world federated learning scenarios, where thousands or millions of devices might participate. This raises concerns about the generalizability of the findings.

- The comparison of utilities in Figure 3 seems unfair. For the non-linear and linear methods, agents’ utilities are distinct functions of model accuracy, meaning that even with the same model accuracy, their utilities would differ. Comparing utilities directly without accounting for the different utility functions makes it difficult to draw meaningful conclusions about the effectiveness of the proposed method.

- Typo line 412: incentives -> incentivizes

### Questions
- The authors claim that the work does not involve data sharing, but $c_im_i$ formulation is the same as [1]. Does this imply that the analysis from [1] can readily be extended to cases without data sharing?

- In Figure 4, data contribution from non-linear RealFM in MNIST case goes to 10^8 magnitude, while it is 10^4 for Cifar10 case. I find this unreasonable, as Cifar10 is a harder task and more data will be helpful. This has something to do with the chosen phi function, where utility can go to infinity when accuracy is close to 1 (which is the case for easier tasks).

[1] Karimireddy et al. Mechanisms that Incentivize Data Sharing in Federated Learning

### Soundness
3

### Presentation
2

### Contribution
2
