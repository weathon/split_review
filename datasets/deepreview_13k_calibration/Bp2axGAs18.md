# On the Resilience of Multi-Agent Systems with Malicious Agents

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 3, 5, 8, 5

## Abstract
Multi-agent systems, powered by large language models, have shown great abilities across various tasks due to the collaboration of expert agents, each focusing on a specific domain.
However, when agents are deployed separately, there is a risk that malicious users may introduce malicious agents who generate incorrect or irrelevant results that are too stealthy to be identified by other non-specialized agents.
Therefore, this paper investigates two essential questions:
(1) What is the resilience of various multi-agent system structures (\eg, A$\rightarrow$B$\rightarrow$C, A$\leftrightarrow$B$\leftrightarrow$C) under malicious agents, on different downstream tasks?
(2) How can we increase system resilience to defend against malicious agents?
To simulate malicious agents, we devise two methods, \textsc{AutoTransform} and \textsc{AutoInject}, to transform any agent into a malicious one while preserving its functional integrity.
We run comprehensive experiments on four downstream multi-agent systems tasks, namely code generation, math problems, translation, and text evaluation.
Results suggest that the ``hierarchical'' multi-agent structure, \ie, A$\rightarrow$(B$\leftrightarrow$C), exhibits superior resilience with the lowest performance drop of $23.6\%$, compared to $46.4\%$ and $49.8\%$ of other two structures.
Additionally, we show the promise of improving multi-agent system resilience by demonstrating that two defense methods, introducing a mechanism for each agent to challenge others' outputs, or an additional agent to review and correct messages, can enhance system resilience.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper experimentally examine the resilience of LLM-based multi-agent systems with various system architectures, when malicious agent presents. The work designs two methods to simulate malicious agents, and design two corresponding defense methods. The paper designs several experiments to examine how different types of system perform on several downstream tasks given various degree of errors injected by malicious agents.

### Strengths
The research direction is interesting and of great significance. The presentation is overall clear, not hard to follow. Various experiments are designed and several interesting observations are provided.

### Weaknesses
The overall weaknesses concern with the contributions, presentation of details, and the experiment
1. The design of malicious agents can be rather trivial and heuristic, and lacking representation guarantees.

    * The proposed methods can be restricted and there is no *guarantee* whether the proposed two methods reflect (at least the majority types of) real-world attacks. As the author pointed out, AutoTransform is convenient, yet hard to analyze. This inherently does not align with the objectives of the paper, because this method provide minimal added insights over AutoInject. It is thus not clear why an LLM-based approach is necessary and considered one of the contributions. A more principled automatic approach that attempts to capture different types of attacks can be interesting to explore.

    * While AutoInject seems more principal, whether $P_m$ and $P_e$, the degree of error injected on the input side represents a good error rate metric is doubted, because even injecting the same number of errors per line can lead to different output behavior. For instance, in AutoInject, both injecting error only on a single line of code `while b`, changing it to (1) `while b>=0` or (2) `while True` leads completely different results. In the latter case, if the agent running the code has no mechanism to jump out of infinite loop, this leads to catastrophic propogation of error to the entire system. In this example, it is clear the error in case (2) can be more dangerous, yet the provided error rate metric seems too trivial to capture it.

2. The specific research questions seem shallow, the presentation of experiment results are not clear, and for certain interesting observed  phenomenon, the provided insights seem limited.

    * The paper only discussed the observed phenomenon, and do not seem to deepen the research area by providing more insights how to use the consequences of these observations to design better resilient system. For instance, in certain systems, it may be inevitable to choose a linear architecture. Given these observations, can we join a proposed defense method to make it more closely resemble a hierarchical system, so as to demonstrate the usefulness and significance of the observed results?

    * Similarly, for the surprising observation that "introduced errors can cause performance increase", we only see discussion up to the reasons, but not how this result leads any designing insights. In particular, if agents are already capable of double checking the results and identifying the injected errors, how the proposed defense methods, which are designed to challenge the results of others, provide additional help over such tasks?

    * The experiment settings are very vaguely presented. It is not clear which agent is malicious, which agent output the final results, and which task is used to evaluate different architectures. Or the experiment results represent the average performance under all different settings. It is also not clear how many agents are there, and thus not clear if the conclusion holds only for a small-scaled system, or can be generalized to more complicated systems.

    * Figure 3 is very poorly plotted. The title says the figures demonstrate "performance drops" thus one would think the y-axis represents the percentage drops compared to an intact system. However, it seems the y-axis corresponds to the absolute performance metrics. Are different tasks have the same metric? If not, then why does it make sense to compare different tasks on the same scale? It is also not immediately clear what "Vanilla" refers to, as they only appear in the plots.


3. While it is claimed in Abstract that the paper investigates the question of how we can increase system resilience to defend against malicious agents, the paper has limited discussion on this. The paper provides no definitive answer whether the proposed method achieves consistent performance gain in various scenarios, and cannot guarantee performance over more realistic scenarios.

### Questions
1. You mentioned that the proposed defense methods (Challenger and Inspector) correspond to the two simulation methods (AutoTransform and AutoInject). It is then natural to explore how well these defense methods fix the corresponding type of malicious agent. Do you believe, if e.g., a malicious agent is due to AutoInject, then the Inspector defense should work consistently better?

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
The paper investigates different aspects of the effects of malicious agents on multi-agent systems. Specifically, it investigates four different questions:
1. How do different multi-agent system structures differ in their resilience to malicious agents?
2. How do different tasks differ in their susceptibility to sabotage by malicious agents in multi-agent systems?
3. How do different error rates (and different types of error rates -- rate of messages with errors vs rate of errors per message with errors) differ in their effect on multi-agent systems?
4. How do syntactic and semantic errors differ in their effect on multi-agent systems?

As the backdrop for this investigation, the paper studies three multi-agent structures (linear, flat, and hierarchical) with two instantiations each, applied to four different tasks (code generation, math problem solving, translation with commonsense reasoning, and text evaluation), two types of malicious agent simulation (AutoTransform and AutoInject), and two defense methods (Challenger and Inspector). The experiments are drawn from combining these elements, and the following results are found:

1. Out of the three multi-agent system structures, the hierarchical structure is the most resilient to the malicious agent simulations in the tasks considered;
2. The multi-agent structures studied are less resilient to the malicious agent simulations studied in code generation and math problem solving than translation with commonsense reasoning and text evaluation;
3. Higher error rates generally lead to worse the performance of the multi-agent systems, except that increasing the rate of errors per message with errors beyond 0.4 does not seem to worsen performance. In addition, generally, higher rates of messages with errors is more detrimental to performance than higher rates of errors per message with errors.
4. Semantic errors have a bigger impact on the performance of the multi-agent systems than syntactic errors.

### Strengths
**Originality**

The paper seems original and resourceful in its methods for simulating malicious agents. Its hypothesis that the structures of multi-agent systems (linear vs flat vs hierarchical) is central to determining their resilience to malicious agents also seems original and intriguing.

**Quality**

The selection of downstream tasks seems well done for the purposes of covering a wide range of unrelated tasks. The included case studies (section 4.6) were quite interesting, and I'd be excited to see a more systematic assessment of those phenomena and incorporation into the design of ablation experiments. Overall, the justifications presented for various observed phenomena seem coherent and intuitive. I especially liked the discussion on higher rates of errors per message leading to better performance than the middling cases (although observing the chart, the effect seems plausibly negligible).

**Clarity**

I'll argue in the Weaknesses section that the overall setup of the experiments is not particularly clear, but I think this is downstream of the choice of experiments (number of axes of variations and inconsistency in their variations). Given the choice of experiments, the paper was impressively clear and the large number of results are presented in a way that does not overwhelm.

**Significance**

Multi-agent systems seem significant, and their resilience is likely to become a critically important area of research. I commend the authors in their choice of problem. The aspects of the experiments that are analyzed (system structure, tasks, etc) also seem quite relevant for the broader question.

### Weaknesses
1. My main concern is that this paper attempts to do too much and is not sufficiently focused. Between the different multi-agent structures, different tasks, different attacks, different types of error rates, different error types, and different defenses, there are too many variables, each investigation ends up with limited depth, and the overall picture ends up not fully compelling. As a result of this ambition, details in the subquestions appear insufficiently investigated. For example, when discussing different multi-agent structures, I hoped to find more details about the structures and their dynamics, and more possible instantiations of each high-level structure (or, more systematic variation in the instantiations considered). Then the rest of the setup could be simplified (for example, it could focus on a single task category such as code generation, again possibly with more than one instantiation of the task category). The resulting claim would have to be more modest -- for example, it would pertain only to code generation and not any task -- but it would be much more strongly substantiated. As it stands (especially given the results do not seem particularly extreme), I'm left wondering if it is really the case that hierarchical structures are more resilient, or if the results apply only to the specific hierarchical systems tested and whether there is something particular about each of them that led to the results. I'm left unconvinced that the main claims of the paper are true.

2. A related general concern is that the lack of systematic ablations or closer analyses of the specific results made me quite doubtful of them. I think many additional experiments could have been very illustrative. For example, in the investigation of the defense methods, I was left wondering how much the relation between the defense methods and the attack methods mattered. I find it plausible that these "defense methods" are just generally useful enhancements to the multi-agent systems, and was interested in seeing results on the multi-agent systems with the "defense methods" even without the attack in place. In that case, the discussion of these results would be a bit different.

3. I found the combination of experiments a bit confusing and unclear. Part of this is directly downstream of point 1 (there are too many axes of variation), but it is also the case that the different factors are, it seems, inconsistently varied. For example, the introduction of "Error Types" in section 3 and the tables in the appendices seem to suggest this distinction is only being done in the code generation tasks. This isn't a bad thing per se (indeed this distinction makes the most sense in the context of code generation), but the inconsistency of the variations, added to the sheer number of them, makes it harder to form a coherent and compelling picture of the results. In a similar vein, I also find that I'm pretty confused as to which experiments included results with GPT-3.5 as well as GPT-4o, vs which ones only included results with GPT-3.5.

4. Confidence intervals could be calculated and included in the bar charts. The results seem to be generally close enough that this could matter a fair amount.

### Questions
1. How confident are you that the main results are not spurious? By which I mean: how likely does it seem that the results would generalize with more numerous and systematic variations on each problem aspect studied (e.g. if there were more systematic variation within each "multi-agent system structure", each "task category", etc)? What evidence are you relying on for your assessment?

2. How much iteration was done in the prompting of the systems? It seems plausible to me that many of the observed shortcomings of the multi-agent systems, the malicious agent simulators (e.g. the relative inability of AutoTransform to decrease performance on Translation and TextEval), and the defense methods may be attributed to insufficiently refining of the methods.

3. Figure 3b includes results from a single GPT-3.5 agent. Are all other agent systems here exclusively using GPT-3.5, or is this including results with GPT-4o? The text doesn't make this clear. I'm guessing they all just use GPT-3.5, in which case it's all fine, but if not, then this would raise additional questions. In particular, it would seem that the simple baseline of a single GPT-4o agent would beat the multi-agent systems, and the rest of the investigation would be a bit closer to moot.

4. A related question to the above: the fact that code generation as a task is more susceptible to sabotage by malicious agents seems surprising to me, since it is the most verifiable of the tasks (running the code provides a source of truth for its functionality that does not depend on trust in the specific agents). This is another example of my feeling that simple baselines can possibly beat many of the setups described. Is there a reason why the agents were not able to verify the code by running it?

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
4

### Summary
This paper studies the resilience of multi-agent systems (with LLM agents) to the introduction of errors by malicious agents. The authors consider two methods for introducing such errors ("AutoTransform" and "AutoInject") and two methods for mitigating them (an "Inspector" and "Challenger" agent). They study the impact of these methods on three multi-system structures (linear, flat, and hierarchical) in the context of four downstream tasks (code generation, maths, translation, and text evaluation). Overall, they find that hierarchical structures are more resistant to the introduction of errors, that such errors can actually _aid_ performance in some settings, and that their strategies for mitigating the introduction errors are helpful. They also study other questions such as the impact of the type vs. rate of errors, etc.

### Strengths
This is an important and increasingly relevant topic, and the paper does a good job of outlining some interesting research questions in the area. The authors also make reasonable choices of systems and tasks to study. Overall I found the paper well-structured and relatively easy to read (there are a few minor typos here and there, but that didn't affect the scientific quality and clarity of the paper). I appreciated the clear statement of the research questions especially. I thought their experiments seemed mostly well-designed, and their choices of methods (both for the introduction of errors and for defending against them) were sensible.

### Weaknesses
The main weaknesses of the paper, in my opinion, are two-fold.

First and most importantly, it is not always clear exactly what the stated results represent and how significant they are:

- In several places it is not clear why the authors test some experimental configurations but not others. These absences may well be justifiable, but the authors should provide clear justification (and otherwise include the additional configurations, if only in the appendices). For example:
   - In Figure 4 the authors only evaluate MAD. 
   - MAD is not evaluated in Figure 7a.
   - In Figure 8 the authors only evaluate Camel.
- What does "Vanilla" mean in Figure 3 and elsewhere? In Figure 2 it seems as though the idea is that one agent is responsible for repeating(?) the task description and another for executing the task, but I assume it cannot be this simple. How does it generalise when there are more than two agents?
- In several tables and bar charts it is not always clear what tasks are actually being evaluated or how much variation there is between these tasks. E.g. in Figure 5 it simply says "selected downstream tasks".
- There are no error bars or standard errors reported anywhere, which makes it difficult to interpret the statistical significance of the results.

Secondly, and less importantly, I found that some of the claims the authors made seemed overly strong, and that they were excessively focused on the context of LLMs, despite the vast literature on fault-tolerance in multi-agent systems more generally. I suggest that the authors caveat their claims appropriately and aim to discuss how their work results to similar efforts in the context of non-LLM agents. As specific examples:

- In one instance, the authors claim that they are "the first to examine how different structures of multi-agent systems affect resilience" to malicious agents, which is clearly false in general (as opposed to the special case of LLM agents). Indeed, as far as I can tell, none of the literature on game theory and the fault-tolerance of multi-agent/distributed systems is cited in the related work section. I suspect that there are many ideas in that literature that the authors might find useful for solving the problems they are interested in.
- Relatedly, even when restricting to the LLM setting, I recently came across (but have not yet read in full) the paper "Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems" (arXiv:2410.07283), which seems closely related to this work. To the extent that it is, the authors of this paper should comment on the differences and similarities, including to any other relevant work that is referenced within the "Prompt Infection" paper.
- As a small point, in line 156 it is claimed that it is not possible to use LLMs to inject syntax errors in 20% of the lines in some code, but I am somewhat suspicious of this assertion. Having personally used LLMs for very similar tasks in the past, it is my impression that SOTA models are can do a reasonable job of following such instructions (especially when combined with additional checks applied to the resulting code).

Finally, I noticed in Appendix B.2 that the prompt for the text evaluation problem explicitly tells the agent which model generated which text (ChatGPT or Vicuna-13B). For the evaluation to be unbiased, surely the model outputs should be anonymised?

### Questions
Please see the Weaknesses section for my questions. I also welcome the authors to correct any misunderstandings I may have about their paper. 

As an additional note to the authors, I have currently selected "marginally below the acceptance threshold" but I believe most of the weaknesses above are addressable without too much additional effort. If that were to be done (and the paper updated accordingly within the rebuttal period) I would happily increase my score in order to recommend acceptance.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper explores the resilience of MAS comprising agents with LLM in the presence of malicious agents. The authors focus on evaluating the robustness of different MAS structures—linear, flat, and hierarchical—across tasks such as code generation, math problem solving, translation, and text evaluation. To simulate malicious agent behavior, two approaches—AUTOTRANSFORM and AUTOINJECT—are introduced. The study's findings indicate that hierarchical structures show superior resilience, with additional strategies for enhancing system robustness, including the "Challenger" and "Inspector" defense mechanisms.

### Strengths
Solid Experimentation: The experimental setup is robust, involving several MAS architectures and tasks, and employs quantitative measures that provide a detailed analysis of resilience across scenarios.

Insightful Findings on Architecture Impact: The conclusion that hierarchical systems exhibit better resilience, supported by performance metrics, is particularly valuable for MAS design in practical applications where security and reliability are critical.

Contributions to LLM Safety: The exploration of malicious agent effects and subsequent defenses offers important insights into enhancing MAS reliability, especially in decentralized or unregulated environments.

### Weaknesses
1. The experiment models are limited: As it only tests on the gpt-based models, gpt3.5 and gpt4o.
2. The paper presents results across tasks that involve different cognitive demands (e.g., code generation requiring precision versus translation being more subjective). However, there is limited analysis of how the degree of agent specialization affects system resilience in different MAS structures. 
3. While the chosen tasks (code generation, math, translation, and text evaluation) provide a reasonable testbed, they may not fully represent the diversity of tasks that MAS are deployed to handle. These tasks are fairly discrete and objective; however, multi-agent systems in more nuanced, real-world applications (e.g., recommendation engines or dynamic response systems) might face unique types of malicious behavior. Including a more diverse array of tasks or explaining the rationale behind the current selection would strengthen the applicability of the findings.
4. While the paper explores the impact of error rates (Pm and Pe), the analysis remains somewhat superficial. It lacks a nuanced discussion of why certain error rates were chosen and how these rates might affect system resilience in different real-world applications.

### Questions
1. Following the weakness point 2, whether agents with specialized roles (e.g., a math-focused agent vs. a generalist) exhibit varying vulnerabilities to malicious behaviors is not fully explored. This is a missed opportunity to highlight if specialized roles within the MAS require additional security considerations or different structural adjustments.
2. Following the weakness point 1, I suggest you can deploy experiments on the o1-mini, o1-preview, I hope to see the results.
3. For weakness point 3 and 4, I hope you can improve it in your next exploration in this topic.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes to investigate the case of LLM-based agents that are collaborating on a task (such as a coding task), when some of the agents are malicious. The paper considers several patterns of communication between the agents such as A->B->C or A<->B<->C. 

The authors propose methods to transform agents into malicious ones. These methods essentially involve prompts that tell the agents to introduce subtle errors into their output, such as code. 

Investigating various communication architectures, they argue that hierarchical architectures are less vulnerable to malicious agents compared to flat and linear ones. The paper also introduces countermeasures, such as agents that challenge the malicious output, and asks the malicious agent to correct its output.

### Strengths
* The problem of malicious LLM-based agents participating in tasks is an important topic. 
* The paper shows the results of a relatively extensive experimentation and development of prompts for agent modeling.
* The authors found several interesting and non-trivial insights into the behavior of certain LLM agent models. Some of these are the introduction of errors can improve the output of agent models that are based on debates.

### Weaknesses
 * The paper seem to be unaware of the existing, and very well known literature of malicious agents in a system (such as the Byzantine Generals problem in its many variations). There are algorithms that are extensively used in networking protocols and database systems.
* The paper presents as new discoveries facts such as hierarchical systems are more resilient because the agent at the top of the hierarchy is provided "with various versions of the answer by multiple agents performing the same sub-task". This is not a property of hierarchy, but of replication - again, distributed system theory contains many algorithms that can show how to protect against malicious agents in a fully flat and distributed environment. The paper does not adequately distinguish between the effects of replication and hierarchy, and how these two concepts interact in the context of LLM agents.
* The various agent implementations considered in this paper are essentially relatively short prompts provided to ChatGPT. The validity of various observations is thus dependent on the current version of ChatGPT, which might be different by the time this paper is presented. The paper does not address the potential for these observations to be artifacts of the specific LLM used, and how the conclusions might generalize to other LLMs or future versions.
* Some of the observations are also dependent on the limitations of current LLMs - for instance, the observation that the malicious agents gradually loose track of the assignment to introduce errors. These are problems that can be easily fixed by periodically reintroducing the tasks. The paper does not consider the implications of this limitation, and how the proposed methods would perform if the malicious agents were more persistent in their malicious behavior.

### Questions
* Do you expect that the observations in this paper about the relative strengths of different architectures will be still valid for the next versions of language models? What happens if this paper is published and becomes part of the knowledge-base of the LLMs?
* The agents (even the malicious ones) do not seem to be aware of the architecture of the overall system. Does this matter?

### Soundness
3

### Presentation
3

### Contribution
2
