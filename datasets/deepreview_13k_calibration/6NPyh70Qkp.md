# Adaptive Continual Learning Through Proactive Detection of Transfer and Interference

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Continual learning (CL) requires models to sequentially learn multiple tasks, maximizing transfer and minimizing interference. CL methods based on pre-trained models (PTM) have shown strong performance by integrating PTM fine-tuning with traditional approaches. Despite these promising results, current methods lack the ability to proactively detect task transfer and interference at the local optimization level, limiting their effectiveness in maximizing transfer and minimizing interference. To address this issue, we propose adaptive continual learning strategies through proactive detection of transfer and interference. We derive the conditions under which task transfer and interference occur from a model optimization perspective, based on the Fisher matrix and gradient update directions. Based on them, we proposed a task transfer distance metric to help model modules detect transfer and interference during continual learning. We propose a dynamic parameter update mechanism and a dynamic expansion strategy, based on LoRA fine-tuning and a Mixture of Experts (MoE) mechanism, to handle varying levels of task transfer and interference. Experiments results of seven benchmarks show that our method achieves the best accuracy with a limited number of parameters, maximizing transfer and minimizing interference.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new continual learning approach that addresses the importance of proactive detection of transfer and interference. They first propose a new metric for task transfer distance measurement, and accordingly design a dynamic parameter update mechanism based on LoRA finetuning on a subset of experts in MOE mechanism, such that the previous and current tasks can be well balanced. Experiments on 7 benchmarks are provided to show the transfer effectiveness of the proposed approach.

### Strengths
1. The proactive detection of transfer distance between tasks and a corresponding adaptive continual learning design is generally reasonable and novel to me.

2. Extensive evaluations on multiple benchmark datasets are provided.

### Weaknesses
1. The authors make a huge effort to explain the design details of the proposed approach but lack enough discussion on the high-level intuitions and key insights behind their designs. Therefore, it is hard to appreciate the paper's value through reading the paper.

2. Generally, the presentation in the paper is poor and hard to follow. Typos and grammar issues happen frequently. The fonts in the figures are too small. The figure references in Section 4.3 seem to be all wrongly placed.

3. The experiments are mostly about how the proposed approach outperforms the existing approaches, but without in-depth analysis on the reasons behind the results. Besides, the authors address the importance of the transfer and interference, but the analysis presented in Section 4.4 is weak and fails to highlight the value of the distinguishment.

4. The proposed approach only works with the pretrained Transformer architectures, but not other models, but the authors do not clarify that clearly in early sections of the paper.

### Questions
1. Is the proposed approach only applicable to Transformer models in vision tasks?

2. In Section 3.3.2, how many and which old branches do you select as "a few old branches" to participate in learning the new task?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the challenges of continual learning (CL), particularly in maximizing knowledge transfer while minimizing interference among tasks. The authors propose a novel method that enhances the performance of pretrained models by integrating proactive mechanisms to detect transfer and interference at the local optimization level. The framework was tested on several benchmark datasets, demonstrating significant improvements in accuracy compared to traditional CL methods.

### Strengths
1. The authors introduce a novel adaptive continual learning strategy that effectively balances transfer and interference. 
2. The empirical validation shows promising results across various benchmarks.

### Weaknesses
1. While the authors present a comprehensive framework for continual learning, the writing is challenging for readers to follow. In the methods section, many techniques are employed, such as MoE, FIM, and PCA; however, the reasons and intuitions behind using these techniques are only briefly mentioned. Furthermore, the authors do not reference whether these commonly used techniques have been applied in this field, making it difficult to assess the contribution of this paper.
2. Additionally, the use of numerous symbols in the methods section complicates comprehension, as their meanings are not clearly defined. The authors should simplify irrelevant introductions (e.g., the formulation of LoRA, which is introduced but not further used) and consider providing a table listing all used symbols.
3. The claims made in Section 3.2 are weak and would benefit from additional evidence for support.
4. Ablation studies are lacking; the effects of different components (e.g., various pretrained models) should be evaluated.
5. Minor issues:
  - Typically, only the best results should be highlighted in bold, rather than including all results.
  - Typos include a missing space in line 424, potential inconsistency with "k_t" in line 297, and incorrect subscript usage in line 342.

### Questions
Why does the formulation of $\beta$ in Eq. (10) seem misaligned with its definition?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper tackles the continual learning problem with pre-trained ViT. The topic is important to the machine learning field. The authors adopt the combination of MOE and GEM to tackle this problem. The proposed method is evaluated on several datasets against other baselines.

### Strengths
1.	This paper tackles the continual learning problem with pre-trained ViT. The topic is important to the machine learning field.
2.	The authors adopt the combination of MOE and GEM to tackle this problem. 
3.	The proposed method is evaluated on several datasets against other baselines.

### Weaknesses
1.	The writing of this paper is problematic, with many overlapping with existing works. For example, the authors have put much effort into the fisher information matrix, which is a common technique in EWC [1], and the bound in Line 228 is also directly copied from [2]. I would suggest the authors improve their writing by highlighting their own contributions and avoiding using vague descriptions. The extensive discussion of the Fisher information matrix, while relevant to continual learning, does not sufficiently differentiate the paper's specific use case or novel contribution beyond its established application in EWC. The direct borrowing of the bound without proper contextualization or modification also raises concerns about the originality and depth of the theoretical analysis.
2.	Overall, this paper makes a minor combination of GEM [3] and MOE-Adapters [4]. The basic idea for gradient projection is directly borrowed from [3], while the way the authors adopt the MOE and LORA is a simple modification of [4] (the only difference lies in the parameter-efficient tuning structure on LORA against Adapter). Hence, I am curious about the contribution of this paper. The core mechanism of gradient projection, as implemented, appears to be a straightforward application of the GEM approach, lacking substantial novelty. Similarly, the integration of MOE and LoRA, while practically relevant, seems to be a superficial adaptation of existing methods, with the change from Adapters to LoRA being incremental rather than transformative. The paper needs to articulate more clearly how these components are uniquely combined or modified to address specific challenges in continual learning.
3.	The experimental results are also weak, lacking many ablation results. For example, is the method sensitive to hyper-parameters? How do we decide the number of experts? How about removing different modules in the current framework? Are all of them efficient in the whole framework? With these details missing, the current experimental part only shows numerical results against other baselines, which is less informative. The absence of a thorough ablation study leaves significant gaps in understanding the method's behavior. The sensitivity to hyperparameters is a critical aspect that needs to be explored, as it directly impacts the practical applicability of the proposed approach. The number of experts is a key design choice that requires empirical justification, and the contribution of each module to the overall performance needs to be rigorously evaluated through controlled experiments.

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper considers how to mitigate interference and forgetting between tasks in continual learning through the transfer of knowledge between tasks. The proposed method combines LoRA (Low-Rank Adaptation) and MoE (Mixture of Experts) to fine-tune pre-trained models.

### Strengths
The approach of performing continual learning through the transfer of knowledge between tasks is intuitive.

### Weaknesses
1. The writing in this paper is poor, making it difficult to follow.

2. The section "The extraction and update of principal directions" in Section 3.3.1 is essentially the GPM (ICLR 2021) [1] algorithm and should not be considered a contribution of this work. It should not be described in such detail.

3. It is recommended that the author include an overview section at the beginning of Section 3 to introduce the whole process of the proposed method, and at the end of Section 3, present Algorithm to summarize the whole process of the method.

4. There is a lack of a problem formulation section that explains what problem you are solving and what settings you are considering. Specifically, existing continual learning settings include task incremental learning, class incremental learning, domain incremental learning, and so on. This paper does not even mention what continual learning setting the authors are considering.

5. The experimental setup is not clearly described, such as learning rate, batch size, epoch, etc., are not provided. The hyperparameter settings for the method are also not clearly explained.

6. The writing in this article is difficult to follow. If the author can improve the writing and satisfactorily address the issues I am concerned about, I would consider raising the score.

### Questions
The authors only introduced the use of the MoE (Mixture of Experts) structure in Section 3.1, and from Figure 2, it can be seen that the proposed method maintains a task-specific router for each task. Since the router is task-specific, I would like to ask if the proposed method is addressing the class incremental learning problem. If so, since class incremental learning requires task labels are unavailable during the inference phase, how do the proposed method selects the task routers to use during inference for a given test sample?
If this is not clearly explained, then this method would not be solving the problem of class-incremental learning. However, in the experiments, the method is compared against baselines that are class-incremental methods, which makes the comparison unfair.

### Soundness
2

### Presentation
1

### Contribution
2
