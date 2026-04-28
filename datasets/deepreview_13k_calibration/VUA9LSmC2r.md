# Learning Embodied Vision-Language Programming From Instruction, Exploration, and Environmental Feedback

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5

## Abstract
The fusion of vision and language in recent vision-language models (VLMs) represents a significant advancement in multimodal comprehension and interpretation. Furthermore, when seamlessly integrated into an embodied agent, it signifies a crucial stride towards the creation of autonomous and context-aware systems capable of formulating plans and executing commands with precision. In this paper, we introduce Octopus, a novel VLM designed to proficiently decipher an agent's egocentric vision and textual task objectives and to formulate intricate action sequences and generate executable code. Our design allows the agent to adeptly handle a wide spectrum of tasks, ranging from mundane daily chores in simulators to sophisticated interactions in complex video games. Octopus is trained by leveraging GPT-4 to generate training data, i.e., action blueprints and the corresponding executable code, within our experimental environment called OctoVerse, which provides instant feedback to refine the agent’s decision making. Through a series of experiments, we illuminate Octopus's functionality and present compelling results. By open-sourcing our model architecture, simulator, and dataset, we aspire to ignite further innovation and foster collaborative applications within the broader embodied AI community.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript proposes a model and simulator for instruction-following tasks in Embodied AI, leveraging GPT-4 for a human-model-agent task-execution paradigm.

### Strengths
The manuscript makes reference to relevant methodology in EAI — designing agents that include foundation models, which perform intermediate reasoning tasks

### Weaknesses
Section 1 / Throughout — The manuscript forgets to properly motivate its contributions. What problem is this work supposed to be solving? What research questions are examined by this manuscript?

Section 1 — Most of the Introduction section is unnecessary. The space should instead be used to describe what is added on top of GPT-4 to make the model proposed in this paper a sufficiently distinct contribution. How is OctoVerse different from other EAI simulators? Why does the community need OctoVerse? What problems can be solved in OctoVerse that cannot be solved elsewhere? The manuscript fails both to motivate and explicitly describe its contributions.

Section 2 — Call it “Related Work”. The dimensions on which this section compares the proposed work with the prior art are all wrong. Firstly, because the manuscript is attempting to propose a new environment and tasks, it should identify the limitation of other, similar simulators/datasets and explicitly discuss the proposed improvements. Regarding claims for novel modeling contributions, the manuscript must first propose research questions or problems that the approach attempts to solve. Next, a set of related work can be organized to discuss their attempts at answering said research question and solving said problems, as well as discuss their limitations or weaknesses. Finally, this structure affords the manuscript to describe how its proposed work improves on the prior art, according to those research questions and identified problem(s).

Section 3 — The manuscript does not make clear what was originally provided by OmniGibson / GTA-V, versus what is added by OctoVerse. Also, again, the manuscript is missing motivation for why anyone should use its proposed environment. The problem formulation needs a lot of work.

### Questions
N/A — see above.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduced Octopus, a vision-language model mapping the visual input to the action codes. The fine-tuned dataset is collected with the GPT-4 where the simulator feedback is incorporated to generate the system feedback. The author further proposed a RLEF to improve the performance.

### Strengths
- This paper proposed a novel VLM  to transfer the visual input to the executable codes, driving the agents.
- The GPT-4 along with a simulator is used to collect training datasets. OminiGibson and OctoGTA are used respectively.
- An RLEF module is used to boost the model's performance further.

### Weaknesses
 - More related works in Section 2.1 are needed to help the reviewer identify the paper's contributions, like [1-4]. 
- The authors term the simulation they used "OctoGibson" which is built upon OmniGibson. Can the authors give more details to elaborate the main difference between them, or did they just use that Simulator to collect the dataset?
- A better format is needed. Some lines need a reformat in the revised version. One example is "3.2 Instructions From Exploration", lines above and below seem to belong to the same paragraph.
- More experiments are needed. The author only conducts the experiments on the datasets they collected and lacks a direct comparison with more relative frameworks as discussed in Section 2.1. 
- The author uses the GPT-4 to collect the training data, and one implicit assumption is that the performance of the GPT-4 is optimal or near-optimal. A comparison between the GPT-4 generated data sample and the human-collected sample would help. Or, did the author conduct some data quality control before the use of dataset?

- When using GPT-4 plus a simulator to collect the dataset, the location of the target object is directly obtained from the simulator? And this information be stored and used for later training? With this approach, the final complete robotic system still needs a separate vision model besides the ViT-L in the VLM. Can the author give some discussion on this design choice?

- RLEF. It is very interesting to see the usage and effectiveness of RLEF. However, I am curious as to why you chose CodeLLaMA-7B as the reward model while using MPT-7B for the complete VLM? 

- In Table 2, there is a comparison between Octopus and  MPT-7B. Also, the performance is not consistently superior, a further discussion is needed. And the metrics' definition is needed to help the understanding. 

- Ablation: 3B: what is the 3B model? 

- The author inputs 10 images to the VLM and discusses the standard version vs the random version.  Would other designs help?

- The author states multiple times with "open-sourcing" in the main text, a link to the anonymous website would be helpful.

- See weakness.

### Questions
- The author uses the GPT-4 to collect the training data, and one implicit assumption is that the performance of the GPT-4 is optimal or near-optimal. A comparison between the GPT-4 generated data sample and the human-collected sample would help. Or, did the author conduct some data quality control before the use of dataset?

- When using GPT-4 plus a simulator to collect the dataset, the location of the target object is directly obtained from the simulator? And this information be stored and used for later training? With this approach, the final complete robotic system still needs a separate vision model besides the ViT-L in the VLM. Can the author give some discussion on this design choice?

- RLEF. It is very interesting to see the usage and effectiveness of RLEF. However, I am curious as to why you chose CodeLLaMA-7B as the reward model while using MPT-7B for the complete VLM? 

- In Table 2, there is a comparison between Octopus and  MPT-7B. Also, the performance is not consistently superior, a further discussion is needed. And the metrics' definition is needed to help the understanding. 

- Ablation: 3B: what is the 3B model? 

- The author inputs 10 images to the VLM and discusses the standard version vs the random version.  Would other designs help?

- The author states multiple times with "open-sourcing" in the main text, a link to the anonymous website would be helpful.

- See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper leverages GPT4 to generate vision and language training data from OmniGibson and GTA-V. Then, based on the data, they train the model modified from the Otter model and perform some downstream embodied tasks to demonstrate the performance.

### Strengths
1. The idea of using GPT4 with crafted prompts to acquire training data from existing environments is interesting.

2. Error management and environment feedback are reasonable.

### Weaknesses
1. The novelty of this paper is limited. Essentially, it uses GPT4 with the prompt engineer to collect data from two embodied environments and then trains a vision-language agent model. Moreover, The agent model does not have a specific framework diagram to show the detailed parts, making it difficult to see which part of the model is its innovation point. I suggest providing a framework diagram to clearly explain where the model is newly proposed in the paper and how it differs from existing methods.

2. This paper appears to employ an intentional use of uncommon or less frequently used words in many sentences, substituting them for simpler, more common terms that could convey the message more clearly. As a result, the reading experience becomes somewhat disjointed, and the text may come across as rather weird to the reader.

3. The reason for using both OmniGibson and GTA-V environments to generate data seems not obvious. A more obvious comparison between the two environments is required, such as the visual comparison of the tasks. Furthermore, the specific task design within each environment is not clearly articulated, making it difficult to assess the diversity and complexity of the generated data.

4. In Section Error Management, when the agent executes the wrong command, how does the method perform "error management" on it? It seems that this section only claims the cases under which a task is defined as failure, and does not show how to manage such failure. The lack of clarity on how the system recovers or adapts from errors is a significant concern.

5. In Section ENVIRONMENTAL FEEDBACK, what if there are multiple erroneous states in a task sequence?  Which are the positive states and which are the error states at this time? And it may not be said that if one of the states is wrong, then its previous states must all be negative. The current description lacks the nuance to handle complex sequences with varying degrees of error.

6. The experimental baselines are unfair and unclear. For Blind LLMs, without visual input to GPT4, GPT4 cannot ground language into the visual environment, which will inevitably lead to worse results. As for TAPA, the reader cannot understand what kind of model it is and its workflow. Even the OVD are not introduced or cited. The lack of proper baselines makes it difficult to assess the true contribution of the proposed method.

7. What are the tasks of the four testing environments? The authors did not give a detailed introduction. The absence of task details hinders the reproducibility and understanding of the experimental results.

8. Some titles and analyses of the experimental sections appear to be uninformative. For example, **LLMs Does Not Depend on Observation**, is this a conclusion or a statement? If it is a statement, the authors have already said before that this baseline has no visual input, and it is also contrary to the subsequent titles which are all conclusions. In addition, in the ablation experiments, larger models and more components trained can bring more performance improvements, which is common sense in sense, but the authors put them as ablation experiments alone and do not give any insights.

### Questions
1. How to train the reward model $r_{\phi}$? More details are needed.

2. A visual example of task trees is required for better understanding.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose an embodied vision-language planner and programmer (Octopus) trained with reinforcement learning with environmental feedback, as well as two embodied environments that yield feedback necessary to train the aforementioned model, with data collected by GPT4. Octopus takes egocentric views and tasks specified in language, and outputs next actions and code to execute it. The method is tested on environments based on OmniGibson and GTA-V.

### Strengths
I appreciate the introduction of reinforcement learning from environmental feedback, by efficiently using environmental rewards from the simulator + GPT-4. Though the approach of using code-writing LLMs to execute plans is not new, I believe applying it to embodied tasks in the proposed formulation is a nice demonstration of how to leverage foundation models in these embodied environments.

### Weaknesses
W1. The data collection process relies on GPT-4, which takes as input language of systems message + environment message to output the required plan, code, and target state. This relies on the strong assumption that the systems + environment message fully captures the environment state, since the planning must be done without access to the view of the visual scene. I presume this means that the systems prompt must be elaborate, handcrafted, and task specific, such that GPT-4 can plan reasonably in the environment using possible objects at hand. Is there a robust way of designing such prompts for different/new tasks without tuning?

W2. From my understanding, GPT-4 generates the target states, and whether the target states have been met is used as environmental feedback for training Octopus. It seems possible that GTP-4 will generate an incorrect or trivial target state to satisfy the language task goal, and be able to successfully reach that predicted target state, without actually achieving the task goal. Is this understanding correct? In this case, the errors from GPT-4 seem more harmful than having unsuccessful execution from GPT-4 generated code.

W3. The results on Table 2 are not particularly convincing of this method’s success. Octopus should indeed outperform blind LLMs that do not take visual input. TAPA outperforms/is of equal performance in 2 of the 5 tasks. The paper lacks analysis on why this is the case. Where does TAPA fail? It is also hard to compare when the vision models are different; does OVD and CLIP-ViT perform similarly in terms of capturing information from the input scene?

Nit: Should add a figure describing Octopus model architecture; notations in methods section are not well defined.

### Questions
Q1. Is there a systematic way of generating the systems message able to generalize to new datasets? Or does it need to be hand-crafted and tuned for Omniverse & GTA & other datasets?

Q2. Can you provide more analysis or experiments on where Octopus may outperform prior work?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
