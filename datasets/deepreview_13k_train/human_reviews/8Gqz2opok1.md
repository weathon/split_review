# C-Adapter: Adapting Deep Classifiers for Efficient Conformal Prediction Sets

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
Conformal prediction, as an emerging uncertainty quantification technique, typically functions as post-hoc processing for the outputs of trained classifiers. 
To optimize the classifier for maximum predictive efficiency, Conformal Training rectifies the training objective with a regularization that minimizes the average prediction set size at a specific error rate.
However, the regularization term inevitably deteriorates the classification accuracy and leads to suboptimal efficiency of conformal predictors.
To address this issue, we introduce \textbf{Conformal Adapter} (C-Adapter), an adapter-based tuning method to enhance the efficiency of conformal predictors without sacrificing accuracy. 
In particular, we implement the adapter as a class of intra order-preserving functions and tune it with our proposed loss that maximizes the discriminability of non-conformity scores between correctly and randomly matched data-label pairs.
Using C-Adapter, the model tends to produce extremely high non-conformity scores for incorrect labels, thereby enhancing the efficiency of prediction sets across different coverage rates.
Extensive experiments demonstrate that C-Adapter can effectively adapt various classifiers for efficient prediction sets, as well as enhance the conformal training method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces C-Adapter, an adapter-based tuning method designed to improve the efficiency of conformal predictors without compromising classification accuracy. This approach is highly relevant to uncertainty quantification, where conformal prediction frameworks generate prediction sets that, with a specified coverage rate, are likely to include the true class. C-Adapter seeks to optimize prediction efficiency while preserving or enhancing model accuracy, which holds significant potential for high-stakes applications such as medical diagnostics.

### Strengths
1. The results demonstrate that the proposed method significantly reduces prediction set sizes while maintaining accuracy.
2. C-Adapter is versatile, working effectively with a range of classifiers and showing strong compatibility with black-box models.
3. Empirical results indicate that C-Adapter performs consistently across various datasets, models, and evaluation metrics.
4. Minimal hyperparameter tuning and high computational efficiency make C-Adapter highly practical for deployment.

### Weaknesses
1. The primary concern with this paper is the lack of comparison with related methods. The authors tested the proposed C-Adapter across various benchmarks (Table 1), loss functions (Table 2), values of α (Table 3), and distribution shifts (Table 4), but did not include comparisons with other approaches in conformal prediction. This makes it difficult to assess the true novelty and performance gains of C-Adapter relative to existing techniques. For example, methods that directly optimize for set size or employ different nonconformity measures could provide a more robust baseline for comparison.
2. While the use of adapters for conformal prediction is a novel application, the concept of adapters itself is well-established. The insight for choosing adapters over other modules, such as LoRA, is not sufficiently discussed and would benefit from further elaboration. The paper should provide a more detailed justification for why adapters are particularly well-suited for this task compared to other parameter-efficient fine-tuning methods. Specifically, the paper lacks a discussion on how the structural properties of adapters, such as their placement within the network, contribute to the observed performance gains in conformal prediction.

### Questions
1. The authors are encouraged to include some related methods in the comparisons to provide a more comprehensive evaluation.
2. The motivation and insight for employing the Adapter module should be further emphasized to clarify its significance in the proposed approach.

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
The paper "C-Adapter: Adapting Deep Classifiers for Efficient Conformal Prediction Sets" introduces C-Adapter, a method that improves the efficiency of conformal predictors while preserving classification accuracy. By adding an adapter layer to trained classifiers, C-Adapter maintains top-k accuracy through label ranking preservation. It optimizes a unique loss function to enhance non-conformity score separation between correct and incorrect predictions, resulting in more efficient prediction sets. Tested on CIFAR-100 and ImageNet, C-Adapter significantly reduces prediction set sizes and outperforms existing methods like Conformal Training, adapting well across various classifiers and scoring functions with minimal computational cost.

### Strengths
Originality: The paper is original in proposing C-Adapter, an adapter-based method for improving the efficiency of conformal predictors while maintaining accuracy. Unlike traditional methods such as Conformal Training, which can compromise classifier performance, C-Adapter innovatively integrates an adapter layer that preserves label ranking to maintain top-k accuracy. The introduction of intra order-preserving functions and a new loss function tailored for conformal prediction is novel and adds depth to the methodology.

Quality: The quality of the work is strong, supported by both theoretical justifications and comprehensive empirical results. The authors provide a solid mathematical foundation for their approach, including proofs and detailed discussions on the properties of the proposed method. The experiments are well-designed and conducted across various benchmarks, such as CIFAR-100 and ImageNet, using multiple classifiers. This extensive evaluation highlights the robustness and effectiveness of C-Adapter. The paper also compares its method with existing solutions like Conformal Training and demonstrates clear improvements.

Clarity: The paper is generally clear, with a well-organized structure that guides the reader through the problem, methodology, and experimental results. The introduction and related work sections set the stage effectively, and the results are presented with informative figures and tables. However, the clarity could be further enhanced by simplifying some complex mathematical sections and providing more intuitive explanations. This would make the paper more accessible to readers who are not specialists in conformal prediction or the specific mathematical frameworks used.

Significance: The paper's contribution is significant, particularly for the field of uncertainty quantification in machine learning. C-Adapter presents a practical and adaptable solution that can be applied to a variety of classifiers and settings, including black-box models. Its ability to maintain classification accuracy while reducing prediction set sizes has practical implications for high-stakes applications such as medical diagnostics and financial forecasting, where efficient and reliable uncertainty estimates are crucial. The method's flexibility and minimal computational overhead further enhance its significance, positioning it as a valuable tool for both research and practical implementations.

### Weaknesses
While the paper provides strong theoretical support, certain sections, particularly those involving the mathematical underpinnings of intra order-preserving functions, may be difficult for readers unfamiliar with this concept. To improve accessibility, the authors could include a simplified overview or illustrative examples to help readers intuitively grasp the key ideas without needing extensive background knowledge. This would broaden the paper’s reach and make it more appealing to a wider audience.

While the paper briefly addresses distribution shifts using ImageNet-V2, a more detailed exploration or comparison with other methods in this context would strengthen the claim of C-Adapter’s robustness. Further experiments with synthetic or real-world data shifts could provide deeper insights into its performance under more varied conditions.

While the paper claims C-Adapter is insensitive to hyperparameters, the provided analysis on the parameter T is limited. A more comprehensive exploration of hyperparameter sensitivity, including the impact of different tuning strategies and settings, would help verify this claim. Showing how C-Adapter behaves under a variety of hyperparameter configurations can reassure practitioners of its reliability in different scenarios.

### Questions
While C-Adapter is shown to outperform Conformal Training (ConfTr), what are the specific conditions or datasets where ConfTr might still be preferable or complementary to C-Adapter?

The results indicate that C-Adapter improves conditional coverage. What are the underlying mechanisms that enable this improvement and how it compares to methods specifically tailored for conditional coverage?

The evaluation focuses on standard score functions (THR, APS, RAPS). How would C-Adapter perform with more specialized or non-standard score functions used in specific domains?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors proposed an adapter-based tuning strategy to enhance conformal prediction performance without sacrificing the model's performance. They implemented this adapter as a class of intra-order-preserving functions to maximize the discriminability of non-conformity scores between correctly and randomly matched data-label pairs. This approach achieved high non-conformity scores for incorrect labels, enhancing the efficiency of prediction sets across different coverage rates.

### Strengths
**S1.** The paper is very well written and presented. 

**S2.** The methodological development is well written, with a comprehensive background and related works. 

**S3.** I found the experimentation well-motivated, covering important ablation studies, including alpha, training strategy, adaptation strategy, and parameter $T$. The authors achieved considerable improvement across different feature extractor backbones. Besides, the experiments on alpha under THR and APS demonstrate the robustness of their C-Adapter strategy.

### Weaknesses
 **W1. Methodological Novelty.** I found the contributions made by the authors are somewhat limited. The intra order-preserving function is adapted from (Rahimi et al., 2020). Overall, the complete approach is somewhat like a combination of the existing SOTAs, including the intra order-preserving function, conformal training (Rahimi et al., 2020, Stutz et al., 2021). Other than the theoretical demonstration and an additional learnable layer (the adapter layer), I would suggest the authors to specifically highlight any other methodological contribution. 

**W2. Loss function explanation.** One of the limitations of their work is the quality of the approximation depends heavily on the choice of $T$, which seems to be not affected by the prediction set size that much, according to the experimental findings. What is the rationale behind the insensitiveness of their approach to this parameter $T$? Besides, they approximated the loss function with sigmoid which might not be strictly convex over the entire domain. Hence, this approximation might introduce non-convexities that could impact the convergence and optimization process.

### Questions
I tried to cover most of my concerns and questions in the *Weaknesses* section. I kindly request the authors to review that section.

### Soundness
3

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
3

### Summary
The submission presents a method to improve conformal training (Stutz et al 2021) for classification through an adapter-based tuning method. The authors claim significant efficiency improvements. The authors draw attention to an existing with conformal training - specifically that the regularization term in conformal training may deteriorate classifier accuracy, and offer a method to alleviate this. The key idea is to use intra-order-preserving functions (Rahimi et al. 2020) as an extra component applied to a pre-trained model. The authors demonstrate the synthesis of two methods through CIFAR-100 and ImageNet classification tasks.

### Strengths
To the best of my knowledge, no other work has introduced an “adapter” for conformal training to improve the efficiency of prediction sets. It combines two interesting works and presents interesting empirical results, albeit in limited settings. And could be interesting to the community. Given the clarifications in the authors’ response, I would be willing to increase the score.

The submission is clear, mostly technically correct, and experimentally rigorous. The main strength of the paper is its empirical findings. Although only applied to limited settings/tasks, the empirical results support their claims. Evaluating the effectiveness of C-Adapter on other tasks (NLP or time series), more SOTA architectures and potentially more impactful applications would provide a more comprehensive understanding of its capabilities and limitations.

### Weaknesses
The main weakness of the submission is that it lacks theoretical insight into the efficacy of the method. When does C-adapter perform better/worse than conformal training? Is this always guaranteed? Furthermore, the submission could use an in-depth theoretical analysis of the robustness of C-Adapter - its robustness to distribution shifts, adversarial examples, and noisy data. Theoretical investigations would significantly strengthen the claims of robustness made based on empirical observations.

With that being said, I have several concerns and questions for the authors:
1. The main motivation behind his paper is that increasing \lambda decreases the classification accuracy, leading to larger average size of prediction sets. However, this is not the case in Fig 1 (blue lines) presented - CIFAR-100 has a U shape, and ImageNet is almost flat. Please explain why this could be the case and why the relationships could differ between datasets.
2. The authors present a training objective designed to optimize the efficiency of conformal predictors over the entire range of alpha values (0, 1). Please explain why this was done. Practically, maybe only one \alpha value could be used. Does only optimizing for one \alpha value improve performance compared to all?
3. The authors test C-Adapter's performance when trained on ImageNet and then tested on ImageNet-V2. This approach evaluates how well the adapted model generalizes to a different but related dataset, simulating a distribution shift scenario. However, the authors say in page 10 - “Notably, coverage will not be affected under this setting, as the calibration and test sets remain exchangeable”. A distribution shift means that calibration and test sets are non-exchangeable. If this is the case, the claim that C-adapter is robust to distribution shift is not warranted. Please explain. Furthermore, quantification of the distribution shift (if there is) would significantly strengthen this claim.
4. Will the code and data be publicly available?

### Questions
With that being said, I have several concerns and questions for the authors:
1. The main motivation behind his paper is that increasing \lambda decreases the classification accuracy, leading to larger average size of prediction sets. However, this is not the case in Fig 1 (blue lines) presented - CIFAR-100 has a U shape, and ImageNet is almost flat. Please explain why this could be the case and why the relationships could differ between datasets.
2. The authors present a training objective designed to optimize the efficiency of conformal predictors over the entire range of alpha values (0, 1). Please explain why this was done. Practically, maybe only one \alpha value could be used. Does only optimizing for one \alpha value improve performance compared to all?
3. The authors test C-Adapter's performance when trained on ImageNet and then tested on ImageNet-V2. This approach evaluates how well the adapted model generalizes to a different but related dataset, simulating a distribution shift scenario. However, the authors say in page 10 - “Notably, coverage will not be affected under this setting, as the calibration and test sets remain exchangeable”. A distribution shift means that calibration and test sets are non-exchangeable. If this is the case, the claim that C-adapter is robust to distribution shift is not warranted. Please explain. Furthermore, quantification of the distribution shift (if there is) would significantly strengthen this claim.
4. Will the code and data be publicly available?

### Soundness
3

### Presentation
3

### Contribution
3
