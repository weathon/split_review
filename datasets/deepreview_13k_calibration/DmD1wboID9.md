# BayesPrompt: Prompting Large-Scale Pre-Trained Language Models on Few-shot Inference via Debiased Domain Abstraction

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 6, 8

## Abstract
As a novel and effective fine-tuning paradigm based on large-scale pre-trained language models (PLMs), prompt-tuning aims to reduce the gap between downstream tasks and pre-training objectives. While prompt-tuning has yielded continuous advancements in various tasks, such an approach still remains a persistent defect: prompt-tuning methods fail to generalize to specific few-shot patterns. From the perspective of distribution analyses, we disclose that the intrinsic issues behind the phenomenon are the \textit{over-multitudinous} conceptual knowledge contained in PLMs and the \textit{incomplete} knowledge for target downstream domains, which jointly result in that PLMs \textit{mis-locate} the knowledge distributions corresponding to the target domains in the universal knowledge embedding space. To this end, we intuitively explore to approximate the complete target domains of downstream tasks in a debiased manner, and then abstract such domains to generate discriminative prompts, thereby providing the de-ambiguous guidance for PLMs. Guided by such an intuition, we propose a simple yet effective approach, namely \textit{BayesPrompt}, to learn prompts that contain the domain discriminative information against the interference from domain-irrelevant knowledge. BayesPrompt primitively leverages known distributions to approximate the debiased factual distributions of target domains and further uniformly samples certain representative features from the approximated distributions to generate the ultimate prompts for PLMs. We provide theoretical insights with the connection to domain adaptation.}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes BayesPrompt  to inject the semantic knowledge about the label into the label prompt to adjust the knowledge learned from pretraining to better fit downstream tasks. The method is to learn prompts that contain the domain discriminative information for the interference from the domain-irrelevant knowledge by approximating the factual distributions of downstream domains. The approach learns a representative model that injects the latent knowledge contained in labels into the prompt construction, thereby empowering the inference of relations.

### Strengths
The paper works on a very interesting problem to adjust pretraining knowledge of LLM to downstream tasks. The paper provides theoretical analyses demonstrates that BayesPrompt can tighten
the upper bound of the classification error on the downstream inference of PLMs. Table 2 provide standard deviations over multiple runs.

### Weaknesses
The paper may benefit a lot from better writing, including more clear presentation of the motivation and methods. 
- what does author refer to for "unabridged Domain", "partial domain", in figure 2? 

"Thee over-multitudinous conceptual knowledge contained in PLMs and the abridged knowledge for target downstream domains, which jointly result in that PLMs mis-locate the knowledge distributions corresponding to the target domains in the universal knowledge embedding space. 
"
- what does the author refer as "over-multitudinous conceptual knowledge" and "the abridged knowledge "?

It is not fully convinced to the reviewer that the problem motivates the method can be solved by the method proposed. 
It is unclear that how by "leveraging Gaussian mixture distribution BayesPrompt is able to approximate the debiased factual distributions of downstream domains and further uniformly samples certain representative features from the approximated distributions to generate the ultimate prompts for PLMs". Why the proposed approach can better approximate the downstream tasks distribution? by injecting label -related information? What is the bias referred here? Is there any produces to reduce the bias? The author may refer the bias as "irrelevant pretraining knowledge" that is confounding for the downstream tasks ? not very clear why introducing "Gaussian mixture distribution" can help solve the problem? is it for sampling and easy injecting label-related knowledge? 

by injecting label dependent knowledge, the PLM may learn a PLM distribution that is useful for the downstream task, which makes sense. but is it unfair, as BayesPrompt already uses label information but other methods don't?
 
It is not very clear how Figure 2 motivates the paper.  Figure 1 (domain knowledge is helpful ) and Figure 2 (domain knowledge may lead to negative impact?) seem not to align well. 

Method section: how does  label prompt word lp and type prompt word tp fit in eq(6)? Can the author also bring some clarify to training? 
 
Why does the approach focus on relation extraction tasks (used in method section)? how about other tasks? Is this method currently specific for relation extraction tasks? 

Table 2: the improvement seems not to exceed one standard deviation over other baselines. The category of tasks seem limited. not very convinced on the effectiveness of the methods.

### Questions
See above.

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a prompting method named BayesPrompt to generate prompts for PLMs. The authors argue that the over-multitudinous knowledge implicit in PLMs can hinder the performance of prompt-tuning methods in few-shot settings. Thus, BayesPrompt aims to approximate the unbiased target distribution to generate discriminative prompt for specific domains.
Experimental results show the effectiveness of BayesPrompt on relation extraction (RE) tasks. Also, the authors provide theoretical analysis over BayesPrompt on lowering the classification error upper bound.

### Strengths
1) The task that improves the generalization capabilities of PLMs is challenge in the prompt tuning community. The authors provide a new view from the "mislocated knowledge distributions" between PLMs and target domain, which is interesting. 

2) The motivation that adopts the Bayesian approaches to model dataset-specific information and performing prompting on the latent space is novel.

3) The provided theoretical analyses and extensive experiments help readers to understand the method.

### Weaknesses
1) As can be seen from Tables 1 and 3, the proposed BayesPrompt presents a completely different improvement. Can the authors provide a detailed explanation?

2) Please provide more discussion about the ablation results at Figure 4(c).

### Questions
BayesPrompt's training complexity is higher than its baseline, is there any potential for optimization?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes BayesPrompt, a Bayesian approach to approximate the factual distributions of downstream domains 
and thereby generating discriminative prompts for PLMs. The authors articulate that the intrinsic issues behind the poor performance of finetuned PLMs on few-shot downstream tasks roots from two main shortcomings: (i) over-multitudinous of conceptual knowledge contained in PLMs, (ii) an abridged knowledge for target downstream domains. The paper takes a stride in addressing this challenge with both theoretical (tailored towards a classification problem) as well as experimental results.

### Strengths
- The paper is well written, well structured and has a clear narrative. 
- The authors pay utmost attention to details, from notations and math to presentation of the results, making the paper easy to follow.
- The paper has a healthy mix of a (simplified) theoretical and qualitative arguments, based on which the approach is devised. 
- The results seem to be promising, comparing against some recent baselines. 
Overall, it seems like a solid contribution.

### Weaknesses
 - The paper is essentially a shortened version of a much longer manuscript, where the authors are constantly cutting the content short and referring the reader to different sections of the appendix (appendix is referred to 11 times throughout the paper!). So, the main body of the paper is not really self-contained and heavily relies on the appendix. By the same token, the main algorithm of the paper had to be pushed to the Appendix, which could be a natural choice in the main text to clarify the end-to-end procedure. 
- The impact of the proposed approach is rather marginal when compared to the closest competitors (say RetrievalRE), especially on standard RE performance in Table 3, while at the same it comes at the cost of extra training complexity. Any reason behind this?  
- No Ablation studies. There are design choices that could potentially establish the basis for Ablation studies (such as Kernel size and so).

### Questions
No further questions (beyond what's already raised in weaknesses), and after reading through the Appendix.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Prompt-tuning is a fine-tuning paradigm based on large-scale pre-trained language models (PLMs), which can reduce the gap between downstream tasks and pre-training objectives. This paper focus on the challenge of poor generalization to specific few-shot patterns of the Prompt-tuning. Through distribution analysis, they reveal that the root cause of this issue is the overabundance of conceptual knowledge in PLMs and the truncated knowledge for target downstream domains. This collective effect misaligns the knowledge distributions corresponding to the target domains in the universal knowledge embedding space. To address this issue, they propose BayesPrompt, an approach that intuitively explores debiased approximation of unabridged target domains of downstream tasks. BayesPrompt generates domain-discriminative prompts to provide unambiguous guidance for PLMs. Further, they theoretically show that BayesPrompt tightens the upper bound of the classification error on PLMs' downstream inference on classification error bounds. The experimental results show that the proposed method achieves SOTA performance on benchmarks.

### Strengths
1.	The paper reveals the principles of the challenge of prompt-tuning on pre-trained large models for few-shot tasks.
2.	The methodology of using the Bayesian prompt is novel and effective.
3.	The theoretical guarantees the performance of the proposed method.
4.	The evaluation presents the benefits of the proposed method.

### Weaknesses
1.	This paper utilizes the GMM to approximate the distribution of the target domain which may not be unabridged. The real distribution of the target domain is complex and unknown.
2.	The PLMs utilized in the evaluation are not clear. Using various PLMs may be better to show the generality of the proposed method.

### Questions
1.	Why can GMM approximate the target domain? What are its benefits than a learnable generator (VAE or GAN)?
2.	Is it required to train a specific GMM for each input sentence (X, Y)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
