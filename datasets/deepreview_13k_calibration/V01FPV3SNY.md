# Defending Against Alignment-Breaking Attacks via Robustly Aligned LLM

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Recently, Large Language Models (LLMs) have made significant advancements and are now widely used across various domains. Unfortunately, there has been a rising concern that LLMs can be misused to generate harmful or malicious content. Though a line of research has focused on aligning LLMs with human values and preventing them from producing inappropriate content, such alignments are usually vulnerable and can be bypassed by alignment-breaking attacks via adversarially optimized or handcrafted jailbreaking prompts. In this work, we introduce a \textbf{R}obustly \textbf{A}ligned \textbf{LLM} (RA-LLM) to defend against potential alignment-breaking attacks. RA-LLM can be directly constructed upon an existing aligned LLM with a robust alignment checking function, without requiring any expensive retraining or fine-tuning process of the original LLM. Furthermore, we also provide a theoretical analysis for RA-LLM to verify its effectiveness in defending against alignment-breaking attacks. Through real-world experiments on open-source large language models, we demonstrate that RA-LLM can successfully defend against both state-of-the-art adversarial prompts and popular handcrafted jailbreaking prompts by reducing their attack success rates from nearly 100\% to around 10\% or less. 

{
\centering\textcolor{red}{\normalsize{\textbf{WARNING: This paper contains unsafe model responses. Reader discretion is advised.}}}
}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a Robustly Aligned LLM (RA-LLM) as a countermeasure to jailbreaking attacks. The primary methodology involves randomly removing tokens from the prompt and assessing the failure rate under aligned LLMs.

### Strengths
1. The underlying principle of RA-LLM is evident: the strategic removal of tokens from the prompt has the potential to neutralize the adversarial prefix, thereby mitigating the effectiveness of the attack.

2. The introduced methodology demonstrates substantial robustness when tested on Vicuna-7B and Guanaco-7B.

### Weaknesses
1. The concept of partially erasing the prompt as a defensive measure against jailbreak attacks has been previously explored, as evidenced by concurrent work [1]. It would be beneficial if the authors delved deeper into this method to enhance its defensive capabilities. Furthermore, it might be worth comparing the RA-LLM's performance with the perplexity-based defense [2], which has also demonstrated commendable robustness.

2. The experimental evaluations appear to be limited to open-source LLMs. Is it feasible for the RA-LLM to be effective on GPT3.5/4? Comprehensive experimental results on GPT3.5/4 would enhance the study's credibility. The absence of such results raises concerns about the generalizability of the proposed method to more widely used, proprietary models.

3. In assessing computational costs, the authors have focused on financial implications rather than time expenses. The reviewer posits that time cost is of paramount importance, as it directly relates to the model's efficiency. The evaluation should include a detailed analysis of the time overhead introduced by the RA-LLM, particularly in comparison to the standard inference time of the base LLMs.

### Questions
See weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a method to defend alignment-breaking attack by perturbing the input prompt to see whether the request is rejected by an aligned LLM, which is interesting. Experiments on both attack dataset and QA datasets verify the effectiveness of the proposed method.

### Strengths
1. Defending the alignment-breaking attack for LLMs is a very important research direction to protect LLMs from being misused.

2. The proposed method seems to be quite effective according to the reported experimental results.

3. The proposed method is very easy to implement.

### Weaknesses
1. I wonder whether it is enough to have only one dataset for ASR and BAR evaluation.

2. The size of the experimental dataset seems to be small.

3. This paper does not consider the adaptive attack scenario.

### Questions
I wonder whether the proposed method can make some false positive errors.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on defending current LLMs against adversarial attacks (i.e., jailbreak attacks). The authors propose a method that requires multiple times of model inference. 

The first inference is the conventional inference that takes the original prompt (e.g., harmful instruction and jailbreak prompt) as the input and collects the output. Subsequently, this paper randomly drops the words in the original prompt, inferences to get the output, and detect the harmfulness of this output. Through multiple times of such procedure, the harmfulness of this original prompt is determined by collecting these detection results.

This paper shows experimental results on one dataset and two models.

### Strengths
1. The topic of this paper is important in the field of LLM.
2. The proposed method is intuitively reasonable that can defends adversarial attacks to an extent (e.g., the GCG attack).

### Weaknesses
1. **Lack of baseline comparisons.** This paper did not compare with a highly related baseline, that is detecting harmfulness based on the model output [1]. This baseline requires roughly $L_{in} + (L_{in}+L_{out})$ input cost and $L_{out}$ output cost, where the overall cost could be much smaller than this paper's method (if the $L_{out}$ is not too large). Besides, this baseline has a simple variation, where we can instruct the LLM to revise the output of first stage, which could also potentially improve the helpfulness and reduce harmfulness.
2. The experiments are not comprehensive. There are only two small tables. Only two relatively small models, one dataset, open-source models are considered. Since such method is more appropriate for proprietary models, experiments on proprietary models are needed.
3. The claim of "such alignment checking is not robust" (page 4, Robust Alignment Check Function) is not well-supported. What is the relationship between adversarial prompts [2] and such claim? In think this point is critical. If the authors cannot fully clarify the drawbacks of existing alignment checking methods, the motivation of this paper will seem to be weak.
4. The authors approximate $AC(\cdot)$ by only inspecting the existence of prefix in a pre-collected prefix set (e.g., “I can not”, “I’m
sorry”). However, is the approximation robust? It is unclear. Such prefixes may vary across different models, for example, some models may output "as a helpful and harmless chatbot, my job is to ....". Since there are so many potential prefixes, I do not think enumerating to construct a prefix set is a robust solution.
5. **Computational Cost**. The current calculation manner of computational cost is not convincing: authors seem to compare the per-token cost, however, this method requires much larger token length. Through a rough calculation, this method requires $n*(1-p)=20*(1-0.3)=14$ times of input cost, which has not been revealed by the authors.

### Questions
see weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
