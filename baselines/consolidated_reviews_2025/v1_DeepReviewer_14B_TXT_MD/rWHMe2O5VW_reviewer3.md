### Summary

This paper proposes a new approach named Graph ODE with factorized prototypes (GOAT) to address the problem of modeling interacting dynamical systems. The core of GOAT is to incorporate factorized prototypes from contextual knowledge into a continuous graph ODE framework. Specifically, GOAT employs representation disentanglement and system parameters to extract both object-level and system-level contexts from historical trajectories, which allows us to explicitly model their independent influence and thus enhances the generalization capability under system changes. Then, we integrate these disentangled latent representations into a graph ODE model, which determines a combination of various interacting prototypes for enhanced model expressivity. The entire model is optimized using an end-to-end variational inference framework to maximize the likelihood. Extensive experiments in both in-distribution and out-of-distribution settings validate the superiority of GOAT.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-organized and clearly written. 
2. The paper proposes a new approach named Graph ODE with factorized prototypes (GOAT) to address the problem of modeling interacting dynamical systems. The core of GOAT is to incorporate factorized prototypes from contextual knowledge into a continuous graph ODE framework. Specifically, GOAT employs representation disentanglement and system parameters to extract both object-level and system-level contexts from historical trajectories, which allows us to explicitly model their independent influence and thus enhances the generalization capability under system changes. Then, we integrate these disentangled latent representations into a graph ODE model, which determines a combination of various interacting prototypes for enhanced model expressivity. The entire model is optimized using an end-to-end variational inference framework to maximize the likelihood. Extensive experiments in both in-distribution and out-of-distribution settings validate the superiority of GOAT.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not organized clearly. The authors should reorganize the paper to make it more readable.
2. The paper does not have sufficient experimental results to support the claims made in the paper.
3. The paper does not have enough theoretical analysis to support the claims made in the paper.

### Suggestions

The paper's organization needs significant improvement to enhance readability and logical flow. Currently, the structure makes it difficult to follow the core ideas and contributions. For instance, the introduction should clearly articulate the problem being addressed, the limitations of existing methods, and the specific novelty of the proposed GOAT approach. The methodology section should then systematically present the different components of GOAT, such as the factorized prototypes, the graph ODE framework, and the variational inference framework, with clear explanations and justifications for each design choice. The experimental section should be structured to directly address the claims made in the introduction, with a clear description of the datasets, baselines, and evaluation metrics. Finally, the discussion and conclusion should summarize the key findings and their implications, as well as acknowledge the limitations of the work and suggest future research directions. A more structured approach to presenting the material would greatly improve the paper's clarity and impact.

To strengthen the experimental results, the authors should include a more comprehensive set of experiments that directly validate the claims made about the model's performance. Specifically, the paper should include ablation studies to demonstrate the contribution of each component of the GOAT model, such as the factorized prototypes and the disentangled representations. For example, the authors could compare the performance of the full GOAT model with variants that exclude the factorized prototypes or use a different method for disentanglement. Furthermore, the experimental section should include a more diverse set of datasets, including both synthetic and real-world datasets, to demonstrate the generalizability of the proposed approach. The authors should also provide a more detailed analysis of the results, including error analysis and visualizations, to provide a deeper understanding of the model's behavior. This would help to build a stronger case for the effectiveness of the proposed method.

Finally, the paper would benefit from a more rigorous theoretical analysis of the proposed method. While the authors mention the use of a continuous graph ODE framework, they do not provide a detailed analysis of the properties of the proposed model, such as its convergence, stability, and generalization bounds. A theoretical analysis would help to provide a deeper understanding of the model's behavior and its limitations. For example, the authors could analyze the conditions under which the proposed model is guaranteed to converge to a stable solution, or they could derive bounds on the generalization error of the model. This would help to establish a more solid theoretical foundation for the proposed approach and increase its credibility.

### Questions

1. The paper is not organized clearly. The authors should reorganize the paper to make it more readable.
2. The paper does not have sufficient experimental results to support the claims made in the paper.
3. The paper does not have enough theoretical analysis to support the claims made in the paper.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
