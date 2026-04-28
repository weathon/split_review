# AutoTune for Time Series Transformers using Low Rank Adaptation and Limited Discrepancy Search

- Decision: Reject
- Avg Score: 3.00
- Scores: 5, 3, 1

## Abstract
Transformer models have achieved remarkable results in the field of Natural Language Processing (NLP) with the introduction of breakthrough large language models like GPT and LLaMA recently. Motivated by their ability to capture long-range dependencies, researchers have successfully adapted these models to the task of time series forecasting. However, despite their potential, effectiveness of applying these pre-trained time series transformer models in the target domain is limited due to the need for hyper-parameter optimisation to match the characteristics of the target domain. This paper presents a novel algorithm that uses parameter efficient fine-tuning such as Low Rank Adaptation (LoRA) coupled with Limited Discrepancy Search (LDS) to efficiently auto fine-tune pre-trained time series transformers for a given target domain. Our approach helps in making informed design choices involving LoRA tunable hyper-parameters with strong performance-cost trade-offs that are highly transferable across different target domains. Our experiments demonstrate that autotune efficiently identifies the optimal configuration of LoRA hyper-parameters, achieving an average MASE
improvement of 5.21% across all datasets and 4.76% for out-of-domain datasets compared to zero shot pre-trained models, with improvements as high as 20.59% for one of the out-of-domain datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel method for automatic tuning of time series Transformer models, combining Low Rank Adaptation (LoRA) and Limited Discrepancy Search (LDS). The method aims to efficiently fine-tune pre-trained models, addressing the computational complexity associated with full parameter fine-tuning. LDS is used to optimize the hyperparameters of LoRA to enhance the model's adaptability to target domain tasks. Experimental results demonstrate that the proposed automatic tuning method outperforms both zero-shot and full fine-tuning approaches on most datasets, particularly in unseen target domains.

### Strengths
- The paper presents an efficient parameter tuning scheme for Transformer models in time series forecasting by combining Low Rank Adaptation (LoRA) with Limited Discrepancy Search (LDS).

- The effectiveness of Autotune is demonstrated through experiments on multiple datasets.

### Weaknesses
1. **Experimental Design Limitations**:
   - (1) The main experiments lack performance reports of Autotune on different sizes of the Chronos models. Although the authors stated that only the smallest model size was used to validate the proposed method's applicability, they also compared the performance of all sizes of Chronos T5 models under a zero-shot setting. Therefore, reporting the Autotune results for all model sizes would make the findings more convincing. Specifically, the absence of results on larger models leaves open the question of whether the observed benefits of Autotune are consistent across different model capacities, or if the method's effectiveness diminishes or changes with increased model size. This is crucial for understanding the scalability of the proposed approach.
   - (2) The evaluation metric is singular. Although MASE reflects the overall performance improvement, it fails to capture other characteristics such as overfitting risks, error distribution, and extreme value prediction capabilities. The original Chronos-T5[1] also used WQL, and the work [2] employed additional metrics such as MSE and DTW. The use of a single metric limits the understanding of the model's behavior under different aspects of forecasting performance. For example, a model might achieve a good MASE score while still struggling with predicting extreme values, which is important in many real-world applications. A more comprehensive evaluation would include metrics that assess different facets of the model's performance.
   - (3) Missing ablation study. The authors used the LDS search algorithm to find the optimal LoRA hyperparameter settings, but there is no ablation study on the LDS algorithm itself. Including a comparison with the best hyperparameters selected after n random trials would help demonstrate the significance and necessity of the LDS algorithm. Without this comparison, it is difficult to ascertain whether the LDS algorithm is truly providing a benefit over a simpler random search strategy, or if the observed improvements are merely due to the exploration of a larger hyperparameter space.

2. **Limited Novelty**:
   - Although the authors claim that this is the first work to explore parameter-efficient fine-tuning in time series forecasting (Line 56), there are earlier studies that have explored this area (e.g., Low-Rank Adaptation of Time Series Foundational Models for Out-of-Domain Modality Forecasting). Furthermore, the effectiveness of the LDS search algorithm has not been sufficiently validated through ablation studies. The lack of a thorough comparison with existing parameter-efficient fine-tuning methods makes it difficult to assess the true novelty and contribution of this work.

3. **Writing Issues**:
   - The citation format throughout the paper results in unclear and difficult-to-understand statements, such as those in Lines 38-42.

### Questions
1. Why was only one evaluation metric chosen? Are there any specific reasons related to the task setup for this decision?

2. Why were ablation studies and parameter analysis experiments not provided? Most of the figures in the experimental section only report the MASE scores compared to the baseline across different datasets, adequately demonstrating the effectiveness of the proposed method. However, would including ablation studies on the LDS search algorithm make the findings more persuasive?

3. How efficient is Autotune? After fine-tuning multiple hyperparameters and selecting the best-performing model on the validation set, is there a significant improvement compared to randomly selecting a set of hyperparameters (e.g., from Table 2) for a single LoRA fine-tuning?

4. Can the necessity of the LDS algorithm be demonstrated? The authors could provide a performance comparison by randomly selecting parameters from Table 2, training the model, and selecting the best-performing model on the validation set after n iterations.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a new method for autotune time series transformers, combining Low Rank Adaptation (LoRA) and Limited Discrepancy Search (LDS) to efficiently perform parameter optimization on pre-trained time series models. In this paper, LoRA is used for efficient parameter tuning, and LDS is combined to explore the optimal hyperparameter configuration to make the model perform better in the target domain. Experimental results show that compared with the zero-shot pre-trained model and the traditional full-parameter fine-tuning, the proposed method achieves better performance on multiple datasets.

### Strengths
1. This paper proposes an innovative automatic tuning method that combines the efficient parameter fine-tuning of LoRA and the search strategy of LDS to solve the problem of adaptability of large-scale models in time series.
2. Experimental results show that the proposed method has significant performance improvement on multiple datasets, especially on some target domain datasets, which has significant advantages over zero-shot models.
3. In the process of LoRA fine-tuning, only a small number of parameters need to be adjusted, which significantly reduces the requirements of computing resources compared with full-parameter fine-tuning, thus greatly saving the computing cost.
4. This paper shows that the method has achieved good results on a variety of target domain datasets, showing the versatility and adaptability of the method.

### Weaknesses
1. Although LoRA is suitable for efficient parameter fine-tuning, its application is mainly concentrated in the case of large differences between the target domain and the source domain, and the effect improvement in some specific fields is limited. Furthermore, the effectiveness of LoRA can be highly sensitive to the choice of rank, and the paper does not explore this sensitivity in detail, which could lead to suboptimal performance if not carefully tuned for each dataset.
2. Although LDS optimizes the search space to a certain extent, its essence is still a depth-first search based on limited differences, and the search efficiency may be limited in the face of a larger hyperparameter space. The paper does not discuss the potential for LDS to get stuck in local optima, especially when the hyperparameter space is non-convex, which is common in deep learning models.
3. The use of LDS for hyperparameter searching in LoRA is a key innovation presented in this paper; however, the article does not provide a detailed experimental analysis of this method. It remains unclear whether LDS leads to a reduction in search iterations or an improvement in search efficiency compared with other hyperparameter search methods, such as Bayesian optimization or random search. The paper lacks a comparative analysis of the computational cost and performance of LDS versus these alternatives.
4. This paper employs LoRA as a fine-tuning method for time series forecasting models, demonstrating competitive results compared to zero-shot and full fine-tuning methods. However, as LoRA is already established as a general parameter-efficient fine-tuning approach, such results are widely evidenced in the literature, which, consequently, diminishes the contribution of this paper. The paper does not adequately address the novelty of applying LoRA to time series, given its established use in other domains.
5. Although the paper compares the zero-shot model and the full-parameter fine-tuning, it does not make an in-depth comparison of other advanced fine-tuning methods, such as Adapter or other AutoML strategies, which limits the comprehensiveness of the comparison results. The lack of comparison with other parameter-efficient fine-tuning techniques makes it difficult to assess the true advantage of the proposed approach.

### Questions
I have some doubts about the specific implementation details of the combination of LDS and LoRA in the paper. For example, the selection criteria for LDS and how to effectively handle the size of the hyperparameter space, and whether tuning on different datasets will be affected by specific hyperparameters. In addition, there is a clear definition of the "optimal" hyperparameters in the experimental setup, which may affect the interpretation of the results.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper covers the application of Limited Discrepancy Search (LDS) to optimize LoRA finetuning for transformer-based time-series forecasting models (Chronos in this case). The core idea is to optimize the LoRA training hyperparameters to automate the finetuning of time-series forecasting models for downstream tasks. The authors present results on several different datasets from different domains. They fix the hyper-parameter search space so that each parameter has a finite set of values. They then compare their results versus the zero-shot chronos model, the fully finetuned version and the autotuned version. They show that on average their method increases performance relative to the other versions.

### Strengths
1.	Auto-tuning of time-series models is relatively understudied
2.	They perform their tests on several datasets from a wide range of domains
3.	They choose a model architecture which comes in a range of sizes which makes the results more interesting

### Weaknesses
1.  The novelty is lacking. This research takes a pretrained model and applies LoRA finetuning to it with a new method of hyperparameter tuning. Most of these concepts are not new for time-series analysis
2.  The paper claims to increase performance but often this strategy does not improve the quality of the forecasting. Given that you are finetuning the model for a downstream task how is it that the performance is getting worse in some cases (Table 3 and 4)?
3.  You claim the autotuned model method is improving the performance but what if you simply finetune the models with LoRA and a standard set of hyperparameters would the performance be the same as your method? This is a question you need to answer clearly.
4.  Why do you need figure 5 and table 4? Its looks like it is showing the same thing, it looks like you were trying to fill the space. Figure 4 also looks unnecessarily large and is a generally convoluted way of showing the results.
5.  Why would you not apply this method to each model size, why is it only applied once?
6.  The tuning strategy only seems to be applied to the mini model, a key advantage of LoRA is that you can train a larger model with less compute. Which is the opposite of what was chosen here.
7.  Why are there standard deviations in table 3 but not in table 4.
8.  Figure 2 is not centered
9.  Some references should be in parathesis (for example line 38).
10. All of these models tested are relatively small and could be trained on somewhat accessible hardware even for academia. Why apply LoRA in this case?

### Questions
In general ,I think this paper is too low impact for this conference. Their strategy lacks novelty and the results are not rigorous enough. Particularly in the validation of their method. I do have some questions pertaining to the weaknesses mentioned above:
1. Why did you not compare to a model finetuned using LoRA with default hyperparameters?
2. Can you show how this works with other models? There are many other pretrained time-series forecasting models you could do this with.
3. How does this method improve the accuracy over other existing hyperparameter searching methods?
4. Finetuning a model for time-series analysis with LoRA is not novel, performing a hyperparameter search for the LoRA hyperparameters is not novel, how do we know that the performance increases are due to the use of the LDS algorithm with LoRA?

### Soundness
2

### Presentation
1

### Contribution
1
