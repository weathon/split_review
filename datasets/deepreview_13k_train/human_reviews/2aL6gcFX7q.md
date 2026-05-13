# Understanding Data Poisoning Attacks for RAG: Insights and Algorithms

- Decision: Reject
- Scores: 3, 5, 6, 5, 5

## Abstract
Large Language Models (LLMs) have achieved success across various domains but also exhibit problematic issues, such as hallucinations. Retrieval-Augmented Generation (RAG) effectively alleviates these problems by incorporating external information to improve the factual accuracy of LLM-generated content. However, recent studies reveal that RAG systems are vulnerable to adversarial poisoning attacks, where attackers manipulate retrieval systems by poisoning the data corpus used for retrieval. These attacks raise serious safety concerns, as they can easily bypass existing defenses. In this work, we address these safety issues by first providing insights into the factors contributing to successful attacks. In particular, we show that more effective poisoning attacks tend to occur along directions where the clean data distribution exhibits small variances. Based on these insights, we propose two strategies. First, we introduce a new defense, named DRS (Directional Relative Shifts), which examines shifts along those directions where effective attacks are likely to occur. Second, we develop a new attack algorithm to generate more stealthy poisoning data (i.e., less detectable) by regularizing the poisoning data’s DRS. We conducted extensive experiments across multiple application scenarios, including RAG Agent and dense passage retrieval for Q&A, to demonstrate the effectiveness of our proposed methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies data poisoning attacks against Retrieval-Augmented Generation (RAG) systems. RAG systems can be compromised when attackers inject manipulated data into the retrieval corpus. The authors suggest that succesful attacks may exploit low-variance directions in the data distribution. Based on these findings, the authors introduce two significant innovations: a defense method called Directional Relative Shifts (DRS), which detects potential poisoning by analyzing shifts in low-variance directions, and a stealthier attack method that reduces detectability by minimizing DRS scores for poisoned data. The experiments show the effectiveness of the proposed defense across various RAG applications, such as Q&A systems and medical data retrieval, while the new attack algorithm succeeds in circumventing traditional and DRS defenses under specific settings.

### Strengths
The Directional Relative Shifts (DRS) metric is the most interesting contribution of the paper: it is a novel measure to detect poisoned documents. Moreover, Both theoretical and empirical results are provided. In terms of clarity, the paper is well written and easy to follow.

### Weaknesses
A significant shortcoming is the absence of reported attack success rates in the experimental results. Without this metric, it becomes difficult to fully evaluate the effectiveness of both the proposed attacks and defenses.

The paper also lacks a deep discussion on the computational cost of DRS. The access to clean documents need better justification and analysis.

### Questions
- How defending against poisoning in RAG settings differs from defending against, e.g., jailbreak or prompt injection attacks?

- Can the authors motivate better this assumption?: "We assume the defender has access to both the retriever and the clean data corpus. When a new test document is proposed for injection into the clean corpus, the defender calculates its DRS score (to be defined later in Eq. 3) and compares it with the scores of known clean documents." How can that clean data corpus be garanteed to not poisoned? And how many clean documents would be required so achieve such guarantee?

- Could the authors elaborate on the computational overhead of calculating DRS?

- The paper suggests that attack effectiveness is maximized by targeting low-variance directions within the data distribution. Can the authors provide more detailed empirical evidence on how such low-variance features manifest in real-world documents? Also, could you please specify the experimental settings of Fig. 2?


- A sensitivity analysis of the hyperparameters $\lambda_1$ and $\lambda_2$ would give insight into the attack’s trade-offs between attack sucess rate and evasion of the defense.

### Soundness
3

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
This paper studies both defenses and attacks to retrieval-augmented generation, which has been used in many applications. The proposed attack and defense are based on the observation that poisoning attacks tend to occur along directions for which clean data distribution has small variances.

### Strengths
1. The attacks and defenses to RAG  are an active research topic, given RAG is used in many real-world applications. Additionally, existing attacks are summarized in the paper. 

2. Multiple attacks on RAG are considered.

3. The analysis made in the paper is interesting. For instance, Figure 1 shows some empirical evidence to verify the developed theory.

### Weaknesses
1. One limitation of the method is that the assumption can be strong. For instance, it is assumed that adversarial query has a different distribution from normal query. However, in practice, an attacker may select normal queries as target queries. In this scenario, the distribution of the adversarial query would be the same as the target query. This assumption may hold for certain attacks. The authors may consider narrowing down the scope, i.e., focusing on the scenarios where the adversarial query has a different distribution from the target query. 

2. The assumption 1 is not very clear. How to measure the distance between two texts? The authors may consider adding more explanations to make it easier for readers to understand. Also, assumption 1 states the distance between two texts is bounded, which may not be informative, as it may hold for two arbitrary texts in practice. 

3. The proposed defense may influence the utility of RAG. For instance, if new knowledge is added for a query, it can be rejected if it is substantially different from clean texts in the clean data corpus. In the experiments, it is shown that the false positive rate is very high. Is it because the clean documents are irrelevant to the protected queries? It can be helpful to perform a comprehensive analysis of the proposed defense on the influence of the utility of RAG systems. One naive defense is to reject all documents whose similarities (e.g., embedding vector similarity) are high with protected queries. The authors may consider comparing with some baselines to demonstrate the effectiveness of the proposed defenses. Additionally, the evaluation in Section 5.2 for the proposed attack is very limited.

### Questions
See above.

### Soundness
3

### Presentation
3

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
The paper investigates the vulnerability of Retrieval-Augmented Generation (RAG) systems to data poisoning attacks, where adversaries manipulate the retrieval corpus to influence model outputs. It reveals that effective poisoning occurs along low-variance directions in the clean data distribution, allowing attackers to insert poisoned data that stealthily alters retrieval results. The authors propose a new defense metric, Directional Relative Shifts (DRS), to detect these poisoned entries by examining shifts along susceptible directions. Additionally, they introduce an advanced attack algorithm that regularizes DRS values, making poisoned data harder to detect. Empirical tests confirm the effectiveness of DRS in various RAG applications, demonstrating the need for robust defenses.

### Strengths
1.	The authors attempt to give a deeper understanding and theoretical analysis of existing attacks. It should be encouraged.
2.	This is a well-written paper. The definitions of symbols and the overall flow are clear.
3.	The proposed defense is simple yet highly effective.

### Weaknesses
1. Missing some references.
- Line 65: The authors should provide references for perplexity-based filters (e.g., [1]).
- Line 143-153: The authors should also mention existing attacks against (e.g., [2]).
2. There has been some work discussing the characterization of poisoned samples. In particular, the proposed method (i.e., DRS) is similar to [3] to some extent. The authors should compare their method to existing works.
3. The authors only use AgentPoison as an example to demonstrate the effectiveness of the proposed attack. The authors should conduct more extensive experiments on all discussed attacks to verify its generalizability.
4. According to Section 5.2 (Table 5), the performance of the proposed attack is limited.
5. The authors should directly place the appendix after the references in the main document.

### Questions
1. Add more related references.
2. compare their method to existing works like [3].
3. Conduct more experiments regarding the proposed attacks.
4. Explain the performance of the proposed attack.

Please find more details in the aforementioned 'Weaknesses' part.

PS: I am willing to increase my score if the authors can (partly) address my concerns.

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
This paper investigates vulnerabilities in RAG systems due to adversarial data poisoning attacks. The authors analyze how specific data characteristics affect attack success, proposing a new defense method, Directional Relative Shifts (DRS), which detects poisoned data by monitoring shifts in directions with low data variance. They also introduce a stealthier attack algorithm that minimizes DRS to evade detection. Experimental results indicate that DRS demonstrates strong defense performance, though its effectiveness is somewhat reduced against the proposed attacks.

### Strengths
1. **Innovative Approach** -- The proposed DRS defense is novel in its focus on low-variance directions to detect adversarial data shifts. This approach, within the experimental settings of the paper, demonstrates defensive effectiveness against poisoning attacks.
2. **Comprehensive Evaluation** -- This paper provides extensive experiments in multiple RAG setups, such as autonomous driving and medical Q&A, confirming the generalizability of DRS across diverse applications.
3. **Insightful Theoretical Contributions** -- The theoretical analysis connecting attack effectiveness to data distribution characteristics (specifically low-variance directions) offers valuable insights, potentially influencing future defenses in retrieval systems.

### Weaknesses
 1. **Sparse Theoretical Explanation** -- While DRS’s foundation on variance shifts is intuitive, a deeper theoretical analysis could further clarify why certain dimensional shifts are more vulnerable. Specifically, the paper lacks a rigorous explanation of how the magnitude of variance in a particular direction directly correlates with the effectiveness of a poisoning attack. This would strengthen the defense’s theoretical underpinnings.
2. **Unrealistic Defense Assumptions** -- The defense method assumes prior knowledge of a specific subset of queries that need protection from poisoning attacks. In real-world applications, defenders typically do not have knowledge of which specific queries might be targeted, and a practical defense would need to offer broad protection across all possible queries. This limitation reduces the generalizability and practicality of the proposed DRS-based defense method. The assumption that defenders can pre-select queries for protection is a significant constraint that limits the applicability of the method in real-world scenarios where the attacker's targets are unknown.
3. **Unrealistic Assumption** -- In Section 3.1, the authors illustrate their attack method with an example where, in a knowledge base about food, an adversarial query about mathematics is used to avoid retrieving clean documents. This assumption is unrealistic, as it does not reflect typical user behavior—users are unlikely to ask irrelevant questions, like mathematics queries, in a food-related knowledge base context. This reduces the practical applicability of the assumptions underpinning the theoretical insights. The example, while intended to be illustrative, introduces a scenario that is not representative of real-world user interactions, thereby weakening the practical relevance of the attack model.
4. **Inaccurate Description of Experimental Results** -- In Figure 1, the authors claim that "we can observe that the attack success rates of Ap are higher than BadChain and AutoDan." However, the figure only shows relative changes in certain dimensions and does not explicitly provide data on the actual success rates of each attack. This discrepancy between the description and the figure may mislead readers and reflect a lack of rigor in interpreting experimental results. The figure's focus on relative changes, rather than absolute attack success rates, makes it difficult to validate the authors' claims and raises concerns about the accuracy of their experimental analysis.
5. **Limited Innovation in Attack Method** -- Although the paper claims to develop a new attack algorithm, it essentially modifies existing attack methods by adding a regularization term based on the proposed defense metric (DRS). This adjustment is an incremental improvement rather than a substantive innovation. Moreover, the effectiveness of this “new” attack is limited, as it only partially reduces the DRS defense success rate without significantly overcoming the defense.

### Questions
1. **Clarification on Theoretical Basis** -- Could you provide a more rigorous theoretical explanation for why certain low-variance directions are more susceptible to poisoning attacks in DRS? A deeper analysis would help clarify the underlying vulnerabilities exploited by attackers.
2. **Defense Scope and Practicality** -- Given that the defense currently focuses on protecting a specific subset of pre-selected queries, how would DRS perform in scenarios where the entire query space needs protection? Have you considered evaluating DRS’s effectiveness without pre-selecting queries, to simulate more realistic defensive conditions?
3. **Lack of Attack Success Rate Comparison** -- In the evaluation of the proposed “new” attack algorithm, the paper only presents its detection rate under the DRS defense. Could you provide a comparison of the attack success rates between the new algorithm and traditional attacks?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors conduct a comprehensive analysis of data poisoning attacks on RAG. Specifically, they provide a framework to analyze attacker objectives. They observe that more effective attacks tend to result in larger relative shifts along directions with smaller variances. Based on this observation, the authors design a new filtering method to defend against poisoning attacks. Additionally, they introduce a regularizer to bypass the new detection method. Through experiments, they demonstrate the effectiveness of both the new defense and attack strategies.

### Strengths
The analysis and observations of current poisoning attacks on RAG are novel and interesting.

The paper considers four attack settings to demonstrate the effectiveness of the defense methods, offering a comprehensive and thorough evaluation.

### Weaknesses
Major concern: I am uncertain about the reliability of DRS. For example, if the question is, "Who is the OpenAI CEO?" I would expect the embedding of a clean document ("The CEO of OpenAI is Sam Altman") to be similar to that of a poisoned document ("The CEO of OpenAI is Elon Musk"). I am unsure whether DRS can effectively handle such an attack. This highlights a potential vulnerability where semantically similar but factually incorrect information can easily bypass the detection mechanism. The core issue lies in the reliance on embedding shifts, which may not be significant enough when the poisoned content is crafted to be semantically close to the original.

The clarity of this paper needs improvement.
Some examples: 
1. In Figure 1, what is the Y-axis?
2. In Section 2.1, the attacker’s capability is described as "only injecting poisoned data (e.g., by creating a new Wikipedia page)." However, in Section 5.1.2, the setting appears to change, with the retriever itself being backdoored.
3. In Section 5.1.1, there is no description of the adversarial query.
4. In Section 5.1.1, the statement "For each attack method, we generate 300 poisoned data samples" is unclear. Does "poisoned data samples" refer to poisoned documents?

If I understand correctly, DRS also requires a set of clean samples to compute the threshold, but it is unclear how large and diverse this dataset needs to be.

### Questions
NA

### Soundness
2

### Presentation
2

### Contribution
2
