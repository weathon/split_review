# PARSE-Ego4D: Personal Action Recommendation Suggestions for Ego-Centric Videos

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Intelligent assistance involves not only understanding but also action. Existing ego-centric video datasets contain rich annotations of the videos, but not of actions that an intelligent assistant could perform in the moment. To address this gap, we release \textbf{\ours{}}, a new set of personal action recommendation annotations for the Ego4D dataset. We take a multi-stage approach to generating and evaluating these annotations. 
First, we used a prompt-engineered large language model (LLM) to generate context-aware action suggestions and identified over 18,000 action suggestions. While these synthetic action suggestions are valuable, the inherent limitations of LLMs necessitate human evaluation. To ensure high-quality and user-centered recommendations, we conducted a large-scale human annotation study that provides grounding in human preferences for all of \ours{}. 
We analyze the inter-rater agreement and evaluate subjective preferences of participants.
Based on our synthetic dataset and complete human annotations, we propose several new tasks for action suggestions based on ego-centric videos. 
We encourage novel solutions that improve latency and energy requirements. 
The annotations in \ours{} will support researchers and developers who are working on building action recommendation systems for augmented and virtual reality systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper augments Ego4D for action suggestion annotations, termed as Parse-Ego4D. The action suggestion classes include categories like search, assistant search, assistant local, language, directions, assistant guide and others. With this new proposed dataset, the paper also introduces two tasks: action recommendation systems for (1) explicit user query to action suggestion, and (2) implicit user query to action suggestions.

### Strengths
The motivations behind creating this augmented dataset is based on guessing future usecases in AR/VR systems. They introduce two tasks with this augmented dataset created atop ego4d.  The paper includes performance and efficiency metrics. 
The subjective user study is valuable.

### Weaknesses
The action suggestion labels have been created solely based on narrations. Any limitations in the narrations do not have opportunity in recovering.

The authors already mentioned that temporal groundings are missing. And, without temporal information either for an atomic action or a sequence of actions intuitively action suggestion for real-world captured videos can not be fully utilized.

### Questions
The authors already mentioned that temporal groundings are missing. And, without temporal information either for an atomic action or a sequence of actions intuitively action suggestion for real-world captured videos can not be fully utilized. Would the authors have any insights for how that can be done?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors release pseudo-labels of action recommendations over the Ego4D dataset. They perform the generation of pseudo-labels using a multimodal LLM, and filter the results using human annotators. They perform analysis over the quality of the dataset with intra-human variance and introduce two tasks that make use of this dataset, with baselines of several SOTA models.

### Strengths
1) The work is well motivated for many areas in Human-Robot Interaction, Augmented Reality and Virtual Reality. Systems that can anticipate actions of the actor and act preemptively are very valuable. The paper also outlines many exciting future possibilities of extending this work.
2) LLMs can generate problematic pseudo-labels, but the authors have made sure to introduce strong screening measures, along with some helpful quantitative analysis.
3) The action space of the recommendations is extensive and covers use-cases of many interesting applications.

### Weaknesses
1) I feel the paper is missing qualitative results over the outputs of the LLM (pre and post-human analysis), along with a broader characterization of the dataset. Though to the authors credit, the quantitative analysis is extensive.
2) The lack of video input to any of the baselines results in the trained models missing a lot of contextual information (e.g. head cues) needed to decide when/what recommendations are useful. While it is reasonable video is not ingested by the model producing the pseudo ground truth (video is observed by the human annotators instead), the baselines would be much more powerful if they had access to video.
3) The user study is highly subjective and largely prone to speculative error - of course, the best option would be to ask the actor the survey questions, but that would require a collection of a new dataset.

### Questions
1) I would encourage not just the dataset to be released, but also the LLM code for generating the dataset to be released. Many aspects of this dataset can easily be improved by future authors.
2) I wonder if the authors of Ego4D would consider releasing a highly processed, anonymized descriptors of what the humans are searching when they use their cell phones. This would heavily inform when and what action recommendations are useful.
3) The actions in Ego4D seem to skew heavily towards low-level physical actions. But the actions most helpful to an action recommendation dataset would be cognitive in nature (e.g. plan, wait, search, etc). These actions are represented in the Ego4D dataset, but very very few of the annotations of these actions exist - is it easy for you to see if the LLM does better at producing recommendations for these instances?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new dataset, PARSE-Ego4D, that contains action recommendation annotations for a potential AR assistive agent. The proposed dataset is based on Ego4D, and the annotations were first collected by prompting Gemini Pro and then filtered by human raters based on sensibility, correctness, implicitness, etc. In addition to the dataset, the paper proposes two tasks for query to action prediction.

### Strengths
- I like the paper's research direction of studying personal action recommendations of AR assistive agents. It is new and interesting. If the dataset is released, it may attract new research in assistive AR, leveraging computer vision and LLMs. I also appreciate the author's effort in curating a large dataset and filtering the LLMs-generated results with human raters. The dataset creation is not trivial work, and the authors have put thoughts into the dataset creation, including annotating based on different metrics, e.g., sensibility, correctness, etc.

### Weaknesses
 - First, the paper uses the NeurIPS 2024 Track on Datasets and Benchmark manuscript template instead of the ICLR 2025 template. Such carelessness raises concerns about whether the paper has incorporated review suggestions from NeurIPS or not. 

- Regardless of the previous point, a significant portion of the paper's content describes the creation of the dataset while leaving little space to describe the benchmark tasks, how these benchmark tasks differ from existing research, and whether they are significant enough to attract future researches to use these benchmark tasks. While the paper might be a reasonable consideration for a dataset track submission, it is too thin for a main conference paper in venues like ICLR. 

- The paper should seriously consider improving presentation clarity. For example, I have to read Section 4.2 multiple times, trying to understand what the authors mean by the "implicit" query-to-action task. It wasn't very clear. I also needed to refer back to Figure 1 and try to map that to the inline equation f: c \to (q, a). This is just one place. Again, the paper is too focused to describe the dataset.

### Questions
A few confused places when I read the paper: 

1. Taks 1 is to predict 6 action classes, but there are 7 action categories defined in Section 3.2. Did you omit "others?"
2. Can you elaborate on why NLL is a good metric for Task 2? 
3. How did you choose these baseline methods for benchmarking? Why are there missing entries marked n/a? 
4. 80% of the dataset was rated by just 1 human rater. Is this going to be a limitation?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new dataset called PARSE-Ego4D, which builds on top of the existing Ego4D dataset by collecting personal action recommendation annotations. The authors adopt a two-stage annotation process: they generate context-aware action suggestions using a prompt-engineered LLM in the first stage and evaluate the automated suggestions through human study in the second stage. The authors also propose two tasks for action suggestions based on PARSE-Ego4D: explicit query-to-action and implicit query-to-action. The explicit query-to-action task predicts an action suggestion given the query. On the other hand, the model needs to predict the action suggestion without an explicit user query for the implicit query-to-action task.

### Strengths
- The new set of annotations introduced in the proposed dataset does look practical and timely, considering that it is specifically designed to empower proactive AI assistants. It can be used to develop intelligent systems that provide personalized action suggestions.
- The proposed benchmark, which consists of two tasks, also looks interesting and well-defined. Especially, the implicit query-to-action task is open-ended, leaving the vision community with much room for improvement.
- The paper reads well and is easy to follow. It looks well-organized, with the required figures and tables placed throughout.
- It also discusses the limitations of the proposed dataset and benchmarks in many aspects.

### Weaknesses
 - [W1] 80% of the dataset, which is held for training and validation splits, has only been annotated by a single human rater. This can cause instability in the training process of AI assistant models because the annotations collected by a single annotator might be too noisy. I believe that at least three answers should be collected and averaged (or decided by a majority vote).
- [W2] The action suggestion annotations are highly imbalanced, which can also contribute to instability in the training/validation process. For example, the two types of “instructions” and “assistants” account for over 80% of the annotations. On the other hand, “language” and “other” types account for only 0.02%. I believe breaking down “instructions” and “assistants” types into multiple subdivisions solves this imbalance problem, which might be more practical for dataset users.
- [W3] The explicit query-to-action task is merely a simple classification problem with only 6 classes. Even the simple baselines already achieve 87% accuracy. I highly believe that the authors should subdivide the action suggestions, especially for “instructions” and “assistants” types.
- [W4] The number of verified and high-quality suggestions (defined by the authors in line 220) is 7770, which seems too small and only accounts for 42.43% of the annotations. I believe that the authors should collect more high-quality annotations.
- [W5] I do not believe that the negative log-likelihood (NLL) is the best metric for the implicit query-to-action task. There are other metrics besides BLEU (e.g., ROUGE, WUP, METEOR), and I believe that the authors should propose a new accuracy metric based on these existing ones.
- [W6] The dataset does not consider continual interactions between humans and AI assistants, although the actual users will show continual aspects.

### Questions
- Why not filter out the annotations by the average scores of “sensible” and “correct”? For example, {sensible, correct}>=3 accounts for 65.0%, and I believe the dataset should only contain this 65.0% of the annotations. Annotations with lower scores than 3 (or even 4) might not needed for AI assistant development. The presented results of downstream experiments are also based on the subset of {sensible, correct}>=4, right?

### Soundness
2

### Presentation
3

### Contribution
2
