## Human Reviewer 1

### Summary
The paper proposed a methodological breakthrough. The first systematic study of RL scaling laws. This paper aims to address a core pain point in the field of RL for LLMs: the lack of a scientific framework capable of predicting how RL performance scales with the investment of computational resources. Focus on the problem of unpredictability, research bottelneck on large-scale experiments and algorithm decision makeing difficulty. It show the system investigation of the RL post-training for LLMs. It introduces the concept of scaling laws from the pre-training domain into RL. Acknowledging that RL performance is bounded. The framework provides a new, quantitative language for evaluating and comparing different RL methods. ScaleRL itself is not a algorithmic invention. Instead, through rigorous empirical study, it combines the most effective existing components from the community. The authors propose a two-pronged solution, establish a predictive computation-performance fitting framework based on a sigmodial curve to model the relationship between reward and computation. Futuremore, propose a best-practice recipe scaleRL integrates a series of technical components.

### Strengths
1. Significant computational cost savings: The framework enables researchers to evaluate the potential of different RL methods using a small computational budget
2. Reduced risk in large-scale training: Using ScaleRL recipe, researcher can better predict the LLM training performance before large training.
3. The provided open-source training recipe on 100,000 GPU hours, which can achieves high performance ceiling, is valuable for community.

### Weaknesses
1. Lack of generalization research. The authors also mention it in paper. It hard to predict the generalization performance. Also the experiments focus mainly on math, it is hard to predict whether the findings can be generalized on more difficult, long horizon task, with different training data mixtures, under different architectures. 
2. It doesn’t proposed the new RL algorithm, but a comprehensive large scale experiments on current existing  most effective algorithms.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper studies how RL post‑training for LLMs scales with compute and proposes a practical recipe, ScaleRL, that is claimed to scale predictably and stably to very large budgets. The central methodological contribution is to fit a sigmoidal compute‑performance curve for pass rate (reward) vs. compute,. Using this framework, the paper ablates many design choices, assembles ScaleRL (PipelineRL with off‑policyness, CISPO loss with truncated IS, prompt‑level loss averaging, batch‑level advantage normalization, FP32 logits, zero‑variance prompt filtering, and "No‑Positive‑Resampling" curriculum), and claims that early‑compute fits extrapolate well to much larger runs. A major  result ofthe paper is that an 8B model trained for 100k GPU‑hours follows the curve predicted from the first 50k GPU‑hours, and that ScaleRL attains a higher fitted asymptote than several contemporary recipes. The paper further explores scaling along axes such as context length, batch size, and model scale (including a 17B×16 MoE), and reports downstream gains on AIME‑25.

### Strengths
I like that the paper reframes RL post‑training through a predictive, saturating scaling law for in‑distribution pass rate vs. compute, and leverages it to make early‑compute forecasts, which is an angle that is underexplored relative to pre‑training scaling laws. Also, the study spans ~400k GPU‑hours of ablations and 100k GPU‑hours long runs, which is unusually extensive for open academic RL studies in LLMs. Additionally, the predictive claim is backed by several "fit‑then‑extend" tests: e.g., fitting up to 8k hours and extrapolating to 16k for LOO runs, and fitting to 50k and matching 100k on the main 8B run. The main recipe of the paper, ScaleRL, seems to be a very stable and practical idea.

### Weaknesses
Limited task breadth and generalization evidence:

Most scaling fits are on verifiable math prompts drawn from Polaris‑53K; downstream evaluation focuses largely on AIME‑25. with some math+code multi‑tasking in the appendix. This leaves open how well the sigmoid fits and the ScaleRL recipe transfer to diverse RL setups (e.g., tool‑use, planning, safety‑constrained tasks, preference‑model rewards). A broader suite (beyond math/code) would strengthen the generality claim.

Compute as "GPU‑hours" conflates sample efficiency and throughput differences:

The x‑axis is GPU‑hours rather than effective tokens / updates / actor‑generated tokens. Because PipelineRL increases hardware utilization, improvements in "compute efficiency" may partially reflect systems throughput rather than intrinsic sample efficiency. Reporting both (hardware time and tokenized data processed) would make cross‑recipe comparisons more interpretable.

Misc. Notes:

I think that the Sigmoid choice is empirically motivated but not stress‑tested against alternatives. I see this as a necessary experiment.

The text sometimes describes “pass rate vs. log(compute)” but plots label compute in GPU‑hours on a log scale.

Some scope of the comparisons is missing. For example, value‑augmented baselines (e.g., VAPO/VC‑PPO‑style methods cited in App. A.1) are not included in the main scaling comparisons

### Questions
Can you report the effective tokens generated/consumed (actor and learner sides) for each method so we can decouple throughput from sample efficiency?

Fig. 3c shows a large asymptote jump from 0.52 to 0.61 with FP32 logits. Can you disentangle numerical‑mismatch reduction from any implicit regularization this might induce (e.g., via more accurate IS ratios)? Ablating only generator or only trainer in FP32 would help.

Did you compare sigmoid to Gompertz/Richards/saturating power‑law fits, and evaluate with AIC/BIC or hold‑out residuals?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
In this paper, the authors provide a comprehensive study of the scaling laws for large-scale distributed RL training. Based on the data collected as a result of this study, they propose and analyze a sigmoidal model, ScaleRL, that reasonably interpolates the training data and, crucially, closely extrapolates to additional points to predict the expected performance given a larger training budget. The authors consider the impact of several design choices when implementing RL, including the loss function, loss aggregation, and fp32 precision for logits. An extensive ablation study illustrates the interplay between several design methods and differentiates between substantial versus marginal impact on the peak performance of the training model. The authors provide several plots that illustrate the impact of a large number of design decisions on the training dynamics and use this data as a means to justify the design decisions that define the ScaleRL recipe to yield the best result.

### Strengths
- This is one of the most extensive large-scale RL studies I've had the pleasure to read. In particular, the ablation study illustrated in Figure 4 really highlights the trade-offs the authors considered during the course of this study.
- Given the emphasis and impact of RL as a key component of modern LLM pre-training this study will be particularly useful for researchers attempting to refine foundational models.
- ScaleRL gives a clear baseline recipe for researchers to use when beginning the RL training process and sheds additional light on how to scale RL and the relationship between several tradeoffs.
- This study provides a useful analogy to the heavily studied scaling laws for pre-training.
- I appreciate the fundamental view that a better understanding of the interplay between existing RL training hyperparameters may be more insightful than proposing yet another loss function or base RL algorithm.
- Comparison with

### Weaknesses
- Because the focus of the paper revolves around the comprehensive study of the different training parameters to consider for RL training it does not propose any novel methods, other than the sigmoidal model produced as a result of the collected data.
- The RL experiments are mainly conducted on a single model with 8B parameters and the model may not fit as closely as the structure and number of parameters are changed. However, this is offset somewhat by the experiments conducted on the larger 17B Llama-4 model and illustrated in Figure 5(b).
- It is still quite difficult to accurately interpret the leave-one-out experiments because of the complex interplay that may exist between several design decisions acting jointly.

### Questions
- Out of curiosity, all the graphs start at 1K total GPU hours. Before that threshold, are the graphs uninformative or too similar to provide any interesting information?

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper establishes a scaling law for RLVR training by running experiments on various RL algorithms with different implementation practices. The scaling law categories two key perspectives, asymptomatic reward gain, which defines the upper bound of the training process, and compute efficiency, which quantifies the performance gain versus used compute in RL training. The scaling law allows for predicting performance after RL training up to 100k GPU hours based on 40k GPU hours. The authors also investigate several practices in RLVR training, including loss aggregation, loss function, advantage normalization, dynamic fitlering, FP32 for policy head. Combining the best practice, the authors provide a recipe named ScaleRL that outperforms baselines in terms of both final performance and training efficiency.

### Strengths
1. The proposed scaling law is shown through extensive experiments.
2. The ScaleRL recipe considers a list of different techniques, which would provide valuable insights to the community.
3. Section 4 on scaling training compute across different axes reveals an interesting conclusion that configurations that are less efficient under limited compute may achieve better results given a larger compute.

### Weaknesses
1. In Sec 4, the large scale experiment on model scale makes a comparison between an 8B dense model and a large 17Bx16 MoE model. It would be better to include model scale experiment on comparing model sizes among dense models,

### Questions
1. Is "400,000 GPU hours" in the intro a typo? According to Figure 1, datapoints up to 100k GPU hours are predicted based on datapoints under 40k GPU hours.
2.  How could the scaling law used in practice? In the LOO experiments, the authors fit the parameters A&B in two ways, one is to fit both parameters simultaneously, while the other one is to fit B with a fixed A. In practice, suppose we run two different trials with different configurations, how to compare the two parameters if both A&B are fitted? Also, if we only fit B with a fixed A, how to determine A before at least one complete trial has been completed?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4