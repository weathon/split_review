### Summary

The authors propose a framework for obtaining space and time continuous physics simulation from partial observations using geometric deep learning. Their method is based on two linked dynamical models that lift sparse observations to dense trajectories. They first learn a latent dynamical system in discrete time domain which is then used to obtain a state estimator in the continuous domain using a transformer-based model. The authors provide theoretical results showing that their method should in principle be superior to previous approaches based on auto-regressive models. They also provide experimental results on three standard datasets in fluid dynamics.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

3 good

### Strengths

1. The authors propose a novel method for obtaining continuous physics simulation from partial observations. The method is based on a double dynamical system formulation and can outperform state-of-the-art methods on three standard datasets in fluid dynamics.
2. The authors provide a theoretical analysis showing that their method has smaller error bounds than previous approaches.
3. The authors provide ablation studies to justify their design choices.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical results are not surprising and follow quite directly from the prior literature. Proposition 1 is a straightforward application of Lipschitz analysis, and while the authors claim that their method of performing forecasting in latent space is novel, similar ideas have been explored in prior works. The analysis in Proposition 2, while using a result from Janny et al., 2022, does not provide significant new insights into the method's behavior or advantages.
2. The authors do not compare their method to the latest state-of-the-art methods. While the authors compare to some earlier methods, it is not clear how their method compares to the latest state-of-the-art methods. For example, the authors do not compare their method to recent methods such as "A Learnable Time-stepper for Data-driven PDE Solvers" and "Learning stable and accurate dynamic physics" which have been shown to achieve superior performance compared to earlier methods such as MGN and DINO. Without a comparison to the latest state-of-the-art methods, it is not clear how the authors' method compares to the current best methods in the literature.
3. The authors do not provide a detailed analysis of their method's performance on different types of PDEs. The authors only provide results on three datasets in fluid dynamics. It is not clear how the authors' method would perform on other types of PDEs such as solid mechanics or electromagnetism. The authors should provide results on a wider range of datasets to demonstrate the generalizability of their method.

### Suggestions

The authors should provide a more detailed comparison to existing methods, particularly those that utilize latent space forecasting for PDE modeling. While the authors claim novelty in their specific approach, the core idea of using a latent space for temporal evolution is not entirely new. A more thorough discussion of the differences and advantages of their method compared to these existing approaches is needed. For example, the authors could compare their method to other latent space time-stepping methods, highlighting the specific architectural choices and theoretical justifications that lead to improved performance. This would strengthen the contribution of the paper by clearly delineating the novel aspects of their approach.

Furthermore, the experimental evaluation needs to be significantly expanded to include comparisons with the most recent state-of-the-art methods. The authors should include results from methods such as "A Learnable Time-stepper for Data-driven PDE Solvers" and "Learning stable and accurate dynamic physics", which have demonstrated superior performance compared to the baselines used in the current study. This would provide a more accurate assessment of the proposed method's performance relative to the current state of the field. Additionally, the authors should provide a more detailed analysis of the computational cost of their method compared to these state-of-the-art baselines. This would help to understand the trade-offs between accuracy and computational efficiency.

Finally, the authors should broaden the scope of their experimental evaluation to include a wider range of PDEs beyond fluid dynamics. The current evaluation is limited to three datasets in fluid dynamics, which does not provide sufficient evidence for the generalizability of the proposed method. The authors should include results on datasets from other domains, such as solid mechanics or electromagnetism, to demonstrate the applicability of their method to different types of physical phenomena. This would significantly strengthen the paper by showing that the method is not limited to a specific type of PDE and can be used to solve a wider range of problems. The authors should also analyze the performance of their method on PDEs with different characteristics, such as different levels of nonlinearity or different boundary conditions.

### Questions

1. Can the authors clarify how their theoretical results differ from previous work? It seems that Proposition 1 is a straightforward application of Lipschitz analysis, and Proposition 2 uses a result from Janny et al., 2022.
2. Can the authors compare their method to the latest state-of-the-art methods, such as "A Learnable Time-stepper for Data-driven PDE Solvers" and "Learning stable and accurate dynamic physics"?
3. Can the authors provide results on a wider range of datasets to demonstrate the generalizability of their method to different types of PDEs?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
