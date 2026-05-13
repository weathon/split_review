# Are Large Vision Language Models Good Game Players?

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Large Vision Language Models (LVLMs) have demonstrated remarkable abilities in understanding and reasoning about both visual and textual information. However, existing evaluation methods for LVLMs, primarily based on benchmarks like Visual Question Answering and image captioning, often fail to capture the full scope of LVLMs' capabilities. These benchmarks are limited by issues such as inadequate assessment of detailed visual perception, data contamination, and a lack of focus on multi-turn reasoning. To address these challenges, we propose LVLM-Playground, a game-based evaluation framework designed to provide a comprehensive assessment of LVLMs' cognitive and reasoning skills in structured environments. LVLM-Playground uses a set of games to evaluate LVLMs on four core tasks: Perceiving, Question Answering, Rule Following, and End-to-End Playing, with each target task designed to assess specific abilities, including visual perception, reasoning, decision-making, etc. Based on this framework, we conduct extensive experiments that explore the limitations of current LVLMs, such as handling long structured outputs and perceiving detailed and dense elements.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To address the lack of a comprehensive evaluation framework for assessing Large Vision-Language Models (LVLMs), this study proposes a framework called LVLM-Playground with game-base evaluation. This study collects six games: Tic-Tac-Toe, Reversi, Minesweeper, Gomoku, Sudoku, and Chess, to evaluate both powerful open-source and closed-source models across four tasks: Perceiving, Question Answering, Rule Following, and End-to-End (E2E) Playing. The framework provides insights into the performance shortcomings and iterative improvements of LVLMs. The study also finds that a small amount of data from games can enhance the model's reasoning abilities significantly.

### Strengths
1. This study collects multiple games to evaluate the multimodal large models' abilities in perception, reasoning, decision-making, and adversary, and it also visualizes the games.

2. This study evaluates the top-performing models and presents multiple findings, providing guidance for future improvements of multimodal models.

3. The authors proposed a set of metrics to evaluate the difficulty of test games in terms of Perception, Reasoning, Decision, and Adversary, which can aid in assessing game-based evaluations when selecting games in the future.

### Weaknesses
1. I noticed that in **Findings 6. Gameplay Data Could Enhance LVLMs' Reasoning During SFT**," the early work MiniGPT-4 was used as a base model. Since the SFT stage of MiniGPT-4 only used detail description data, it is difficult to prove that the performance gains are due to the VQA data from the game, rather than other factors like data format. Therefore, I believe that the experiments in Table 5 are not sufficient to fully support your conclusions. I suggest supplementing this with more robust base models, such as LLaVA-1.5 or LLaVA-one-vision.

2. In my opinion, these types of games are all based on dense grid patterns, and the format used to output game states might be too challenging for current multimodal large models. This could potentially limit the evaluation of the model's decision-making abilities.

### Questions
1. I have noticed that various models are currently unable to succeed under the E2E play setting. However, E2E play is a very important setting in LVLM-Playground. Would it be possible to introduce intermediate evaluation metrics to assess model performance?

### Soundness
3

### Presentation
3

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
The primary focus of this paper is the evaluation of “LVLMs” (Large Vision Language Models).  The authors motivate the work by noting that prior benchmarks have three key shortcomings: (i) they fail to assess detailed visual reasoning, (ii) they suffer from data contamination and (iii) they fail to assess multi-turn reasoning.  In response, the authors introduce an evaluation framework called LVLM-Playground that uses 6 games (TicTacToe, Reversi, Sudoku, Minesweeper, Gomoku and Chess) to measure LVLM capabilities. Using these games, the authors assess model performance along 4 axes: perception (i.e., accurate inference of the board state), rule following (whether a given model takes legal moves), question answering (whether the model can answer questions about a game state), and gameplay.  Through their experiments, the authors demonstrate that while frontier models are best at perception, they are (somewhat surprisingly) weaker than open-source models on question-answering tasks. This latter result is investigated and attributed to the influence of post-training (via RLHF). All models completely fail to achieve reasonable gameplay performance across the game suite against strong opponents.

### Strengths
Originality: Leaving aside concurrent work (mentioned below), this is the first work to extend simple game-based evaluations for LLMs to include a detailed evaluation of perception capabilities.

Significance: By introducing a visual component into simple game-based evaluation, the authors open up an interesting avenue of possibilities for efficient evaluation of model capabilities. Board games (such as chess in particular) are well-suited for benchmark generation since simulators provide automatic ground-truth and their large state space renders them relatively immune to contamination. The fact that frontier models struggle on the Chess perception task (Table 2) indicates that there is scope to guide future model development with this approach. As such, I think this work will provide a useful point of reference for the community. 

Clarity: By highlighting challenges with previous benchmarks, the problem is clearly motivated. More broadly, the paper is clearly well-written, and the figures do a good job of communicating key information. Figure 4, for example, communicates the key takeaways of the paper in a compact way.

Quality: Beyond simply using games to construct a benchmark, I think the construction of several game-related subtasks is particularly useful. In particular, examining model capabilities on each game with respect to perception, Q&A and rule following is a nice way to extract additional information beyond end-to-end game playing ability.

### Weaknesses
1. One concern relates to the scale of the overall contribution. As the authors note, there are previous efforts such as SmartPlay (Wu et al., 2023) and GAMA-Bench (Huang et al., 2024) that explore the use of games for evaluating LLMs. The SmartPlay work, for example, also proposes a suite of games and assesses the individual capabilities (such as instruction following, reasoning and planning). As the authors highlight, it is true that these works only operate in text-space (SmartPlay converts image input into text-based visual descriptions for games that require it, rather than feeding in RGB images to the models). This is an important distinction, particularly given the focus of the current submission on assessing detailed perception. Nevertheless, the proximity of prior work somewhat diminishes the contribution of this submission.

2. A second concern relates to the breadth and depth of the analysis. On the one hand, I think the authors did an excellent job of conducting qualitative analysis (both in the form of the findings described in Section 4.1 and the observations contained within Section D of the Appendix).  On the other hand, I think the paper could have been improved by conducting more extensive quantitative analysis to provide further insight. To give a couple of concrete examples: (i) It would be interesting to see how perception performance on games like Gomoku and Chess varies as a function of board complexity (number of pieces on the board); (ii) It would be insightful to perform a manual categorization of a sample of errors on the question-answering task to inform the reader about the distribution of error types that are harming model performance.

### Questions
1. I’m curious to better understand the motivation behind the authors’ choice of using "unbeaten rate" to measure gameplay performance? Given access to games simulators which enable repeated games, this seems like a very high variance estimator of capability. Moreover, it is tightly anchored to the choice of opponent implementation for each game.  Did the authors consider alternatives (for example, creating a pool of opponents at different thresholds and computing Elo ratings?)

2. Related to the first question, did the authors consider evaluation against non-search based opponents? Taking Tic-Tac-Toe as an example, presumably minimax will produce optimal play, so the best that can be achieved is a sequence of draws?

Suggestion: I don’t list this point as  a “weakness” since it is concurrent work, but I would suggest citing relevant pre-prints from the first half of 2024 exploring similar directions. Examples include (1) GTBench (Duan et al., 2024), which also concludes that LLMs struggle against search-based strategies (e.g. MCTS) in games like Tic-Tac-Toe. For this reason, they also include a “random agent” baseline to illustrate that the models have achieved a basic level of competency.  (2) GameBench (Costarelli et al., 2024), which evaluates LLMs across 9 game environments and uses visual input (for models that support this). 

References:
- J. Duan et al., "GTBench: Uncovering the strategic reasoning limitations of LLMs via game-theoretic evaluations." arXiv preprint arXiv:2402.12348 (2024)
- Costarelli, Anthony, et al. "GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents." arXiv preprint arXiv:2406.06613 (2024).

Minor typos/suggestions:
- Minor typo on L379 (missing parenthesis)
- Claude “soonet” is presumably intended to be sonnet in table 4.1 (this typo appears in multiple various places in the paper)
- This is a minor point, but I would suggest citing MuZero in the related work section. This is perhaps the canonical example of achieving very strong performance across multiple games (including Chess, which is used in the current submission) while also being capable of processing RGB input on Atari games by leveraging both learning and search.  Reference: Schrittwieser et al., “Mastering atari, go, chess and shogi by planning with a learned model” (Nature, 2020)

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
This paper proposes a new benchmark to evaluate large vision-language models in structured environments across 4 tasks in 6 games of different difficulties. This benchmark is designed to evaluate different abilities of vision-language models including perception, reasoning, decision-making and adversary.

### Strengths
- This paper is well-motivated and well-written overall. 
- The idea of using structured game environments to evaluate vision-language models is somewhat novel. 
- Some designs of the benchmark are well thought out: for example, it includes games that test different abilities of the vision-language models and cover different difficulty levels and provides clear definitions of the complexity of each ability. 
- The paper is clearly written with sufficient technical details and effective illustrations.

### Weaknesses
The main area of improvement for this paper is the alignment between the experimental designs and the claims. The reviewer is mainly concerned about some of the evaluation task designs and whether they actually test vision-language models’ perception or reasoning abilities like the authors claim. 
- For example, the perceiving task prompts the models to output matrices that correspond to the game states, which not only tests for perception but also requires strong instruction-following ability. Similarly, while the Q&A is mostly designed to test for perception and reasoning (Figure 3), it asks the models to output answers in a particular format and therefore also requires strong instruction-following ability. 
- As the authors discussed in finding 3, all commercial models fail to match the output format or refuse to answer in the Q&A task, which means this task doesn’t actually test their perception/reasoning ability as claimed. 
- In the reviewer’s opinions, the tasks can be designed better to decouple the evaluations of perception/reasoning and instruction following abilities. 
- For example, most VLM evaluation benchmarks adopt the multi-choice Q&A format when testing for their perception/reasoning abilities. And when the answer format is free-form, VLMEvalKit -- one of the most widely used evaluation frameworks of VLMs – uses an LLM as an answer extractor, putting more emphasis on the models’ perception/reasoning abilities rather than their instruction-following ability. 
- Due to the differences in task and evaluation designs, the results reported in this paper (e.g. Table 3) regarding these models’ perception and reasoning abilities deviate a lot from existing works. 
- The authors also claim that gameplay data could enhance LVLM’s reasoning abilities but have only provided very limited evidence on a subset of one VQA benchmark.

### Questions
-	The reviewer appreciates that the authors conducted a human study on the difficulty rating, which mostly though not perfectly aligns with the difficulty rating defined by the authors. The reviewer wonders if the authors could also obtain human ratings for the four dimensions 
-	For finding 6, did the authors use a randomly sampled subset of VQA? Does this subset test for VLMs’ reasoning ability? If not, the authors could consider using a more suitable benchmark or revising their claim.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents LVLM-Playground, a game-based benchmark for evaluating Large Vision Language Models (LVLMs). Using six diverse games and four tasks (Perceiving, Question Answering, Rule Following, and End-to-End Playing), it assesses LVLMs' abilities beyond the limitations of traditional VQA benchmarks. Experiments reveal model weaknesses in handling long outputs, detailed perception, and instruction following (potentially due to RLHF), while also showing that gameplay data can improve reasoning during fine-tuning.

### Strengths
1. Novel Benchmark: LVLM-Playground provides a novel, game-based approach to evaluating LVLMs, offering a more dynamic and comprehensive assessment than traditional benchmarks.

2. Rigorous Methodology: The paper presents a well-structured and technically sound methodology, with detailed task formulations, evaluation metrics, and implementation of AI opponents.

3. Significant Findings:  The benchmark reveals key limitations in current LVLMs, particularly in handling complex visual details and instruction following, while also suggesting gameplay data as a potential avenue for improvement.

### Weaknesses
Re. Finding 3 - I find it less sound. Maybe I am missing something, but -  Yes, VLMs produce long answers, and the expected answers are short, but this is an evaluation problem, not the model’s fault. There  are several ways to overcome it - few-shot prompts with short answers, parsing the answers with regex to a closed set of answers, a model-based LLM, and so on.

### Questions
The LVLM-Playground framework seems highly beneficial for the community. Do the authors plan to publicly release the code and data?

Could the authors elaborate on the evaluation of the Q&A task? Are the methods I mentioned (few-shots, LLM-based evaluation, etc) relevant for overcoming the issue you mentioned?

### Soundness
3

### Presentation
4

### Contribution
4
