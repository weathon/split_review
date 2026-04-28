# GameArena: Evaluating LLM Reasoning through Live Computer Games

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Evaluating the reasoning abilities of large language models (LLMs) is challenging.
Existing benchmarks often depend on static datasets, which are vulnerable to data contamination and may get saturated over time, or on binary live human feedback that conflates reasoning with other abilities. As the most prominent dynamic benchmark, Chatbot Arena evaluates open-ended questions in real-world settings, but lacks the granularity in assessing specific reasoning capabilities.
We introduce \sysname, a dynamic benchmark designed to evaluate LLM reasoning capabilities through interactive gameplay with humans. 
\sysname consists of three games designed to test specific reasoning capabilities  (e.g., deductive and inductive reasoning), while keeping participants entertained and engaged.
We analyze the gaming data retrospectively to uncover the underlying reasoning processes of LLMs and measure their fine-grained reasoning capabilities.
We collect over 2000 game sessions and provide detailed assessments of various reasoning capabilities for five state-of-the-art LLMs. Our user study with 100 participants suggests that \sysname improves user engagement compared to Chatbot Arena. For the first time, \sysname enables the collection of step-by-step LLM reasoning data in the wild.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a new benchmark to evaluate LLM's reasoning capabilities across different reasoning categories. To mitigate issues of data contamination and unspecific human evaluation/comparisons, the authors propose to use three simple text games, where the process of reaching the game answer could also be leveraged to evaluate a model's reasoning capabilities. Moreover, the authors claim that by gamifying the evaluation process, human users are more engaged in the process, leading to better evaluation metrics.
Three games with different rules and goals are used to collect over 2000 interaction sessions, which are then analyzed to compare performance metrics across different open and closed LLMs.

### Strengths
The paper is well-written and fairly clear. It presents and interesting idea to bypass data contamination issues when evaluating LLM capabilities by leveraging text-based games and the sequence of response rounds during their play, to try and evaluate the reasoning abilities of a given model in different dimensions. 

The proposed approach also emphasizes that models output their "rationale" for each game round response, and these are then used to calculate specific metrics that map to the reasoning categories being  evaluated in each game. Such mapping and analysis techniques can highlight important aspects usually not well covered in current benchmarks.

Moreover, specially when such evaluations involve humans, as in the compared Chatbot Arena, gamifying the experience seems and attractive idea.

### Weaknesses
I really like the intended approach and the motivation for the proposed analysis, however, I see a couple weaknesses.

Firstly, the analysis of reasoning capabilities depends on a "replay" of a concluded game session round by round. At each round the replay prompt asks the models to output their "intermediary thought process". As LLMs are know for hallucination and fabricating rationalizations, this could heavily affect the proposed approach. There is no guarantee that whatever "evidence" being generated actually directly corresponds to the original inference rounds. A more robust approach to collect the data might have been to ask for such output during the game. The output pieces for such data could be hidden from the human users through a simple UI.

The selected games also do not necessarily require the level of abstract reasoning being attributed to them in the paper. Akinator/Q20, for example, can be seen as a simple bisect search. Perhaps to properly evaluate deductive/abductive/inductive reasoning, the responses first should have been turned into such problems and then LLMs re-queried to check for response matches. It's also been shown that LLMs don't necessarily perform multi-hop reasoning/answering, but infer a final response based on other context. To claim multi-hop reasoning, more evidence would be required.

The text of the paper, while overall well written and clear, also tends to overclaim, both in terms of reasoning conclusion without enough evidence, but in using terms like "exceptional multi-hop reasoning" (line 377).

Lastly, the comparative study against Chatbot Arena is too shallow and uses limited data. The conclusions attributed to it don't seem solid nor significant for the overall paper. Similar comments apply to the ranking comparisons in 4.5.

### Questions
Claims about reasoning, especially specific types of reasoning, require stronger evidence to support them. I'd expect to see a t least a couple case studies to support the claims presented in the evaluation. Not only some metrics and no detailed analysis.

If Table 2 lists GPT-4o as the best model for Taboo, why don't the metrics in Table 3 support that? The only discussion of the results for the Bluffing game also don't even mention how the described behaviour of other models relates to Claude 3.5 superior performance. 

The calculation of disparity ratio in 3.2.2 is also not detailed enough. The authors claim the metric quantifies how effectively each step divides the answer space into two categories. But it only counts yes/no responses ratios?

In 4.1 the authors state the prompt optimization process uses 200 of the collected game sessions. Does this mean all data collection uses one set of prompts and the analysis uses the different optimized prompts?

Will the code used to calculate the different metrics be released openly? I feel this is a critical step for such benchmarks, as it would allow refining and standardization of definitions and calculations for re-use and reproducibility. Even if the direct mapping to specific reasoning categories describe is still not ideal.


As the comparison with Chatbot Arena and ranking comparisons don't seem to add much to support the main paper contributions, perhaps these could go into appendices to open space for more detailed analysis of the reasoning results.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The author proposes a novel interactive benching platform, GameArena, for evaluating LLM reasoning capability through designed games with humans. Three tasks are included to evaluate deductive, abductive, and inductive reasoning capabilities. Through comparison between GameArena and commonly used Chatbot Arena. The proposed GameArena exhibits a higher rate of useful data for evaluation. Incorporating 100 participants and five SOTA models, the author conducted comprehensive experiments and detailed analysis.

### Strengths
Within 10 pages of content, the paper managed to include abundant information including a detailed description of proposed tasks, comprehensive experimental settings, and multi-aspects analysis across five SOTA models. The author includes three separate games each well evaluating the capability of one specific reasoning skill possessed by tested LLM.  The results and conclusions are solid and well organized. I believe such research could highly benefit the academic society as a reasoning benchmark.

### Weaknesses
- In lines 82 to 84, the author states the effectiveness of data collection sorely based on reasoning assessment. The comparison may not be fair since Chatbot Arena aims to evaluate human preference across a gigantic number of tasks and each pair-wise comparison contributes to the ranking. 
- The description of the Taboo game in Figure 2 is confusing. The target of "utter the target word unconsciously" is ambiguous. An example of human win would be better to demonstrate the expected response fits the target. 
- In line 249, the author mentions "lower the disparity ratio, the higher information gain". But in Akinator game, I suppose both "yes" or "no" narrow down the range of the actual object.  A positive does not contribute more information than a negative response.

### Questions
In section 4.3, a brief demographic information could be described for the recruited 100 participants.
Other than reasoning evaluation, is it possible to assess the preference factors from the comparison data? I bring up this question only out of curiosity. The current contribution is sufficient for this benchmark. It could gain more attention if it can potentially elicit the preference of human evaluators.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces GameArena, a dynamic benchmark designed to evaluate the reasoning capabilities of LLMs. GameArena uses structured games (Akinator, Taboo, and Bluffing) that engage human players while collecting detailed step-by-step reasoning data from LLMs. This paper assess deductive, inductive, abductive, and multi-hop reasoning abilities. It compares GameArena to Chatbot Arena, finding that GameArena yields higher user engagement and more useful data for evaluating reasoning. The paper ranks five state-of-the-art LLMs, showcasing its effectiveness in fine-grained reasoning assessment.

### Strengths
+ Carefully designed metrics.
+ Gamified framework boosts human interests and willingness in participating in the evaluations.
+ Extensive experiments including 5 models, including open-sourced ones and commercial ones.

### Weaknesses
 -  The motivation, especially how using this benchmark can have findings different from / aligning with other benchmarks, such as Chatbot Arena, GameBench, or GTBench, needs further explanation. How can the findings generalize to other games / downstream tasks?
- Results need deeper analysis (question 3, 6).
- Lack of detailed game statistics, for example, the distribution of target words, etc. (question 4). This could be some potential biases for models.

### Questions
The paper is very interesting overall. I enjoy reading how LLMs perform in these games and how to design appropriate metrics to analyze LLMs’ performance. However, I think the authors should make it clearer why choosing these three games, probably at the beginning. There are games like Who Is Spy, Avalon, which can also evaluate LLMs’ reasoning ability.

I have some questions:

1.	How many data did Chatbot Arena and GameArena collect respectively during that period? Maybe we could not compare solely on efficiency rate.
2.	About the recall rate in the Bluffing game: in my understanding, the ground truth is either True or False, while the prediction is a 5-level Likert scale. How to calculate recall rate in this case?
3.	Why GPT-4o performs the best in the Taboo game in terms of win rate, but is not the best in terms of multi-hop reasoning and abductive reasoning?
4.	What is the diversity of user-generated objects (for Akinator game), statements (for Bluffing game), and system-pre-defined target words (for Taboo game)?
5.	What are the temperature, top_p, and other parameters you used for the LLMs?
6.	Is there any superficial correlation (shortcut learning) in LLMs’ responses? For example, after responding “Eggs, of course” in Figure 2, the system prompts the LLM that the target word has appears. But it is obvious that the word is Egg – one can tell even without previous context.
7.	Some existing work also uses social deduction games to evaluate LLMs’ reasoning abilities, like Werewolf [1], Avalon [2,3], Taboo game [4], and Who is Spy [5]. What is the contribution of this paper except using some different games?
8.	The intermediate results are obtained after gaming in my understanding. Did you try to use these intermediate results when gaming to serve as a special CoT method to improve model performance?
9.	What is the correlation with Chatbot Arena? How much performance (either good or bad) in GameArena can correlate with performance on Chatbot Arena? And how much cannot?

[1] Zelai Xu, Chao Yu, Fei Fang, Yu Wang, and Yi Wu. 2023. Language agents with reinforcement learning for strategic play in the werewolf game. arXiv Preprint: 2310.18940.

[2] Shenzhi Wang, Chang Liu, Zilong Zheng, Siyuan Qi, Shuo Chen, Qisen Yang, Andrew Zhao, Chaofei Wang, Shiji Song, and Gao Huang. 2023. Avalon’s game of thoughts: Battle against deception through recursive contemplation. arXiv Preprint: 2310.01320.

[3] Ziyi Liu, Abhishek Anand, Pei Zhou, Jen-tse Huang, Jieyu Zhao. 2024. InterIntent: Investigating Social Intelligence of LLMs via Intention Understanding in an Interactive Game Context. arXiv Preprint: 2406.12203.

[4] Pengyu Cheng, Tianhao Hu, Han Xu, Zhisong Zhang, Yong Dai, Lei Han, Nan Du. 2024. Self-playing Adversarial Language Game Enhances LLM Reasoning. arXiv Preprint: 2404.10642.

[5] Tian Liang, Zhiwei He, Jen-tse Huang, Wenxuan Wang, Wenxiang Jiao, Rui Wang, Yujiu Yang, Zhaopeng Tu, Shuming Shi, Xing Wang. 2023. Leveraging Word Guessing Games to Assess the Intelligence of Large Language Models. arXiv Preprint: 2310.20499.

Overall, the presentation is good in this paper. There are still some minor issues:

1.	Line 254: the “average round number” might be ambiguous. It can refer to a certain round like the i-th round, or the total number of rounds.
2.	Table 2 & 3: It will be better to put the models in the same order for a more convenient comparison.
3.	Figure 5: the caption should appear below the figure.
4.	An extra “without” at line 782.

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
This paper presents GameArena, designed for evaluating LLM reasoning capabilities through interactive games with humans. It consists of three games for three reasoning abilities (Akinator game: deductive and multi-hop reasoning; AI Taboo game: abductive and multi-hop reasoning; AI Bluffing game: inductive and multi-hope reasoning). They collected more than 2,000 game sessions with 100 participants and evaluated five current LLMs through analyzing the reasoning steps retrospectively. They also show that their gamified platform allows a better user engagement through data collection, and more useful (meaningful) data when compared with current popular ChatArena platform.

### Strengths
1. Construct an interesting benchmark LiveBench that can capture three different types of reasoning (deductive, abductive and inductive), and build an interactive game platform that potentially allows real-time/live data collection.
2. Describe the benchmark construction steps clearly with illustrative examples and show clear motivations for each game included for evaluations.
3. Good designs on metrics (recall rate, disparity ratio, average first appear, average final rank etc) that can demonstrate the specific LLM reasoning abilities comprehensively.
4. Evaluation on data efficiency between ChatbotArena and Game Arena(4.2) is done well alongside Human validation on the reliability of the ranking system (4.5).

### Weaknesses
1. Regarding Table 4 on comparing GameArena, ChatArena, GPQA ranking, having n = 5 seems too small to have stat. significant result given that the statistics in Table 4 are mostly the same between three especially bluffing aspects. Recommended to validate with more samples or provide p-values to show they are stat significant result.
2. Does not mention the potential limitations of the work: it could relate to the benchmark topic distribution, the annotators distribution and any things that are worth mentioning if people are going to use this benchmark.
3. The notion of this work being the first to apply GWAP techniques for benchmarking LLMs (line 525) is not fully correct. Researchers in other subfields (e.g. HCI: human-AI collaboration, AI-augmentation) have investigated this for a long time. It is better to cite some recent relevant works on annotation and benchmarks. For example, guessing names for subcultures: DOSA [1] ; human-AI redteaming game on cultural knowledge benchmarks: CulturalBench [2]; annotation game on image caption: SentenceRacer [3]

### Questions
1. Can you provide benchmark statistics (e.g. topic) and annotator demographics to show if the users inputs are diverse and give a bigger picture of this benchmark? 
2. In Section 4.2 (line 327), for the comparison between Chatbot Arena and GameArena, is GameArena also collected in the wild during the same period? It seems unfair to compare the data efficiency between two if GameArena gives money incentives but ChatbotArena depends on community engagement (which is reasonable to have lower efficiency).
3. It would be great if you can provide some lessons learned on your work to inspire future research. Any insights on constructing the data collection? Any discussion/trend on the reasoning evaluation results? Any future work direction? Without such lessons, it’s hard to understand what readers should take away from this work (besides the benchmark contribution, which is valuable in itself).

### Soundness
3

### Presentation
4

### Contribution
3
