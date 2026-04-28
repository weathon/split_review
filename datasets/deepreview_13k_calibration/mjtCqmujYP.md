# Reward-Augmented Data Enhances Direct Preference Alignment of LLMs

- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 6, 6, 3, 5

## Abstract
Preference alignment in Large Language Models (LLMs) has significantly improved their ability to adhere to human instructions and intentions. However, existing direct alignment algorithms primarily focus on relative preferences and often overlook the qualitative aspects of responses, despite having access to preference data that includes reward scores from judge models during AI feedback. Striving to maximize the implicit reward gap between the chosen and the slightly inferior rejected responses can cause overfitting and unnecessary unlearning of the high-quality rejected responses. The unawareness of the reward scores also drives the LLM to indiscriminately favor the low-quality chosen responses and fail to generalize to responses with the highest rewards, which are sparse in data. To overcome these shortcomings, our study introduces reward-conditioned LLM policies that discern and learn from the entire spectrum of response quality within the dataset, helping extrapolate to more optimal regions. We propose an effective yet simple data relabeling method that conditions the preference pairs on quality scores to construct a reward-augmented dataset. This dataset is easily integrated with existing direct alignment algorithms and is applicable to any preference dataset. The experimental results across instruction-following benchmarks including AlpacaEval 2.0, MT-Bench, and Arena-Hard-Auto demonstrate that our approach consistently boosts the performance of DPO by a considerable margin across diverse models such as Zephyr, Mistral, Qwen2, Llama3.1, Gemma2, and SPPO. Additionally, on six academic benchmarks including GSM8K, GPQA, MUSR, TruthfulQA, BBH, and ARC, our method improves their average accuracy. When applying our method to on-policy data, the resulting DPO model outperforms various baselines and achieves state-of-the-art results on AlpacaEval 2.0. Through comprehensive ablation studies, we demonstrate that our method not only maximizes the utility of preference data but also mitigates the issue of unlearning, demonstrating its broad effectiveness beyond mere dataset expansion.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel method to enhance the direct preference alignment of Large Language Models (LLMs) by incorporating reward-augmented data. The authors identify limitations in existing direct alignment algorithms, such as overfitting and unlearning of high-quality rejected responses, and propose a reward-conditioned policy to address these issues. The method involves a simple data relabeling technique that conditions preference pairs on quality scores, creating a reward-augmented dataset. This approach is shown to improve the performance of various models across multiple benchmarks, including instruction-following and academic benchmarks.

### Strengths
- The paper presents a creative solution to the problem of overfitting and unlearning in direct preference alignment by introducing reward-conditioned policies. This approach is novel and extends the capabilities of existing alignment algorithms.
- The experimental results demonstrate significant performance improvements across a range of models and benchmarks. The comprehensive ablation studies further validate the effectiveness of the proposed method.
- The proposed method has broad implications for improving the alignment of LLMs with human preferences, which is a critical area of research for developing more reliable and user-friendly AI systems.

### Weaknesses
 - While the method is innovative, it builds heavily on existing direct preference alignment algorithms.
- The experiments are extensive but primarily focus on instruction-following and academic benchmarks. Including additional real-world applications, diverse datasets could strengthen the generalizability claims.

### Questions
- What are the benefits of keeping the rejected high-reward samples? Can the author provide evidence for consequential effects of the unlearning problem when LLM finetuned with the original DPO? The authors might need to start with a model that is not DPO fine-tuned and start to fine-tune using DPO and the proposed method.
- How does the proposed method compare with other recent advancements in preference alignment, such as those using model-based reinforcement learning or other reward-based approaches?
- Can the authors analyze which are rejected but high-reward samples in human feedback cases? Are they actually beneficial?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes augmenting reward modeling datasets with goal-conditioning. In this setting, one requests a response that has a particular reward score and assigns a binary label as to whether or not the datapoint achieves that score. Extensive experiments show that doing so improves the win rate and other capability-related evaluations of the model over relevant baselines.

### Strengths
The empirical results in Section 6 are comprehensive across different capability and alignment evaluations as well as different models. The trends in the results are fairly consistent across settings, I think. The method itself is computationally efficient and simple to implement.

### Weaknesses
1. I am confused about Tables 1 and 2. How did you compute $\pi^*$? What are the assumptions used? If you assume a standard setting like the DPO paper, you would never get a policy that always generates one response over the other (because Bradley-Terry inherently assumes some noise). Also, just more realistically, LLMs are softmax parametrized, and the probability of a response can never be exactly 0. Overall, I am confused about Section 3.1, where, for example, "reward sparsity" is used to describe something different than what it traditionally means (sparsity over trajectory time, not over the dataset) and the logic is unclear. This makes the motivation for the algorithm unclear -- Section 3.2 is titled way too strongly for a method that has no clear theoretical backing. This weakness is the reason for giving a 6 instead of an 8. It is hard to justify accepting a paper with such vague and possibly incorrect text, even if the idea and method are performant.

2. I don't understand the method. All datapoints have only a binary indicator that one response was preferred over the other. So how are you determining the value of $r_w^i$ and $r_l^i$? Without some additional information, they would all be the same. 

3. I think the accuracy of the reward model matters a lot, and PairRM and ArmoRM are both pretty good reward models from my understanding. It might be better to do a more stark separation where eg one flips the ArmoRM score and sees what happens. I think this would be interesting, since LMs usually don't use the context in the way that we expect them to.

Minor: I would not use "unlearning" as a term to describe the phenomenon since that has a very different meaning in ML literature.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses fundamental limitations in direct preference alignment algorithms that use binary preference data, where models tend to unnecessarily unlearn high-quality rejected responses while indiscriminately learning low-quality chosen ones. The authors propose a simple reward-augmented data relabeling method that conditions the training data on explicit quality scores, which allows models to learn patterns across the full quality spectrum. This approach is orthogonal to existing direct alignment algorithms and can be applied with any direct preference algorithm.

### Strengths
1. The method is straightforward to implement, requires no architectural changes, and can be easily integrated with existing alignment algorithms.

2. The method is versatile since it works with both offline and online preference data and can handle multi-dimensional reward attributes.

### Weaknesses
1.  While the paper uses a 1-10 scale, there's no analysis of how different scoring scales (e.g., 1-5, 1-100) might affect performance or what the optimal scale might be. It is unclear if the method's effectiveness is sensitive to the granularity of the reward signal, and whether a more fine-grained or coarse-grained scale would yield better results. The choice of a 1-10 scale appears arbitrary without justification.

2. The paper does not include human evaluation studies to validate the effectiveness of reward-augmented responses. The reliance on automated metrics, particularly those using LLMs as judges, may not accurately reflect real-world performance or human preferences. It is crucial to assess if the improvements observed translate to genuine improvements in response quality as perceived by humans.

3. The paper would benefit from a discussion of limitations and potential future directions. The current discussion lacks a critical analysis of the method's shortcomings, such as its potential sensitivity to the quality of the reward signal or its applicability to different types of tasks. A more thorough discussion of these limitations would provide a more balanced view of the method's strengths and weaknesses.

### Questions
What led to choosing the 1-10 scale for quality scores, and have you explored whether other scoring ranges might be more effective for reward conditioning?

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
This paper tackles the limitations of direct alignment in LLMs by introducing reward-conditioned policies. The authors propose a data relabeling method that incorporates reward goals into preference datasets, allowing the model to learn from both high- and low-quality responses. By conditioning on the highest reward at inference, the approach enhances LLM performance across benchmarks, improving alignment and reducing overfitting.

### Strengths
This paper presents a novel approach to preference alignment in LLMs by introducing reward-conditioned policies. The method enhances model performance by conditioning on reward values, enabling LLMs to better generalize to high-quality responses and mitigate the unlearning Issue.

### Weaknesses
1. The method relies heavily on reward labels, whether in directly constructing the reward-augmented dataset or through a multi-attribute rewards dataset. The actual impact of these rewards on data quality remains unexplored. It is unclear if the model would benefit more from high-reward rejected answers than from low-reward chosen answers, which warrants further investigation.
2. Learning from preference usually involves guiding the model towards specific output styles, such as aligning to certain type of instructions or adapting to varied language tones. The authors used previously unseen instructions in DPO training that match existing data, potentially limiting the model's adaptability. The experimental results require additional examples and detailed explanations to clarify this impact. And in appendix $D_N^i$ training prompts should be added.
3. The authors’ setup inadequately considers response scores (rewards), despite splitting the augmented dataset into two categories, $r_w^i$ and $r_l^i$. The rationale categorization of additional quality dimensions should further considered beyond binary labels.
4. The proposed approach and insights lack a strong foundation. Restructuring the dataset (new pairs) based on reward intuitively seems more effective. In contrast, positive and negative goal-conditioned learning does not necessarily ensure that higher-quality responses receive more attention.
5. The formatting in line 200 contains typographical errors. $r_{g = r_l^i}(x, y_w^i) = 0$.

### Questions
1. How does the reliance on reward labels impact the overall data quality, and would the model benefit more from incorporating high-reward rejected responses compared to low-reward chosen ones?
2. How does the use of previously unseen instructions in DPO training affect the model's adaptability, and could additional examples or detailed explanations enhance the clarity of the experimental results?
3. Could the authors further justify the categorization of responses beyond binary labels, and would explain how positive and negative goal-conditioned learning enhances attention of data with varying quality.

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
This paper proposes a method for learning from a reward-augmented preference dataset. The method is straightforward. During training, the LLM is prompted with a special text like "Generate a response of reward 5". If such a prompt is given, only the response that has reward 5 is preferred during DPO training, the other response (even it has a higher reward) is considered as dispreferred one. This allows us not only to learn from preferred response data but also learn from the suboptimal response. This also allows the leverage of quantitative reward values. Exps is conducted on reward datasets like UltraFeedback, and show improvement over the DPO method.

### Strengths
1. The proposed method is straightforward and easy to understand.
2. Experiments show that the proposed method outperforms DPO on multiple base models and various benchmarks.
3. The algorithm can somewhat mitigate the unlearning problem of DPO, which might be useful.

### Weaknesses
1. **Conditioning on low reward data is only empirically useful.** Despite improvements indicated by the experiments, I find the method to be highly empirical and lacks theoretical guarantees. During sampling, the LLM is always prompted to generate only high-reward responses, which makes learning low-reward prompts during training useful only because it proves "generalization". The method's reliance on specific reward values during training, without a clear theoretical underpinning, raises concerns about its robustness and general applicability. It is unclear why learning to generate low-reward responses would improve performance when the goal is to generate high-reward responses. The paper lacks a detailed analysis of how this training strategy affects the model's internal representations and its ability to generalize to unseen scenarios.

2. **Lack of comparison with other reward-augmented methods**. One main claimed contribution of the paper is being able to learn from quantitative rewards, but it did not compare with any reward-augmented methods. Related prior works are 

Noise Contrastive Alignment of Language Models with Explicit Rewards   https://arxiv.org/abs/2402.05369

Ulma: Unified language model alignment with demonstration and point-wise human preference https://arxiv.org/abs/2312.02554

3. **Reward labels can be extremely noisy.**  In the experiments, all datasets use GPT-4 generated reward, which is much more deterministic than human reward. Preference learning exactly tries to avoid noises in human evaluations and only considers preference order. If the dataset reward is given by a human instead of GPT4. One response can be of multiple rewards according to different annotators. So it is unreasonable when you prompt the LLM to generate a response of reward 9, the response of reward 10 is "dispreferred". This approach seems particularly vulnerable to the inherent subjectivity and variability in human reward assignments, which could lead to inconsistent or even detrimental training signals. The paper does not adequately address the potential impact of noisy reward labels on the model's learning process.

4. **Reward values are continuous.** The method conditioned the LLM on a specific given reward value. However, since the reward signal is an inherently continuous value, it is not very suitable for use as the condition. "Generate a response of reward 3.75" does not make much sense, compared with "Generate a response that is truthful/contains no mathematic mistakes (some deterministic requirement)"

### Questions
Above

### Soundness
3

### Presentation
2

### Contribution
2
