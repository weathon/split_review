# Dynamic Modeling of Patients, Modalities and Tasks via Multi-modal Multi-task Mixture of Experts

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Multi-modal multi-task learning holds significant promise in tackling complex diagnostic tasks and many significant medical imaging problems. It fulfills the needs in real-world diagnosis protocol to leverage information from different data sources and simultaneously perform mutually informative tasks. However, medical imaging domains introduce two key challenges: dynamic modality fusion and modality-task dependence. The quality and amount of task-related information from different modalities could vary significantly across patient samples, due to biological and demographic factors. Traditional fusion methods apply fixed combination strategies that fail to capture this dynamic relationship, potentially underutilizing modalities that carry stronger diagnostic signals for specific patients. Additionally, different clinical tasks may require dynamic feature selection and combination from various modalities, a phenomenon we term “modality-task dependence.” To address these issues, we propose M4oE, a novel Multi-modal Multi-task Mixture of Experts framework for precise Medical diagnosis. M4oE comprises Modality-Specific (MSoE) modules and a Modality-shared Modality-Task MoE (MToE) module. With collaboration from both modules, our model dynamically decomposes and learns distinct and shared information from different modalities and achieves dynamic fusion. MToE provides a joint probability model of modalities and tasks by using experts as a link and encourages experts to learn modality-task dependence via conditional mutual information loss. By doing so, M4oE offers sample and population-level interpretability of modality contributions. We evaluate M4oE on four public multi-modal medical benchmark datasets for solving two important medical diagnostic problems including breast cancer screening and retinal disease diagnosis. Results demonstrate our method's superiority over state-of-the-art methods under different metrics of classification and segmentation tasks like Accuracy, AUROC, AUPRC, and DICE.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the author present a new framework for training multi-modal networks, called the Multi-modal Multi-task Mixture of Experts. The framework consists of two components:
- MSoE: Modality specific mixture of experts --> for each modality, they learn a function g that applies:
 column-wise softmax (D) on X times a learnable matrix, multiplied by X, followed by row-wise softmax (C) on the output and a linear combination to compute the prediction.
- MToE: Modality shared modality task mixture of experts --> connects tasks to input modalities by learning a task embedding shared across experts.

They also propose a mutual information loss and evaluate the approach on four publicly available medical imaging datasets for breast cancer and OCT.

### Strengths
The framework presented is original and interesting. It outperforms existing baseline models. The authors run experiments on multiple datasets and conduct an ablation study.

### Weaknesses
 - The paper presentation requires improvement. For example, there is unnecessary use of ; and there is incorrect use of opening quotations ". The authors also repeatedly introduce the abbreviations - this should be done once.
- I found it difficult to parse through Figure 2 (Can you relate it with the textual explanation of the functions?)
- The authors only compare to a few baselines, can you incorporate more? There is a lot of literature on multimodal learning now.
- Are the performance improvements significant? Can you conduct significance testing and provide confidence intervals?
- The experiments are conducted on medical imaging datasets. How does this apply to other non-imaging modalities where modality competition may be more pronounced. For example, this could be applicable to MIMIC CXR (chest X-rays) and MIMIC EHR where downstream tasks are more dependent on the EHR modality.
- The main results section in the text should also discuss the quantitative results.
- What was your hyperparameter tuning strategy? It is unclear if these baselines have been best optimized.
- Can you also compute AUROC and AUPRC for the classification tasks? Accuracy is not sufficient.

### Questions
- Can the authors discuss the scalability of the framework? What is the computational complexity?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper mainly addresses two challenges in clinical tasks: patient-level and task-level dynamic fusion. For the patient-level fusion, a modality-specific MoE is employed. For the task-level fusion, a modality-task MoE with conditional MI regularization between experts and modalities given tasks is adopted. The experiments using EMBED, RSNA, VinDR, and GAMMA datasets outperform existing methods in both single-task and multi-task settings.

### Strengths
- The paper is well-structured and easy to follow. 
- The motivation is clearly stated and convincing. 
- The experiments show promising results over many baselines both in stand-alone and add-on manners.  
- The paper adopted PID to make a fair comparison of synergy information.

### Weaknesses
 - As far as I understand, there have been works leveraging the shared and specific information across modalities and should be included in discussions, see [1-3]. 
- Is there an ablation study for a reduced number of experts? How sensitive is this method when the number of experts decreases compared to other MoE methods? What is the procedure for choosing the number of experts? 
- Please discuss the computational cost compared to the baselines.

### Questions
- Are there any ablation studies on datasets other than EMBED?
- Are there any theoretical explanations on why the method mitigates gradient conflict?
- Is there any clinical interpretation of the results in Figure 5? For example, the difference in modality contribution across different tasks.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a multi-modal, multi-task, mixture of experts for various medical diagnoses to address the challenges of sample-dynamic modality fusion (and modality-task dependence (selecting the right modalities for a task). Concretely, this is done by using a combination of modality-specific experts and experts shared between modalities and tasks. M4OE shows promising initial results in terms of both absolute performance and enforcing modality utilization.

Based on the weaknesses and questions outlined my score indicates a rejection for now, but I generally like the motivation of the paper, especially the aspect on modality utilization. I am willing to increase my score if my concerns are addressed and questions clarified.

### Strengths
- The M4OE is highly effective at enforcing modality utilization - this is a meaningful contribution that many multimodal models suffer from, although I do have some questions about this.
- The overall performance of the model is outperforming the baseline, even if the results are missing crucial information to validate the statistical significance of the results.
- Strong visuals that are additive to the understanding of the paper.
- Good conceptual motivation of the paper, although I believe that the motivation would further benefit from some concrete examples of sample dynamism and clinical examples of tasks that are modality-dependent.

### Weaknesses
- Abstract: the one-liner for sample-dynamic modality fusion is unclear as the specific and shared information always varies per sample unless they are identical. To my knowledge, sample-dynamic spans a much wider field of problems like missingness, robustness to noise, which the manuscript does not consider. The term 'sample-dynamic' is not consistently used, sometimes appearing as 'sample-adaptive' which further adds to the confusion. The core issue is that the manuscript does not clearly define what aspect of sample-dynamism it is addressing, and how this differs from any other multimodal fusion problem where the fusion weights are sample-dependent.
- Abstract: “Results demonstrate superiority over state-of-the-art methods” is extremely vague. Along which metric? It is also unclear if this superiority is statistically significant, as no confidence intervals or standard deviations are reported.
- You claim an expansive space by saying that the method is “multi-modal multi-task”, but your experiments only look at multi-view settings of a single modality (images). I would encourage you to narrow the scope/claim of the paper as the paper does not consider heterogeneous modalities (images, text, tabular, etc.). The experiments are limited to different views of the same image modality, which does not fully validate the claim of a general multi-modal approach. The paper should either expand its experiments to include diverse modalities or narrow the scope of its claims.
- Experimental setup: I would encourage you to provide more detail in this section to aid reproducibility. For example, it is unclear whether cross-validation is used. No confidence intervals or standard deviation of results are reported to judge the statistical significance of the results. Additionally, no code was provided in the supplementary materials that would help with the clarification of the experimental setup. The lack of detail in the experimental setup, including the absence of cross-validation details, statistical significance measures, and code, significantly hinders reproducibility.
- Literature: missing out on the largest corpus of literature (intermediate fusion), which many latent variable models for multimodal fusion fall under, many of which are using a mix of modality-specific and shared spaces. The paper fails to acknowledge a large body of work on intermediate fusion and latent variable models, which are highly relevant to the proposed approach. This omission weakens the paper's positioning within the existing literature.

### Questions
- How do you determine which expert sees which task? The connection between Figure 1 and the method section is not very clear.
- The manuscript talks a lot about sample adaptivity, but how does your experimental setup show that the model handles sample adaptivity effectively? Which aspects of sample adaptivity?
- Figure 3c suggests that the modality utilization is forced towards the same mean in your method. What about cases where modality dominance/competition is good? For example, if I have one very noisy modality, wouldn’t it be desirable to have the modality that contains all the signal to get all the model’s attention? Isn’t this graph showing that we enforce equal utilisation of all modalities regardless of the signal? Additionally, does this finding not contradict your claim in Figure 1, which is that only some experts are used (as opposed to all experts with a more balanced contribution).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces M4oE, a framework for multi-modal, multi-task learning in medical diagnosis. M4oE addresses two primary challenges in multimodal diagnosis: sample-dynamic modality fusion and modality-task dependence. The framework incorporates modality-specific modules and a modality-shared modality-task mixture of experts (MoE) to dynamically learn both unique and shared information across modalities. A conditional mutual information loss is used to optimize the framework efficiently. Experimental results on two medical diagnostic tasks demonstrate M4oE’s advantages over existing methods.

### Strengths
1. The M4oE framework is a novel contribution, with two innovative components—modality-specific modules and a modality-shared modality-task MoE—that allow for efficient learning of both distinct and shared information across modalities for multiple tasks.

2. The analysis is comprehensive, including detailed evaluations of modality competition, modality-task dependence, and sample-level modality contributions.

### Weaknesses
1. The M4oE framework is complex, raising concerns about optimization and practical implementation. Including a discussion on computational resources and runtime would help readers assess its feasibility for real-world applications. Specifically, the paper lacks details on the memory footprint of the model, the training time per epoch, and the inference time for a single sample, which are crucial for evaluating its practical applicability. Furthermore, the number of parameters in the model should be compared to other state-of-the-art methods to understand the trade-off between performance and model size.

2. The paper does not address whether M4oE can function effectively when certain modalities or tasks are unavailable—a common scenario in clinical settings. Clarifying this would strengthen the model’s applicability. The absence of a discussion on how the model handles missing modalities or tasks limits its practical use in real-world scenarios, where data is often incomplete. It is important to understand how the model's performance degrades with missing inputs and whether it can adapt to such situations.

### Questions
1. Could the authors provide computational resource requirements and runtime comparisons for M4oE and baseline methods?

2. In Figure 4, the similar difference between subfigures (a) and (b) and between (c) and (d) suggests both M4oE and the baseline might be capturing modality-task dependence. Could the authors clarify?

3. In Figure 3, is it reasonable to assume that the diverse distribution in (c) is preferable to that in (b), given the absence of a known ground truth distribution for each modality? Using the method in Liang et al. (2024) to quantify modality interactions could provide a more rigorous evaluation.

4. In Figure 1(a), under Part 3, should the label for the green triangle be $G_p$?

### Soundness
3

### Presentation
3

### Contribution
2
