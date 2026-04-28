# FedGT: Identification of Malicious Clients in Federated Learning with Secure Aggregation

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
We propose FedGT, a novel framework for identifying malicious clients in federated learning with secure aggregation. 
Inspired by group testing, the framework leverages overlapping groups of clients to identify the presence of malicious clients in the groups via a decoding operation.
The clients identified as malicious are then removed from the model training, which is performed over the remaining clients. 
By choosing the size, number, and overlap between groups, FedGT strikes a balance between privacy and security.
Specifically, the server learns the aggregated model of the clients in each group\textemdash vanilla federated learning and secure aggregation correspond to the extreme cases of FedGT with group size equal to one and the total number of clients, respectively.
The effectiveness of FedGT is demonstrated through extensive experiments on the MNIST, CIFAR-10, and ISIC2019 datasets in a cross-silo setting under different data-poisoning attacks. 
These experiments showcase FedGT's ability to identify malicious clients, resulting in high model utility. 
We further show that FedGT significantly outperforms the private robust aggregation approach based on the geometric median recently proposed by Pillutla \emph{et al.} in multiple settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method based on group testing to combine identification of malicious clients in FL with secure aggregation, which provides a tradeoff between privacy and Byzantine robustness.

### Strengths
1.	The ideal of using group testing to enable Byzantine resilience with secure aggregation is interesting.

### Weaknesses
1.	As the core technical contribution is to shift the paradigm from testing individuals to testing groups, and no novel testing strategy is proposed, the reviewer feels that this paper fits better venues on security or coding, compared with ML venues.  The application of group testing to secure aggregation, while interesting, lacks significant novelty in the context of machine learning. The core idea of using a pre-existing group testing framework, without substantial modification or adaptation to the specific challenges of federated learning, makes the contribution incremental rather than transformative for the ML community.

2.	More background and context need to be provided about error correcting codes and the design of assignment matrix A. For example, why one needs to choose A with good distance properties and how to choose it. Readers who are not familiar with coding theory may find it difficult to understand. The paper needs to elaborate on the connection between the properties of the assignment matrix A (derived from error-correcting codes) and the performance of the group testing scheme. Specifically, the importance of minimum distance in the code and its impact on the ability to identify malicious clients should be explicitly discussed. The process of selecting appropriate codes, such as BCH or Reed-Muller codes, should also be explained with more detail, including the trade-offs involved in choosing different code parameters (e.g., code length, dimension, and minimum distance).

3.	Conventional linear block codes (defined by their generator matrices) are defined on finite fields, for which binary addition (or XOR) is used. However, in the context of group testing, the check node is evaluated using logical OR operation. It is not clear how conventional block codes can be directly used here as candidates for the assignment matrix. The paper does not adequately address the fundamental difference between the algebraic operations in coding theory (typically XOR over finite fields) and the logical OR operation used in group testing. This discrepancy raises concerns about the direct applicability of standard linear block codes for constructing the assignment matrix. The authors need to clarify how the properties of codes designed for error correction, which rely on algebraic structures, translate to the logical operations used in group testing, and whether this translation introduces any limitations or performance penalties.

### Questions
1.	In Figure 1(c), why FedGT outperforms oracle?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript proposes FedGT, a secure aggregation framework for detecting malicious clients in federated learning. FedGT classifies each client into several overlapping groups, enabling the server to predict the presence or absence of malicious clients within each group. This allows the removal of such clients from the training of the global model. By adjusting the group sizes, FedGT achieves a balance between security and privacy. In addition, the manuscript investigates targeted label flip attacks and untargeted label permutation attacks, comparing their performance with RFA and oracle methods across varying numbers of attackers. Experimental results demonstrate that FedGT effectively identifies malicious clients, reducing attack accuracy.

### Strengths
- This manuscript's focus on secure federated learning is crucial in federated learning studies. The manuscript is well-structured, presenting a clear and coherent flow of ideas, which enriches the readability and understanding of the content.
- The method presented in this paper is innovative, as it combines group testing and secure federated learning aggregation techniques. It treats the identification of malicious clients as a decoding process, where the defective vector is determined based on the known distribution matrix and test results.
- The paper evaluates the proposed FedGT method, focusing on its effectiveness in mitigating poison attacks and safeguarding client privacy.

### Weaknesses
 - The article's limitation in considering scenarios with a fixed number of clients (15 and 31) raises concerns about the scalability and performance of FedGT as the number of clients increases. Further investigation is necessary to assess the method's effectiveness in larger-scale scenarios and address potential challenges related to the size of the assignment matrix. Specifically, the decoding complexity of $\mathcal{O}(2^m)$, where m is the number of tests, poses a significant computational bottleneck as the number of clients grows, potentially limiting the practical applicability of the method in large-scale federated learning settings. The authors should provide a more thorough analysis of the computational costs associated with the decoding process and explore potential optimization strategies to mitigate these challenges.
- In a related work section, the authors mention that RFA performs less well than other robust federated aggregation schemes. So why not use these better performance schemes as comparison schemes for FedGT?
- In Figure 3, the top-1 accuracy of FedGT is inferior to RFA and Oracle when the number of attackers is small and only exceeds RFA when the number of malicious clients under the subgraph (c) of Figure 3 is 5, which challenges the validity of the method. The fact that FedGT only outperforms RFA when a substantial portion of clients are malicious raises questions about its effectiveness in more realistic scenarios with fewer attackers.
- The authors should consider a larger number of attackers. Especially when the number of clients is 31, the number of attackers is too small to prove the effectiveness of FedGT to resist the collusion of multiple attackers. The experiments with 31 clients only consider 6 attackers, which is a relatively small fraction and may not adequately represent real-world scenarios where a larger number of clients could be compromised. This limits the ability to assess the method's robustness against coordinated attacks.
- FedGT has more assumptions than a typical federated learning security aggregation algorithm. Prior knowledge includes the number of malicious clients and additional test sets, which weaken the contribution made in the paper. The requirement of knowing the number of malicious clients beforehand is a strong assumption that may not hold in practice. Furthermore, the need for an additional test set, which is not always available, restricts the applicability of FedGT in various real-world scenarios.

### Questions
- In Appendix E, the authors demonstrate that the privacy of the FedGT implementation is equivalent to that of the security aggregation scheme for r clients. However, it would be helpful to provide a more formal and detailed explanation of the specific definition of privacy.
- The choice of decoding method will affect the performance of FedGT. What is the basis or reason for choosing the Neyman-Pearson scheme? Does Neyman-Pearson's hypothesis accurately describe the problem of reality?
- In addition to the test set, FedGT uses an additional enhanced data set. However, the authors need to provide more clarity regarding the composition and role of this data set. Specifically, the authors should describe in more detail what the enhanced data set comprises and how it limits the application of FedGT.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors employ group testing to detect malicious clients in FL. In particular, they investigate both vanilla FedAvg and secure aggregation algorithms in different parameter settings of group sizes. They conduct a formal analysis of the effectiveness and privacy guarantees on the varying group sizes. In addition, the authors evaluate their testing method in several datasets in terms of efficiency, utility, and effectiveness.

### Strengths
1. Using group testing to detect malicious clients in FL seems new and effective.

2. The analysis and evaluation on the proposed method are comprehensive and thorough.

### Weaknesses
1. The cost (particularly the communication) of group testing seems quite high, scale with the number of groups.

2. The privacy consideration seems not sufficient. I am wondering if the model difference between two testing groups could reveal individual's updates. For example, if group A includes C1, C2, C3, and group includes C2, C3, then the difference of the two aggregated models could reveal the model updates of C1. This is a concern because even if the individual updates are not directly revealed, the server could potentially infer sensitive information about a client's data by observing the change in the aggregated model when that client is included or excluded from a group. The use of secure aggregation does not inherently prevent this type of differential privacy leakage, as the aggregation itself is still a linear operation that can be analyzed by the server.

### Questions
See my comments above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new scheme for defending against poisoning attacks in cross-silo FL under secure aggregation. The scheme uses optimal coding techniques to split the federated learning clients into possibly overlapping groups. Each group's models are securely aggregated into a single model the server observes. Each group's aggregated model is tested by the server separately on auxiliary data for maliciousness. This allows the server to detect the presence of malicious or severely out-of-distribution clients in each group and, from that, deduce the identity of the malicious clients based on their group participation patterns cleverly chosen by the server. Finally, the server removes the perceived malicious clients from the federated process. The scheme tradeoffs privacy and security by allowing different sizes of groups to be chosen by the server, which, thanks to the optimal coding scheme used, also corresponds to the effective secure aggregation size of the FL process. The authors show experiments on different datasets and models, demonstrating that the scheme can be effective at defending against malicious clients while ensuring the privacy of benign clients.

### Strengths
- Solves an important problem
- The proposed method is an interesting application of group testing theory.
- Encouraging results that such a method can work in this setting despite the simplistic instantiation of it
- The method can work even when applied only at a single communication round.
- Interesting connection between coding theory and privacy of secure aggregation

### Weaknesses
 - **Structure and Novelty of the submission:**   
There are three major components to this paper. First, the paper suggests the use of group-testing strategies to determine which clients are malicious in the context of the cross-silo FL setup with secure aggregation. In this context, the authors prove how overlapping test groups affect the overall client privacy, as secure aggregation is not commonly applied over overlapping groups. This part of the paper is novel and constitutes the biggest technical contribution of the paper. Then, the authors use optimal codes to determine an efficient way to group clients such that a chosen level of privacy is ensured while the decoding ( aka malicious client identification ) can work well. This is mostly based on prior work from coding theory and contains little to no technical novelty. Finally, the paper then applies the optimal detection strategy from [1] without any changes to the problem of malicious client identification. The paper does not give proper credit to [1], given that it essentially just applies the algorithm presented there and instead re-derives most of the work in Section 5. To this end, there is little to no novel technical contribution in that part of the paper either. One area where the paper could have expanded on [1] and could have provided a real technical contribution is instantiating the many choices of [1] to the FL problem considered. Unfortunately, the paper does very little of that as it takes the absolute simplest choice for a test, models the threshold $\Lambda$ as a tunable hyperparameter ( pretty much independent of the proposed FA/MD trade-off ), assumes $\delta$ is known ( something that even the authors agree is not a reasonable assumption ), and use embarrassingly simple $Q(t|s)$ model. All in all, therefore, the paper provides very little novel technical contribution, which is sad, as the idea of applying group testing to this problem seems interesting and promising.   
Structurally, the paper wastes Section 5 by re-deriving [1] without giving [1] the proper credit and also compromising the explanation of the decoding, as the space is not enough for a full explanation of the decoding method. This space would have been much better spent on explaining the instantiation of [1] to the federated setting, e.g., what coding scheme is used, what test is used, how is $Q(t|s)$ chosen, etc., which is currently done all over the place. Further, it would have been good if the paper explained the properties of this instantiation and why it makes sense in the federated case. For example, the paper could have explained what the chosen coding strategies guarantee in the context of the FL problem being solved, what their communication complexity is, and how reasonable a test based on additional validation data and known attack parameters ( such as the targetted classes and number of malicious clients ) is. 
- **The defense relies on unreasonable assumptions and introduces too many hyperparameters:**   
While the experiments provided in the paper suggest the proposed group testing strategies have the potential to constitute a good defense, the particular instantiation is unsatisfactory.   
In particular, in the main paper, the authors assume unrealistic knowledge by the defender, such as known $\delta$ and known target class in the targetted version of the attack. While $\delta$ is shown to be not that important in Figure 9, wrong $\delta$ should be the default setting in which all experiments are carried out, as it is the only way to carry out the attack in the first place. Providing experiments with known $\delta$ is fine for ablation purposes but nothing more. Moreover, the known target is also a big assumption, as if the test is carried out for multiple targets, this can introduce additional noise in the test and lower the presented results.  
Further, the added hyperparameters $\Lambda$, $p$, and $\rho$ are hard to tune in practice. In particular, choosing $\Lambda$ heuristically depending on the setting, is hard and only possible through several re-trainings of the model. This is caused by the author's choice to tune $\Lambda$, which is an uninterpretable parameter in $(-\infty,\infty)$ to which the results are very sensitive, instead of $\Delta'$, which can be interpreted as a tradeoff between FA and MD. Further, I find the chosen model of $Q(t|s)$ which only depends on a single $p$ (the probability of error), too simplistic and hard to guess. I would suggest the authors instead at least choose $Q(t|s)$ as a probability distribution of the hamming distance between $t$ and $s$. This will at least account for the fact that individual tests can fail separately. Finally, $\rho$ is likely to be dependent on the heterogeneity level and complexity of the problem and might also be hard to tune.
- **Current experimental results are not strong enough:**   
Despite the multiple hyperparameters introduced by the authors, the method still produces results that, in many cases, do not beat the baseline the authors themselves provide( [2] ). This is especially visible in Figures 4 and 5 in the Appendix, where the authors' method consistently performs worse in simple settings like MNIST. It seems that the proposed model, as it is, is mostly capable of beating [2] in heterogeneous settings where targetted attacks with known targets are applied. While this is an important setting that is worth solving separately, this is a clear drawback of the method that is not discussed by the authors. If this is where the method really works better than alternatives, the whole paper needs to focus on this setting and explain why this setting is favorable to their method ( or unfavorable for other methods ). Further, to allow realistic apples-to-apples comparisons, as mentioned above, authors should remove the known target and $\delta$ assumptions (which I assume are not needed by [2]) and discuss how many clients are being securely aggregated by [2]. If the experiments for [2] aggregate all clients ( which I suspect is the case ), then the numbers are even worse for the proposed method, as [2] is in the "most private" setting where security is harder to achieve and yet still beats the proposed method regularly.
Finally, another concern regarding the results is the fact the method seems to affect more clean accuracy compared to [2] and even the no defense ( according to Tables 1-3 ). This might suggest that good defense properties demonstrated in the paper are currently achieved on the back of too-high FA rates, tanking the clean performance. 
- **Runtime concerns:**
The authors say in the main paper repeatedly they focus on the cross-silo FL setting which they define to be up to 100 devices. Yet, in their experiments, the authors only use 15, and in the scaling experiment in Appendix J, they claim they do not even scale to 31 when some more precise encodings are used. This needs to be explicitly discussed in the main paper, but also severely jeopardizes the applicability of the proposed algorithm.
- **Other:**
1. The discussion on communication complexity needs to be at least partially moved to the main paper. The authors keep claiming their communication complexity as an important contribution, but unless one reads the appendix, they do not even know what the communication complexity of this and baseline models are.
2. In all experiments, provide information on what the FA and MD rates are. Further, provide experiments where you change $\Lambda$ and show how this affects FA and MD rates and how it affects the attacker's accuracy and the model's clean accuracy.
3. Make explicit in **the main paper** that the current methodology works only for data poisoning and not model poisoning. ( Essentially bring the "**Beyond data poisoning**" point from Appendix L to the main paper )
4. If the authors plan on keeping Sec. 5, which I do not recommend, they should at least provide some justification for the forward and backward formulas. 
- **Nits:**
1. The last paragraph on page 3 does not explain when a test is positive ( i.e. is it when the group has a malicious client or when there isn't ). Add this to the definition
2. The $s=d \vee A^T$ notation, when first introduced, is confusing if the reader is unfamiliar with the group testing literature. Maybe explain that this is matrix multiplication where the dot product uses "ands" for multiplication and "ors" for additions.

### Questions
- Can the authors provide an additional experiment where they change $\Lambda$ and show how this affects the FA and MD rates and how it affects the attacker's accuracy and the model's clean accuracy? Which is more detrimental for the performance of FedGT - high FA or high MD ratios?
- Can the authors explain why the CIFAR10 attack success goes down even without defense in Figure 4 ?
- Can the authors provide a linear scale version of Figure 4? Log scale in the attacker's accuracy both makes it hard to read and also obfuscates the results, which are not naturally log distributed. 
- Can the authors provide experiments where the defender does not know the targets for the targeted attacks?
- Can the authors explain how many clients are securely aggregated by [2] in their experiments?
- Can the authors provide runtimes of the method for different numbers of clients and encodings? Can the authors provide a worst-case or average-case runtime analysis (in terms of big-O notation)?

All in all, this paper has the potential to introduce a very interesting defense mechanism with good performance and interesting properties. However, it does not do any of this. It does not properly instantiate the algorithms used in the federated setting, as it chooses super basic tests and sets everything else to impossible to obtain in practice hyperparameters. Possibly due to this, the results on the defense side are underwhelming, even when the comparison is done in a very favorable way to the proposed method by giving more information to the defender than typically assumed while also comparing to a method that cannot benefit from the trade-off described in this paper in terms of security-vs-privacy. Further, the method seems to be very computationally expensive to the server in cases where more than a handful of clients are available, and the clean accuracy is sometimes severely penalized possibly due to a high FA ratio.


[1] Gianluigi Liva, Enrico Paolini, and Marco Chiani. Optimum detection of defective elements in non-adaptive group testing. In Annu. Conf. Information Sciences and Systems (CISS), Baltimore, MD, 2021.   
[2] Krishna Pillutla, Sham M. Kakade, and Zaid Harchaoui. Robust aggregation for federated learning.
IEEE Transactions on Signal Processing, 70:1142–1154, 2022.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
