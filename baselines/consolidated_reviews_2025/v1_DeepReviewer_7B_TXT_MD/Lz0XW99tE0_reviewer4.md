### Summary

The paper introduces CrysBFN, a novel approach to generating crystal structures using Bayesian Flow Networks (BFNs) tailored for periodic data. The authors address the unique challenges posed by crystal structures, which involve periodic boundary conditions and crystal symmetries, by extending BFNs to operate on the hyper-torus. This adaptation allows for more accurate and efficient generation of crystal structures compared to existing methods. The paper presents extensive experiments demonstrating that CrysBFN achieves state-of-the-art performance on several benchmarks, including crystal ab initio generation and stable structure prediction tasks. Notably, the method exhibits significantly improved sampling efficiency, requiring only 10 function evaluations (NFEs) compared to previous diffusion-based approaches that needed thousands of steps. The authors provide a detailed theoretical analysis of their approach, including the non-additive accuracy dynamics and the entropy conditioning mechanism, which are crucial for the method's success. The paper also includes ablation studies to validate the importance of each component of CrysBFN, further solidifying the contribution of the work.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- **Novel Approach to Crystal Structure Generation:** The paper presents a creative and technically sound approach to crystal structure generation by extending Bayesian Flow Networks (BFNs) to handle periodic boundary conditions and crystal symmetries. This adaptation is a significant step forward in the field, as it addresses the unique challenges posed by crystal structures that are not well-handled by existing generative models.
- **Theoretical Rigor:** The authors provide a thorough theoretical analysis of their method, including the non-additive accuracy dynamics and the entropy conditioning mechanism. This analysis is crucial for understanding the inner workings of CrysBFN and provides a solid foundation for the method's effectiveness.
- **State-of-the-Art Performance:** The paper demonstrates that CrysBFN achieves state-of-the-art performance on several benchmarks, including crystal ab initio generation and stable structure prediction tasks. This is a significant achievement, as it shows that the method outperforms existing approaches in terms of both accuracy and efficiency.
- **Improved Sampling Efficiency:** CrysBFN significantly improves sampling efficiency, requiring only 10 function evaluations (NFEs) compared to previous diffusion-based approaches that needed thousands of steps. This efficiency is a crucial advantage, as it makes the method more practical for real-world applications.
- **Ablation Studies:** The paper includes ablation studies that validate the importance of each component of CrysBFN, further solidifying the contribution of the work. These studies provide valuable insights into the method's design and help to understand the impact of each component on the overall performance.

### Weaknesses

#### Some Related Works


#### comment

 - **Limited Discussion of Limitations:** While the paper presents a novel and effective approach, it lacks a thorough discussion of the limitations of CrysBFN. For instance, it does not address potential failure cases or scenarios where the method might struggle to generate realistic crystal structures. A more detailed analysis of these limitations would provide a more balanced view of the method's capabilities and help guide future research.
- **Lack of Comparison with Other Generative Models:** The paper focuses primarily on comparisons with diffusion-based methods, but it does not compare CrysBFN with other generative models, such as graph neural networks or other specialized crystal structure generation methods. This omission makes it difficult to assess the relative strengths and weaknesses of CrysBFN compared to a broader range of approaches. A more comprehensive comparison would provide a clearer picture of the method's novelty and effectiveness.
- **Insufficient Analysis of Computational Cost:** Although the paper highlights the improved sampling efficiency of CrysBFN, it does not provide a detailed analysis of the computational cost associated with training and inference. This information is crucial for assessing the practical applicability of the method, especially in resource-constrained environments. A more thorough analysis of the computational cost would help to understand the trade-offs between accuracy and efficiency.
- **Lack of Real-World Applications:** The paper demonstrates the effectiveness of CrysBFN on benchmark datasets, but it does not provide concrete examples of how the method can be applied to real-world problems. Including case studies or examples of practical applications would help to demonstrate the practical relevance and impact of the work.

### Suggestions

The paper would benefit significantly from a more detailed discussion of the limitations of CrysBFN. Specifically, the authors should explore scenarios where the method might fail to generate realistic crystal structures. For example, how does the model perform when generating materials with very high or low coordination numbers? Are there specific types of bonding patterns or crystal structures that the model struggles with? A thorough analysis of these failure cases would provide a more balanced view of the method's capabilities and help to identify areas for future improvement. Furthermore, the authors should discuss the sensitivity of the model to hyperparameter choices and provide guidance on how to select appropriate values for different types of crystal structures. This would help to make the method more accessible and practical for a wider range of users.

To strengthen the paper, the authors should include a more comprehensive comparison with other generative models, particularly those that are specialized for crystal structure generation. While the paper focuses on comparisons with diffusion-based methods, it is important to benchmark CrysBFN against other approaches, such as graph neural networks or other specialized methods. This would provide a clearer picture of the method's novelty and effectiveness compared to a broader range of approaches. The comparison should not only focus on quantitative metrics but also include a qualitative analysis of the generated structures. For example, how do the generated structures compare in terms of their physical plausibility and diversity? This would help to highlight the unique advantages of CrysBFN and its potential impact on the field.

Finally, the paper should include a more detailed analysis of the computational cost associated with training and inference. While the paper highlights the improved sampling efficiency of CrysBFN, it is important to understand the computational resources required for training and inference. This information is crucial for assessing the practical applicability of the method, especially in resource-constrained environments. The authors should provide a breakdown of the computational cost associated with each step of the method, including the training of the Bayesian flow and the inference process. This would help to understand the trade-offs between accuracy and efficiency and to identify potential areas for optimization. Additionally, the authors should provide concrete examples of how the method can be applied to real-world problems. Including case studies or examples of practical applications would help to demonstrate the practical relevance and impact of the work.

### Questions

- **Scalability to Larger Systems:** How does the performance of CrysBFN scale with the size of the crystal system? Are there any limitations or challenges when applying the method to larger and more complex crystal structures?
- **Generalizability to Different Crystal Systems:** Can CrysBFN be generalized to different types of crystal systems, such as ionic crystals or quasicrystals? If so, what modifications or adjustments would be necessary?
- **Comparison with Other Generative Models:** How does CrysBFN compare to other generative models, such as graph neural networks or other specialized crystal structure generation methods? Are there any specific advantages or disadvantages of using CrysBFN compared to these alternative approaches?
- **Sensitivity to Hyperparameters:** How sensitive is CrysBFN to the choice of hyperparameters? Are there any guidelines or best practices for selecting appropriate hyperparameter values for different types of crystal structures?
- **Potential for Bias in Generated Structures:** Are there any potential biases in the generated crystal structures? How can these biases be mitigated to ensure the physical plausibility of the generated materials?

### Rating

8

### Confidence

4

**********
