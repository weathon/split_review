# On the Role of Attention Heads in Large Language Model Safety

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
\subfile{Abstract/Abstract}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a method named Ships, which assesses each attention head’s contribution to LLM safety at both the query and dataset levels. It also proposes a heuristic search-based method, Sahara, to identify a group of safety-related attention heads. Ablating these heads led to a notable increase in ASR on Llama-2-7b-chat and Vicuna-7b-v1.5. The approach is claimed to be more parameter and computing efficient than previous methods.

### Strengths
1. To my knowledge, no other work has attempted to interpret each attention head’s contributions to LLM safety. I'm glad to see such work.

2. The method for assessing the importance of attention heads to safety is intuitive and reasonable.

### Weaknesses
1. Other previous works, such as those identifying safety-related parameters through probing [1], could also be discussed.

2. There are inconsistencies in notation usage that need to be addressed. To name a few:
- In Eq 2, 7 and 8, $d_k$ denotes the model dimension. However in line 297, $d$ is used instead.
- In Appendix A.1, $N = d/n$ should be clarified. Specifically, the derivation of the modified attention matrix $h_i^{mod}$ is unclear. The presented lower triangular matrix A seems arbitrary and lacks proper justification. It's not clear how this modification relates to the original attention mechanism and why it is a valid way to assess head importance.
- Throughout the paper, $L$ and $n$ are used to denote the number of layers and the number of heads, respectively, but Algorithm 1 uses $\mathbb{L}$ and $\mathbb{N}$ for the same.
- Equation 5 defines parameter importance on safety as $\Delta p = p (\theta_O) - p (\theta_O \backslash \theta_c)$. However, $\Delta p$ is never mentioned again. Instead, Equation 9 uses KL divergence between two probabilities. I guess $\Delta p$ means to represent the difference between two probabilities computed by some function.
- Typo: Eq.6, $h_i^m$ → $h_i$

3. The impact of ablating safety-related heads on model utility could be evaluated.

4. Additional clarifications needed:
- In Table 3, are the results at the bottom obtained by, using Ships on each query to identify and ablate the most important head, then assessing whether the attack was successful for that query? If so, why does query-level Ships perform worse than dataset-level Ships?
- Line 264 notes that 0.006% of all parameters corresponds to the number of parameters in a single attention head. However, Section 4 suggests that ablating 0.006% of parameters (potentially one head) can achieve an ASR of approximately 0.72 on Llama. Yet, Figure 4(a) indicates that ablating at least two heads is necessary to surpass an ASR of 0.7. What is the group size used in Table 1?

### Questions
See Weaknesses.

### Soundness
2

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
The authors study how heads contribute to LLM safety, and find that by modifying less than 0.006% of the parameters (a significantly smaller number of parameters than before), safety alignment is degraded significantly. The authors propose Safety Head ImPortant Score (Ships) which measures individual heads’ contributions to model safety. On the dataset level, the authors propose an algorithm Sahara that iteratively choose important heads, creating a group of heads that degrades safety performance for a dataset. The method is efficient in compute hours needed, and impact safety at greater granularity than before. The authors study the effect of safety attention heads, including experiments of concatenating heads to a pre-trained model, and observes that safety capability is close to that of aligned model.

### Strengths
- The paper proposes a novel method for mechanistically locating and ablating heads that are important to safety alignment, with greater granularity and less compute than prior methods. The method of head ablation is well motivated and the experiments are detailed, considering course correction (reverting back to safety) as well.
- The paper is well written and organized

### Weaknesses
1. The helpfulness / utility measurement is done with lm-eval, which mostly consists of single-turn question and answering utility measurement. More comprehensive utility measurement would benefit the paper. 
2. Sahara uses heuristic to choose group size, and group size is important to how safety capability is affected. Such size heuristics (more than 3) might not hold for different models with different number of parameters. 
3. The paper is overall well-written with some small typos:  "Bottom. Results of attributing attributing specific harmful queries using Ships" (line 445). Consider changing the color for axis label for Figure 13. It's currently quite hard to read.

### Questions
Q1. What lm-eval helpful tasks were experimented on for Figure 6b?

Q2: Why do you think there is minimal overlap between the top-10 attention heads via UA ablation and SC ablation (line 477-478)? In combination with results from Appendix E, does this suggest SC is not a good ablation method?

Q3: What do you think contribute to safety capability improve when ablating a small head group between 1 and 3 (line 371)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes the Safety Head Important Score (Ships) to evaluate the contribution of individual attention heads to the safety of language models. It presents the Safety Attention Head AttRibution Algorithm (Sahara), which identifies groups of attention heads that contribute to safety. The authors demonstrate through experiments that certain attention heads are crucial for safety, showing how their ablation can significantly increase the model's susceptibility to harmful queries.

### Strengths
1. The paper introduces a novel approach to understanding the safety mechanisms within large language models (LLMs) by presenting the Safety Head Important Score (Ships) and the Safety Attention Head AttRibution Algorithm (Sahara).
2. It effectively shifts the focus from generalized model parameters to specific attention heads that have a direct impact on the model's ability to reject harmful queries.
3. This work addresses a significant gap in the literature by systematically exploring the role of multi-head attention mechanisms in ensuring model safety, an area that has been relatively underexplored.
4. The discussions in Sections 4 and 5 are comprehensive and logically coherent, incorporating several insightful analyses and discussions.

### Weaknesses
1. Lines 256 and Appendix B.3 indicate that the ASR metric used in this paper employs a keyword-detection method, which is noted in [1] as having limitations that “lead to false positive and false negative cases.” Why is the GPT4-judge method, validated in [1] as a more comprehensive and accurate metric, not used? This method is commonly employed in 2024 LLM safety papers to measure ASR. The inaccuracies of ASR based on keyword detection in assessing successful attacks weaken the experimental data and analysis presented in the paper.
2. The analysis of Figure 2 is relatively weak (Lines 261-267). For instance, according to Figure 2, the improvement in ASR for Vicuna on Advbench and Jailbreakbench (direct) is quite limited, yet these two datasets are highly mainstream in the field of LLM safety. Does this not weaken the conclusions drawn in Lines 262-263?
3. There are still some writing issues in the paper, such as the figure numbering in Line 496, which should refer to Figure 6.
4. Is Figure 6b derived from Llama2 or Vicuna? I couldn't find this information in the paper. Additionally, Figure 6 shows an average decline of about 0.1 in Zero-Shot Task Scores, indicating a 15% decrease compared with the vanilla model. Given that the ASR determination in the paper only detects refusal keywords, I am concerned that the decline in helpfulness may reduce the model's understanding of harmful queries, potentially leading to responses that are affirmative but do not align with the harmful query. This could be counted towards the ASR, further undermining the discussion surrounding Figure 2.

### Questions
1. Could you consider adding a new ASR metric, such as the GPT4-judge referenced in [1]? Alternatively, an analysis of the accuracy of the ASR based on keyword detection (in relation to human judgments) could be included.
2. In light of the second weakness, would it be possible to incorporate additional models, such as Gemma (instruct), to enhance the generalizability of the conclusion that “ablating the attention head with the highest Ships score significantly reduces safety capability”?

[1] Fine-tuning aligned language models compromises safety, even when users do not intend to!

I will reconsider my score if all these issues are adequately addressed.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work makes an essential contribution to the field of LLM interpretability and safety, especially given the increasing deployment of LLMs in sensitive areas where maintaining safety is paramount. By focusing on the attention heads, the authors target a critical yet underutilized aspect of LLM architecture. The Ships metric and Sahara algorithm also address interpretability efficiently, which is crucial for scaling such safety measures in larger models.

The results are promising; however, further research could examine whether these safety heads are consistent across more diverse LLM architectures beyond the ones tested (Llama-2-7b-chat and Vicuna-7b-v1.5). Additionally, the analysis of the trade-offs between safety and model helpfulness could be expanded to understand better how balancing these factors could affect real-world applications.

Overall, this paper offers valuable insights into safety interpretability and contributes a more resource-efficient framework for analyzing and enhancing LLM safety capabilities.

### Strengths
-Great presentation with easy to understand figures and well written concise mathematical concepts/methodology are key strenghts.
-The need of only 0.006% of parameter modification to achieve a SOTA ASR is also impressive.
-I found also interesting that the ablation tests showed clearly the contribution of safety from each head, with only a few ones being critical.
-The Sahara algorithm could be relevant in verifying the safety of LLMs.

### Weaknesses
Further research could examine whether these safety heads are consistent across more diverse LLM architectures beyond the ones tested (Llama-2-7b-chat and Vicuna-7b-v1.5). Additionally, the analysis of the trade-offs between safety and model helpfulness could be expanded to understand better how balancing these factors could affect real-world applications.

### Questions
How could one deploy the Ships and Sahara during the development process?
Which other use cases would be possible?
Robustness, related to attacks and otherwise, are often related to OOD samples. Could you posit the results of the paper in relation to OOD? And in this case, are the number of models and datasets used in the current study sufficient to evaluate it?

### Soundness
4

### Presentation
4

### Contribution
3
