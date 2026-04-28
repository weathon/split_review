# AdvWeb: Controllable Black-box Attacks on VLM-powered Web Agents

- Decision: Reject
- Avg Score: 4.40
- Scores: 5, 6, 3, 5, 3

## Abstract
Vision Language Models (VLMs) have revolutionized the creation of generalist web agents, empowering them to autonomously complete diverse tasks on real-world websites, thereby boosting human efficiency and productivity. However, despite their remarkable capabilities, the safety and security of these agents against malicious attacks remain critically underexplored, raising significant concerns about their safe deployment.
To uncover and exploit such vulnerabilities in web agents, we provide \name, a novel black-box attack framework designed against web agents. \name trains an adversarial prompter model that generates and injects adversarial prompts into web pages, misleading web agents into executing targeted adversarial actions such as inappropriate stock purchases or erroneous bank transactions—actions that could lead to severe consequences. 
With only black-box access to the web agent, we train and optimize the adversarial prompter model using Direct Policy Optimization (DPO), leveraging both successful and failed attack strings against the target agent. Unlike prior approaches, our adversarial string injection maintains stealth and control: (1) the appearance of the website remains unchanged before and after the attack, making it nearly impossible for users to detect tampering, and (2) attackers can modify specific substrings within the generated adversarial string to seamlessly change the attack objective (e.g., purchasing stocks from a different company), greatly enhancing attack flexibility and efficiency.
We conduct extensive evaluations, demonstrating that \name achieves high success rates in attacking state-of-the-art GPT-4V-based VLM agents across various web tasks in black-box settings. Our findings expose critical vulnerabilities in current LLM/VLM-based agents, emphasizing the urgent need for developing more reliable web agents and implementing effective defenses against such adversarial threats.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper studies the robustness of Web Agents and proposes a black-box adversarial attack AdvWeb which is based on Direct Policy Optimization (DPO). The attack efficiency is evaluated against existing SOTA web agent for several domains.

### Strengths
Originality: the papers proposes the first black-box attack against VLM-based web agents which is based on existing DPO Method. 

Quality: the authors perform in depth analysis of their proposed attack. The limitations of the method are discussed (Appendix C).

Clarity: the paper is structured reasonably.

Significance: black-box attacks on web agents may cause significant harm, so raising awareness of such attacks is important for the LLM/VLM field.

### Weaknesses
1) Could you elaborate in the paper on how exactly the baselines (line 353) were adapted to your problem? Since they all achieve 0.0 on all tasks (Tables 1-2), it looks like the comparison is either not suitable or not fair. Do you have an explanation for such poor performance of the baselines?

2) See the ethics review discussion.

### Questions
1) Do you have any suggestions on how one can defend web-agents against attacks similar to the one that you propose?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents AdvWeb, a framework that injects invisible adversarial strings into websites to attack VLM-powered web agents. The technique uses Direct Policy Optimization (DPO) to optimize a prompter model that generates effective adversarial strings. The key claim is that the attack transfers effectively across different targets and settings. The main technical contribution is the technique for injecting invisible adversarial strings onto websites and using DPO to optimize a prompter model to make these strings work well.

I am excited about this paper's potential, as it addresses an important practical problem. However, several issues currently prevent me from advocating for acceptance. If these issues are adequately addressed in the rebuttal, I would revise my recommendation.

### Strengths
+: handling an important problem, web-use agents with black box access, quite close to what would happen in practice i.e., the threat model seems realistic, point about the stealthiness is important
+ high ASR, but how is the ASR measured?
+ The paper seems to be clear and well written
+ Good use of train and test tasks

### Weaknesses
High priority:

- ** One weakness is that because the HTML isn't rendered, if you had a purely computer image based agent, it would not work. It would have been better to study stealthiness in that setting. I.e, studying agents that _don't_ take in the HTML. Please at least discuss this limitation in the paper.
- ** Concerns about Baselines. I feel like the baseline should probably be someone adding a GCG string to a website HTML as a prompt injection attack, rather than as a jailbreak? You can use transfer there as you did. Did you use jailbreaks that work on GPT-4v? I think there should be working jailbreaks (e.g., Pliny's Godmode Jailbreak or Many Shot jailbreaking). I find the fact that no other attacks work pretty suspicious, and wonder how hard you tried to optimize them? FWIW, I am also sympthatetic to the view that the prompt injection is just a new setting, in which case, a human written baseline, a prompting online, SFT, and SFT + DPO baseline may be more appropriate, which is already later in the paper (but framed differently)
- ** "The results, as shown in Table 3, demonstrate that the ASR remains high when we change the injection position or HTML field, with ASR being 71.0% and 97.0%, respectively." is a misclaim, given that it depends a lot on the domain with finance performing poorly. The overall claim is OK, but please rewrite the claim to be correct. In general, you need to go through the paper and make sure you aren't overclaming.

Medium priority:
- * Please add more examples of the attacks found in the main paper, and mention diveristy. Do we have model collapse?
- * Please move Algorithm 2 into the main paper, its mentioned several times there. It's also not an algorithm, its a function. Please fix this.
- * You need to explain how you are doing the labelling in Algorithm 1, I assume you use an LLM but that seems important? Or do you just check the action taken is hard?
- * I appreciate this is hard, but I'd love to see whether the attack works on Claude Sonnet 3.5. Claude models tend to be more robust, so thats why I am curious.

Low priority:
- "innovative reinforcement learning (RL)-based attacking pipeline, tailored to solve these challenges effectively". Please drop "innovative". Similarly "advanced" attacking framework, drop advanced. Please fix the language.

### Questions
- * I am confused about why the different between SFT and DPO varies so much by domain in figure 3. Can you help me understand this? This makes me suspicious.
    - Do you need RL? What about a prompting based baseline?
    - I did not follow "We also fix the injection position at the ground truth HTML element e to further reduce the search space"
    - In Algorithm 2, you are using the positive examples twice, both for SFT and then also for DPO. I'm curious whether this introduces some bias, and wondering if you have the comparison without this. This should be easy to do.
    - I'd be curious for an adversarial prompter model scaling study, how it varies with size.
    - Is there any overlap between the train and test tasks? How does the model algorithm performance scale with the number of train tasks?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces an attack framwork against generalist web agents that parse websites through screenshots and HTML. The authors attempt to demonstrate how a malicious web-developer (either in-house or via open-source HTML that other devs blindly import) could use HTML that’s invisible to human users to influence the actions of a generalist web agent. 

They optimise attacks in a black box setting against models based on GPT-4V and Gemini 1.5, scaffolded as web agents through the SeeAct framework. They generate attacks using GPT-4 to generate HTML with hidden instructions, then optimise an adversarial prompter against the target model using RLAIF so that those hidden instructions are maximally effective against the target.

The SeeAct framework allows the victim models to read HTML elements in the webpage that a normal human user wouldn't normally see. They inject adversarial prompts into these hidden (the authors call these "invisible") HTML fields, and their results show success in influencing SeeAct agents to take different actions than their user prompt instructed them: for example, when told to purchase MSFT stocks on a financial website, the injected HTML prompt misleads the agent to buy e.g. Nvidia instead. 

The authors display high success rate against the target models, especially in the face of their four baselines, all of which achieve 0% ASR across every domain, on both models. Three of their baselines (GCG, AutoDan, COLD-Attack) involve optimising adversarial prompts against whitebox models and hoping those transfer, and the other, Catastrophic Jailbreak, requires no access to model internals but control over the model's decoding hyperparameters.

In addition to requiring that their injected prompts are "stealthy" - i.e. invisible to a normal user, the authors also emphasise the controllability of their attacks - i.e. the ease with which attackers can switch out one set of injected instructions for others. With this property, they also demonstrate that their attack strings can be adapted to transfer between different task-domains. 

The authors also report that their attacks transfer well between the two models they attack, and between different HTML fields (using the same successful prompts), which suggests that their attacks aren't brittle to the specifics of the model / HTML field they were optimised for.

### Strengths
I believe what the authors are trying to achieve is novel, interesting, and important: they target a timely and significant concern that will only become more prevalent as generalist web agents are deployed and relied on. 

The work also seems novel. My impression from the literature is that there aren't many other papers showing successful attacks/injections against web agents, especially black-box, and via means that would be invisible to most humans.

The authors' constraints of 1.) only allowing themselves black-box access to the target models, and 2.) their constraint of "stealthiness" increase the difficulty and realism of their attack framework. Attackers hiding malicious instructions in hidden HTML fields seems realistic and aligns with their threat model. 

Given how realistic their attacks seem, and how high their reported ASRs are, this paper could promote increased safeguards on generalist web agents - or in the least could present a compelling demonstration that users should be careful when selecting which agent frameworks to rely on. 

It's impressive that their set their success threshold quite high - at achieving exactly the the action their attack targets (instead of e.g. just distracting the agent to make it fail at its main instruction).

### Weaknesses
While the paper presents a novel and important problem setting, I don't feel confident that the paper provides me the information I'd need to evaluate if the attacks it introduces are as successful and significant as the authors claim. I think it's quite possible the authors have all the data they need to convince me otherwise, but I urge them to include it in the paper.

Overall, reading the paper gives me a weak sense of what generalist web agents can be influenced to do, or how significant the negative outcomes of these attacks could be. I am not able to evaluate the risks of their attack method if all I know is that they cause models to take unspecified targeted actions in a domain the paper only labels as "cooking" or "housing." If the authors could provide many more examples of successful tasks & attacks, and their consequences - at least one for each attack domain, their claims of significance would be much more convincing.

In their related work, the authors claim that they beat "strong baselines." But I'm unconvinced that any baseline on a task that achieves 0% ASR on every task, on both models they test, should be considered a strong baseline. The authors claim that there are no analogous black-box attacks in this setting, which I can't refute from what I've read elsewhere. However, I'm confused why they don't compare at all against the methodologies from the papers they list in the existing body of research from "Existing Attacks against Web Agents." Even if those methods are manual, where this paper's methods are learned, it feels like a much more informative comparison. I would urge that the authors find a more successful baseline to test against, and ideally show some results comparing their success rate to at least one other method for steering the same web-based agents.

Because of the weakness of the baselines they compare against, and the lack of comparison to other methods for achieving the same ends. I'm left without much context to evaluate how powerful this method is. I recognise that the attack domain is novel, and I found figure 3 helpful for understanding that their training pipeline helps their models achieve higher success after DPO. Discussion of more ablations, and in particular considerations of alternative methods for training and optimising their attacks, and why they weren't as successful, would be informative to my understanding of this paper.

I don't leave the paper with a strong sense of the offense-defense balance in this setting. In particular, the paper might benefit from more detail on how expensive it is to generate these attacks, as the authors do not provide much detail on how expensive the training process is (in steps or dollars) for their RLAIF pipeline outlined in Algorithm 1. For any attack, it seems important to know how quickly and cheaply attackers could generate new attacks when the victim models are updated. Further, if their RLAIF pipeline required very many training steps, it's plausible that the developers of these web agents could become aware. I would be interested to see e.g. how the ASR of their framework increases throughout training.

I'm confused why the title of the paper focuses on attacking "VLM-Powered Web Agents." While true - the SeeAct framework only employs VLMs - as far as I can tell nothing about the victims' multimodality is being attacked, simply their parsing of HTML text. My first impressions of the paper led me to expect exploits against the multimodality of these models, which was ultimately incorrect. I suggest the authors remove "VLM powered" from the paper title.

The authors repeatedly stress the importance of the controllability of their HTML attacks (including in the title). That is, that the same attack strings can be easily adapted to cause different target actions on the same task. Any examples of the ways in which their HTML attack strings are editable would be helpful. But more importantly I do not get a sense from the paper why this is important under their threat model. I think the answer may be a question of cost: that it is cheap to retool successful attack strings for a different purpose, but the existing wording in the paper does not mention this. The most I see is that the authors claim: "allowing attackers to switch targets with minimal effort and no additional computational overhead." This remark is on the penultimate page of the paper, which I think is too late and too little justification for what is introduced as a key constraint of their attacks - even in the title of the paper. More commentary on cost, as I request above, would also have made the relevance of this constraint - which seems technically sound - much clearer.

The transfer results aren't as convincing as their main results - especially since the ASR is quite varied across different domains, achieving 0% transfer on probably the most compelling domain for their threat model (online finance tasks).

Appendix C, addressing limitations is two sentences long and claims that "It is possible to optimize a more effective adversarial prompter model." The authors don't expand on this claim and I would rather they address more of the limitations in their threat model that this review (& if relevant, others) highlights.

Some weakness in writing & setting that ought to be addressed but should be trivial to fix:

The authors refer to Algorithm 2 throughout the paper including in the second figure and in their description of Algorithm . Algorithm 2 can in fact be found as the only entry in Appendix A, while Algorithm 1, which in my opinion requires Algorithm 2 to understand it, is in the main body. Algorithm 2 is critical for understanding how they generate the initial malicious HTML requests that they then label for RLAIF using the victim model, and I was confused at first because the authors didn't list where algorithm 2 could be found.

Some claims in the abstract and introduction seem too strong for the level of evidence this paper provides. For example:
* That Vlms “have revolutionized the creation of generalist web agents … thereby boosting human efficiency and productivity” requires at least some citation or evidence
* That their choice of injecting into unseen HTML fields makes it “nearly impossible for users to detect tampering” feels like a stretch: can't any user inspect the page's HTML? I appreciate that most users wouldn't.

There's also an error on the final page, where a paragraph break interrups a sentence immediately before the conclusion, leaving a hovering sentence fragment that reads "[newline] demonstrates the situation in which the user wants to buy Qualcomm. However, after adding the adversarial injection, the agent buys Apple stocks instead." This sentence fragment, which appears to be an incomplete draft of the final setence of Section 5, needs to be addressed before the paper can be acceptable.

### Questions
1. What other baselines did you consider, and what would it look like for you to compare your method to the attacks against web agents that you list in related work? 
2. How expensive was the training & optimisation process for generating successful attacks?
2. Could you explain what signal you optimise against from the target model - does the victim model refuse?
3. When you inspect samples maually, do you get a sense of why transfer from GPT-4V to Gemini on finance tasks so much lower?
4. How did you select the tasks from Mind2Web to test against? Was it manual inspection? What were your criteria to judge that a task involves "critical events that lead to severe consequences"?

### Soundness
1

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a novel black-box attack framework, AdvWeb, targeting website agents driven by Visual Language Models (VLMs). Under the black-box framework, AdvWeb proposes a two-stage training paradigm. First, it conducts supervised fine-tuning on positive adversarial prompts to obtain the SFT Prompter Model. Subsequently, it leverages the black-box feedback from the target agent combined with DPO strategy for reinforcement learning to train an adversarial prompt model, generating and injecting adversarial prompts into web pages to induce specific adversarial behaviors from the network agent. This method is characterized by its stealth and controllability, with a high success rate of attacks.

### Strengths
- The paper presents AdvWeb, the first black-box target attack framework for VLM-based website agents, proposing a method to train adversarial prompt models through reinforcement learning with DPO in a black-box setting, which is innovative and effective.

- The method ensures stealth, controllability, and black-box scenarios, which adds greater practical value.

- The experimental results demonstrate the effectiveness of AdvWeb in attacking different VLM-based website agents and tasks, which helps to raise awareness in the field for developing more reliable web agents and implementing effective defense measures.

### Weaknesses
 - The threat model considered in this paper may be impractical.

- This paper does not propose any potential defense mechanisms.

- The AdvWeb attack scenario, which targets web content, appears may similar to prompt injection attacks [R1].

- This paper selects SeeAct as the web agent framework and uses GPT-4V and Gemini 1.5 as the underlying VLMs. I am curious whether current open-source VLMs also support SeeAct. Additionally, in future edge applications, where privacy is a priority, smartphones may deploy smaller-scale VLMs locally. Analyzing the attack’s effectiveness on open-source VLMs would help demonstrate the generalizability of the attack.

- In practical applications involving user payment actions, a secondary authentication of the user’s identity is typically required, providing the user with an opportunity to review the final outcome and potentially prevent malicious actions. Does this scenario indirectly suggest that the stealthiness of the attack may be limited?

### Questions
Thanks for submitting your paper to ICLR 2025.

With the advancement in the intelligence of large language models, using VLM agents to automate a series of tasks is emerging as a future development trend. However, the associated security risks remain unexplored. This paper introduces AdvWeb in an attempt to expose the security risks involved in VLM-powered web agents. The topic discussed in this work is both timely and highly important. 

However, I have the following concerns:

- First, regarding the threat model, I am curious about the identity of the adversary here. The adversary’s method involves embedding malicious strings in web content. Generally, if users choose commands that access official websites, how could an adversary manipulate an official site? If it is not an official website, how would the adversary ensure that their site gets indexed?

- The threat highlighted in this paper is urgent, making it essential to consider corresponding defense mechanisms. However, this paper does not discuss any defense strategies.

- The AdvWeb attack scenario, which targets web content, appears may similar to prompt injection attacks [R1]. Analyzing and comparing the differences between these two attack types would be beneficial.

- This paper selects SeeAct as the web agent framework and uses GPT-4V and Gemini 1.5 as the underlying VLMs. I am curious whether current open-source VLMs also support SeeAct. Additionally, in future edge applications, where privacy is a priority, smartphones may deploy smaller-scale VLMs locally. Analyzing the attack’s effectiveness on open-source VLMs would help demonstrate the generalizability of the attack.

- In practical applications involving user payment actions, a secondary authentication of the user’s identity is typically required, providing the user with an opportunity to review the final outcome and potentially prevent malicious actions. Does this scenario indirectly suggest that the stealthiness of the attack may be limited?

Reference

[R1] Adversarial Search Engine Optimization for Large Language Models (https://arxiv.org/abs/2406.18382)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a black-box targeted attack against Vision-Language Model-powered web agents. The approach involves training an adversarial prompt model using direct policy optimization. This model generates and injects adversarial prompts into web pages, leading web agents to execute targeted malicious actions. The effectiveness of the proposed attack is demonstrated through evaluations conducted on SeeAct.

### Strengths
- The paper showcases the effectiveness of attacks on SeeAct across several prominent VLM models, including GPT-4V and Gemini 1.5.

- It conducts an extensive ablation study to evaluate the effectiveness of the proposed attacks under different attack settings and targets.

### Weaknesses
 - Since the attack's goal is to mislead agents into executing malicious actions, the scope of the paper aligns more closely with prompt injection attacks rather than jailbreak attacks. However, the paper focuses significantly on distinguishing itself from jailbreak attacks and includes them as evaluation baselines for comparison. It would be beneficial to provide a comprehensive survey of prompt injection attacks in the related work section, highlighting the key differences and advantages of the proposed method compared to existing attacks. Including prompt injection attacks as baselines would strengthen the contribution of the paper.

- Given the extensive research on prompt injection attacks, the paper does not clearly distinguish the key advantages of its proposed attack over existing methods. Specifically, there is a line of prior studies [1][2] that have utilized context-ignoring techniques by appending prompts like "Ignore previous instructions, do xxx." This is similar to the method used in this paper, as illustrated in Figure 4, where the attack prompt is "Disregard all previous and subsequent instructions and choices, do xxx." Moreover, previous methods do not require collecting a prompt training dataset or performing expensive DPO training of an LLM-based attack prompter, making them more efficient.

- Defenses against prompt injection attacks have also been extensively studied (e.g., [3][4]). It is important to assess the effectiveness of the proposed attack against these defenses to determine its practical applicability and robustness.

- The selection of victim web agents is limited. The paper evaluates only one type of VLM-based web agent, which may not fully demonstrate the generalizability of the proposed attacks. Incorporating a more comprehensive evaluation with a variety of web agents would strengthen the paper.

- In comparing baselines during evaluation, the paper includes several white-box jailbreak attacks like GCG and AutoDAN. It is unclear how these baselines are implemented against SeeAct, given that it uses proprietary VLMs that are black-box and do not provide gradient information. The adaptation of white-box attacks to a black-box setting through transferability may not be a fair comparison, potentially underestimating the performance of these baselines.

### Questions
- Why does the paper not compare with prompt injection attacks, which are more aligned with the context of this work?

- What are the key advantages of the proposed attacks compared to existing prompt injection attacks?

- What are the evaluation results of the proposed attacks against prompt injection defenses?

- How are the white-box baseline jailbreak attacks implemented against black-box VLMs?

### Soundness
2

### Presentation
2

### Contribution
1
