# Improved Techniques for Optimization-Based Jailbreaking on Large Language Models

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
\textcolor{red}{\textbf{Warning:} This paper contains model outputs that are offensive in nature.}
Large language models (LLMs) are being rapidly developed, and a key component of their widespread deployment is their safety-related alignment. Many red-teaming efforts aim to jailbreak LLMs, where among these efforts, the Greedy Coordinate Gradient (GCG) attack's success has led to a growing interest in the study of optimization-based jailbreaking techniques. Although GCG is a significant milestone, its attacking efficiency remains unsatisfactory. In this paper, we present several improved (empirical) techniques for optimization-based jailbreaks like GCG. We first observe that the single target template of \texttt{``Sure''} largely limits the attacking performance of GCG; given this, we propose to apply diverse target templates containing harmful self-suggestion and/or guidance to mislead LLMs. Besides, from the optimization aspects, we propose an automatic multi-coordinate updating strategy in GCG (\textit{i.e.}, adaptively deciding how many tokens to replace in each step) to accelerate convergence, as well as tricks like easy-to-hard initialisation. Then, we combine these improved technologies to develop an efficient jailbreak method, dubbed $\mathcal{I}$-GCG. In our experiments, we evaluate on a series of benchmarks (such as NeurIPS 2023 Red Teaming Track). The results demonstrate that our improved techniques can help GCG outperform state-of-the-art jailbreaking attacks and achieve nearly 100\% attack success rate.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a new method for an optimization-based search of jailbreaking prompts for conversational LLMs fine-tuned for safety. While heavily inspired by prior work - notably the Greedy Coordinate Gradient (GCG), authors add three modifications that improve the attack success rate and convergence speed. First, they introduce the easy-to-hard initialization, starting by attacking questions that are known to be easier to jailbreak than others. Second, they add an additional target string to obtain in the jailbroken model, confirming that the output about to be generated is harmful. Third, the authors modify an update rule from a single-mutation evolutionary search on the jailbreaking string to within-step recombination of best-performing mutations. The authors call their method the Improved-GCG (I-GCG) and demonstrate its superior performance to the alternative methods on the AdvBench benchmark, achieving a 100% success rate, as well as faster convergence, achieving a 10x speed-up on the original method.

### Strengths
- The field of LLM jailbreaking is currently the focus of the LLM security community and is central to developing secure LLM-based products. As such, the research is timely and interesting.
- Authors perform an extensive comparison of their method not only to the original method but also to other alternative methods (Table 2)
- Authors investigate the attack convergence time and transferability, which are essential for real-world applicability
- Authors perform an ablation study, providing information to other researchers in developing their own attack methods
- Authors provide sufficient information and the code required to replicate their results

### Weaknesses
 - The paper is not well-structured, and even somebody familiar with the domain requires several re-reads to understand the authors' contribution and their interest in the real-world setting. A major rewrite is recommended, notably to better situate this work compared to prior knowledge, inspiration for this work, and the authors' contribution. For instance, putting forward benchmarking results would be helpful to understand the added value of this work better.
- Notably, the first two paragraphs, providing an introduction and an overview of the field, are full of citations with unclear relevance. 
 1. I do not understand the choice of Kasceni et al. 2023 and Chang et al. 2023 as references for the concept of LLMs, which, in my opinion, are entirely unrelated, much less landmark papers or recent reviews. The same criticism applies to all the citations in the following paragraph. 
 2. There are missing fundamental papers in the field to situate the paper and prior work, even for a topic expert who has not followed the field for a year. I believe [1-2] would be mandatory.
 3. In the second paragraph, each citation group needs a short introductory paragraph to explain their relevance/importance and to be broken into 2-3 citations at most. As such, groups of up to 8 citations are cited without clear motivation or reason to the reader and do not read as relevant.
- Additional landmark papers needed to situate the topic of research and contribution for the general public are missing in the "Related work" section, eg [3] for LLM-based jailbreak methods
- One of the essential improvements proposed by the authors - easy-to-hard initialization - requires knowledge of the themes for which LLMs are easier to jailbreak. This, in turn, would require a measured performance of the "difficulty" of jailbreaking across themes and LLM/LLM families, whether as found by the authors (e.g., convergence time to jailbreak from default initialization) or as reported by previous work. Not reporting such results makes the model's results significantly less useful and hard to validate.
- The addition of an explicit harm awareness prompt (e.g., "my output is harmful") seems to reduce the scope of attack to the outputs LLMs have been safety fine-tuned to recognize as harmful or harmfulness for which they can recognize from the context present in their training data. This seems to narrow down the scope of the attack. While this does not reduce the effectiveness of the attack on standard benchmarks, I believe this narrowing of scope requires discussion.

### Questions
- L178-L182: Why did you classify this approach, dependent on the attacker LLMs, with optimization-based jailbreak methods rather than with LLM-based jailbreak methods?
- L366-L367: While the usage of ChatGPT-3.5 is consistent with prior art, this model is known to be more prone to jailbreaks than more recent GPT-4, Claude, or LLaMA-3.X models. Could you please explain the choice of ChatGPT-3.5 here?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents an improved optimization-based jailbreak method for large language models (LLMs) called I-GCG, building upon the existing Greedy Coordinate Gradient (GCG) attack. The authors address the limitations of GCG, such as its low efficiency in generating jailbreak prompts, by introducing several advancements. Key improvements include:

	1.	Diverse Target Templates: Instead of using a single target template, I-GCG employs varied target templates with harmful self-suggestions to better mislead LLMs.
	2.	Automatic Multi-Coordinate Update Strategy: This strategy allows adaptive updates of multiple tokens at each iteration, accelerating convergence compared to the single-token updates in traditional GCG.
	3.	Easy-to-Hard Initialization: I-GCG begins with simple jailbreak cases to generate initial suffixes, which are then used as starting points for more complex jailbreaks.

Experimental results show that I-GCG achieves nearly 100% attack success rates on multiple LLMs and outperforms prior jailbreak methods in both effectiveness and efficiency. This approach significantly reduces the time required for successful attacks, advancing the field of adversarial attacks on aligned LLMs.

### Strengths
•	Enhanced Attack Efficiency: The proposed I-GCG method significantly improves upon traditional GCG by accelerating convergence with an automatic multi-coordinate update strategy. This reduces the number of iterations required and, consequently, the total attack time.
	•	Higher Success Rate: I-GCG achieves a nearly 100% success rate across various LLMs, outperforming other state-of-the-art jailbreak methods in effectiveness, especially on models with stronger security alignments.
	•	Diverse Target Templates: By using varied target templates with harmful self-suggestions, I-GCG effectively bypasses LLMs’ alignment mechanisms, showcasing a novel approach that enhances the jailbreak success rate.
	•	Efficient Initialization Strategy: The easy-to-hard initialization allows for effective scaling from simple to complex jailbreaks. This structured initialization improves both attack robustness and adaptability across a range of malicious prompts.
	•	Comprehensive Evaluation: The authors rigorously test I-GCG on multiple benchmarks and models, including those from the NeurIPS 2023 Red Teaming Track, providing strong empirical evidence for its superiority over previous jailbreak methods.
	•	Transferability: I-GCG demonstrates improved transferability of jailbreak prompts across different LLMs, indicating its potential to generalize effectively to a broader set of models and attack scenarios.
	•	Well-Defined Optimization Techniques: The paper provides clear mathematical formulations and experimental validation of the techniques used, such as the multi-coordinate update strategy, which supports the paper’s methodological rigor.

### Weaknesses
•	Scalability to Larger Models: While I-GCG shows strong performance on models such as LLAMA2-7B, the paper does not address scalability issues for substantially larger models (e.g., 70B+ parameters), where optimization costs and computational demands may significantly increase. The paper lacks a discussion on how the multi-coordinate update strategy would perform with the increased dimensionality of larger models' embedding spaces. It is unclear if the observed convergence speed would be maintained, or if the computational overhead would negate the benefits of the accelerated updates. Furthermore, the memory requirements for storing gradients and intermediate results during the optimization process could become a limiting factor for models with significantly larger parameter counts.
	•	Lack of Defensive Strategies Discussion: Although the study provides insights into vulnerabilities, it lacks a discussion on potential defense mechanisms or mitigations that could counteract the proposed jailbreak methods, which could be valuable for guiding future security improvements. The paper does not explore how techniques like adversarial training, input sanitization, or output verification might impact the effectiveness of I-GCG. A discussion of these defense strategies and their potential to mitigate the attack would provide a more complete picture of the overall security landscape and the practical implications of the proposed method.

### Questions
•	How is the ASR (Attack Success Rate) calculated? Does it only count as successful if it passes all three checks: rule-based judgment, GPT-3.5 check, and manual review?
	•	What does “average iterations” in Table 1 mean? Does it refer to the average number of iterations required to achieve a successful jailbreak for the first time with ASR?
	•	The paper mentions using GCG as the baseline; could you specify the number of candidates set for vanilla GCG in this context?

### Soundness
4

### Presentation
4

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
This paper focuses on improving optimization-based jailbreaking techniques for large language models (LLMs). The authors note that while existing methods like the Greedy Coordinate Gradient (GCG) attack have made progress, there is room for improvement in attacking efficiency. The paper contributes by identifying limitations in existing jailbreaking techniques and proposing novel strategies to enhance both the effectiveness and efficiency of jailbreaking LLMs. The developed I-GCG method demonstrates significant improvements over previous methods in terms of attack success rate and transferability.

### Strengths
The paper presents a combination of techniques to improve optimization-based jailbreaking. The idea of using diverse target templates with harmful self-suggestion and guidance is original. The automatic multi-coordinate updating strategy adaptively decides the number of tokens to replace in each step. The authors use multiple datasets (AdvBench and HarmBench) and several threat models (VICUNA-7B-1.5, GUANACO-7B, LLAMA2-7B-CHAT, and MISTRAL-7B-INSTRUCT-0.2) to evaluate the proposed I-GCG method. This wide range of evaluations provides a robust assessment of the method's performance under different conditions.

### Weaknesses
The paper focuses on improving the jailbreak attack but does not extensively explore how the proposed techniques interact with existing or potential defense mechanisms in LLMs. Understanding how LLMs can defend against the enhanced I-GCG attack and proposing counter-defense strategies would make the research more complete. This could involve testing the method against LLMs with advanced safety features or fine-tuned with specific defense-oriented training.

The easy-to-hard initialization and the automatic multi-coordinate updating strategy are effective in the current setup, but they might be sensitive to the initial conditions and hyperparameter choices. A more in-depth analysis of the stability and robustness of these techniques under different initialization values and optimization parameter settings could strengthen the method.

### Questions
1） In the experiment using HarmBench (NeurIPS 2023 Red Teaming Track), the target response format was set differently than in the other experiments. What was the rationale behind this change, and how did it impact the comparability of the results?、
2）The automatic multi-coordinate updating strategy seems to be a key improvement in I-GCG. However, the paper does not discuss how the choice of the top-K tokens and the token combination process might affect the diversity and quality of the generated jailbreak suffixes. Can you provide more insights into this?
3）The current work focuses on jailbreaking LLMs in the context of generating harmful text. How applicable are the proposed techniques to other potential security threats or malicious uses of LLMs, such as information extraction, influence operations, or evading content filters in different modalities (e.g., image generation)?

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
3

### Summary
This work proposes I-GCG, an optimization-based jailbreak to improve ASR and efficiency. Compared to current methods, I-GCG formulates its optimization goal by integrating harmful information into the standard template. Also, they introduce an automatic multi-coordinate updating strategy that selects the top-p single-token suffix candidates to generate multi-token suffix candidates. Finally, the authors incorporate an easy-to-hard initialization mechanism, initially targeting a simpler jailbreaking task and then transferring the optimized suffix to more challenging tasks. Experimental results demonstrate the superior ASR and reduced time cost compared to other jailbreaks against several LLMs.

### Strengths
1. The authors present specific examples (Figs. 1-2 and the highlighted sentences on page 5) to emphasize the limitations of current jailbreaks that rely on a single target template, thereby distinguishing this work from previous studies.
2. This paper is well-structured, with a clear motivation and a methodology that is easy to follow.
3. The study includes recent jailbreaks published in 2023 and 2024 for comparison. The results show a high ASR and reduced time costs, supporting the contributions claimed in this paper.

### Weaknesses
1. This paper presents an incremental improvement over existing works. While the three proposed techniques differ from previous jailbreaks, their novelty is limited. The core idea of optimizing a suffix to elicit a desired response is not new, and the specific modifications, such as incorporating harmful information into the template and using a multi-coordinate update, appear to be relatively straightforward extensions of existing gradient-based optimization methods. The paper lacks a deep theoretical analysis of why these specific modifications lead to significant improvements, making the contribution seem more empirical than fundamental.
2. The reasons behind the improvements in jailbreak effectiveness and efficiency from the reformulated optimization goal and multi-coordinate updating strategy are not thoroughly analyzed. While the paper claims that incorporating harmful information into the template improves the attack, it does not provide a clear explanation of the underlying mechanism. Similarly, the multi-coordinate update is presented as a speedup technique, but the paper does not delve into the convergence properties or potential trade-offs of this approach. A more rigorous analysis of the optimization landscape and the impact of these modifications is needed.
3. Fig. 5 illustrates different levels of difficulty associated with malicious questions for successful jailbreak attempts. However, this result is presented solely for LLAMA2-7B-CHAT, which weakens the motivation for using the easy-to-hard initialization approach, as the difficulty of jailbreaking questions may vary on other models. Besides, this approach incurs extra time costs by requiring the jailbreaking of an easy task, raising the question of whether allocating extra time to a simple task can actually result in greater time savings on a complex task. The paper does not provide a clear justification for the assumption that an easy-to-hard initialization will consistently lead to faster convergence on more complex tasks across different models.
4. I-GCG achieves high ASR on only one dataset (AdvBench). Given the straightforward nature of the methodology, experiments on additional datasets and models would provide a more comprehensive assessment. The lack of evaluation on diverse datasets and models limits the generalizability of the findings. The paper needs to demonstrate that the proposed method is robust and effective across a broader range of scenarios.

### Questions
1. In equation 6 and 7, $x^S(0)$ and $x_0^S$ serve as initial jailbreak suffixes for the start of optimization. It is unclear why the authors formulate them as constraints.
2. The analysis of the difficulty of jailbreaking different questions, particularly whether this difficulty remains consistent across other models, is lacking.
3. It is unclear whether allocating extra time to a simple task can actually result in greater time savings on a complex task.
4. Jailbreaking results on additional models, such as LLAMA2-7B alongside LLAMA2-7B-CHAT, are worth discussing. Experimental results on more datasets could further validate the effectiveness of the proposed method.
5. Providing further elaboration on the contributions of this work would be beneficial.

### Soundness
2

### Presentation
3

### Contribution
2
