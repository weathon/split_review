# On Differentially Private Federated Linear Contextual Bandits

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
We consider cross-silo federated linear contextual bandit (LCB) problem under differential privacy, where multiple silos (agents) interact with the local users and communicate via a central server to realize collaboration while without sacrificing each user's privacy. We identify three issues in the state-of-the-art: (i) failure of claimed  privacy protection and (ii) incorrect regret bound due to noise miscalculation and (iii) ungrounded communication cost. 
To resolve these issues, we take a two-step principled approach. First, we design an algorithmic framework consisting of a generic federated LCB algorithm and flexible privacy protocols. Then, leveraging the proposed framework, we study federated LCBs under two different privacy constraints. We first establish privacy and regret guarantees under silo-level local differential privacy, which fix the issues present in state-of-the-art algorithm.
To further improve the regret performance, we next consider shuffle model of differential privacy, under which we show that our algorithm can achieve nearly ``optimal'' regret without a trusted server. 
We accomplish this via two different schemes --  one relies on a new result on privacy amplification via shuffling for DP mechanisms and another one leverages the integration of a shuffle protocol for vector sum into the tree-based mechanism, both of which might be of independent interest. Finally, we support our theoretical results with
numerical evaluations over contextual bandit instances generated from both synthetic and real-life data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies the problem of differentially private federated linear contextual bandits. Especially, it first identifies the potential privacy leaking from the adaptive communication strategy adopted in previous works, and the incorrect regret bound. To resolve these issues, this work proposes the Private-FedLinUCB framework, which can flexibly enable both silo-level local DP and shuffle DP. Especially, the shuffle DP guarantee is achieved via two different approaches. Theoretical analyses demonstrated the provable efficiency of the proposed framework. In particular, under SDP, the centralized performance can be approached.

### Strengths
- This work identifies the existing issues in the previous study on differentially private federated contextual bandits, which I believe is valuable. Especially, since adaptive communication schemes are widely adopted in studies of federated contextual bandits, it is important to highlight its potential risk of privacy leaking.

- This work nicely combines DP with federated contextual bandits, where the techniques, especially, two types of approaches to obtain shuffle DP, may be of interest for future studies in this line.

- The overall presentation is satisfactory and the study is thorough and complete. Theoretical results are sound based on my understanding.

### Weaknesses
 - The discussion from federated LDP to SDP is a bit unsmooth in my mind. From the reading, it seems that the authors cannot remove the additional $M^{1/4}$ gap from centralized performance and then the focus is turned to a slightly weaker DP notion of SDP (instead of studying whether the gap can be closed in LDP). I would suggest the authors first justify both DP notions in federated contextual bandits (especially SDP), and then state their corresponding results. Specifically, a more detailed explanation of why the $M^{1/4}$ factor arises in the LDP setting and why it is difficult to remove would be beneficial. Furthermore, the practical implications of using SDP over LDP in this context should be discussed, as SDP provides a weaker privacy guarantee. A concrete example or scenario where SDP is more appropriate than LDP in federated contextual bandits would help clarify this choice.

- Related to the first point, it would be nice to add some discussions on whether the $M^{1/4}$ gap from centralized performance can be closed; otherwise, the significance of the result is hard to measure. It is unclear if this gap is inherent to the problem or an artifact of the proposed algorithm. A discussion of potential lower bounds or theoretical limitations would be valuable to understand the optimality of the proposed method. If the gap cannot be closed, it would be important to explain why, and what fundamental challenges prevent achieving better performance under LDP.

- In terms of the DP techniques, I understand that there are many different choices and this work adopts two certain ones. It would be nice to clarify whether the adopted ones are necessary or if there are other feasible choices. Specifically, a discussion of the trade-offs between different DP mechanisms, such as Gaussian noise versus other noise distributions, or different aggregation protocols, would be beneficial. The authors should explain why the chosen techniques are suitable for this specific problem and if other alternatives could offer better performance or privacy guarantees. For example, are there specific properties of the chosen mechanisms that are crucial for the theoretical analysis or practical implementation?

- The fixed batch size selection potentially can be improved. Although performing adaptive communication protocol is no longer feasible, it might still be a good choice to have the batch length exponentially growing (as in many low-switching bandit studies) instead of being a fixed one. The authors should provide a more detailed justification for using a fixed batch size, especially considering that adaptive batch sizes have been shown to be effective in similar bandit settings. A discussion of the potential benefits and drawbacks of using an exponentially growing batch size in this context would be valuable. For instance, could an exponentially growing batch size lead to improved regret bounds or better privacy-utility trade-offs?

- A recent work [R1] studies a different kind of DP notion in federated contextual bandits. It would be nice to include and discuss it.

### Questions
I would love to hear the authors' opinions on my concerns in the weakness part. If I missed or misunderstood anything, please feel free to let me know.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers silo-level LDP and SDP in federated contextual bandit problems. It points out the existing gap in previous LDP federated bandit works and provides new approaches with regret and communication cost analysis under LDP and SDP.

### Strengths
1. The paper identifies a significant gap in the existing literature on federated linear bandits.
2. The discussion of related works and the comparison of theoretical results are detailed and clear.
3. The algorithm design appears to be reasonable, and while I haven't reviewed the proof in detail, it seems that the theoretical results align with the algorithm's design.

### Weaknesses
I don't find any obvious weakness of the paper.

### Questions
It appears that the algorithm design in this paper heavily relies on a binary-tree-based mechanism, which can only be applied to linear setting. Is it possible to generalize the algorithm or the analysis to nonlinear models, such as Generalized Linear Models (GLM)?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper Investigates linear contextual bandits user the cross-silo DP. It seems that this paper is motivated by clear holes in the work of Dubey and Petland (2020), which is a highly cited paper. This work succinctly identifies the errors in that paper, as well as proposes their own solution. It is quite remarkable, since that work is well cited, but the arguments of the authors seem convincing to me. 

In addition to showing the errors with that work, this work further develops a variant of LinUCB that provides the required level of privacy, and computes the regret bound. Another variant is considered where shuffle DP is used, which enables regret equal to the regret achieved by the super node.

### Strengths
* Important to set the record straight if errors in Dubey and Petland (2020) is not well known
* Intuitive algorithms that build on well studied baselines
* Generally good flow and writing
* Thorough treatment, including shuffle DP setting as well

### Weaknesses
I think related work sections should be in the main body of the paper for a 9 page paper

I find Section 3 to be a bit prose heavy.

### Questions
Since there is so much discussion of Dubey and Petland (2020), I would like to see some if the information related to it included in the abstract.

I find Section 3 to be a bit prose heavy.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper delves into the exploration of federated learning in the context of linear contextual bandits (LCBs) while incorporating the principles of differential privacy (DP). The proposed algorithmic framework encompasses several key components, including LinUCB exploration, a distributed variant of the tree-based mechanism, privacy amplification, and a fixed batch update approach. This comprehensive approach offers compelling solutions for addressing both silo-level local DP and shuffle DP concerns. Additionally, the authors have identified and rectified an error pertaining to the total injected privacy noise, as previously reported in Dubey & Pentland 2020, contributing to the advancement of this field.

### Strengths
1. The analysis in this paper is notably meticulous, particularly in its identification of the mistake in the previous results. The presentation of the findings is commendable, as it effectively illustrates the potential privacy vulnerabilities present in Dubey & Pentland 2020. Furthermore, it compellingly highlights the necessity of a more robust silo-level local DP setting. The comparison with related work is both thorough and detailed, contributing to a well-rounded understanding of the research landscape.

2. The paper provides a comprehensive narrative that encompasses regret and communication guarantees under varying privacy constraints. Impressively, the authors extend these guarantees to a broader range of privacy parameters, demonstrating a thorough exploration of the subject matter. Moreover, the novel extension of the current amplification analysis to their specific case adds a valuable dimension to the research.

### Weaknesses
1. The paper, while containing valuable insights, may benefit from some improvements in terms of clarity and presentation. Firstly, the algorithmic design, which incorporates several components and explores various privacy settings, could be made more accessible by summarizing the results in a table format. This would provide readers with a quick and clear overview of corresponding regret, communication, and algorithmic elements across different settings. Specifically, the table should clearly delineate the differences in regret bounds, communication costs, and the specific privacy mechanisms (e.g., silo-level LDP, shuffle DP) employed, along with the corresponding algorithmic variations. Additionally, in terms of organization, it might be helpful to reconsider the placement of the concluding remarks, which currently reside under the simulation results. Furthermore, there appears to be a spacing issue in the section discussing the tree-based mechanism, possibly resulting from the authors' use of the vspace command in LaTeX.

2. While the paper offers valuable contributions, the novelty and inspiration of the problem itself could be further developed. The concept of silo-level Local Differential Privacy (LDP), while important and rigorous, may be considered relatively straightforward to formulate. Additionally, the solutions presented in the paper largely draw upon existing results and algorithmic designs, rather than introducing fundamentally new insights or modifications to established findings, which limits the potential of this paper. The core algorithmic components, such as LinUCB exploration and the tree-based mechanism, are well-established. The adaptation of these techniques to the federated learning setting with differential privacy, while practically relevant, does not introduce significant theoretical novelty. The privacy amplification techniques used also seem to be standard applications of existing results, rather than novel derivations or extensions.

### Questions
None.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good
