# EmpathyRobot: A Dataset and Benchmark for Empathetic Task Planning of Robotic Agent

- Decision: Reject
- Scores: 5, 3, 8, 8

## Abstract
Empathy is a fundamental instinct and essential need for humans, as they both demonstrate empathetic actions toward others and receive empathetic support. As robots become increasingly integrated into daily life, it is essential to explore whether they can provide human-like empathetic support. Although existing emotion agents have explored how to understand humans' empathetic needs, they lack to further enable robots to generate empathy-oriented task planning, neglecting the evaluation of empathetic behaviors. To address this gap, we introduce \textbf{EmpathyRobot}, the first dataset specifically designed to benchmark and enhance the empathetic actions of agents across diverse scenarios. This dataset contains 10,000 samples based on human feedback, encompassing information from various modalities and corresponding empathetic task planning sequences, including navigation and manipulation. Agents are required to perform actions based on their understanding of both the visual scene and human emotions. To systematically evaluate the performance of existing agents on the EmpathyRobot dataset, we conduct comprehensive experiments to test the most capable models. Our findings reveal that generating accurate empathetic actions remains a significant challenge. Meanwhile, we finetune an \ac{llm} on our benchmark, demonstrating that it can effectively be used to enhance the empathetic behavior of robot agents. By establishing a standard benchmark for evaluating empathetic actions, we aim to drive advancements in the study and pursue of empathetic behaviors in robot agents. We will release our code and dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
1) Empathy robot is a large dataset with 10,000 samples for agent actions with the focus on empathetic actions with a three step process: scenario understanding, outcome decision, and action execution. 
2) The paper introduces empathy specific metrics motivated by prior works. 
3) The paper fine-tunes LLMs on their benchmark. Authors show that their fine-tuned Llama3-8B outperforms strong baselines such as GPT-4o.

### Strengths
1) Strong motivation for an empathy-driven dataset 
2) Useful empathy specific metrics motivated by prior works

### Weaknesses
1) Distinction between emphatic planning vs scenario understanding: the authors claim that scenario understanding is dependent on ‘the person’s underlying emotions’ and empathetic planning includes formulating a high-level plan of what to do after comprehending the scenario. For example, after noticing the person hasn’t eaten anything because of being too upset, the model may come up with a plan like 'Find the person some of his favorite food, then comfort him.’ What is the purpose of the scenario understanding module vs the empathetic planning module when both are conditioned on the person’s emotions? Is it a way of carrying out chain-of-thought? Or are there distinct purposes of the two modules as I don’t quite understand why they can't be combined. Both module seems reasonable but it is difficult to see the importance of each module without ablations e.g., removing the empathic planning module when evaluating empathetic actions. 

2) The paper claims that the benchmark helps *evaluate and enhance empathetic actions for robot agents* (Figure 1). I would like to see the usefulness of this on robotics tasks. 

3)  In figure 6, what are the prompts for GPT4o? It is difficult to believe that prompt engineering GPT4o would yield to poor empathetic responses.

### Questions
1) Is the character pool from a ground-truth annotated dataset or is this generated as well? 

2) What are labels here?
*Empathy Response Generation Second, we generate empathetic action sequences for each scenario and create labels for them.* (3.2)

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a new benchmark called EmpathyRobot to evaluate the "empathetic" actions of agents when interacting with humans in various simulated environments. The authors assess the performance of various rule-based agents on performance on this benchmark.

### Strengths
1. The paper proposes a nice benchmark to capture an under-studied element of virtual agents, empathy. The authors derive a clear benchmark with various tasks in VirtualHome to illustrate how one might measure such an ability.

### Weaknesses
1. The paper proposes a much more elaborate scenario in the introduction than what is ultimately actually studied in the benchmark: we are only constrained to a specific set of empathy measures and moreover, there is no robotics task or continuous state space in sight (despite the name of the benchmark being EmpathyRobot). The limited discrete rule-based agents tested are a far cry from real deployment scenarios for these types of systems in the real world.

2. There have now been a large body of benchmark-agents-style tasks that, stemming from the Puig et al. VirtualHome environment papers, offer tiny incremental advances on one another. I feel that every other conference, I review a similar paper: "We want to study this [very detailed social/behavioral] element of robots, and so we derive a benchmark from VirtualHome called [x] then evaluate [xyz] agents on it". I do not think these incremental pieces of benchmark work are deserving to be continuously published at high-caliber ML conferences.

### Questions
1. How is EmpathyRobot any different from the previous (very long line) of similar social behavior/coordination agents papers? What is the key contribution of novelty that, as a community, we can actually derive from incremental work such as this? 

2. How does a highly constrained discrete state and action space actually tell us anything meaningful about robots or robotic behaviors in the real world? Real tasks involving continuous control are a far cry from what the authors write of here, and it would be helpful to have a clear sense of what contribution or task the paper is actually studying.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
EmpathyRobot is the first dataset for evaluating and enhancing the empathetic actions of robot agents, embedded in the virtual environment and empowered by LLMs.

EmpathyRobot takes realistic social interactions as examples and combines Embodied AI, social events, dialogues, and actions together, making it a comprehensive dataset for the studies on human empathy process.

Besides, EmpathyRobot proposes a systematic evaluation framework with four levels of empathetic difficulty settings, performing comprehensive evaluations on the sota models.

### Strengths
The dataset is specifically designed to evaluate and benchmark the empathetic actions of robot agents.

The evaluation is comprehensive, EmpathyRobot designs different levels of "empathy" and conducts comprehensive evaluations on the many models. 

The agent design is flexible and can be embedded in a variety of virtual environments. 

The methodology of dataset generation makes a lot of sense, giving researchers the opportunity to generate diverse scenarios in different social interactions.

### Weaknesses
There is little information about releasing the dataset and how the dataset will be maintained. 

What is the practical applications of the dataset. Is there any integration conducted into e.g. character.ai to illustrate the effectiveness of the dataset?

### Questions
See weaknesses

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents EmpathyRobot, a dataset and benchmark designed to enable robotic agents to exhibit empathetic behaviors by understanding human emotions and planning contextually appropriate actions. It introduces 10,000 multimodal samples and an evaluation framework, aiming to address gaps in existing benchmarks that focus on task completion without assessing empathy. Through experiments with large language models, the authors demonstrate that empathy-driven task planning remains a challenging area for current AI. However, the assumption of “ground truths” for empathy scenarios could be limiting, as empathy may vary significantly based on individual perceptions, making some “correct” responses subjective.

### Strengths
- Originality: EmpathyRobot is pioneering in creating a benchmark for empathetic robotic behavior.
- Quality: The dataset is meticulously designed, with a comprehensive evaluation framework.
- Clarity: Clear writing and illustrative examples.
- Significance: This work supports crucial advancements in empathetic AI research, relevant to social intelligence in robotics.

### Weaknesses
 - The framework’s reliance on “ground truths” for empathy might overlook the subjective nature of empathy, where responses could vary by cultural or personal perspectives.
- Large models face challenges with inference speed; discussions on optimizing these for practical use could strengthen the paper.

### Questions
Overall, this paper makes valuable contributions to advancing socially intelligent AI. My question, however, is whether defining two “ground truth” actions per scenario is a reliable measure for performance, given the subjective nature of empathy.

### Soundness
3

### Presentation
4

### Contribution
3
