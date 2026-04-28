# Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
We study the problem of in-context learning (ICL) with large language models (LLMs) on private datasets. 
This scenario poses privacy risks, as LLMs may leak or regurgitate the private examples demonstrated in the prompt.
We propose a novel algorithm that generates synthetic few-shot demonstrations from the private dataset with formal differential privacy (DP) guarantees, and show empirically that it can achieve effective ICL.
We conduct extensive experiments on standard benchmarks and compare our algorithm with non-private ICL and zero-shot solutions. 
Our results demonstrate that our algorithm can achieve competitive performance with strong privacy levels.
These results open up new possibilities for ICL with privacy protection for a broad range of applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study addresses the challenges of in-context learning (ICL) with large language models (LLMs) on private datasets, focusing on privacy concerns. The researchers propose an algorithm that generates synthetic few-shot demonstrations with formal differential privacy (DP) guarantees, enabling effective ICL while protecting private information in prompts. Their empirical experiments demonstrate that this approach maintains competitive performance with strong privacy levels. Additionally, they explore zero-shot solutions where LLMs generate their own demonstrations, showing potential for achieving privacy without compromising performance.

### Strengths
1)The paper studies simple approach of achieving privacy in ICL (synthetic data generation and use it as demonstrations)

2)Paper for most parts is clearly written and is easy to read.

### Weaknesses
1) No comparison with real-world threat models has been provided. Epsilon-utility trade-offs can be misleading without testing them against actual attacks, as epsilon guarantees are built upon numerous assumptions, as indicated in [1, 2, 3]. For a comprehensive evaluation, it is essential to conduct experiments that demonstrate trade-offs between  empirical privacy and utility.


2) *"*..A different line of work (Feyisetan et al., 2020; Xu et al., 2020; Du et al., 2023) focuses on sanitizing user texts locally before releasing them to the server based on metric local differential privacy (Chatzikokolakis et al., 2013). Such methods usually incur huge overheads to the utility of the sanitized text ..*"* This statement is not necessarily true and it should be revised to avoid making broad generalizations. As evidenced in a recent study [3], the use of a language model prompted "zero-shot" to generate paraphrases exhibited a clear and significantly better (empirical)privacy-utility tradeoffs.

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies how to incorporate differential privacy into in-context learning with large language models. The authors propose a DP algorithm which generates synthetic few-shot examples from a private dataset; these “demonstrations” can then be used downstream for in-context learning without incurring additional privacy costs. The authors evaluate their algorithm across several benchmark datasets and privacy regimes, including a fully private ($\epsilon=0$) case which doesn’t use the private dataset at all.

### Strengths
1. The empirical evaluation (including an ablation study) is very thorough.
2. Compared to previous / concurrent work, I think the “generating synthetic few-shot data” approach is really practical since (due to post-processing) answering any number of queries now doesn’t affect the privacy guarantee.
3. The proposed framework is flexible enough to adapt to many potential use cases, and I could see that there could be interesting future work down the line.

### Weaknesses
None of the experimental baselines compare the proposed algorithm to existing work. In particular, I think it could be instructive to see how DP few-shot generation compares to DP fine-tuning approaches.

### Questions
It seems likely the the PATE-like component of Algorithm 1 could (similarly to PATE) have a stronger data-dependent privacy analysis if the models “agree.” While by no means necessary, I would be interested to see this!

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To prevent the leakage of private data, the current approach necessitates consulting the large model only in a zero-shot manner. In this article, the author proposes a solution by generating multiple synthetic prompts based on private data. This enables leveraging the performance boost afforded by few-shot learning while maintaining privacy guarantees.

### Strengths
In the current industry practice, safeguarding privacy data requires organizations to pre-train or fine-tune large models, demanding substantial resources. Leveraging synthetic data as prompts to enhance large model capabilities not only preserves privacy but also significantly reduces resource consumption.  Adding noise to the probability of generating the next word in a large model is a relatively novel approach.

### Weaknesses
Generating a composite prompt requires consulting the large model M*L times, leading to a significant consumption of resources.
  + The necessity of employing an untrusted model to generate the next word poses a challenge. While open-source large models are an option, their performance in generation tasks tends to be lower compared to closed-source counterparts. There is some uncertainty surrounding the final quality of the synthesized prompt, including aspects such as length, coherence, and overall fluency. The method's reliance on a large model for generating synthetic prompts introduces a potential vulnerability. If the large model used for prompt generation is biased or contains inaccuracies, these issues could be propagated into the synthetic prompts, thereby affecting the performance and reliability of the downstream model. Furthermore, the computational cost of generating M*L prompts is not only a one-time cost but also a recurring overhead if the private data changes or if the model needs to be adapted to new tasks. This makes the approach less flexible and potentially more expensive in dynamic environments.

### Questions
Pls specify the quality of the synthesized prompt.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies an emergent and important problem of how to generate private demonstrations for in-context learning. The authors proposed to generate synthetic few shot examples from the private database (Algorithm 1). As a result of post-processing property of DP, number of queries does introduce extra privacy cost.

### Strengths
Studies an important problem and provide intuitive solution. Theoretical analysis looks correct to me.

The experiments compared with a strong competitor (asking LLM to generate its own demonstrations). Moreover. this finding is also interesting in its own sense (with 20-30% accuracy improvement in many cases.)! Private ICL shows comparable accuracy to the non-private  few-shot prompt accuracy.

### Weaknesses
Algorithm 1 seems to incur M foundation model api calls. How much monetary cost does the algorithm incur?

In the paper, the author investigated report noisy max with exponential mechanism. Will using RNM with gaussian mechanism lead to better accuracy?

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
