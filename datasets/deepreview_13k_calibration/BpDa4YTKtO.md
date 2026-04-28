# Robust Locally Differentially Private Graph Analysis

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 3, 6, 8

## Abstract
Locally differentially private (LDP) graph analysis allows private analysis on a graph that is distributed across multiple users. However, such computations are vulnerable to poisoning attacks where an adversary can skew the results by submitting malformed data. In this paper, we formally study the impact of poisoning attacks for graph degree estimation protocols under LDP. We make two key technical contributions. First, we observe LDP makes a protocol more vulnerable to poisoning – the impact of poisoning is worse when the adversary can directly poison their (noisy) responses, rather than their input data. Second, we observe that graph data is naturally redundant – every edge is shared between two users. Leveraging this data redundancy, we design robust degree estimation protocols under LDP that can significantly reduce the impact of poisoning and compute degree estimates with high accuracy. We prove that our robust protocols achieve the optimal levels of accuracy and soundness via information-theoretic lower bounds. Finally, we evaluate our proposed robust degree estimation protocols under poisoning attacks on real-world datasets to demonstrate their efficacy in practice.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the problem of data poisoning attacks to graph data analysis under local differential privacy, specifically targeting the estimation of node degree distribution. Although the studied problem is important, the contribution is incremental, and the proposed solution, along with its theoretical analysis, contains flaws.

### Strengths
1. The studied problem is important. 

2. Extensive theoretical analysis is provided.

### Weaknesses
1. The graph data perturbation involved in this work does not satisfy LDP. This work is based on edge LDP, which protects the existence of an edge between any two users. In terms of adjacency vector, the sensitivity of an edge’s existence should be 2 bits. Thus, when applying RR to perturb that vector, the probability should be $\frac{1}{1+e^{\epsilon/2}}$, rather than $\frac{1}{1+e^\epsilon}$. In terms of degree perturbation, the sensitivity of an edge’s existence should be 2, as the edge connects to two nodes and affects the degree of both nodes. Thus, when applying Laplace noise, it should be $Lap(2/\epsilon)$, rather than $Lap(1/\epsilon)$. This issue has been widely studied in the literature [1-2].

[1] Liu Y, Wang T, Liu Y, et al. Edge-Protected Triangle Count Estimation under Relationship Local Differential Privacy. IEEE Transactions on Knowledge and Data Engineering, 2024.

[2] Ye Q, Hu H, Au M H, et al. LF-GDPR: A framework for estimating graph metrics with local differential privacy. IEEE Transactions on Knowledge and Data Engineering, 34(10): 4905-4920, 2022.

2. The contribution is incremental. The difference between input poisoning and output poisoning in the context of LDP has been thoroughly studied in the literature. In addition, it is unclear how the honest error differs from the malicious error. Can the authors provide a concrete example for illustration? 

3. The experimental evaluation needs to be improved. It is unclear what observation and conclusion can be made from Figure 4. The figure lacks clear labels and explanations of the axes, making it difficult to interpret the results. Furthermore, the specific attack scenarios used in the experiments are not clearly defined, making it hard to assess the practical relevance of the findings. The number of experiments seems limited, and it is unclear if the results are consistent across different datasets and parameter settings. 

4. The presentation needs to be improved. There are quite a few typos in the manuscript. Here are some examples. 
- In page 2, “upto” -> “up to”
- In page 4, “reponse” -> “response”
- In page 5, “In our first scenario, consider” -> “Our first scenario considers”

### Questions
Please refer to the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper explores the vulnerability of locally differentially private (LDP) graph analysis to poisoning attacks, where adversaries skew results by submitting malformed data. The authors highlight that LDP protocols are particularly susceptible to such attacks and leverage the natural redundancy in graph data to design robust degree estimation protocols under LDP. They propose a formal framework to analyze protocol robustness, focusing on accuracy for honest users and soundness for malicious ones. The paper introduces new protocols that significantly reduce the impact of adversarial poisoning and computes degree estimates with high utility. Comprehensive empirical evaluations on real-world datasets validate the effectiveness of these protocols. The study contributes to the understanding of poisoning attacks under LDP and provides practical solutions for more secure graph analysis.

### Strengths
The paper focuses on an interesting research question and builds on strong theoretical foundations, including information theory and differential privacy, to establish lower bounds and prove the efficacy of the proposed solutions.

### Weaknesses
My fundamental concern lies in that the practical significance of the paper is rather unclear. The paper gives an motivating real-world example, which involves degree collection on social networks. In practice, social networks often publicly display the number of followers or connections a user has, rendering the need for private degree aggregation obsolete. Furthermore, the paper does not clearly articulate the specific scenarios where the proposed LDP protocols for degree estimation would be necessary, especially given the existing literature on private network publishing. The distinction between aggregated degree calculation and network publishing is not clearly defined, making it difficult to assess the novelty and practical relevance of the proposed approach.

### Questions
If the major focus of the paper more targeted to aggregated degree calculation or network publishing?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces a systematic framework for analyzing poisoning attacks in Local Differential Privacy (LDP) protocols for graph degree estimation. The authors propose two key metrics: honest error and malicious error, to quantify the impact of adversarial manipulation on both honest users and overall estimation accuracy. Their analysis reveals that poisoning attacks are more effective when targeting randomized response mechanisms compared to direct input manipulation. The work contributes two novel attack vectors: degree inflation and degree deflation, providing a comprehensive examination of potential adversarial strategies. To counter these threats, the authors leverage the inherent redundancy in graph structures—specifically, the property that edges are naturally reported by both connected vertices—to develop two defensive protocols. The empirical evaluation encompasses both synthetic and real-world (Facebook) datasets of varying scales, demonstrating the effectiveness of their findings and proposed defenses. Their results provide important insights into the vulnerability of LDP protocols in graph statistics and offer practical approaches for enhancing robustness against poisoning attacks.

### Strengths
**Originality:**
The paper presents the first comprehensive study exploring poisoning attacks in LDP protocols for graph degree estimation. The work introduces several novel ideas. These include:
-Demonstrating that poisoning attacks on randomized responses (i.e. output of the noise addition required for LDP) are more effective than input data poisoning
- Leveraging edge-sharing properties between adjacent nodes for malicious user detection
- Developing a method to distinguish between LDP-induced and malicious inconsistencies
- Proposing solutions that exploit the inherent redundancy in graph edge reporting for attack mitigation

**Quality:**
The paper demonstrates technical soundness through:
- An appropriate mathematical formulation of the real-world graph degree estimation problem
- Rigorous analysis of dual sources of edge distribution inconsistency: LDP randomization and malicious manipulation
- Comprehensive parameter evaluation across privacy budget ($\epsilon$), accuracy error, malicious error, database size, and adversary size and bounds

**Clarity:**
The work presents its ideas through:
- Practical motivation grounded in real-world applications, particularly social network influence analysis (e.g., Mastodon)
- Systematic development of robust degree estimation protocols that address both malicious and honest errors

**Significance:**
The paper makes several significant contributions:
- Direct applicability to real-world scenarios of influencer detection and manipulation in social networks
- A good (but perhaps not comprehensive in terms of data sources) empirical validation using both synthetic and Facebook datasets
- Practical defensive measures for preventing adversaries from promoting malicious users as influential nodes

The work provides both theoretical insights and practical defensive measures against poisoning attacks in LDP protocols for graph analysis. The comprehensive parameter analysis and thorough experimental validation across multiple datasets demonstrate both the theoretical and practical significance of the contributions.

### Weaknesses
 **Writing and Technical Issues:**
- There is redundant wording in line 122, page 3: "distributed graphs and has been widely studied widely"
- The reference formatting lacks consistency throughout the paper. For instance: 
1. Author names are inconsistently abbreviated (e.g., "Xiaoyu Cao, et al." vs. full author lists)
2. Conference/journal names and their formatting vary (e.g., inconsistent capitalization and abbreviations)
3. In the current version, the latest reference is from the year 2022; The reference section could be strengthened by including recent (2023-2024) developments in LDP poisoning attacks, particularly works on LDP protocol robustness and defense mechanisms against output poisoning. This additional context would further highlight the paper's pioneering contribution to LDP-protected graph poisoning attacks. A list that is far from exhaustive is given below. Other references have been updated but not reflected as such: e.g., Li et al. (2022) on fine-grained poisoning attacks has appeared in a more final form at USENIX Security 2023.

**Figures and Visualizations:**
1. Figure Quality:
- Figures 3 and 4 are not provided in vector format, resulting in poor scalability and reduced readability when zoomed
- The font styles and sizes in subcaptions (a)(b)(c)(d) lack consistency across Figures 3 and 4, etc..
2. Experimental Design and Presentation:
- A limitation in the experimental design appears in Figure 4, where the varying database sizes (m=1332 vs m=1320) lack rigorous theoretical motivation. The authors' justification that these parameters "meet the asymptotic theoretical error bounds" requires more substantial analytical support to establish the connection between these specific numerical choices and the theoretical foundations.
- The choice of $\epsilon$ values (0.7 and 3.00) requires justification. It is unclear why these specific values were chosen, and how they relate to the practical application of the proposed methods. A more detailed explanation of the rationale behind these choices is needed, especially considering the range of possible values for $\epsilon$.
- Consider using other additional visualization methods for the comparative analysis, as it might better highlight the differences in some malicious errors and honest errors.

**References:**
1. Huang, Kai, Gaoya Ouyang, Qingqing Ye, Haibo Hu, Bolong Zheng, Xi Zhao, Ruiyuan Zhang, and Xiaofang Zhou. "LDPGuard: Defenses against data poisoning attacks to local differential privacy protocols." IEEE Transactions on Knowledge and Data Engineering (2024).
2. Sun, Xinyue, Qingqing Ye, Haibo Hu, Jiawei Duan, Tianyu Wo, Jie Xu, and Renyu Yang. "Ldprecover: Recovering frequencies from poisoning attacks against local differential privacy." arXiv preprint arXiv:2403.09351 (2024).

### Questions
**Venue Fit and Positioning:**
While the paper presents solid technical contributions in security and privacy, its fit with ICLR's focus on learning is not immediately clear. Privacy/security of ML is certainly on topic for ICLR, however it would be appreciated if the authors elaborate on their thoughts here, and whether they had considered a security/privacy venue. Given that  many cited works on LDP and poisoning attacks appear in security and privacy venues.

**Technical Clarifications:**
- The finding that "the rate of flagging is less aggressive for FB since it is a sparse graph" (line 508) is not readily apparent in Figure 3. Could the authors clarify this observation with supporting evidence?
- How does the computational complexity of the proposed protocols scale with very large graphs? Are there any limitations or performance bottlenecks?
- For the experiments comparing input poisoning and response poisoning, what informed the choice of different database sizes (m=1332 vs m=1320)? How do these specific values relate to the theoretical bounds?
- The paper uses an argument about the Bernoulli distribution to distinguish between LDP-induced and malicious inconsistencies. It would be appreciated if the authors might elaborate on the theoretical justification here; The sensitivity of this modeling choice to different graph topologies (beyond the tested Facebook and synthetic datasets) and different attack patterns. How might the results be affected by: networks with heterogeneous degree distributions, social networks exhibiting power-law connectivity, and graphs with varying density across different regions?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper continues a line of study on exploring the impact of poisoning attack in local differential privacy. In particular, they consider the task of estimating the degrees of each vertex under the widely used notion of edge-level DP, in which two graphs are considered neighboring if they differ in one edge. For the poisoning setting, they consider two types of attack. First is the input poisoning, where a malicious user falsify their underlying input. A stronger one is the response poisoning, where the adversary has access to the implementation of the LDP randomizer.

Under such settings, they first show that the navie implementation of the Laplace mechanism or the Randomized Response mechanism leads to almost trivial gurantee on the soundness. Then, by revealing the fact that the information are naturally redundant for degree estimation, they design a verification mechanism to improve the soundness under poisoning attack, and achieving $O(m(1+1/\varepsilon) + \sqrt{n}/\varepsilon)$ accuracy and soundness with a small failure probability, based on the randomized response mechanism. Finally, they combining the laplace mechanism and improve the the accuracy to logarithmic error for "honest" users.

### Strengths
1. The technical lemmas and theorems in this paper are clearly stated and correct.
2. The hybrid mechanism for reducing the error is interesting.

### Weaknesses
I agree that it is natural to consider the poisoning attack within the context of local DP, and the edge-level (global) differential privacy is a rather standard notion. However, I think using edge-DP in the local DP model is unusual. In particular, I agree that "the users do not explicitly share this information; rather, it is implicitly shared by the structure of the graph itself." My concern, however, is whether studying local differential privacy remains meaningful, given that the graph's structure may *already* "leak" information to other users within it.

In the last review process, I mentioned a typo in Appendix G.3 (in line 1325 of this version) that it should be $|L_i|\leq \frac{1}{\varepsilon}\ln \frac{n}{\delta}$ instead of $|L_i|\leq \frac{1}{\varepsilon}\ln \frac{\delta}{n}$. But the typo seems to be still exist in this version, so I worry that the authors did not tidy up their proofs carefully.

### Questions
The authors have answered my questions in the last review process.

### Soundness
3

### Presentation
2

### Contribution
2
