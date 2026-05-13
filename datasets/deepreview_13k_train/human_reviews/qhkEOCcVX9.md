# A Newborn Embodied Turing Test for Comparing Object Segmentation Across Animals and Machines

- Decision: Accept
- Scores: 3, 8, 8, 6

## Abstract
Newborn brains rapidly learn to solve challenging object recognition tasks, including segmenting objects from backgrounds and recognizing objects across novel backgrounds and viewpoints. Conversely, modern machine-learning (ML) algorithms are "data hungry," requiring more training data than brains to reach similar performance levels. How do we close this learning gap between brains and machines? Here we introduce a new benchmark—a Newborn Embodied Turing Test (NETT) for object segmentation—in which newborn animals and machines are raised in the same environments and tested with the same tasks, permitting direct comparison of their learning abilities. First, we raised newborn chicks in controlled environments containing a single object rotating on a single background, then tested their ability to recognize that object across new backgrounds and viewpoints. Second, we performed “digital twin” experiments in which we reared and tested artificial chicks in virtual environments that mimicked the rearing and testing conditions of the biological chicks. We inserted a variety of ML “brains” into the artificial chicks and measured whether those algorithms learned common object recognition behavior as biological chicks. All biological chicks solved this one-shot object segmentation task, successfully learning background-invariant object representations that generalized across new backgrounds and viewpoints. In contrast, none of the artificial chicks solved this object segmentation task, instead learning background-dependent representations that failed to generalize across new backgrounds and viewpoints. This digital twin design exposes core limitations in current ML algorithms in achieving brain-like object perception. Our NETT is publicly available for comparing ML algorithms with newborn chicks. Ultimately, we anticipate that NETT benchmarks will allow researchers to build embodied AI systems that learn as efficiently and robustly as newborn brains.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper conducts a comparison study on the one-shot object segmentation ability of real animals and machines. Specifically,  the authors create simulated ‘digital twin’ environments that mimic the rearing condition of real biological newborn chicks. In the simulated environments, the ‘artificial chick’ is trained via deep reinforcement learning to segment objects. The experimental results show that ‘artificial chick’ failed in the one-shot object segmentation task while biological chicks are able to solve it.

### Strengths
Originality and Significance:    
The reviewer found the idea of comparing machine and real animals' learning ability in a strictly controlled environment interesting. This line of study might help us learn more about the similarity and difference of animal brain and deep neural network. 
 

Quality:   
While the idea of the paper is interesting, the reviewer found some claims are not well-supported by the experiments. Please see the Weakness section for more details.


Clarity:    
The presentation is mostly clear. However, many improvements, particularly on the figures, are needed.  Please see the Weakness section for more details.

### Weaknesses
1. The technical contribution of the paper is limited. Specifically, the proposed ‘artificial chick’ is a PPO agent trained with ‘imprinting reward’, which encourages the agent to move close to an object. It is not surprising that this simple baseline with a heuristic reward fails to solve the one-shot object segmentation task. The use of a basic PPO agent with a hand-crafted reward function, without exploring more sophisticated RL techniques or intrinsic motivation, significantly limits the conclusions that can be drawn about the capabilities of artificial agents in this task. The reward function itself is quite simplistic, and does not encourage the agent to learn a generalizable representation of the object, but rather to simply move towards it, which is not a true segmentation task.

2. The reviewer found main claims in the paper are not well-supported by the experiments. Specifically, the authors claimed that ‘’... none of the algorithms learned background-invariant object representations that could generalize across novel backgrounds and viewpoints”. However, the ML algorithm the authors used in the paper are just  PPO with different architectures and a heuristic reward. The reviewer thinks those simple methods well-represent the state-of-the-art one-shot object segmentation methods. There are many works on one-shot segmentations [1, 2]. Incorporating those methods in the ‘artificial chick’ might make the experiments more convincing. The claim of background-invariance is not adequately tested, as the core algorithm is not designed to learn such invariance. The experiments should include a more diverse set of algorithms that are specifically designed for one-shot segmentation tasks, rather than relying solely on a basic RL approach.

3.  The reviewer has concerns on the significance of the paper. The main finding here is that the RL trained agent failed the one-shot segmentation task. It seems expected. Providing more insights and analysis of why it fails may make the paper more valuable. The paper lacks a detailed analysis of the failure modes of the RL agent. A more in-depth investigation into why the agent fails, such as examining the learned representations or the agent's behavior in different scenarios, would be beneficial. Without this analysis, the paper's findings are not particularly insightful.

4.  The presentation in the experimental section is unclear. Particularly, the text and numbers in figure 3, which show the only experimental result of the paper, are ineligible.

### Questions
1. According to section 2, the biological chicken data is from previous work (Wood et al. 2021). However, in the abstract, the authors claim that “we raised newborn chicks in controlled environments …”. This seems contradicting. Could you clarify?    


2.  In Introduction, it reads “However, most studies with newborn subjects have produced data with a low signal-to-noise ratio,”. The reviewer has difficulty following the content. Please give citations for ‘some studies’ and elaborate what is the ‘produced data’ here.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
## Update
 
I thank the authors for the answer. I stand by initial review and believe this paper should be accepted.

## Original

This paper aims to benchmark the intelligence of embodied AI systems against that of biological ones (animals). Towards this end, they propose a new benchmark, the Newborn Embodied Turing Test (NETT). 

In NETT, an agent is born into an environment with a display showing a singular rotating object. The agent must then learn to properly identify that object when presented with distractor objects or when it is placed on novel backgrounds. The biological agents are chicks that learn this skill via filial imprinting and the artificial agents are DRL agents that learn this via an filial-imprinting-like reward.

The authors find that while biological chicks are well suited to learn this task, their artificial counterparts are not. The authors consider a variety of DNN architectures and find that none perform significantly above chance.

### Strengths
This paper presents a convincing experiment that directly compares the capabilities of biological and artificial chicks. I really like how controlled the setup is. You can't perfectly control for all the differences between biological and artificial systems (as the authors note in their limitation section), but this paper does an admirable job at reducing this gap as much as possible.

The authors examine a variety of different DNN architectures with the aim to close the gap between biological and artificial chicks.

The discussion section is well-written and presents a balanced discussion that points out the limitation of the experiments presented and contains interesting pieces of information.

### Weaknesses
Figures in the paper are very low resolution (and possibly heavily compressed with lossy compression). This is particularly noticeable for figure 3, which is nearly illegible.

The number of trials used for training artificial chicks seems rather small at 1000. Similarly, the episode length of 1000 seems long given how small the environment is. Why were these numbers chosen? Are they similar to the number of times the biological chicks turn towards their object and how long they stay facing it?

There has been work in deep reinforcement learning algorithms that may be applicable here. One example is as DAAC and IDAAC ("Decoupling Value and Policy for Generalization in Reinforcement Learning", Raileanu and Fergus).

### Questions
### Questions

1. Did the authors perform the biological chick experiments themselves or are those directly from Woods & Woods 2021? (I was unable to get access to this paper to check myself.) If the authors performed this experiment, has it been checked by an Institutional Review Board (IRB) or similar?

### Suggestions for Improvement

This paper reminded me of "Exploring Exploration: Comparing Children with RL Agents in Unified Environments" by Kosoy et al. These two works perform different experiments and have different goals, but the authors may want to mention this work.

Some "high-water" marks for artificial chicks would be useful. If one was trained on the test set, how would it do? Ideally it should perfectly solve the task. If one was trained with a singular object but many different backgrounds, how would it do?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors aimed to put both state-of-art vision models and biological vision on similar levels of data diet. They do this by rearing newborn chicks in a very controlled visual environment where they have access to limited visual experience. By exploiting the imprinting ability of chicks, their ability to segment foreground from background is studied. Then vision models are trained with exact same data by instantiating them as the vision modules in a RL agent rewarded to go towards the imprinting object. Finally both the models and chicks are probed for their ability to segment new objects and/or new backgrounds and it was found that the models fare much worse compared to the newborn chicks. This indicates that the state-of-art models lack something that newborn chicks' visual system has.

### Strengths
Rarely do I see works with this novelty, quality and significance. 

* Studying deep learning models in a setting where the data diet is controlled is timely and needed. 
* The data collected from newborn chicks is compelling and novel. 
* The results showing that current models lack the necessary mechanisms can be very impactful. 
* The data collection procedure and analysis opens up a ton of possibilities for future work. 
* The paper is overall well written.

### Weaknesses
 * Perhaps the biggest weakness is that the vision models here are trained in a way that is not very indicative of the state-of-the-art. Most vision models that is used in the community are usually a combination of self-supervised training and supervision with a lot of exemplars. While this might diminish how relevant this work is for the community, it does not take away from the significance of the work since the goal of the work is to study models when they get only as much visual experience as newborn chicks (i.e newborn chicks are not getting a ton of supervision). 
* PPO agents are trained for a lot of episodes (original PPO paper (Schulman, 2017) did 1M episodes) usually while this work only does 1000 episodes. This is probably okay since this setting is much simpler. But I would still train one model for much more steps to rule out strange behaviors (like grokking (Power, 2022))
* The paper might benefit from an expanded section on the differences between birds and mammal brains, especially since the audience is likely to be more from the computational side. While I do appreciate the effort in section 1.1, it might be helpful to expand it a bit more.

### Questions
* Why does Figure 1 make it seem like this is a cyclic process? I don't see why it is put on a circle - step 1 does not follow step 6?
* I wish this was called something other than a Turing test. I think most people (as far as I know) think of the imitation game when they hear Turing test while this is very different. I feel like this is significantly different enough to warrant a different. I almost feel like calling this Turing test is underselling it. Would another name that highlights the "limited exposure to environment" aspect of this work be better suited? Turing test says nothing about how much experience the models get to have?
* Section 2.1 : Was the second display blank (all black) or just a background?
* Section 2.2 : Do the RL agents need to be called "artificial chicks"? I think calling them "RL agents" or something is less confusing. 



Improvement to the paper -
* All the figures need major revamp. The text is barely readable and they need to be of higher resolution. Figure 2 needs to say what "F" and "N" stand for. Figure 2 could also be made such that the backgrounds and foregrounds are easily distinguishable.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces a benchmark, the Newborn Embodied Turing Test (NETT), and reveals the limitations of current machine learning algorithms compared to newborn brains in object segmentation tasks. However, the experimental results of this work are insufficient to validate the claimed fairness of the NETT.

### Strengths
1.	This work's main contribution is the introduction of the Newborn Embodied Turing Test (NETT) benchmark, which enables a direct comparison of the learning abilities between newborn animals and machines in object segmentation tasks.

### Weaknesses
1.	The evaluation of this proposed NETT benchmark is not comprehensive enough. Many variables were not taken into consideration during the data collection process for the biological chicks, such as their binocular vision compared to the single camera of artificial intelligence chicks. Meanwhile, biological chicks might roam around while artificial intelligence chicks do not. These unaccounted variables raise doubts about the effectiveness of the proposed benchmark. The validity of the benchmark may be compromised due to the discrepancies in sensory capabilities and behavior between biological and artificial chicks. Further refinement and consideration of these variables are necessary to ensure the reliability and validity of the benchmark.
2.	The presentation of this work still needs improvement, as the figures are not in vector format. For example, Figure 3 lacks clear labels for the x and y axes, making it difficult to understand the meaning of the figure.

### Questions
1.	The evaluation of this proposed NETT benchmark is not comprehensive enough. Many variables were not taken into consideration during the data collection process for the biological chicks, such as their binocular vision compared to the single camera of artificial intelligence chicks. Meanwhile, biological chicks might roam around while artificial intelligence chicks do not. These unaccounted variables raise doubts about the effectiveness of the proposed benchmark. The validity of the benchmark may be compromised due to the discrepancies in sensory capabilities and behavior between biological and artificial chicks. Further refinement and consideration of these variables are necessary to ensure the reliability and validity of the benchmark.
2.	The presentation of this work still needs improvement, as the figures are not in vector format. For example, Figure 3 lacks clear labels for the x and y axes, making it difficult to understand the meaning of the figure.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
