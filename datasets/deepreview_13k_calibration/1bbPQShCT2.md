# I-PHYRE: Interactive Physical Reasoning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Current evaluation protocols predominantly assess physical reasoning in \textit{stationary} scenes, creating a gap in evaluating agents' abilities to \textit{interact} with dynamic events. While contemporary methods allow agents to modify initial scene configurations and observe consequences, they lack the capability to interact with events in real time. To address this, we introduce \ac{benchmark}, a framework that challenges agents to simultaneously exhibit intuitive physical reasoning, multi-step planning, and in-situ intervention. Here, \textit{intuitive physical reasoning} refers to a quick, approximate understanding of physics to address complex problems; \textit{multi-step} denotes the need for extensive planning sequences in \ac{benchmark}, considering each intervention can significantly alter subsequent choices; and \textit{in-situ} implies the necessity for timely object manipulation within a scene, where minor timing deviations can result in task failure. We formulate four game splits to scrutinize agents' learning and generalization of essential principles of interactive physical reasoning, fostering learning through interaction with representative scenarios. Our exploration involves three planning strategies and examines several supervised and reinforcement agents' zero-shot generalization proficiency on \ac{benchmark}. The outcomes highlight a notable gap between existing learning algorithms and human performance, emphasizing the imperative for more research in equipping agents with interactive physical reasoning capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces I-PHYRE, a benchmark for intuitive physical reasoning capabilities in decision-making agents. It consists of four different block-removal games and benchmarks three planning strategies against them, implemented with both supervised and reinforcement learning. I-PHYRE's design centers on three principles: physical reasoning, multi-step planning, and in-situ intervention. 

The four games are "basic" (teaching basic principles of physics), "noisy" (minor perturbations), "compositional" (combining various structures to require multi-step reasoning), and "multi-ball" (multiple dynamic events occurring concurrently, motivating carefully timed in-situ intervention). The planning strategies are "planning-in-advance" (generating an entire plan with timings based only on the initial state), "planning-on-the-fly" (generating the next action at each timestep given the observation - standard RL-type setup), and "combined" (generating the entire plan, then updating it after executing the first action). 

Experiments include results from model-free deep RL agents as well as some other baselines in supplementary on the games. Everything is compared to a human baseline. The paper specifically discusses how agents perform when generalizing (without further training) from the basic split to other splits, as well as how the three training strategies differ.

Finally, the paper gives analysis of sources of difficulty in I-PHYRE, performance by offline algorithms, and limitations/future work.

### Strengths
#### Quality
- Overall, a solid paper. Intuitively, if an agent did well on I-PHYRE, I would believe that it had robust intuitive physics capabilities in certain domains, which is what a benchmark should convince me of.
- Appendix G is very valuable. It does rest on the assumption that all failures are either of bad order or bad timing, which eliminates more basic failures, but since it is a simple simulator, and since Appendix G clearly shows that all the failures in Basic are timing-based (i.e. all the failed plans have correct order), I am convinced that the Basic split teaches nontrivial principles and the other splits 

#### Clarity
- Very well-written! Clear language
- The text organization is really useful, especially in the results section. The subsections make sense and each paragraph follows a claim-warrant structure. In terms of readability, papers often fall apart in the results section; this one does not. 

#### Originality
I-PHYRE seems to have an original design. However, it's not the first interactive intuitive physics benchmark. The paper should compare to [1] and [2], though I do think it serves different, valuable purposes.

#### Significance
The tasks in I-PHYRE are distinct from other related work and test compelling aspects of intuitive physics reasoning. So, I think if the paper can prove its claims, it is significant. 

[1] Physion: Evaluating Physical Prediction from Vision in Humans and Machines. Bear, D. M. et al. arxiv preprint: arXiv:2106.08261. 2021. 
[2] Jain, A. et al. "Generalization to new actions in reinforcement learning." ICML 2020.

### Weaknesses
#### Quality
- The paper says that RL agents perform well on the noisy split, sort of justified by the fact that their noisy results "correlate" with their basic results. But that doesn't follow - the noisy results are clearly of lower magnitude even if they follow the same trends (across what factor of variation?), and we aren't given a correlation statistic to warrant this claim. The same applies to "correlation diminishes in the compositional and multi-ball splits... inherent complexities of these tasks impact performance negatively." The correlation claim is similarly 1) nonobvious from looking at Fig 2, even if it does sort of look true, 2) not backed up by a number, 3) not clear why it matters - even if the performance on these two were correlated with perf on basic across whatever factor of variation, but lower in magnitude, I would accept that they are harder (and I of course do, just from looking at Fig 2). Then making a claim that this difficulty is due to the "inherent complexities of these tasks" is, while not unbelievable, strong. I'm not doubtful, just not convinced. 
- The discussion has a section titled "why do current RL agents fail on I-PHYRE?", which in my opinion is the most important aspect of a benchmark paper other than conceptual design and grounding in the environment. The paper claims three benefits: physics modeling being hard, multi-step interventions, and action timing - i.e. asserting that its design principles have effectively resulted in challenges for agents. However, this is all prose and little analysis of actual results - it would help to spell out for the reader which quantitative result comparison should lead to each conclusion. (Appendix G does a good job of this).

#### Clarity
- Figure 1 (repeated from a previous review I did of this paper, as the figure hasn't changed):
  - Colors are hard to follow, maybe better to annotate split on box
  - Since the boxes are much larger than the arrows, sort of look like two columns, and generally don't look like flowchart elements, it's confusing that the top-left box isn't the best one to start reading with. Bigger arrows and/or numbering would help.
  - "Wrong order leads to no overlap elimination timing for two balls" - I don't understand this
  - Compositional solution isn't that clear - annotation of key occurrences in each step might help
- "Combined" planning strategy needs better explanation (a step-by-step could help) - it sounds like the whole plan is generated based on the initial state, then the first action is executed, then the plan is updated, and that's it. But I'm not totally sure if the entire plan is updated, if it's ever updated again later after subsequent actions, etc.
- Figure 2 needs to be more organized and readable (in the previous version it was also hard to follow, but still more organized)
  - Strategies should be put into separate subplots (with the same axes) or otherwise cued, especially since there are different numbers of each, making it hard to eyeball
  - Baselines (especially the human comparison point) can be horizontal lines crossing the figure
  - Not every algorithm gets every planning strategy, which doesn't seem to *only* be a function of the nature of the algorithm - so it's confusing to take all of this in just in the form of bars and text
- Fig 3 would benefit from organization as well - e.g. group strategies by color and differentiate within them by line texture.

#### Originality
- The paper claims the three planning strategies as a contribution, but they aren't original - they are baselines just like the offline methods tested on I-PHYRE. I agree that the *results* are a contribution, but I would fold that into the third contribution bullet, or at least make it clear that the "devised" planning strategies themselves shouldn't be considered original.

Nits: 
- Different parts of the paper use different naming conventions for agents - e.g. "SAC-I" in one place, "SAC Inadvance" in another. Better to use the same thing throughout.

### Questions
- In a previous version of the paper, failure on I-PHYRE was ascribed to sparse action requirements and delayed reward. Now, those concepts are being pitched as being inherent to multi-step reasoning (delayed reward) and action timing (sparse action requirements), but it's not true that failing for those reasons means that if the agents were better at handling them, they would robustly learn to handle multi-step reasoning problems and in-situ intervention problems. Could you flesh this argument out more? 
- What exactly is the nature of the "combined" strategy, and could you say more on why it's effective?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes I-PHYRE, an interactive physical reasoning benchmark. While previous physical reasoning benchmarks mainly focus on reasoning happening in stationary scenes, I-PHYRE tests physical reasoning in an interactive format. This demands the agent to quickly understand the underlying physics, plan over multi-steps, and perform timely manipulation within a scene. The authors formulated I-PHYRE into four game splits to measure the agents' capability to learn and generalize about essential principles of physics, and
conducted extensive evaluations of existing learning algorithms and human performance. They showed a significant gap between human and learning algorithms, and also analyzed what are the main factors of current learning methods fails.

### Strengths
1. Clear motivation and novel design achieving the motivation.
     - The authors clearly stated I-PHYRE’s contribution compared to other existing benchmarks. 
     - The proposed task of block elimination is well designed for the stated purpose, highlighting interactivity of physical reasoning. 
     - Additionally, dividing the tasks into 4 types for testing different types of generalization is well designed.
2. Thorough experiments and analysis
     - The experiments are very thorough, including multiple reinforcement learning baselines, multiple planning strategies, learning from offline data, integration with large language model(LLM), human evaluation, etc.
     - The authors also tried to analyze what makes learning algorithms difficult to generalize, and came up with three plausible factors.      
     - Additionally, the authors also quantitatively analyzed how significant action timing influences the performance of the algorithms.

### Weaknesses
1. The visualization of Figure 1. is slightly hard to understand at first glance. Although the authors explain the figure more thoroughly in page 3, it would be better to either separate the figure into several images or add another image that describes the task more briefly. Specifically, the depiction of the different game splits and their relationship to the overall task could be made clearer with a dedicated visual representation for each split.

2. Although the experiment was thorough, it can be that 40 games is a small number of games to anticipate strong generalization. It would be better if the authors have tested learning methods in a larger scale. For instance, the authors can try more diverse configuration given the same basic physics to model in the scene. Specifically, varying the initial positions and velocities of objects within each template could provide a more robust test of generalization. Furthermore, increasing the number of templates, while keeping the core physical principles constant, could offer a more comprehensive evaluation of the agents' ability to learn and apply these principles across diverse scenarios.

3. The cited work [1] also contains interactivity in the benchmark, although it mainly tackles generalization to new actions as the authors mentioned. However, the degree and nature of interactivity in [1] could be further elaborated upon to clearly distinguish it from the interactivity emphasized in I-PHYRE.

### Questions
1. I wonder why the authors simply concatenated the predicted states with the current states when performing model based reinforcement learning. A more dominant approach to use would be 
     1. Along with the dynamics model, also train a reward model that predicts the reward given a state.
     2. Given a reward model and a dynamics model, perform planning (e.g. CEM planning)

2. There are also other recent model based RL methods the authors can try, such as [1]. 



[1] Temporal Difference Learning for Model Predictive Control, International Conference on Machine Learning, 2023, Hansen et al.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a series of intricate tasks centered on physical reasoning and interaction. Additionally, it suggests three distinct approaches for task resolution using supervised or reinforcement learning methods. To conclude, an extensive user study is executed to gauge human proficiency across various learning techniques.

### Strengths
The study introduces a valuable benchmark for assessing model predictions concerning physical outcomes. The benchmark's interactive nature facilitates real-time planning, crucial for real-time physics interactions, particularly when timing plays a key role in the dynamics. Furthermore, it supports multi-step interventions, promoting long-term predictions over brief, single-step action forecasts.

### Weaknesses
1. Please add a table grid to Figure 2 for clearer comparisons.
2. The author notes the absence of 3D interactive environments as a limitation. However, this is a significant point to address since many high-performing models should ideally transfer seamlessly to robotics. A 3D interactive environment would greatly facilitate this transition. Notably, papers like ComPhy feature 3D environments, as referenced in Table 1 by the author.
3. I appreciate the author's use of this paper as a benchmark for various RL approaches, highlighting the need for more research in this domain to address physical reasoning tasks. What potential solutions or recommendations does the author suggest for this benchmark?

### Questions
Mentioned in weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the problem of interactive physical reasoning with focus on intuitive physical reasoning (approximate capability to predict physical outcome), multi-step planning (execution of multi-step actions to complete the task), in-situ interventions (necessity for timely object manipulation to succeed). To study this problem authors propose a block elimination task where the task is to ensure all red balls fall into the hole by removing minimum number of blocks. The benchmark consists of 40 unique games segmented into 4 splits: Basic split for training and noisy, compositional and multi-ball splits for testing generalization of physical understanding of agents. Authors also propose 3 different planning strategies: planning in advance, planning on the fly, and combined strategy to solve I-PHYRE using both supervised and reinforcement learned agents. In addition, authors also benchmark human performance on the task and compare it with current learning algorithms.

### Strengths
1. Proposed problem statement is interesting and relevant to advance physical understanding ability of learned agents. The proposed block elimination task captures the multi-step planning and necessity for timely actions which are novel aspects of the benchmark
2. The experimental setup demonstrates performance of 3 strong baselines using different learning paradigms i.e. reinforcement and supervised learning. It also demonstrates effectively that proposed baselines significantly underperform and there’s a lot of room for improvement
3. The paper benchmarks and establishes a human baseline for interactive physical reasoning
4. The paper is well written and easy to follow

### Weaknesses
1. It is unclear if the learned agents can generalize to unseen games from the basic split. The benchmark tests generalization to noise, compositionality and multi-ball setup but doesn’t present results on unseen games with properties similar to basic split. It would be good if the authors can add a unseen basic split and present performance of trained agents on unseen basic split. The Noisy split seems like a substitute of basic split but as it is using same games from basic split + some noise I am worried it is not a good representative of generalize to unseen games with similar properties
2. The training dataset of 20 games for basic split seems too small a dataset to lead to any meaningful generalization to complex splits on which generalization is being tested. Can authors describe why they chose a small dataset for training? Is it possible to procedurally scale the training data? If not, why?
3. Results presented in fig. 2 and 3 only show comparison of different methods on average reward on evaluation split it doesn’t highlight what is the success rate of these baselines on full task. It would be nice to have a comparison on achieved success on the full task to get a better sense of the results.
4. Poor performance on compositional and multi-ball splits for RL trained baselines look as expected with MLP policies and no large scale RL training. Can authors elaborate more on whether the I-PHYRE benchmark expects emergence of compositional generalization to such complex splits by training on just the basic split games? If yes, have authors tried using recurrent policies? Eventhough limited but recurrent networks have demonstrated some form of compositional generalization [1] in limited machine translation tasks which require “mix-and-match” strategies to solve the task (which is true for I-PHYRE compositional split)
5. The proposed task operates in a simple 2D environment which is less realistic setup

### Questions
1. How is the combined strategy baseline implemented and what is the action space of this baseline? From the text in main paper it seems like this baseline predicts continuous values at the start of the episode and keeps updating the full vector after each timestep. Is this correct? 
2. Why are the combined strategy baseline trained only for < 100k step in Fig. 3 experiments? 
3. Have authors tried using a on-the-fly version of GPT-4 baseline presented in the appendix? How well does that perform? By on-the-fly version, I mean querying GPT-4 after each timestep to output the next action instead of using just the initial scene

The primary concern I have is around the small size of training dataset and the challenges around scaling it. I'd appreciate if authors can discuss issues and concerns around that question. I am open to updating my rating if authors answer my questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
