# Linear Combination of Saved Checkpoints Makes Consistency and Diffusion Models Better

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
\vspace{-0.8cm}
  Diffusion Models (DM) and Consistency Models (CM) are two types of popular generative models with good generation quality on various tasks. When training DM and CM, intermediate weight checkpoints are not fully utilized and only the last converged checkpoint is used. In this work, we find that high-quality model weights often lie in a basin which cannot be reached by SGD but can be obtained by proper checkpoint averaging. Based on these observations, we propose \nameshort{}, a simple but effective and efficient method to enhance the performance of DM and CM, by combining checkpoints along the training trajectory with coefficients deduced from evolutionary search. We demonstrate the value of \nameshort{} through two use cases: \textbf{(a) Reducing training cost.} With \nameshort{}, we only need to train DM/CM with fewer number of iterations and/or lower batch sizes to obtain comparable sample quality with the fully trained model. For example, \nameshort{} achieves considerable training speedups for CM (23$\times$ on CIFAR-10 and 15$\times$ on ImageNet-64). \textbf{(b) Enhancing pre-trained models.} Assuming full training is already done, \nameshort{} can further improve the generation quality or speed of the final converged models. For example,  \nameshort{} achieves better performance using 1 number of function evaluation (NFE) than the base model with 2 NFE on consistency distillation, and decreases the NFE of DM from 15 to 9 while maintaining the generation quality on CIFAR-10.
  
  
  
  
  \keywords{Consistency Model \and Diffusion Model \and Weight Averaging \and Evolutionary Search}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes LCSC (Linear Combination of Saved Checkpoints), a method to improve the performance and efficiency of diffusion and consistency models. The underlying idea is to use an optimal linear combination of model checkpoints saved during training. These optimal coefficients are determined using an evolutionary search method. The authors demonstrate that this approach can not only decrease the training cost but also enhance the performance of pre-trained models. The experiments which were performed on CIFAR-10 and ImageNet-64 provably demonstrate that this approach results in an increase in training time and improvements in evaluation metrics.

### Strengths
- The simple methodology presented seems to have a well-motivated theoretical basis, and is quite effective in improving the training of diffusion and consistency models. Further, this method does not require backprop and side steps the need for differentiable loss functions through the evolutionary search.
- The analysis presented on the method along with the visualizations of the landscape to demonstrate that optimal model weights lie in basins which are inaccessible by optimization but may be accessible through checkpoint averaging.
- It has clear value in reducing compute time and improving model performance as demonstrated through the experiments. Seems like there's speedups by an order of magnitude which is quite impressive.

### Weaknesses
See questions

### Questions
- Currently, the experiments seems to be limited to image generation tasks. Would it be possible to demonstrate this to another diffusion task such as audio or video?
- Have you studied how these coefficients change over the course of training? There perhaps maybe an interpretability study to understand the importance of different stages of training on the best performance
- On a similar front, can it be extended to layers? That is, composition of weights on layers may differ from the composition of overall weights and perhaps lead to a better result?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a method named LCSC for training diffusion models by linearly combining the intermediate weight checkpoints using an evolutionary algorithm. LSCS can significantly reduce the training cost of a diffusion model without sacrificing the generation quality. In addition, a pre-trained diffusion model can achieve better performance by fine-tuning with LCSC with few training iterations. The numerous experiment results are provided to demonstrate the effectiveness of LCSC in different datasets.

### Strengths
(1) The motivation is clear and easy to understand. The authors also provide theoretical analysis about why LCSC is better than EMA.

(2) The method is simple and straightforward, which uses the evolutionary search to linearly combine checkpoint weights. It seems that LCSC can be easy to implement and applied with different diffusion models.

(3) As shown in the experiment results, LCSC can significantly reduce the training cost of a diffusion model and enhance the pre-trained diffusion models. 

(4) The authors provide a lot of experiment results to study LCSC from different aspects.

### Weaknesses
(1) It seems that the experiments about reducing the training cost only focus on datasets with small resolution (CIFAR-10 and ImageNet-64). I understand that the cost for training a diffusion model on a dataset with large resolution (e.g, LSUN-bedroom, COCO) from scratch is more expensive. I believe that such a set of experiments can make the LCSC more attractive. The lack of high-resolution experiments limits the assessment of LCSC's scalability and practical applicability in real-world scenarios where high-fidelity image generation is often required. Specifically, the computational demands and memory requirements for high-resolution image generation can expose potential bottlenecks or limitations of the proposed method that are not apparent in lower-resolution settings. Furthermore, the generalization capability of LCSC to more complex data distributions present in high-resolution datasets remains unclear.

(2) In my opinion, the experiment results about text-to-image generation are not convincible enough to validate the effectiveness of LCSC. The number of training iterations for fine-tuning LCM with LoRA is very small, which is only 6K with the batch size of 12. The authors should use a larger number of training iterations, or show that the generation quality of LCM will not improve with further training. I'm wondering whether the experimental settings for evaluating LCM with LCSC is suitable, since the generated images (Figure 2 and Figure 10) are in anime style while CC12M and MS-COCO are not. Besides the LCM, the authors could also fine-tune the pre-trained Stable Diffusion v1.5 for a few iterations with LCSC to see if LCSC can further enhance it. The current evaluation lacks a thorough investigation into the impact of LCSC on text-to-image generation with diverse styles and datasets, which is crucial for establishing its robustness and generalizability. The use of a single style (anime) for evaluation raises concerns about potential biases and limitations in the assessment of LCSC's performance.

### Questions
(1) Can LCSC reduce the training cost of DM (not CM)? I only find experiments about reducing training cost with consistency distillation and consistency training but not vanilla DDPM. 

(2) It seems that most experiments are based on CM. Do you think LCSC is more suitable for CM and CD compared with DM? And why?

(3) Could you provide the CLIP-score for text-to-image generation?

### Soundness
3

### Presentation
2

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
The authors introduce a novel approach to enhance the performance and reduce the training costs of Diffusion Models (DM) and Consistency Models (CM) by learning a linear combination of saved checkpoints using evolutionary algorithms. The paper builds upon existing theoretical frameworks, demonstrating that Exponential Moving Average (EMA) models converge faster than their last-tier counterparts under specific conditions. Through a motivational experiment involving a grid search over numerous linear combinations of three checkpoints (with and without EMA), the authors reveal the existence of superior solutions compared to the traditional EMA approach. The proposed method, termed Linear Combination of Saved Checkpoints (LCSC), is further validated experimentally, showing significant reductions in training costs via fewer iterations and smaller batch sizes, as well as improvements in generation quality when applied to fine-tuned checkpoints.

### Strengths
1. Impressive Experimental Results: The experiments, particularly those presented in Tables 1 and 2, convincingly demonstrate the efficacy of LCSC for both CD and CT, showcasing significant reduction in training costs.
2. Innovative Findings: Figures 4 and 6 highlight the potential for significantly better linear combinations of checkpoints than the naive EMA solution, indicating a promising direction for future research.
3. Theoretical Foundation: The theoretical analysis providing insights into the convergence behavior of EMA models adds depth and credibility to the proposed method.
4. Practical Implications: By achieving speedups of up to an order of magnitude or more, LCSC offers tangible benefits in reducing computational resources and training time, which is highly relevant in the context of large-scale model training.

### Weaknesses
1. Search Cost Disparity Between DM and CM: Tables 8 and 9 indicate that the search cost is more substantial for Diffusion Models (DM) compared to Consistency Models (CM), suggesting that LCSC is less effective in reducing training costs for DM. This is particularly concerning given that DMs often require significantly more computational resources than CMs, making the higher search cost a practical limitation. The paper should more clearly address the implications of this disparity, especially considering the computational demands of large-scale DM training.
2. The coefficients derived by the evolutionary algorithm (EA) lack interpretability, with some being significantly large (>6) and others near zero (Fig. 8). Additionally, coefficients learned from different seeds show considerable disagreement, despite yielding similar performance improvements (as seen in Fig. 9). The lack of interpretability may hinder the understanding of the model's behavior and its generalizability. It also raises concerns about the possibility of overfitting. The large magnitude of some coefficients, combined with the variability across different runs, suggests that the optimization process might be unstable or sensitive to initial conditions. This makes it difficult to understand what each checkpoint contributes to the final model.

### Questions
1. Potential Overfitting of Weights (Fig. 8): The weights depicted in Fig. 8 exhibit large absolute values (greater than 6), which might indicate overfitting. Could the authors address the following points?
- Regularization: Were any regularization techniques employed to constrain the magnitude of the coefficients?
- Interpretability: What is the theoretical or intuitive justification for assigning such large weights to certain checkpoints?
2. Convergence Curves Post-LCSC Application: Visualizing the convergence behavior after applying LCSC can provide a clearer understanding of its impact on training dynamics. Including convergence curves would help illustrate how LCSC influences the training process compared to baseline methods like EMA.
3. Convergence Curve of LCSC itself. How many iteration of evolution does it undertake before achieving a satisfactory solution?
4. Add experiments for further assessing the robustness of LCSC-Derived Coefficients.
5. Enhancing Interpretability of Coefficients: Understanding the role and significance of each coefficient can aid in demystifying the model's behavior. Implementing constraints or regularization techniques to limit the magnitude of coefficients may improve their interpretability. Alternatively, providing a theoretical justification or empirical analysis explaining the distribution of coefficient values can enhance comprehension.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper targets the efficient training problem for diffusion models and consistency models. They find that proper checkpoint merging can significantly improve the training convergence and final performance. Therefore they develop an evolutionary search algorithm for linearly combining the checkpoints. The experiments showcase their LCSC can reduce the training cost and enhance the performance of pre-trained diffusion models.

### Strengths
1. The finding that proper checkpoint merging can significantly improve the training convergence and final performance is novel and interesting to me.
2. The theoretical analyses for EMA are promising and solid.
3. The experiments are extensive and convincing.

### Weaknesses
1. The details for how to get the metric landscapes are missing. Do you apply a grid search for all $x,y$ with the formula $\theta_{(x, y)}=\theta_{n_0}+x\left(\theta_{n_1}-\theta_{n_0}\right)+y\left(\theta_{n_2}-\theta_{n_0}\right)$. If so, what is the grid interval? And what is the interval between $n_0$, $n_1$ and $n_2$? It is quite strange that the optimal points are always located inside of the regions surrounded by $n_0$, $n_1$, and $n_2$. Does it mean the models are always oscillating? Please provide more explanation.
2. The claim in lines 528-529 that "a small subset of weights is characterized by coefficients of large magnitude" is interesting but needs more evidence. It's not clear how this is quantified or what the threshold for 'large magnitude' is. A more rigorous analysis, perhaps involving statistical measures of the coefficient distributions, would be beneficial.
3. Please provide more insights about why the coefficients of some iterations in Figure 5 are negative. It is clear that the negative coefficients mean the models at these iterations have a negative effect on the final performance but why does this happen? Is it because the models at these iterations have a relatively lower FID? This needs more investigation into the properties of these specific checkpoints and their impact on the merged model.

### Questions
1. How to get such smooth metric landscapes?
2. How to prove "a small subset of weights is characterized by coefficients of large magnitude"?
3. Why do the models at some iterations have negative coefficients?

### Soundness
3

### Presentation
4

### Contribution
3
