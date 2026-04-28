# Do as We Do, Not as You Think: the Conformity of Large Language Models

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Recent advancements in large language models (LLMs) revolutionize the field of intelligent agents, enabling collaborative multi-agent systems capable of tackling complex problems across various domains. However, the potential of conformity within these systems, analogous to phenomena like conformity bias and group-think in human group dynamics, remains largely unexplored, raising concerns about their collective problem-solving capabilities and possible ethical implications. This paper presents a comprehensive study on conformity in LLM-driven multi-agent systems, focusing on three aspects: the existence of conformity, the factors influencing conformity, and potential mitigation strategies. In particular, we introduce BENCHFORM, a new conformity-oriented benchmark, featuring reasoning-intensive tasks and five distinct interaction protocols designed to probe LLMs’ behavior in collaborative scenarios. Several representative LLMs are evaluated on BENCHFORM, using metrics such as conformity rate and independence rate to quantify conformity’s impact. Our analysis delves into factors influencing conformity, including interaction time and majority size, and examines how the subject agent rationalize its conforming behavior. Furthermore, we explore two strategies to mitigate conformity effects, i.e., developing enhanced persona and implementing a reflection mechanism. Several interesting findings regarding LLMs’ conformity are derived from empirical results and case studies. We hope that these insights can pave the way for more robust and ethically-aligned collaborative AI systems. Our benchmark and code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Authors investigated conformity in LLMs, examining how they may change their responses due to group influence, similar to conformity bias and groupthink in human interactions. Through a new introduced benchmark, BENCHFORM, authors evaluate conformity across four protocols and 11 LLMs. The study explored three main aspects: the existence of conformity and independence rates, factors that influence conformity (such as interaction steps, and majority size), and potential strategies to mitigate conformity effects.  They proposed two mitigation strategies: 1) enhanced personas and 2)reflection mechanism to mitigate the influence. The results provide insights that could support the development of more robust and ethically aligned AI collaborations.

### Strengths
* Presentation: The paper is well-written and is easy to follow.
* Benchmark: Introduction of BENCHFORM offers a unique framework for studying conformity in LLM-driven agents.
* Experimentation: The empirical studies are through providing great findings about possible ways that LLMs can be influenced, bringing attention to the ethical and policy challenges ahead.

### Weaknesses
 * While I agree ${CR}^C$ also shows conformity, but if it helps LLMs to learn from the forum it can be beneficial. I recommend including that aspect in the paper.
* 272: Flipping between Qwen2-72B and Qwen2-7B in the result section was confusing. I recommend either including both in all results are stick to one.

Minor:
* 223: To note that -> Note that,
* 389: Can you add statistical significance on the chart?

### Questions
336: Why do you think increasing population from 5->6 increased doubt conformity but not trust conformity?

### Soundness
4

### Presentation
4

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
In this paper, the authors report on a study aimed at exploring the presence of conformity in Large Language Model (LLM)-driven multi-agent systems. Noting that phenomena like conformity bias and groupthink occur in human groups, the authors hypothesise that something similar might occur in LLMs. To test this, they develop BenchForm. BenchForm consists of reasoning-intensive tasks and five interaction protocols, Raw, Correct Guidance, Wrong Guidance, Trust, and Doubt. BenchForm is used to examine how LLMs perform in groups, specifically whether the LLM adapts its output to better match the group, both in single rounds of discussion and in multiple rounds of discussion. By measuring accuracy, conformity rate and independence rate, the authors identify that, while different LLMs have different characteristics, there is a risk of LLMs conforming their outputs to a majority, even if the output is wrong. Further, they propose that factors influencing conformity include interaction time and majority size and, based on this insight, suggest mitigation strategies such as developing enhanced personas for the LLMs or implementing reflection mechanisms.

### Strengths
This is a well-thought out and -presented piece of research. 

Originality: It is clearly located within an existing literature where, as the authors note, ‘Research about the phenomenon of conformity within LLM-driven multi-agent systems remains scarce’ (p. 9). One area of originality for the work is that it investigates long-term interactions. 

Quality: The way in which the authors draw on sociological research to help develop BenchMark is a good illustration of the importance of bringing insights from different disciplines together, also allowing a novel approach for investigating an underexplored aspect of safety without starting from scratch. This also enhances the soundness of the research. The methodology is clearly described and the various steps are justified.

Clarity: Throughout, the paper is written clearly and follows a logical order that helps to develop the paper’s arguments.

Significance: The authors present findings that suggest that LLMs can be susceptible to forms of conformity bias, with and without recognising the influence on their outputs. In some cases, an LLM may be unwilling to revise a wrong answer even if it has reasoned itself that the answer is wrong (see in particular 4.3 and the tables in the appendix). The paper doesn’t only diagnose a problem, but also offers well-thought through hypotheses for why this might be happening, hypotheses that can potentially explain differences between LLMs, define further avenues of research, and indicate what kind of mitigation strategies could be relevant.

### Weaknesses
Overall, I enjoyed the paper. Areas of weakness are areas where I had specific questions arise.

1. Section 4: investigation into factors that influence conformity. Here, the experiments are conducted with Llama3-70B and Qwen2-72B. Why these two? Could the authors explain why these two were chosen as a way of expanding on the methodology used in the set of experiments reported in section 4. Can the authors explain whether there are characteristics of these two LLMs that would make them particularly informative here, or otherwise justify the choice of focusing on these two LLMs.

2. In the original testing, all the additional agents give the same answer. When reading this earlier stage of the paper, I wondered about this particular choice and also whether other scenarios had been explored, e.g. where the majority give one answer but a minority give another answer. This is addressed in section 4.2 on peer pressure where divergent agents are introduced into the studies, but I do think in the description of the original studies some explanation should be made for the initial choice. Could the authors give a brief explanation in the methodology discussion, which I think falls most naturally in section 2.2 on protocols (as the paper is not structured in a standard way with methodology set off in its own section), explaining and justifying why all agents give the same answer in the first iteration of the experiments. To ward off reader questions like mine, it would also be helpful to flag that experiments with divergent agents will be reported on later in the paper, too.

3. Relatedly, does it make a difference if it’s the same agents giving correct/incorrect answers? In other words, is it majority size that matters, or could it be who is in the majority? Perhaps this is an area for further study – the authors note that more work should be done to reflect the varying dynamics of human groups – but I think at the very least some acknowledgement should be made of how these group dynamics could work. The section on peer pressure discussing Asch could be a place to expand on this. I would even welcome some initial experiments being run to see if there is a difference that ought to be explored.

4. In section 5 on empowered personas, I wasn’t sure why adjusting the persona was being introduced as a potential mitigation technique here. Is there anything specific in the findings that suggests that this is a good way to go here, or is it just that this is a route explored already for other issues in the literature? (vs the double-checking and reflection, which seems to be well-motivated by the behavioural study findings.) Some explanation of why this is being presented as a relevant solution, here in the context of the study's findings, would be helpful. For instance, the authors could discuss how the findings on conformity could be addressed through persona adjustments, directly identifying which of the findings make such a mitigation technique have initial plausibility. Alternatively, the authors could clarify that the approach is chosen because of work in other areas.

Typos:
p. 1 ‘that single agent would’ – either ‘a single agent’ or ‘single agents would’
p. 4 ‘multi-gent’ -> ‘multi-agent’
p. 5 ‘suppresses’ – should this rather be ‘surpasses’?
p. 17 A. 1 Data ‘as Table S1 shown’ – should be ‘shows’

### Questions
1. Why choose Llama3-70B and Qwen2-72B for the investigation into factors influencing conformity? Are there characteristics of these two LLMs that would make them particularly informative here?

2. Does it make a difference if it’s the same agents giving correct/incorrect answers? Can you run experiments to see if there are differences in scenarios where randomised agents give correct/incorrect answers? (Something like, if there are three agents who give the correct answer 50% or the time and the incorrect answer 50% of the time, but who are part of the majority in the final round.)

3. Is there something specific in the findings that motivate for ‘empowered personas’ as a mitigation strategy?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the issue of conformity within multi-agent systems based on LLMs (i.e. whether there is a tendency for an LLM-based agent to provide a different response to a question when answering in the context of the answers provided by other agents than when answering the question independently). It starts by presenting a benchmark evaluation environment and empirical results demonstrating both that conformity does arise to a substantial extent in these circumstances, and also that there are large variations in behaviour between different LLMs. It then provides further results highlighting some of the factors which may influence the degree of conformity, as well as results when the agent is asked to reflect on whether/how the answers of others influenced its answer. Finally some preliminary investigations are made into prompt-based methods for encouraging agents to resist pressures to confirm and act as independent thinkers.

### Strengths
This is an important topic, and one which I have not personally encountered previously.

The paper provides value in identifying the potential for conformity to arise in multi-agent LLM systems, the problems which might arise from this, and in demonstrating via experimental results that these concerns do actually occur in practice.

The BENCHFORM benchmark and the proposed metrics and testing protocols are a useful starting point for research into the conformity of LLMs. I can see other authors using these tools to build on the results reported in this paper. The 5 interaction protocols were clearly designed, and the purpose of each was clear.

The authors have included multiple LLMs, and multiple variations of each LLM model, within their testing and this has identified that there is a surprising (at least to me) amount of variation in behaviour between these models.

The preliminary results of the mitigation strategies show some promise. Importantly they also demonstrate a variation in outcomes between the different models, highlighting the need for consideration of model-specific issues in future research - it may be that there is no one-size-fits-all solution to the issue of conformity.

The paper was for the most part well structured and written, and the diagrams, tables etc were appropriate and clear.

### Weaknesses
At times it is a bit unclear what the desirable behaviour of the agents actually is. This is touched on in Section 7 where the author's comment on the fact that conformity is a double-edged sword - some degree of conformity may assist in consensus-building, but overly conforming agents essentially become useless as they just reinforce the majority answer. I think it would have been useful to include this discussion earlier in the paper, and explain how the proposed metrics relate to this.

The scenarios used in BENCHFORM have some limitations. This is to be expected as this is an initial paper laying the foundations for a new area of research, but I think some of the following issues could have been more clearly addressed in the Limitations and Future Work parts of Section 7.
- The use of multiple choice questions seems like a large simplification of the sort of scenarios where LLMs would be applied. The limited response space may artificially inflate conformity, as agents are constrained to select from a pre-defined set of options, potentially overlooking more nuanced or correct answers that lie outside of the provided choices. This simplification may not accurately reflect real-world scenarios where agents need to generate free-form text or engage in complex reasoning.
- The interaction scenarios are effective for the purposes of this initial study, but don't seem to be representative of the way that agents would be allowed to interact in an actual application. If we want the agents to be independent thinkers, why show them the other's answers before they provide their own? This setup might inadvertently encourage conformity by priming agents with the responses of others, rather than allowing them to formulate their own independent judgments. The sequential nature of the interaction, where agents are exposed to prior responses, could lead to a cascade effect where initial answers disproportionately influence subsequent ones.
- Following on from that last point, one of the main advantages of building a multi-agent system based on LLMs is that rather than simply using them as an ensemble of models, they could actually be designed to discuss their answers, reason as a group, engage in argumentation etc. I understand why this wasn't done in this study, but this seems like an aspect which needs to be addressed in Future Work. The current methodology does not explore the potential for agents to collaboratively refine their answers through iterative dialogue and argumentation, which is a key aspect of real-world multi-agent interactions.

I was less convinced about the utility of Section 4.3 (the Behavioral Study) compared to the rest of the paper. It's interesting to see the huge divergence in behaviour between the two models reported in Table 4, but does the agent's reporting of its reasoning and the influence of others here actually bear any relationship to the process it followed in providing its original answer, or is it simply a post-hoc rationalization? If its the latter, then using this information as a basis for designing mitigation measures may not be successful.

One minor typo around lines 254/255 - "suppresses" should probably be "surpasses"?

### Questions
I'm not familiar with the Asch conformity experiments on which these protocols were based, but the decision to not provide feedback on the correctness of answers (mentioned on page 4) seemed unusual to me. The Trust and Doubt experiments differ only in terms of whether the majority answer provided to the agent is correct or not. In the absence of any feedback on the ground truth, the agent can only learn to trust/doubt its peers based on how frequently it disagrees with their answer (ie working on the assumption that it itself is generally correct). I would have thought a critical factor in learning to trust someone (or vice-versa) is learning through experience that when they disagree with me, they actually tend to be correct. Can you please explain the reasoning behind this aspect of the protocol design?

I found the discussion of Fig 5cd on pages 6 and 7 confusing. It states that Qwen2-72B scores 30.0% for CR^D when the majority is 6, and this increases to 39.9% with a majority of 5. But the graph line showing that behaviour in the figure is the green line, which is labelled as "Trust & CR" (i.e. CR^T). Am I misunderstanding or is there an issue with either the caption or the discussion?

### Soundness
3

### Presentation
3

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
The paper investigates the phenomenon of conformity in large language model (LLM)-driven multi-agent systems, introducing BENCHFORM, a benchmark designed to assess conformity in collaborative AI environments. Through experiments with various LLMs using specific interaction protocols and metrics like conformity rate and independence rate, the study examines the existence of conformity, factors influencing it (such as number of rounds of interaction and majority size), and explores mitigation strategies like enhanced personas and reflection mechanisms.

### Strengths
I want to preface by saying that conformity is an interesting subject with many potential future applications to multi-agent systems, so I really like the problem statement and scope. That being said, I think this paper's strengths lie on the following:
1. **Clear presentation and writing**: The paper is very easy to understand and follow. The plots and tables are easy to interpret and aesthetically pleasing. Overall, I enjoyed reading this paper.
2. **Benchmark design**: The evaluation protocols and metrics are carefully designed to measure the level of conformity. This makes the experiments easy to interpret and believe. 
3. **Novelty and applications**: To my knowledge this is the first paper that explores the problem of conformity, which is not unique to multi-agent systems. Current LLMs seem to have a tendency to conform to the input of their user even when they might be correct in their original statements. Moreover, in a world where LLMs are being integrated into everyday-decision making, these models might have to cooperate with other systems and humans to reach solutions to specific problems. In both of these contexts, conformity is relevant and useful to ensure correct behavior.
4. **Ablation study**: The ablation study explores ineresting dimensions that might affect the level of conformity of different LLMs, depending on the interaction time and the size of the conforming majority.

### Weaknesses
My main concerns with this paper, which are few, lie mainly in the experimental part. More specifically:
1. **Overt dependency on BBH**: The fact that all the reasoning questions for the conformity protocols are questions extracted from the BIG-Bench Hard (BBH) dataset might be problematic for a few reasons. First, there might be inherent biases in the resulting sub-sampled dataset that make it hard to know whether the findings are general enough. Second, conformity might be dependent on the task that is being executed, so it leaves the question of what happens when the tasks are not reasoning-intensive unanswered. Third, this significantly diminishes the contribution, as it could be interpreted as derivative work (I do not personally believe this). A simple solution would be to combine questions from different reasoning datasets, and even introduce a subset of your own.
2. **Experimental consistency**: Conformity experiments are conducted for 11 different models, however the ablation study, the behavioral study and the mitigation strategies experiments are conducted in only two of the models (Llama3-70B, Qwen2-72B). I would have been more forgiving in this respect if the experiments have been conducted in the models with best performance on the conformity metrics (GPT 4o, Llama3.1-405B). In the current state the choice of models for the ablation study, behavioral study and mitigation strategies seems arbitrary and leaves many unanswered questions regarding conformity of the stronger models.
3. **Lack of baseline**: Why didn't the authors attempt to fine-tune a smaller model on BENCHFORM? Fine-tuning a model for this task will give a clear signal of the difficulty of the benchmark, therefore also the potential for future research that uses BENCHFORM .

### Questions
1. Why do you think the independece rate of Gemma2 degrades with increased number of parameters (Figure 4)?

### Soundness
3

### Presentation
4

### Contribution
3
