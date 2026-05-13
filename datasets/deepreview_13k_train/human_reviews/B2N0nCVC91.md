# FLIP: Flow-Centric Generative Planning for General-Purpose Manipulation Tasks

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
We aim to develop a model-based planning framework for world models that can be scaled with increasing model and data budgets for general-purpose manipulation tasks with only language and vision inputs. To this end, we present \underline{FL}ow-Centr\underline{I}c generative \underline{P}lanning (\name), a model-based planning algorithm on visual space that features three key modules: 1) a multi-modal flow generation model as the general-purpose action proposal module; 2) a flow-conditioned video generation model as the dynamics module; and 3) a vision-language representation learning model as the value module. Given an initial image and language instruction as the goal, \name\ can progressively search for long-horizon flow and video plans that maximize the discounted return to accomplish the task. \name\ is able to synthesize long-horizon plans across objects, robots, and tasks with image flows as the general action representation, and the dense flow information also provides rich guidance for long-horizon video generation. In addition, the synthesized flow and video plans can guide the training of low-level control policies for robot execution. Experiments on diverse benchmarks demonstrate that \name\ can improve both the success rates and quality of long-horizon video plan synthesis and has the interactive world model property, opening up wider applications for future works. Video demos are on our website: \href{https://nus-lins-lab.io/flipweb/}{https://nus-lins-lab.io/flipweb/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work, the authors consider the task of high-dimensional generative planning for manipulation tasks. Specifically, they seek to design a prediction task which is relevant for manipulation planning and can also operate in a task-agnostic way on widely-available data. The model-based planning primitives are: an action generation module (generating 2D flow), a state transition model (generating next frame of video given flow + current observations), and a value function for determining how close a state is to the goal (based on language-conditioned visual encodings). This allows them to search for a flow-based plan, which at execution time can be executed by a learned plan-conditioned low-level policy. They evaluate the ability of their model to make coherent / correct plans on several benchmark tasks, and evaluate its utility for policy execution on the LIBERO-LONG task.

### Strengths
# Originality

The high-level approach is a reasonable combination of ideas in planning, visual representations, and generative modeling. On the flow generation component, It’s difficult to establish the level of novelty as there are a number of concurrent works proposing generative flow models for manipulation (e.g. GeneralFlow, Track2Act, etc.), but I think the combination of ideas here - for planning - is original/novel.

# Quality

The quality of this paper is high. The experiments are thorough and comprehensive (with two caveats, discussed later).

The design of each component is sound, and there are lots of details / modifications that the authors conducted (and motivated!) which I found interesting and commendable. For instance, the ideas about video chunking (instead of per-frame) for value prediction, and the details about conditioning a model on flow, action space ablation, etc. are all solid contributions for other practitioners.

# Clarity

The paper is quite clear - each step of the algorithm is well explained.

# Significance

This paper is of moderate significance. I think the flow-based (particle-based) generative modeling approach as an action space has a lot of potential to be powerful, and clearly shows improvements for reconstruction / video generation.

### Weaknesses
The primary weakness of this paper is that, while the representation + models they built are quite interesting and useful for modeling the actual video domain they are imitating, the actual downstream utility of their method is not sufficiently characterized. Specifically, the method simply does not substantially outperform ATM, which has no planning at all and uses a similar generative representation, on the actual downstream manipulation task. Moreover, the inclusion of flow only seems to hurt the downstream policy in comparison to video conditioning. I’m not saying this method can’t show meaningful improvements over other approaches, but either the LIBERO setting chosen, or the particular low-level policy chosen, yield results that do not support the claim that this generative flow modeling + planning method provides downstream utility. Especially given the overhead. Of particular concern is the Ours-FV results, which are not well-explained.

Another weakness is that the experiments seem to be restricted to single domains, even though the method seems to have been designed to be task-agnostic - I would have liked to see the authors leverage this property more, e.g. by training predictive models on the full LIBERO benchmark and then finetuning on a subset of tasks for policy learning, or similar (even internet-scale pretraining… although I realize this is out of scope for this contribution / infeasible if there are resource constraints).

Another existential issue is that this paper is framed as a “flow generation for manipulation” paper, but the bulk of the experimentation+analysis is geared towards video prediction which has little to do with manipulation. I don’t think it stands on its own as simply a video prediction paper (at least on these tasks alone) - and I would have liked to see a larger emphasis on the actual analysis for manipulation tasks (e.g. geometric precision is a visual prediction problem, or feasibility, or other downstream metrics).

### Questions
Why doesn’t this method offer significant downstream benefits compared to ATM, which has no planning, on the selected benchmark?

How much does the action space affect downstream performance? If you were to retrain ATM with this adjusted action space, would the ranking change significantly? Do the marginal benefits of your model come from this component (unrelated to the planning contribution)?


---
# Post-Rebuttal Update

The authors have addressed many of my concerns adequately, and greatly strengthened their paper with the modifications to their downstream policy architecture (as well as additional details in the appendix). Bumped score to Accept.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new model-based planning framework called FLIP. It consists of 3 components: 1) a flow generation network that generates action flows given the current image observation and a language instruction 2) a video generation (dynamics model) that conditions on the flow and generate future video frames 3) a value function that evaluates the task progress (reward) given the image observation and language description. The key is the introduction of using flow as an action representation and condition the video generation model on the flow. The whole system can be used for model-based planning to generate video plans given a task, and the flow itself can also be used for guiding low-level policy execution. Various experiments are performed in both simulation environments and real-world videos.

### Strengths
- This paper is overall clearly written.
- The experiments cover a range of test settings, and the ablation studies help understand each component of the method.
- Overall the experiment results are good, which demonstrates the effectiveness of the proposed method.

### Weaknesses
 - I feel the paper could have compared to some stronger baselines, for some of the experiments. E.g., for experiments in section 5.1 and section 5.2, a stronger baseline than UniPi could be UniSim [1]. The reviewer understands that the code may not be open-sourced, in this case, at least some discussion to the paper should be included. There is another very recent work DIAMOND [2] that can do very long-horizon and detailed video prediction into the future conditioned on actions. Both of these paper use just a diffusion model without the need to first extract action flows, which seems to contradict to the key proposal of this paper, which is to make the model flow-centric. Some discussion on this would be appreciated.
- For the flow generation model -- why using a C-VAE instead of a diffusion model? Some discussion on this design choice would be appreciated. 
- For all experiments, please specify the quality of the video demonstrations, e.g., are they collected using a random policy, or are they expert videos? This would be important to understand, e.g., in section 5.1., if the system can learn from sub-optimal data for planning or does it need optimal demonstrations.

### Questions
Please see the weakness section

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes FLIP, a model-based planning algorithm on visual space.
The algorithm consists of three main modules 1) a flow generation model as an action proposal module, 2) a flow-conditioned video generation model as a dynamic module, and 3) a value module.
The flow generation model generates flows based on the observation and a language instruction.
The video generation model generates videos with a Diffusion Transformer based the predicted flows.
The value module, built on a vision-language representation model, is used to assign values for each frame in a video to enable model-based planning in the image space.
Model-based planning algorithm leverages the three modules to search for a sequence of flow actions and video plans that maximizes the discounted return.
Experiments were performed to evaluate the capability of the proposed method on generating video plans, generating long-horizon videos, and accomplishing manipulation tasks.
The proposed method outperforms comparing baseline methods and showcases interactive properties, zero-shot transfer capability, and scalability.

### Strengths
The paper is well-written and clear. 
Leveraging CVAE to address the multi-modality of flows is well-motivated.
Additionally, the paper proposes to use a mixed-conditioning mechanism for multi-modal conditional video generation.
For the value module, the paper modifies the original LIV method and uses video clips instead of video frames as a unit to account for the noisy value prediction.
Experiments show that the proposed method surpasses comparing baseline methods in generating video plans, long-horizon videos, and performing manipulation tasks.
The paper also showcases interesting interactive properties, zero-shot transfer ability, and scalability of the proposed method.

### Weaknesses
1. There are no real-robot experiments to validate the effectiveness of the proposed method in policy learning in the real world. Incorporating such experiments and comparing with recent policy learning methods (e.g. ATM, OpenVLA [1] or Octo [2]) would provide a more comprehensive understanding of FLIP's performance in real-world policy learning.

2. The paper only evaluates the policy learning capability on a suite of LIBERO, i.e. LIBERO-Long. Conducting an evaluation to assess the generalization capability of the proposed method, e.g. on the LIBERO-Object suite, would be beneficial. Also, including a comparison with recent policy learning methods, like OpenVLA [1] or Octo [2], would further strengthen the paper.

2. In Sec. 5.2, the paper compares with IRASim on a text-to-video task. However, IRASim generates video based on a trajectory instead of a text. For the text-to-video task, it would be better to compare with a text-to-video method (e.g. [3]).

### Questions
1. In Sec. 5.1, the paper compares with FLIP-NC, an ablation of the proposed method FLIP which has no value module as guidance. Is it possible to provide more details on how FLIP-NC performs beam search without a value guidance?

2. Is it possible to provide a more detailed description on the typical failure modes of FLIP in policy learning (Sec. 5.3) ?

3. In the Dynamics Module Experiments in Sec. 5.4, the paper compares with LVDM and IRASim on short-horizon video generation. The proposed method is provided with ground-truth flows to generate videos. What information is provided for the two comparing baseline methods?

4. Are the flow generation model and the video generation model trained individually or jointly?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a model-based planning framework (FLIP) designed for general-purpose robotic manipulation tasks using language and vision inputs. The framework allows for the progressive synthesis of long-horizon action plans, starting from an initial image and language instruction. FLIP effectively uses image flows to represent complex movements, enhancing the planning process for manipulation tasks across various objects and robots. They propose a multi-modal flow generation model predicting actions by generating dynamic representations of movements, simulating future video sequences based on the proposed actions, and evaluate the generated videos to maximize the task's success probability.

### Strengths
- The paper is well-written and methodically presented. 
- FLIP introduces a novel approach to model-based planning by integrating multi-modal inputs, which enhances its versatility for various manipulation tasks
- FLIP is designed to scale with increasing model and data budgets, making it suitable for a variety of applications and capable of leveraging more extensive datasets as they become available.
- The generated plans can be used to inform and train low-level control policies which can support several hierarchical policies that require strategic decision-making and planning.

### Weaknesses
 - The framework may struggle with ambiguities in language instructions or unexpected changes in the environment. 
- Depending on the computational demands of the multi-modal modules, real-time performance in dynamic environments could be a concern. Evaluating the speed and efficiency of planning under real-time constraints would be crucial.


### Questions
- How does FLIP compare to other state-of-the-art planning frameworks in terms of efficiency and effectiveness?
- What are the limitations of using image flow as an action representation? In which scenarios/tasks, this would not be ideal? 
- How does FLIP handle ambiguities in language instructions?
- Are there any results on the real robot that show the applicability on world models even for quasi-static tasks? 
- How will the model's performance be affected in the presence of noise or visual obstructions? 
- How does the performance of FLIP depend upon or scale with the size of the available data, numerical analysis for the same would be helpful to understand the efficiency of the proposed approach.

Please also address other comments in the weaknesses section above.

### Soundness
3

### Presentation
3

### Contribution
3
