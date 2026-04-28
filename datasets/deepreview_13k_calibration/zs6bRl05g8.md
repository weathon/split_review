# Accelerating Block Coordinate Descent for LLM Finetuning via Landscape Correction

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Training and finetuning large language models (LLMs) are resource-intensive tasks, with memory limitations being a key bottleneck. A classic optimization method, block coordinate descent (BCD), offers solutions by segmenting the trainable parameters into multiple blocks and optimizing one active block at a time while freezing the others, thereby significantly reducing memory cost. However, we identify that blindly applying BCD to train LLMs can be inefficient for two reasons. First, optimizing only the active block requires backpropagating through multiple deeper yet inactive blocks, resulting in wasteful computations. Second, the frozen blocks, when they are not quite close to optimality, can narrow the optimization landscape, potentially misguiding the training of the active block. To address these issues simultaneously, we propose integrating BCD with *landscape correction*, which unfreezes the inactive blocks and updates them in a cost-efficient manner during the same backpropagation as the update to the active block. We show that our method empirically improves vanilla BCD with minimal additional computation and memory. Experiments on 8B and 70B models demonstrate that our proposed method surpasses memory efficient baselines and matches Adam's downstream performance while reducing memory cost by 80% compared to Adam.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Recently, a method called BAdam, which utilizes block coordinate descent (BCD), has gained attention in LLM fine-tuning for its memory efficiency. 
This study reveals a drawback of BCD optimization in neural network training: the frozen blocks can narrow the optimization landscape, potentially misleading the training of the active block, resulting in suboptimal solutions. 
Based on this intuition, the authors propose the BREAD method, which corrects the loss landscape of BCD. Also, the authors experimentally demonstrate the superiority of BREAD over the existing baselines in terms of both memory-efficiency and performance.

### Strengths
1. It is the first study to identify the issue in BCD, where frozen blocks that are far from optimality can interfere with the optimization of the active block.
2. It theoretically demonstrates, through a regression problem on a three-layer shallow network, that suboptimal solutions may indeed arise.
3. For LLM fine-tuning tasks, it shows improvements over existing baselines in both memory efficiency and performance.

### Weaknesses
I have several concerns.

1. Although it is intuitive that BCD optimization can lead to suboptimal solutions in a regression problem using a 3-layer shallow network, the situation could differ for a general L-layer deep neural network. Moreover, since LLM fine-tuning often involves classification tasks rather than regression, it would be helpful to have a theoretical analysis or at least some intuition on how this approach would perform with loss functions like cross-entropy.

---

2. Convergence analysis is missing. For a landscape correction scheme like BREAD, there should be at least some convergence results, even in the context of convex optimization, to show whether it is a provably convergent algorithm. I think it is crucial in optimization literature.

---

3. The performance improvement in the main experiment of LLaMA-3 fine-tuning appears marginal. It would be beneficial to include more comprehensive experimental results across a variety of settings, such as with alternative architectures like Phi-3 or Mistral, and other benchmark tasks.

---

4. Additionally, according to Table 1, BREAD is slower than BAdam in terms of Epoch GPU hours. Therefore, for a clearer understanding of the BREAD method, it would be helpful to include a figure comparing learning curves in terms of wall-clock time rather than just the number of iterations, as shown in Figure 3.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose integrating BCD with landscape correction to address two issues in fine-tuning LLMs with BCD: 1. inefficient computation due to backpropagation through deeper layers and 2. limited exploration of the optimization landscape inherent to BCD. They provide theoretical insights based on a three-layer neural network and demonstrate empirical performance improvements, albeit with increased computational and memory requirements.

### Strengths
1. The proposed method is easy to follow and interesting, involving the addition of correction parameters during BCD to improve performance.
2. The paper presents results on LLaMA models across various tasks to validate the effectiveness of the proposed method.

### Weaknesses
1. The algorithm lacks a theoretical convergence rate guarantee, although establishing such a rate for BCD optimization is challenging.
2. In Appendix B.1 of the BAdam paper, various ordering strategies for block partitioning in BAdam are investigated; however, this paper neither provides any rationale nor presents similar results.
3. It is surprising to observe that BREAD-SGD-partial demonstrates convergence similar to BREAD-SGD, and the reason for this behavior is unexplained.
4. I believe there is an error in the example used in Proposition 2. Specifically, the expressions $Ce_1=W_3^{(1)}-y$ and $y-W_3e_1=y-W_3^{(1)}$ does not subtract to 0.

### Questions
See the above weaknesses for questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents BREAD, a method designed to overcome limitations of block coordinate descent (BCD) in LLM fine-tuning by introducing landscape correction. The authors claim that BREAD unfreezes and updates inactive blocks using a lightweight optimization approach, addressing inefficiencies in derivative usage and suboptimal training landscapes. The method is evaluated through experiments on 8B and 70B LLMs, demonstrating memory savings and competitive downstream performance.

### Strengths
- The two issues of BCD are particularly intriguing and their demonstration via 3-layer NN is interesting.
- The experimental results look promising.

### Weaknesses
 - **Presentation**. The paper’s presentation could be improved, particularly in terms of notations and the clarity of the method descriptions.
- **Limited technical contributions**. The technical novelty appears limited, as BREAD is essentially a combination of LoRA and BCD while BREAD-SGD is a combination of LOMO [1] and BCD. The core idea of using low-rank updates to correct the landscape in BCD is not fundamentally new, given the existing literature on low-rank adaptation methods like LoRA and GaLore, which also aim to efficiently modify model parameters. The method seems to apply these techniques within a BCD framework without introducing significant algorithmic innovation.
- **Experiments**. Additional experiments, as outlined below, are necessary to strengthen the findings.

- **Baselines**
    - Results for LOMO are still missing.
    - Quantitative results for other variants (BREAD-partial, BREAD-SGD, BREAD-SGD-partial) are not included in Tables 2 and 3.
- **Statistical significance**. The authors should report standard deviations across multiple random seeds to assess the robustness of the results.
- **Ablation studies**. The authors should include ablation studies that explore the effect of the choice of D, K, and r on performance.



### Questions
1. **Algorithm 1**
    - Are there two separate instances of the Adam optimizer being used?
    - It is unclear how U and V are initialized and used.
    - What constitutes a single iteration? Is it defined as one while loop or one landscape correction update?
    - How is one epoch of training data sampled for Algorithm 1?
2. **Notation**
    - Ensure that all notations used in Section 2 are properly introduced.
    - What does $n$ represent in Section 4.2?
3. **Experimental settings**
    - How is alpha chosen for LoRA because rank 80 is a pretty weird setting.
    - The evaluation setup is not fully aligned with MathInstruct [2] regarding the choice of out-of-domain datasets and the number of shots used.
4. **Baselines**
    - How does the proposed method compare with LOMO?
    - The authors should include the performance of other variants for a more comprehensive evaluation.
5. **Ablation studies**. The authors should include ablation studies that explore the effect of the choice of D, K, and r on performance.
6. **Statistical significance**. The authors should report standard deviations across multiple random seeds to assess the robustness of the results.
- Minor:
    - In the proof of Proposition 2, $C = [y - W_3^{(1)}, 0, \ldots, 0]$ should be corrected.
    - Note that mathematical fine-tuning also falls under instruction tuning.
    - In Table 2 (Llama 3.1-8B, SimulEQ, 4-shot), the best result is incorrectly highlighted.

[1] Lv, Kai, et al. "Adalomo: Low-memory optimization with adaptive learning rate." *arXiv preprint arXiv:2310.10195* (2023).

[2] Yue, Xiang, et al. "Mammoth: Building math generalist models through hybrid instruction tuning." *arXiv preprint arXiv:2309.05653* (2023).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents  a method designed to improve the efficiency and convergence speed of block coordinate descent (BCD) in large language model (LLM) finetuning. The authors identify two main limitations of traditional BCD when applied to deep neural networks: (1) the ineffective use of computed gradients for inactive blocks during backpropagation, leading to wasted computational resources, and (2) the suboptimal optimization landscape created by freezing most blocks, which can hinder convergence.
To address these challenges, BREAD integrates a lightweight landscape correction mechanism that updates inactive blocks using low-rank matrix adjustments. So the method becomes SGD/ADAM on all layers but for inactive layers the LORA structure is constructed for SGD/ADAM to optimize.

### Strengths
The paper introduces an innovative combination of block coordinate descent (BCD) with a novel "landscape correction" approach, termed **BREAD**, tailored for large language model (LLM) finetuning. The originality stems from identifying limitations in the traditional BCD approach blending of BCD with lightweight, low-rank updates.
Empirical results from experiments on models like Llama 3.1-8B and Llama 3.1-70B demonstrate the method's effectiveness.
The paper is structured well.

### Weaknesses
1. In Case II of the proof for Proposition 1, it is unclear why \( z_3^* \) necessarily has at least one negative entry. The reasoning behind this is not evident.

2. The proposition does not adequately illustrate the global optimization landscape when applying BCD to a DNN. A single step in BCD resulting in a higher loss does not imply eventual failure. Therefore, the conclusion stating, 'our analysis reveals that the sub-problem of BCD potentially excludes parts of the optimization landscape that provide search directions toward the optimal solution,' is not clearly justified.

3. The described method involves performing SGD on all inactive layers for LoRA and also on active layers, making it more similar to Galore than true BCD. It is unclear how this approach achieves lower memory cost compared to Galore.

4. Demonstrating an extreme example in the propositions does not conclusively show that BCD performs worse than other methods in general. Experiments should be conducted to test the hypothesis that BCD restricts the search space. This could be verified by measuring the change in magnitude for each layer and comparing the results between BCD and BREAD to substantiate that BREAD indeed expands the search space more effectively.

### Questions
Please see Weakness.

### Soundness
2

### Presentation
3

### Contribution
2
