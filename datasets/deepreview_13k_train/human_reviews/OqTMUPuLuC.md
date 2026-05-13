# DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models

- Decision: Accept
- Scores: 5, 8, 6, 6

## Abstract
\lipsum[1]

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel framework for autonomous driving systems based on LLM and tailored components. Contributions of this paper are several folds:

- Knowledge-Driven Paradigm: The paper introduces a knowledge-driven paradigm for autonomous driving, differentiating it from existing data-driven approaches. This paradigm is inspired by human driving, which relies more on knowledge and understanding rather than mere data accumulation.

- DiLu Framework: The authors propose the DiLu framework, integrating large language models (LLMs) with autonomous driving systems. Several modules are proposed based on recent advances of AI agent: A Reasoning Module that utilizes LLMs for decision-making based on common-sense knowledge; A Reflection Module that assesses decisions and updates them based on safety and correctness, using the knowledge from LLMs.

- Experimentation and Results: Extensive experiments demonstrate the framework's capability to make proper decisions, its strong generalization ability, and the potential for real-world application. The paper compares DiLu with reinforcement learning methods, showing its superior performance in generalization and adaptability.

### Strengths
- Innovative Approach: The integration of LLMs into autonomous driving systems represents a significant shift from traditional data-driven methods, potentially offering more adaptable and human-like decision-making.

- Generalization Ability: DiLu shows a strong ability to generalize from one environment to another, a crucial aspect for real-world applicability.

- Continuous Learning: The framework's ability to continuously evolve and improve through its memory and reflection modules is a key strength.

### Weaknesses
 - Complexity and Scalability: The integration of LLMs and the need for continuous updating and reflection may introduce complexity, potentially impacting the scalability of the system. The proposed memory module, while intended to mitigate this, may still face challenges in terms of efficient retrieval and storage as the amount of driving experience grows. The computational overhead of querying the LLM for each decision, even with few-shot learning, could also become a bottleneck in real-time applications.

- Real-World Application: While the framework shows promise, the transition from controlled experiments to real-world application can be challenging, given the unpredictable nature of real-world environments. The paper does not address the robustness of the system to noisy sensor data, unexpected events, or variations in road conditions. The reliance on a text-based representation of driving experiences may also limit the system's ability to capture the nuances of real-world driving scenarios.

- Dependence on LLMs: The framework's reliance on LLMs means that its performance is heavily dependent on the capabilities and limitations of these models. The paper does not discuss the potential for biases in the LLM's knowledge base to influence driving decisions, nor does it address the challenges of ensuring the reliability and consistency of LLM outputs. The lack of fine-tuning of the LLM also raises concerns about its ability to adapt to specific driving styles or regional traffic patterns.

- Evaluation thoroughness: The authors only evaluate the proposed methods with oversimplified metrics (collisions) and compared to a simple baseline (RL). The limitation of the evaluation poses a question mark on how such system actually performs in the real driving scenarios, compared to sota autonomous driving systems. The evaluation should include more comprehensive metrics, such as time to completion, lane keeping accuracy, and smoothness of driving, and should compare against more advanced baselines.

### Questions
While LLM-based agent systems have shown success in various embodied systems, the adaptation of it in the AV tasks is still unclear to the reviewer. AI agent system has shown prominent success in task planning for open world robotic tasks, but AV has a different setting (with different challenges). The motivation and advantages of using AI agent system for AV needs to be elaborate more.
On the other hand, the authors didn't evaluate the proposed framework thoroughly enough (with only simple metrics and simple baselines). This further raises questions of the reviewer regarding how promising or what are the key advantages of using AI agent system in AV setting.
Finally, the proposed AI agent follows a typical setup compared to the other existing works in robotics tasks. The authors should highlight more on the unique challenges and design choices tailored for the AV task.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a novel and interesting approach leveraging LLMs in autonomous driving to perform knowledge-based reasoning about making high level driving decisions. The approach is motivated by how humans learn to drive. There are three straightforward pieces of the method: reasoning, recall, and reflection. The method is evaluated in simulating driving scenarios and positively compared against a SOTA RL method and ablations of the approach.

### Strengths
The proposed method is well-motivated by human behavior and generally clearly explained. The experiments justify each portion of the method for achieving the goal task of autonomous driving.  The method is novel, simple, and has potential to be used in the real world. Overall, an interesting perspective on the self-driving car problem.

### Weaknesses
The memory module requires more description in Section 3.2. The process of storing experiences is somewhat unclear. The writing could be interpreted to mean that every scenario is stored separately or that the similarity between the keys is used to map similar experiences to the same memory store (which seems to be what the authors are actually doing). Either a new figure or updates to the existing figures would also add to clarity and precision.

This paper never discusses limitations. I strongly recommend making room to discuss the relationship between this approach and approaches which focus on safety. In fact, the “reflection” module is being presented as a safety mechanism. However, the trustworthiness of the results from the LLM is never discussed. Diving into reliability and limitations is important in a method which claims to address safety for transparency in a safety critical task where results are currently deployed in the real world. Specifically, the paper should address the potential for the LLM to generate incorrect or unsafe driving actions, and how the system would detect and mitigate such errors. The current reflection module seems insufficient to guarantee safety, as it relies on the LLM's self-assessment, which may not always be accurate. A more robust safety mechanism, perhaps involving external validation or a rule-based system, should be considered.

I thought the following claim in the abstract was slightly misleading given LINGO-1 (which the authors do cite). “To the best of our knowledge, we are the first to instill knowledge-driven capability into autonomous driving systems from the perspective of how humans drive.” I think that the correct way to phrase what the authors mean is specifically saying that they are the first to “use human-like knowledge-based reasoning to make autonomous driving decisions” or something similar since leveraging it in decision making is the distinction with prior work. “Instill” is a vague term which could also describe what LINGO-1 is doing.

### Questions
It is fairly odd in the experiments that two different GPT versions are used. Why did the authors not just use GPT-4?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a framework for utilizing the few shot and self-correction capabilities of LLMs for the task of AV planning, where the following abilities of the framework are highlighted:
- Store successful experiences in memory and leverage them to improve future rollouts through similarity retrieval and usage in few-shot prompting.
- Ability to learn from unsuccessful experiences (ones with collisions) by applying LLM self-correction and storing the modified experience among the successful experiences in the memory

The above components, dubbed as reasoning and reflection modules respectively, are integrated along with memory in a closed loop setting without any back-propagation objective. 

A number of prompting techniques including chain-of-thought and few-shot prompting are used to get better reasoning. The environment used for experiments (Highway-Env) only requires four discrete decisions, hence the LLM is prompted to select one amongst these four decisions for each frame after going through CoT reasoning.

The experiments are used to demonstrate the following key claims:
- The memory module combined with few-shot prompting provides much better results than using no memory module (zero-shot) or using lesser shots. 
- The more the number of experiences in the memory, the better.
- The ability to generalize is better with more few-shot experiences fed into the LLM
- Adding successful and corrected experiences both help in improving performance
- Better generalization capability compared to RL method GRAD.

### Strengths
- The motivating idea of human knowledge distillation for AV planning is sound, interesting, and under-explored.

- The overall framework formulation towards leveraging LLMs via appropriate prompting, retrieval, and self-correction is interesting and well set up. It would have been exciting to see formulations for LLMs assisting planning stacks (instead of directly doing discrete action decision making) - which could be much more valuable to existing systems.  

- The flywheel effect created from storing both successful and unsuccessful + corrected experiences in memory is an important contribution.

- The paper provides a good foundation for other exciting work to build upon, especially with the promise to open source upon acceptance.

- The experiments are fairly extensive towards investigating all the different components of the proposed framework.

### Weaknesses
 -  One of the main proposed advantages is better generalization through instilling human knowledge-driven capabilities instead of a data-driven only approach. However, the experimental settings derived from HighwayEnv are too restrictive to help extrapolate how such LLM based reasoning would perform on diverse new scenes using retrieval + few shot prompting. While it is perfectly fine to work with restricted settings and smaller datasets for new research work, the bridge to answer the most interesting questions is too long.

- As mentioned in strengths section, providing directions and initial experiments on assisting planning stacks (instead of directly doing discrete action decision making) could provide a lot of value.

- The experiment settings used to demonstrate generalization are not too convincing. The number of lanes and traffic density is changed, but this is still an extremely similar environment where the retrieved few-shot scenarios could be nearly directly applicable.

- Under the above setting, it is possible that with a large enough memory module the task reduces to simply copying the answer from one of the retrieved experiences. It would be good to see a baseline where the decision from one of the retrieved experiences is used as is (voting with mixture of experts or winner takes all)

- The metric movement with CitySim in Figure 7b and Table 1 correction row do not seem significant to make the corresponding claims?

- Nit: The key frame sampling for successful experiences seems like an important detail that has not been explained.

- Minor nit: The claim for this being the first work addressing AV planning via leveraging LLMs might need to be revised with recent papers like GPT driver (depending on chronology).

### Questions
- What kind of diverse interactions do we get from the Highway-env simulator? Would it be possible to evaluate the framework under more interactive / challenging conditions, especially wrt agent interactions? It would be interesting to see the generalization to intersections, interactions with peds, aggressive agents etc.

- The correction experiences intuitively should provide a strong boost to performance since they are akin to hard example mining and injecting reasoning about the negative outcomes. However the corresponding results in Table 1 do not show strong improvements. Is it possible understudied and warrants more extensive experimentations?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper includes a LLM into a framework which controls the decisions of a driving agent in a simulator. The authors define a concept, they call knowledge-based driving, and argue how their framework implements this and performs better than data-based methods. They test against one reinforcement learning based baseline in the Highway-env simulator.

### Strengths
The idea to use an LLM for scenario understanding and decision making in driving is very interesting. The authors have proposed a decent suggestion for integration and practically showed that it works.

The figures help getting a good top-level overview of the modules. Some parts are missing like how does the correction module work which is only an arrow in Figure 5?

### Weaknesses
The language could be clearer, less vague and heavily simplified to make the arguments easier to understand. 

The evaluation against a single self-trained RL baseline makes it hard to estimate the performance. Since it seems there is no limit to the perception of the own agent, another fair comparison would be a simpler approach where a statistical or rule-based approach would have all information of all cars and drive. Without having a state-of-the-art RL method that is already optimized on highway-env it is hard to see if the performance gain comes from the proposed method or from the failure to adopt the RL method on the task.

Conceptually it is hard to imagine right now how this is supposed to drive in real time. Is the video sped up or slowed down? It is a challenge of the last decade how to get convolutional networks fast enough to be usable in a car. The computation challenges are not discussed at all. What is the reaction time of this and is execution speed a bottleneck?

The claims are too broad and don't even fit as motivation. If data driven vision methods are bad, how do you get your current frame to work on? It's as if you argue, your LLM is better than observing the road, it doesn't make sense if they need to work together in the end.

The better choice to get a motivation would be the domain of scene understanding on a higher level, e.g. knowledge-graphs, planning, behavior prediction etc. Theoretically even Imitation Learning, specifically Behavioral Cloning could be a better field to compare. The LLM is reacting but is doing so because it should be able to react to close cars but understand the whole scenario. This understanding of a scenario is a hard problem and would be a much better motivator to contrast this work against.

Claims that the knowledge-based system is how a human drives can not be supported by the current state of research and not by the citations in this paper. I think the paper would benefit from not making the claim that they imitate a system in humans but limit themselves to saying, they designed a framework to include an LLM in a continuous learning setting where it outperforms certain other approaches.

Please add enough details from Johnson et al. 2019 to understand the vector similarity on an idea level. Make the paper more self-complete.

What is the data the LLM is trained on? If the training data contains driving situations from several countries, how to make sure it is following the appropriate traffic rules?

What are the 5 human crafted experiences and why are they needed?

Figure 7 a) could be easily replaced by a table to save space.

It is a bit unsatisfactory to have only a comparison against one baseline which was re-trained on this particular data. Is there no standard scenario on Highway-Env or another RL-based approach that was already applied to Highway-env to compare against? I could not find one myself so I don't see this as a downside in my rating but I think it would make the paper stronger if the authors could find a way to compare against more than one baseline.

### Questions
- What are the more precise concepts of knowledge-driven human driving that inspire this?
- Instill knowledge-driven capabilities sounds very vague. Methods that acquire experiences from real-world dataset covers all learning-based methods depending on what you mean with acquire. The abstract could be more concrete, it's hard to take away anything apart from that a LLM seems to do decision making while following a continuous learning scheme. 

The language is hard to follow and the citations do not seem to support the claims well. In the Introduction, the sentence "This phenomenon inevitably leads to the marginal performance of data-driven methods." is one example for a broad claim without enough support in citations. There are autonomous cars driving in cities today with vision algorithms which are data-driven. They do not show marginal performance. The citations for this claim are one work describing a methodology to categorize corner cases in three common sensor modalities, so not very related, and the second citation "Chen et al. 2022" seems to be a catch all "survey of surveys" which is a large list of autonomous driving surveys with some added, partially trivial, thoughts. 

Other examples where statements are too broad and hard to understand are: "Furthermore, this task is particularly formidable and expensive for autonomous driving systems due to the complex challenge of iterating diverse and unpredictable driving scenarios." What is this sentence supposed to say? The authors should heavily simplify their language to deliver their points clearer. Formidable and expensive can be understood in many different ways and distracts from the core argument the authors want to make.

Claims that the knowledge-based system is how a human drives can not be supported by the current state of research and not by the citations in this paper. I think the paper would benefit from not making the claim that they imitate a system in humans but limit themselves to saying, they designed a framework to include an LLM in a continuous learning setting where it outperforms certain other approaches. 

Please add enough details from Johnson et al. 2019 to understand the vector similarity on an idea level. Make the paper more self-complete.

What is the data the LLM is trained on? If the training data contains driving situations from several countries, how to make sure it is following the appropriate traffic rules?

What are the 5 human crafted experiences and why are they needed?

Figure 7 a) could be easily replaced by a table to save space. 

It is a bit unsatisfactory to have only a comparison against one baseline which was re-trained on this particular data. Is there no standard scenario on Highway-Env or another RL-based approach that was already applied to Highway-env to compare against? I could not find one myself so I don't see this as a downside in my rating but I think it would make the paper stronger if the authors could find a way to compare against more than one baseline.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
