### Summary

The authors propose a method for data-driven PDE forecasting that addresses three key requirements: (1) learning from sparse observations, (2) generalizing to new initial conditions, and (3) achieving space and time continuity. The method combines a learned latent-space auto-regressive model with a learned state observer, both of which are implemented using geometric deep learning techniques. The authors provide theoretical results supporting their approach and demonstrate its effectiveness through experiments on three standard fluid dynamics datasets, outperforming strong baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a strong theoretical foundation for their method, including error bounds and convergence analysis.
- The method achieves state-of-the-art performance on three standard fluid dynamics datasets, demonstrating its practical effectiveness.
- The authors provide thorough ablation studies and analysis of their method's performance, including comparisons to strong baselines and evaluations of its computational efficiency.

### Weaknesses

#### Some Related Works


#### comment

 - The method relies on several assumptions, such as regular time sampling and observability, which may limit its applicability to certain types of PDEs or data.
- The method's performance may be sensitive to the choice of hyperparameters and network architectures, which could require careful tuning for different applications.
- The method's computational cost may be higher than some other approaches, particularly for large-scale simulations or long prediction horizons.

### Suggestions

The authors should more thoroughly investigate the limitations imposed by the regular time sampling assumption. While many PDE datasets are regularly sampled, many real-world scenarios involve irregular or missing data. The authors could explore techniques such as interpolation or imputation methods to handle irregular time series, or consider adapting their method to work with time-series data that is not uniformly sampled. Furthermore, a more detailed analysis of the observability assumption is needed. The authors should clarify what specific conditions on the observation operator and the PDE dynamics are required to ensure that the system is indeed observable. This could involve analyzing the rank of the observability matrix or providing a more rigorous theoretical justification for the chosen observation operator. Without a more detailed discussion of these limitations, the practical applicability of the method remains unclear.

Regarding the sensitivity to hyperparameters and network architectures, the authors should provide a more systematic approach to hyperparameter selection. While they mention that the model is not overly sensitive, a more thorough analysis is needed to understand the impact of different hyperparameter choices on the model's performance. This could involve performing a sensitivity analysis, where the authors vary each hyperparameter individually and observe the resulting changes in performance. Additionally, the authors should provide more guidance on how to choose appropriate network architectures for different types of PDEs. This could involve providing a set of guidelines or heuristics based on the characteristics of the PDE being modeled. Without a more systematic approach to hyperparameter selection and network architecture design, it is difficult to assess the robustness and generalizability of the method.

Finally, the authors should provide a more detailed analysis of the computational cost of their method. While they mention that their method is more efficient than some baselines, a more thorough comparison is needed to understand the trade-offs between computational cost and performance. This could involve providing a breakdown of the computational cost of each component of the method, as well as comparing the computational cost of their method to other state-of-the-art approaches. Furthermore, the authors should discuss the scalability of their method to large-scale simulations and long prediction horizons. This could involve performing experiments on larger datasets or analyzing the computational complexity of their method. Without a more detailed analysis of the computational cost and scalability, it is difficult to assess the practical feasibility of the method for real-world applications.

### Questions

- How does the method perform on PDEs with highly chaotic or turbulent behavior?
- Can the method be extended to handle non-autonomous PDEs with time-varying coefficients or forcing terms?
- How does the method compare to other approaches that use implicit neural representations for PDE solving, such as DeepONets or FNOs?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
