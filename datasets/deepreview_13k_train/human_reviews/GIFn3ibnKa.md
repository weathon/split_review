# Explore To Mimic: A Reinforcement Learning Based Agent To Generate Online Signatures

- Decision: Reject
- Scores: 5, 5, 1

## Abstract
Recent advancements in utilising decision making capability of Reinforcement Learning (RL) have paved the way for innovative approaches in data generation. This research explores the application of model free on-policy RL algorithms for generating online signatures and its controlled variations. Online signatures are captured via e-pads as sequential structural coordinates. In this study, we have introduced a robust on-policy RL agent named as SIGN-Agent, capable of  generating online signatures accurately. Unlike other RL algorithms, on-policy RL directly learns from the agent's current policy, offering significant advantages in stability and faster convergence for sequential decision-making. The proposed SIGN-Agent operates in a random continuous action space with controlled exploration limits, allowing it to capture complex signature patterns while minimizing errors over time. The downstream applications of this system can be extended in diverse fields such as enhancing the robustness of signature authentication systems, supporting robotics, and even diagnosing neurological disorders. By generating reliable, human-like online signatures, our approach strengthens signature authentication systems by reducing susceptibility towards system-generated forgeries, if trained against them. Additionally, the proposed work is optimized for low-footprint edge devices, enabling it to function efficiently in the area of robotics for online signature generation tasks. Experimental results, tested on large, publicly available datasets, demonstrate the effectiveness of model free on-policy RL algorithms in generating online signature trajectories, that closely resemble user's reference signatures. Our approach highlights the potential of model free on-policy RL as an advancement in the field of data generation targeting the domain of online signatures in this research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces an RL-based approach to generating online signatures using established on-policy RL methods (PPO, TRPO, A2C). The architecture includes a Sign Moderator designed to capture user-specific signature traits and improve signature quality. The system is tested on public datasets, with potential applications in digital authentication, robotics, and medical diagnostics.

### Strengths
* Originality: Using RL for signature generation is novel 
* Quality: The methodology is detailed. Multiple RL algorithms are compared. The author provided solid experimental insights.
* Clarity: The paper is well-organized. The author clearly explained the workflow, model components.
* Significance: The application has potential in secure signature generation and could be impactful in authentication, robotics, and diagnostics

### Weaknesses
 * The paper doesn’t propose new ML techniques.
* The paper lacks comparisons to recent SOTA generative models, which would help clarify how SIGN-Agent performs against advanced baselines.

### Questions
* As mentioned in weakness section, why there is no comparison with SOTA generative models? Is it because of some identified technical issues? Can the author share the insights?
* I have difficulty understanding how the reward function handles cases where the generated signature and the target signature differ in length. Does the author use interpolation? If one signature is 'smaller' or is in a different shape from another signature, how is the distance between signatures measured to ensure an accurate reward calculation?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes the use of on-policy RL algorithms (A2C, PPO, TRPO) in the online signature generation setting, with applications in robotics, authentication systems, and the diagnosis of certain neurological disorders (Parkinson's, Alzheimer's, dyslexia).

The authors design an environment with a simple interface and a distance-based reward function to judge signature accuracy, and show that RL algorithms outperform several generative model baselines (such as GANs, diffusion models, etc.) in terms of resulting signature accuracy. The authors further show that signature generation at inference time is fast across a variety of hardware, from a Raspberry Pi to an NVIDIA GPU.

### Strengths
The paper tackles an interesting problem with a variety of applications, and the RL baselines seem to clearly outperform the baseline generative modeling-style methods. Furthermore, it is very cool to note that the RL algorithm can perform inference fast even in resource-constrained hardware settings.

### Weaknesses
The paper doesn't "fill in the middle" in the sense that it doesn't compare to imitation learning methods in this setting, which I think can work well in this situation. Because you have datasets consisting of real human signatures, I feel like an imitation learning method that learns to model the sequential "signature distribution" could work as well here and is simpler than standard RL.

The main algorithmic point that stood out to me is the lack of off-policy RL algorithms which have been studied in this work currently. Because SIGN-Agent is trained on a single offline dataset, off-policy RL algorithms have their own advantages (e.g. global Q-value coverage, better sample efficiency etc.) that on-policy RL algorithms lack, which matters when it comes to generating signatures in any space as well as faster training convergence. In the space of signature generation, I feel like this may bring benefits that were not adequately studied yet.

### Questions
I am a bit confused by how the inference process works: when it comes to generating a signature for a person, does the agent have to "re-learn" how to write the specific signature or just generate from its policy at any time? I figure if you want to generate a signature of a specific person, re-learning might have to happen, especially for a memoryless model-free RL algorithm.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper introduces an RL-based signature generator. The generator, or policy, takes the current pen position as input and outputs a continuous value representing the delta between the current and next positions. The authors use the negative distance between the actual and generated signature positions as the reward signal. For their experiments, they apply three on-policy RL algorithms: PPO, TRPO, and A2C. The results show that RL-based algorithms can achieve a low distance between generated and real signatures.

*Disclaimer*: There may be misunderstandings in the above summary, as I found it challenging to fully understand the details presented in the paper.

Overall, the paper and its experiments do not meet the scientific rigor expected at ICLR, and significant rewriting is necessary before it would be suitable for publication. I recommend rejection.

### Strengths
I regret to say I did not find any notable strengths in this paper.

### Weaknesses
## Writing

The Related Work section feels disorganized. As someone new to the literature on signature generation, it's difficult to understand the similarities and relationships between this paper and the works mentioned in L129-L145. Do you adopt a similar formulation with a different approach, or is this a novel formulation? How do previous works improve upon one another, and what differentiates them? Where are the potential optimizations compared to prior work?

To clarify, my suggestion would be to add a subtitle for each paragraph, such as Online Signature Generation, Imitation Learning, and Inverse RL. In each paragraph, describe the specific limitations of previous work (vague terms like "requiring enhancements for scalability" aren't helpful) and explain how your paper addresses them. Do you use a different formulation to overcome these limitations? Do you apply IL or IRL, and why or why not? Additionally, avoid merely listing prior works, as currently done in L129-L136. Instead, aim for a concise summary that connects each work to your approach.

Section 3.1, titled "Overview of Proposed Method," primarily reviews three well-known on-policy RL algorithms. As a paper submitted to ICLR, the authors should assume that readers have expertise in these areas and move these introductory explanations to the appendix. This section also includes questionable claims, such as PPO "helps prevent drastic policy updates, ensuring stable training" or TRPO "significantly improves stability, ... allowing the SIGN-Agent to produce smoother and more realistic signature strokes." Please avoid making claims without supporting ablation studies. Additionally, if all three RL algorithms have unique advantages, how to choose among them or why using them all? Do they have specific strengths and weaknesses relative to each other?

Algorithm 1 does not seem to be referenced in the text. It should also be moved to the appendix, as it doesn't add unique insights to "signature generation."

In contrast, Section 3.2, which should be the core content, needs to be expanded with more detail. What is the exact neural network policy architecture? What are the state and action dimensions? Is the environment deterministic? If there are multiple signatures per individual, how does a single policy capture the variety of styles? What is the exact reward function—is it the negative distance or a normalized distance, possibly using a Gaussian kernel? When does the generation process terminate—do you use a maximum generation length, or is there a special termination mechanism?

In Section 3.3, I had difficulty understanding the Sign Moderator concept. Is it used for data augmentation? Is it applied only during inference or for both training and inference? What are the Q table's rows and columns, and how is it constructed? How is planning implemented here?

## Experiments

My primary concern is that the proposed approach doesn't seem to offer clear advantages. Current state-of-the-art AI systems for text, image, and video generation typically use supervised learning. However, the authors claim that RL is more effective for signature generation. Why?

How is the training and test data split? Evaluating the RL-based generator on data used for training is not fair to other baselines. The RL agent's KLD is significantly lower than that of supervised learning methods—potentially suggesting an issue, as these values are not even of the same order. It's also unusual that the diffusion network (a paper in 2022) performs worse than the GAN network (a paper 2020). Could you provide example snapshots of the generated signatures for all methods? Lastly, while generative models are known to generalize to some degree, how does the RL-based approach generalize beyond the training set?

Why were three RL algorithms used and evaluated against one another? What is the purpose of this comparison?

### Questions
I have presented my questions in the weaknesses section.

### Soundness
1

### Presentation
2

### Contribution
1
