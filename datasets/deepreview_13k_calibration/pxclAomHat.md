# On the Optimization Landscape of Low Rank Adaptation Methods for Large Language Models

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 8, 8, 5, 6, 5

## Abstract
Training Large Language Models (LLMs) poses significant memory challenges, making low-rank adaptation methods an attractive solution. Previously, Low-Rank Adaptation (LoRA) addressed this by adding a trainable low-rank matrix to the frozen pre-trained weights in each layer, reducing the number of trainable parameters and optimizer states. GaLore, which compresses the gradient matrix instead of the weight matrix, has demonstrated superior performance to LoRA with faster convergence and reduced memory consumption. Despite their empirical success, the performance of these methods has not been fully understood or explained theoretically. In this paper, we analyze the optimization landscapes of LoRA, GaLore, and full-rank methods, revealing that GaLore benefits from fewer spurious local minima and a larger region that satisfies the \pl, a variant of Polyak-Łojasiewicz (PL) condition, leading to faster convergence. Our analysis leads to a novel method, GaRare, which further improves GaLore by using gradient random projection to reduce computational overhead. Practically, GaRare achieves strong performance in both pre-training and fine-tuning tasks, offering a more efficient approach to large-scale model adaptation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper builds on previous work (LoRA and GaLore) that uses low-rank adaptation to reduce the memory footprint of LLM training. This paper provides an analysis of GaLore, which compresses the gradient matrix, showing it has fewer problematic local minima and better convergence properties. Based on this analysis, they propose a new method called GaRare that improves GaLore further by using random projections to reduce computational overhead. GaRare achieves reasonable better performance on both pre-training LLMs and fine-tuning them for specific tasks.

### Strengths
This paper provides a sound theoretical analysis that reveals the optimization landscapes of different adaptation methods for training Large Language Models (LLMs). A key strength of this paper is the in-depth examination of the parameter spaces where the PL∗ condition is satisfied, revealing that GaLore and full-rank methods have larger favorable regions compared to LoRA. This theoretical foundation explains the superior convergence rates and performance of GaLore by demonstrating its lower occurrence of spurious local minima, which often hinder optimization in training processes. Such insights into the conditions that facilitate faster and more reliable convergence are invaluable for developing more efficient LLM training techniques.

### Weaknesses
Limited Experiment Setup: The experimental validation of the proposed methods is confined to modifications of the MLP layer, whereas practical applications of LoRA predominantly target the attention layers within LLMs. This discrepancy raises concerns about the generalizability and practical relevance of the findings. Specifically, the analysis and experiments focus on the MLP layers, which are less computationally intensive and have different gradient characteristics than the attention layers. The paper lacks experiments on attention layers, which are the primary focus of low-rank adaptation methods like LoRA in practice. This limits the applicability of the theoretical analysis and the practical impact of the proposed method. 

Marginal Performance Improvements: The performance improvements reported on the GLUE benchmark for GaRare, compared to the LoRA baseline and GaLore, are marginal. This minimal gain questions the practical value and impact of the proposed method in real-world application. Such incremental improvements might not justify the complexity or the computational costs associated with implementing GaRare. The reported gains are not substantial enough to warrant the adoption of a new method, especially considering the added complexity of random projections. The paper needs to demonstrate more significant performance improvements to justify the introduction of GaRare.


### Questions
1) why we switch to RoBERTa for fine-tuning experiment? while the pretraining is performed on LLaMa? It would be more convincing and interesting to see FT results on LLaMa, which is the widely applied in practice. 

2) Another benefit of LoRA is its application in low data regime, I wonder what is the results of the proposed methods at different training dataset size.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper provides a theoretical analysis of low-rank adaptation methods for large language models (LLMs), focusing on LoRA and GaLore. The authors demonstrate that GaLore benefits from a more favorable optimization landscape than LoRA and full-rank methods, characterized by fewer spurious local minima and a larger region satisfying the PL* condition. Building on these insights, they introduce GaRare, a novel method that improves upon GaLore by employing gradient random projection to reduce computational overhead. Empirical results show that GaRare performs strongly in pre-training and fine-tuning tasks, offering an efficient approach to large-scale model adaptation.

### Strengths
+ I believe the paper is a great application of the PL* condition to fine-tuning LLMS which is of significant interest. 
+ The theoretical analysis is rigorous and well-founded.
+ The paper contributes a valuable tool by introducing GaRare and demonstrating its practical efficiency.

### Weaknesses
 - Some sections of the paper, especially those detailing the theoretical results could be more accessible--understandable given the page limit.

### Questions
N/A.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper has two main contributions:
Firstly the authors conduct analysis on the theoretical properties of GaLore from the PL* condition perspective, which suggests that GaLore, compared with LoRA, has a larger region that satisfies the PL* condition, which provides faster convergence. Additionally, compared with full model training, the projected optimization approach suffers less from spurious minima issue, making it easier for optimization. These two arguments provide theoretical insights on the advantages of GaLore.
Then, the authors proposed a new method: GaRare, which uses random projection rather than SVD to find the low dimensional space, which improves memory efficiency in that the projection matrix no longer needs to be stored during training. GaRare, with lower memory cost, has the same theoretical properties of GaLore, as argued by the authors, and indeed shows performance comparable to GaLore on several empirical evaluation tasks, ranging from small-scale MLP-CIFAR10 experiments to LLM pre-training experiments.

Overall I find the paper well written, technically sound, and emprical results sufficiently supporting the claims.

### Strengths
- Parameter efficient learning / fine-tuning is a heated topic, lots of new methods are proposed but it is unclear why some methods are better / worse. The submission studies the advantages of GaLore and drawbacks of LoRA from an optimization perspective, providing useful insights and theoretical framework for understanding the PEFT methods.

- Learning rate swipe is conducted, making the emprical results more convincing!

- Low-bit training setting is considered, and the proposed method still shows performance competitive with GaLore, demonstrating the practical usefulness of the method.

### Weaknesses
 - There exists couples of gap between the theoretical analysis's setting and the actual experiments: 1. The theory suggests a squared loss should be used but all experiments used cross entropy loss; 2. The theoretical analysis is limited to MLP.

- Same color is used to represent different ranks and optimization methods (Figure 1. and Figure 2.), which could be confusing. The authors could consider using different colormaps for these two figures.

- It is true that the random projection matrix does not need to be stored, but I think they still need to be materialized during forward propagation and would still cost O(mr) memory overhead if I understand correctly.

- (Minor) The proposed method uses random projection, which could introduce additional sensitivity to random seed in experiments.

### Questions
- The theoretical analysis focuses on train-from-scratch setting, is there any difference between training from scratch v.s. fine-tuning setting? 

- How much extra runtime overhead would the random matrix generation cost in practice?

- How much difference would the "mr" term make in practice (Table 1, memory overhead of GaRare v.s. GaLore)? Since m is the output size, which would be pretty small in practice, e.g. 10 for cifar-10, and is much smaller than n, the input size, it would be nice if the authors could provide some example values of "m" and "r" in the caption of the table to better illustrate the differences.

### Soundness
3

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
3

### Summary
This paper investigates the optimization landscape of LoRA and GaLore from a theoretical standpoint, focusing on conditions like the PL* region and the prevalence of spurious local minima. This analysis seeks to clarify GaLore's fast convergence and strong empirical performance. Building on these insights, a streamlined variant called GaRare is introduced, leveraging gradient random projection for efficiency. Experiments validate GaRare's effectiveness, supporting its advantages with reduced computational demands and comparable performance to GaLore.

### Strengths
1. The paper applies theoretical insights from Lederer (2020) and Liu et al. (2022) to analyze LoRA and GaLore, offering an inspiring and interesting theoretical explanation of their behavior.
2. The paper introduces a streamlined variant of GaLore, named GaRare, and provides experimental results that effectively validate its performance and efficiency.

### Weaknesses
1. The paper does not explicitly link the quality of the optimization landscape to convergence speed or generalization performance, which undermines its stated goal of theoretically explaining the performance of LoRA and GaLore. Many claims also lack this connection (e.g., lines 60-61, 289-291, and 301-304), making them appear weaker and less convincing. For instance, while the paper discusses the size of the PL* region, it doesn't quantitatively show how a larger PL* region translates to faster convergence or better generalization. Similarly, the analysis of spurious local minima lacks a clear connection to the actual training dynamics and final model performance. The paper needs to provide more direct evidence that the observed landscape properties directly impact the training process and the quality of the resulting models.
2. The theoretical results in this paper are derived from analyses of MLPs, whereas LLMs, with their attention mechanisms, layer normalization, etc., are more complex. Since there is a gap between MLPs and LLMs, and the paper does not directly validate its theoretical results on LLMs (instead of relying only on the convergence and performance outcomes), the theoretical conclusions are less convincing. The paper assumes that the theoretical insights from MLPs will directly translate to LLMs, but this assumption is not rigorously justified. The paper should either provide theoretical results that are directly applicable to LLMs or provide empirical evidence demonstrating that the theoretical insights from MLPs hold true for LLMs.
3. The paper does not clearly motivate GaRare; it lacks evidence or justification for GaRare's advantages over GaLore based on theoretical analysis. Additionally, a more detailed algorithmic presentation is needed, particularly to clarify the process of recovering updated parameters from projected gradients, which would enhance understanding. The paper introduces GaRare as a streamlined variant, but it does not provide a theoretical basis for why random projections should preserve the optimization landscape benefits of GaLore. The algorithmic description is also insufficient, leaving the reader unclear about how the gradient random projection is actually implemented and how the parameters are updated.

### Questions
1. Is the formulation in Lederer (2020) fully compatible with that in Liu et al. (2022), allowing the results to be applied here without conflicting with prior findings?
2. Is it fair to compare the occurrence of spurious local minima between LoRA and GaLore when different definitions are used (i.e., standard vs. projected)?
3. How do the computational costs of these methods compare in Table 1? Does GaRare introduce any additional slowdown?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new algorithm GaRare, which implements gradient low-rank projection through random matrices and improves the memory and computational efficiency of GaLore. Through optimization landscape analysis, it is proved that GaRare retains the advantages of GaLore, satisfies the PL condition, and avoids spurious local minima. Experiments verify the superiority of GaRare in performance and efficiency.

### Strengths
1. By analyzing the PL conditions and spurious local minima, this paper systematically reveals GaLore's advantages in optimizing the landscape and LoRA's shortcomings.

2. This paper proposes the GaRare algorithm and provides rigorous theoretical proof that it can maintain GaLore's optimization advantages.

### Weaknesses
1. The GaRare algorithm proposed in this paper is mainly based on combining and improving existing methods, especially gradient low-rank projection through random matrices instead of SVD. Although this method is more efficient, it is technically more of an optimization of the existing GaLore and low-rank adaptation methods rather than proposing a new theoretical framework or algorithm. The core idea of using random projections to approximate low-rank matrices is not novel, and the paper does not sufficiently explore the theoretical implications of this approximation in the context of gradient-based optimization beyond what is already known about random projections. The analysis focuses on retaining the properties of GaLore, but it does not deeply investigate the potential limitations or biases introduced by the random projection, such as the impact on the optimization trajectory or the potential for increased variance in the gradient estimates.

2. Although the paper theoretically analyzes the optimization advantages of GaRare, the experimental results do not fully demonstrate the improvement of this method compared to existing methods. In some experiments, its effect is not better than the full-rank method or LoRA. The paper lacks a comprehensive analysis of the trade-offs between memory efficiency and performance. The experiments do not sufficiently explore the scenarios where GaRare might be expected to significantly outperform other methods, particularly in very high-dimensional settings or with extremely large models. The reported results do not clearly show that GaRare consistently achieves a better balance between memory usage and performance compared to existing methods across a range of tasks and model sizes. Furthermore, the paper does not provide a detailed analysis of the sensitivity of GaRare to the choice of random projection matrix, and how this choice impacts the final performance.

### Questions
1. GaRare uses Gaussian distribution to generate random projection matrices, but how about other distributions or generation methods? Does the choice of different distributions have an impact on the convergence speed and performance of the model?

2. Can the author add more experiments on practical tasks, such as fine-tuning end-to-end generation challenges or diffusion models, to further verify the results of GaRare?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper provides theoretical analysis of the optimization landscapes for different low-rank adaptation methods used in training large language models (LLMs), specifically comparing LoRA, GaLore, and full-rank methods. The authors prove that GaLore benefits from fewer spurious local minima and a larger region satisfying the PL* condition compared to LoRA. Then, they propose GaRare, a method using random projection matrices instead of SVD-based ones, achieving similar benefits as GaLore, in terms of the optimization landscape, but with reduced computational overhead.

### Strengths
1. Important focus on understanding optimization landscapes of fine-tuning techniques
2. Practical algorithm (GaRare) that improves efficiency
3. Comprehensive experimental validation
4. Clear mathematical formulation and complete proofs
5. Good connection between theory and practice

### Weaknesses
1. Theoretical analysis limited to MLP architectures, making conclusions about LLMs less direct.
2. Incomplete empirical comparisons:
   - Limited LoRA experiments (mainly rank 2). It would be better to experiment with different LoRA ranks (r = 4, 8, 16, 32) for a more reliable validation of the results. 
   - Missing comparisons with recent methods (e.g. AdaLoRA, SoRA) that yields better performance than full rank fine-tuning (on GLUE), while promoting sparse low rank matrices. Could you explain why these methods, even though they promote sparsity, yield better results than full rank tuning? And how do they integrate within your theoretical framework?
   - No standard deviations reported. Could you please report these for a more reliable assessment of the performance of your proposed algorithm compared to baselines across all experiments (CIFAR / GLUE).
3. Some claims about LoRA’s performance relative to full-rank fine-tuning are oversimplified.
   - Contradicts findings from AdaLoRA paper with higher ranks.
   - Doesn’t account for sparse adaptation methods’ success.
4. Ambiguous definition of projected spurious local minima.
   - Unclear relationship between projected minima and full-rank space:  how these minima relate back to the full-rank landscape?
5. Limited novelty in theoretical results: some of the theoretical results appear to be direct extensions of established theorems.
6. Memory analysis could be more detailed.

### Questions
1. How sensitive is GaRare’s performance to the choice of random seed and projection frequency? Could you perform an ablation study to probe the stability of your proposed method and report the results?
2. Could the theoretical framework be extended to transformer architectures?
3. How do the projected minima relate to the full-rank optimization landscape?
4. Why weren’t comparisons with higher-rank LoRA (r=8) and other recent low rank adaptation techniques included?

### Soundness
3

### Presentation
3

### Contribution
3
