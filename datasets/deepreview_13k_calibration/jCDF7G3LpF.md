# EFFICIENT JAILBREAK ATTACK SEQUENCES ON LARGE LANGUAGE MODELS VIA MULTI-ARMED BANDIT-BASED CONTEXT SWITCHING

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 5, 6

## Abstract
Content warning: This paper contains examples of harmful language and content.
Recent advances in large language models (LLMs) have made them increasingly vulnerable to jailbreaking attempts, where malicious users manipulate models into generating harmful content. While existing approaches rely on either single-step attacks that trigger immediate safety responses or multi-step methods that inefficiently iterate prompts using other LLMs, we introduce ``Sequence of Context" (SoC) attacks that systematically alter conversational context through strategically crafted context-switching queries (CSQs). We formulate this as a multi-armed bandit (MAB) optimization problem, automatically learning optimal sequences of CSQs that gradually weaken the model's safety boundaries. Our theoretical analysis provides tight bounds on both the expected sequence length until successful jailbreak and the convergence of cumulative rewards. Empirically, our method achieves a 95\% attack success rate, surpassing PAIR by 63.15\%, AutoDAN by 60\%, and ReNeLLM by 50\%. We evaluate our attack across multiple open-source LLMs including Llama and Mistral variants. Our findings highlight critical vulnerabilities in current LLM safeguards and emphasize the need for defenses that consider sequential attack patterns rather than relying solely on static prompt filtering or iterative refinement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel Sequence of Context (SoC) jailbreak attack that leverages Multi-Armed Bandit (MAB) to automatically guide context selection. The authors provide an in-depth theoretical analysis of the upper bound on the expected sequence length. Experimental results demonstrate the effectiveness of the proposed method in jailbreaking language models.

### Strengths
1. The use of MAB for automated context selection in jailbreaking is novel
2. The theoretical derivation of the upper bound for the SoC attack length is well-established
3. The experimental results effectively demonstrate the method's efficacy

### Weaknesses
1. Compared to other automatic jailbreak attacks (e.g., GCG, PAIR), this method requires dataset collection and policy model training, making it more resource-intensive and time-consuming
2. The proposed method is limited to pre-defined harmful query categories, and its extensibility to unseen categories is not thoroughly investigated
3. The paper lacks comparison with state-of-the-art jailbreak attacks in terms of attack success rate and computational cost

### Questions
1. Could you explain the necessity of including the direct malicious query (DMQ) in the context? Given that language models with safety alignment typically reject DMQs, would it be possible to remove DMQ from the context to reduce context length?
2. How does the proposed judgment method compare with widely-used judgment systems (e.g., Llama Guard family) that are more common in jailbreak literature?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel jailbreaking attack paradigm named the sequence of contexts (SoC) attacks. By leveraging techniques in multi-armed bandit (MAB), this paper maximizes the likelihood of a successful jailbreaking attack (decided by CSQ). A theoretical upper bound for the gap between the obtained and optimal rewards is presented. Experimental results show that the proposed strategy indeed enhances the effectiveness of jailbreaking attacks.

### Strengths
**About novelty**

+ This paper studies jailbreaking attacks from an MAB perspective, bringing new insight into this area of research.

**About contribution**

+ This paper proposes a DMQ dataset that includes 3000 queries collected from previous works. The following works can use this as a benchmark.
+ The experimental results (figures 2 and 3) demonstrate that the proposed method enhances the effectiveness of jailbreaking methods, compared to the naive strategy. 

**About presentation**

The presentation is clear. The algorithms and figures are well-made.

### Weaknesses
 **About contribution**

+ This paper does not compare the proposed jailbreak attack with the existing methods.
+ The only theorem in this paper is almost trivial, and more importantly, the assumptions and limitations of this theorem are not discussed. 
It is encouraging to include theoretical analysis in LLM research. However, the results are not strong enough to serve as "one of the main contributions" (as stated in Line 253) of an ICLR paper.

In brief, the authors claim three main contributions: creating a dataset, proposing a novel jailbreaking attack strategy, and providing a theoretical analysis. However, I think contributions (ii) and (iii) are slightly overstated. That is why I gave a score of 5 for this paper.

**About presentation**

+ This paper contains too many acronyms. I suggest adding a list of acronyms in the appendix. Besides, the authors do not provide a detailed explanation for some of the terms (e.g., sequence of context attack, and context switching queries) at their first appearance. It would make this paper more easy to follow if the authors add some explanations for the terms and reference them (e.g., see Section xxx for detailed discussions) when the term is mentioned for the first time.

+ The citation style (i.e., the green boxes) is dazzling.

### Questions
See the weakness part.

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
This paper discovers the LLMs intend to reject direct malicious queries (DMQs), but answer when followed by content switching queries (CSQs). For automatically generating DMQs and CSQs, the authors propose a framework based multi-armed bandit (MAB) to jailbreak LLM automatically. They introduce a dataset of CSQs based on MAB. And they give a mathematical derivation for the proposed method to prove key bounds.

### Strengths
### 1. The discovery about switching the context leads jailbroken
This paper presents a context switching attack, which is a novel method compared to existing works. And combined with multi-armed bandit, SoC can automatically jailbreak LLMs.


### 2. Theoretical Results
Section 4 establishes a upper bound on the length of SoC attack sequence. And I believe a method which has a mathematical proof is more solid than existing jailbreak works.

### Weaknesses
### 1. Poor readability
In the abstract and in the overview (Figure 1) , the authors mention "multi-armed bandit (MAB)", but they do not explain what is MAB in the introduction.I suggest the authors revise this, it confuses me until I have read related works.

In addition to MAB, the introduction has unreasonable content. With four paragraphs, more than half introduction is irrelevant to the contribution of this paper. And in the third paragraph, there are too many concepts are proposed but lack of details. I suggest that the authors adjust their introduction, current version has poor readability.

I think it is not appropriate to introduce how this paper uses MAB in related work. And why is T both rounds and sequence length (*total reward over T rounds*: line133; *attack sequence length T*:line137)? What does T represent in the subsequent content?

There are a lot of abrupt concepts introduced without much explanation in context. In line 215, I can not find any information or reference about *policy $\pi$* and *action-value Q* (including cost C in line 240). I can only speculate that this has something to do with reinforcement learning. And in Algorithm 1, what does  $E_{explore}$ stand for and what does  $E_{exploit}$ stand for? I can not find any explanation.

### 2. Lack of comparison
This paper only demonstrate SoC can jailbreak LLMs, but has no comparison with prior works. I believe that there are many excellent baseline jailbreak methods. The SoC attack has similar format with the In-Context Attack[8] which also jailbreak LLMs based on context. Besides, the authors optimize their method with reinforcement learning, but the binary reward is very similar to PAIR, which use LLM optimize jailbreak prompt[9].


### 3. Few experiments
In the entire paper, only four figures in Figure 3 prove that SoC is effective, and there is a lack of comprehensive experiments from multiple angles. For example, with different hyperparameters such as J and K, I am not sure whether this method can be generalized or only performs well under certain specific parameters.



### Questions
### 1. Related Works
I believe that in the `White-Box Attack`, the authors should not cite a lot of attack but is irrelevant to jailbreak. Besides GCG, there are many white-box attack, such as fine-tuning attack[1, 2], improved GCG[3], interpretability-based[4, 5]. Nevertheless, I am only making a suggestion. Whether the author makes modifications or not will not change my rating.

### 2. Why does the authors think modern LLMs avoid responding to malicious questions by classifier?
In Section 3.1 line 155-line157, the authors mention "In most instances, such queries fail to produce harmful responses and can be guarded using straightforward strategies, such as employing a classifier to flag harmful words and phrases". Current LLMs do not use those filter, but are fine-tuned to align with human values[6, 7].

### 3. There is no update for $\pi$ or $\pi^{*}$
Algorithm 1 aims to optimize a policy $\pi$, however, where is update for $\pi$ or $\pi^{\star}$. Why can Algorithm 1 obtain a optimized policy $\pi^{\star}$? This confuses me as to how Soc Attack works.

### typos
1. Incorrect use of quotation marks: line 153-155, 
2. Do B and C refer to the appendix? line 201 & 202 & line 318 & line 321 & line 365
3. Do you mean harmful or harmless? line 213-214: *which assigns a binary reward indicating whether the response is harmful or unsafe.*
4. *see-D.0.1*, *see-D.0.2*, *see-D.0.3* and *see-D.0.4* mean Appendix D.0.1, Appendix D.0.2, Appendix D.0.3 and Appendix D.0.4?

---


[1] FINE-TUNING ALIGNED LANGUAGE MODELS COMPROMISES SAFETY EVEN WHEN USERS DO NOT INTEND TO!

[2] SHADOW ALIGNMENT: THE EASE OF SUBVERTING SAFELY-ALIGNED LANGUAGE MODELS

[3] AmpleGCG: Learning a Universal and Transferable Generative Model of Adversarial Suffixes for Jailbreaking Both Open and Closed LLMs

[4] Uncovering Safety Risks in Open-source LLMs through Concept Activation Vector

[5] How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States

[6] Training language models to follow instructions with human feedback

[7] Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel method for jailbreaking large language models (LLMs) through "Sequence of Contexts" (SoC) attacks and utilizes a multi-armed bandit (MAB) framework to automate the optimization of the attack process. The paper also provides an in-depth theoretical analysis of the sequence length required for a successful jailbreak and the convergence of total rewards.

### Strengths
The study not only experimentally demonstrates the efficiency of the proposed method, achieving an attack success rate of over 95%, but also provides a solid theoretical foundation for LLM jailbreak attacks.

### Weaknesses
1. It is a natural question: why do you not compare your work with other methods，such as GCG[1] , AutoDAN[2], PAIR[3], RENELLM[4] and so on? 
2. Since your work requires selecting a sequence of context-switching queries, I am curious about it time complexity. 
3. In my opinion, testing only on Mistral and Llama is not sufficient to demonstrate the advantages of your work. Moreover, you have only chosen small LLMs (up to 8B), which is not convincing. As far as I know, Llama has a 13B version. What's more, CHATGPT is necessary to be choose.
In conclusion, without comparisons, it is difficult for me to fully assess the contributions of this paper, especially considering that there are many papers on LLM jailbreaks. If you address my concerns, I will consider giving a higher score.

### Questions
See weekness.

### Soundness
3

### Presentation
3

### Contribution
3
