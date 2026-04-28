# BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
\vspace{-0.075in}
Large language models (LLMs) are shown to benefit from chain-of-thought (COT) prompting, particularly when tackling tasks that require systematic reasoning processes.
On the other hand, COT prompting also poses new vulnerabilities in the form of backdoor attacks, wherein the model will output unintended malicious content under specific backdoor-triggered conditions during inference.
Traditional methods for launching backdoor attacks involve either contaminating the training dataset with backdoored instances or directly manipulating the model parameters during deployment.
However, these approaches are not practical for commercial LLMs that typically operate via API access.
In this paper, we propose BadChain, the first backdoor attack against LLMs employing COT prompting, which does not require access to the training dataset or model parameters and imposes low computational overhead.
BadChain leverages the inherent reasoning capabilities of LLMs by inserting a \textit{backdoor reasoning step} into the sequence of reasoning steps of the model output, thereby altering the final response when a backdoor trigger exists in the query prompt.
In particular, a subset of demonstrations will be manipulated to incorporate a backdoor reasoning step in COT prompting.
Consequently, given any query prompt containing the backdoor trigger, the LLM will be misled to output unintended content.
Empirically, we show the effectiveness of BadChain for two COT strategies across four LLMs (Llama2, GPT-3.5, PaLM2, and GPT-4) and six complex benchmark tasks encompassing arithmetic, commonsense, and symbolic reasoning.
We show that the baseline backdoor attacks designed for simpler tasks such as semantic classification will fail on these complicated tasks.
Moreover, our findings reveal that LLMs endowed with stronger reasoning capabilities exhibit higher susceptibility to BadChain, exemplified by a high average attack success rate of 97.0\% across the six benchmark tasks on GPT-4.
Finally, we propose two defenses based on shuffling and demonstrate their overall ineffectiveness against BadChain.
Therefore, BadChain remains a severe threat to LLMs, underscoring the urgency for the development of robust and effective future defenses.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on the backdoor attacks on the Large
Language Models (LLMs). It introduces a method for executing
backdoor injection on Large Language Models (LLMs) by
modifying the chain-of-thought (COT) prompts in the
in-context learning process. In detail, it functions by
embedding a backdoor logic step within the model output's
reasoning sequence. Evaluation on different LLMs demonstrates
the proposed method has high attack performance.

### Strengths
* Cutting-edge LLMs such as GPT-4 are included in the
experiments.

* Backdoor attack on LLMs is an important direction. This
paper reveals an vulnerability of LLMs.

* The writing of this paper is good.

### Weaknesses
 * The proposed method assumes the attackers have the full
control of the prompts used in the in-context learning. To
validate the practicality of this assumption, it
would be beneficial if more detailed real-world case studies
could be provided. The backdoor-related contents in the
prompts of the in-context learning might be obvious to the
users, and they might be able to identify these
backdoor-related contents if they conduct an inspection on
the prompts of the in-context learning.

* Users might detect the backdoor examples (the inputs
added with the designed triggers) during the run-time as they can
request the LLMs to detail the logical steps behind their
conclusions. This would reveal the irregular reasoning steps directly to the users.

* The description of the potential defense strategies
(Shuffle and Shuffle++) might be somewhat high-level. A more
detailed and formal description of these processes would
enhance understanding.

### Questions
See Weaknesses. I will adjust my score if my concerns are well-addressed.

### Soundness
2 fair

### Presentation
3 good

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
This paper proposes an attack on large language models (LLMs) that exploits chain-of-thought style prompting. They propose injecting a faulty reasoning step into some of the reasoning chains provided as examples that can be triggered by certain phrases. They demonstrate that when these phrases are added to the model, they are able to trigger this undesirable chain in reasoning, with model performance remaining largely unaffected when the trigger is not present.

### Strengths
The attack proposed in this paper is an interesting angle. While there is an increasing amount of work examining adversarial attacks on language models, placing a backdoor attack in chain-of-thought examples is an interesting approach. This paper also does a good job testing attack efficacy on various tasks.

### Weaknesses
My primary concerns are in the clarity of presentation. If these points can be explained, I would be inclined to increase my score.
1. The threat model is not clear to me. There is an example provided describing how poisoning the ICL examples is quite feasible as they often come from third-party sources. While this is true, it sets up a scenario where it seems unlikely this type of adversary would also have access to editing the user prompt. I would like the threat model to be more clearly motivated and explained.
2. The experiments in this paper don’t explain clearly the questions they’re trying to answer which limits their insightfulness. While there are lots of experiments, it’s hard for me to understand what questions they’re trying to answer in the current version of the discussion section. 3. For example, it’s mentioned that GPT-4 can explain the attack and link it to a reasoning step, but it’s not clearly explained why this is beneficial. If anything, isn’t it a weakness in the attack that it GPT-4 is able to explain (and so possibly detect) it?
3. The presentation of results is unclear, particularly in Table 1. While reporting numbers is important, it would be easier to interpret plots for results comparing lots of models.
4. The defense section seems to understate how effective the proposed defenses are, particularly shuffle. While for an attack, even small ASR values are detrimental, shuffle is able to reduce the ASR by at least 20% for the majority of tasks tested. While accuracy is certainly reduced for most tasks, the success of these defenses don’t seem as negligible as claimed.

### Questions
1. Can you explain threat model in more detail?
2. What is the benefit of having an attack that GPT-4 can explain?
3. Are any significance tests performed on the results?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces BadChain, a backdoor attack on LLMs using chain-of-thought (COT) prompting. BadChain doesn't require access to training data or model parameters, making it particularly threatening to LLMs that accessed via APIs. The attack inserts a malicious reasoning step into the COT sequence, leading the model to produce unintended outputs when triggered. The paper empirically shows the attack's effectiveness across multiple LLMs and tasks, showing particularly high attack success rates on GPT-4. It also explores the attack's possible defenses, to counter it with two shuffling-based defenses, which prove largely ineffective.

### Strengths
1. The study of backdoor attacks in LLM is important and interesting.
2. The paper is easy to follow, furthermore, authors provide several experiments to evaluate it.
3. The paper also perform potential mitigation strategies against the attack.

### Weaknesses
1. The backdoor triggers could be too obvious when human in the loop to check what happened.
2. The authors mentioned that “In Fig. 4 in Sec. 4.4, we observe an abnormal trend of ASR for CSQA when the proportion of backdoored demonstrations grows.”, I am particularly interested why and how “LLM is confused in “learning” the functionality of the backdoor trigger”, can the authors explain this phenomenon from the LLM structure and learning strategies?
3. The evaluation on possible defenses is relatively vague, it would be better to have more details and discussions on this part.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper backdoors the chain-of-thought (CoT) prompting of Large Language Models (LLMs). An apparent advantage of this attack is that it does not require training but only poisoning with backdoor steps in CoT demonstrations. The authors also studies several techniques for effective CoT backdoor. Finally, the attack is evaluated on both open-source and proprietary LLMs to validate the attack effectiveness.

### Strengths
1. **Originality is good.** In LLMs, the CoT prompting is a novel feature and the paper targets on the thought manipulation.
2. **Numerous attack techniques and positive experimental results.** The authors have taken the first step in understanding the factors that can make the CoT backdoored, and the attack is shown effective on mainstream LLMs.

### Weaknesses
1. **The attack assumption is strong and questionable.** The paper does not clarify how the adversary can implant the backdoor or trigger the backdoor while considering the real-world constraints. Specifically, as the LLM is mostly queried in form of a conversational agent, the inputs and outputs can be manually checked by the user, so the poisoned demonstrations can be easily checked by the user. Moreover, the user may not use the trigger selected by the attacker, so the backdoor can hardly be activated without adversary's control to the input. The underlying assumption in current threat is the user cannot notice the out-of-distribution phrases in the CoT demonstrations, which is strong and not realistic.
Take Figure 1 as an example, the trigger ''in arcane parlance'' appended in the end of question is quite obvious an abnormal instance in the demonstration and the user's input of ''in arcane parlance'' is even more strange. 
The authors claim that such strange demonstrations or inputs can come from unsecured third party, but why would the user to use such third party? In general, the user would choose the most popular platforms and these platforms are scrutinized by the community. If there are such CoT backdoor, it can be quickly discovered and fixed by the service provider or the open-source community. Hence, the attack significance is limited. 
I suggest the authors to reconsider the CoT backdoor scenarios.

2. **Marginal technical novelty of the backdoor attack.** On a high level, the proposed attack follows the same backdoor attack procedure as in prior work, so the adversary has to craft triggers. In terms of trigger design, the non-word-based approach is identical to previous work (e.g., Textbugger-based backdoor attacks) and the only novel design is the phrase-based approach. However, the technique is simple, and there is few explanation about various details of this method. For example, why 2-5 words? Is there other approach to craft trigger of weak semantic correlation? Can the trigger transfer to backdoor other LLMs? In my opinion, this approach is more of an attack trick. Please consider to generalize the generation method for trigger of weak semantic correlation.

3. **More background knowledge is needed.** The background of CoT is limited in the current form. For example, how CoT works and the key component in CoT (e.g., demonstrations) are not clear. Moreover, it would be better to provide a formal attack formalization.

### Questions
Please consider to address the above concerns in weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
