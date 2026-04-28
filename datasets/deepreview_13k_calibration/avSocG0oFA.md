# Revisiting Delta-Parameter Pruning For Fine-Tuned Models

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
Storing open-source fine-tuned models separately introduces redundancy and  increases response times in applications utilizing multiple models. Delta-parameter pruning (DPP), particularly the random drop and rescale (DARE) method proposed by Yu et al., addresses this by pruning the majority of delta parameters—the differences between fine-tuned and pre-trained model weights—while typically maintaining minimal performance loss. However, DARE fails when either the pruning rate or the magnitude of the delta parameters is large. We highlight two key reasons for this failure: (1) an excessively large rescaling factor as pruning rates increase, and (2) high mean and variance in the delta parameters.
To address these, we develop two algorithmic improvements: (1) DARq, which modifies the rescaling factor in DARE, leading to significant performance gains at high pruning rates (e.g., >30% on COLA and SST2 for encoder models, with even larger improvements in decoder models), and (2) AdamR, an in-training modification that incorporates appropriate Delta regularization before applying DPP. We also demonstrate that DARq can be seamlessly combined with vanilla parameter-efficient fine-tuning techniques like LoRA and can facilitate structural DPP. Additionally, we revisit the application of importance-based pruning techniques within DPP, demonstrating that they outperform random-based methods when delta parameters are large. Through this comprehensive study, we develop a pipeline for selecting the most appropriate DPP method under various practical scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes improved algorithms for Delta-Parameter Pruning (DPP), notably DARq and AdamR, which achieve substantial performance gains at high pruning rates.   It begins with a comprehensive analysis of DARE, an existing DPP approach, and leverages insights from this analysis to develop two enhanced algorithms. Furthermore, the proposed DARq method can be integrated with a parameter-efficient fine-tuning strategy to further minimize delta parameters. Additionally, the paper provides guidance on applying DPP across various scenarios.

### Strengths
1 The  paper provides a detailed analysis of DARE about the failure cases 

2 base on the observation of DARE, they proposed two improved methods

3 their present the effectiveness of their method through theoretical and experimental points.

4 good presentation for reading 

5 consider different scenarios

### Weaknesses
see questions

### Questions
1 could you explain why you present a different range of regulation strength instead of a unity strength range to better understand the trend of the scale of dp in the Figure 6 ?

2 how do you conduct the experiments on the different regulation strengths in Figure 4? do they keep all other hyperparameters the same?

3 have you try lora + adamr-l2/adamr-l1?

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
This work makes progress over DARE to obtain Prunable Delta Paramters at higher pruning rates. Towards this, the authors propose DARq, that modifies, the rescaling factor based on the insight that it is more prudent to look at output layer perturbations when pruning DPs as opposed to worrying about the expected change in delta parameters. The authors also propose to use AdamR, different from AdamW since it uses regularisation based on gradient norm, to obtain DPs that are more prunable than those obtained by AdamW. The authors also experiment with importance based pruning methods to show that they can obtain better result than random pruning. They also show that DARq works with structural pruning, LoRA.

### Strengths
S1. The problem considered is quite interesting and not well-addressed in the literature

S2. The paper is well written

S3. Empirical results evidently show that DARq is performs quite well. The other insights provided are valuable too.

### Weaknesses
W1. This paper seems quite exploratory. The authors do not conclude by providing a single method that they recommend to use for obtaining DPPs. While the authors present a flowchart (Figure 4), it does not provide a clear, single best approach. The lack of a definitive recommendation makes it difficult for practitioners to directly apply the findings. It would be more impactful if the authors could identify a specific configuration or set of parameters that consistently yields the best results across different scenarios, rather than presenting a range of options without clear guidance on which to prioritize.

W2. Conclusions derived from Theorem 3.1 seem misleading. The authors provide an upper bound as opposed to a lower bound. On line 229, authors claim "from Thm. 3.1 as p increases, the absolute difference in outputs $|h^{diff}_{i} |$ grows at a rate of $\mathcal{O}((1 − p)^{-\frac{1}{2}})$", which is incorrect. But rather, $|h^{diff}_{i} |$ grows at most by $\mathcal{O}((1 − p)^{-\frac{1}{2}})$. It's not clear how tight this bound is to precisely make subsequent analysis hold true. The analysis would benefit from a discussion of the tightness of this bound, perhaps by showing empirical evidence of how closely the observed growth rate matches the theoretical bound, or by providing a more detailed mathematical analysis to justify the claim that the bound is tight enough to be useful.


Typos:
Line 137: powerful

### Questions
Please refer to the weaknesses.

### Soundness
2

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
4

### Summary
The paper addresses limitations in the random-rescaling Delta-parameter pruning method (DARE), which struggles with high pruning rates or large mean/variance in delta parameters. To tackle this, the authors propose two new approaches: (1) DARq, a post-training rescaling modification strategy, and (2) AdamR, a DDP-aware fine-tuning method. They validate the effectiveness of these methods through experiments on various model architectures and datasets.

### Strengths
* This work provides a clear analysis of why DARE struggles with high pruning rates and large delta parameter mean/variance cases. Additionally, it includes a theoretical proof of DARq’s effectiveness as a modified rescaling strategy.
* The paper presents comprehensive experiments on both encoder- and decoder-based language models across multiple datasets. DARq, with various rescaling variations, consistently outperforms other state-of-the-art methods across models and datasets, demonstrating its robustness. Moreover, DARq can be combined with parameter-efficient tuning approaches, such as LoRA, broadening its applicability.
* The AdamR fine-tuning method achieves promising results, effectively maintaining performance even at high pruning rates.

### Weaknesses
 This paper only compares their method with DARE, but there are lots of other methods proposed in the neural network pruning community. I wonder how this method compares to some existing pruning methods. For example, measuring the importance of weights in the original model and pruning the delta parameters based on that.

### Questions
* In Table 3, could you elaborate on why global rescaling outperforms local rescaling?
* In Table 5, after a 0.99 pruning rate, the pruned model seems to be able to achieve better performance than the original and AdamR-L2 fine-tuned models. For instance, in the RoBERTa-COLA cell, it reaches 59.01 at a 0.99 pruning rate with a standard deviation of 1.26, indicating that it can outperform the unpruned model (59.27) in optimal test runs. Does this suggest the potential for further pruning? Could you experiment with even higher pruning rates to assess the method's limits?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors revisit delta-parameter pruning (DPP) for fine-tuned models, focusing on the limitations of the existing Random Drop and Rescale (DARE) method when dealing with high pruning rates or large delta parameters. They identify two key issues causing DARE's performance degradation: the excessively large rescaling factor at high pruning rates and the high mean and variance in the delta parameters. To address these challenges, they propose two algorithmic improvements:

1. **DARq**: A modification of DARE that adjusts the rescaling factor, leading to significant performance gains at high pruning rates.
2. **AdamR**: An in-training regularization technique that incorporates delta (L2) regularization during fine-tuning to control the mean and variance of delta parameters before applying DPP.

They demonstrate that their methods outperform the original DARE, especially at extreme pruning rates, and can be combined with parameter-efficient fine-tuning techniques like LoRA. Additionally, they show that importance-based pruning methods can outperform random-based methods when delta parameters are large.

The findings of this work seem very high utility and are of substantial increase in performance in edge cases where the original methods failed very strongly. A very good step forward for DPP methods.

### Strengths
- **Comprehensive Analysis**: The paper provides a thorough analysis of the limitations of the existing DARE method, identifying the root causes of its failure at high pruning rates.
- **Innovative Solutions**: The proposed methods, DARq and AdamR, are well-motivated and offer practical improvements over existing techniques.
- **Empirical Validation**: Extensive experiments on both encoder and decoder models across various datasets showcase the effectiveness of the proposed methods, with significant performance gains.
- **Flexibility and Compatibility**: The authors demonstrate that DARq can be combined with existing fine-tuning techniques like LoRA and can be used for structural pruning, increasing its practical utility.
- **Revisiting Importance-Based Pruning**: By exploring the application of importance-based pruning methods within DPP, they offer valuable insights into scenarios where these methods may be more effective.
- **Clear Recommendations**: The paper provides a practical pipeline for selecting the appropriate DPP method under different scenarios, which is valuable for practitioners.

### Weaknesses
 - **Complexity of Methods**: While the proposed methods are effective, they introduce additional complexity, such as tuning the rescaling factor \( q \) in DARq, which may require validation data or additional computations. The process of selecting this parameter is not fully clear, and the paper does not provide sufficient detail on how to efficiently determine the optimal value of \( q \) without incurring significant computational overhead or relying on a validation set. This lack of clarity could hinder the practical adoption of the method.
- **Limited Theoretical Depth**: The theoretical analysis, while helpful, could be further deepened to provide more rigorous guarantees or insights into why the proposed methods work. For example, a more detailed analysis of the convergence properties of AdamR and its interaction with the optimization landscape would be valuable. The paper does not provide a strong theoretical justification for the specific form of delta regularization used in AdamR, which could limit its generalizability.
- **Applicability Scope**: The methods are primarily validated on language models and NLP tasks; it would strengthen the paper to demonstrate their applicability to other domains or types of neural networks. The current experimental setup does not explore the performance of DARq and AdamR in areas such as computer vision or speech recognition, which are important for assessing the broader impact of the proposed techniques. The paper should include experiments on diverse architectures and tasks to demonstrate wider applicability.
- **Clarity in Presentation**: Some sections, particularly the methodology and theoretical analysis, could benefit from clearer explanations and more intuitive descriptions to make them accessible to a broader audience. The description of the AdamR method, for example, could be made more explicit, with a clearer explanation of how the delta regularization is incorporated into the optimization process. The paper could also benefit from more illustrative examples to clarify the practical implications of the proposed methods.
- **Dependence on Regularization**: The AdamR method relies on in-training modifications and specific regularization strategies, which may not always be feasible or may interact unpredictably with other training dynamics. The paper should provide more discussion on how the regularization strength in AdamR should be chosen. There is a lack of guidance on how to select the appropriate regularization strength for different tasks and models, which could lead to suboptimal performance if not carefully tuned.

### Questions
1. **Scalability and Applicability to Other Domains**: While your methods have shown impressive results on language models, have you considered how DARq and AdamR might scale to even larger models or different architectures beyond NLP? Specifically, do you anticipate any challenges or necessary modifications when applying these techniques to other domains such as computer vision or speech recognition?

2. **Automated Selection of Rescaling Factor in DARq**: The selection of the rescaling factor \( q \) in DARq appears to be crucial for maintaining performance after pruning. Have you explored automated methods for selecting \( q \) without relying on a validation set or manual tuning? For instance, could analyzing the statistics of the delta parameters during pruning provide a way to determine an optimal \( q \) more systematically?

3. **Impact of AdamR on Training Dynamics**: Introducing delta regularization through AdamR alters the fine-tuning process. How does this affect the convergence, stability, and overall training dynamics compared to standard fine-tuning methods? Are there any trade-offs, such as increased training time or complexity, that practitioners should be aware of when integrating AdamR into their training pipelines?

### Soundness
4

### Presentation
3

### Contribution
4
