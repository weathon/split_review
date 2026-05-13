# LLMPhy: Complex Physical Reasoning Using Large Language Models and World Models

- Decision: Reject
- Scores: 6, 3, 5, 3, 5

## Abstract
Physical reasoning is an important skill needed for robotic agents when operating in the real world. However, solving such reasoning problems often involves hypothesizing and reflecting over complex multi-body interactions under the effect of a multitude of physical forces and thus learning all such interactions poses a significant hurdle for state-of-the-art machine learning frameworks, including large language models (LLMs). To study this problem, we propose a new physical reasoning task and a dataset, dubbed~\emph{TraySim}. Our task involves predicting the dynamics of several objects on a tray that is given an external impact -- the domino effect of the ensued object interactions and their dynamics thus offering a challenging yet controlled setup, with the goal of reasoning being to infer the stability of the objects after the impact. To solve this complex physical reasoning task, we present $\llmphy$, a zero-shot black-box optimization framework that leverages the physics knowledge and program synthesis abilities of LLMs, and synergizes these abilities with the world models built into modern physics engines. Specifically, $\llmphy$ uses an LLM to  generate code to iteratively estimate the physical hyperparameters of the system (friction, damping, layout, etc.) via an implicit analysis-by-synthesis approach using a (non-differentiable) simulator in the loop and uses the inferred parameters to imagine the dynamics of the scene towards solving the reasoning task. To show the effectiveness of $\llmphy$, we present experiments on our TraySim dataset to predict the steady-state poses of the objects. Our results show that the combination of the LLM and the physics engine leads to state-of-the-art zero-shot physical reasoning performance, while demonstrating superior convergence against standard black-box optimization methods and better estimation of the physical parameters. Further, we show that $\llmphy$ is capable of solving both continuous and discrete black-box optimization problems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of reasoning about the result of a complex multi-body physical interaction; specifically, the goal is to predict which objects will remain upright on a tray after an external force is applied by a pusher mass. This prediction is done by prompting an LLM to answer a multiple choice question about upright objects given the context of a synthesized video sequence of the multi-body physical interaction produced by a physics simulator. The key contribution of LLMPhy is an iterative framework between an LLM and the physics simulator to infer unknown physical properties of the objects in the scene, thereby allowing the physics simulator to synthesize the aforementioned video sequence.
	
The physical properties of the object categories are inferred by having the LLM generate programs for the simulator that attempt to model a reference dataset of videos of objects experiencing a different external force than the test set. The generated programs essentially consist of LLM-generated values for the unknown physical parameters, LLM-generated scene layouts that attempt to match those in a given reference video (object class, object location, and object color for each object in the video), and executable code for the physics simulator. This inference process is iterative and uses the error between the reference video's object trajectories and the simulated object trajectories as feedback to the LLM in order to generate updated (and ideally better) values of the unknown physical properties and a better scene layout. Once the values of the physical properties of the objects are estimated through this optimization process, they are applied to new scenarios involving more objects and a different external force; given only the first frame of a video of an interaction and the inferred object properties, an LLM generates a program for the simulator which then synthesizes a video of the interaction. This video is the video mentioned above that is provided as context to an LLM to answer a multiple choice questions about which objects will remain upright.
	
In addition to the LLMPhy framework, this paper also introduces a novel task and dataset.

### Strengths
- The paper is well written and organized, and the method is clearly explained and reasonably illustrated for further clarity.

- Both the problem and the proposed method are thoroughly mathematically formulated, which further helps with making the method understandable.

- The problem being addressed, namely reasoning about the result of complex multi-body physical interactions, is challenging and is relevant for enabling important future embodied capabilities.

- I like the ablation over the source of the physical parameter values (Random and Ground Truth), and I agree with the conclusions drawn from that ablation.

### Weaknesses
 - The experiments are limited. Only 3 objects categories are included in the experimentation, and the scenarios consist exclusively of a single external force being applied to a tray containing objects; further, the reasoning question that is being answered is relatively simple (which objects remain upright) compared to the kind of information one might want for practical uses, such as the pose of the objects.

- Only GPT4o is used for the LLM, which makes any extrapolation or empirical trend to other models imposible.

### Questions
I am recommending a weak rejection (marginally below acceptance) at this point primarily due to the limitations of the experiments. I think the paper is very well written with a robust technical description, but it is hard to draw conclusions from the experiments, preventing the paper from being a sufficiently significant scientific contribution. While I also think that the specific physical reasoning being evaluated is simple (which objects remain upright), more comprehensive experimentation would make this paper acceptable. To be clear, its potential impact is bounded by this simplicity, but I think the problem is still sufficiently interesting and challenging.
	
Here are some actionable additional experiments that would certainly help improve my recommendation:
- Introduce more object categories that exhibit sufficiently distinct physical behaviors after interaction
- Allow multiple sizes of the tray during testing to investigate having more objects and different configurations of objects.
- Test multiple initial positions and velocities for the pusher; as I understood, only one initial position and velocity was used in the tests (line 403-405).
- It would be better to include more LLMs for evaluations, ideally at least another SOTA black-box model and a SOTA open model. However, this can be prohibitive due to cost, so this is a lower priority than other experimental improvements as long as it is clearly acknowledged that conclusions about LLMs more generally are not possible.
	
I would also be interested in an ablation that provided ground-truth scene layouts during the optimization process in order to better understand the optimization performance of the LLM with respect to just the physical properties.

Here are some questions that I would appreciate having answered:
- What is the format of the multiple choice answers?
- Does the model exhibit consistency when presented with the inverse question, i.e., which objects will be knocked over?
- Why does each object category have the same allowable tilt \alpha?
- While Figure 3 shows the trajectory error, I wonder about the error for each individual parameter value; it seems like this should be available and might be interesting. Do the individual physical properties pose different difficulty for the LLM to infer?

Here are some minor comments (these had no impact on my recommendation):
- Since images are provided as input in some phases, it would be good to clarify that the LLM in question is multi-modal. Some readers may expect the acronym VLM for models that can also accept images as input. This is stated, but I recommend being proactive about avoiding any confusion about what the input is and how it is encoded.
- Figure 3 x-axis intervals should be integers
- missing space: "atleast" line 396
- double word: "aproaches that that use" line 460
- mispelling: "differnetiability" line 487
- Recommend a general grammatical pass, several other minor errors
- It would be good to write out PSNR (line 427)

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a task, dataset, and solution for an LLM-prompting based physics parameter estimation and trajectory estimation using privileged simulator feedback in the loop.

### Strengths
The authors attempt a novel task for improving low-level physical reasoning using an LLM, such as predicting physics parameter or object trajectories, instead of most prior works (to the best of my knowledge) do very high level semantic physical reasoning with LLMs. I believe this line of work is quite interesting, but the paper is needs more work both in terms of experimental study and presentation. See comments / suggestions below.

### Weaknesses
1. The abstract doesn’t differentiate proposed work with existing literature and justify the need of a new dataset/method.
2. Writing is a slightly unstructured and somewhat informal. For instance, L110: ‘..leads to significant improvements in performance against alternatives, including using Bayesian optimization and solely using only LLM for..’ would read more formal for a research paper as ‘leads to x% improvements over baseline methods that use only LLM or Bayesian optimization for..’. The current statement is unclear as to weather these are two different baselines or not. The use of word ‘significant’ without any concrete number is not standard for a research paper. L123: ‘Our experiments using LLMPhy on the TraySim dataset demonstrate promising results’, same issue with the word ‘promising’ - it is vague and not very concrete. L192: ‘Our attempt to solve the…’ - is grammatically incorrect and not sure what’s the meaning of the statement. These are just a few examples but for me most the paper reads like an initial draft and some writing iterations will significantly improve it’s presentation and understanding. Also, organizing the text in subsections (in Section 2, for instance) will improve the presentation. L325: ‘X is the input data, and Λ is the desired result.’ - very ambiguous notation definition. Major writing revision is needed.
3. There’s a claim that the method is generalizable to any simulation however results for only one simulation is presented. If the claim to true, the method application on other existing simulations should be shown as well. Or the authors should discuss what are the challenges for doing so.

### Questions
1. A qualitative example should be provided in the main paper instead of just in supplements to ground the method for the reader.
2. How will this method generalize to real world if ground truth values from the simulator are used?
3. What are plots submitted in supplementary supposed to mean, they are neither referenced in the main of supplementary pdfs.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a framework called LLMPhy, which combines large language models (LLMs) with physics engines to tackle complex physical reasoning tasks. The proposed method is tested on a new dataset, TraySim, where the model predicts object stability and interactions on a tray after an impact. LLMPhy operates in two phases: parameter estimation and simulation, with the LLM synthesizing hypotheses and the physics engine verifying them in a feedback loop. 

Key Strengths: 

TraySim Dataset: A tailored benchmark for multi-object physical interactions.

Zero-Shot Reasoning: Achieves notable improvements over Bayesian optimization on complex tasks. 

Limitations: 

Limited Parameter Scope: Currently models only four physical attributes, reducing generalizability. 

No Real-World Testing: Results are based solely on simulations, lacking validation in physical settings.

### Strengths
The paper proposes a black-box optimization framework that uses In-context learning to enhance the physical reasoning skills of SOTA LLMs.To augment the reasoning, the framework leverages the coding capability of LLMs and give it access to a simulator. This paper is a valuable contribution to physical reasoning using LLMs, presenting an original approach that effectively combines the strengths of language models and physics-based simulations. The results are promising, though some improvements in scalability, dataset credibility, and validation across physical engines would strengthen the framework’s applicability and robustness.

### Weaknesses
(1) my first concern is the limited physical parameters, the model currently explores only four physical parameters, which restricts its application to broader and more complex real-world scenarios. This constraint is acknowledged by the authors but remains a significant limitation for potential applications in varied physical environments.

(2) Dataset Scale and Generalization: With only 100 sequences, TraySim may be limited in capturing the full complexity of physical interactions. Expanding this dataset or testing LLMPhy on existing physics-based benchmarks could provide a more comprehensive understanding of the model’s generalization ability.

(3) Absence of Real-World Validation: While the simulation results are promising, real-world validations or experiments in a physical setup would enhance the credibility of the proposed method. Without real-world tests, it remains uncertain how well the model's inferred physical parameters would translate to actual physics.

### Questions
(1) how would LLMPhy perform when scaled to more complex environments with additional physical parameters? Besides, since different physics engines can have unique methods for simulating physical interactions, how might the choice of simulator (e.g., using MuJoCo vs. others) affect the model’s predictions and the general applicability of the method?

(2)  the simulator access setup is interesting, if applicable to real-world tasks, we can use LLM augmented with simulators to perform physical reasoning in real-world. However, the paper is assuming a perfect simulator  that can simulate real-world environment, which makes the results less interesting. It would be nice to add such experiments (studying how sim2real gaps will impact the evaluation)
Since the paper only use synthetic dataset to evaluate, this raise the question if the method applies to real-world robotics settings

(3) Reproducibility with Open-Source LLMs: Given that GPT-4o is closed-source, how feasible is it to adapt LLMPhy to open-source alternatives, and what changes would be necessary to maintain accuracy?

(4) Can the authors provide insights into how the framework might handle situations where parameter estimation fails due to high variability in initial conditions or other environmental factors?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a new framework combining Large Language Models (LLMs) with physics engines and optimization algorithms for complex physical reasoning. This approach cab infer and simulate multi-object dynamics under physical interactions. The authors propose a new dataset, TraySim, where objects on a tray are impacted by an external force, simulating dynamic, inter-object interactions.

### Strengths
This paper addresses an important question in AI by enabling large language models to perform complex physical reasoning, which is essential for real-world applications. The authors introduce a new framework, LLMPhy, that combines large language models with optimization algorithms and a physics simulator to estimate physical parameters and predict interactions. They also present a new dataset, TraySim, designed to benchmark models on multi-object physical reasoning tasks, making it a valuable resource for advancing AI’s capabilities in dynamic environments.

### Weaknesses
First, the paper lacks a discussion on its relationship with existing datasets like CoPhy and ComPhy, which also aim to infer physical properties of objects. These datasets offer benchmarks widely used in physical reasoning research, and a comparison of the proposed method on them would strengthen the validation of LLMPhy and clarify its distinct contributions.

Second, several established methods already tackle similar tasks, such as the approach presented in the ComPhy paper and methods like https://arxiv.org/abs/2012.08508 The absence of comparisons with these methods and relevant literature weakens the contextual positioning of LLMPhy within existing approaches.

Third, the methodology lacks clarity, especially regarding critical details like how multiview images are utilized to reconstruct object shapes and the specific inputs provided to the LLM. For example, if the LLM samples optimization variables based on physics knowledge from its training data, is object category information also supplied to guide this process?

Lastly, the unclear explanation of how raw RGB video data is converted into simulation inputs makes it difficult to assess how this approach could apply in realistic scenarios beyond controlled simulations. This raises concerns about the generalizability of LLMPhy to real-world applications.

### Questions
The authors may provide answers for my clarification questions about the method.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces LLMPhy, a zero-shot black-box optimization framework that integrates LLMs with physics engines to predict the dynamics of objects on a tray under external impact. The framework comprises two main phases:
1. The LLM infers the physical parameters of objects, including the coefficient of sliding friction, stiffness, damping, and rotational inertia, based on in-context learning examples and the objects' physical trajectories extracted from video data. The LLM then generates a program to simulate these trajectories, aiming to minimize the error between simulated and actual observed trajectories.
2. The LLM determines the scene layout by inferring object characteristics such as class, location, and color, based on the previously inferred physical parameters, the initial frame of the video sequence, and additional in-context examples.

Finally, LLMPhy refines its predictions using feedback from the simulator to minimize error. At each step, it keeps a record of previous attempts and errors, which helps the model improve its accuracy over multiple trials.


This work also introduces TraySim, a new dataset of simulated video sequences featuring a tray with varying numbers of objects. Evaluation of TraySim reveals that the proposed method outperforms baseline approaches, including random selection of physical parameters and direct use of an LLM.

### Strengths
This work presents a new approach that combines the strengths of large language models with advanced physics simulators. Additionally, it establishes a benchmark dataset, TraySim, which could be valuable to support future research in physical dynamics prediction.

### Weaknesses
1. The optimization step in Algorithm 1 appears to depend largely on the LLM’s ability to learn from previous errors through repeated attempts, making the approach heavily reliant on trial-and-error. Other optimization algorithms, such as CMA-ES, might also achieve comparable or potentially even better results. To strengthen the paper’s claims, consider including comparisons with additional optimization algorithms.
2. The proposed method is similar to the approach in the paper "Eureka: Human-Level Reward Design via Coding Large Language Models." In that work, an LLM is used to design reward functions that help train a reinforcement learning agent to teach a five-fingered robotic hand how to spin a pen.
3. The choice of intersection over union (IoU) as the evaluation metric is unclear. What does the answer set consist of? Why not simply use an exact match with the answer set instead?
4. In the second phase of LLMPhy, it’s unclear why predicting the color of the object is relevant for understanding its dynamics. Additionally, why is an LLM necessary to infer the object’s starting location? Wouldn’t it be simpler to use the tau function to extract the object’s location directly from the first frame of the image?
5. In Figure 2, an LLM processes the question along with the synthesized dynamics video to produce an answer, but it is unclear where the paper explains this process in detail. How exactly is this achieved?
6. The generalizability of the proposed Algorithm 1 is unclear, as it appears that the algorithm needs to be reinvoked for each new scenario to infer the physical parameters of the objects. Is there a way to enable the LLM to remember what it has learned and apply it to future scenarios?

### Questions
1. How is $\tau$ implemented?
2. Why choose to generate programs rather than directly generating relevant values for each attribute, especially when no real program logic, such as if conditions, for loops, or external libraries, is used?

### Soundness
2

### Presentation
2

### Contribution
1
