# Accelerate Quantization Aware Training for Diffusion Models with Difficulty-aware Time Allocation

- Decision: Reject
- Scores: 6, 3, 3, 6

## Abstract
Diffusion models have demonstrated remarkable power in various generation tasks. Nevertheless, the large computational cost during inference is a troublesome issue for diffusion models, especially for large pretrained models such as Stable Diffusion. Quantization-aware training (QAT) is an effective method to reduce both memory and time costs for diffusion models while maintaining good performance. However, QAT methods usually suffer from the high cost of retraining the large pretrained model, which restricts the efficient deployment of diffusion models. To alleviate this problem, we propose a framework DFastQ (Diffusion Fast QAT) to accelerate the training of QAT from a difficulty-aware perspective in the timestep dimension. Specifically, we first propose to adaptively identify the difficulties of different timesteps according to the oscillation of their training loss curves. Then we propose a difficulty-aware time allocation module, which aims to dynamically allocate more training time to difficult timesteps to speed up the convergence of QAT. The key component of this is a timestep drop mechanism consisting of a drop probability predictor and a pair of adversarial losses. We conduct a series of experiments on different Stable Diffusion models, quantization settings, and sampling strategies, demonstrating that our method can effectively accelerate QAT by at least 24\% while achieving comparable or even better performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents a new method called DFastQ that makes training diffusion models, like Stable Diffusion, faster and more efficient. This method focuses on how hard different training steps are and adjusts the training time accordingly, giving more time to the harder steps. A key part of this approach is a mechanism that predicts which steps need more attention and uses special losses to help with this training.

### Strengths
The paper introduces the DFastQ framework, which innovatively applies a difficulty-aware perspective to quantization-aware training (QAT). This approach identifies the varying difficulties of different timesteps based on the oscillation of their training loss curves. By dynamically allocating more training time to difficult timesteps and less to easier ones, the method optimizes training efficiency.

The paper introduces a clever timestep drop mechanism that leverages adversarial loss functions to dynamically adjust how training time is allocated based on the difficulty of each timestep. This innovative approach not only improves the training process but also provides a sophisticated way to fine-tune model performance.

The authors provide experimental validation across multiple models and quantization settings, demonstrating the effectiveness of their proposed method. The results show that DFastQ can accelerate QAT by at least 24% while achieving comparable or improved performance metrics, such as FID scores.

### Weaknesses
An in-depth explanation of how the Coefficient of Variation (CV) is computed in practice—specifying the window size and how the loss values are selected—would allow for better reproducibility and understanding of how difficulty is quantified. Specifically, the paper should detail whether the window slides by one step or multiple steps, and how the loss values are aggregated within the window (e.g., mean, median, etc.) before calculating the CV. Furthermore, the paper should clarify if the task loss used for CV calculation is the same across all timesteps or if it's normalized or adjusted differently for each timestep. This level of detail is crucial for others to replicate the method accurately.

It would be valuable to analyze the impact of the difficulty-aware time allocation versus a uniform allocation of training time. Similarly, evaluating the effectiveness of the timestep drop mechanism independently would clarify what aspects of the proposed approach are most beneficial. The paper should include ablation studies that isolate the effects of the dynamic time allocation and the timestep drop mechanism. For instance, a comparison of training with and without the dynamic time allocation, while keeping the drop mechanism constant, would be beneficial. Similarly, the drop mechanism should be evaluated in isolation, perhaps against a uniform drop strategy or a baseline without any drop mechanism.

Expand the description of how the difficulty of timesteps is assessed, particularly the criteria used to define "difficult" versus "easy" timesteps. The current definition based on oscillation is somewhat vague. It would be helpful to provide a more concrete definition, perhaps by specifying a threshold for the CV that distinguishes between difficult and easy timesteps. Additionally, the paper should discuss how the difficulty assessment is affected by different training stages. For example, are timesteps that are initially easy likely to remain easy throughout training, or can their difficulty change over time?

Additionally, provide a more thorough analysis of the computational efficiency gains achieved through the proposed method. While the paper mentions a reduction in training time, it lacks a detailed breakdown of where these gains come from. For example, the paper should quantify the reduction in FLOPs or GPU hours achieved by the proposed method compared to a baseline QAT approach. It should also analyze the overhead introduced by the difficulty assessment and dynamic time allocation mechanisms to provide a complete picture of the computational cost.

### Questions
How to ensure that the difficulty assessment of timesteps remains accurate throughout the training process? Could you provide more details on the frequency and method of updating the difficulty metrics during training?

Can you elaborate on how the timestep drop mechanism affects the overall convergence speed? Specifically, how do you measure the effectiveness of this mechanism compared to traditional QAT approaches?

In Table 1, while you report improved performance and reduced training time, could you provide insights on any potential trade-offs in model quality, especially with different quantization settings?

You tested various quantization bit-widths. Could you provide more detailed findings on how the choice of bit-width impacts both the training time and the final model performance?

### Soundness
3

### Presentation
3

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
This paper aims to speed up the training process of diffusion models. Quantization-aware training (QAT) is introduced to identify the difficulties of different timesteps. Then the training time is dynamically allocated more training time to difficult timesteps. Experiments on various Diffusion models are conducted to demonstrate the ability to accelerate the training process. Overall, the method is intuitive. However, the novelty is limited, and the experiment quality is lower than the bar.

### Strengths
1. Speeding up the training process of the diffusion model is an important research problem.
2. Quantization-aware training is introduced to identify the difficulties of different timesteps in training. Training time is dynamically allocated in different stages.

### Weaknesses
1. The contribution is marginal. Basically, there is only one contribution: identify the difficulties of training with QAT. Identifying different stages [1,2,3] of training is not novel. The core idea of using quantization-aware training to identify difficult timesteps lacks significant novelty, as QAT itself is a well-established technique. The application to diffusion models, while interesting, doesn't represent a substantial conceptual leap. The paper essentially combines two existing ideas without introducing a fundamentally new approach or insight into the underlying mechanisms of diffusion model training.

2. According to the experimental results, there is only a 25% reduction in training time. Is it worth it to introduce such a heavy framework? A simple sampling strategy [4,6, 7] can significantly reduce the training time. The author did not compare a vast majority of works [4,5,6,7] in speeding up the training process of DM. The reported 25% reduction in training time may not justify the complexity of the proposed framework, especially when simpler sampling strategies can achieve comparable or even better results. The overhead of implementing and tuning the QAT-based dynamic allocation might outweigh the benefits, making it less practical than alternative methods. The lack of comparison with other established acceleration techniques further weakens the claim of efficiency.

3. The rationale behind allocating more training time is not clear. While the stages are identified, why not just increase the learning rate? The paper does not provide a clear justification for why allocating more training time to difficult timesteps is superior to simply adjusting the learning rate. It's unclear why the proposed method is more effective than a more straightforward approach, such as a learning rate scheduler that prioritizes difficult timesteps. The absence of a detailed analysis of the effects of different learning rate strategies makes this aspect of the method less convincing.

4. The experiment quality is low. In fact, there is only one model introduced in the experiment: SD-x.x. It is not conclusive at all. More different types of DM are supposed to be experimented with. The experimental validation is limited by the use of a single diffusion model architecture, making it difficult to generalize the findings. The lack of diversity in the models tested raises concerns about the robustness and applicability of the proposed method to other diffusion model architectures. The conclusions drawn from the experiments are therefore not sufficiently supported by the evidence provided.

5. Paper presentation can be improved, e.g., Figure 3, 4, and and 5 are unprofessional.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper concerns acceleration of training or fine-tuning diffusion models (DMs), taken quantization into consideration. Such an approach can produce a good quantized model and full-precision diffusion model. The authors argue that the difficulty associated with time steps in DMs should play important role in convergence and quality of the trained DM. They propose a metric to measure step difficulty, and use this to enforce training more on hard steps. A step predictor is trained to predict difficulty level of each time step, and it can output a probability to sample a step for training. The authors further propose two losses to train the step predictor. The overall loss for training consists of two stages, one for training the quantized model and one for training the step predictor. To evaluate their method, pretrained Stable Diffusions are used to finetune on COCO dataset. EfficientDM is used as the baseline for comparison. The experimental result suggests that the proposed method seems to converge in fewer iterations with less training time and achieve comparable FID-to-FP32.

### Strengths
**Originality:**
- This paper propose to replace uniform step selection in traditional training methods for QAT by difficulty-based selection to train more on difficulty steps. This is reasonable. Difficulty is based on coefficient of variation which measures the occilation level of the loss. 
- The authors then propose to use a neural network to predict probability to select a step for training.

**Quality:** 
The results of finetuning pretrained stable diffusions to produced quantized models are encouraging. Their method can reduce much training time, compared to EfficientDM without LoRA.

**Clarity:**
The writing is quite easy to follow.

**Significance:**
The accelaration in QAT is potentially significant to practical applications.

### Weaknesses
The main weakness of this paper appears to be the mismatch between their model design and experimental setting. 
- In order to better focus on some steps, the authors propose to predict drop probability $p_t$ for each timestep $t$. This probability belongs to [0,1] as discussed in lines 268-269. Those probabilities have a sum up to $M$, which appears in their proposed loss $L_{cons}$. However, in their experiments, $M = 0.6T$ is used and can cause $p_t >1$, since the total number of timesteps $T$ is often large (e.g. 1000). Table 3 even reports with $M=0.8T$. 
- Those probabilities are used to form step selection $q(t) = (1-p_t)/\sum_j (1-p_j)$. A question arises: what it means when choosing such a large bound $M$ on the sum $\sum_j (1- p_j)$ for experiments? It seems that the authors heuristically choose $M$ in their experiments without a reasonable principle. 

Beside, the authors only took EfficientDM as the main baseline, which may limit understanding about significance and applicability of their proposed QAT method.

### Questions
- Can the authors provide some discussion about the mismatch indicated before?
- It is unclear how to count Convergence iteration in their experiments. Can the authors explain more on it? It is very important to make a fair comparison with the baseline. One can think that the less training time may be due to early stopping, and may vanish when using the same number of iterations for those methods.

### Soundness
1

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
This paper focuses on developing an efficient Quantization-Aware Training framework for the approximation and speedup of Diffusion models. The key idea behind the efficiency gains lies behind the realization that not all training timesteps are equal in terms of their impact in the final model quality, and "difficult" timesteps, where there are a lot of oscillations in the loss, are emphasized more in the proposed framework, while "easy" ones are not, thus resulting in the desired speedups.

### Strengths
+ The idea of selectively spending more time on difficult training timesteps cleverly and dynamically allocates the effort where needed.
+ The proposed approach is practical and appears to work well

### Weaknesses
 - Some details are missing from the experimental evaluation (see questions below)

 - How well does the proposed drop predictor perform? Are there any guarantees that it will work well? What would happen to the overall performance if it does not perform well? Does it default to the uniform drop? Or can it be worse?

- In the experimental section it is stated that the same hyperparameters are maintained for all experiments. This statement is short most likely due to space limitations, but it would be important for there to be a short statement in the main body of the paper about stability with respect to hypeparameter choice.

### Questions
- How well does the proposed drop predictor perform? Are there any guarantees that it will work well? What would happen to the overall performance if it does not perform well? Does it default to the uniform drop? Or can it be worse?

- In the experimental section it is stated that the same hyperparameters are maintained for all experiments. This statement is short most likely due to space limitations, but it would be important for there to be a short statement in the main body of the paper about stability with respect to hypeparameter choice.

### Soundness
3

### Presentation
3

### Contribution
3
