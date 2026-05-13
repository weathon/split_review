# On Orchestrating Personalized LLMs

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
This paper presents a novel approach to aligning large language models (LLMs) with individual human preferences, sometimes referred to as Reinforcement Learning from *Personalized* Human Feedback (RLPHF). Given stated preferences along multiple dimensions, such as helpfulness, conciseness, or humor, the goal is to create an LLM -- without completely re-training -- that best adheres to this specification. Starting from specialized expert LLMs, each trained for one such particular preference dimension, we propose a black-box method that merges their outputs on a per-token level. We train a lightweight Preference Control Model (PCM) that dynamically translates the preference description and current context into next-token prediction weights. By combining the expert models' outputs at the token level, our approach dynamically generates text that optimizes the given preference. Empirical tests show that our method matches or surpasses existing preference merging techniques, providing a scalable, efficient alternative to fine-tuning LLMs for individual personalization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper explores Reinforcement Learning from Personalized Human Feedback (RLPHF), introducing a new black-box approach for generating personalized outputs. This approach includes a lightweight Preference Control Model (PCM) that dynamically adjusts next-token prediction weights based on a user’s preference description and the current context. The method requires access to the top output logits of each expert model, bypassing the need for direct weight access. A reward model for each preference dimension, alongside the REBEL online reinforcement learning algorithm, is employed to train the PCM to optimize the average reward for specified preferences. MPD outperforms prior preference-merging techniques in the experiments.

### Strengths
The method operates as a black-box, requiring only top logits rather than access to expert model weights.

The method is a scalable solution for personalization by using token-level merging, which reduces the need for extensive fine-tuning.

MPD demonstrates faster performance than previous weight-merging techniques on most modern computing resources.

### Weaknesses
Details about the architecture of the Preference Control Model (PCM) are limited and could be expanded.

The MPD training approach appears conventional, lacking novelty in this aspect.

The paper does not assess MPD's performance with larger or alternative LLM architectures beyond Tulu-7B.

The code is not open source, which limits reproducibility. The reasons for its performance advantages over Personalized Soup are not clearly explained.

### Questions
In Figure 1, which components represent the expert models? Are these expert models distinct or identical?

Do the expert models utilize different prompts to reflect varied preferences?

If the expert models are identical, what advantages does MPD offer over using a single model for preference alignment?

### Soundness
3

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
5

### Summary
This paper introduces a novel framework, Merged Preference Dimensions (MPD), for dynamically aligning large language models (LLMs) with individual user preferences without re-training the entire model. By utilizing a lightweight Preference Control Model (PCM), it merges outputs from expert LLMs trained in specific preference dimensions (like humor or conciseness) at the token level. This approach allows for real-time customization of LLM outputs to suit individual preferences, demonstrating superior performance in adapting to user-specified dimensions compared to traditional methods. The framework is efficient, scalable, and requires no access to original training data, offering a flexible solution for personalized language generation.

### Strengths
1. The paper is well-written.
2. The problem of personalized LLMs is timely and interesting.

### Weaknesses
1. Significance of the Problem: The manuscript describes a solution for a "black-box method" using trained expert models for each preference dimension. However, the necessity and practicality of these black-box expert models are questionable as they do not seem to exist in practice. As described in the manuscript, the expert models are not pre-existing and are instead trained by the authors following the procedure from Jang et al. (2023). This approach contradicts the concept of using already available black-box models and raises questions about the real-world applicability of the proposed method. The argument that industry might have such models is not convincing, as the models needed are very specific to individual preference dimensions, not general character models.

2. Lack of Technical Novelty: Based on the approach described, I do not find significant innovation in this paper, especially in comparison to existing literature cited as [1-3], particularly [3]. The content in Section 3.1 looks similar as in [1], and Section 3.2 seems to extend existing work on RLHF and REBEL without introducing substantial new insights or advancements. This overlap with prior works might limit the perceived contribution of the current study. Specifically, the token-level merging of expert outputs, while presented as a core contribution, appears to be a straightforward application of existing techniques rather than a novel methodological advancement.

3. Experimental Setup: The experimental design, as mentioned, appears to be flawed (refer to Question 2).

### Questions
1. Figure 1 Query: The user input is stated as “I want a helpful, concise, and funny response!”. It is not clear why the weights for the three dimensions are set as 0.4, 0.1, and 0.5 respectively. How can this distribution of weights be explained?

2. Source of Weights: Regarding the Koala and Ultrafeedback datasets and the preference dimensions listed in Table 1, I am curious about how the authors derived the different lists of weights for these dimensions. Is it possible to obtain the ground truth for these weights, or are the weights generated by the Preference Control Model (PCM) interpretable?

3. PCM Training Process: The Final Reward is obtained by an average weighted sum of different Bradley-Terry Rewards. Why does the PCM employ a non-uniform weighting in this context? An explanation of the choice of weights used and their impact on the model’s output would provide deeper insights into the PCM’s functionality.

4. Computational Cost and Scalability: The training process for the Merged Preference Dimensions (MPD) framework appears to require loading multiple pre-trained LLMs as well as the PCM simultaneously. I am concerned about the computational cost and scalability of this training process. Could the authors provide details regarding the computational resources required and discuss the potential limitations in terms of scalability?

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Merged Preference Dimensions (MPD), a method for aligning large language models (LLMs) with personalized human preferences. Instead of fine-tuning or merging model parameters, MPD dynamically merges the outputs of specialized expert LLMs at the token level. 

A lightweight Preference Control Model (PCM) translates the preference description and current context into weights for combining the next-token predictions of the experts. This approach offers a black-box, parallelizable solution for personalized text generation. Empirical results on Koala and UltraFeedback datasets show that MPD achieves higher pairwise win rates compared to existing preference merging and prompting techniques.

The idea is novel and interesting, with the PCM acting as a orchestra conductor, while the models are like individual players.

### Strengths
* **Novelty:**  MPD introduces the innovative idea of context-dependent, token-level merging of expert LLM outputs, which differentiates it from previous parameter merging techniques.
* **Practicality:** The black-box nature of MPD and its applicability to different architectures make it more practical for real-world scenarios.  The parallelizability and lack of retraining for preference changes are further advantages.
* **Efficiency:** The demonstrated inference speed advantage due to parallelization is a valuable contribution, particularly in contexts where multiple preferences need to be served concurrently.

### Weaknesses
 * **Limited Preference Dimensions and Generalizability:** The selected preference dimensions appear arbitrary and lack sufficient justification. The paper does not adequately address the generalizability of MPD to a more diverse and nuanced range of human preferences. Given the limited number of dimensions explored, it remains unclear how MPD would perform with a substantially larger set, which would be necessary to capture the true complexity of human preferences.

* **Scalability of Preferences and Combinatorial Explosion:** The necessity of enumerating all preference combinations during training introduces a scalability bottleneck. While the paper acknowledges this limitation and briefly touches upon handling new preferences, the proposed approach does not convincingly demonstrate MPD's scalability to a higher-dimensional preference space. The combinatorial explosion inherent in an increasing number of dimensions raises concerns about the feasibility of training MPD with a realistically large preference set.

* **Justification for Tulu-7B and Model Size:** The rationale for selecting Tulu-7B as the base model is insufficiently explained. An evaluation of MPD using more widely adopted, powerful LLMs (e.g., Llama 3, Qwen2.5, Anthropic, GPT, etc,) would significantly strengthen the paper's conclusions. Furthermore, the relatively small size of the tested model (7B) raises questions about the robustness and generalizability of the learned merging strategy. The observed win rates near 50% suggest a limited effect size, potentially attributable to the PCM's capacity.

* **Insufficient Detail on Reward Models and Training:** The paper lacks crucial details about the reward models, including their architecture, training data, and evaluation metrics. This lack of transparency hinders reproducibility and a thorough understanding of the evaluation process. Similarly, essential details about the LoRA training procedure, such as rank, alpha value, batch size, and optimization parameters, are omitted. These hyperparameters can significantly influence the performance and output distribution of LLMs, making their disclosure essential for reproducibility and analysis.

### Questions
* The paper relies on LLM-as-a-judge [2] for evaluation, a methodology known to be susceptible to positionality bias. Could you please talk about whether measures were taken to mitigate this bias, such as comparing both A vs. B and B vs. A, as recommended in prior work such as [1]. This omission raises concerns about the reliability of the reported win rates, (though human evaluation has been conducted as well).
* How does MPD's performance scale with an increasing number of preference dimensions? What strategies are being considered to mitigate the combinatorial explosion of preference combinations during training?
* In comparison to methods that employ smaller LLMs to generate natural language rules for controlling larger models (e.g., [3]), what are the specific advantages of MPD's token-level probability merging approach? Why is this preferable to using freeform natural language rules generated by a smaller LLM to guide a single, more powerful LLM?
* What was the rationale for choosing Tulu-7B as the base model? Have experiments been conducted with other similarly sized LLMs (e.g., Llama 3 8B, Qwen2.5 7B) or larger, more powerful models (Gemini, Llama 70B, Sonnet, etc)? If so, how do the results compare?
* Please provide comprehensive details on the reward models, specifying their architecture, training data, and evaluation metrics. How was the accuracy and calibration of these models ensured?
* Please provide detailed information about the LoRA training procedure for both the expert models and the PCM, including the rank, alpha value, batch size, and other relevant hyperparameters.


[1] https://arxiv.org/abs/2305.14314

[2] https://arxiv.org/abs/2306.05685

[3] https://arxiv.org/abs/2410.03731

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
4

### Summary
The authors propose a method for merging LLM outputs on a per-token level to improve LLM personalization, using an additional control model to control how to combine multiple expert model outputs. The control model is trained via an online RL algorithm (the authors show results with PPO and REBEL). The proposed method outperforms other personalization methods (prompting, souping) based on both llm-as-a-judge and human experiments. Additional ablations justify some design decisions such as merging in the probability space and transforming the reward via a bradley-terry model.

### Strengths
- The core idea is straightforward (merging output probabilities and weighting based on preferences) and the paper does a good job of exploring various design decisions around it (how to train the control model, logits vs probabilities, RL algorithm choice), and is clearly laid-out and written.
- The performance improvements seem robust, with llm-as-a-judge and human evaluation results both suggesting the proposed approach improves over prior work.
- The discussion about inference efficiency is interesting and raises a good point about parameter merging-based approaches, although I think the fact that this method requires a potentially higher memory footprint for inference is a drawback.

### Weaknesses
 - The method has some limitations addressed in the paper: having to train on all preference pairs (which may make scaling to a large number of preferences less feasible), having to retrain the model if new preference types are introduced, and having a larger memory footprint compared to parameter merging methods at inference time.
- Results shown are always winrate over all prompts, which makes it details on where and how the method is improving unclear beyond a handful of qualitative examples. I would be curious if breaking down results per-preference dimension (shown in Table 1) and comparing with baselines would yield any interesting observations - perhaps some methods are better than others at particular preference dimensions?
- Some clarification would be useful around the methods - see my questions below.

### Questions
- Is preference prompting used for the MPD (Uniform) setting (for generating responses)? I don’t quite understand how this could yield better personalization otherwise.
- How many expert models are trained? Is it one per row in Table 1, or one per A/B pair? I found this a bit unclear.
- I am curious about how well an expert-only baseline would do, where we compare just using one of the expert models for generation - do we gain anything by merging the output distributions token-by-token, or does this perform similarly to picking the best output from relevant expert models? 
- It would be interesting to see some analysis on the weights that get chosen by the control model.

### Soundness
3

### Presentation
4

### Contribution
3
