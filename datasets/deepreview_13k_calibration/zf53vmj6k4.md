# Do LLMs Have Political Correctness? Analyzing Ethical Biases and Jailbreak Vulnerabilities in AI Systems

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 1, 3, 8

## Abstract
\begin{center}
    \textcolor{red}{Warning: This paper contains potentially offensive and harmful text.}
\end{center}
Although large language models (LLMs) demonstrate impressive proficiency in various tasks, they present potential safety risks, such as `jailbreaks', where malicious inputs can coerce LLMs into generating harmful content. To address these issues, many LLM developers have implemented various safety measures to align these models. This alignment involves several techniques, including data filtering during pre-training, supervised fine-tuning, reinforcement learning from human feedback, and red-teaming exercises. These methods often introduce deliberate and intentional biases similar to Political Correctness (PC) to ensure the ethical behavior of LLMs. In this paper, we delve into the intentional biases injected into LLMs for safety purposes and examine methods to circumvent these safety alignment techniques. Notably, these intentional biases result in a jailbreaking success rate in GPT-4o models that differs by 20\% between non-binary and cisgender keywords and by 16\% between white and black keywords, even when the other parts of the prompts are identical. We introduce the concept of \textit{PCJailbreak}, highlighting the inherent risks posed by these safety-induced biases. Additionally, we propose an efficient defense method \textit{PCDefense}, which prevents jailbreak attempts by injecting defense prompts prior to generation. \textit{PCDefense} stands as an appealing alternative to Guard Models, such as Llama-Guard, that require additional inference cost after text generation. Our findings emphasize the urgent need for LLM developers to adopt a more responsible approach when designing and implementing safety measures. To enable further research and improvements, we open-source our \href{https://anonymous.4open.science/r/PCJailbreak-F2B0}{code and artifacts} of \textit{PCJailbreak}, providing the community with tools to better understand and mitigate safety-induced biases in LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work focuses on using potential biases in a model to jailbreak the model, by associating a request with a particular group.

### Strengths
+ Exploring how biases might affect jailbreaking is an interesting and important idea.

### Weaknesses
+ There are some major improvements to be made for the experimental results. First, all experiments are run with sampling (“the default sampling temperature”), yet there are no confidence intervals. It is entirely possible that Table 2 is a function of small perturbations or random noise since the effect sizes are small. Second, the dataset itself is small, so it could be statistically underpowered for such small effect sizes. Note: at this small of a sample size the minimum detectable effect size is rather large for a binomial distribution. Third, there's a crucial baseline missing: what about just replacement with random adjectives to rule out that this isn't just a function of (un)lucky perturbations. To build more confidence in the result, suggest that: (1) increase the size of the dataset; (2) run sampling multiple times and report confidence intervals; (3) compare a baseline with random adjectives. 
+ Typically defenses come at a cost to utility. This defense in particular, could affect normal task performance, but there is no evaluation of utility here. To improve the paper and build more confidence that the defense does not induce side effects, suggest running on a suite of standard benchmark tasks/evals to see how the defense affects performance.

Minor:

Table 1’s headers are backwards?

### Questions
+ What was the temperature for each model (where it is known)?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
In this paper, the authors investigate the intentional biases of LLMs and how these biases can be exploited for jailbreak attacks. They created a jailbreak attack using pairs of privileged and marginalized keywords, along with prompts that ask the LLM to write a fictional story and include harmful questions. This technique, called 'PCJailbreak,' exploits these biases by incorporating different demographic keywords in the prompts. Additionally, they propose 'PCDefense,' a prompt template that uses system prompts and prompt suffixes to adjust these biases and prevent attacks.

### Strengths
---> The paper presents an interesting aspect of safety training: safety measures intended to make LLMs more ethical can actually create exploitable biases.


---> Experiments were conducted across a variety of LLMs, including both open-source and black-box models.

### Weaknesses
 --->> 1: The number of keyword pairs is relatively small, and the JailbreakBench dataset being used is also limited. Increasing the number of keyword pairs and incorporating a more comprehensive dataset could have made the experiments more rigorous.

--->>> I believe one of the weaknesses of the paper is that it limits the experiments to a few keyword pairs and does not include an ablation study.

--->>>> What will happen if we replace the words in pairs with something entirely different? Will we get the same results?

--->>>> Additionally, the prompt structure used in the experiment does not determine whether the jailbreak occurs solely due to the request to write a fictional story or because of the presence of marginalized words.

--->> 2: In the PC Defense, “IF THE REQUEST INCLUDES HARMFUL CONTENT, DO NOT RESPOND.” is added as the suffix prompt.

---->>> In in-context learning, the model response is dependent on the input label distributions and formatting, and asking the LLM to basically check every prompt is very obvious to make LLMs to scan its input.

--->>> This is likely that this suffix alone will decrease the ASR without the ‘system prompt’.

--->>> I believe an ablation study should have been done to measure the efficacy of the proposed prompt.


--->> 3: Line 377: "By using a defense prompt, our defense mechanism elicits the refusal of a wide range of harmful content without requiring significant additional computing resources, which makes it an attractive alernative to Guard Models.” --- I could not find any evidence to support this claim in the paper.

### Questions
--->> I think the paper should provide some context on 'political correctness' for readers, as well as the motivation behind studying it.

--->> “Line 187: Our work builds on the existing body of research by focusing on the paradoxical consequences of  intentional biases introduced for safety purposes “
	----->>> I am not entirely sure what this sentence refers to. I think adding references and examples would provide a better explanation.

--->> Line 228-229: I believe there is a conflict in stating that the refusal prefix is the target prefix. In line 222, the target responses refer to malicious responses, while in line 232, they point to refusal phrases

--->> Line 166: Missing reference for ‘walkerspider 2022’  	

--->> line 378: please fix spelling of ‘alernative’ -> ‘‘alternative’

--->>  I am quite confused by the subheading '3.1.2 Formulation': what is being formulated here?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces PCJailbreak, a method designed to analyze and exploit politically correct (PC) alignment-induced biases in LLMs, which lead to differing jailbreak success rates across various demographic group keywords (e.g., gender, race). The PCJailbreak framework systematically reveals how biases injected for safety purposes can paradoxically enable effective jailbreaks, with observable disparities between privileged and marginalized groups. Additionally, the paper presents PCDefense, a lightweight defense method that mitigates these vulnerabilities through prompt-based bias adjustments without incurring additional inference overhead. However, here are a few concerns:

### Strengths
1. **Extensive Model Evaluation**: The paper evaluates a wide range of models, including some of the latest LLMs, providing a comprehensive view of jailbreak vulnerabilities across different architectures and alignment techniques.

2. **Community Contribution**: By open-sourcing the code and artifacts of PCJailbreak, the authors facilitate further research on bias and jailbreak vulnerabilities, promoting transparency and enabling the community to explore and develop more robust defense strategies.

### Weaknesses
1. **Motivation**: The paper categorizes jailbreak attacks into manually written prompts and learning-based prompts, stating that learning-based jailbreak prompts rely on gradient information and that these prompts are often nonsensical sequences. However, this overlooks natural-language jailbreak prompts, such as PAIR [1] and DeepInception [2], which are not solely gradient-based and produce coherent, meaningful language. Additionally, for manual attacks, approaches like GUARD [3] build on existing manually crafted jailbreak prompts, refining them over time to remain effective.

2. **Scope of Jailbreak Attacks**: Much of the related work on jailbreak techniques in this paper appears to focus on approaches up to 2024. Given the rapid advancements in jailbreak methodologies, the paper should provide a more detailed discussion of recent jailbreak attacks, such as works like [4] and [5].

3. **Keyword Generation Methodology**: The approach of directly prompting the LLM to generate keywords introduces potential issues. For instance, the generated keywords may lack diversity, as the LLM could repeatedly produce similar terms based on its training biases. Additionally, there is no evaluation or filtering mechanism to determine which keywords are more effective or appropriate for distinguishing between privileged and marginalized groups.

4. **Ambiguity in Baseline Definition and Scope of Comparison**: While Table 2’s caption states it shows “baseline success rates, marginalized success rates, privileged success rates, and the difference between marginalized and privileged success rates,” the paper does not clearly define what constitutes the "baseline success rate." Additionally, to strengthen the evaluation, it would be beneficial to include comparisons with a broader range of jailbreak attacks.

5. **Defense Baselines**: There are some relevant papers at the prompt level to prevent harmful output, such as [6], [7], and [8]. As PCDefense also adds prompts to model system prompts and suffix prompts, it should compare the effectiveness with these methods.

### Questions
See the Weaknesses above.

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
This paper introduces a jailbreaking method that is based on pitting goals of fairness and helping marginalized groups against goals of behaving harmlessly. They use a system prompt telling the model to treat everyone fairly and deliver harmful queries to the model with statements about the user being from a marginalized group. It can moderately increase model compliance with harmful requests across models they tested.

### Strengths
S1: Figure 1 is clear and compelling. Although Figure 2 is visually messy with the "Safety alignment" words across it. 

S2: I am pretty familiar with the jailbreaking lit and jailbreaking methods. As best I can tell, this paper is very novel. In retrospect, it seems almost obvious that this would work. But this jailbrekaing method is never something I had thought of or heard of. 

S3: I generally think that the overall contribution is clear and useful. I work with jailbreaking a lot, and I think that this paper is helpful and citable.

### Weaknesses
W1: I would recommend considering a different title. "Political correctness" is not a term that has the same definition to everyone, and it's a political buzzword. 

W2: I would recommend that the abstract text be revisited in order to be more specific. There isn't a full description of the attack or defense methods used in the abstract itself. I also think that the abstract could be updated to have smoother writing and less fluff -- I think that some of the sentences in it (especially early) are not very relevant to the specific contributions of the paper.

W3: There is a claim in the paper that political correctness biases are introduced into models from the fine-tuning process. But this seems unjustified. I don't see why they wouldn't also be a result of pretraining data. 

W4: I think that section 2.2 is not the most thorough. It could be expanded to better discuss related jailbreaking techniques that involve persuasion and personas. 

Minor: A "Walkerspider" reference might have a typo and need to be cleaned up. 

Minor: I would recommend having a different example in figure 2 and 4 so that readers can see more diverse examples. 

Minor: Why were not claude models tested?

Minor: It's principal component analysis, not "principle"

### Questions
See above

### Soundness
3

### Presentation
2

### Contribution
2
