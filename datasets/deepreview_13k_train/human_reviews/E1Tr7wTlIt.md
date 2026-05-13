# $\lambda$-SecAgg: Partial Vector Freezing for Lightweight Secure Aggregation in Federated Learning

- Decision: Reject
- Scores: 1, 3, 5, 5, 6, 1

## Abstract
Secure aggregation of user update vectors (e.g. gradients) has become a critical issue in the field of federated learning. Many Secure Aggregation Protocols (SAPs) face exorbitant computation costs, severely constraining their applicability. Given the observation that a considerable portion of SAP's computation burden stems from processing each entry in the private vectors, we propose Partial Vector Freezing (PVF), a portable module for compressing computation costs without introducing additional communication overhead. $\lambda$-SecAgg, which integrates SAP with PVF, "freezes" a substantial portion of the private vector through specific transformations, requiring only $\frac{1}{\lambda}$ of the original vector to participate in SAP. Eventually, users can "thaw" the public sum of the "frozen entries" by the result of SAP. To avoid potential privacy leakage, we devise Disrupting Variables Element for PVF. We demonstrate that PVF can seamlessly integrate with various SAPs and it poses no threat to user privacy in the semi-honest and active adversary settings. We include $7$ baselines, encompassing $5$ distinct types of masking schemes, and explore the acceleration effects of PVF on these SAPs. Empirical investigations indicate that when $\lambda=100$, PVF yields up to $99.5\times$ speedup and up to $32.3\times$ communication reduction.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper introduces $\lambda$-SecAgg, a secure aggregation protocol for federated learning (FL) designed to reduce computational and communication overhead through Partial Vector Freezing (PVF). This paper claims that by freezing and processing only a fraction of the private vector entries, the method significantly reduces the burden on the server and participating devices while ensuring all vector entries are eventually aggregated. To further enhance privacy, the paper incorporates Disrupting Variables Extension (DVE). The authors empirically demonstrate substantial performance gains in terms of speedup and communication reduction across various secure aggregation protocols.

While the paper presents an interesting method to reduce the overhead in secure aggregation, the privacy analysis in Section 4.1 is fundamentally flawed. The authors underestimate the information leakage from $y^{i}$, which compromises the claimed privacy guarantees.

### Strengths
1. This paper considers a timely and important problem in secure aggregation protocol to reduce computational and communication overhead.

### Weaknesses
1. Most importantly, the privacy analysis in Section 4.1, which claims no privacy leakage from $y^{i}$, is flawed. Although the paper asserts that no specific element of the original vector $x$ can be deduced directly from $y^{i}$, this does not mean there is no privacy leakage. In fact, $y^{i}$ reveals significant information about $x$. For example, in the case where $\lambda = 2$ and $x$ has two elements, the server can infer $x_1$ in terms of $x_2$ from $y^{i} = a_{11}x_1 + a_{12}x_2$. While $x_1$ cannot be fully determined without $x_2$, the conditional probability of guessing $x_1$ correctly is now $1/p$ instead of $1/{p^2}$. This reduction in entropy, $H(x)$, shows that $y^{i}$ contains valuable information, thus reducing privacy. The authors should revise the privacy analysis and clarify the impact of knowing $y^{i}$ on the security of the original vectors.

### Questions
Please see the comment in the weaknesses.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present a new system to improve the computational overhead of secure aggregation using a new approach called Partial Vector Freezing. This approach reduces the number of entries processed in the secure aggregation protocol, by projecting chunks of the client input vector onto a different space, and only aggregating $1/\lambda$ of the entries of each chunk securely and sending the rest of the entries in the clear. The server aggregates the entries from all clients and recovers the original input vectors by projecting the inputs back to the original space. The paper further bolsters privacy through the Disrupting Variables Extension, which applies noise calibrated for Local Differential Privacy to frozen vectors. Experimental results demonstrate substantial computation improvements compared to state-of-the-art secure aggregation protocols.

### Strengths
- The focus of privacy-preserving federated learning is a crucial topic
- Extensive evaluation that covers a wide range of existing secure aggregation protocols

### Weaknesses
 - The approach impacts the robust privacy guarantees traditionally upheld by state-of-the-art secure aggregation protocols. These protocols typically ensure that an adversary gains no additional information about the inputs of honest clients beyond what is inferred from the aggregated output. However, Partial Vector Freezing (PVF) significantly reduces this privacy. As pointed out by the authors, it is possible for the server to learn whether two clients have similar vector chunks. Although the authors propose a mitigation strategy through Local Differential Privacy to reduce the detection of exact matches, this measure does not fully mitigate the issue of input privacy. The noised client inputs may still leak partial information that allows the server to deduce similarities between inputs. Given this trade-off, the computational gains provided by PVF do not justify the notable privacy impact. For instance, in the context of PracAgg, the masking computation is relatively lightweight. It involves field operations and pseudorandom generator evaluations, typically implemented with efficient cryptographic functions like AES. Additionally, the more computationally intensive pairwise key agreements are independent of the vector size and remain necessary regardless of the implementation of PVF.
- Another concern is the soundness of the security proof presented in Theorem 1. Specifically, the claim that the protocol execution is indistinguishable from random simulation seems to be inaccurate. The distribution of Hybrid 1 is not indistinguishable from that of Hybrid 0, as the distribution of frozen vectors $y_i$ does not exhibit properties of uniformly sampled vectors. While the random vectors are sampled uniformly from $\mathbb{Z}_p$, the frozen vectors in the protocol are the actual inputs masked with centered Gaussian noise of bounded variance. This results in a non-uniform distribution over $\mathbb{Z}_p$ undermining the indistinguishability between the two hybrids. Furthermore, other parts of the security proof are incomplete.  For instance, in Hybrid 3, it is stated that the adversary-controlled clients $\mathcal{C}$ call the ideal functionality. However, in simulation-based proofs, it is typically the simulator, not the adversary, that has direct access to the ideal functionality. Clarifying this aspect would strengthen the proof’s rigor and ensure alignment with standard cryptographic practices.

### Questions
1. The baseline runtime figures for the secure aggregation protocols presented in Figure 1 and Table 1 appear notably higher than those reported in related literature. For instance, in the case of PracAgg with a vector length of 100k elements, Figure 1 shows a client runtime of 14 seconds and a server runtime of 140 seconds. In contrast, the original paper by Bonawitz et al. (2017) reports significantly lower runtimes for similar conditions, with client runtimes around 300 milliseconds (Figure 6a) and server runtimes at most 5 seconds (Figure 7a). Could you clarify the reasons for this discrepancy in runtime comparisons?
2. Could you provide a more detailed analysis of the privacy impact of your scheme, particularly focusing on the amount of differentially private noise that would be sufficient to mitigate privacy risks effectively? A clearer discussion on how the noise level was determined and its implications on both privacy and utility would be valuable.

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
This paper introduces a novel method called λ-SecAgg, which integrates a module named Partial Vector Freezing (PVF) into Secure Aggregation Protocols (SAPs) for federated learning. The main goal of this method is to reduce the computational overhead by “freezing” most of the entries in user update vectors, allowing only a fraction (1/λ) of the original vector to be processed through secure aggregation. The frozen entries can later be “thawed” to recover the full aggregated vector, ensuring that no information is lost in the final aggregation. Additionally, the paper proposes a Disrupting Variables Extension (DVE) that enhances privacy by adding noise to the frozen entries using Differential Privacy (DP). The authors perform extensive empirical evaluations across seven baselines, demonstrating that PVF can achieve up to 99.5× speedup and 32.3× communication reduction without compromising user privacy or security.

### Strengths
Innovation: The concept of freezing and unfreezing vector entries in the context of secure aggregation is very novel. This approach effectively reduces the computational burden on SAP, which has been a significant bottleneck in real-world federated learning applications, especially for large-scale models such as Large Language Models (LLMs).

Comprehensive Evaluation: The authors evaluate their approach on seven different baselines covering various secure aggregation protocols (e.g., homomorphic encryption-based, SMPC-based, mask-based). The experimental results show substantial improvements in computation time and communication cost.

Privacy and Security: The paper proves the privacy guarantees of λ-SecAgg under semi-honest and active adversary models through security analyses. In addition, the authors introduce extensions such as DVE, which further strengthens the privacy guarantees.

### Weaknesses
Clarity and readability: Although this paper presents a novel approach, some sections are dense and difficult to understand, especially the mathematical derivations and safety analyses. It is suggested that the authors could improve the readability of these sections by providing more intuitive explanations and breaking down the steps as much as possible. In addition, the readability of some diagrams and formulas (e.g., those in Sections 3 and 4) is too low, and it is suggested that the reader could improve them by simplifying them or providing more detailed explanations.

Impact of noise on accuracy: Although the paper claims that the impact of DVE (adding noise to DP) on accuracy is negligible, the experimental results on the loss of accuracy due to DP noise are not detailed enough. It is suggested that the authors can add relevant experiments for this part.

Scalability to Multiple Users: This paper focuses on performance improvements for single users and servers, but does not discuss scalability to multiple users. It is suggested that the authors validate the approach of this paper in the context of multiple simultaneous users, especially with respect to communication overheads and system latency.

### Questions
This paper presents a novel and practical approach to reduce the computational overhead of secure aggregation in federated learning by proposing λ-SecAgg with partial vector freezing (PVF). The strengths of the method lie in its innovative design, theoretical rigor and comprehensive evaluation, showing significant performance improvements. However, there are areas that could benefit from further clarification, particularly in terms of readability, real-world evaluation, and the impact of noise on accuracy. It is recommended that the authors consider the above comments to further refine and optimize the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper addresses the challenges of secure aggregation in federated learning, particularly the high computation costs associated with Secure Aggregation Protocols (SAPs). The paper introduces a novel approach called Partial Vector Freezing (PVF), designed to reduce computation without increasing communication overhead. In addition, the paper proposes the disrupting variable extension to PVF to support enhanced privacy. The extensive experiments show the effectiveness of the proposed proposal.

### Strengths
1. The PVF significantly compresses the length of the vector involved in SAP.
2. The disrupting variables extension method improves privacy, without the computational overhead.
3. The authors conduct extensive experiments

### Weaknesses
1. Lack of Novelty in the Proposed Solution:
While I appreciate the clarity and straightforwardness presented in your methodology, I am concerned about the apparent simplicity of the proposed solution. The approach, as described, seems to lack the level of innovation. The core idea of freezing parts of the vector before secure aggregation, while intuitively appealing, does not seem to introduce a fundamentally new concept. It would be beneficial to explore the theoretical underpinnings of this approach more deeply, perhaps by relating it to existing techniques in dimensionality reduction or sparse coding. A more detailed comparison with alternative methods, highlighting the specific advantages and disadvantages of PVF, is needed to justify its novelty. The paper should emphasize any novel insights or improvements that your solution offers beyond a straightforward application of vector freezing.
2. Informality in Security Analysis:
The security analysis section of your paper appears to be somewhat informal and lacks the rigor typically required for a comprehensive evaluation of a proposed system or method. The analysis does not delve into specific attack models or provide formal security proofs. For example, the paper should analyze how the disrupting variables extension method affects the overall security guarantees of the system. It is not clear how the magnitude and distribution of the disrupting variables are chosen and how they impact the privacy of the aggregated data. A more structured and detailed security analysis is essential to establish the trustworthiness and robustness of the proposed approach, possibly incorporating formal security proofs or simulations to demonstrate the effectiveness of your security measures against various attack scenarios.

### Questions
1. In practical applications, how should this value \lambda be determined?

2. Are there any fundamental differences between the aggregation method of k^i and that of y^i?

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
3

### Summary
This paper devises a portable module named \lamba-SecAgg for secure aggregation in federated learning. The authors also propose an extension involving disrupting variables to enhance privacy. Through extensive experiments, they demonstrate the efficiency of the proposed method, achieving up to 99.5× speedup and up to 32.3× communication reduction.

### Strengths
1.Theoretical proofs.
2.The experimental results demonstrate that PVF achieved 99.5 \times speedup and up to 32.3 \times communication reduction.

### Weaknesses
1. Writing/technical issues:
(1) In the Introduction section, the author methioed that "the minimal noise added by DP is insufficient to thwart attacks", yet they also suggest considering "DP in the extension for enhanced privacy." It remains unclear why DP is considered later if it's initially deemed insufficient. The specific types of attacks that minimal DP noise cannot defend against should be explicitly stated to justify this apparent contradiction. Furthermore, the mechanism by which DP is intended to enhance privacy in the extension, given its initial inadequacy, requires further clarification.
(2) The introduction of "compression-based techniques" in Figure 3 and Section 2 feels somewhat abrupt, primarily due to the lack of clarity in the classification of existing solutions outlined in the Introduction section. The criteria for categorizing methods into secure aggregation techniques and compression-based techniques are not well-defined. A more detailed analysis of the limitations of existing methods, particularly those that are not compression-based, would help readers better understand the specific niche and motivation for the proposed PVF. The connection between compression and secure aggregation should be made more explicit.
(3) The definition of adversary in the threat model is not very clear. Specifically, the adversary's knowledge, such as access to intermediate computations or specific user data, and their capabilities, such as the ability to collude or manipulate messages, are not adequately defined. A more precise definition of the adversary model is needed to properly assess the security guarantees of the proposed method. The assumptions about the adversary's resources should also be stated.
(4) Figure 4 is too abstract to understand. The specific operations and data transformations occurring at each stage of the process are not clearly depicted, making it difficult to grasp the core mechanism of the proposed method. A more detailed explanation of the figure's components and their interactions is needed.
(5) In Section 3.3, while discussing secure aggregation, it is noted that the requirements for data accuracy are relatively high. However, the introduction of DP typically involves adding noise to the data. It would be beneficial to clarify how the accuracy of the data can be maintained after noise has been added, particularly in the context of the freezing and melting processes. The specific mechanisms used to control the noise level and its impact on the final aggregation result should be explained in more detail, including the trade-offs between privacy and accuracy.

2. Experimental issues:
(1)The neural network architectures and datasets are not intruduced in the ‘Experimental settings’. The specific details of the models and datasets used, including the number of layers, activation functions, and data preprocessing steps, should be provided to ensure reproducibility and allow for a proper evaluation of the method's performance.
(2)The setting of (\lambda = 100) in some experiments requires further explanation. The rationale behind choosing this specific value, and its impact on the performance and security of the proposed method, should be discussed. A sensitivity analysis of this parameter would also be beneficial.
(3)The experimental validation, although comprehensive, is limited to specific neural network architectures and datasets. Its generalisability to other models and types of data may require further examination. The authors should discuss the potential limitations of the experimental setup and suggest future research directions to address these limitations.

### Questions
Please refer to the weakness above.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper studies how to reduce the computational cost in privacy-preserving federated learning (FL) with secure aggregation (SecAgg). SecAgg is a primitive that improves the privacy-utility trade-off in FL as it hides individual model updates sent to the server. However, most efficient applications require to mask each parameter of the model with random noise, incurring into a large computational cost if models are big. 

The current work proposes a technique that reduces the computational cost by only performing SecAgg to a subset of model parameters, while still recovering the (claimed to be) private aggregation of the entire model.

### Strengths
- Reducing the communication cost in privacy preserving ML an interesting topic.

- The presentation of the protocol is fairly clear.

### Weaknesses
 # Main Weaknesses 

The major weakness of the protocol is the **lack of any standard notion of security**. The protocol is based on the fact that revealing the undetermined system of linear equations $\breve{A}x = y$ where $\breve{A}$ and $y$ are public does not compromise the privacy of $x$. From a security point of view, letting the adversary gain the knowledge of $\breve{A}x$ is **completely unsafe**. A clear example is already given the detailed comments subsection below for certain choices of $\breve{A}$. 

Even if the paper proposes some defenses to avoid the most obvious threats in the choice of $\breve{A}$ (i.e. if the system of equations already directly exposes some coordinates of $x$), these defenses are only a minor improvement in the overall security. The protocol is in fact insecure for any $\breve{A}$. For example, consider that a party joins the aggregation protocol with a vector $x = (x_1, 0, \dots, 0)$ (i.e., a vector where $x_1$ is the only non-zero value). In this case, values of $\breve{A}x$ will always be multiples of $x_1$. Therefore, the claim of Theorem 1 does not hold: multiples of $x_1$ are *distinguishable* from uniformly random numbers, contrary to what is claimed in hybrid 1 ($H_1$) in the proof of Theorem 1 (Appendix D.1).  This renders the proof of Theorem 1 incorrect. 

The computational improvements of this protocol come from the insecure modification described above. This makes the protocol inapplicable. Moreover, the attempts to further "complicate" the linear equations by the presented enhancements also follow an unsafe methodology lacking proper proofs (see my detailed comments below). 

In addition to the above, the work ignores important lines of work in compression under privacy constraints (e.g. see [R1-R5] below) and differentially private-based aggregation (e.g., by the use of correlated noise [R6-R8]), directly related to the current contribution. 


# Detailed Comments 

- Page 2, Section 2: 
    - "Mask-based" approaches are an instantiation of "SMPC-based" approaches. 
    - "(i) improving the masking mechanism":  it is not clear what this means 
    - "Note that the security of FL remains an open issue": this is too broad and it is not clear what "security" means in this context
- Page 3: 
    -  Section 2: "However, their ability to prevent poisoning attacks is limited (Ma et al., 2023)": not sure how the reference is relevant here. Does  (Ma et al., 2023) provides evidence about this statement? 
    - Section 3,  "ultimately imposing significant computational burdens": "burdens" $\rightarrow$ "burden"; is this computational burden significant with respect to the computational cost of local training steps required by ML? 
- Page 4: 
    - Def 1: "... where $AK$ denotes the additional knowledge ..": so far no mention of "additional knowledge has been made", so it is not clear to what this refers. Also, it should be explicitly clarified that $rank(A, Ax)$ means the rank of the horizontal concatenation of $A$ and $Ax$. 
   - "... rendering it impossible to determine that specific confidential vector." this is an overly strong statement (at least if no additional context is given). Consider for example that $A$ equals the identity matrix. Indeed $\breve{A}x$ has infinite solutions (all possible values of the removed coordinate of $x$). However, almost all coordinates of $x$ will be revealed if $\breve{A}x$ is revealed. 
- Page 5, Sec 3.3: 
    -  "... even if some secagg entries are compromised": There is no motivation of the extra defense, explaining how these entries would be compromised. 
    - "complicating the relationships among entries and further enhancing privacy": This lacks a proof. Providing privacy by obscurity (i.e, providing an obfuscation technique without proving that indeed it reduces to hard problem for the adversary) is a bad practice in the field of security.


### Questions
Could please you address the points raised in "Main Weaknesses" above? 

In addition to these questions: 
- Could you illustrate in more detail what which masking operations of the compared SecAgg protocols do you avoid by the use of your proposal? It seems that either performing a matrix-vector multiplication or masking operations does not eliminate the dependency of the dimension of a vector $x$ in the computation. 

- If we compare the computational cost of the SecAgg protocol and the computational cost of a local training step for a client, what proportion of the computation the SecAgg overhead represents? How does this change for different models?

### Soundness
1

### Presentation
2

### Contribution
1
