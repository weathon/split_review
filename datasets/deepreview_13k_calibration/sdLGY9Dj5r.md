# Collaborative Discrete-Continuous Black-Box Prompt Learning for Language Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 8, 5

## Abstract
Large Scale Pre-Trained Language Models (PTMs) have demonstrated unprecedented capabilities across diverse natural language processing tasks. 
Adapting such models to downstream tasks is computationally intensive  and time-consuming, particularly in black-box scenarios common in Language-Model-as-a-Service (LMaaS) environments, where model parameters and gradients are inaccessible. Recently, black-box prompt learning using zeroth-order gradients has emerged as a promising approach to address these challenges by optimizing learnable continuous prompts in embedding spaces, starting with \textit{randomly initialized discrete text prompts}.  However, its reliance on randomly initialized discrete prompts limits adaptability to diverse downstream tasks or models. To address this limitation,
this paper introduces ZO-PoG, a novel framework that optimizes prompts through a collaborative approach, combining Policy Gradient optimization for initial discrete text prompts and Zeroth-Order optimization for continuous prompts in embedding space. By optimizing collaboratively between discrete and continuous prompts, ZO-PoG maximizes adaptability to downstream tasks, achieving superior results without direct access to the model’s internal structures.
Importantly, we establish the sub-linear convergence of ZO-PoG under mild assumptions.
The experiments on different datasets demonstrate significant improvements in various tasks compared to the baselines. 
Our code is available at the following anonymous URL: https://anonymous.4open.science/r/ZO-PoG-12B4.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a framework for prompt optimization in LLMs that combines discrete and continuous prompt tuning. This framework alternates between optimizing discrete prompts through policy gradient methods and continuous prompts via zeroth-order gradient optimization. The authors establish the sub-linear convergence of ZO-PoG under assumptions of Smoothness, Bounded Variance, Bounded Loss, and Lower-Bounded Parameters. This framework was evaluated on five datasets (CoLA, MNLI, QNLI, SNLI, WNLI) from the GLUE benchmark using RoBERTa-large, GPT2-XL, and Llama3 as backbone models. The code has been provided.

### Strengths
1. ZO-PoG combines discrete and continuous prompt optimization. Discrete prompts are refined through policy gradient in the parameter space, and continuous prompts are adjusted using zeroth-order gradients. This dual optimization approach enhances the adaptability and efficiency of prompt learning.
2. The authors provide a theoretical analysis showing ZO-PoG’s sub-linear convergence, validating its efficiency. Sub-linear convergence means that ZO-PoG requires fewer iterations to achieve satisfactory performance, making it a computationally efficient solution for black-box prompt learning.
3. The framework is tested on five datasets and demonstrates improvements over other black-box prompt learning methods. Results from the ablation study confirm that each component positively contributes to ZO-PoG’s overall performance, further validating its design choices.

### Weaknesses
1. Assumption 3 requires the loss function to be bounded. Does this assumption hold for the loss function in LLM fine-tuning? If not, could this assumption be relaxed in the theoretical analysis presented in this paper? Specifically, the cross-entropy loss, commonly used in LLM fine-tuning, is theoretically unbounded, which could invalidate the convergence guarantees of ZO-PoG. The paper should discuss the implications of this assumption and consider alternative loss functions or modifications to the theoretical analysis to address this issue.
2. This paper evaluates ZO-PoG on five datasets from the GLUE benchmark, while methods like BBT and SSPT report results on additional datasets. It would be valuable if the authors could provide performance comparisons of ZO-PoG on a broader range of datasets to offer a more comprehensive evaluation. Expanding the evaluation to include datasets with different characteristics would better demonstrate the robustness and generalizability of the proposed approach. For instance, datasets with longer sequences or different task types could reveal potential limitations of ZO-PoG.
3. I recommend that the authors discuss the query complexity of zeroth-order optimization following the theorem, as this would provide a clearer understanding of the computational efficiency of the proposed approach. The analysis should include a discussion on how the query complexity scales with the dimensionality of the search space and the desired level of accuracy, which is crucial for practical applications.

### Questions
Given that the loss function of LLMs is unbounded, I'm wondering if Assumption 3 can be relaxed in theoretical analysis to better reflect practical scenarios?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new approach to black-box prompt learning by jointly optimizing both discrete text prompts and continuous embeddings, with a convergence analysis. Experiments on five commonly used datasets demonstrate its superiority.

### Strengths
- The paper is clearly written and easy to follow
- The proposed method is technically sound 
- The experimental results show the proposed method has a significant performance improvement.

### Weaknesses
 - My main concern lies in that why the authors did not employ the true black-box models, such as GPT-4 and Claude-3.5, as their backbone models. Since the proposed method aims at black-box prompt learning, it would be more convincing to show how it works with these leading black-box API.  Is it still necessary to optimize the prompts for such powerful models in terms of cost versus benefit? It would be much better to include these results. 
- Why choosing a random matrix $\textbf{A}$? Is it good enough? If not, why not optimizing it or how to choose a better one?
- How does the performance change as the prompt length increases? Better show more results on different lengths.
- Does this method works only on natural language tasks? How does it behave on math or code tasks?

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In the paper "Collaborative Discrete-Continous Black-Box Prompting Learning For Language Model," the authors propose a new method for learning prompts, considering LLMs as a black box model. Under this assumption, the algorithms only have access to token and output (thus possible computation of a loss); therefore, it is impossible to access gradient and modify embeddings contrary to classical prefix tuning.



Similar to the CMA-ES approach, the authors propose to learn prompt embeddings in a low dimension and then project it to the input dimension of the model. The input embeddings correspond to the addition of the continuous prompt and representation of tokens of the vocabulary  $Az + p_0$($p_0$ sampled from the vocabulary). Contrary to previous approaches, authors propose to learn $z$ using the zeroth-order approximation.
In addition, the authors propose to learn the distribution of discrete prompt tokens over the vocabulary (sampling p_0). The distribution is approximated using the gamble softmax distribution, where parameters are estimated using a policy gradient with a baseline (REINFORCE).

The authors propose to analyze the convergence of the algorithm proposed in section 4. The approach is then evaluated on different GLUE tasks, and performances are compared with the manual prompt approach (designing the tokens of the prompts manually) and other black box prompting approaches. Three LLMs are compared: RoBERTa large, GPT2-XL, and Llama3. 
An ablation study is set up, removing the Gumbel softmax (using a policy gradient approach from [1] instead), removing the discrete prompts optimization and the continuous prompt optimization.   

For all experiments, the settings were tested at 20 and 50 prompt lengths.

The contributions are the following : 
 * A new algorithm for black box prompting.
 * A new approach to select (sample) $p_0$ for discrete prompts  using  Gumbel softmax (contrary to the previous approach, choosing random token vocabulary)
* State-of-the-art results in black box prompting.
* Convergence analysis of the proposed method

### Strengths
* The approach and related works are well-described and motivated
* New algorithm  for black box prompting combining previous ideas with new one proposed
* Proposal of optimizing discrete prompt using gumbel softmax
* State-of-the-art result for approach in a black box setting
* Relevant Ablation study removing some part of the algorithm to judge the effect of the different component
 * Justification of the algorithm

### Weaknesses
 * Limited dataset and configuration (20 and 50-length prompt) evaluation
* The related works section could have been extended

### Questions
* In the 5.1 section, the authors observed a significant difference depending on the model when compared to the manual prompt (first result line of the tables). Particularly, GPT2-XL and mostly Llama3 have, for most datasets, lower improvement using black box rather than manual prompt, particularly on the CoLA dataset. The authors state that it is due to the nature of the CoLA corpus. Does the fact that Roberta is an encoder only and the others are decoders (different pretraining tasks) have a role in this difference? The latter are thus more likely to get better performances on grammatically correct prompts.
* What is the prompt size for manual prompts? How did you select manual prompts?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the problem of soft prompt optimization for pre-trained language models. In some previous works, random initialization is applied to a soft prompt which will be added to a low-dimensional vector's random projection. The authors proposed to optimize this random initialization as they believe this may lead to suboptimal performance. Technically, an alternating optimization method is proposed where the random initialization is optimized via a policy gradient method over token distributions, and the low-dimensional vector $z$ is optimized through zeroth-order optimization. Detailed convergence analysis is provided and empirical results are shown to justify the effectiveness of the proposed method.

### Strengths
- This work improves previous literature with special consideration on optimizing the initialization of soft prompts. The mixing of discrete prompt and soft prompt optimization is also innovative.
- Theoretical analysis of convergence is given to justify the design and principle of the proposed alternating optimization method.

### Weaknesses
 - The authors stated their focus is on PTMs that can be interacted solely via APIs. However, most commercial models nowadays do not open embedding access,  which makes the soft prompt tuning method not practical and thus less significant. Especially in the experimental section, only a few white-box models are included and no black-box models are not considered.
- The recent literature on prompt optimization is not included. For example, InstructZero [1], ZOPO [2], and TRIPLE [3] were proposed to use a derivative-free method (Bayesian optimization or zeroth-order method) to optimize soft or discrete prompts. ZOPO and TRIPLE also project the discrete prompts into an embedding space to conduct optimization. Those methods need to be at least discussed and possibly compared.

[1] Chen, L., Chen, J., Goldstein, T., Huang, H., & Zhou, T. (2023). Instructzero: Efficient instruction optimization for black-box large language models.

[2] Hu, W., Shu, Y., Yu, Z., Wu, Z., Lin, X., Dai, Z., ... & Low, B. K. H. (2024). Localized zeroth-order prompt optimization. 

[3] Shi, C., Yang, K., Yang, J., & Shen, C. (2024). Best arm identification for prompt learning under a limited budget. 


- A strong motivation for this work is to improve the random initialization which is claimed to lead to a suboptimal performance. However, no empirical or theoretical justification is given. I suggest the authors conduct some ablation studies to demonstrate the sensitivity of prompt optimization performances given random initialization (number of random initialization or different random seeds). 
- Why alternating optimization is necessary? Could the author demonstrate the difference between <just using one round of soft-prompt optimization + one round of zeroth-order optimization> and <the alternating optimization strategy>? I also feel a joint optimization is feasible here, where the low-dimensional $z$ and the encoded probability of the initialization prompt can be jointly optimized by zeroth-order optimization. These points should be helpful for justifying why the alternating optimization is designed.
- Assumption 1 normally does not hold in practice, especially when the loss function only produces discrete values for some NLP tasks, e.g., accuracy. I understand this assumption has to be made for the theory to work, but at least some level of justification should be given.
- Limited empirical results.
    - More representative baselines proposed in recent years should be considered.
    - Only one benchmark (i.e., GLUE) is considered. I expect to see comparisons on other more practical benchmarks, such as mathematical reasoning task GSM8K and some text generation tasks.

### Questions
See the questions above.

### Soundness
2

### Presentation
3

### Contribution
2
