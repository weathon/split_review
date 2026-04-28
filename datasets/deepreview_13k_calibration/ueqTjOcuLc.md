# Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View

- Decision: Reject
- Avg Score: 5.00
- Scores: 1, 8, 8, 3

## Abstract
As Natural Language Processing (NLP) systems are increasingly employed in intricate social environments, a pressing query emerges: \emph{Can these NLP systems mirror human-esque collaborative intelligence, in a multi-agent society consisting of multiple large language models (LLMs)?} 
This paper probes the collaboration mechanisms among contemporary NLP systems by melding practical experiments with theoretical insights. We fabricate four unique `societies' comprised of LLM agents, where each agent is characterized by a specific `trait' (easy-going or overconfident) and engages in collaboration with a distinct `thinking pattern' (debate or reflection). 
Through evaluating these multi-agent societies on three benchmark datasets, we discern that certain collaborative strategies not only outshine previous top-tier approaches but also optimize efficiency (using fewer API tokens). 
Moreover, our results further illustrate that LLM agents manifest human-like social behaviors, such as conformity and consensus reaching, mirroring foundational social psychology theories. 
In conclusion, we integrate insights from social psychology to contextualize the collaboration of LLM agents, inspiring further investigations into the collaboration mechanism for LLMs.}, hoping to catalyze further research in this promising avenue.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper is based on study of societies of agents using LLMs that highlight the potential of collaboration mechanisms. The findings from the authors show influence of collaborative capabilities of LLM agents, with different agent traits, thinking patterns and collaborative strategies. The authors draw a parallel between the emergence of human-like behaviors in these agents with social psychology theories emphasizing their potential. The authors posit that collaboration mechanisms of machine society with multiple agents warrants deeper exploration. Looking at understanding how different LLM architectures influence these behaviors is also left as future study topic noting that integrating insights from social psychology could also guide the development of more socially aware NLP systems.

The paper probes the collaboration mechanisms among contemporary NLP systems by melding practical experiments with theoretical insights. The study conducted utilizes four ‘societies’ comprised of LLM agents, where each agent is characterized by a specific ‘trait’ (easy-going or overconfident) and engages in collaboration with a distinct ‘thinking pattern’ (debate or reflection). The authors presents results and conclusions from evaluating these multi-agent societies on three benchmark datasets positing that LLM agents navigate tasks by leveraging diverse social behaviors, from active debates to introspective reflections. In addition, as per authors, certain collaborative strategies only optimize efficiency (using fewer API tokens), but also outshine previous top-tier approaches. Moreover, the authors results further illustrate that LLM agents manifest human-like social behaviors, such as conformity or majority rule, mirroring foundational Social Psychology theories. The authors also committed to sharing code and datasets to catalyze further research in this promising avenue.

There are key details missing (please see questions for specific details). In addition, the conclusion from the study lay on shaky grounds, subjective to interpretation from the figures (covered in detail in questions). I will encourage significant revision of this study.

### Strengths
The paper is based on study of societies of agents using LLMs that highlight the potential of collaboration mechanisms. The findings from the authors show influence of collaborative capabilities of LLM agents, with different agent traits, thinking patterns and collaborative strategies. The authors draw a parallel between the emergence of human-like behaviors in these agents with social psychology theories emphasizing their potential. The authors posit that collaboration mechanisms of machine society with multiple agents warrants deeper exploration. Looking at understanding how different LLM architectures influence these behaviors is also left as future study topic noting that integrating insights from social psychology could also guide the development of more socially aware NLP systems.

The paper probes the collaboration mechanisms among contemporary NLP systems by melding practical experiments with theoretical insights. The study conducted utilizes four ‘societies’ comprised of LLM agents, where each agent is characterized by a specific ‘trait’ (easy-going or overconfident) and engages in collaboration with a distinct ‘thinking pattern’ (debate or reflection). The authors presents results and conclusions from evaluating these multi-agent societies on three benchmark datasets positing that LLM agents navigate tasks by leveraging diverse social behaviors, from active debates to introspective reflections. In addition, as per authors, certain collaborative strategies only optimize efficiency (using fewer API tokens), but also outshine previous top-tier approaches. Moreover, the authors results further illustrate that LLM agents manifest human-like social behaviors, such as conformity or majority rule, mirroring foundational Social Psychology theories. The authors also committed to sharing code and datasets to catalyze further research in this promising avenue.

### Weaknesses
There are key details missing (please see questions for specific details). In addition, the conclusion from the study lay on shaky grounds, subjective to interpretation from the figures (covered in detail in questions). I will encourage significant revision of this study.

1. If the agent composition of society doesn’t have a marked difference then what is the utility of having such composition?

2. on mmlu S1 is doing better on min for e.g. but not on the avg. how can we be confident that the differences are attribute to not by chance and are truly significant

3. starting with P0 helps but for best perf. you need to add at least 1 P1 at end. Even with same two P0 and one P1. Why might that be the case

4. How are the agents initialized and conditioned? is the prompt indicating how agents should behave enough? what specific LLM settings were used and how does it personifies how agents are implemented for this study (are overconfident agents default to 0 shot prompting and easy going multi shot?)

5. what were the tasks details for subject of this study? if we just have one agent (either of two types) how many prompts (in case of reflection) it takes for it to get to the answer? are the tasks based on knowledge (like valid chess move pieces) that may be available to the agents as part of their training data? if yes, why will it change on reflection? and what is source of this change (is there a query in background that fill in the context)?

6. It seems there are differences between all three tasks and not just Math vs MMLU and Chess move validity

7. behavior in section 3.2 is contradictory. It will be good to have comprehensive analysis, how many times collaboration helped arrive at correct answer across all tasks? the qualitative explanation can go only so far. Also, a key point needing details is around the factual information (where the information may be a fact that can be recalled/learn from training data) vs the problem where answer may not be factual but available as a set of rules with multiple possibilities. 

8. section 4.1 "we utilize the majority vote (Li et al., 2022; Cobbe et al., 2021) method to determine the answer for each round.”: how much of this is if you do multishot prompting on an LLM and use ensemble of LLMs? Is there a society aspect to this? or is it just that the ensemble of LLMs gives better answer

9. section 4.1 "Wavering Answers resemble model hallucination due to the occurrence of self-contradictory answers.": how can we be sure this is from hallucination? And not model changing it’s output to what user prefers from set of possibilities

10. "We group samples from different societies under the same strategy because the effect of society is minimal": what is the scientific evidence to prove that this is indeed the case? 

11. collaborative strategies play a significant role in performance: I dont see a significance test to lay this claim

12 4.1 conclusion 2 For continuous reflection strate- gies, the proportion of “Wavering Answers” occurrences is the highest among all strategies as seen: Doesnt seem to be the case from figure 4 d-f

13. 4.1 conclusion 2 the strategy of “Pure Debate” (i.e., p0 p0 p0 ) can effectively re- duce this fluctuation (hallucination): Doesnt seem to be exclusive to pure debate the case from figure4 d-f

14. 4.1 conclusion 2: if that is true why is hallucination lower for P0P1P1 or P0P1P0

15. section 4.2 number of agents: doesnt seem to be always case on both accounts

16. section 4.2 more rounds: Doesn’t seem to be always the case. The pattern seems inconsistent as is defintion of good or bad. Also, the improvement needs statisitcal significance.

17. Section 4.2 Other Collaborative Strategies: Doesn’t seem to be always the case. All except for 1 case the performance consistently drops. Also, what is significant drop needs defintion (at least for one case where they are pretty close). And same with what is good or bad performance to begin with.

### Questions
1. If the agent composition of society doesn’t have a marked difference then what is the utility of having such composition?

2. on mmlu S1 is doing better on min for e.g. but not on the avg. how can we be confident that the differences are attribute to not by chance and are truly significant

3. starting with P0 helps but for best perf. you need to add at least 1 P1 at end. Even with same two P0 and one P1. Why might that be the case

4. How are the agents initialized and conditioned? is the prompt indicating how agents should behave enough? what specific LLM settings were used and how does it personifies how agents are implemented for this study (are overconfident agents default to 0 shot prompting and easy going multi shot?)

5. what were the tasks details for subject of this study? if we just have one agent (either of two types) how many prompts (in case of reflection) it takes for it to get to the answer? are the tasks based on knowledge (like valid chess move pieces) that may be available to the agents as part of their training data? if yes, why will it change on reflection? and what is source of this change (is there a query in background that fill in the context)?

6. It seems there are differences between all three tasks and not just Math vs MMLU and Chess move validity

7. behavior in section 3.2 is contradictory. It will be good to have comprehensive analysis, how many times collaboration helped arrive at correct answer across all tasks? the qualitative explanation can go only so far. Also, a key point needing details is around the factual information (where the information may be a fact that can be recalled/learn from training data) vs the problem where answer may not be factual but available as a set of rules with multiple possibilities. 

8. section 4.1 "we utilize the majority vote (Li et al., 2022; Cobbe et al., 2021) method to determine the answer for each round.”: how much of this is if you do multishot prompting on an LLM and use ensemble of LLMs? Is there a society aspect to this? or is it just that the ensemble of LLMs gives better answer

9. section 4.1 "Wavering Answers resemble model hallucination due to the occurrence of self-contradictory answers.": how can we be sure this is from hallucination? And not model changing it’s output to what user prefers from set of possibilities

10. "We group samples from different societies under the same strategy because the effect of society is minimal": what is the scientific evidence to prove that this is indeed the case? 

11. collaborative strategies play a significant role in performance: I dont see a significance test to lay this claim

12 4.1 conclusion 2 For continuous reflection strate- gies, the proportion of “Wavering Answers” occurrences is the highest among all strategies as seen: Doesnt seem to be the case from figure 4 d-f

13. 4.1 conclusion 2 the strategy of “Pure Debate” (i.e., p0 p0 p0 ) can effectively re- duce this fluctuation (hallucination): Doesnt seem to be exclusive to pure debate the case from figure4 d-f

14. 4.1 conclusion 2: if that is true why is hallucination lower for P0P1P1 or P0P1P0

15. section 4.2 number of agents: doesnt seem to be always case on both accounts

16. section 4.2 more rounds: Doesn’t seem to be always the case. The pattern seems inconsistent as is defintion of good or bad. Also, the improvement needs statisitcal significance.

17. Section 4.2 Other Collaborative Strategies: Doesn’t seem to be always the case. All except for 1 case the performance consistently drops. Also, what is significant drop needs defintion (at least for one case where they are pretty close). And same with what is good or bad performance to begin with.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper looks into collaboration between language models in a societal setup, containing n agents with 2 traits (easy-going, overconfident) and 2 thinking patterns (debate, reflection). They compare collaborations between LLMs with human collaboration behavior backed by theories from Social Psychology. The collaboration behaviour is studied for three different tasks and they demonstrate interesting parallels with dynamics of human society. They also argue that scaling up is not always the key, specifically in the context of collaboration.

### Strengths
- The paper explores a less explored area of collaboration between language models, giving a glimpse into how machines can potentially work in a collaborative set up and to what extend this parallels human society. 
- The description of the experimental setup and execution is clearly articulated. The methods are intuitive and supported by clear depictions and problem formalization making it easy to follow. 
- The experiments explore the desired research questions in a systematic manner and they observations are explained by drawing from theories in Social Psychology

### Weaknesses
 - The societal setup is oversimplified in terms of the number of traits and the size of the society. As a preliminary study, it is a good start. However, this is not clearly acknowledged in the paper. 
-  The study involves two identical language models interacting with each other, essentially sharing a common knowledge base. This setup differs from a typical human societal arrangement, and the impact of this factor  is not explicitly addressed. For instance, it is unclear what would be the impact of using different language models for the agents.
- They argue that scaling is not the key and supports their claim with intuitive explanations. However, the scaling is limited to 3-4 agents and 2-4 rounds, which makes the observations seem a bit far fetched,

### Questions
- How would a potential non-simplified collaboration setup look like and how this would influence the observations made in the paper ?
- What is your motivation to chose agents backed by same language model rather than different model? How do you think using different models would influence the current experimental setup ?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the potential for Large Language Models (LLMs) to exhibit human-like collaborative mechanisms in a multi-agent system. By creating four unique societies of LLM agents, each possessing distinct traits (being easy-going or overconfident) and thinking patterns (either debate or reflection), the study evaluates their collaborative mechanisms on three benchmark datasets. Results indicate that these LLM agents demonstrate a range of social behaviors, including active debating and introspective reflection. The paper promotes the use of social psychology insights to understand the collaboration of LLM agents better and provides a framework for evaluating multi-agent collaboration, emphasizing the potential of collaboration over mere scale in LLM performance.

### Strengths
The section provides a structured breakdown of the conceptual framework, detailing agent traits, thinking patterns, and collaborative strategies. It lays out the foundation for the study and justifies the relevance of the adopted strategies.

The inclusion of different datasets (High School Multiple-Choice, Math, and Chess Move Validity) to test the collaboration mechanisms is commendable, ensuring a broad evaluation spectrum.

The decision to frame the study using social psychological concepts is innovative. The puzzle-shaped agent representation is also a novel approach that aids in breaking down complex concepts into narrative visuals.

### Weaknesses
Assumption on Traits Influence:
The assertion that collaborative strategies overshadow the influence of agent composition may be premature. More extensive experiments or deeper analysis would strengthen this claim.

Unclear Real-world Application:
While the section details the mechanisms of collaboration and results in a simulated environment, its direct implications or applications in real-world scenarios are not clearly addressed.

### Questions
How generalizable are the findings beyond the datasets used?
Could there be other potential agent traits or thinking patterns that were not considered in this study?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study explores various configurations of multi-agent collaboration in problem-solving across MMLU high-school multiple-choice, MATH, and Big-bench chess move validity task. The authors manipulate agent traits (overconfidence vs. easygoing), thinking pattern (debate vs. reflection), and collaborative strategies (permutations of agents' thinking patterns across multiple rounds). 

The primary focus of the experiment is on a three agents, with the composition of four different types of societies based on distinct agent traits. For example, Society 1 consists of three overconfident agents, while Society 4 comprises three easygoing agents. There are three rounds and the total configuration is expanded to eight possibilities by permuting {debate and reflection}.

These experiments with diverse configurations are conducted using ChatGPT, yielding results that exhibit significant variability.

### Strengths
The exploration of collaboration dynamics involving multiple LLMs is interesting.

### Weaknesses
 - The experiment results exhibit significant variance, making it challenging to derive meaningful insights and conclusions. The W-T metric, which the authors use as a complementary measure, also fails to reveal a consistent pattern.
- The fact that all experiments were conducted on a single model, ChatGPT, further hurts the generalizability of the findings. Moreover, as ChatGPT is a closed proprietary model that silently gets frequent updates, replicating the results will be considerably challenging.
- The writing style appears to prioritize flashy rhetoric over establishing clear connections to social psychology theories or frameworks. For instance, drawing parallels between the tendency of LLMs to conform to the majority and the concept of "conformity" in social psychology can be misleading. LLMs are well-known to show sycophant behaviors [1]. Furthermore, the selection of experimental design (e.g., trait types, thinking pattern) is not very well-grounded in social psychology. I suggest the authors to lower the tone and drop the emphasis on social psychology.

### Questions
- Given the considerable variance observed in all the experiments, what do the authors consider to be the primary takeaway or key message?
- Regarding the results of the W-T metric, is there any discernible pattern or meaningful conclusion that can be drawn from them?
- Have experiments been conducted involving two agents? I'm assuming that strategies involving p0p1 or p0p0 might potentially yield the best results.
- Were any statistical tests performed on the results of the experiments?
- Is there a reason for not testing the experiments with other models?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
