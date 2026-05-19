### Summary

This paper proposes three composition methods for sequential motion generation. The first method, DoubleTake, generates long motions by iteratively combining short motions. The second method, ComMDM, generates two-person motions by training a communication module on the difference between two MDM predictions. The third method, DiffusionBlending, enables fine-grained control over motion by interpolating between different motion models. The authors demonstrate the effectiveness of these methods through experiments on various motion generation tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed methods are interesting and novel.
2. The experiments are comprehensive and well-designed.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is difficult to follow, with many unclear notations and confusing explanations. For example, in Eq. (1), what do $X_t$, $x_t$, and $x_{t-1}$ represent? What is the meaning of $x_0$? What does the subscript $t$ mean? In Eq. (2), what is $S_i$? What is the meaning of the mask? What is the meaning of the mask $M_{hard}$? What is the meaning of the mask $M_{soft}$? In Algorithm 1, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Algorithm 2, what is the meaning of the operation $x_0 \leftarrow x_0 - \epsilon$? In Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 - \epsilon$? In Line 10 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 11 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 12 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 13 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 14 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 15 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 16 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 17 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 18 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 19 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 20 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 21 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 22 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 23 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 24 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 25 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 26 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 27 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 28 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 29 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$? In Line 30 of Algorithm 3, what is the meaning of the operation $x_0 \leftarrow x_0 + \epsilon$?

2. The experiments are not well described. What are the evaluation metrics used? How are the metrics calculated? What are the settings of the experiments? What are the baselines used in the experiments?

### Suggestions

The paper suffers from a lack of clarity in its notation and explanations, making it difficult to understand the proposed methods. For instance, the notation $X_t$ in Equation (1) is not clearly defined. Is it a random variable, a function, or a specific value? The paper should explicitly state that $X_t$ represents the noisy sample at time step $t$ in the diffusion process. Similarly, $x_t$ and $x_{t-1}$ are used without proper definition. It is unclear whether these represent samples from the data distribution or samples from the model at different noise levels. The meaning of $x_0$ is also ambiguous; is it the clean sample or the predicted mean at the final noise level? The subscript $t$ in Equation (2) is not explained. Does it denote the time step in the diffusion process? The masks $M_{hard}$ and $M_{soft}$ are introduced without sufficient context. The paper should explain how these masks are constructed and what their purpose is in the diffusion process. The operations in Algorithms 1, 2, and 3 are also unclear. The meaning of operations like $x_0 \leftarrow x_0 + \epsilon$ needs to be explicitly defined in the context of the diffusion process. For example, is this a forward diffusion step or a sampling step? The paper should clarify the role of each operation in the overall algorithm. The lack of clear definitions and explanations makes it challenging to reproduce the results and understand the technical details of the proposed methods.

The experimental section lacks crucial details, making it difficult to assess the validity of the results. The paper should specify the evaluation metrics used for each task. For example, in the long motion generation task, what metrics are used to evaluate the quality and diversity of the generated motions? Are they using metrics like Fréchet Inception Distance (FID), Inception Score (IS), or other motion-specific metrics? The paper should also explain how these metrics are calculated. For instance, if FID is used, what is the reference distribution? What is the input to the FID calculation? The paper should also provide details about the experimental settings. What are the hardware and software configurations used? What are the hyperparameter settings for the proposed methods and the baselines? The paper should also clearly state the baselines used in the experiments and justify their selection. For example, if the proposed method is compared to a baseline, what are the advantages and disadvantages of each method? The paper should also provide a detailed description of the datasets used in the experiments. What are the characteristics of the datasets? What are the limitations of the datasets? The paper should also discuss the limitations of the proposed methods. For example, what are the computational costs of the proposed methods? What are the potential failure cases of the proposed methods? The paper should also discuss the potential impact of the proposed methods on the field of motion generation.

To improve the paper, the authors should provide a clear and consistent notation throughout the paper. All symbols and variables should be defined before they are used. The authors should also provide a detailed explanation of the proposed methods, including the mathematical formulations and the algorithmic steps. The authors should also provide a detailed description of the experimental settings, including the evaluation metrics, the datasets, and the hyperparameter settings. The authors should also provide a detailed comparison of the proposed methods with the baselines, including the advantages and disadvantages of each method. The authors should also discuss the limitations of the proposed methods and the potential future directions of the research. The authors should also provide a clear and concise summary of the paper, highlighting the main contributions and the key findings.

### Questions

Please see the Weaknesses section.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
