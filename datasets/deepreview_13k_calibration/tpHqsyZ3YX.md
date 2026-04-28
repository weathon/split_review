# ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs

- Decision: Accept
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
As large language models (LLMs) are increasingly being integrated into various real-world applications, the identification of their vulnerabilities to jailbreaking attacks becomes an essential component of ensuring the safety and reliability of LLMs. 
Previous studies have developed LLM assistants, known as the adversarial prompter, to automatically generate suffixes that manipulate target LLMs into generating harmful and undesirable outputs.
However, these approaches often suffer from low performance or generate semantically meaningless prompts, which can be easily identified by perplexity-based defenses.
In this paper, we introduce a novel two-stage method, $\texttt{ProAdvPrompter}$, that significantly improves the performance of adversarial prompters.
In $\texttt{ProAdvPrompter}$, the first stage (Exploration) utilizes the loss information to guide the adversarial prompter in generating suffixes that are more likely to elicit harmful responses.
Then the second stage (Exploitation) iteratively fine-tunes the prompter using high-quality generated adversarial suffixes to further boost performance.
Additionally, we incorporate the prompt template to aid in the Exploration stage and propose a filtering mechanism to accelerate the training process in the Exploitation stage.
We evaluate $\texttt{ProAdvPrompter}$ against the well-aligned LLMs (i.e., Llama2-Chat-7B and Llama3-chat-8B), achieving attack success rates of 99.68% and 97.12% respectively after 10 trials on the AdvBench dataset, thereby enhancing performance by $\sim 2$ times compared to previous works.
Moreover, $\texttt{ProAdvPrompter}$ reduces training time by 20% on Llama3-Instruct-8B, generates more generalized adversarial suffixes, and demonstrates resilience against the perplexity defense.
An ablation study further evaluates the effects of key components in $\texttt{ProAdvPrompter}$ (the prompt template and the filtering mechanism).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Build upon the previous work[1], proadvprompter propose a two-stage training technique with dataset filter in the second stage to obtain a generation model to produce jailbreak suffixes.

### Strengths
The method seems very to be effective, achieving a very high ASR.

### Weaknesses
1. The novelty of this work is doubtful, since the first stage Exploration pipeline is exact the same as AdvPrompter, and proposing a two-stage fine tunning workfolw with filter in the second stage seems to be lack of novelty. Moreover, there seems to be no significant technique contribution and methodology difference between two stage, as both are collecting the dataset (intact or filtered) first and then tuning the model. Maybe authors could consider the difference between various fine tune method and investigate their impact on training the jailbreak prompters to give a technique insightful conclusion. For example, is LoRA much more robust to get a better jailbreak prompter than SFT, or something like that. Furthermore, it would be better if the author could explain the intuition why involving a exploitation stage can significantly improve the ASR, and give some ablation studies to show how the proposed exploitation stage contribute to this result.
2. It seems the ProAdvPrompter setup is different across different target model, which might imply the two-stage pipeline is not robust across different models.

Typos:
In line 135, the hyperlink refers to Equation 2, which should be Equation 1 instead.
The input of Algorithm 1 contains repetitive discription of "the initial parameter theta_0"

### Questions
1. In table 1, can you further explain what is the term "Adaptive to input"? do you mean universality of the suffix?
2. In figure 2, what is "template alone" methods? There is no explanation abut this term till the end of this section.  In addition, Where are these numerical results from? For AdvPrompter results in Figure 2.a, the Vicuna-7B and Vicuna-13B results seem to be quoted (exact the same) from the AdvPrompter original paper[1], while the reported Mistral ASR 98.1% does not align with the Mistral ASR in AdvPrompter. 
3. Is the tested ProAdvPrompter universal or not. (line 122 specify the following discussion to be all universal, but the examples given in Table 4 are not)

### Soundness
3

### Presentation
3

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
This study proposes ProAdvPrompter, a two-stage approach to enhance adversarial prompting effectiveness. During the Exploration stage, loss feedback directs the prompter to generate suffixes more likely to induce harmful responses. In the Exploitation stage, ProAdvPrompter undergoes iterative fine-tuning with high-quality adversarial suffixes to further improve performance.

### Strengths
1. This paper is well-written, with the authors providing a clear and comprehensive presentation of the algorithm process and their perspectives.
2. The proposed method achieves state-of-the-art ASR performance compared to the selected baseline attacks.
3. The baselines chosen by the authors are all recent, reflecting a strong selection of relevant comparisons.

### Weaknesses
The method proposed in this paper shows a slight lack of innovation.
It consists of two stages: in the first, Exploration stage, the authors adopt the search strategy of Paulus et al. (2024) along with beam search. In the second, Exploitation stage, they apply fine-tuning to produce high-quality adversarial suffixes. While the second stage displays more originality than the first, it generally divides into two sub-phases—dataset generation and training—to yield refined adversarial suffixes. Although effective, this approach remains relatively conventional.


I have several concerns about this paper:

Firstly, the contribution of this paper to the community is not convincing. The method of obtaining better experimental results through ensemble learning has already been widely used in the community since the era of machine learning. The author’s paper seems more like an application of ensemble learning methods.

Secondly, I still don’t understand why the time required for the author to use more methods would be shorter than the time needed to use just one method.

### Questions
1. In Table 2, the authors present experiments on only one dataset, Advbench; including additional datasets would enhance the comparison. 

2. In lines 394-395, the authors state that the evaluation primarily focuses on ASR, training time, and generation time. However, Table 2 omits results for training and generation times. Additionally, in Figure 4, the authors display only Advprompter’s training time, while training times for AutoDan and GCG are not shown, though generation times for AutoDan, Advprompter, and GCG are included. A complete presentation of all experimental results is recommended for thoroughness.

### Soundness
2

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
This paper introduces a novel two-stage method, which significantly enhances the performance of adversarial prompters. The Exploration stage uses loss information to guide the prompter in generating harmful suffixes, while the Exploitation stage iteratively fine-tunes the prompter to further improve performance.  The paper also demonstrates reduced training time and resilience against perplexity defense, with an ablation study further evaluating the effects of key components.

### Strengths
- The ProAdvPrompter method proposed in the article achieves a very high attack success rate on two well-aligned LLMs. The article validates the performance of the method on two mainstream open-source LLM models, such as llama2-chat and llama3-chat.

- The article analyzed the limitations of existing state-of-the-art methods, and specifically proposed improvement strategies with clear research motivation.

- The method section of the article is very detailed, clearly demonstrating the principles of the proposed method.

### Weaknesses
 - It seems that the method in this article has not been experimented on closed LLMs (such as transfer-attacking), please refer to the [1]. We all know that in practical applications, black-box models occupy a considerable market share and pose greater security issues. Therefore, can the method proposed in the article also reveal the security issues of black-box models?
- Although the method has achieved excellent performance, the entire pipeline appears to be quite lengthy, which may pose significant difficulties for replication.


### Questions
- Although the method in the paper has achieved outstanding performance, there seem to be too many adjustable factors in the two-stage training process, such as the parameter $\gamma$ in line 19 of algorithm 1, $k$ in line 15, $T_{1}, T_{2}$, etc. This raises the question of whether the method in this paper is sensitive to these parameters? As far as I know, exploring all possible parameter settings requires a significant amount of effort.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a two-stage method called ProAdvPrompter which uses adversarial prompters (LLM) to generate adversarial suffixes. ProAdvPrompter achieves high attack success rate, with good readability, adaptability and fast speed.

### Strengths
1. The experimental results suggest ProAdvPrompter achieves high attack success rate, with a low perplexity.
2. The exploration and exploitation of ProAdvPrompter is an interesting and effective idea.
3. The paper is well-written and clearly expressed.

### Weaknesses
1. The method needs to fine-tuning the adversarial prompter at each stage. Although once the adversarial prompter has been trained, the attack process is fast. But I still concern the training cost of adversarial prompter at training stage. 
2. The experiment results suggest ProAdvPrompter achieves high ASR. Is the reported ASR tested on safety questions in other domain? I concern the two-stage fine-tuning makes the adversarial prompter overfitted on the trained data

### Questions
1. is the paper evaluates the transferability of the generated attack prompts? (across datasets or target LLMs)
2. Will an adversarial prompter without safety alignment will produce better results?
3. The influence of adversarial prompter. Will a bad adversarial prompt LLM produces a poor ASR?

### Soundness
3

### Presentation
3

### Contribution
3
