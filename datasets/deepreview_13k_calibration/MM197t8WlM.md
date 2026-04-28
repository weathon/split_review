# Local Flow Matching Generative Models

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6

## Abstract
Flow Matching (FM) is a simulation-free method for learning a continuous and invertible flow to interpolate between two distributions, and in particular to generate data from noise in generative modeling. In this paper, we introduce Local Flow Matching (\lfm{}), which learns a sequence of FM sub-models and each matches a diffusion process up to the time of the step size in the data-to-noise direction. In each step, the two distributions to be interpolated by the sub-model are closer to each other than data vs. noise, and this enables the use of smaller models with faster training. The stepwise structure of \lfm{} is natural to be distilled and different distillation techniques can be adopted to speed up generation. Theoretically, we prove a generation guarantee of the proposed flow model in terms of the $\chi^2$-divergence between the generated and true data distributions. In experiments, we demonstrate the improved training efficiency and competitive generative performance of \lfm{} compared to FM on the unconditional generation of tabular data and image datasets, and also on the conditional generation of robotic manipulation policies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes to divide the original Flow Matching (FM) into a sequence of parts, called Local Flow Matching (LFM). The authors provide theoretical analysis of the convergence of the forward process, and the theoretical guarantee of the $\chi^2$ divergence between the real data and generated data distributions. The authors evaluated the proposed method on different tasks, tabular data generation, image generation, robotic manipulation and so on.

### Strengths
The authors proposed the Local Flow Matching (LFM), which divides the Flow Matching into a sequence of local parts. The approach is intuitively correct. The authors provided theoretical analysis of the convergence of the forward process, showing that the $\chi^2$ divergence between the noise distribution and noised real data distribution decreases exponentially w.r.t. the number of sub-flows. Furthermore, the authors presented the theoretical results showing the $\chi^2$ divergence between the real distribution and the generated distribution is close w.r.t. the flow training loss $\epsilon$.

### Weaknesses
From the experiments, it turns out that the proposed LFM is not working as well as the original Flow Matching (FM) (Lipman et al., 2023). The proposed method achieved an FID of 8.45 on the CIFAR-10 dataset whereas the FM achieved a lower FID of 6.35 on the same dataset. On ImageNet 32x32 dataset, the proposed method achieved an FID of 7.0, but the FM achieved a lower FID of 5.02. The authors should compare with FM on the CIFAR-10, ImageNet 32x32, the Oxford Flowers and the LSUN Church datasets.

The proposed LFM seems to require more training time than the original FM because for training $v_n$ we need to inference from $v_1$ to $v_{n-1}$ for each sample. 

The proposed method also need more inference time since we need to inference from $v_1$ to $v_N$.

### Questions
What does $g \bot x'_l$ mean in Eq. 6? and why do we need this constraint?

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
3

### Summary
This paper presents Local Flow Matching (LFM), an enhancement of Flow Matching (FM) for faster, efficient generative modeling. LFM divides the process into sequential FM sub-models, each bridging distributions that are progressively closer from data to noise, allowing smaller models and quicker training. This stepwise approach also enables the use of distillation techniques to further accelerate data generation. Theoretically, LFM provides a generation guarantee based on $\chi^2$-divergence. Experiments show LFM’s improved training efficiency and strong performance in generating tabular data, images, and robotic manipulation policies.

### Strengths
The paper explores integrating flow-matching submodels into diffusion processes to enable faster and more efficient learning and inference. The approach is novel and is supported by theoretical guarantees of generation. Experimentally, the method can be applied to various tasks, including image generation, tabular data generation, and robotic manipulation.

### Weaknesses
1. More details should be provided, such as the number of function evaluations (NFEs) and the used ODE sampler for all methods in Table 1 and Table 2, to better demonstrate LFM's effectiveness.

2. Although the tasks are diverse, the paper lacks a solid comparison with prior methods on some fundamental tasks. For instance, comparing LFM with Rectified Flow and OU diffusion on CIFAR-10 with the same amount of batches would offer a clearer understanding of LFM's training efficiency and distillation effects.

3. The advantage of LFM on fast training has not been demonstrated well except Table 2.

### Questions
1. Can you clarify more on how the method benefits fast training based on the experimental results?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Local Flow Matching (LFM), a generative approach that builds upon the existing Flow Matching (FM) framework. LFM improves upon FM by dividing the global flow into multiple local flow sub-models. Each sub-model is trained to match a diffusion process between closer intermediate distributions, which reduces the model size and accelerates training.

### Strengths
1.	The paper offers a fresh approach in the field of generative modeling, combining ideas from diffusion processes and FM. The idea of breaking down a single large flow into several smaller steps (local flows) is natural.
2.	The paper provides solid theoretical guarantees, specifically proving a generation guarantee in terms of the $\chi^2$-divergence between the generated and true data distributions. The experiments are comprehensive, covering a range of tasks from image generation to robotic manipulation, and the results demonstrate the performance of LFM.

### Weaknesses
1.	FM simplifies the diffusion process into a single step, transforming a trajectory from a curve into a straight line, thus reducing training costs and improving sampling efficiency. However, this paper reverses that advantage by breaking this single step into multiple segments. The division of the trajectory into multiple steps could introduce added computational complexity, potentially negating the efficiency gains that FM originally aimed to provide. The authors claim that FM does not necessarily yield straight trajectories, but this claim requires more rigorous justification, especially given the theoretical underpinnings of FM which are based on optimal transport. The paper should provide a more detailed analysis of the conditions under which FM trajectories deviate from straight lines and how LFM addresses this issue more effectively.

2.	The paper presents some conceptual ambiguities regarding key terms. Continuous Normalizing Flows (CNF) and neural ODEs are two distinct models, but the paper incorrectly states that "CNF trains a neural ODE" (Line 106). In fact, FM is a method for training CNF models, not a model in itself, much like the proposed LFM method. The paper conflates these concepts in several places (e.g. Line 41, 51), which could cause confusion. The paper needs to clearly distinguish between CNFs, neural ODEs, and the training methods used for them, such as FM and LFM, to avoid further misinterpretations.

3.	The paper highlights improved training efficiency through the use of smaller local models. However, the exact speed improvements are not always well-quantified. For example, while the paper states that LFM leads to faster convergence and reduced memory usage, these claims could be supported by more detailed analysis. Providing concrete timing metrics (e.g., runtime comparisons, memory benchmarks across different hardware) would bolster the argument for LFM's practical benefits. The paper should include a more thorough analysis of the computational costs, including a breakdown of training time per epoch and memory usage for both LFM and FM, under comparable conditions, to substantiate the claimed efficiency gains. More information can be found in Questions part.

4.	In line 127, a reference is used as the subject of the sentence but is enclosed in parentheses. Please correct this formatting issue and ensure consistency throughout the paper.

### Questions
1.	In the training process, at each step, the target distribution is generated from the sample of the previous step through the Ornstein-Uhlenbeck (OU) process. What is the theoretical basis for using the OU process in this context? This essentially defines checkpoints along the probability path. Would a different process yield similar results, or is there a specific reason the OU process was chosen?

2.	In Appendix B1, how were the stepwise parameters $\rho$ and $c$ selected? Were they chosen solely based on extensive experimentation and selecting the ones that gave the best results, or was there a more principled approach to their selection?

3.	In the image generation tasks (Table 2), it would be beneficial to include comparisons with Flow Matching (FM) [1], rather than only with InterFlow, as Local Flow Matching (LFM) is based on FM. This would better illustrate the claimed improved training efficiency. Additionally, either in the main text or in the appendix, it would be helpful to provide a comparison of the total number of parameters for each method across all experiments, rather than only ensuring the same training scheme.

[1] Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, and Matthew Le. Flow matching for generative modeling. In The Eleventh International Conference on Learning Representations, 2023.

### Soundness
2

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
3

### Summary
The paper proposes a novel generative model, Local Flow Matching (LFM), which segments Flow Matching along the time dimension. The transition between two distributions within each time segment is modeled using a smaller-scale sub-model. This generative model offers the advantages of having smaller sub-models, faster convergence during training, and greater convenience for distillation.

### Strengths
The paper provides a detailed theoretical proof that the data distribution generated by LFM is close to the true data distribution, demonstrating the exponential convergence of the forward process and the generation guarantee of the backward process. In addition, the paper conducts extensive experiments to validate the effectiveness of LFM, including generation on two-dimensional toy data, tabular data generation, image generation, and robotic manipulation. Moreover, the paper is well-written.

### Weaknesses
Some experimental details in the paper may need further clarification. The data in Table 2 is used to demonstrate that LFM requires less computational cost, but the model sizes of both LFM and InterFlow are not provided. Additionally, it is unclear whether the training data shown in the table refers to the data used by each sub-model individually or by all sub-models collectively. Specifically, the paper should clarify if the reported training data in Table 2 represents the total dataset size or the size of the dataset used to train each individual sub-model within LFM. This distinction is crucial for understanding the computational efficiency claims. Furthermore, the absence of explicit parameter counts for both LFM's sub-models and the InterFlow model makes it difficult to assess the true computational cost savings. The paper should provide a detailed breakdown of the number of parameters for each sub-model in LFM, the total number of sub-models, and the parameter count of the InterFlow model to allow for a more rigorous comparison.

### Questions
Could you provide more detailed data regarding the issues mentioned in the weaknesses, such as the specific number of parameters for each sub-model in LFM, the number of sub-models, and the parameter count of the InterFlow model (or explain why the total number of parameters across all sub-models is equal to that of InterFlow). Could you provide the amount of data required to train each sub-model?

### Soundness
4

### Presentation
3

### Contribution
3
