### Summary

The paper proposes a two-step training method for physics-informed machine learning where only coarse-grained measurements are available. The method consists of an "encoding" module that reconstructs fine-grained state from the coarse-grained input, and a "transition" module that predicts the subsequent state. The proposed method is tested on three PDEs: wave equation, linear and nonlinear shallow water equation.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method seems to be a reasonable extension of existing methods.
- The proposed method outperforms the baselines on the three PDEs.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method seems to be an incremental extension of existing methods.
- The proposed method is only tested on three PDEs, and it is not clear how sensitive the method is to the boundary conditions.
- The proposed method seems to be only useful for prediction, but not for inference or inverse problems.

### Suggestions

The paper's primary weakness lies in its incremental nature. While the proposed method combines existing techniques, the novelty is not sufficiently justified. The authors should provide a more detailed analysis of the specific challenges addressed by their approach that are not already handled by existing methods. For example, a more thorough discussion of the limitations of applying standard physics-informed neural networks (PINNs) directly to coarse-grained data would be beneficial. Furthermore, the authors should explore alternative architectures or training strategies that could offer more significant improvements over existing methods. A more rigorous comparison with state-of-the-art techniques, highlighting the unique advantages of the proposed method, is needed to establish its contribution to the field.

The limited scope of the experimental validation is another concern. Testing the method on only three PDEs does not provide a comprehensive understanding of its generalizability. The authors should consider expanding their experiments to include a wider range of PDEs with varying characteristics, such as different boundary conditions, non-linearities, and dimensionality. Additionally, the sensitivity of the method to different types of boundary conditions should be thoroughly investigated. For instance, the performance of the method under Dirichlet, Neumann, and Robin boundary conditions should be evaluated and compared. This would provide a more robust assessment of the method's applicability to diverse physical systems. Furthermore, the authors should explore the impact of different levels of coarsening on the performance of the method, as this is a critical factor in real-world applications.

Finally, the paper's focus on prediction limits its applicability. The authors should explore the potential of their method for inference and inverse problems. For example, the method could be extended to estimate unknown parameters or initial conditions from coarse-grained data. This would significantly broaden the impact of the proposed method and make it more relevant to a wider range of scientific and engineering applications. The authors should also discuss the limitations of their method in the context of inference and inverse problems, and suggest potential avenues for future research in these directions. Addressing these points would significantly strengthen the paper and enhance its contribution to the field.

### Questions

- What are the main challenges that the proposed method addresses that cannot be handled by existing methods?
- How sensitive is the proposed method to the boundary conditions?
- How can the proposed method be used for inference or inverse problems?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
