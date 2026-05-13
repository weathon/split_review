# Efficacy of Language Model Self-Play in Non-Zero-Sum Games

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Game-playing agents like AlphaGo have achieved superhuman performance through self-play, which is theoretically guaranteed to yield optimal policies in competitive games. However, most language tasks are partially or fully cooperative, so it is an open question whether techniques like self-play can effectively be used to improve language models. We empirically investigate this question in a negotiation game setting known as Deal or No Deal (DoND). Crucially, the objective in DoND can be modified to produce a fully cooperative game, a strictly competitive one, or anything in between. We finetune language models in self-play over multiple rounds of filtered behavior cloning in DoND for each of these objectives and evaluate them in self-play and in collaboration with humans.
We find that language models improve substantially in self-play, achieving 14-17$\times$ higher scores in task reward after finetuning. 
Further, the trained models generalize to both cooperation and competition with humans, scoring 2.5-6$\times$ higher than base models.
We view these results as an early promising sign for language model self-play in cooperative settings, despite a lack of theoretical guarantees.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes to study how LLMs learn in competitive games. They choose to investigate using mostly GPT-3.5 and the game Deal or No Deal (DoND) where two players negotiate to split a set of items.

They find that GPT-3.5 is unable to play the game using just prompting but through iterations of supervised finetuning on successful self-play data, it learns to improve its play. Improvement are seen not just in self-play but also when evaluated playing with humans. Warm-starting from a GPT-3.5 model finetuned on task-specific data does even better.

Analyzing the improvements, models are largely just learning the rules and making valid proposals, not strategically negotiating. Still, iterative self-play does reduce the rate of hallucinating wrong preferences and inconsistent. As expected, cooperative play increases the length and diversity of messages (as more information can always be used) while semi-competitive play reduces both (perhaps to reduce exploitability).

### Strengths
I really enjoy the research direction and perspective of the authors. Agentic LLms are becoming more popular and their interactions in non-cooperative environments are understudied, so this work has a novel and interesting approach.

The authors do well to demonstrate where their self-play is effective, especially the result that it learns to reduce hallucinations. They also provide interesting analysis of human-AI play and different ways in which training affects results. There are a lot of interesting insights to be gained from this paper and I give the authors some slack for attempting something quite novel and difficult (LLM self-play). It is clear that there are many challenges in this direction (LLaMA-70B was not good enough at initialization!) so all reasonably positive results are encouraging.

### Weaknesses
The major weaknesses of this paper is the lack of explicit understanding of their own game dynamics, which are crucial for understanding expected behaviour, baselines on performance, and conclusions that can be drawn. This is likely because of missing insights from previous, non-LLM work. The overall story of the paper is also muddled and so it is unclear what are the main insights and whether the experiments support the conclusions. I believe this is fixable in the review period and give my recommendations for what the authors can improve.

Overall, I think the authors should formalize the competitiveness of the game, explain why they study competitiveness since their results seem negative, and give a more full, coherent story. If the authors answer one of the three major weaknesses here I will increase my score and if they answer all three I will increase my score again.

First and foremost, the authors claim to work on semi-competitive games but never actually measure the competitiveness of their game! This is crucial, as proven theoretically in the famous work by Crawford and Sobel (1982), the level of achievable communication is inversely proportional to the level of competition in the game. Communication is not useful in a fully competitive game. This was further shown to be true in neural networks learning to communicate (emergent communcation) in semi-competitive games by Noukhovitch et al (2021) which also looks at an extremely similar negotiation game (Cao et al, 2018)

The competitiveness of DoND depends on the specific items and preferences each player has over the items. A game with $\lambda=1$  can be highly competitive if both players have similar values for the same items, highly cooperative if they value different items, or a mix of the two. Without knowing this, it is impossible to say whether a score of 5 is good or not. At minimum, the authors should calculate the average competitiveness of the game and have a line in Figure 2 for the average pareto-optimal score in the semi-competitive game.

You show "Pareto-Optimality" in Table 2 but this term is never defined or the value formally stated. I believe this to be the score for each player if the items were to be divided such that players had as high and as similar possible scores (i.e. a "fair" pareto optimal). This should be formalized.

As well, the that your game is "cooperative, competitive, or anything in between" in your abstract is not necessarily true. You should show this as done in Noukhovitch et al. 

**There should be no communication in a fully competitive game**

As proven by Crawford and Sobel, and shown empirically by Noukhovitch et al, a fully competitive game should have no communication. Indeed the best action for your DoND agents with $\lambda = -1$ is to not communicate and fail to agree to any deal as that will allow them to get score 0.

Your experiments trying to achieve valid agreements makes no sense as it is explicitly advantageous to *not* reach agreements. As argued by Noukhovitch et al, when there is no incentive to communicate, agents will not communicate.

**What is optimal play?**

To figure out if your models are actually learning the rules of the semi-competitive game you should outline what optimal play really is. Noukhovitch et al (2021) argues that the negotiation game is an ultimatum game which would give first-mover advantage and mean the first player should win most of the points. The rounds of dialogue in-between are cheap talk that shouldn't affect this game-theoretic optimal play, but I am open to other interpretations.

If the actual gains in your setting come about from learning to play the game and follow the rules (Section 6.1, 6.2) then what is the point of competition in your setting? Why does it matter if the game is competitive if all you're doing is learning to play?

Further, Ross et al (2024) show that LLMs are generally altruistic. Based on this analysis, they should not be playing the competitive game effectively (at least at initialization) as they would seek to maximize fairness for their opponent. This suggests to me that your competitive scenario is not even maximizing the competitive objective and your results seems to suggest this too.

You should make a strong argument for whether self play and competitive games are a negative result and why it matters. This is especially important since GPT-4 seems to play the game reasonably well at initialization so it is unclear why you're training and not creating a better prompt.

The paper feels a lot like a splattering of results without a very coherent backbone. This is fixable and I am also willing to change my view.

Currently the story reads as 
- Here's a challenge for LLMs: DoND and a solution: iterative finetuning with LLM self-play data
- Here's how it improves over a very basic prompt baseline
- Here's an analysis that shows that it's really just learning the basic rules of the game
- Here's a slight difference between cooperative and competitive play

This is a bit underwhelming and entirely hinges on the fact that your deal or no deal game is difficult to play using prompts alone. I am not convinced of this. I am especially not convinced that a better prompt could solve the cooperative game with GPT-3.5. 

I think you need to reformat this to make it clear how difficult DoND is or, more likely, to argue that perfect prompting of LLMs is difficult and your self-play method is an easier approach to getting complex agentic behaviour. One method (just as an example) would be to actually find the perfect cooperative prompt and show how it fails in the competitive case, demonstrating how much harder it would be to transfer the prompts.

For cooperative play, it is clear you are learning the rules of the game and cooperation. But what is being learned in the semi-competitive game? The competitive game includes the ability to exploit other agents, so are you really learning the game if you're not learning to exploit other agents? This is an interesting negative result that contributes to Ross et al (2024) if you're showing that even training on a competitive game does not easily achieve a competitive but altruistic strategy, but this should be clear.

- why do errors occur in 22% of cooperative games but only 1% of semi-competitive? (section 6.1)

- how can you be sure that human-AI performance is not bolstered by humans compensating for your AI playing badly?

- why do you talk about fully competitive games in both the intro and game objectives when communication is not useful in 2 player fully competitive games (Crawford and Sobel, 1982)

- Can you change the words "finetuning" in Section 5.3? It is very confusing to differentiate between the "warm-started" model and the act of iterative finetuning towards the task.

- You claim that Humans are to blame for not reading overly long messages but it could be that the blame is with the model for learning to generating long output: this is actually just alignment tax / language drift. As shown in Figure 3 left, is your model drifting away from human-preferred language towards longer useless text when being trained in self-play?

- Why do you include lying about an item preference value in your errors for 6.2? Lewis et al argued that this lying could be advantageous / effective deception.

- Your method of iterative finetuning with interactive LLMs with filtering is quite close to Rest-EM, so this probably deserves a citation.

- The negotiation game of Lewis et al (2017) itself based on a negotiation game of Devault et al (2017)

- The citation and explanation of how SPIN (Chen et al, 2024) is *not related* feels superfluous and strange. Just don't have it in related work.

- KL is always used to prevent language from drifting too far, CICERO is just a simple case of this. You can cite Jaques et al (2019) for this if you'd like. Also, if I'm not mistaken, the language component of CICERO was trained a bit separately from the game-playing component which is the real way it didn't drift too far from initialization. 

- Why are you citing Chen et al (2021) for GPT-3.5 in Section 3? I think this is a mistake

### Questions
**major**

- why do errors occur in 22% of cooperative games but only 1% of semi-competitive? (section 6.1)

- how can you be sure that human-AI performance is not bolstered by humans compensating for your AI playing badly?

**minor**

- why do you talk about fully competitive games in both the intro and game objectives when communication is not useful in 2 player fully competitive games (Crawford and Sobel, 1982)

- Can you change the words "finetuning" in Section 5.3? It is very confusing to differentiate between the "warm-started" model and the act of iterative finetuning towards the task.

- You claim that Humans are to blame for not reading overly long messages but it could be that the blame is with the model for learning to generating long output: this is actually just alignment tax / language drift. As shown in Figure 3 left, is your model drifting away from human-preferred language towards longer useless text when being trained in self-play?

- Why do you include lying about an item preference value in your errors for 6.2? Lewis et al argued that this lying could be advantageous / effective deception.

**references**

- Your method of iterative finetuning with interactive LLMs with filtering is quite close to [Rest-EM](https://arxiv.org/abs/2312.06585), so this probably deserves a citation.

- The negotiation game of Lewis et al (2017) itself based on a negotiation game of [Devault et al (2017)](https://aaai.org/papers/10335-10335-toward-natural-turn-taking-in-a-virtual-human-negotiation-agent/)

- The citation and explanation of how SPIN (Chen et al, 2024) is *not related* feels superfluous and strange. Just don't have it in related work.

- KL is always used to prevent language from drifting too far, CICERO is just a simple case of this. You can cite [Jaques et al (2019)](http://arxiv.org/abs/1907.00456) for this if you'd like. Also, if I'm not mistaken, the language component of CICERO was trained a bit separately from the game-playing component which is the real way it didn't drift too far from initialization. 

- Why are you citing Chen et al (2021) for GPT-3.5 in Section 3? I think this is a mistake

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores finetuning LLMs with self-play data in the negotiation game "Deal or No Deal" (DoND). The authors implement a filtered behavior cloning on LLMs and achieve promising results. They also build a web interface which allows humans to play DoND against their trained models. The experiments demonstrates that their method enables LLMs to achieve substantial performance gains across various game objectives—ranging from cooperative to competitive settings. The study also highlights improvements in task adherence and reduced hallucination rates, suggesting the models became more aligned with game rules over time.

### Strengths
- A key innovation of this work is the self-play training on large language models, which I believe is a novel approach. While self-play has been successfully used in other domains with smaller models, applying it to LLMs in a negotiation game is interesting. This novel approach expands the scope of self-play, making it as a promising technique for training LLMs in complex, dialogue-based tasks.
- The experimental results demonstrate substantial improvements, with the performance of the models increasing multiple times through finetuning.
- The modified DoND game environment in this paper is highly engaging for evaluation across different interaction types, including cooperative and competitive objectives.
- The authors plan to make their dataset and code publicly available, which may encourage further research in the field.

### Weaknesses
 - The study exclusively focuses on language models and does not incorporate any reinforcement learning (RL) baselines for comparison. Including RL-based models could have provided a broader benchmark, highlighting the unique contributions of self-play for LLMs while also revealing potential strengths or weaknesses relative to established RL techniques.
- The self-play data generation and subsequent finetuning require substantial computational resources, resulting in high training costs. The authors mentioned themselves in the paper that they only ran a small scale baseline experiment on GPT-4 due to its high cost.

### Questions
- Can you further elaborate why the performance in iteration 3 is worse in Table 1? Do you have any examples showcasing the overfitting?
- What do you think is the reason why open source LLMs cannot improve their performance with your method?
- How long does it take to finetune one round/iteration?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the application of self-play training to language models in non-zero-sum settings through experiments in the Deal or No Deal negotiation game. The authors modify DoND to create cooperative, semi-competitive, and strictly competitive game objectives. Empirical results show substantial improvements in model performance across cooperative and semi-competitive settings in self-play and interactions with humans, but limited gains in strictly competitive scenarios. The study also identifies increased instruction adherence and reduced hallucinations as benefits of self-play while noting limitations in strategic behavior learning.

### Strengths
1. The paper provides extensive quantitative results demonstrating significant performance improvements. And results show models trained with self-play perform better in collaboration with humans.
2. Includes detailed analysis of errors, agreement rates, and Pareto optimality.
3. Provides detailed insights, such analyses of dialogue length and hallucination rates.
4. The paper is clearly presented and easy to follow.

### Weaknesses
1. In cooperative games involving humans, performance declines as the number of rounds increases from 8 to 10. Why does this occur? This trend is not seen in other game settings.
2. The experiments and analysis are limited to a single game, which could introduce bias. Evaluations across additional environments are needed for validation.
3. The study only considers cooperative and semi-competitive settings. Including a wider range of competitive and cooperative levels could provide deeper insights into the impact of cooperation on the effectiveness of self-play.

### Questions
1. What could be the underlying reasons for the observed performance decline in cooperative games involving humans after 8 to 10 rounds? Why is this trend not present in other game settings?
2. What alternative environments/games could be explored to strengthen the study's findings?
3. Would expanding the study to include more competitive and cooperative levels provide a more comprehensive understanding of the impact of cooperation on self-play efficacy?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work studies whether self-play can improve language models' (LM) performance in cooperative and semi-cooperative games. They use Deal or No Deal (DoND) as the testbed and find self-play based on filtered behavior cloning significantly improves LMs' performance and generalizes to gameplay with humans.

### Strengths
1. Good clarity: the manuscript is well-organized and easy to follow. The DoND game and the idea of language model self-play are clearly described.
2. Good analysis and discussion: the authors give a detailed analysis of the effect of self-play in the DoND task. They also discuss the limitations and directions for future improvement.

### Weaknesses
This work studies the question of "whether techniques like self-play can effectively be used to improve language models (in cooperative tasks)". My main concern is that the current manuscript mainly presents preliminary empirical results and lacks solid and sufficient evidence to support a conclusion. Below is the detailed discussion.

1. Limited insights on why and how to make language model self-play work. Self-play has been known to be effective in non-language-based cooperative settings like MPE [1], SMAC [2], GRF [3], etc., so it is expected to work in language-based cooperative settings. Some previous work, as mentioned in the paper, finds that the self-play of language model can diverge from human-interpretable language, while this work finds it leads to performance improvement in DoND. Instead of just presenting these empirical findings, a more important question is to understand why language model self-play works in some tasks but fails in others, and how to make it work in more general tasks. However, this work mainly provides a limited and hypothetical analysis of this question in DoND only. It would be more insightful if the authors could investigate more general settings to provide an in-depth understanding behind the empirical findings.
2. Potential overclaim due to limited task, model, and training. This work investigates only one task (DoND) with one LM (GPT-3.5) and trained for just ten rounds. This is more like a case study and it would require evidence on more tasks with more LMs and training for more rounds to support the authors' claim that "self-play leads to large improvements in both the cooperative and semi-competitive settings" (L047-048). In fact, the authors also mentioned some preliminary results that may negatively impact the current claim.
    1. More models: as mentioned in L190, Mixtral 8x7B and LLaMA-2-70B fail to improve from the first round of self-play. This shows that self-play can lead to no improvement in some LMs. Providing results of Mixtral 8x7B and LLaMA-2-70B can examine the soundness of the claim.
    2. More training: as mentioned in L258-259, the authors "do not report score for any model after the 10th iteration as they to stabilize or even decline". If the performance can decrease with more training rounds, is it possible that, with more self-play rounds, the model will still diverge to uninterpretable language? It would be better if the authors could provide results of more iterations to examine the long-term stability of language model self-play.
    3. More tasks: as mentioned in L466-467, the performance increase in DoND "can be almost entirely attributed to an increase in the percentage of completed games, rather than better strategic reasoning or negotiation tactics". In fact, cooperative DoND may be too easy because the agents can simply share their values for each item and reach the optimal decision. The current results mainly show that self-play can improve LM's understanding of a specific task, instead of reasoning or decision-making ability. It would be more convincing if the authors could provide results in other more complex reasoning and decision-making tasks.

Therefore, I think the current manuscript mainly presents preliminary empirical results and lacks solid and sufficient evidence to support its claim.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
