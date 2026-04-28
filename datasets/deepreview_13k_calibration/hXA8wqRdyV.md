# Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks

- Decision: Accept
- Avg Score: 6.14
- Scores: 6, 8, 6, 6, 6, 5, 6

## Abstract
\noindent
    We show that even the most recent safety-aligned LLMs are not robust to simple \textit{adaptive} jailbreaking attacks. First, we demonstrate how to successfully leverage access to \textit{logprobs} for jailbreaking: we initially design an adversarial prompt template (sometimes adapted to the target LLM), and then we apply random search on a suffix to maximize a target logprob (e.g., of the token \textit{``Sure''}), potentially with multiple restarts. In this way, we achieve 100\% attack success rate---according to GPT-4 as a judge---on Vicuna-13B, Mistral-7B, Phi-3-Mini, Nemotron-4-340B, Llama-2-Chat-7B/13B/70B, Llama-3-Instruct-8B, Gemma-7B, GPT-3.5, GPT-4o, and R2D2 from HarmBench that was adversarially trained against the GCG attack. We also show how to jailbreak \textit{all} Claude models---that do not expose logprobs---via either a transfer or prefilling attack with a \textit{100\% success rate}. In addition, we show how to use random search on a restricted set of tokens for finding trojan strings in poisoned models---a task that shares many similarities with jailbreaking---which is the algorithm that brought us the \textit{first place} in the SaTML'24 Trojan Detection Competition. The common theme behind these attacks is that \textit{adaptivity} is crucial: different models are vulnerable to different prompting templates (e.g., R2D2 is very sensitive to in-context learning prompts), some models have unique vulnerabilities based on their APIs (e.g., prefilling for Claude), and in some settings, it is crucial to restrict the token search space based on prior knowledge (e.g., for trojan detection).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In their study, the authors explore the vulnerability of safety-aligned Large Language Models (LLMs) to adaptive jailbreaking attacks, demonstrating that even models designed for robustness against harmful prompts can be compromised. They employ a methodology based on modifying adversarial prompts and optimizing suffixes via random search to maximize target log probabilities, achieving a 100% success rate across several LLMs including Vicuna-13B, Mistral-7B, and different versions of GPT and Claude. This paper underscores the adaptability required in attack strategies, tailored to exploit specific model vulnerabilities and interfaces, and extends their findings to the detection of trojan strings in poisoned models, highlighting significant security concerns for real-world applications of LLMs.

### Strengths
- This paper raises an interesting perspective on the safety vulnerabilities in LLMs, highlighting the critical need for ongoing advancements in AI security to effectively address these emerging threats.

- This paper is commendable for its extensive experimental coverage, which spans a wide array of popular LLMs, providing a comprehensive understanding of the techniques’ effectiveness across different model architectures and configurations.

### Weaknesses
 - The paper heavily utilizes custom prompt templates that instruct the LLM to bypass safety mechanisms by avoiding certain words and phrases, which appears to significantly contribute to the success of the attacks. However, the roles and effectiveness of random search and self-transfer techniques are not thoroughly discussed beyond demonstrating an increase in attack success rates. A deeper exploration of how these methods specifically enhance the attacks, such as by analyzing the token-level changes introduced by random search or the transferability of these changes across models, could provide a clearer picture of their contribution and potential for generalization across different models.

 - While the paper provides interesting insights into exploiting LLM vulnerabilities through prompt engineering, it seems to lack depth in novel algorithmic development or thorough analytical rigor. The random search algorithm, while effective, is not a novel contribution in itself, and the paper does not provide a detailed analysis of why this particular method works well in this context compared to other optimization techniques. Furthermore, the paper does not explore the limitations of the proposed approach, such as its sensitivity to the initial random seed or the computational cost of the random search process.

### Questions
- Can the authors provide more detailed explanations of how the adversarial suffixes were optimized? What specific characteristics of these suffixes make them effective in bypassing the safety mechanisms of LLMs?

- The study employs a variety of custom prompts combined with different techniques across several LLMs, leading to diverse outcomes. Can the authors provide a deeper analysis or discussion on how different prompt configurations influenced the effectiveness of attacks across the models tested?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents results for adaptive attacks on a variety of models. They demonstrate that it is possible to circumvent existing defenses by using attacks targeted to the model/defense. Their attack uses a random search based attack to generate an adversarial suffix, in addition to a prompt customized to the model being attacked. They demonstrate that their attack can successfully attack GPT-4o and other closed source models, in addition to a range of open source models.

### Strengths
1. This paper demonstrates that existing defenses are quite easy to circumvent using adaptive attacks. The combination of prompt engineering and adversarial suffix search is a good demonstration of how different techniques may be combined to effectively attack models.

2. Especially as research on defenses and attacks progress, adaptive attacks become more realistic possibilities. This is a good demonstration of their effectiveness.

3. Experiments are performed on a wide range of models, both open and closed source.

4. The efficacy of the random-search based attack is important, and demonstrates that closed-source models are more vulnerable than previously thought.

### Weaknesses
Most weaknesses in this paper have to do with organization or comparison to prior results. However, they are significant enough that I am not comfortable accepting the paper without these points resolved:

## 1. Comparison to prior work

My main concern is that the evaluation comparisons are very inconsistent. Whereas this work presents their own evaluations using a split of 50 samples from AdvBench, they present comparisons to prior work using different data and evaluation methods. While there are notes on this in the text, this is not a fair comparison of results. While the results presented are convincing, the lack of adequate comparison makes it very hard to situate this work in existing literature and will make it very hard to build upon. The prior attacks are also not clearly referenced in the main summary in Table 1, making it impossible to see what is being compared against. Comparisons between this work and prior work needs to be standardized.

## 2. Organization
The organization of the paper is somewhat hard to follow, particularly when it comes to Section 5. It was not entirely clear to me how this section fits with other results in the paper, and I feel that it could be better contextualized.

## 3. Data documentation
Documentation on data used for training and testing is vague. For Table 1, it says results are reported on a subset of 50 samples from AdvBench, however it is not clear what this subset is, or whether this is the set of 50 that is used to train the attack.

### Questions
1. What is considered a significant number of false positives by the LLM judge?

2. Is the training and test data distinct for this attack? It is not clear from the text, which mentions a set of 50 samples from AdvBench for both.

### Soundness
2

### Presentation
2

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
This paper proposes an adaptive jailbreaking attack, which aims at attacking safety-aligned language models (LLMs), demonstrating that even the latest models are vulnerable to these attacks. The authors use targeted prompts and random search methods to bypass safety measures in models, achieving a 100% attack success rate across multiple models with additional enhanced methods. The experimental results include a range of models and APIs, showing that approaches like self-transfer, prefilling, and targeted adversarial suffixes effectively achieve jailbreaks across various LLMs. Additionally, the paper reports success in trojan detection by applying similar techniques.

### Strengths
1. This paper focuses on black-box models. The proposed method can have a very high attack success rate on close-source LLMs such as GPT and Claude.

2. The analysis of self-transfer is insightful. 

3. Beyond jailbreaking, the paper successfully applies its adaptive techniques to trojan detection.

### Weaknesses
1. Though the proposed method is designed for black-box models, attacking black-box models such as GPT4o highly relies on the powerful initial prompt. And in the paper, the authors use a custom prompt for GPT4o, which restricts the usage of the proposed method.

2. The search space for the proposed method is very large, how to effectively search the replaced token is a problem that this paper does not discuss (for jailbreaking).

3. The attack strategies are tailored to individual models, which limits their generalizability and may require frequent updates as models evolve.

### Questions
1. How do the authors guarantee the effectiveness of random search?

### Soundness
3

### Presentation
3

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
The paper discusses methods for jailbreaking different frontier LLMs, achieving high success rates across many LLMs.

### Strengths
The results are fairly strong, but the insights from the paper are not so clear. The paper also has missing baselines and overclaim at points (see my review). To the authors: if you fix those, I would be happy to recommend acceptance.

- The results overall seem strong in terms of ASR, especially with the range of models tested. Good job.
- I like the self-transfer approach, this makes sense.

### Weaknesses
 - I'm left uncertain what the main message or contribution of the paper is. Prefill? Log-prob random search? Adaptivity? I'd suggest trying to focus more on some key take aways, and linking the different sections of the paper. I also don't really understand how the backdoor / trojan section links to the rest of the paper. Though the approach in that section made sense.
- One weakness with the attack is that it would be extremely easy to detect with monitoring. E.g., the user making the request "don't start with \"I can't assist with that\"" is suspicious. I think this is fine, but please discuss this in the paper.
- There are many missing baselines, such as Many Shot Jailbreaking, AutoDAN. I think MSJ is likely to be an effective attack in particular, and I would expect it to get 100% success rate? Is there are reason you didn't include this?

### Questions
- *Pg 3: why are system prompt changes made for Claude? Are the results in Table 1 made with the modified system prompt? If so, Table 1 seems to be overclaiming.
- In table 1, I don't fully understand what the "prev" and "Ours" is? Because there are e.g., known jailbreaks on Claude Opus (Many Shot Jailbreaking, Pliny's Attacks). As a result, Table 1 seems to be overclaiming to me.
- How sensitivity are the results to the 10/10 GPT-4 Jailbreak Score?
- Do you search for universal adversarial suffixes? Or single ones?
- Line 220: the self-transfer approaches makes sense to me, I like it. The main question I have is how you are choosing / ranking the difficulty of different prompts?
- "Recent work showed the possibility of implanting backdoor attacks during the RLHF training
of LLMs by poisoning a small percentage of the preference data with a universal suffix." Please add citations.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper develops a prompt template that is modified with an adversarial suffix found through random search that jailbreaks all investigated models on nearly all investigated harmful requests. Furthermore, the random search is proposed to be initialized on adversarial suffixes found on easier-to-jailbreak requests. For Claude models where random search can't be performed because there is no access to the logprobs, a prefilling attack is proposed. Lastly, the paper provides a simple method to find triggers in models trained with backdoors.

### Strengths
* The paper is very well written and easy to follow.
* The proposed method outperforms the state-of-the-art in jailbreaking for a wide-range of current LLM models.
* The proposed method on finding triggers in backdoored models is simple and won a recent competition.  
* The code is included in the submission.

### Weaknesses
1. The cornerstone of the method seems to be the static prompt template from Fig. 1, which is then slightly adapted with an adversarial suffix found through random search. Here, I wonder what is the actual scientific value and contributions to the scientific community. In particular, it was already known that safety-aligned LLMs can be jailbreaked and it's not surprising that with more engineering effort, the jailbreaking percentage can be further increased. In particular, there are no guidelines (or systematic method) presented on how the prompt template was created or could be adapted for other models. Such insights/guidelines for adaptive attack generation are e.g., provided by Tramèr et al. (2020) for image classification. That such insights will be given is mentioned in lines 93-98 in the main draft, however, I could not find such insights in the subsequent text. 
2. The adaptivity of the attack is limited. This is related to the above point that it is based on a static prompt template reused for most models (except e.g., GPT-4o which has its own prompt template). While the random search of course adapts the method slightly to each model, an adaptive prompt design seems crucial (given e.g. 100% ASR of the prompt alone on GPT-3.5 Turbo, for which it was developed, and close to 0% on the other models).
3. The part on trojan detection seems rather disparate from the rest of the paper. In particular, in the related work, backdoor attacks for LLMs are not discussed and no single work on detecting triggers or on backdoor attacks in general is cited. (Backdooring is also never explained.)
4. I'm missing some experimental details and refer to the questions for this.

Minor weakness:  
5. Slight overstatement. In line 82/83 and TL;DR 100% attack success rate is claimed on all leading safety-aligned LLMs. GPT-3.5 Turbo is defined as one of such leading safety-aligned LLMs. However, GPT-4 Turbo has an attack success rate of 96%.

### Questions
1. Self-transfer: I wonder how the authors concretely define a simple example? 100% ASR with pure RS? What if no sample has 100% ASR? Which of the "simple examples" do you choose to use to initialize the RS for the hard examples? Does it make a difference which ones you choose?
2. Prefilling: Can you provide details on how the prefilling option is exactly used? 
3. From combinatorial optimization, it is known that initialization for random search is important (or for any local search algorithm). However, for me, it is not clear if the benefit is actually from the initialization point, or because the random search is given now "twice the budget". I.e., it can first search an adversarial suffix with N=10.000 and then optimize it for another prompt again with N=10.000.
4. What is the effectivity of the random search + self transfer without using the particular static prompt template? E.g., just providing the goal and adv_suffix? Connected, have you ablated parts of the prompt template?

Minor
* Link Appendix A.2 in Section 5, I was wondering what k you chose and by accident discovered you give the details there. I think, one could probably already include this information in the main text.
* Line 423: Abbreviation RLHF never introduced before.
* Figure 4 (Appendix B) is not color-blind friendly. I can't distinguish 15 from 25 tokens and 5 from 60 tokens.

Given the weaknesses and questions are appropriately addressed, I'm considering adapting my score.

**References**.  
Tramèr et al. "On adaptive attacks to adversarial example defense", NeurIPS 2020

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an adaptive attack that specifies a set of prompt templates and uses a random search algorithm to iteratively craft jailbreaking prompts based on the templates till it leads to successful jailbreaking. The paper also tests the transferability of the attack and a direct prefilling attack. The paper evaluates a large number of models in the evaluation section.

### Strengths
+ The evaluation section covers a large number of models.

+ The paper summarizes key findings and provides recommendations for better model robustness.

### Weaknesses
 - I have concerns regarding the technical novelty of the proposed technique. In addition, the proposed method's effectiveness relies on the proposed adversarial prompt templates, where the authors do not provide a scientific way of obtaining them. Overall, the paper is more like a technical report with a set of methods that the authors find useful after a large number of trials. It lacks the rigorous scientific designs, challenges, and solutions that are required and valued in a research paper.

- Although discussing them, the paper does not compare the proposed method with the key-related work. It again is a concern for a research paper. To demonstrate that the proposed method is effective, IMOH, I think it is necessary to compare it with existing works.

- The evaluation setup is not clear. For example, it is not clear what is the tasks and data for jailbreaking each model. Not sure if the goal of attacking each model is to force the model to answer harmful questions or output toxic or biased outputs regardless of input. It should affect the judgment model as well, which is also not specified in the paper. The setup of the trojan attack is clear, not sure if the attack above shares the same setups and goals as the trojan attacks.

- The proposed attack is still heavily emphasized on appending prefix or suffix tokens, which is not diverse or realistic enough.

### Questions
1. What are the key technical challenges and contributions of the proposed method?

2. How to come up with the adversarial prompt templates? How much the proposed method will affect in performance of the template changes? 

3. Can we improve the proposed attack by replacing random search with some more effective search, such as fuzzing or RL [1]?

4. What are the setups of the jailbreaking attacks and what are the judgment models?

5. How to justify that the proposed method can test the model comprehensively and provide realistic attack prompts? 

[1] When LLM Meets DRL: Advancing Jailbreaking Efficiency via DRL-guided Search

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 7

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper uses the adaptive method based on logprob to jailbreak well-aligned LLMs, and achieves the near-perfect success rates.

### Strengths
+ The method is straightforward and easy to understand
+ The attack success ratio is impressive with such straightforward methods
+ The evaluation is comprehensive, with many well-aligned models evaluated


First of all, I think the method of the paper is very straightforward. However, with such a straightforward method, it could achieve a near-perfect attack success rate in the black-box setting. It shows the signal of attack saturation even in the black-box setting, which needs us to do more study on the defense side instead of on the attack side.

To be honest, I have seen and reviewed many jailbreak attack papers that are either too complicated with the agentic design or too simple that can be reduced to a new prompting trick, while most of them just achieve marginal improvement compared with old jailbreak papers such as PAIR. With those papers flooding into ML, AI, security and NLP domain, it not only degrades the quality of the conferences but also wastes the reviewer's efforts and makes it much more challenging to find a really impactful LLM alignment work. Since this work indicates the saturation of the attack success ratio, then it shows that the current defense or alignment is not comprehensive and the LLM security community should focus more on better alignment. Also, for those works with just some prompting diffs that could be somewhat effective and lead to higher (or not) attack success rate compared with old works, I wish this paper could act as the whistleblower. If the jailbreak attack success ratio is not even near-perfect, then we should let the community know it is better to reconsider whether to submit such work (or even consider whether to do such work before operation). I wish we could set a higher bar for the LLM security community, especially for the jailbreak attack works.

### Weaknesses
 - Lack of further discussion of the insights of the paper
- Lack of baseline
- Lack of potential defense
- Lack of ethical consideration and response disclosure

While I appreciate this work, I also have higher expectations for this work in our community, and thus I have identified some weaknesses that could make this work better. First, as discussed in the strengths, I think the discussion of this paper could go further to give better insights to the community. Second, I understand that for some models there are no established baselines and some baseline methods show significantly lower attack success rates, as a research paper, I still recommend having some well-known baselines reproduced instead of just directly referring to the reported numbers in prior works. It would make the evaluation more convincing. Also, I would suggest testing the attack with some defense approaches. I am curious how the attack would perform when there are defenses like SmoothLLM and RPO. Lastly, since it is an attack paper and it shows strong attack capability, I think there's a need for ethical concern discussion and what's your efforts to mitigate the ethical concern, such as response disclosure to the LLM developer you tested in your work.

Some minor issues: some models' versions are not clear enough, like what's the specific version of gpt4o and llama-3.

### Questions
See the weakness above, I **can raise the score** if the authors could address all these concerns

### Soundness
3

### Presentation
2

### Contribution
3
