# Sassha: Sharpness-aware Adaptive Second-order Optimization with Stable Hessian Approximation

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Approximate second-order optimization methods have gained attention due to their low computational and memory overhead.
While these methods have the potential to accelerate neural network training, they often exhibit poorer generalization compared to first-order approaches. To address this limitation, we first analyze existing second-order methods through the lens of the loss landscape, demonstrating that their reduced generalization performance is somewhat attributed to the sharpness of the solutions they converge to. In response, we introduce Sassha, a novel approach designed to enhance generalization by explicitly reducing sharpness. In fact, this sharpness minimization scheme is designed to accommodate lazy and stable Hessian updates, so as to secure efficiency and robustness besides flatness. To validate its effectiveness, we conduct a wide range of deep learning experiments including standard vision and language tasks, where Sassha achieves competitive performance. Notably, Sassha demonstrates strong generalization in noisy data settings and significantly outperforms other methods in these scenarios. Additionally, we verify the robustness ofSassha through various ablation studies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose Sassha, a second-order optimizer combining ideas from sharpness-aware minimization and lazy second-order optimization. They provide experiments on image (CIFAR, ImageNet) and language (Glue, wikitext-2) tasks, reporting improved performance over baseline methods.

### Strengths
The paper is well-structured and written, and the overall presentation is good. It is easy to understand the central ideas and several questions I had when reading the paper were addressed shortly after with a suitable ablation study. The experimental results comparing Sassha to other second-order optimizers are convincing, and the gains over those baselines seem consistent. In general, the experimental evaluation is broad in terms of models and datasets. The ablation studies about why the lazy Hessian updates might benefit from SAM are insightful and support the claims made (although I have a few questions, see below).

### Weaknesses
 **Novelty**

In my understanding, the presented method can be seen as applying SAM to Sophia-H as base-optimizer, with a few tweaks (using the square root and changing the clipping function of Sophia for bias correction). While I am unaware of work investigating SAM with second-order optimizers explicitly, it is well-known that adding SAM typically improves over the respective base-optimizers for many cases (e.g. SGD, Adam, AdamW, Lion, …) on the investigated datasets. I, therefore, think that it is not very surprising that also second-order methods benefit from SAM-like training. The main novelty and contribution of this work seem limited to the additional tweaks required when using second-order optimizers as SAM base optimizers. However, the performance of plain Sophia + SAM is not explored in comparison to Sassha.

**Comparison to SAM**

While Sassha improves over other second-order methods, the improvements over SAM-like methods are less clear. For Cifar, the results are relatively close, sometimes within standard deviations or even lower for the same computational budget (Table 14). For ImageNet, it would be good to see the models trained to convergence (e.g. 300 epochs). Additionally, I could not find the search space for the SAM parameter rho in these experiments. Assuming it matches the range reported for the label noise experiment (Table 13), I recommend trying slightly larger rho values and reporting results, ideally with accuracy vs. rho plots (as e.g. seen in Figure 5a of Becker et al. [1]), to allow a more thorough comparison between SAM and Sassha. For the language tasks, the comparisons to SAM are missing completely. Finally, to prove that Sassha is a sensible approach as a stand-alone method, comparisons to other SAM-like optimizers (e.g. [2], ...) would be necessary. In terms of presentation, I suggest including the SAM numbers in the Tables in the main paper alongside the second-order methods instead of the Appendix. 

**Unclear motivation for the square root**

The choice to use the square root of the Hessian needs further explanation. The authors state that “underestimating curvature seems to be more prevalent under sharpness minimization,” but it is unclear if there are experiments directly supporting this claim. They suggest that training instabilities may result from certain entries approaching zero, but this alone does not justify using the square root, as similar stability could be achieved by adding a small scalar value or using clipping operations that preserve larger values, which might align better with the derivations in Section 4.1. A more detailed discussion of the square root’s impact on optimization—beyond mitigating instabilities from small Hessian entries—would be valuable. In the experiment on lazy Hessian training, both the square root and SAM are omitted, which (to my understanding) effectively reduces the algorithm to Sophia-H, with clipping instead of bias correction as the only difference.

### Questions
- Can the authors explain why Sophia-H and AdaHessian are so slow in terms of wall clock time (G.3)?
- Also, part of the speedup compared to Sophia-H might vanish when Sophia-H is used with a k-interval like Sassha. I think this should be stated more clearly.
- Is there a reason that Sophia-H is investigated, but Sophia-G is omitted?
- Did the authors use Shampoo or distributed Shampoo?


Minor remarks:

- In line 113 a reference is missing
- In Figure 5 the captions b) and c) don’t align with the y-axis label
- I suggest including the pseudo-code (Algorithm 1) in the main paper, since from Section 4 alone it is unclear what the final algorithm looks like.

### Soundness
3

### Presentation
4

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
This paper firstly investigates the solution sharpness of different second-order optimizers, pointing out that current second-order optimizers tend to converge to sharp solutions. Based on their findings, the authors combine SAM and second-order optimizers and design a sharpness-aware second-order optimizer, Sassha. Experiments show that Sassha can get better solutions than other second-order optimizers and is more robust to label noise than other second-order optimizers and SAM.

### Strengths
1. The perspective to investigate the sharpness of solutions obtained by second-order optimizers is novel, inspiring the community to design sharpness-aware second-order optimizers.
2. The findings of the lazy Hessian updates with SAM is interesting. I believe this deserves deeper investigations.
3. The robustness to label noise of Sassha is important.

### Weaknesses
1. The technical contribution of Sassha is minor, since Sassha just combine SAM and common second-order optimization techniques.


2. Although Sassha beats other second-order optimizers, its improvement seems incremental in standard training. The authors claims second-order optimizers converge faster than first-order optimizers, but Sassha is evaluated with the same training epochs (and Sassha needs one more forward-backward propagation). I thihk Table 6 shows the convergence advantage of Sassha, but the comparison only includes SAM and ViT model. Moreover, they did not compare SAM in stardard training, which seems that Sassha cannot performs better than SAM with same training budget.
    
    Overall, I think the authors should compare Sassha with other baselines including SAM under the same training time to validate the effectiveness.


3. It lacks deeper investigations why second-order optimziers converge to sharper solutions. The current paper just shows the phenomenon without any intuitive or theoretical results.

### Questions
1. In Table 7, why the average sharpness of SGD and SAM is negative values?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper targets the issue of poor generalization in second-order deep learning optimization methods, which has been a significant barrier to wider application despite their theoretical advantages. This work first provides empirical evidence that existing second-order methods converge to sharper minima compared to SGD, potentially explaining their inferior generalization. The authors thus propose SASSHA, which combines sharpness-aware minimization with efficient second-order optimization, incorporating several technical innovations for stability and efficiency. The method is evaluated on computer vision and language tasks, showcasing consistent improvements over both first-order and second-order baselines. The theoretical analysis, while preliminary, provides useful insights into the convergence properties. The experimental results support the main claims, showing improved generalization, computational efficiency, and robustness to label noise.

### Strengths
**(S1) Clear and reasonable motivation:** The paper attempts to bridge second-order optimization with sharpness awareness, a direction that holds some merit. The systematic investigation connecting second-order optimization with solution sharpness is insightful, supported by comprehensive empirical evidence using multiple complementary metrics (eigenvalue analysis, loss perturbation, trace calculations). 

**(S2) Technical Soundness:** The integration of sharpness awareness into second-order optimization is done thoughtfully, with each component carefully designed and theoretically justified. The square root pre-conditioner is a clear and insightful design that effectively addresses the numerical instabilities inherent in second-order methods while maintaining computational efficiency. The lazy Hessian update scheme demonstrates favorable trade-offs in second-order optimization, providing significant computational benefits without sacrificing performance.

**(S3) The Presentation Clarity:** This manuscript demonstrates reasonable organization and writing clarity that makes its technical content accessible. The progression from motivation through empirical observation of second-order methods' convergence to sharp minima to the proposed SASSHA method, follows a logical flow. The experiments are presented in a systematic manner with appropriate tables and figures, particularly the visualization of loss landscapes in Figure 2 which effectively shows the sharpness differences between optimizers. While the mathematical notation is mostly consistent and the algorithmic description is complete, the authors could have provided more intuitive explanations of key concepts, especially regarding the interaction between sharpness awareness and second-order information.

### Weaknesses
 **(W1) Technical Originality:** However, the core idea of combining sharpness-awareness with second-order information is relatively straightforward and could be considered incremental. The empirical investigation of sharpness measures largely confirms known intuitions about the relationship between curvature and generalization. The technical contribution, while potentially useful and providing knowledge advancement to the optimization community, builds directly on existing work (SAM and diagonal Hessian approximation) with limited fundamental breakthroughs.

**(W2) Critical Experimental Gaps:** The experiments suffer from significant oversights that cast doubt on the method's practical applications. The authors avoid testing on large-scale models (>100M parameters), raising questions about the scalability to modern deep neural networks. Furthermore, the absence of results on fundamental computer vision tasks, such as object detection and semantic segmentation,  suggests potential limitations in the performance consistency of the method. More importantly, the paper lacks comparison with recent sharpness-aware variants like ASAM [1] and GSAM [2], making it impossible to assess whether the proposed method represents genuine progress in the field.

**(W3) Technical Concerns:** The square root pre-conditioner, while empirically shown to provide stability benefits, appears to be an arbitrary choice without a rigorous mathematical foundation. The authors fail to explore or justify why this specific power transformation is optimal, neglecting to investigate other potential functional forms that might provide superior conditioning. The hyper-parameter k for Hessian update intervals introduces additional complexity to the already challenging problem of tuning optimization parameters, yet the paper provides insufficient guidance on its selection across different architectures and tasks. In addition, the memory requirements of storing and updating the diagonal Hessian approximation, though lower than full second-order optimizers, could still be prohibitive for large-scale applications, especially in resource-constrained environments. I recommend the authors provide additional experiments and discussions on these aspects.


**(W4) Implementation Complexity:** The proposed SASSHA method requires maintaining multiple sets of statistics and careful coordination between the sharpness-aware perturbation and Hessian approximation components. The potential for numerical instability in regions of low curvature is particularly worrying, as the paper does not provide robust safeguards against such scenarios. The absence of adaptive strategies for crucial hyper-parameters like the perturbation radius means practitioners must rely on costly trial-and-error tuning. 

### Questions
Please refer to Weaknesses for detailed questions. I hope my review helps to further strengthen this paper and helps the authors, fellow reviewers, and Area Chairs understand the basis of my recommendation. I also look forward to the rebuttal feedback and further discussions, and would be glad to raise my rating if thoughtful responses and improvements are provided.


## **-------------------- Post-Rebuttal Summary --------------------**

The additional experiments, discussions, and revised manuscript provided by the authors have significantly strengthened the work and addressed most of my concerns. I suppose this work now can provide knowledge advancement to the community, and I look forward to the final version manuscript, which incorporates the additional insights and information presented in the rebuttal stage.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper addresses the generalization limitation of approximate second-order optimization methods. An approach called 'SASSHA' is proposed to enhance generalization by explicitly reducing sharpness. Empirical experiments are conducted to validate the effectiveness and robustness of SASSHA. It is demonstrated that SASSHA achieves good performance and strong generalization in noisy data settings and outperforms other methods.

### Strengths
1. Detailed explanation of techniques used in ‘SASSHA’ is given.

2. A series of experiments are conducted to verify the improvement of ‘SASSHA’.

### Weaknesses
1. See the question part.

2. Some incomplete references in line 113.

### Questions
1. In Section 5, empirical experiments compare the performance of SASSHA with some baselines. How does the empirical performance of ‘SASSHA’ compare with those approximate second-order algorithms similar to SASSHA, particularly those mentioned in Section 4.1& 4.2?  Only one comparison is presented in Section 5.4.

### Soundness
2

### Presentation
3

### Contribution
2
