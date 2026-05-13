# TMGBench: A Systematic Game Benchmark for Evaluating Strategic Reasoning Abilities of LLMs

- Decision: Reject
- Scores: 5, 5, 8, 5

## Abstract
The rapid advancement of large language models (LLMs) has accelerated their application in reasoning, with strategic reasoning drawing increasing attention.
To evaluate the strategic reasoning capabilities of LLMs, game theory, with its concise structure, has become the preferred approach for many researchers.
However, current research typically focuses on a limited selection of games, resulting in low coverage of game types. 
Additionally, classic game scenarios carry risks of data leakage, and the benchmarks used often lack extensibility, rendering them inadequate for evaluating state-of-the-art models.}, a benchmark characterized by comprehensive game type coverage, novel and diverse scenarios, and flexible game organization. 
Specifically, we incorporate all 144 game types summarized by the Robinson-Goforth topology of 2×2 games, which are constructed as classic games in our benchmark. 
Furthermore, we employ synthetic data generation techniques to create diverse, higher-quality game scenarios through topic guidance and human inspection for each classic game, which we refer to as story-based games.
Lastly, to provide a sustainable evaluation framework adaptable to increasingly powerful LLMs, we treat the aforementioned games as atomic units and organize them into more complex forms through sequential, parallel, and nested structures.
We conducted a comprehensive evaluation of mainstream LLMs, covering tests on rational reasoning, reasoning robustness, Theory-of-Mind capabilities, and reasoning in complex game forms. 
The results revealed that 
LLMs still have flaws in the accuracy and consistency of strategic reasoning processes, and their levels of mastery over Theory-of-Mind also vary.
Additionally, o1-mini, the latest reasoning model from OpenAI, was also evaluated across the sequential, parallel, and nested game structures and reached accuracy rates of 66.6\%, 60.0\%, and 70.0\%, respectively, highlighting the challenges posed by {\bench}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces TMGBENCH, a benchmark for systematically evaluating the strategic reasoning abilities of LLMs. By evaluating some LLMs on TMGBENCH, the paper identifies several flaws in LLMs’ performance, such as low accuracy rates and unstable inconsistency.

### Strengths
- The paper is well written and well organized.
- The games included in TMGBENCH are comphrehensive.

### Weaknesses
 - I am not fully convinced there exists the need for a benchmark fo evaluating strategic reasoning abilities of LLMs. In fact, there lacks an universal definition of the ability of strategic reasoning. In other words, what are the fundemental differences between tasks that require strategic reasoning and tasks that do not?


- If there is a clear definition of strategic reasoning, I would expect a more systematic study of existing LLMs on strategic reasoning. Why some LLMs perform better than others in terms of strategic reasoning? What are the influencing factors of LLMs? Data, Architecture, Model Size, training objectives?

### Questions
Regarding weakness 1:

- Do you have a clear definition of tasks that require strategic reasoning, as used in this paper?

- Could you explain more on how TMGBENCH addresses gaps in existing benchmarks for evaluating LLM reasoning capabilities?

- What are the fundemental differences between tasks that require strategic reasoning and tasks that do not, perhaps with concrete examples?

Regarding weakness 2:

- Could you conduct an analysis of how different LLM characteristics (e.g., model size, architecture, training data, or objectives) correlate with performance on TMGBENCH? and why.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors create TMGBench, a game theory based benchmark for testing the strategic reasoning abilities of LLMs. They create a large number of games based on the "Robinson-Goforth topology of 2x2 matrix games" as well as utilizing synthetic data generation to build on top of said games for further game development. The games are then combined in a variety of ways, creating a complex structure for the LLMs to reason in. The authors then evaluate a selection of LLMs on the benchmark and report their results.

### Strengths
- Models are tested rigorously; 2,880 times for a single model in the single game tests, the complex games have a baseline of being tested 20 times, and there's testing for positional bias with the reFoToM / reSoToM prompts.
- Extensibility: this is a great way of creating a difficult-to-overfit-to benchmark, using the synthetic data generated stories as additional "games" to play.
- The metrics used (ID, BD, PAR) are comprehensive for evaluating a model's performance and good insight to how the models perform in these situations.
- The tables and figures nicely present the findings of the experiments and are mostly given good descriptions.

### Weaknesses
 - The paper can be hard to follow at times. It would be nice to have examples of the complex games to solidify the reader's understanding. The description given for sequential games doesn't quite make sense to me, even with two introductions. And because of that, I'm not sure how well it upholds the task of "testing for strategic reasoning".
- I'm not convinced that parallel forms are actually a test of strategic reasoning either, this seems closer to measuring the model's "working memory" and being able to keep track of the different situations at a given time step. But, this may be based on a misunderstanding of what the form is describing; it's not clear to me based on the descriptions given.
- The prompt given for `Example of classic game: classic/111` gives me pause for the rest of the prompt generation. "Player A and Player B are playing a game. Either of them has two choices, namely A1, A2/B1, B2." Is this telling the model that the choices are {A1, A2} or {B1, B2}? I assume this, but that could lead to the model being confused about the task rather than being honestly judged on the difficulty of the task.

- a number of simple proofreading errors:
	- "sequential form, where LLMs are required to response multiple game tasks in a row" --> "to respond to multiple games"
	- "As explained in Section 2.2, our benchmark are perfectly suitable" --> your benchmark what?
	- "as for practical result provide by LLMs," --> results provided by
	- "which we expect robuster LLMs" --> "more robust LLMs", I'm not sure if "robuster" is a word, but if it is it's not commonly used.
		- "using CoT prompting, which is robuster"
	- "We perform 4 independent tests on each data point, covering both the classic setting and the story-based setting. Basically, we conduct 2,880 tests to generally evaluate a certain model"
		- this is weird, "Basically, we conduct 2,880 tests..." these should be combined to make flow better.
	- "We setup the test by divided it into several types" --> "by dividing it"

### Questions
- interesting that llama70B did worse on DA than 8B, why do you think this is?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a benchmark TMGBENCH. TMGBENCH incorporates 144 game types based on the Robinson-Goforth topology of 2×2 games and provides three forms (sequential, parallel, and nested) to construct more complex games using those 144 game types. Several LLMs were compared on the benchmark using several quantified metrics to identify their strengths and weaknesses.

### Strengths
- The paper is very well-written.
- Objectives are clear, and how those objectives are achieved by this work is well demonstrated.
- Quantified metrics and visualisations have been used to compare LLMs on different tasks to assess their capabilities. 
- Extensive experiments were conducted to exam the failure cases and the effect of ToM. 
- Limitations were also discussed.
- Generation pipeline was demonstrated in Appendix.
Overall, the reviewer quite enjoyed reading this paper.

### Weaknesses
No particular weakness was identified by the reviewer. The reviewer is not an expert in game theory or reasoning. It is quite likely that the reviewer is unfamiliar with some pieces of related work or crucial part of this work.

### Questions
It is stated that “Theoretically, using these atomic games, we can expand the framework to generate infinitely many increasingly complex game forms.” However, standard answers are required to compute the inconsistency map. The reviewer wonders how to obtain the standard answers to newly generated games?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a benchmark for strategic reasoning comprised of all 2x2 game ordinal payoff arrangements. Additional evaluation capabilities include testing agents when reasoning on compositions of these games (in parallel, sequentially, or where one game influence the choices in a subsequent game) and reframing the games in story-based scenarios. Evaluations study open and closed source LLMs on this benchmark, assessing: how well they produce optimal choices, the extent to which they exhibit asymmetrically biased responses when payoff matrices are flipped, and using theory of mind to improve performance. The results demonstrate that existing LLMs do not saturate the benchmark, have varying degrees of bias based on the payoff structure and story framing, and struggle to leverage theory of mind to improve results.

### Strengths
# originality
Modest.

Evaluating LLMs in strategic reasoning games is a thoroughly investigated topic (as attested by the related work). Examining anti-symmetric reasoning patterns is a question I have not seen probed before and important to consider for this setting in general.

# quality
Modest.

Experiments demonstrate the benchmark can find differences among LLMs. Models fail to saturate the success criteria, particularly for more stringent requirements like perfect answering or demonstrating theory of mind. Biases based on the generated stories show there is clear room for improving LLM context sensitivity, however it is not clear how much this could be mitigated by different prompts for the strategic reasoning (a dimension not explored in the paper).

# clarity
Modest.

The introduction was vague and hard to follow without reading the rest of the paper. Experiments are documented well. Some figures were hard to parse or could use a different presentation (notes below).

# significance
Modest.

There are numerous evaluations for strategic reasoning in game theoretic games. This focuses on 2x2 games, omitting multi-agent agents or repeated/multi-turn games (excepting the composite games tested). The paper will be of some interest to the community focusing on this subset of LLM capabilities.

### Weaknesses
Note: These weaknesses are phrased as questions to facilitate discussion.

# originality
How do the games in this benchmark cover those not covered in the "game theory" subsection of the cited paper "A Survey of Strategic Reasoning with Large Language Models"? Or for the "Societal Behavior" examples that include theory of mind?


# quality

The experiments should include statistical tests when claiming differences among model types. At least in the cases where multiple runs were possible or multiple scenarios are being aggregated (for example, in Table 1 and Figure 5). Many claims seem plausible, but the tests are there to provide rigor.

The paper would benefit from evaluating the concern stated in the introduction that there is scenario leakage of common game forms. Was there evidence of scenario leakage based on the games in Robinson-Goforth topology results? Do the games most likely to be leaked (like Prisoner's Dilemma) demonstrate substantial performance differences relative to other games?


# clarity 

The introduction could be clearer on details later explained in the paper. Examples: 
- "performance variability marked by coefficients" - Coefficients of what?
- "marked by an asymmetric pattern" - What asymmetric pattern?

Figure 6 is hard to read. It might be better plotted by showing the differences in scores between the classic and story-based settings instead.

# significance

What are the key insights we learn from TGMBench that were not revealed in prior benchmarks? This is not very clearly articulated in the paper and would help establish it's originality and significance. As TGMBench is a benchmark, the value it provides derives in exposing LLM capabilities that are not already apparent in alternatives.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
2
