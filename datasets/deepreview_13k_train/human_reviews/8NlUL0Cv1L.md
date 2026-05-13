# Generative World Explorer

- Decision: Accept
- Scores: 5, 8, 6, 6

## Abstract
Planning with partial observation is a central challenge in embodied AI. 
A majority of prior works have tackled this challenge by developing agents that physically explore their environment to update their beliefs about the world state. In contrast, humans can \textit{imagine} unseen parts of the world through a mental exploration and \textit{revise} their beliefs with imagined observations.
Such updated beliefs can allow them to make more informed decisions, without necessitating the physical exploration of the world at all times. To achieve this human-like ability, we introduce the \textit{Generative World Explorer (Genex)}, an egocentric world exploration framework that allows an agent to mentally explore a large-scale 3D world (e.g., urban scenes) and acquire imagined observations to update its belief. This updated belief will then help the agent to make a more informed decision at the current step. To train \textit{Genex}, we create a synthetic urban scene dataset, Genex-DB. Our experimental results demonstrate that (1) \textit{Genex} can generate high-quality and consistent observations during long-horizon exploration of a large virtual physical world and (2) the beliefs updated with the generated observations can inform an existing decision-making model (e.g., an LLM agent) to make better plans.3pt}{\includegraphics[height=1.pdf}}\xspace}
\newcommand{\worldwideweb}{\raisebox{-1.3pt}{\includegraphics[height=1.05em]{pics/internet-icon.pdf}}\xspace}
\begin{center}
    \small
    \renewcommand{\arraystretch}{1.2}
    \begin{tabular}{rll}
        \worldwideweb & \textbf{Website} & \url{https://generative-world-explorer

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Humans have the capacity to imagine the future and revise their beliefs about the world based on these imagined observations. Building on this concept, the authors have introduced a video generation model, GeNex, which enables an agent to mentally explore future imagined observations. Subsequently, a Large Language Model (LLM) is utilized as the policy model to predict future actions.

### Strengths
The concept is intriguing and the explanation is clear and straightforward.

### Weaknesses
1. There are some errors in the mathematical formulations presented, particularly in equations (3) and (4), which are confusing.
2. Although SCL is highlighted as a contribution, its effectiveness is not demonstrated in the experimental results.
3. The use of latent diffusion with temporal attention is not a novel architecture.
4. The real-world dynamics of vehicles do not allow for pure rotation, which the paper seems to overlook.
5, Table 3 presents an unfair comparison.

### Questions
1. Equation (3) is incorrect
2. The derivation of Equation (4) is unclear. Could you explain how it was formulated?
3. Is the LLM policy model fine-tuned or used as is?
4. The space of 'state' & 'belief' is not clearly defined.
5. It is unclear whether the diffusion model has been overfitted to the dataset, potentially making it inadequate for handling complex real-world interactions.
6. The entire framework appears to have little connection with POMDP.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces the challenge of planning with partial observation in embodied AI and highlights how humans can mentally explore unseen parts of the world to update their beliefs and make informed decisions. To replicate this human-like ability, the authors propose the Generative World Explorer (Genex), a video generation model that enables agents to mentally explore large-scale 3D worlds and acquire imagined observations to update their beliefs. They train Genex using a synthetic urban scene dataset, Genex-DB, and demonstrate that it can generate high-quality and consistent observations during long-horizon mental exploration and improve decision-making in an existing model.

### Strengths
+The idea of build a Generative World Explorer is interesting, and I think it will be useful to the development of embodied AI research.

+ It's practical to apply the proposed Genex to the embodied decision making process.

### Weaknesses
-There is a gap between the training data (synthesized with unity) and test data (captured from google street), the degrees of freedom of in the observation perspectives, google street seems to more limited compared to the unity. But the gap between training and test data may not  be always "bad", because such gap may show more "Generalizability".

-In the following sentence “An embodied agent is inherently a POMDP agent (Kaelbling et al., 1998): instead of full observation, the agent has only partial observations of the environment.” , “a POMDP agent” seems to lack rigor. POMDP (Partially Observable Markov Decision Process) is a modeling framework that can be applied to describe the behavior of an agent in an environment where full state information is not available. Visual observation is only one channel for information acquisition. Saying that incomplete visual observation necessarily leads to a POMDP is also not very rigorous.

### Questions
Overall I think this is a good paper that can contribute to the subsequent development of the field of embodied AI.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper works on the problem of decision-making in the partial observation setting. To tackle the task, the authors introduce a novel panorama-based video diffusion model which can imagine the observations from different positions. The authors further combine the generative model and the LLM to help the decision making process. To evaluate the decision making performance, they design a benchmark over 200 scenarios in single and multi-agent settings. The results show that their pipeline achieves better performance by augmenting the agent's imagination ability via the generative model.

### Strengths
1. Leveraging generative models to complete the partial observations to a full “world” understanding is reasonable to utilize the priors learned from the data.
2. For the panorama representation, they design the spherical-consistent learning during their learning process to improve the consistency of the panorama image. From their results, the panorama truly shows better consistency and leads to better representation of the scene.
3. The authors conduct extensive experiments and create a benchmark for demonstrating the challenging cases under the partial observation constraints.

### Weaknesses
1. In this work, the authors actually construct an explicit representation for “the imagination prior” to make decision making. However, in the benchmark setting, most questions seem only related to a specific case. For single-agents, just try to avoid some unseen cars. And for multi-agent, try to make the other two agents avoid collision. The task setting seems not challenging and common enough to demonstrate the usefulness of such imagination ability. Also it’s hard to see the real performance through such discrete choice-making decision accuracy. Potentially, the method can serve as a role to generate the bird-eye map from a single panorama image and can reveal the hidden cars not in the observation. 
2. The paper mentions such imagination can be further updated based on new observations, however, in this work, there is no integration of the imagination and the new observations.

### Questions
1. How to determine what’s the trajectory to explore if the world is unlimited? And how to make sure the information is enough to make a decision?
2. Is there better way to evaluate the imagination ability, like the 3D concept error with GT (there is hidden car or not, how much unobserved information is discove

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
The authors of this study investigate the problem of  planning with partial observation, which is important in embodied AI. To achieve this, the authors propose a video generation model Generative World Explorer (Genex), that allows an agent to simulate the world through panoramic representation. The authors also propose an imagination-driven POMDP framework, where generated images assist the agent in decision-making through question-answering (QA).

### Strengths
1. Importance of the work: While world models with front-view and multi-view videos are actively investigated by the research community, the generation of panoramic videos is seldom explored. This paper introduces a novel training strategy specifically for panoramic video generation, contributing valuable insights for the community.
2. In this work, the authors aim to define an embodied agent with belief revision driven by imagination, which is able to imagine hidden views through imaginative exploration..
3. Two new datasets called Genex-DB and Genex-EQA have been collected to facilitate the proposed pipeline. The scenarios include a diverse range of styles: Realistic, Animated, Low-Texture, and Geometric.
4. On the proposed dataset Genex-DB and Genex-EQA, the proposed method Genex achieves favorable results in panoramic video generation and embodied QA, compared to other baselines.

### Weaknesses
1. My main concern is the **actual impact** of the proposed 'imagination' on embodied QA. While the authors show an approach to link the panoramic video generation with embodied QA, the experiments do not explicitly demonstrate the effectiveness of the ''imagination generation''. How about the results of POMDP without imagination？
2. As far as the reviewer knows, most of the generation models (including the SVD used in this paper) are poor in the reasoning ability, because essentially they are just simulating the probability of objects appearing. In most cases, if there are no explicit constraints like specified object category, the generation model wouldn't expect an ambulance to be here in most cases. This is an open question and the reviewer wants to see the point of the authors. Additionally, could the authors provide more examples of the imagination results, particularly challenging cases like those shown in Fig.12?
3. Some **concerns about the Genex-EQA questions**. The questions and answers in the dataset are quite subjective. For example in the second row and second column in Fig.12, the gt choice is "Signal the car to stop for the pedestrian". This action seems impractical for an autonomous driving vehicle. Further clarification on the methodology and rationale behind the question and answer collection process is needed to understand the dataset's reliability.
4. For panoramic video generation task, though the method serves as a baseline, it is beneficial to have **some comparisons with previous single-view world models** (because they can also perform panoramic video generation task by just replacing the data) and demonstrate why these models fail to generate panoramic videos.

### Questions
1. Some typos: L96: imaginatively-imaginative; L186: a-an; Fig.15 Imaginatin-Imagination.
2. Fig link: L379: Fig.2? Maybe this should be Fig.6.

The reviewer has identified four major concerns and would like the authors' responses to these points. Please answer each concern in the rebuttal stage. The reviewer will respond according to the authors' rebuttal in the discussion phase.

### Soundness
2

### Presentation
2

### Contribution
4
