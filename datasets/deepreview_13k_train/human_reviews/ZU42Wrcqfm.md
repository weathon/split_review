# FedSMU: Communication-Efficient and Generalization-Enhanced Federated Learning through Symbolic Model Updates

- Decision: Reject
- Scores: 5, 8, 5, 5

## Abstract
The significant communication overhead and client data heterogeneity have posed important challenges to current federated learning (FL) paradigm. Most compression-based and optimization-based FL algorithms typically focus on addressing either the model compression challenge or the data heterogeneity issue individually, rather than tackling both of them. In this paper, we observe that by symbolizing the client model updates to be uploaded (i.e., normalizing the magnitude for each model parameter at local clients), the model heterogeneity can be mitigated that is essentially stemmed from data heterogeneity, thereby helping improve the overall generalization performance of the globally aggregated model at the server. Inspired with this observation, and further motivated by the success of Lion optimizer in achieving the optimal performance on most tasks in centralized learning, we propose a new FL algorithm, called FedSMU, which simultaneously reduces the communication overhead and alleviates the data heterogeneity issue. Specifically, FedSMU splits the standard Lion optimizer into the local updates and global execution, where only the symbol of client model updates commutes between the client and server. We theoretically prove the convergence of FedSMU for the general non-convex settings. Through extensive experimental evaluations on several benchmark datasets, we demonstrate that our FedSMU algorithm not only reduces the communication overhead, but also achieves a better generalization performance than the other compression-based and optimization-based baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces FedSMU, a federated variant of the Lion optimizer, designed to address communication efficiency in federated learning (FL). The FedSMU algorithm uses the Lion optimizer's sign-based updates, reducing client-to-server communication costs to 1-bit per parameter. The paper also provides a convergence analysis for both FedSMU and the original Lion optimizer, and compares to other compression-based methods.

### Strengths
1- Compared to FedLion, the design of FedSMU is better suited for FL, specifically in handling communication constraints. FedSMU has a communication cost of only 1-bit per parameter from the client to the server. On the other hand, FedLion incurs even higher communication costs than FedAvg and shows weaker performance in practice compared to FedSMU.

2- By sending only 1-bit per parameter, FedSMU balances the magnitude of updates between different clients, which is beneficial for handling data heterogeneity. The paper also provides strong motivation for this choice.

3- In experimental evaluations, FedSMU performs better than other communication-efficient FL methods, especially in settings with high data heterogeneity.

### Weaknesses
Major: Missing related work: FedSMU is really similar to the Distributed Lion Training [1]. Technically, it's the same method with standard changes (Local steps and Partial client participation). This makes the novelty of the paper limited. Additionally, this paper (in addition to averaging) also considers majority vote for aggregating the client updates, and it seems that it works better in practice.

[1] Liu, Bo, et al. "Communication Efficient Distributed Training with Distributed Lion." arXiv preprint arXiv:2404.00438 (2024).

----------------------
1- The paper acknowledges that clients in FL can dynamically join or leave. However, the FedSMU algorithm requires clients to maintain and track their momentum state, which may introduce practical limitations in scenarios with dynamic participation. Specifically, if a client only participates once, the stored momentum will be stale and potentially detrimental.

2- Given the comparison with SCAFFOLD on CIFAR-10 and Shakespeare datasets, benchmarking on additional datasets and model architectures could strengthen the paper’s results. The current evaluation lacks diversity in both data and model complexity, limiting the generalizability of the findings. For instance, performance on a more complex dataset like Tiny ImageNet or with a transformer architecture would be valuable.

3- Additional experiments comparing methods based on both communication cost and the number of rounds would provide clearer insights into practical efficiency. Comparisons with SCAFFOLD, FedAvg, etc., based on communication cost would be helpful. Comparison in terms of the number of rounds  vs compression-based method and non-compression-based methods also missing. Communication cost is an important factor, however the number of rounds in which clients need to compute gradients is also important. The paper should provide a more comprehensive analysis of the trade-offs between communication efficiency and convergence speed.

4- Given the paper’s claims regarding generalization improvement, experiments that explicitly measure generalization (e.g., by comparing validation performance at similar training error levels) are needed to substantiate this claim further. The current results do not clearly isolate generalization ability from training performance.

### Questions
1- Can you plot the accuracy vs MU for different methods, checkpoints and dataset to better show the correlation between them? 

2- How does your model compare to other methods in terms of wall-clock time? (A balance for comparing number of rounds needed vs communication costs.)

3- Can you include compression for server-to-client communication as well? A comparison to some baselines can be helpful.

4- Can the convergence bound improve with more number of local steps and more participation per round?  

5- Can this method improve over SCAFFOLD in CIFAR-10 and Shakespeare with more communication (more rounds or other variant like FedSMUMC)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Authors:
- Develop a compression-based FL algorithm called FedSMU. 
- FedSMU uses the sign operation to achieve a 1-bit compression and thus greatly saves the communication cost.
- We conduct a convergence analysis of FedSMU under the general non-convex settings and dependence is optimal for such assumption in terms of T.
- Authors conducted a series of experiments to demonstrate the superiority of FedSMU

### Strengths
- originality: Handling signed information is interesting for distributed training from a theoretical perspective.
- quality: The text is written pretty in quality form.
- significance: Results are interesting for theoretical advancements.

### Weaknesses
In this section, I provide constructive and actionable insights on how the work could improve. However, they are not so critical:

**Minor Comments:**

q1: **Line 60:** The statement "However, most of these algorithms will lose a certain amount of information due to compression, resulting in a decrease in accuracy" needs clarification. If the authors mean this is true for a specific number of rounds/epochs, then it is accurate. However, in general, variance-reduced techniques do not necessarily lead to a loss of accuracy. The convergence guarantees for these methods are comparable to those without compression, although they may require more rounds. The authors should consider discussing the convergence rates relevant to specific situations.

q2: **Line 64:** The phrase "mitigate the client variance" lacks clarity. It would be beneficial to specify what type of variance is being addressed—variance in model updates, loss functions, or another context.

q3: **Line 68:** The claim "Additionally, it remains unknown whether these optimization-based algorithms are compatible with the current compression techniques" is misleading. If there exists a theorem demonstrating compatibility, then it is established. Typically, these theorems analyze convergence behavior on the training set, and generalization aspects may not be straightforward. Thus, stating that compatibility "remains unknown" is inaccurate, as compression techniques are an integral part of training algorithms in Federated Learning.

q4: **Line 85:** The term "Lion optimizer" is not properly referenced in the Introduction section.

----

**Middle Comments:**

----

q5: **Line 300:** The statement "FedLion requires the additional transmission of the full-precision momentum terms, resulting in a significantly higher communication cost compared to our FedSMU that only necessitates a 1-bit communication for each dimension of the model updates" lacks clarity regarding the necessity of momentum terms on the server side of Algorithm 1. 

q6: Can momentum terms be stored on the client side instead?

----
**Request for Discussion:**


q7: I suggest that authors elaborate a bit on why "sign" information 1-bit can be useful for practice or imagine scenarios when it can be useful for society.

The service information for communication includes plenty of headers, for instance:
- The Ethernet header has 14 bytes for the header.
- IPv4 has 20 bytes header. 
- TCP has header 20 header.

Problem-1: 1 bit can not be transferred physically, only 1 byte (approximately).
Problem-2: Even with transferring 1 byte you will need to transfer 54 bytes of headers.

### questions:
 **Major Comments:**

Q1: I can not find "Supplementary Material" and I can not find "Link for code". Without this, I can not reproduce experiments. Please provide it.

Q2: Line 10: The statement "While biased compression with a certain degree of information loss may cause a slight decrease in model performance" is incorrect. Refer to methods like MARINA, DIANA, and EF21 for comparison do not have any inherited limitations with using compression. Please clarify your statement.

Q3: Line 309: The three standard assumptions stated in the analysis are weak and not universally applicable to a range of non-convex objective functions. See references to EF21 and MARINA for examples of relaxed analyses.

- Assumption 4.3 does not allow for the minimization of y=x^2/2 over R.
- Assumption 4.2 does not accommodate data-point subsampling.

I am asking the authors to elaborate on the weakness of assumptions for practical purposes.

Q4: Theorem 4.4: The convergence is established in terms of the $L_1$ norm, which is always greater than $L_2$. While your rates in terms of $L_1$ norm square are inversely proportional to $1/T$ you have a dependency of $d^2$, which becomes problematic.
Please elaborate more on the dependency on dimension. Your method is not Zero-Order to have a dependency on dimension (which for instance Convex Optimization setting has with the Zero-Order optimization class of Algorithms in terms of convergence to full gradient square https://arxiv.org/pdf/1312.2139, p.7)

Q5: State-of-the-art Methods for Top-K Compression: To my knowledge, the state-of-the-art method for Top-K compression is Error Feedback 2021, not FedEF-TopK. For reference, please see:
- https://arxiv.org/pdf/2106.05203
- https://arxiv.org/abs/2110.03294
- https://arxiv.org/abs/2402.10774

If you can for camera-ready make a comparison with EF21. It would be great. I believe all these Q1-Q5 are addressable.

Thanks for your work.

### Questions
**Major Comments:**

Q1: I can not find "Supplementary Material" and I can not find "Link for code". Without this, I can not reproduce experiments. Please provide it.

Q2: Line 10: The statement "While biased compression with a certain degree of information loss may cause a slight decrease in model performance" is incorrect. Refer to methods like MARINA, DIANA, and EF21 for comparison do not have any inherited limitations with using compression. Please clarify your statement.

Q3: Line 309: The three standard assumptions stated in the analysis are weak and not universally applicable to a range of non-convex objective functions. See references to EF21 and MARINA for examples of relaxed analyses.

- Assumption 4.3 does not allow for the minimization of y=x^2/2 over R.
- Assumption 4.2 does not accommodate data-point subsampling.

I am asking the authors to elaborate on the weakness of assumptions for practical purposes.

Q4: Theorem 4.4: The convergence is established in terms of the $L_1$ norm, which is always greater than $L_2$. While your rates in terms of $L_1$ norm square are inversely proportional to $1/T$ you have a dependency of $d^2$, which becomes problematic.
Please elaborate more on the dependency on dimension. Your method is not Zero-Order to have a dependency on dimension (which for instance Convex Optimization setting has with the Zero-Order optimization class of Algorithms in terms of convergence to full gradient square https://arxiv.org/pdf/1312.2139, p.7)

Q5: State-of-the-art Methods for Top-K Compression: To my knowledge, the state-of-the-art method for Top-K compression is Error Feedback 2021, not FedEF-TopK. For reference, please see:
- https://arxiv.org/pdf/2106.05203
- https://arxiv.org/abs/2110.03294
- https://arxiv.org/abs/2402.10774

If you can for camera-ready make a comparison with EF21. It would be great. I believe all these Q1-Q5 are addressable.

Thanks for your work.

### Soundness
3

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
4

### Summary
This paper proposed the FedSMU algorithm to reduce communication costs in federated learning optimization problems. By symbolizing local client updates, FedSMU balanced client contributions and prevented dominance by large updates for Lion optimizer. Theoretical analysis and experiments showed comparable convergence and better accuracy.

### Strengths
The paper addresses an important problem in FL and is easy to follow. The empirical results validate the effectiveness of the proposed method, and the authors also provide a theoretical analysis to support it.

### Weaknesses
 * I believe some descriptions in the paper need to be refined for greater precision. For instance, in Section 3, the statement, “when the number of local update steps is set to  $K=1$ , the entire federated learning process reduces to the standard Lion algorithm,” is somewhat misleading. Even with $K=1$ , there is still a slight mismatch between the standard Lion algorithm and the proposed FedSMU.

* Remark 4.5 is somewhat confusing. The authors state, "we use a 1-bit quantization compression method. If a higher-bit compression (e.g., $\alpha$-bit) is used, the additional coefficient α will further slow down the overall convergence rate." This conclusion seems non-intuitive and not straightforward, as there is no clear indication in the theorem of how the convergence rate is influenced by $\alpha$. Typically, using higher-bit compression results in less compression loss, which would suggest improved performance rather than a slower convergence rate.

* It is unclear to me why $\tau_{\max}$ is used as an indicator for studying partial participation settings. Could you provide the practical value of $\tau_{\max}$ used in your experiments? Is there a specific reason for choosing this $\tau_{\max}$ indicator instead of the more common “sampling ratio $n/m$” (sampling $n$ out of $m$ clients), aside from practical considerations? It seems that in the experimental section, the participation ratio is also used.

* Given that Lion is an adaptive optimization strategy, it is important to discuss and compare it with other adaptive optimization methods, particularly those focused on communication efficiency, such as [1] or communication-efficient versions of AdamW in FL.

* The convergence rate appears to be unrelated to $\gamma_2$. After briefly reviewing the proof in the appendix, it seems that the authors assume  $|\gamma_2 x_t^j| \leq 1$. This is an uncommon assumption in FL optimization (or even in general optimization). Could you provide more details or clarification regarding this assumption?

* Some formatting could be improved: for instance, the scaling of Figure 1, the presentation of $\min$ in equation 1, and the $\min$ and $\max$ in Theorem 4.4.
* It would be helpful to specify the model (e.g., CNN or ResNet) in the captions or when describing figures/tables, as it can be unclear which model was used for the results.

### Questions
* The convergence rate appears to be unrelated to $\gamma_2$. After briefly reviewing the proof in the appendix, it seems that the authors assume  $|\gamma_2 x_t^j| \leq 1$. This is an uncommon assumption in FL optimization (or even in general optimization). Could you provide more details or clarification regarding this assumption?

* Some formatting could be improved: for instance, the scaling of Figure 1, the presentation of $\min$ in equation 1, and the $\min$ and $\max$ in Theorem 4.4.
* It would be helpful to specify the model (e.g., CNN or ResNet) in the captions or when describing figures/tables, as it can be unclear which model was used for the results.

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
4

### Summary
This paper presents a new FL algorithm, FedSMU, that leverages a 1-bit compression and a weight decay strategy with the goal of achieving both communication reduction and improved generalization performance. The proposed algorithm leverages the concept of the Lion optimizer, along with a convergence analysis. The paper also presents numerical experiments of FedSMU, comparing its performance with various FL algorithms by varying degrees of client participation ratios and data heterogeneity using CIFAR-10, CIFAR-100, and Shakespeare datasets, with CNN and RNN models.

### Strengths
- The paper introduces an interesting metric "Magnitude Uniformity" to measure heterogeneity in training, which is effectively used to motivate the proposed method through the numerical results.
- The proposed method integrates the Lion optimizer to enhance communication efficiency, showing significant improvements over FedLion, which is based on a similar concept.
- The proposed method demonstrates superior performance compared to other methods, particularly under low participation rates (Table 4).
- The paper provides clear empirical demonstrations of the impact of client participation rates and data heterogeneity on the generalization performance of FedSMU.

### Weaknesses
 - The convergence result is dependent on the upper bound of the gradients, which is not the case, for example, in the convergence result from FedLion. Moreover, the justification for Assumption 4.3 is weak or even irrelevant to the context of sign-based methods. The assumption requires a bound on the gradients and momentum terms, which is a strong assumption and may not hold in practice, especially with the use of sign-based compression, where gradients can vary significantly in magnitude. This assumption limits the applicability of the theoretical results.
- The theoretical and experimental results seem disconnected. As discussed in Section 4, the convergence may be affected by the model dimension and the maximum participation intervals, which are not demonstrated or discussed in the experimental section. Instead, the experimental section focuses only on demonstrating the performance of FedSMU. There is a lack of direct empirical validation of the theoretical claims regarding the impact of model dimension and participation intervals on convergence. The experimental section should include results that directly support the theoretical analysis.
- The experimental results are difficult to compare across different settings. For instance, the experiments with CNN used client participation rates of 10% and 3% with 100 clients, whereas those with ResNet18 used 30% and 10% with 10 clients. The impact of model sizes could be demonstrated more effectively if consistent experimental settings were used for CNN and ResNet18, as shown in Tables 2 and 3. The inconsistent settings make it difficult to draw meaningful conclusions about the performance of the algorithm across different model architectures and scales. A more controlled experimental setup is needed to isolate the effects of different parameters.
- The definition of generalization and its corresponding performance metric are not clearly defined. The paper lacks a precise definition of what is meant by generalization performance. It is unclear whether the authors are referring to performance on a held-out test set or some other measure of generalization. The lack of a clear definition makes it difficult to interpret the experimental results.
- Fed-LocalLion and Fed-GlobalLion algorithms are arbitrarily devised by the authors, and the ablation studies with these algorithms do not seem to provide meaningful insights into the proposed method. The motivation for these ablation studies is unclear, and the results do not provide a deep understanding of the proposed method. The comparison with these arbitrarily devised algorithms does not offer a strong justification for the design choices of FedSMU.

### Questions
1. What is the definition of generalization performance?
1. Regarding Remark 4.6, FedLion seems to provide the relevant convergence rate for the Lion optimizer, even under weaker assumptions. Please confirm that.
1. The large model used a 30\% participation rate, whereas the other experiments used 10\% and 3\%. Could you clarify why these inconsistent settings were used? This inconsistency makes it challenging to compare the large model's performance with the smaller models. Please consider using the consistent experiment settings.
1. The performance of FedSMU with the large model appears marginal compared to SCAFFOLD. Therefore, the last sentence of Section 5.2.1 may not be accurate. Please confirm and clarify.
1. Could the authors include plots of SCAFFOLD in Figure 2? This may help illustrate the trade-off between performance and communication efficiency more effectively.
1. Which model was used in Section 5.2.2? Please specify for clarity.
1. Why was FedAvg chosen in Section 5.2.3 for benchmarking on data heterogeneity? Would SCAFFOLD not have been a more appropriate comparison?
1. The performance reported in Table 4 is very intriguing. Could you elaborate on why FedSMU works well with low participation rates?
1. The performance of FedLion (Table 4) also appears consistent across different participation rates. Could you explain these results? Are they possibly related to Lion optimizer?
1. There are duplicate references for Chen et al. 2024a,b. Please correct this duplication.
1. Typo: "smay till" should be corrected.
1. In Algorithm 4, the client initialization of $e_0^i$ does not seem necessary. Instead, $M_t$ should be initialized.
1. In Algorithm 5, the client initialization of $m_0^i$ does not seem necessary. Instead, $M_t$ should be initialized. The superscript $i$ in $M_{t-1}^i, M_t^i, G_t^i, U_t^i$ may be typos.

### Soundness
2

### Presentation
1

### Contribution
2
