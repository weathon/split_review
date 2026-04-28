# PuzzlePlex: A Benchmark to Evaluate the Reasoning and Planning of Large Language Models on Puzzles

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Large Language Models (LLMs) have demonstrated remarkable performance in various tasks, yet their comprehensive reasoning and planning capabilities in interactive environments remain underexplored. We introduce PuzzlePlex, a benchmark designed to evaluate reasoning and planning capabilities in a multi-turn adversarial environment. 
PuzzlePlex comprises 24 diverse puzzles, including deterministic and stochastic games, as well as single-player and adversarial scenarios. An important novelty of our benchmark is that it includes multi-step adversarial reasoning games. To succeed in such games, each LLM must maintain a history of its own moves and those of the opponent LLM, generating strategies that outperform the opponent to secure victory.
We implement customized game-playing strategies (such as dynamic programming approaches)  for comparison. 
Our findings indicate that the reasoning and planning abilities of current LLMs are currently poor in puzzle-solving contexts. GPT-4 outperforms other models, successfully competing against customized strategies (such as greedy approaches or dynamic programming) in 49% of cases. However, when faced with strict rule sets, it demonstrates diminished reasoning and planning capabilities. In addition to the 14 multi-turn adversarial puzzles, we report on single-player puzzles and incorporate multi-modal challenges that integrate text and images, revealing that LLMs still significantly lag behind even simple heuristics  in puzzles.
A key feature of our benchmark is its ability to generate game instances with graduated levels of difficulty, allowing it to evolve as LLMs become more sophisticated. This adaptability ensures the continued relevance and utility of PuzzlePlex in assessing the progress of LLM capabilities in reasoning and planning within interactive environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The work introduces a new benchmark, puzzleplex, which helps evaluate LLMs' abilities in solving puzzle-based games. The benchmark covers 24 different puzzles for evaluation, and highlights its inclusion of multi-step adversarial reasoning games. The benchmark evaluate some popular LLMs in its experiments, and show that existing LLMs fail to play very well against rule-based baselines.
------------------------------------
Thanks authors for the response. I think the ToT complementary results are very illustrating; but it is vital to be implemented for all tested LLMs and datasets considering the community's wide recognition of the method for puzzle-solving games. However, the analysis from my view still lacks enough quantitative results, and the authors do not provide how fine-tuning would improve those open models. I believe the work could have more solid contributions by completing those details. So I prefer to maintain my score.

### Strengths
1. Good Motivation: Planning and reasoning are crucial for next-level LLMs. The benchmark could be timely for the community.
1. Systematic Benchmarking: I believe the benchmark provides useful resources for the community, and the results is of reference value to LLM development. I believe the authors have paid much efforts in building it.

### Weaknesses
1. Lack of analysis: While the construction of the benchmark is valuable, I think it is necessary for a benchmarking work to present sufficient analysis on its observation to guide later research and LLM training. However, the insights and analysis provided in this work is very limited, and the main observation of LLMs' lacking planning abilities in puzzle-solving is well-recognized in literature. I think authors should go deeper into the planning and reasoning behaviors of examined LLMs, providing quantitative insights into how LLMs could be improved,  strengths and shortcomings of representative specific LLM, and how open/proprietary LLMs differ.
2. Insufficient prompting strategy: As authors stated in related work, in Tree-of-Thought (ToT) the authors have identified that mere ReAct fails to reasonably represent LLMs' potential in solving puzzle-based games, and ToT could be necessary in such context. However, in PuzzlePlex, it is still the ReAct that is used for prompting rather than the ToT. As a result, I think the current conclusion in this work is of less referential value to community. I suggest authors to use ToT as a major prompting method here, which could significantly improve the referential value of insights in this paper.
3. Fail to show how to improve: As puzzle-based games have strong rule-based baselines, it is valuable to generate data in this way and train open LLMs on the problem to see if there is any reasonable improvement. The LLM community has witnessed too many prompting-based benchmarks in recent years but few endeavor to show how research and open-source community could catch up with proprietary ones.

### Questions
For adversarial multi-turn evaluation, there is a reference work AgentBench[1] in LLM Agent study, which includes an environment called Digital Card Game where evaluated LLMs need to play against rule-based methods and switch sides for each game. I think the authors should consider including the work as a reference.

[1] AgentBench: Evaluating LLMs as Agents (ICLR 24)

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors propose "PUZZLEPLEX", a benchmark that evaluates LLM reasoning and planning capabilities in a multi-turn adversarial environment. The authors also perform experimentation showing that LLM doesn't perform well in this benchmark.

### Strengths
1. The authors propose 24 parametrizable  puzzles
2. the authors propose experimentation on these puzzles, showing llm still can't solve them.

### Weaknesses
1. The binary/ternary scoring system (0,1 for single-player; 0,0.5,1 for adversarial) may be too simplistic and mask important performance nuances
2. No ablation studies to understand which aspects of the puzzles are most challenging for LLMs
3. No discussion of computational resources required or runtime comparisons
4. I would appreciate animation of the puzzle or visualization of it.

### Questions
1. Did you finetune the model on this benchmark? does fientuning help?
2. Did you provide a few-shot example when testing the evaluation? Does the performance improve when you provide some demonstration?
3. How would you expect LLM to solve it, do you think better planning technique would help?

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
3

### Summary
This paper provides a set of 24 puzzles benchmark for assessing the reasoning capabilities of LLMs. The puzzles cover a variety of task types such as single-player/multiplayer, adversarial, deterministic/stochastic, and two modalities of text-only and text-image. The authors then evaluate various open-source and proprietary LLMs, concluding that GPT4-o surpasses all other LLMs. The image-text puzzles also show the low performance of all LLMs on such tasks.

### Strengths
* The paper is well-written and easy to follow.
* Proposing benchmarks to asses the reasoning abilities of LLMs is an important task in the right direction.
* The puzzles support a high variety of possible situations.

### Weaknesses
 * It is not clear how much utility can PuzzlePlex introduce in addition to the previous work SmartPlay (Wu et al., 2024). From what I understand, the main advantage of PuzzlePlex over SmarPlay is the presence of text-image puzzles and difficulty levels. But, the benchmark has only three image-text puzzles, all three of which are the visualized versions of text puzzles. In other words, the tasks are not inherently visual (e.g., like a task such as a jigsaw puzzle), but rather, a powerful enough OCR and a chain-of-thought prompt can bridge the gap between the visual puzzle and text puzzle.

* It is not clear how the puzzles are chosen. I understand the tasks are categorized into different natures. But, what capability is each puzzle measuring? (For instance, long context understanding? Spatial reasoning? Learning from interaction?). Such a categorization is present in SmartPlay while missing in PuzzlePlex.

* Tables 4 and 5 have missing numbers. Is there any particular reason?
* In line 197, the reference to the Communications of the ACM is not correctly written.

### Questions
* Tables 4 and 5 have missing numbers. Is there any particular reason?
* In line 197, the reference to the Communications of the ACM is not correctly written.

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
This paper provides a new benchmark called PuzzlePlex for evaluating reasoning and planning in LLMs. The benchmark consists of 24 puzzles that can be categorized into various types: single-player determinstic vs. stochastic games, and adversarial deterministic vs. stochastic games. In addition, the puzzles are parametrizable in order to provide multiple levels of difficulty. The benchmark is the first to include both single-player and adversarial (2-player) scenarios, as well as to include text-image puzzles. The work evaluates a suite of models on the benchmark and finds that while GPT-4o is generally the strongest model, there is still significant room for improvement.

### Strengths
The paper has several strengths:
1. The work provides a timely benchmark: there is currently a lot of interest in the field in making LLMs better planners an reasoners, and evaluation is an important component of this.
2. Included in the benchmark are classic game-playing and puzzle-solving baseline techniques against which to compare LLMs. 
3. The benchmark provides multiple levels of difficulty in order to retain its relevance and usefulness as LLMs grow stronger over time.
4. The benchmark provides a good variety of game properties: single-player vs. adversarial (two-player), deterministic vs. stochastic., and text vs. text-image.

### Weaknesses
The paper has several weaknesses:
1. There are no CIs or SEs included in the result tables, making it hard to judge sometimes whether results are significant. It would be great if these statistics could be added (probably best in the appendix).
2. It doesn’t seem the authors tried any agent baselines like ReAct [1], Reflexion [2], or inference time methods like Tree-of-Thoughts (ToT) [3]. These kind of methods have been shown to dramatically increase performance sometimes (e.g. Game of 24 in ToT paper which went from 4% success rate to 74% success rate). Without these, it’s unclear what the real ceiling is for these models currently on this benchmark, making it hard to assess how challenging and useful the benchmark will be going forward.
3. The paper generally feels a bit rushed and could use a bit more structure. For example, there is quite a few result tables but oftentimes the captions don’t provide short takeaways (e.g. see the caption for Table 6) making it hard to remember what the purpose of each result table is. In addition, when following the Github link for the code it turns out that some of the figures in the paper are incorrect and the correct ones are included in the repo. These kind of things indicate the paper could potentially benefit from another round of refinement.
4. In section 4.5, the authors identify several types of errors that GPT-4o and Qwen2-72B encounter when playing the puzzles. However, there are no quantitative examples illustrating these kind of errors, nor any quantitative metrics as to how often each of these error types happen, which one is the most common, etc.

### Questions
1. Figure 1 includes an “Evaluator” which is discussed a bit further in Section 3.1 but for the rest doesn’t appear in the paper. Could the authors elaborate a bit on what kind of system the evaluator is and how exactly it works?
2. The paper uses the term “adversarial game” quite a bit. What about these games is adversarial? I don’t fully understand the difference between this and standard competitive 2-player games. Could the authors please clarify?
3. For the tables on the right in Figures 2 & 3, who is the win rate computed against?
4. “To mitigate the risk of exceeding the contextual length, given the likelihood of multiple turns in our games, our evaluation primarily adopts a zero-shot CoT approach.” Do the authors have a sense of how long the current context windows are getting? Models these days can handle pretty large context lengths, so I would be very curious if you’re running into those limits. 
5. In Section 4.1 under the paragraph “Adversarial Text Puzzles”, should Table 4 be Table 3 instead?

### Soundness
3

### Presentation
2

### Contribution
3
