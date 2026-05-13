# A Large Recurrent Action Model: xLSTM enables Fast Inference for Robotics Tasks

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
In recent years, there has been a trend in the field of Reinforcement Learning (RL) towards large action models trained offline on large-scale datasets via sequence modeling. 
Existing models are primarily based on the Transformer architecture, which result in powerful agents. However, due to slow inference times, Transformer-based approaches are impractical for real-time applications, such as robotics. 
Recently, modern recurrent architectures, such as xLSTM and Mamba, have been proposed that exhibit parallelization benefits during training similar to the Transformer architecture while offering fast inference. 
In this work, we study the aptitude of these modern recurrent architectures for large action models.
Consequently, we propose a Large Recurrent Action Model (LRAM) with an xLSTM at its core that comes with linear-time inference complexity and natural sequence length extrapolation abilities.
Experiments on 432 tasks from 6 domains show that LRAM compares favorably to Transformers in terms of performance and speed.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a Large Recurrent Action Model (LRAM) that utilizes xLSTM to address the limitations of Transformer-based models, specifically their slow inference times, which make them impractical for real-time applications like robotics. The authors claim that LRAM offers linear-time inference complexity and natural sequence length extrapolation capabilities. They support these claims with experiments across various domains and 432 tasks, demonstrating favorable performance and speed compared to Transformers.

### Strengths
1. The paper provides a thorough experimental evaluation, covering a wide range of domains and tasks, including common RL benchmarks (Atari, DMControl, etc), robotics simulation environments, and generalization benchmarks.
2. The empirical studies on these benchmarks, especially the comparison between Transformer-based models and LSTM-based models, have brought some useful practices to the community.

### Weaknesses
1. From current status,  the contribution of this paper may be limited. I appreciate the comprehensive experiments in this paper, while the use of xLSTM for faster inference is not surprising, as LSTM-based models are typically faster than Transformer-based models.
2. I think it would be better if the paper discuss when and why to use LSTM-based models versus Transformer-based models. If the primary goal is to improve the inference speed of Transformers, there are already several engineering solutions, such as FlashAttention, that can significantly accelerate Transformer inference.
3. From Figure 6, it appears that the inference speed of Decision Transformers (DT) is acceptable when the batch size (B) is 1, which suggests that the need for an alternative model might be less urgent in some scenarios. As far as I known, in real-world applications, most robotics models perform inference at batch size 1. I suggest the authors do some investigation into scenarios where LSTM-based models are most beneficial.
4.I did some comparative experiments between Transformer and LSTMs architectures. My own visualization experiments suggest that Transformers and LSTMs have different focus points. Transformers tend to have longer memory, while LSTMs often focus on recent states. For more challenging tasks, such as those with sparse rewards, Transformer-based models may perform better due to their ability to handle long-term dependencies, which is consistent to the original DT paper. Maybe the authors could do some similar visualization experiments to investigate the difference among vanilla LSTM, xLSTM and Transformers on sparse and dense reward tasks, respectively.

### Questions
I suggest the authors provide a more detailed comparison with other recurrent architectures and explain why xLSTM is a superior choice for this specific application. Additionally, the authors may offer more insights into the trade-offs between LSTM-based and Transformer-based models, and under what conditions each is more suitable.
This may not be a question, but I think it will be valuable to the community if the paper can further investigate the above point.

### Soundness
3

### Presentation
3

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
This paper conducts a comprehensive empirical study on architectural choices for sequence modeling in offline reinforcement learning. The results show that xLSTM models scale effectively with training tasks and data, outperforming transformers and mamba in both policy performance and inference speed.

### Strengths
* The empirical evaluation is thorough and extensive. THe paper also provides rich experimental details in appendix, providing valuable comparisons across different architectures.
* The release of the data pipeline and dataset can be a useful resource for the community.

### Weaknesses
 * The paper is built upon the decision transformer approach to offline RL. However, this approach is not widely used in the recent recent developments of large-scale embodied or robotic foundation models. To show that xLSTM is a competative architecture, it would be important to validate its advantages for other learning approaches, e.g., generative behavior cloning.
* The ablation study examines the influence of context length, both including and excluding action; however, it looks that even without actions, all choices of context length converge to similar performance. This result goes against the necessity of using xLSTM or other forms of recurrent models. It would be good to more clearly justify when xLSTM could benefit from extended history. 
* In terms of specific architecture designs, the paper considers xLSTM [7:1] and [1:0]. However, the rationale behind these choices is unclear. Moreover, the results look puzzling: the former works better in atari, while the latter works better in procgen. Providing deeper insight into these choices would strengthen the paper.

* In line 380, the authors note `While removing actions improves performance on the robotics domains, it does not affect performance on discrete control. We assume this is because ... by observing previous actions, the agent learns shortcut`. To verify this explanation, could you provide correlation metrics between sequeantial actions in robotic vs discrete tasks, similar to Fig 3 in [1]?

### Questions
In line 380, the authors note `While removing actions improves performance on the robotics domains, it does not affect performance on discrete control. We assume this is because ... by observing previous actions, the agent learns shortcut`.

To verify this explanation, could you provide correlation metrics between sequeantial actions in robotic vs discrete tasks, similar to Fig 3 in [1]?

[1] Fighting Copycat Agents in Behavioral Cloning from Observation Histories, NeurIPS 2020

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
This paper explores the application of a recurrent model (xLSTM) in robotic policy learning, introducing a novel approach called the Large Recurrent Action Model (LRAM), which enhances inference efficiency. In comparison to conventional sequential models used in Offline RL, such as the Decision Transformer, LRAM demonstrates superior performance on tasks within the Procgen and DMControl environments, while achieving competitive results on other benchmarks like Meta-World, Atari, MimicGen, and Composuite. Notably, LRAM benefits from significantly higher throughput, presenting a distinct advantage. Comprehensive experiments and ablation studies highlight the effectiveness of LRAM, incorporating xLSTM or Mamba as its core, showing favorable evaluation performance across various model scales when compared to Transformer-based approaches.

### Strengths
1. The paper is well-written and organized, making it easy to follow.

2. The reviewer appreciates the solid and robust experiments across diverse benchmarks, including thorough ablation studies on context length and action token.

3. Analysis provided in Section 4.3 makes the paper an insightful and valuable study, which may benefit the community.

4. The inclusion of detailed explanations for dataset preparation and training processes is appreciated.

### Weaknesses
The reviewer believes the following aspects can be further improved:

1. The authors are encouraged to discuss the key differences between xLSTM, Mamba, and a typical transformer (such as GPT-2) used in the Decision Transformer.

2. It would be better if the authors could present the normalized performance of the offline datasets (ground truth) presented in Figure 2b.

**Minor**

1. The bottom border of Table 5 is missing.

2. In Lines 1282-1283, the scientific notation should be written as $1e-4$ instead of $1e^{-4}$

### Questions
1. How does the ratio of mLSTM to sLSTM blocks impact performance? Could you provide further observations on specific configurations, such as xLSTM[3:1]?

2. As a follow-up, what would happen if Transformer layers in DT were gradually replaced with sLSTM or mLSTM layers?

3. Could you elaborate on the visual encoder referenced in Lines 186-187? Specifically, is it jointly trained with the downstream policy, and how is it initialized?

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
This paper investigates recurrent architectures for large action models that enable efficient inference. It proposes the Large Recurrent Action Model (LRAM), featuring an xLSTM core, which achieves linear-time inference complexity and supports natural extrapolation to longer sequence lengths. Experiments conducted on 432 tasks across six domains demonstrate that LRAM performs competitively with Transformers, offering advantages in both speed and performance.

### Strengths
1. The paper is well-written and easy-to-read.
2. The study compiles 894 million transitions and conducts experiments across 432 tasks in six domains, demonstrating a substantial research effort.

### Weaknesses
1. There is a lack of analysis regarding certain experimental observations. Specifically, an explanation for the lower performance of the Decision Transformer (DT) compared to recurrent-based agents would be valuable, especially since DT has more parameters, which, according to scaling laws, would be expected to yield higher performance.
2. Additionally, I am interested in understanding why xLSTM outperforms Mamba, as both architectures are designed for linear-time inference complexity. In Line 300, what is meant by "This is an important advantage of xLSTM, as LRAM agents can strongly benefit from more data and consequently larger models"?
3. It would enhance clarity to make key findings more prominent, as in DeMa [1], which also investigates the benefits of integrating Mamba within sequence modeling frameworks.

### Questions
1. Why is only xLSTM mentioned as the core of LRAM in the abstract and introduction? The authors also indicate that both xLSTM and Mamba provide parallelization benefits during training similar to the Transformer architecture while enabling faster inference.
2. How is the shared action head used across all environments, given that each environment may have a different output dimension and that continuous actions require discretization?
3. In Figure 2(b), should the performance of different environments be weighted according to the number of tasks in each environment to prevent any single environment from disproportionately influencing the results? For example, only in ProcGen, xLSTM [1:0] appears to show a distinct advantage.
4. Why did the authors choose to place the results of fine-tuning in Section 4.3 in the appendix, considering that there is still space to present these results in the main paper?
5. I am interested in the training details for multi-task training. With 432 tasks, could the learning curve be affected by conflicting gradients inherent to multi-task learning?
6. In Section 4.4, the authors investigate inference time within a simulation environment. However, during inference, it is common to set $B=1$, where the latency of DT and xLSTM is comparable. A notable difference in inference time only appears when $B=16$. Given this, is the use of xLSTM truly necessary?

### Soundness
2

### Presentation
3

### Contribution
3
