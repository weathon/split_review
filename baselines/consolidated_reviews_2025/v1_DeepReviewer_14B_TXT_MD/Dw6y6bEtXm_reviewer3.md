### Summary

This paper proposes a new framework called Physics-Informed Coarse-grained data Learning (PICL) to incorporate physics information via the learnable fine-grained state representation from coarse-grained data. The PICL framework comprises two modules: the encoding module and the transition module. The key idea behind this training strategy is that we can leverage physics loss to enhance the reconstruction ability of the encoding module and the generalization ability of the transition module, using both labeled and unlabeled data. The PICL framework is evaluated on three different PDEs, e.g., wave equation, linear shallow water equation, and nonlinear shallow water equation with uneven bottom.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well written and easy to follow. The idea of learning the fine-grained state representation from coarse-grained data is interesting and novel.
2. The proposed PICL framework is evaluated on three different PDEs, e.g., wave equation, linear shallow water equation, and nonlinear shallow water equation with uneven bottom. The experimental results show that PICL exhibits superior predictive ability across modeling various PDE-governed physical systems.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed PICL framework is only evaluated on three PDEs, e.g., wave equation, linear shallow water equation, and nonlinear shallow water equation with uneven bottom. It would be better to evaluate the proposed PICL framework on more PDEs. Specifically, the current evaluation lacks examples of more complex, chaotic systems, or systems with strong non-linearities beyond the shallow water equations. The performance of PICL on such systems is unclear, and it is important to demonstrate its robustness across a wider range of physical phenomena.
2. The PICL framework is only compared with three baselines, e.g., PIDL, FNO, and PINO*. It would be better to compare the PICL framework with more baselines. The current baselines do not fully represent the state-of-the-art in physics-informed machine learning, particularly in the context of coarse-grained data. For example, methods that explicitly address the challenges of learning from low-resolution data, or those that use different neural network architectures, should be considered for a more comprehensive comparison.

### Suggestions

The paper would benefit from a more thorough evaluation of the PICL framework across a wider range of partial differential equations (PDEs). The current selection of PDEs, while representative of some common physical systems, does not fully capture the diversity of challenges encountered in physics-informed machine learning. Specifically, the inclusion of more complex systems, such as those exhibiting chaotic behavior or strong non-linearities, would provide a more robust assessment of the framework's capabilities. For instance, evaluating PICL on the Navier-Stokes equations, which govern fluid dynamics, or the Kuramoto-Sivashinsky equation, a model for chaotic systems, would be valuable. These systems present significant challenges due to their complex solution spaces and sensitivity to initial conditions. Furthermore, it would be beneficial to explore the performance of PICL on PDEs with different types of boundary conditions and forcing terms, as this would provide a more comprehensive understanding of its generalizability.

In addition to expanding the range of PDEs, the paper should also include a more comprehensive comparison with state-of-the-art baselines. The current comparison with PIDL, FNO, and PINO* is insufficient to fully contextualize the performance of PICL. There are several other methods that should be considered, particularly those that are designed to handle coarse-grained data or that use different neural network architectures. For example, methods that employ super-resolution techniques to enhance the quality of the input data before feeding it into the model could be a relevant comparison. Furthermore, comparing PICL with methods that use different types of neural networks, such as graph neural networks or transformers, would provide a more complete picture of its relative strengths and weaknesses. It is also important to ensure that the baselines are implemented with comparable computational resources and hyperparameter tuning to ensure a fair comparison.

Finally, the paper should provide more details on the implementation of the PICL framework, including the specific choices of hyperparameters and network architectures. This would allow other researchers to reproduce the results and build upon the proposed method. Furthermore, it would be beneficial to include an ablation study to analyze the contribution of each component of the PICL framework, such as the encoding module and the transition module. This would provide a deeper understanding of the inner workings of the framework and help to identify areas for further improvement. The paper should also discuss the limitations of the proposed method and suggest potential directions for future research.

### Questions

Please refer to the Weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
