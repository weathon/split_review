## Human Reviewer 1

### Summary
R-Horizon is motivated by existing LLM reasoning benchmarks' over-emphasis on _immediate, single-turn tasks_. It instead proposes a method to automatically generate _long-horizon, interdependent reasoning tasks_ via query composition, which enables it to curate the R-Horizon benchmark using existing (single-turn) datasets targetting math, coding, and agentic capabilities. The paper finds out that even the SOTA reasoning models suffer performance degradation as the number of composed queries (subproblems) increase. The paper then further suggests RLVR training over query-composed dataset, which demonstrates considerable improvement in both LRM's single- and multiple-problem performance. Extensive analysis and ablation studies provide important insights into the causes of performance degradation and why training with composed dataset works better.

### Strengths
- The paper is overall clearly motivated, well-written, and easy to follow.
- The lack of long-horizon, multi-stage/problem evaluation of LRMs is indeed a practical concern, and the paper's approach of using query composition to automatically combine single-turn queries within one interdependent problem is (an example of) an elegant solution.
- On top of the R-Horizon benchmark, the paper further conducts solid RLVR training on the composed dataset, which increases both single and multi-problem performance and further highlights the importance of equipping LRMs with multi-step compound reasoning skills.

### Weaknesses
- Even though the paper mentions that it constructs composed problems using both math, coding, and agentic datasets, most of the construction details and analysis are centering around the math criteria (see Q1 below). And the RL training is also solely done on math-related datasets.
- For the analysis on the RL training, it would be great to see similar "error type distribution" plot (as in Figure 5) for the model before & after the training. This helps gain further insights on _why & how the performance on multi-query problems_ increase over the training.
- While the writing is good overall, certain plots are hard to read due to ambiguous legends & captions. As an example, on Figure 8 the x-axis shows "Query 1/2/etc.", which I believe actually denotes the number of composed queries but can be misunderstood as query indices. Also certain plots have (unexplained) error bars/intervals while some do not.

### Questions
1. For the dataset construction for coding tasks, it's mentioned that _"unlike the sequential composition used for mathematical tasks, we apply a directly composed concatenation format ... without adding explicit dependencies"_. So (a) what is exactly this "directly composed concatenation format" (hard to tell simply from the given prompt in Appendix)? (b) isn't the point of R-Horizon benchmark to create interdependent, long-horizon reasoning tasks? I think the compromise made here undermines the overall validity (i.e. many of the analysis made in the paper, e.g. the "dependency reasoning error, applies to math only).
2. For the reward design, the distinction between the "last" and "all" rewards is a bit non-intuitive as I thought they should be very similar when the problems are inter-dependent. Is it even possible for a model to obtain positive "last" reward even when its "all" reward is 0 (the other direction is trivial)?
3. For **Figure 6**, how can the error positions be even larger than the output lengths (even query num is low)?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper introduces R-HORIZON, a benchmark and training framework designed to evaluate and enhance long-horizon reasoning in Large Reasoning Models (LRMs).
Existing benchmarks mainly assess single-step reasoning, where each question is independent. R-HORIZON addresses this gap by composing interdependent multi-step queries from existing datasets (e.g., MATH500, AIME24/25, LiveCodeBench, WebShaper).
The authors evaluate 25 state-of-the-art reasoning models (e.g., DeepSeek-R1, Qwen-3-235B, Gemini-2.5, Claude-Sonnet-4) and show that all suffer severe performance degradation as reasoning horizons increase.
Furthermore, they train models using R-HORIZON-based reinforcement learning (RLVR), demonstrating substantial gains on both composed and standard reasoning tasks (+17.4 on long-horizon tasks and +7.5 on AIME24).

Overall, the paper provides a new perspective on reasoning length, reflection behavior, and token budget allocation, revealing fundamental limits in current LRMs and proposing a practical solution for improvement.

### Strengths
Novel and impactful evaluation paradigm.
R-HORIZON systematically measures reasoning depth and breadth, exposing weaknesses that single-horizon benchmarks cannot reveal.

Comprehensive empirical analysis.
The evaluation across 25 strong LRMs and multiple domains (math, code, agentic tasks) convincingly demonstrates consistent long-horizon degradation patterns.

Actionable training insights.
The reinforcement learning experiments with R-HORIZON data provide a scalable and cost-effective way to enhance long-horizon reasoning, with clear empirical gains and behavioral analyses (reflection, budget allocation).

### Weaknesses
Multi-step reasoning is indeed necessary; however, in this paper, simply combining several basic math problems offers limited reflection of contextual consistency in true multi-step reasoning. Tasks such as “1 + 2 = ?” followed by “previous answer + 4 = ?” can essentially be summarized into a single query like “1 + 2 + 4 = ?”, which weakens the intended long-horizon reasoning challenge.

Moreover, maintaining contextual consistency across multi-step reasoning is highly dependent on prompt design, yet the paper does not clearly explain how prompts are constructed or formatted for solving these composed problems.

The evaluation on closed-source models is insufficient, as only o4-mini was included.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper proposes R-HORIZON, a benchmark and data construction framework for evaluating and improving long-horizon reasoning in large reasoning models (LRMs). Using Expanded Problem Composition (EPC), it links independent problems into multi-step dependency chains. Evaluating 25 LRMs across math, code, and agentic tasks, the authors find significant performance degradation as reasoning length increases. They further integrate R-HORIZON data into RL from verifiable rewards (RLVR) using Group Relative Policy Optimization (GRPO), showing that such training enhances models’ sustained reasoning ability.

### Strengths
**Strengths:**

1. The paper is well-written, clearly structured, and easy to follow.
2. It introduces meaningful long-horizon benchmarks and corresponding datasets that are valuable for advancing research on large reasoning models (LRMs).
3. The extended benchmarks effectively reveal the limitations of current LRMs in maintaining long-horizon reasoning.
4. The authors conduct reinforcement learning (RL) experiments on the constructed datasets, demonstrating notable improvements in sustained reasoning performance.
5. The paper provides comprehensive analyses and insights into the proposed data construction and evaluation methods.

### Weaknesses
**Weaknesses:**
1. While the proposed methods enable verifiable long-horizon reasoning evaluation, the constructed benchmarks appear somewhat artificial and may not fully reflect realistic reasoning scenarios.  
2. Similar efforts, such as *GSM-Infinity* [1], have explored benchmark construction for increasing reasoning complexity. The paper would benefit from a clearer discussion of how its approach differs from these prior works.

[1] GSM-Infinite: *How Do Your LLMs Behave over Infinitely Increasing Context Length and Reasoning Complexity?* (ICML 2025) https://arxiv.org/abs/2502.05252

### Questions
**Questions for the Authors:**
1. In **Figure 11**, the entropy of RL training decreases as *n* increases (e.g., *n=4* vs. *n=1*). Could the authors provide an explanation or hypothesis for why longer reasoning chains lead to lower entropy?  
2. Is it possible that the poor performance of models on **R-HORIZON** arises because they have not been exposed to similar long-horizon or compositional data during pre-training or intermediate training? Have you attempted any supervised fine-tuning (SFT) or cold-start experiments on such data?  
3. Could the improvement in original tasks after RL with R-HORIZON stem from the fact that the constructed datasets yield more balanced reward signals (i.e., less likely to produce all-correct or all-wrong rollouts), thereby improving rollout efficiency?  
4. The paper reports an increase in reasoning efficiency (shorter thinking length) after RL. Could this be because higher *n* naturally leads to longer responses, which increases the truncation ratio during RL training, thus implicitly encouraging more concise reasoning?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
5

---

## Human Reviewer 4

### Summary
The authors propose a new dataset for long-horizon reasoning and then also train a model on their dataset with Reinforcement Learning (RL). The new dataset is based on six other datasets targeting math (MATH500, AMC23, AIME24 and AIME25), code generation (LiveCodeBench) and agentic tool usage (WebShaper). Long-horizon problems are generated by combining several independent problems into a single one, where the problems have to be solved (usually) sequentially since later problems rely on the results of earlier problems, thereby transforming them into a long-horizon task. 25 language models are then evaluated on the developed dataset and their results are analyzed. In addition the author also generate a training dataset based on the Skywork-RL dataset and use it to fine-tune an existing model with custom reward functions, which then is also evaluated.

### Strengths
* with the increase in context lengths of modern language models, long-horizon reasoning is a relevant topic and the dataset seems to be good contribution
* the writing is mostly clear
* good evaluation in general and large number of RLMs tested
* good ablation study
* detailed appendix with good overview over additional results as well as the evaluation setup

### Weaknesses
* I found the motivation a bit lacking: the new dataset is somewhat artificial in its dependencies - a proper motivational example would be beneficiary in my opinion
* not a weakness per se, but I found the third chapter a bit too high-level without much details
* writing primarily in the evaluation is at times a bit imprecise or not entirely accurate:
  * 4.1:
    * AMC23 is not discussed
    * for MATH500 it seems that there is also data for 20 composed query numbers
  * 4.2, first paragraph: "R1-Qwen-7B drops from 93.6% (n = 1) to 0% (n = 16), which is 34.1% more than the 32B model" - reference is unclear (probably MATH500); Where does the 34.1% come from?
  * 5.1, Effective Reasoning Length of LRMs:
    * "gap between the actual accuracy and theoretical accuracy of models becomes increasingly larger" - not necessarily true on AIME24
    * "7B model’s error range is (4-6k tokens) while the 32B model’s error range is (8-10k tokens)" - context is missing, probably for MATH500
  * Reflection is not defined or at least explained, which also makes it unclear why it matters.
  * Sometimes "expected accuracy" and sometimes "theorectical accuracy" is used? I assume they are the same thing, so I suggest to use one term consistently.
  * Appendix D.3: "Figure 14 (b) and (c) show that all models fail to allocate thinking budget reasonably according to problem difficulty" - seems to be somewhat not true for R1-Qwen-7B

minor issues:
* introduction: no reference for CoT
* Figure 1: Theoretical Accuracy is not introduced at this point. (only on page 4)
* 2.2:
  * "Su et al. (2025); Yang et al. (2025b); Wu et al. (2025b) investigates..." - It should be "investigate", since it is a plural.
* Algorithm 1: "and Create" - lowercase create?
* 4.1: I believe, there is no whitespace before a footnote.
* 4.3, Impact of Number of Composed Queries and Different Reward Schemes: n=1 is not really a composed problem
* Figure 5: not very readable in terms of fontsize as well as chosen color for example for early stop and output truncation - I had to zoom in to 400% to find an instance for output truncation
  * similar issue for Figure 6, especially the theoretical accuracy as well as Figures 7 to 9
* Figure 6: missing whitespace before the brackets in the subfigure titles (also for Figure 9)
* sometimes it is "Math500" and sometimes it is "MATH500" in the evaluation figures
* Figure 8: x axis label might be misleading, maybe something like "2 Queries" or just "2" and so on would be better?
* Appendix F.1: "policy loss 5 with" - should probably be something like "policy loss (see Eq. 5) with"
* Appendix H: details on model, which generated the responses are missing, where the questions are coming from, etc.
* references:
  * consider the proper capitalization of the titles, at least for proper names and abbreviations to improve readability
  * place of publication of arXiv references can only surmised from the URL
  * consider adding the access date for web references
  * [Guo et al. 2025] - cited differently than the other arXiv references
  * [Luo et al. 2025a/b] - URL is not a proper link
  * [MAA 2024/2025] - consider using something like the xurl package to fix the formatting
  * [Muennighoff et al. 2025] - cited differently than the other arXiv references - maybe this could be the blueprint for the others

### Questions
* Figure 2: What are the circles with a red outline?
* 4.2, last paragraph: Why is AIME25 more challenging than AIME24?
* Figure 6: How can the error position be above the token length? Because wrong answers tend to be longer for smaller query numbers?
* How much can the six benchmarks (MATH500, AMC23, AIME24/25, LiveCodeBench and WebShaper) be considered out of distribution compared to the training dataset based on Skywork-RL?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3