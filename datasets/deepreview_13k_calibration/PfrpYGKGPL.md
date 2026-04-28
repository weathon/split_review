# The Entity-Deduction Arena: A playground for probing the conversational reasoning and planning capabilities of LLMs

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 3, 5, 6

## Abstract
Large language models (LLMs) are currently effective at answering questions that are clearly asked. However, when faced with ambiguous queries they can act unpredictably and produce incorrect outputs. This underscores the need for the development of intelligent agents capable of asking clarification questions to resolve ambiguities effectively. This capability requires complex understanding, state tracking, reasoning and planning over multiple conversational turns. However, directly measuring this can be challenging.
In this paper, we offer a surrogate problem which assesses an LLMs's capability to deduce an entity unknown to itself, but revealed to an judge, by asking the judge a series of queries. This entity-deducing game can serve as an evaluation framework to probe the conversational reasoning and planning capabilities of language models.
We systematically evaluate various LLMs and discover significant differences in their performance on this task. We find that strong LLMs like GPT-4 outperform human players by a large margin. 
We further employ Behavior Cloning (BC) to examine whether a weaker model is capable of imitating a stronger model and generalizing to data or domains, using only the demonstrations from a stronger model. 
We finally propose to use Reinforcement Learning to enhance reasoning and planning capacity of Vicuna models through episodes of game playing, which lead to significant performance improvement. 
We hope that this problem offers insights into how autonomous agents could be trained to behave more intelligently in ambiguous circumstances.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This research assesses the reasoning performance of Large Language Models (LLMs) using the Entity-Deduction Arena (EDA) task, in which LLMs ask a judge questions to infer an entity. According to the study, GPT-4 performs better than humans when it comes to strategic questioning. It emphasizes how well Reinforcement Learning (RL) and Behavior Cloning (BC) work to improve reasoning abilities, especially in larger models, and how well BC transfers skills from more complex models to simpler ones. The study enhances LLMs' capacity to handle unclear queries by indicating that LLMs have an underlying structure of knowledge that may be improved with training.

### Strengths
1. Innovative Testbed: The research presents the EDA as a novel testbed for assessing LLMs' strategic planning and deductive reasoning skills in handling unclear user intents through questioning to deduce entities.

2. Performance Analysis: Systematically assessing different LLMs, the study finds notable variations in their performance, with more powerful models such as GPT-4 surpassing human players, highlighting the sophisticated capabilities of existing LLMs.

3. Model Size Insights: Results imply that performance increase may not be primarily determined by the model's size. This disproves the notion that larger models are necessarily more effective and shows that smaller models can also gain a great deal from fine-tuning.

### Weaknesses
The paper could discuss more extensively the autonomous learning capabilities of LLMs. Prior research suggests LLMs like GPT-4 may have limited autonomous planning capacity and rely heavily on well-designed heuristics. The paper's task relies solely on textual goals, which may not fully capture the challenges LLMs face with numerical or spatial reasoning, and how they adapt to diverse prompt requirements

### Questions
The paper observes that LLMs tend to fall into repetitive patterns and accumulate errors, particularly in weaker models. Can the authors elaborate on potential approaches to mitigate these undesirable behaviors? Additionally, how might these patterns impact the long-term learning and adaptability of LLMs in more complex or dynamic environments?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper, based on the prototype of the entity deduction game, carries out a series of experimental designs. The author presents the purpose of the experiment, the process, defines the criteria for success or failure, and introduces a scoring formula for evaluation. In datasets related to entities and things, a comparison experiment of the entity deduction game was conducted on several LLMs. The results showed that GPT-4 possesses a superior ability to narrow down compared to other LLMs. Furthermore, the paper explores the possibility of enabling other weaker models to acquire this capability through reinforcement learning.

### Strengths
The perspective of the paper is quite interesting. It identifies specific characteristics of GPT-4 in the entity deduction game task, such as superior LLM knows about backtracking or employing a good strategy to divide the potential solution space instead of simply performing enumeration.

### Weaknesses
In the presentation, I believe the author should use a paragraph to summarize the unique contributions of the paper.
1. The paper lacks novelty and robustness to pass the bar of ICLR. The experiments designed don't show much improvement compared with referenced prototype. The datasets leveraged in the experiments, both in terms of range (two categories entities and things) and quantity, have certain limitations. However, the paper lacks discussion on this aspect. Moreover, given the inherent randomness in GPT's responses, it raises the question of whether multiple repeated experiments were conducted to ensure the stability of the results.
2. The formula introduced in this paper lacks a thorough explanation and rigor. Why pick linearity? Any insight to pick 0.02 as coefficient?
3. The observation and conclusion from experiments seem rather preliminary. The "entity deduction game" and the so-called "path planning" requires a more strict formulation for deeper analysis. This is especially true for the criterion of what can be a good path.
4. The ability of path planning can easily be influenced by domain knowledge. I suggest that if we want to rigorously examine planning capability, perhaps we could consider a much narrower and common sense domain, for example, having GPT guess numbers within a certain range.
PS: I  did try this number-guessing experiment on GPT-4. GPT-4 doesn't necessarily choose the binary search as the optimal path; it often opts for a narrower range enumeration.

### Questions
As stated above

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to evaluate the ability for LLMs to generate useful clarification questions in dialogue via an entity deduction game (20 Questions). The paper evaluates several popular LLMs as well as human performance, performs some analysis and experiments (e.g., on the game strategies, performance in planning and reasoning), and also experiments with distilling policies from strong LLMs to smaller open-source models.

### Strengths
The motivation is compelling and the task is clear. 20 Questions has been studied in prior work in the NLP community, but this seems to be the first large-scale study evaluating LLMs on the task. The experiments are also relatively clearly defined. I found research questions well-motivated and generally set up well, and they brought a lot of interesting experiments to mind that would be cool to explore more in more detail: e.g., could you somehow probe the top-N guesses directly from the model activations by training some additional probe on them? how are improvements on open-source models attributed to reasoning vs. planning (e.g. comparing the fine-tuned open source models to GPT-4 like the experiment in RQ2)?

### Weaknesses
 * Some of the discussion is over-anthropomorphizing models. For example, in the introduction "intelligent behavior has been achieved" through what are common components of an enterprise dialogue system... it would be more precise and accurate to say that this is just traditionally how the problem of building dialogue systems, including ones that ask clarification questions, has been broken down. Some of the conclusions on why performance is strong is unsubstantiated, e.g., that GPT-4's performance is due to its zero-shot generalization ability. Wording like "realize" (in RQ1) also is attributing cognition to these models that I personally don't think is warranted.
* There needs to be precise, quantifiable evaluation of the judge's performance. Without this evaluation it's impossible for a reader to understand how much of an influence its errors has on the game. It's not enough to say that the judge is a strong model; the error rate needs to be measured directly, especially since the judge's responses are crucial for the game's dynamics. The impact of judge errors could be particularly significant if the judge consistently misinterprets certain types of questions or entities, leading to skewed results.
* The evaluation set is really small! It's hard to conclude general performance on asking clarification questions when the set of target entities is so small. Ideally, we would be able to analyze performance across a number of entity features: how rare it is, how prototypical it is, how precise of an entity it is (e.g., specific breed of dog vs. dog in general), whether it's abstract or concrete, etc. With just 30 entities, it's hard to make any conclusions along these axes of difficulty. Figure 2 starts to get at this, and I think there are hints at interesting findings here (even just looking at human performance, to be honest) -- for example, umbrellas and cookie cutters are non-prototypical instances of their hypernyms in wordnet (respectively "canopy" and "kitchen utensil"). But with only 30 evaluation examples I don't think any strong conclusions could be made. Furthermore, the entities were generated using GPT-3.5, which introduces a potential bias where the models might perform better on these items due to their familiarity during pre-training. This could lead to an overestimation of the models' true capabilities.
* Details on recruiting and managing crowdsourcing for the human baseline needs to be included in the main paper. There are also no details I could find in the appendix, e.g., on pay or the crowdsourcing platform used. There appears to be a lot of noise in the human dialogues (e.g., questions in the bottom game of table 6 appear to be obviously non-optimal) and I am wondering how workers were incentivized to actually try at the game. I also think analysis comparing the human strategies and LLM strategies should be in the main paper.
* I would have liked to see evaluation of human players on the reasoning task given a dialogue history generated by a model (and vice versa); essentially the experiment in Table 4 but replacing Vicuna 7B with a human. Since humans appear to perform worse, is this because they are worse at planning or reasoning (as defined in this paper)?
* I think the finding that these models have consistent strategies in question asking is cool, but it's not very surprising, because these are (mostly) deterministic models after all.

### Questions
* How were the entities chosen? The paper mentions they are manually curated, but from where?
* Why are the responses different for the celebrity dataset? ("dunno" vs. "maybe")
* What does "retrospective perspective" mean in Table 3 caption?
* How do you measure uncertainty in the model's top-N predictions as mentioned in the discussion of RQ1?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the unreliability of Large Language Models (LLMs) when responding to ambiguous queries and emphasizes the need for intelligent agents that can ask clarifying questions. Using an entity-deducing game to evaluate LLMs' conversational skills, the authors find significant performance variations, with GPT-4 outperforming humans. The study also explores Behavior Cloning for model emulation and uses Reinforcement Learning to improve Vicuna models, aiming to better equip autonomous agents for ambiguous situations.

### Strengths
1. The paper underscores the need for intelligent conversational agents to proactively ask questions in uncertain situations, aiding effective problem-solving across various applications.
2. It highlights the shift from modular task management to employing Large Language Models (LLMs) for end-to-end autonomous agent development, enhancing complex task completion.
3. The paper tackles the challenge of accurately capturing nuanced user intents, suggesting the use of entity-deducing games to evaluate and improve LLMs' conversational skills.
4. A systematic evaluation of different LLMs is conducted, exploring enhancements using high-performing models and introducing methods to improve LLMs using game-based learning.

### Weaknesses
1. The major concern is that entity-deducing game is one small problem in terms of conversational reasoning and planning capabilities of language models. I am not convinced that a single game is a full reflection of the LLM reasoning ability
2. The experimental scale in the paper is limited. The conclusion in the paper should be drawn from at least thousands of samples.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
