# REGENT: A Retrieval-Augmented Generalist Agent That Can Act In-Context in New Environments

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 5, 8

## Abstract
Building generalist agents that can rapidly adapt to new environments is a key challenge for deploying AI in the digital and real worlds. Is scaling current agent architectures the most effective way to build generalist agents? We propose a novel approach to pre-train relatively small policies on relatively small datasets and adapt them to unseen environments via in-context learning, without any finetuning. Our key idea is that retrieval offers a powerful bias for fast adaptation. Indeed, we demonstrate that even a simple retrieval-based 1-nearest neighbor agent offers a surprisingly strong baseline for today's state-of-the-art generalist agents. From this starting point, we construct a semi-parametric agent, \texttt{REGENT}, that trains a transformer-based policy on sequences of queries and retrieved neighbors. \texttt{REGENT} can generalize to unseen robotics and game-playing environments via retrieval augmentation and in-context learning, achieving this with up to 3x fewer parameters and up to an order-of-magnitude fewer pre-training datapoints, significantly outperforming today's state-of-the-art generalist agents.
Website: \website{} % Uncomment for arxiv and camera-ready version

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces REGENT, a retrieval-augmented generalist agent designed to adapt to unseen environments without finetuning. It leverages in-context learning and achieves significant generalization across different environments, including robotics and game-playing. It proposed a retrieve-and-play method and incorporated a transformer-based policy to train on sequences of queries and retrieved neighbors.

### Strengths
1. The work is well-organized and easy to follow.
2. The observation that the simple retrieve-and-play method can match or surpass the performance of state-of-the-art generalist agents in unseen environments is interesting.

### Weaknesses
1. This paper uses nearest neighbor retrieval, claiming it is effective for small training datasets. Yet, they use transformer architecture, known as data hungry. These contradict each other. To prove that nearest neighbor retrieval is indeed effective, it should also be compared to other retrieval methods. Specifically, the paper should explore the impact of different distance metrics (e.g., cosine similarity, Euclidean distance in embedding space) and retrieval sizes (k-NN with varying k values) on the final performance. The current analysis lacks a thorough investigation into the sensitivity of the retrieval mechanism.
2. There are some places that the author overclaims:

- The author claims multiple times that Gato "struggles to achieve transfer to an unseen Atari game even after finetuning, irrespective of the pretraining data". Note that in Section 5.2 and Figure 9, Gato did a comprehensive study to show that they can transfer to new tasks with few demonstrations. The claim that Gato struggles irrespective of pretraining data is not accurate, as the original paper demonstrates transfer with sufficient pretraining and finetuning.

- The author claims that their model has the ability to adapt to new tasks via in-context learning. However, the ICL refers to a model's capacity to learn and perform tasks by observing examples "without requiring additional training." The LLM can do ICL **without training via RAG**. This is conceptually different from what the author claimed ICL in their paper. The authors should clarify that their method is learning to perform in-context learning, rather than directly performing ICL as typically understood.

- The author claims that methods like decision transformers cannot generalize to new goals caused by changes in visual observation/available control/game dynamics. Nevertheless, the experimental setting in this paper is simple: the simulation benchmark, like Metaworld, does not involve many visual changes between different tasks. To verify that the REGENT can indeed handle these environmental changes, it is recommended that a real robot experiment be conducted, as Gato does in their paper. The current experiments do not sufficiently demonstrate the robustness of the method to significant visual and dynamic changes.

3. Why is JAT/Gato finetuned on new demonstrations, as it is already trained by all data, such as 50 tasks in MetaWorld? This seems to make JAT/Gato overfitting on the target dataset, thus performing extremely badly in experiments in Figure 4. The comparisons are not fair, and the author should provide proper reasons and compare them with the vanilla JAT/Gato. The paper needs to clarify the training procedure for JAT/Gato and justify the finetuning process, as it appears to disadvantage the baseline.

4. Missing highly-related reference [1,2].

### Questions
Please see weaknesses part.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a method that pre-trained on diverse demonstrations across different environments and tasks that can be adapted to unseen environments via in-context learning, with very few expert demonstrations, and without any fine-tuning. The method is a semi-parametric model that leverages a simple retrieval-based 1-nearest neighbor agent and in-context learning based on other retrieved neighbors to generalize to unseen robotics and game-playing environments. The authors show that their approach is more sample-efficient and parameter-efficient than strong baselines such as Gato.

### Strengths
+ This paper proposes a novel and interesting idea of combining a 1-nearest neighbor agent with a Transformer pre-trained to perform in-context learning from retrieved N-nearest neighbor demos. This approach seems to work well for both the Gato setup and the ProcGen setup regarding generalization over unseen environments for robotics or game-playing tasks.
+ The results of the simple 1-nearest neighbor agent show that it serves as a surprisingly strong baseline, which provides insights for solving tasks in the unseen environment.

### Weaknesses
 + The paper will be stronger if its experiments are also performed on a larger set of manipulation tasks (ManiSkill2, RLBench, etc.)

### Questions
+ I am curious what are the results of REGENT without the help of the 1-nearest neighbor agent.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes REGENT, a retrieval-augmented generalist agent that can adapt to new environments without fine-tuning. REGENT can outperform other RL  agents with fewer parameters in two settings.

### Strengths
1. The methodology is well-explained and easy to understand.

2. REGENT demonstrates better performance than larger models (JAT/Gato) with fewer parameters across multiple environment types.

### Weaknesses
1. Limited Comparison Scope:

While the paper draws inspiration from retrieval-augmented generation (RAG) in language models, it lacks comparisons with recent LM embodied agents that use retrieval-augmented methods. Some existing work:
- https://arxiv.org/abs/2308.10144
- https://arxiv.org/abs/2402.03610

2. Insufficient Ablation Studies, some valuable ablations could have included:
- Analyzing performance w/wo image information in the context
- Testing various context sizes
 - Analyzing the REGENT's inference latency per state is crucial for real-world deployment. Given the retrieval mechanism and context processing at each step, runtime performance analysis would be valuable for assessing practical applicability


3. Training Data Requirements:

While REGENT shows improved data efficiency compared to baselines like JAT/Gato, it still requires substantial pretraining data across different embodied settings (14.5M transitions in JAT/Gato setting, 12M in ProcGen). This raises questions about its true few-shot learning capabilities and practical applicability in scenarios where large-scale demonstration data is unavailable across task families.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work proposes to leverage retrieval augmentation to reduce the amount of training data required for training generalist agents.
The authors introduce $\texttt{REGENT}$, a retrieval-augmented architecture that incorporates a non-parametric retrieval component (R&P) with learning of a parametric policy.
Further, they demonstrate theoretical guarantees for performance with respect to the number of expert demonstrations.
They pre-train $\texttt{REGENT}$ on 4 different domains and evaluate on unseen levels and holdout tasks, where it exhibits strong performance compared to baselines.

### Strengths
The authors provide theoretical guarantees for performance with respect to the number of demonstrations.

$\texttt{REGENT}$ is a novel architecture that effectively incorporates retrieval augmentation for imitation learning.

Retrieval augmentation enables training on much less data than other generalist agents.

The authors demonstrate the promise of retrieval augmentation for unseen levels and tasks.

### Weaknesses
 **Significance of results:**

The authors only provide averages in all figures (except for Figure 7), but no variance estimates. How do those look? Are the results on the unseen tasks statistically significant?

The authors claim that $\texttt{REGENT}$ outperforms JAT even after fine-tuning, but there is little information about the fine-tuning protocol, i.e. what fine-tuning technique is used, etc. Therefore it is difficult to determine the significance of the results. Can the authors elaborate a on this?
Also there are fine-tuning techniques specifically designed for few-shot learning, which may be more suitable in this setting [1,2].

On unseen levels of ProcGen the authors only compare $\texttt{REGENT}$ to R&P, but no results for MTT, why is this the case?
BC is a very weak baseline for training from scratch. The authors should compare to other more recent imitation learning techniques [3,4,5] that use the same amount of expert demonstrations as $\texttt{REGENT}$. This would shed light on the significance of the reported results.

Another interesting experiment would be zero-shot evaluation without having expert demonstrations on the unseen tasks. If $\texttt{REGENT}$ performs well in this scenario, this would greatly strengthen the paper.

There is a lack of ablation studies, for example performance on varying the number of examples in the context and ablation on different distance metrics.

Finally, it is not really clear why the authors differentiate between the two different settings. Why not include ProcGen in the first setting?
Why are different baselines used for the different settings? MTT could also be applied to the first setting, right?
At least having a fixed set of all baselines across both settings would strengthen the paper.

**Limitations and claims**

- The authors claim that deployment on unseen tasks is instantaneously, this is not true though, as deployment in an unseen environment requires collection of expert demonstrations which in turn requires training of an expert policy. This should be made more explicit as a limitation of the proposed method.
- Moreover, claims on "handful of examples" should be caveated as thousands of samples are not a handful.
- Authors claim apples-to-apples comparison between JAT and $\texttt{REGENT}$ when being trained on the same amount of data. This is not apples-to-apples though as $\texttt{REGENT}$ uses expert demonstrations of the unseen tasks. The more fair comparison is to fine-tuning JAT.
- Further, the work would benefit from a bit more accurate positioning on the landscape of methods that do or do not rely on demonstrations. This is an important aspect, as there are approaches that aim at leveraging in-context learning in the context of learning-to-learn as in meta-learning [6]. Examples are [7,8], where the latter also relies on retrieval augmentation. 

**Presentation:**

Presentation can be improved, in particular:

* Eq. 1 & 2: $c_t$ is provided as input to the policy, but it is never used, it is only used in Eq. 3, as R&P does not rely on context information
* Figure 3: enumeration in caption, but not in figure, either remove them in caption or add in figure
* Paragraph on $\texttt{REGENT}$ architecture is not really clear as the reader does not have an overview what modalities are represented in the training data, therefore the choice of encodings seem arbitrary.
* Theorem 5.2: $\boldsymbol{H}$ represents the horizon, right? In section 3 it is not boldface, this should be consistent.
* Figure 8: hard to follow what actions are "good" or "bad" as there is no explanation for the action index

### Questions
- Why is the scaling factor for MixedReLU set to 10? This seems like an arbitrary choice, why not remove it entirely?
- Does the number of demonstrations for MTT on ProcGen match the number of demonstrations for $\texttt{REGENT}$?
- Is it always the case that $\texttt{REGENT}$ only receives the current query state in its context? Have you tried providing more sequential information?
- What ProcGen mode is being used? Easy or hard?
- How important is the ordering in the context of $\texttt{REGENT}$? Did you try permuting the order?
- In Figure 15 in Appendix D not all curves show improvement for using more demonstrations, do the authors have an intuition why this is the case?
- From Figures 11, 12, 13, 14 it can be seen that JAT is particularly good on BabyAI, but not good on other domains, while $\texttt{REGENT}$ is very good at Metaworld. Do the authors have an intuition why this is the case?

### Soundness
3

### Presentation
2

### Contribution
3
