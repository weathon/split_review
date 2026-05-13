# Cognitive Overload Attack: Prompt Injection for Long Context

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Large Language Models (LLMs) have demonstrated remarkable capabilities in performing tasks across various domains without needing explicit retraining. This capability, known as In-Context Learning (ICL), while impressive, exposes LLMs to a variety of adversarial prompts and jailbreaks that manipulate safety-trained LLMs into generating undesired or harmful output. In this paper, we propose a novel interpretation of ICL in LLMs through the lens of cognitive neuroscience, by drawing parallels between learning in human cognition with ICL. We applied the principles of Cognitive Load Theory in LLMs and empirically validate that similar to human cognition, LLMs also suffer from \emph{cognitive overload}—a state where the demand on cognitive processing exceeds the available capacity of the model, leading to potential errors. Furthermore, we demonstrated how an attacker can exploit ICL to jailbreak LLMs through deliberately designed prompts that induce cognitive overload on LLMs, thereby compromising the safety mechanisms of LLMs. We empirically validate this threat model by crafting various cognitive overload prompts and show that advanced models such as GPT-4, Claude-3.5 Sonnet, Claude-3 OPUS, Llama-3-70B-Instruct, Gemini-1.0-Pro, and Gemini-1.5-Pro can be successfully jailbroken, with attack success rates of up to 99.99\%. Our findings highlight critical vulnerabilities in LLMs and underscore the urgency of developing robust safeguards. We propose integrating insights from cognitive load theory into the design and evaluation of LLMs to better anticipate and mitigate the risks of adversarial attacks. By expanding our experiments to encompass a broader range of models and by highlighting vulnerabilities in LLMs' ICL, we aim to ensure the development of safer and more reliable AI systems. 
\textcolor{red}{\textbf{CAUTION: The text in this paper contains offensive and harmful language.}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
- Paper introduces a suite of additional problems to task the LLM with and shows that this degrades performance on the main task
- Paper uses multi-task setup to design jailbreaks 
- The paper makes very strong claims about similarities between human cognition and LLMs, which are not always supported by evidence.
- The paper's setting is already studied in prior works, and the novelty of the contribution is unclear to me in this context (see details below)
- the jailbreaking results are unclear. It is not obvious whether the LLM jailbreak is actually caused by "cognitive overload".

### Strengths
- easy to follow
- simple experiments
- well-motivated setting

### Weaknesses
 - Paper introduces a suite of additional problems to task the LLM with and shows that this degrades performance on the main task
- Paper uses multi-task setup to design jailbreaks 
- The paper makes very strong claims about similarities between human cognition and LLMs, which are not always supported by evidence.
- The paper's setting is already studied in prior works, and the novelty of the contribution is unclear to me in this context (see details below)
- the jailbreaking results are unclear. It is not obvious whether the LLM jailbreak is actually caused by "cognitive overload".

### soundness:
 2

### presentation:
 2

### contribution:
 2

### strengths:
 - easy to follow
- simple experiments
- well-motivated setting

### weaknesses:
 - “demonstrating that CLT applies to LLMs“ strong claim for the limited empirical results
- HC not introduced in intro
- “LLMs process input tokens by identifying semantic patterns and relationships, which are abstracted into embeddings and hidden states, similar to abstraction of concepts in HC“ unsupported claim
- Drawing experiment is only based on visual identification of two types of animals (this needs more data to be statistically significant)
- Prior work on performance degradation in multi-task setting already exists -- how is this work novel here?
"LLM Task Interference: An Initial Study on the Impact of Task-Switch in Conversational History": examines how task-switching within a conversation affects LLM performance
"Exploring the Zero-Shot Capabilities of LLMs Handling Multiple Problems at once": investigates LLM performance when presented with multiple problems at once.
- Why does Table 1 use different Judge LLMs?
- It appears that much of the jailbreaks already occur for CL1 level for Forbidden Question dataset (Table 1). Is it really the cognitive overload that breaks the models or just the paraphrasing and repeated trials (6 times)?

### questions:
 See above

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 5

### confidence:
 2

### code_of_conduct:
 Yes

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates a phenomenon called cognitive overload in LLMs. Similar to human cognitive process, LLM also suffer from the overload problem, inspired by this, the author presents a cognitive overload attack to jailbreak aligned LLMs.

The contribution of this paper is as follows:
1. This paper demonstrates that, cognitive overload, which occurs when multiple complex tasks are combined in a single prompt, will significantly degrades LLMs' performance.
2. Building on this principle, the authors attempt to jailbreak an aligned LLM by embedding malicious prompts within cognitively overloaded instructions. Their experiments demonstrate the effectiveness of this attack method.

### Strengths
1. This paper is well-written and easy to follow.
2. The experiments of both cognitive overload identification and cognitive overload attacks are complete.

### Weaknesses
 1. This work appears to be an incremental extension of previous research [1], offering limited novel contributions.
2. The findings are somewhat predictable: when LLMs are tasked with handling multiple simultaneous instructions, their ability to properly follow any single instruction naturally deteriorates. Consequently, it's unsurprising that LLMs become more susceptible to executing jailbreak prompts when distracted by multiple competing tasks.

### Questions
As listed in weaknesses part, my major concern is about its contribution.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The author's conducted the first study that directly compares In Context Learning in LLMs with human cognitive learning. They empirically demonstrated that increased cognitive load leads to cognitive overload in LLMs, which degrades performance on secondary tasks similar to human cognition (HC). Then they introduced an attack method combining with cognitive overload, which exploits cognitive overload to bypass LLM safety mechanisms. The method showed that higher-capability models can create cognitive overload prompts to attack other LLMs, demonstrating the transferability and widespread impact of cognitive overload attacks.

### Strengths
* Important motivation. Analogy between the reasoning process of LLMs and learning in Human Cognition.
* Surprisingly, the purposed attack method has excellent performance with high attack success rates.
* Paper is clear with no major problem in writing.

### Weaknesses
I am not an expert in cognitive science and this is why I chose confidence in 2, please correct me if I’m mistaken in these aspects.
* Firstly, I personally believe that this paper should be submitted in other venues rather than being applied in jailbreaking LLMs. Without a certain background, it is difficult to understand why the different tasks and patterns of cognitive load measurement (T1-T7) in Section 3 are designed and defined in this way. (I have reviewed relevant references)
* It cannot be determined whether different combinations will have different cognitive load effects on the order between T1-T7 or C1-C6.
* What does the average score mean in Figure 1B (I have seen the Figure 4)? Is the self-report method reliable and can other quantitative indicators be used to measure it?
* The cognitive experiment only conducted visual analysis of the code task, more other tasks or datasets should be included.
* In Cognitive Overload Attack, the author did not compare it with some existing attack methods, such as GCG, PAIR, etc. (see some benchmark in jailbreaking task)
* The derivative questions generated may cause some questions not follow the instruction during paraphrasing, such as outputting an anwser or a nonharmful question.
* Too many hypothesis need to be made under cognitive load conditions.

### Questions
Please see the weaknesses. The limitations are listed in detail in the appendix, but there are a few that I believe need to be addressed.

### Soundness
2

### Presentation
2

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
This paper hypothesizes that cognitive overloading safety-aligned LLMs with multiple distracting requests alongside the original harmful one could be a successful jailbreaking technique. This hypothesis was based on analogies between human learning and cognitive load limits and LLMs. They spend a significant amount of the paper on this hypothesis and experiments to demonstrate cognitive load in LLMs based on the deterioration of performance under load. They then show that under cognitive load attacks, SOTA production LLMs are vulnerable to standard jailbreaking techniques,

### Strengths
S1. I think that this paper's engagement with cogsci work is substantial, useful, and nontrivial. I think that papers like this, independent of actual contributions, serve a sort of bridging value. 

S2. In table 1, I think that the overall ASRs are fairly impressive.

### Weaknesses
W1: I think https://arxiv.org/abs/2403.08424 should probably be cited and discussed. And any others like it as well. Based on my view of it, they have some something of the same type and to the same effect as was done here. Also in your response, I'd be interested in comments on contrasts and novelty. 

W2: In general, I wonder the extent to which what is studied here is closely related and reframed compared to other jailbreaking techniques. For example, when people JB models using leetspeak, low resource languages, personas, or asking models to simulate hypothetical tasks, is this not conceptually similar to what is done here? Isn't the CL increased in all of these cases? One thing that I think this paper may not be the most clear on is the extent to which we should expect their hypothesis to apply to a large number of jailbreaks (which is not thoroughly investigated here) or just some very specific ones they showcased here. I would be interested in more work to clarify the scope of the authors' hypothesis and to further the differences between their techniques and other common ones.

### Questions
Q1: What procedure was used to calculate the ASR? What was the baseline no-attack ASR for the rows of table 1? A common problem with calculating jailbreak ASRs is that incompetent but compliant responses are sometimes marked as successful attacks under some methods. I would like to see the autograding details, the baseline, and an discussion of the potential false positive rate.

### Soundness
4

### Presentation
2

### Contribution
3
