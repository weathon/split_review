# GPT-Driver: Learning to Drive with GPT

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
We present a simple yet effective approach that can transform the OpenAI GPT-3.5 model into a reliable motion planner for autonomous vehicles. Motion planning is a core challenge in autonomous driving, aiming to plan a driving trajectory that is safe and comfortable. Existing motion planners predominantly leverage heuristic methods to forecast driving trajectories, yet these approaches demonstrate insufficient generalization capabilities in the face of novel and unseen driving scenarios. In this paper, we propose a novel approach to motion planning that capitalizes on the strong reasoning capabilities and generalization potential inherent to Large Language Models (LLMs). The fundamental insight of our approach is the reformulation of motion planning as a language modeling problem, a perspective not previously explored. Specifically, we represent the planner inputs and outputs as language tokens, and leverage the LLM to generate driving trajectories through a language description of coordinate positions. Furthermore, we propose a novel prompting-reasoning-finetuning strategy to stimulate the numerical reasoning potential of the LLM. With this strategy, the LLM can describe highly precise trajectory coordinates and also its internal decision-making process in natural language. We evaluate our approach on the large-scale nuScenes dataset, and extensive experiments substantiate the effectiveness, generalization ability, and interpretability of our GPT-based motion planner.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a novel method for motion planning in the context of autonomous driving, where they propose to use GPT to both output the motion plan and to explain the reasoning behind it. They fine-tune the GPT model using textual representation of the surrounding context and the output motion plan, and show that the method compares very positively when compared to the existing state-of-the-art.

### Strengths
- A very relevant problem being evaluated.
- Interesting and novel approach being proposed.
- Promising experimental results.

### Weaknesses
 - The method does not seem to be very feasible for online execution.
- The method seems to critically depend on the existing SOTA methods as its integral part, making the overall system quite complex.
- The experimental section can be improved.

- The authors should fix the format of the references. Instead of "P3 (Sadat et al., 2020)" they use "P3 Sadat et al. (2020)" throughout the work, which is incorrect and adds some confusion in several places.
- Figure 1 is not referenced in the text.
- The method assumes the existing strong method for perception and prediction, which seems like quite a large requirement. The input to GPT assumes detections and their predicted trajectories, which seems to add quite a lot of complexity (both from the training and inference standpoint).
- Related to this, the authors don't really do an ablation study of the perception/prediction module, which would give an indication of how robust is GPT to this part of the methodology.
- In eq (2) the authors say that the input to their model is a map, yet that is not the case as they don't provide the map to the model.
- Later they say that their model can indeed take the map as an input, but given that they represent all inputs as a text it is far from clear how can that be done.
- In Section 4.2 the authors say that other approaches depend on various heterogeneous inputs "which makes their systems intricate and time-consuming", yet the proposed method also depends on the same inputs since it depends on UniAD. So the authors are not being really honest in this case.
- In Section 4.3 it is unclear if the authors use fully trained UniAD for generating input strings for their method, or if they use partially trained UniAD. This should be clarified.
- Some sort of latency analysis should be provided, beyond just a handwavy explanation from Section 4.6. This is important for the practical application of their method and is something that the authors should explore.

### Questions
I found the work quite interesting, and the combination of the motion planner with GPT seems like a neat idea (although not that novel at this point). However, the method seems far from being actually applicable in the real world, which the authors don't really explore or address (beyond a very brief explanation in Section 4.6 that seems insufficient and handwavy). Moreover, the explanations of the method can be improved significantly, and the methodology itself seems quite complex and dependent on the existing SOTA methods.
Detailed comments can be found below:
- The authors should fix the format of the references. Instead of "P3 (Sadat et al., 2020)" they use "P3 Sadat et al. (2020)" throughout the work, which is incorrect and adds some confusion in several places.
- Figure 1 is not referenced in the text.
- The method assumes the existing strong method for perception and prediction, which seems like quite a large requirement. The input to GPT assumes detections and their predicted trajectories, which seems to add quite a lot of complexity (both from the training and inference standpoint).
- Related to this, the authors don't really do an ablation study of the perception/prediction module, which would give an indication of how robust is GPT to this part of the methodology.
- In eq (2) the authors say that the input to their model is a map, yet that is not the case as they don't provide the map to the model.
- Later they say that their model can indeed take the map as an input, but given that they represent all inputs as a text it is far from clear how can that be done.
- In Section 4.2 the authors say that other approaches depend on various heterogeneous inputs "which makes their systems intricate and time-consuming", yet the proposed method also depends on the same inputs since it depends on UniAD. So the authors are not being really honest in this case.
- In Section 4.3 it is unclear if the authors use fully trained UniAD for generating input strings for their method, or if they use partially trained UniAD. This should be clarified.
- Some sort of latency analysis should be provided, beyond just a handwavy explanation from Section 4.6. This is important for the practical application of their method and is something that the authors should explore.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studied the application of LLM in motion planning for autonomous driving. In the proposed GPT-Driver framework, perception and prediction results (e.g., object types, coordinates, and predicted future coordinates) together with the ego states are converted into language tokens. Then, they are used to prompt an LLM to produce a planned trajectory alongside its decision-making process in natural language. In particular, the authors propose a fine-tuning scheme with auto-generated reasoning labels to fine-tune a GPT-3.5 model for the purpose of motion planning. The results show that the GPT-Driver outperforms existing learning-based motion planners in terms of imitating human drivers and performs on par with top methods in collision rate.

### Strengths
1. The proposed method is simple, straightforward, and well-performing in the studied driving scenarios. 
2. It provides informative insights on the feasibility and performance of steering LLMs into motion planners producing numerical waypoints. It is particularly interesting and promising that the authors show that GPT-Driver can outperform existing approaches after few-shot fine-tuning.

### Weaknesses
While the proposed GPT-Driver has demonstrated impressive performance, the paper lacks in-depth analysis to help the audience gain a deeper understanding of the model's performance and limitations:

1. For example, an ablation study should be conducted to evaluate the benefit of having chain-of-thought reasoning in the LLM's output. While it is well-known that chain-of-thought reasoning boosts LLM's performance, it is worth evaluating its contribution to the motion planning task. Specifically, the analysis should examine if the reasoning process is truly guiding the trajectory generation or if the LLM is simply generating a plausible trajectory without relying on the intermediate reasoning steps. The study should also investigate the impact of the length and complexity of the reasoning on the final trajectory accuracy.

2. Also, there should be an ablation study to evaluate the benefit of having the auto-generated chain-of-thought reasoning labels during fine-tuning. While the proposed method to auto-label the chain-of-thought reasoning through hypothetical ego-trajectory is sensible, it is not guaranteed to generate the ground-truth reasoning process (i.e., identifying the actual causal objects and their relations to the ego agents). The authors claimed that this strategy worked well in practice. I wonder how the authors evaluated the quality of the auto-generated labels and drew such a conclusion. There should be numerical results to examine the quality of the auto-generated labels, and an ablation study to validate that the fine-tuning process indeed benefits from the plausibly noisy and inaccurate reasoning labels. For instance, what is the impact of varying the quality of these labels on the final performance? How does the model perform when trained with human-annotated reasoning labels, if available, compared to auto-generated ones?

3. The GPT model is only prompted with a simplified textual description of the traffic scene, e.g., without maps, historical trajectories of the objects, or predicted future trajectories over multiple timesteps. It is quite surprising that the GPT model can surpass carefully designed learning-based planners by a large margin in L2 errors. It is rather counter-intuitive as the information currently missing (e.g., maps, historical contexts, future trajectories) is normally considered important for motion planning in autonomous driving. The authors should provide an in-depth analysis and pinpoint the scenarios where GPT-Driver has clear advantages against SOTA methods and cases where GPT-Driver suffers. Only showing the average L2 errors and collision rates could be misleading, as the average statistics highly depend on the data distribution. For example, are there specific scenarios, such as lane changes or intersections, where the GPT-Driver excels or struggles compared to other methods? A more granular analysis of performance across different driving situations is needed.

### Questions
1. Could the authors clarify how the hypothetical ego trajectory is generated? Whether an object is identified as critical seems to highly depend on the hypothetical ego trajectory. The authors should discuss how they designed the generation algorithm and adjusted the hyperparameters. 

2. Is the motion planning performance evaluated with the most likely output sequence? How stable and reliable is the GPT-Driver in generating sensible reasoning processes and trajectories? Is it able to account for multi-modality in driving behavior?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose some techniques for using ChatGPT3.5 to generate driving trajectories (as a list of coordinates) from a language representation of the world/ego state. The approach outperforms end-to-end learning-based approaches on a computer vision driving benchmark.

### Strengths
- How to best utilize LLMs for autonomous vehicles is an interesting and timely question that I think is of great interest to the community.
- That the authors achieved such a huge improvement with fine tuning is a surprising insight (going from worst to best results), but potentially useful if it checks out.

### Weaknesses
 - The benchmark comparison seems a bit apples to oranges. You compare against end-to-end computer vision approaches from CVPR, but your approach assumes the object detections are given and only solves the planning part. Even if you use the detections from a competing CV method, it is unclear to me how strong this result is as planning is perhaps not the main focus of their approach. It would have been good to have some conventional planning stack as baseline as well.
- Your portrayal of related work outside of CV/learning seems weak/dated with the most recently cited planning paper being from 2018. I quite frequently see conventional planning/optimization papers for autonomous driving at other venues (robotics, AI...). Check some recent surveys, I include one which does not use your terminology of "rule-based" for these either (not sure what you mean by that). [1] S. Teng et al., "Motion Planning for Autonomous Driving: The State of the Art and Future Perspectives," in IEEE Transactions on Intelligent Vehicles, vol. 8, no. 6, pp. 3692-3711, June 2023, doi: 10.1109/TIV.2023.3274536.
- This really is "GPT"-driver, it just uses the web APIs for ChatGPT for prompting and fine tuning. GPT is state of the art (at least if you had used 4.0) so is somewhat defensible, but it would have been interesting to see how this generalized across other LLMs.

Minor questionable claims or presentation issues:

- You write "Albeit simple, these approaches attempt to simultaneously regress waypoints across different scales, e.g. coordinate values ranging from 0 to over 50, which generally results in imprecise coordinate estimations of the more distant waypoints": This seems like it would be fixed by a simple rescaling, is this really a fundamental problem with IL approaches? This also does not mention RL-based approaches (see [1]) 
- Sec 3.2:  Does all of the IL approaches really use absolute value loss, that seems oddly specific? The discussion of how a number is encoded as a text string seems pretty obvious/trivial.
- "It is worth noting that these state-of-the-art planners heavily rely on multiple heterogeneous observations such as detections, predictions, occupancy grids, and maps, which makes their systems intricate and time consuming." You rely on their detections (maybe predictions, unclear) so this seems at least half misleading.

### Questions
- What data did you use for fine tuning vs evaluation? I am not very familiar with this particular benchmark, but your trajectory prediction errors are surprisingly low. The optimal trajectory for driving is in reality sometimes ambigious, possibly multi-modal and an open research problem, so it seems a bit suspicious that you can get centimeter precision on trajectory prediction. 
- Can you clarify what prompts you used in your three-stage approach for training. Fig 3. seems to only include the prompt for the final stage?
- Isn't your information about the obstacles both incomplete and technically cheating (acausal) in the simple prompting baseline, since you do not include obstacle velocities, but seemingly where they will be in the future? Care to comment on what this description really means, where they will stop / be x seconds? in the future?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The author proposed a scheme utilizing ChatGPT for motion planning, where perception results (or ground truth) are used as inputs. With meticulous prompt design and finetuning through the API, the approach achieved commendable open-loop performance on the large-scale Nuscenes dataset. Additionally, experiments were designed to demonstrate the large language model's generalizability (few-shot) and interpretability (reasoning) for motion planning tasks.

### Strengths
1. The overall text flows smoothly and is easy to understand.
2. Seeing the large language model demonstrate impressive performance and few-shot capabilities in such a simple manner is astonishing. This can better motivate people to continue validating the exploration of large language models in the direction of motion planning.
3. The author will open-source the code, and since the experiment is relatively simple, I believe there is a high probability that the experiment can be reproduced. The confidence level in the experiment's results is very high.

### Weaknesses
1. While I personally appreciate the simplicity and effectiveness of this research, I do not believe it possesses sufficient novelty to be a paper for ICLR. The article simply utilizes the ChatGPT API for finetuning, which can be regarded as an application experiment report on motion planning using ChatGPT. Since it does not introduce any new modules or methodologies, I think its actual contribution to the field is quite limited.
2. Motion planning ultimately needs to be validated in a closed-loop system, as the results from open-loop and closed-loop scenarios are not always aligned, as highlighted in [1]. In cases where perception results (or ground truth) are directly used as input, it is easy to integrate into a closed-loop system, and there are numerous readily available public datasets for closed-loop testing, such as Nuplan, Waymo Motion Dataset, MetaDrive, etc. If closed-loop results could be obtained, I believe it would significantly enhance the credibility and contribution of the paper.
3. The descriptions in the RELATED WORKS section of the article are somewhat inaccurate. Dauner et al. (2023)[1] is actually a rule-based method.

### Questions
1. I hope to see closed-loop results; please refer to the "Weaknesses" section for more details.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
