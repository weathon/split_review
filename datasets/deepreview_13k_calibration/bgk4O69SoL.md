# Latent Preference Coding: Aligning Large Language Models via Discrete Latent Codes

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 5, 6, 6

## Abstract
Large language models (LLMs) have achieved remarkable success, yet aligning their generations with human preferences remains a critical challenge. Existing approaches to preference modeling often rely on an explicit or implicit reward function, overlooking the intricate and multifaceted nature of human preferences that may encompass conflicting factors across diverse tasks and populations. To address this limitation, we introduce Latent Preference Coding (LPC), a novel framework that models the implicit factors as well as their combinations behind holistic preferences using discrete latent codes. LPC seamlessly integrates with various offline alignment algorithms, automatically inferring the underlying factors and their importance from data without relying on pre-defined reward functions and hand-crafted combination weights. Extensive experiments on multiple benchmarks demonstrate that LPC consistently improves upon three alignment algorithms (DPO, SimPO, and IPO) using three base models (Mistral-7B, Llama3-8B, and Llama3-Instruct-8B). Furthermore, deeper analysis reveals that the learned latent codes effectively capture the differences in the distribution of human preferences and significantly enhance the robustness of alignment algorithms against noise in data. By providing a unified representation for the multifarious preference factors, LPC paves the way towards developing more robust and versatile alignment techniques for responsible deployment of powerful LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper deals with an important problem in the alignment research: modeling of complex human preferences and proposes a method using latent discrete variables, named LPC, to solve this problem. Authors first conduct extensive objective derivations and further conduct experiments on three alignment methods: DPO, SimPO, and IPO.

### Strengths
1. The mathematical derivation looks fancy.
2. The paper is well-written.
3. The idea of using latent variables for various alignment objectives is intuitive and inspiring.

### Weaknesses
1. Although the mathematical derivation is elegant, but the experimental design and results do not demonstrate that this method is truly effective.
2. This work is like other works in past research in NLP using latent variables, presenting valid theoretical derivations but limited effectiveness, along with questionable robustness and training stability.
3. Although I really like the idea of using latent variables for various alignment objectives modeling, the architecture is too complex and seems unstable. I really worried about the practicability of this method. The authors try to prove the generalization of this method by using it on three alignment methods: DPO, SimPO, and IPO, but it is hard to ignore that the mathematical derivation is necessary for every alignment algorithms that have different alingment objective functions. This significantly undermines the practical applicability of this method. If others want to apply this method to other alignment algorithms, they would first need to perform complex mathematical derivations. Moreover, there is no way to guarantee the correctness of these mathematical derivations for other alignment algorithms.
4. The design of experiements are not good. Choosing to evaluate on the three tasks (commonsense reasoning, mathematical reasoning, truthfulness) are not convincing. I find the experiements fail to verify the effectiveness of LPC on modeling the "COMPLEX" human intentions, especially in the contradicting scenario, e.g., the scenario where we need to guarantee both helpfulness and harmlessness.
5.  The main experimental results in Table 1 are reward scores. However, the paper does not even mention what kind of reward model it is using, let alone any details that can help determine the trustworthiness of the evaluation results. If the reward model chosen in the paper is not reliable at all, the results presented in Table 1 are meaningless.

### Questions
1. Let's first assume the results in Table 1 is reliable. Why are some results of using LPC is much worse than not using LPC? Have you analyzed about this? Any ablation results you can share?

### Soundness
2

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
4

### Summary
This paper addresses the challenge of aligning large language models (LLMs) with complex human preferences that may be conflicting across tasks and populations. The authors propose Latent Preference Coding (LPC), a framework that models implicit preference factors using discrete latent codes without relying on predefined reward functions. LPC integrates with various offline alignment algorithms and infers underlying preferences directly from data. Experiments demonstrate that LPC improves performance across multiple benchmarks and enhances robustness against noisy data, offering a promising approach for more versatile LLM alignment.

### Strengths
1. This paper is well written and easy to follow.
2. This paper have extensive experiments to verify the effectiveness of their proposed method.
3. The idea of using latent code to model complex human preferences is interesting.

### Weaknesses
1. The time computational cost of this method during training process is unclear compared to existing methods like DPO, SimPO.
2. While the idea of learning a prior distribution for latent codes is straightforward and its effectiveness has been demonstrated empirically, it is essential for the authors to further explain how this prior network can capture complex human preferences like from some theoretical proof or previous work.
3. The authors state that the advantages of latent preference coding are mitigating the notorious posterior collapse issue and achieving better interpretability. It would be beneficial to conduct an ablation study using continuous representations to learn human latent preferences.

### Questions
See the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Latent Preference Coding presents an innovative approach that leverages discrete latent variables to model the underlying factors behind human preferences. By implicitly capturing these factors without relying on predefined objective weights or manually defined reward functions, LPC provides a unified framework compatible with various alignment algorithms.

### Strengths
1. The idea behind LPC is interesting. The framework eliminates the need for manually defined reward functions and predefined combination weights, a limitation present in many other methods.
2. Experiments were conducted using three different base models and three alignment algorithms, showcasing LPC’s broad applicability.

### Weaknesses
1. The training settings for the discrete latent space are not clearly specified. Specifically, the dimensionality of the latent variable, the size of the codebook, and the training procedure for the codebook itself are not detailed. This lack of clarity makes it difficult to reproduce the results or understand the sensitivity of the method to these hyperparameters.
2. The TSNE visualization lacks distinct clusters, making it difficult to discern what the latent code has actually learned. Without clear separation between different preference clusters, it's hard to validate the claim that the latent space is effectively capturing distinct preference factors. The visualization should ideally show clear groupings corresponding to different preference types.
3. Table 1 does not include results for MMLU, which is a benchmark on the OpenLLM leaderboard. The absence of this standard benchmark makes it harder to compare the performance of LPC against other methods in the literature.
4. The scores reported in Table 3 are generally low. For example, fine-tuning on Llama3-8B-Instruct using SimPO often yields scores of 20+ as reported in SimPO paper. Could there be differences in settings affecting these results? The low scores raise concerns about the effectiveness of the method or potential issues with the experimental setup.
5. Additional benchmarks, such as MT-Bench or Arena-Hard, would enhance the comprehensiveness of the evaluations. The current evaluation is limited and does not cover a wide range of tasks, making it difficult to assess the generalizability of the approach.

### Questions
1. In Equation (10), is \( h_{x,y} \) at each timestep summed with \( z \)?
2. The purpose of the flipped-label experiment is unclear. Could you clarify how LPC mitigates the significant drop in win rate in such cases? Additionally, how would the results vary if the flip rate were 10% or 90%?

### Soundness
2

### Presentation
2

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
This paper proposes LPC for solving the problem of aligning large language models with human preferences. LPC captures the multifaceted nature of human preferences through the introduced discrete latent variables. In addition, LPC can be integrated with a variety of offline preference algorithms, including DPO, IPO, SimPO, and so on. A unified approach is provided to represent complex preference structures, which in turn enhances the performance of LLMs.

### Strengths
1. The overall framework of the paper is relatively novel, capturing the multifaceted nature of human preferences with the help of discrete latent variables.
2. The constructed LPC framework can seamlessly integrate multiple existing alignment methods with high applicability and scalability.

### Weaknesses
 1. The discussion and analysis of existing work is relatively brief.

2. Generalization ability is unclear: While LPC performs well on noisy data, the validation of its ability to generalize across tasks is more underdeveloped and does not demonstrate its adaptability to a broader range of tasks.

3. Insufficient discussion of LPC complexity: LPC methods' computational cost and implementation complexity in practical applications are not discussed in detail, especially the computational resource requirements for large-scale models.

### Questions
1. How do human preferences and discrete potential coding correspond in the LPC framework? How do we distinguish different preference elements?

2. What is the specific task division between a priori and a posteriori network, and what is the purpose of designing them? How do they operate when there are no preferences? How are the cues designed?

3. What is the performance of LPC in dealing with extreme cases (e.g., extremely noisy data or cases where preference labels are entirely missing)?

### Soundness
3

### Presentation
2

### Contribution
3
