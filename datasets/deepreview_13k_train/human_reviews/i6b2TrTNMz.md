# A Third-Person Appraisal Agent: Learning to Reason About Emotions in Conversational Contexts

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
Emotion reasoning is crucial for achieving human-like emotional understanding in Emotion Recognition in Conversation (ERC). Current ERC datasets provide only emotion-labeled utterances, lacking the rich annotations necessary for emotion reasoning. Although Large Language Models (LLMs) show promise in generating rich emotional knowledge, they still struggle to apply this knowledge effectively for emotion reasoning. To address these challenges, we propose a learning framework based on cognitive appraisal theory, utilizing an agent powered by LLMs to learn emotion reasoning from a third-person perspective, which we refer to as the third-person appraisal agent. This learning framework comprises two phases: self-evaluation and meta-evaluation. In the self-evaluation phase, the agent generates appraisals essential for inferring emotions, incorporating counterfactual thinking to refine its appraisals. The meta-evaluation phase uses reflective actor-critic reinforcement learning to train the agent to generate accurate appraisals during testing. The training samples are appraisals generated during the self-evaluation phase, which eliminates the need for human annotations. By fine-tuning a specialized LLM in this framework, our approach significantly outperforms LLM baselines across ERC tasks, demonstrating improved reasoning and generalization across various dialogue datasets. Additionally, we provide interpretable results that clarify the model’s reasoning process behind its predictions. To the best of our knowledge, this research is the first to apply cognition-based methods to enhance LLMs' emotional reasoning capabilities, marking a significant advancement toward achieving human-like emotional understanding in artificial intelligence.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an approach to improve emotion recognition capabilities in large language models based on cognitive appraisal theory. The authors develop a well crafted appraisal generation prompt, enabling the model to generate plausible appraisals. Through self-evaluation and meta-evaluation phases, the model is refined to accurately reason about emotions contextually within conversations.
The proposed method results in a model good at generating accurate third-person appraisals, ultimately leading to improved emotion recognition performance.

### Strengths
The paper presents a solution for a very relevant problem in dialogue. Whilst LLMs have proven to be very good at many dialogue tasks, they often fail to capture the intricacies in emotion recognition.

The proposed methodology not only improves the emotion recognition ability of the LLM, but ultimately improves the interpretability of the prediction process, which could be very useful when using such emotion recognition models in downstream applications.

### Weaknesses
The paper presents a method, which could potentially be interesting to a wider audience and applicable to a wider range of reasoning problems. However, the approach is only tested on a single problem, emotion recognition within dialogue. The paper would be more impactful if it addressed at least one other reasoning task.

The RL approaches in the paper are not novel approaches, but rather the design of the methodology and the prompts designed for appraisal. Hence, it would be beneficial to test this methodology on a wider range of tasks.

### Questions
How could this approach be generalised to other tasks? Currently, the prompt is designed for this specific task, and it is not clear how one could easily generate a prompt for other tasks (without prompt engineering and testing).

### Soundness
3

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
3

### Summary
This paper proposes a method to build an emotion evaluation and reasoning dataset for conversations using reflection, along with an offline fine-tuning strategy for emotion evaluation agents based on reinforcement learning. The work introduces the reflexion method from LLMs, where one LLM evaluates emotions while another LLM reflects from a counterfactual perspective - thinking about "Is my judgment correct? Why? How should I judge if the context changes?" and guides the first LLM to update its evaluation according to the reasoning. This approach enables automatic collection of reliable emotion evaluation data in conversational contexts without human annotation. Using this automatically labeled data, the paper presents an offline RL-based fine-tuning strategy. Experiments on IEMOCAP and DailyDialog datasets show improved accuracy and F1 scores in emotion evaluation.

### Strengths
1. The proposed automatic data labeling method and offline RL fine-tuning approach show better results in understanding speakers' motivations, attitudes, and goals. This demonstrates the effectiveness of the proposed method.
2. The paper is the first to introduces reflection mechanisms into emotion evaluation, emphasizing self-reflection during the evaluation process. Ablation studies prove the importance of this design choice.
3. As an application-oriented work, the paper demonstrates well-designed experiments, promising results, and clear engineering value.

### Weaknesses
1. The paper over-packages its innovations. The core work is simply: a) applying reflection mechanism to emotion evaluation, b) using reflection to automatically collect high-quality data without human annotation and c) fine-tuning a new evaluation LLM using offline RL with this data. The "Appraisal Generator LLM" and "Appraisal Evaluator LLM" are just LLMs used for reflection, which are essentially the same thing doing self-reflection. The "THIRD-PERSON APPRAISAL AGENT" is just the fine-tuned evaluation LLM. Despite Figure 2's complex appearance, there's no real interaction, feedback loop, or collaborative decision-making between modules. Figure 2 is just a one-way pipeline: M_X—>(M_G<—>M_E)—>M_A.

Here are the suggested revisions for better presenting the paper's contributions:

1) It is suggested to reorganize the Introduction section to clearly state the three core contributions: a) Application of reflection mechanisms to emotion evaluation. b) An automatic data collection method using reflection without human annotation. c) Implementation of an offline RL-based fine-tuning approach with the collected data. Remove excessive theoretical packaging in the Introduction section and focus on engineering improvements and concrete methodological contributions. 

2) Simplify the pipeline of the whole approach (Figure 2). The actual data flow is a straightforward pipeline of M_X—>(M_G<—>M_E)—>M_A. It is suggested to remove unnecessary complexity and show the actual data flow more clearly. Try to highlight the practical workflow in each module and between modules.

2. The innovation is limited. While the paper claims to use cognitive science theories and shows fancy formulas and pseudo-code, there's no novel system design, and it uses classic RL methods. The interesting findings are mainly in data collection (using reflection for automatic annotation) and engineering optimization. At its core, it's a solid engineering paper with good practical improvements. But "new method" and "good implementation" are different things. The paper should describe its contributions more honestly and consider submitting to conferences or journals focusing on applied innovations.

Here are the suggested revisions for better presenting the paper's contributions:

1) I suggest you elaborate on the unique value of reflection mechanisms in emotion evaluation. For example, combining specific examples where emotional evaluation is not satisfactory, try to discuss why emotional evaluation performs badly (because of the lack of reflection). Then, emphasize the necessity of introducing reflection in emotional evaluation and reasoning.

2) The "PHASE 1: SELF-EVALUATION" actually is the method for automatically collecting data. It is suggested to reorganize the Sections 2.2 and 2.3.1. If focusing on automatic data collection using reflection, please provide detailed analysis of quality assurance mechanisms in automatic data collection and provide statistic comparison of the cost or quality of collected data with human annotations. The focus should be on the consistency and reliability

3) Based on the offline-RL method in this paper, try to emphasize the difficulty of finetuning the LLM by directly SFT, such as not suitable to handle complex emotional transitions, or anything else. You should explan the reason for choosing RL / offline-RL instead of general training strategy. 

4) This work chooses to fine-tune one LLM rather than continue with two frozen LLMS for reflection, obviously hoping for a shorter time consumption. This is a very specific and meaningful choice in the actual scenario. I suggest you highlight your advantage in reasoning efficiency, such as great time savings and no loss of accuracy. Different training methods (such as SFT) have different effects on the accuracy.

3. The paper uses too many mathematical symbols to express simple logical relationships. For example, the basic "try-feedback-improve" process is written in an unnecessarily complex way. While trying to appear more "academic", this actually makes the core ideas harder to understand. Consider using expressions that balance academic rigor with clarity.

Specifically, Algorithm 1 and equiations in Section 2.3.1 should be simplified. I suggest you to draw an figure to represent this feedback loop process. The data collection section mainly provides "how to collect high-quality data", there is no need to worry about how the figure will shorten the length of the content. The novel insight that can be provided is in the data collection process.

### Questions
1. Inaccurate or Inconsistent Statements.

    1). For accuracy, suggest changing "To the best of our knowledge, we are the first to integrate counterfactual thinking into a verbal RL-based strategy"  in  line 77-78 to "To the best of our knowledge, this is one of the first works to integrate counterfactual thinking into a verbal RL-based strategy for emotion reasoning tasks". This avoids implying no RL methods have used counterfactual reasoning before, while highlighting the innovation in emotion reasoning and verbal RL.

    2). Regarding contributions, there's an inconsistency between two "first" claims: line 111-112 “To the best of our knowledge, this is the first attempt to apply cognition-based methods to enhance the emotion reasoning capabilities of LLMs in the context of ERC.” and line 77-78 “To the best of our knowledge, we are the first to integrate counterfactual thinking into a verbal RL-based strategy.” Are you referring to the same or different things in these statements?

    3). Sections 2.2 and 2.3.1 are overcomplicated. The simple self-reflection concepts are presented in an unnecessarily complex way.

    4). Line 113-115 “We design an appraisal knowledge prompt, grounded in the principles of cognitive appraisal theory, to generate appraisal knowledge. This approach enables the agent to teach itself how  to reason, thereby addressing existing challenges in ERC” discusses the appraisal knowledge prompt. This shouldn't be listed as a contribution in the Introduction section. It's better presented as part of implementing other innovations. Moreover, since the prompt details are only mentioned in the appendix, it's unsuitable to treat it as an innovation.

2. Too brief and overly general related work. 

    1). The section didn’t clarify why adding reflection to emotion reasoning tasks is necessary.  When mentioning research "remains limited” in line 139, what specific limitations exist?

    2). I suggest you to reorganize the content of related work. Specific areas of related work that should be expanded upon and emphase three topics: a) self-reflection/feedback in Emotion Evaluation: previous non-LLM or LLM emotion evaluation method from the pespective of introducing reflection. b) self-reflection in other aspects (such as LLM agent). c) [optional] cognition in LLM agent. If you still want to associate with cognitive theory, you should introduce what work on LLM agent has been further improved by applying reflective / feedback-related cognitive science theories. 

    No matter two or three topics, you should explain why directly tranfer the self-reflection in other aspects into emotion evaluation is not enough. What the special issue in the filed of emotion evaluation when using the self-reflection in LLM agents? 

3. Writing Clarity Suggestions

    1). To better demonstrate the effectiveness of your proposed methods, it is suggested to reorganize Table 1 into three parts comparing: Mistral (original vs. fine-tuned), Gemma (original vs. fine-tuned) and LLAMA (original vs. causal prompt vs. fine-tuned).

    2). A small mistake: "cause" should be "causal"

    3). The causal prompt details are missing in both the paper and the appendix.  It is suggested to add this setting to the appendix.

4. [Optional] Suggestions to Enhance Innovation

    1). If you plan to release the 600 training examples, this could count as an innovation in data collection. However, the paper doesn't mention building a dataset or any plans to make it public.

    2). What does the dataset collected during the “self-evaluation phase” look like? The paper jumps directly to model inference results from the “meta-evaluation phase” without showing the dataset characteristics.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a new framework to perform the task of ERC. They take inspiration from the cognitive appraisal theory and present a two step process for ERC -- In the first step, the authors generate appraisals using an LLM and improve these generated appraisals using verbal RL. In the next step, the trajectory of improvement along with dialogue context is passed on to a trainable LLM to learn emotions. The proposed method shows better results than the models authors compared their system with.

### Strengths
- The authors propose an interesting approach to the task of ERC. Emotion reasoning makes sense to mimic human emotion formation.
- The language of the paper is easy to follow.

### Weaknesses
 - One major flaw is in how the authors generate the initial appraisals. The authors provide the true emotion labels in the prompt to generate the appraisals thus swaying the LLM in favor of generating the appraisals for that emotion. However, as mentioned in the cognitive appraisal theory, emotions *arise* from appraisals, which means that appraisals come before emotions, which is not the case for how the prompt is constructed. This then violates what the authors claim in Section 2.3 that "This LLM simulates human cognitive appraisal when reasoning about emotional states."
- It is unclear what is "appraisal knowledge xi" in section 2.3.1 or "appraisal context xi" in Algorithm 1.
- From Table 2, it is evident that the "AppraisalKnowledge Prompt" is the main contributor to the model performance. I feel like it might be due to the fact that that prompt contains the true emotion label, which in turn makes the appraisal knowledge contain that emotion label (as is the case in Figure 1. The appraisal contains "frustrated" and "angry" which are the emotion labels).
- The paper seems rushed with multiple typos and silly mistakes. For example:
   - Figure 3: "reply" --> "replay"
   - Table 6: "Table 1"? "three datasets" --> "two datasets"

### Questions
- It would be interesting to talk about the multi party nature of most of the real world conversations. And how can this multi-party phenomenon affects the proposed method.
- Speaker information in the instruction part would also be an interesting thing to see.
- Are the LLMs mentioned in Table 1 also finetuned?

### Soundness
2

### Presentation
2

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
In the area of Emotion Recognition in Conversation (ERC), this paper proposed a learning framework based on cognitive appraisal theory, utilizing an agent powered by LLMs to learn emotion reasoning from a third-person perspective. Experimental results on two benchmark datasets of ERC, IEMOCAP and Dailydialog, validate that the proposed method outperforms some LLM baselines.

### Strengths
1. This paper describes the motivation, the proposed methodology, and the experimental in details, which is easy to follow.
2. Motivation for emotional reasoning from a third-person perspective is interesting and promising.
3. Experimental results show that the proposed third-person appraisal agent outperforms Mistral-7B-Instruct-v0.3, Gemma1.1-7B-Instruct, and LLAMA-3.1-8B-Instruct on the IEMOCAP test set. 
4. A large number of ablation experiments were conducted to verify the effectiveness of appraisal knowledge generation, self-evaluation phase, meta-evaluation phase. In addition, experiments were conducted on DailyDialog to demonstrate generalization.

### Weaknesses
1. The representations of Fig. 1, Fig.2, and Fig.5 should be optimized. For example, the font size of the emotion labels in Figure 1, as well as the alignment of the text boxes; the module sizes and framework alignment in Figure 2; and the alignment of the text boxes in Figure 5, among others.
2. Improve the accuracy of emotion recognition by employing large language models to emotional reasoning is promising, but the experimental results did not highlight the advantages of large language models for emotional reasoning and comprehension. Previous ERC work [1] [2] [3] [4] have significantly higher emotion recognition accuracy than the proposed third-person appraisal agent, even without emotional reasoning.
3. The experiments in this paper are conducted only on a subset of the IEMOCAP and DailyDialog datasets. Such a small amount of data is insufficient to demonstrate the effectiveness of the proposed method. More datasets should be considered as experimental benchmarks, e.g., MELD [5], M3ED [6], EmoryNLP [7], etc.
4. While ERC in the textual modality is certainly relevant, generalization to multimodal scenarios (visual, audio, and textual) is even more relevant and interesting [1] [2] [4].

### Questions
1. Why set the fixed window length to 5, reflective cycle to 2? Is there a priori knowledge or is it based on empirical settings?
2. How fast is agent's emotional reasoning and emotion recognition? Is it comparable to previous ERC models?

### Soundness
2

### Presentation
2

### Contribution
2
