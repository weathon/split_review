# Progressive Parameter Efficient Transfer Learning for Semantic Segmentation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Parameter Efficient Transfer Learning (PETL) excels in downstream classification fine-tuning with minimal computational overhead, demonstrating its potential within the pre-train and fine-tune paradigm. However, recent PETL methods consistently struggle when fine-tuning for semantic segmentation tasks, limiting their broader applicability. In this paper, we identify that fine-tuning for semantic segmentation requires larger parameter adjustments due to shifts in semantic perception granularity. Current PETL approaches are unable to effectively accommodate these shifts, leading to significant performance degradation. To address this, we introduce ProPETL, a novel approach that incorporates an additional midstream adaptation to progressively align pre-trained models for segmentation tasks. Through this process, ProPETL achieves state-of-the-art performance on most segmentation benchmarks and, for the first time, surpasses full fine-tuning on the challenging COCO-Stuff10k dataset. Furthermore, ProPETL demonstrates strong generalization across various pre-trained models and scenarios, highlighting its effectiveness and versatility for broader adoption in segmentation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper finds that there is a perceptual granularity gap between pre-trained models and downstream segmentation tasks, necessitating significant parameter adjustments. However, existing PETL approaches fail to effectively address this gap due to the constraint of limited trainable parameters. To tackle this issue, the paper introduces ProPETL, which incorporates an additional midstream adaptation phase to progressively align pre-trained models with downstream segmentation tasks. Specifically, the paper conducts an in-depth analysis of candidate progressive adaptation strategies, such as Generalized Parametric Adaptation and Decoupled Structured Adaptation, as well as intermediate tasks designed to enhance the perception of finer granularity and diverse classes. Notably, ProPETL achieves state-of-the-art performance on most segmentation benchmarks, surpassing even full fine-tuning.

### Strengths
1. The paper addresses the gap between pre-trained models and downstream segmentation tasks by introducing an additional midstream adaptation process, while maintaining parameter efficiency.
2. The method demonstrates its superiority by outperforming other parameter-efficient approaches and even surpassing full fine-tuning.

### Weaknesses
1. The paper is motivated by the observation that the perceptual granularity gap between pre-trained models and downstream segmentation tasks necessitates significant parameter adjustments. However, for models like SAM[1], which are pre-trained on segmentation tasks, there is a lack of evidence to support that these observations still hold. Specifically, the paper does not provide any analysis on whether the proposed midstream adaptation is still beneficial when the pre-trained model already has strong segmentation capabilities. The assumption that a granularity gap exists for all pre-trained models, regardless of their pre-training task, needs further justification.

2. The necessity of additional midstream adaptation is not entirely clear, as the proposed intermediate tasks resemble data augmentation, which could potentially be integrated into the fine-tuning phase. The paper does not sufficiently explore the potential of achieving similar performance gains by simply incorporating more diverse data augmentations during the standard fine-tuning process. The distinction between the midstream adaptation and data augmentation is not rigorously established, and the paper lacks a comparative analysis to demonstrate the unique benefits of the proposed approach over more conventional data augmentation techniques.

### Questions
Could the intermediate tasks be considered a form of data augmentation? Would performance improve if these intermediate tasks were integrated into the fine-tuning phase? For example, scaling the images to different sizes and generating varying numbers of categories at random ratios during fine-tuning.

### Soundness
3

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
3

### Summary
The paper presents ProPETL, a new method to improve Parameter Efficient Transfer Learning (PETL) for semantic segmentation tasks, which usually have more difficulties in fine-tuning compared to classification tasks. Current PETL methods find it hard because they need to adjust more parameters to handle changes in the details of semantic understanding. ProPETL solves this problem by adding a midstream adaptation step, which gradually aligns the pre-trained models for segmentation tasks. This proposed method achieves the state-of-the-art performance, even better than full fine-tuning, on various evaluation benchmarks.

### Strengths
1. The authors provide a detailed analysis of why existing PETL methods do not perform effectively for semantic segmentation tasks. This paper not only introduces ProPETL but also thoroughly tests its effectiveness compared to state-of-the-art methods across multiple benchmark datasets. The authors conduct extensive ablation studies to show the effect of each component of the method, which supports the strength of the proposed contributions.

2. The paper is well-written and organized clearly, making the paper easy to understand. The authors include background information and visualize to illustrate the weaknesses of current PETL methods and the strength of ProPETL. 

3. ProPETL outperforms full fine-tuning on various benchmarks, showing that parameter-efficient methods can match or even exceed traditional methods.

### Weaknesses
1. The proposed midstream adaptation phase makes the whole framework more complex than previous methods. Selecting intermediate tasks, such as perception granularity and supervision diversity, looks like it’s based on trial and error without a clear, systematic way for users to apply these choices to new datasets or tasks. The paper lacks a rigorous methodology for determining the optimal configuration of these intermediate tasks, making it difficult to generalize the approach. Specifically, the choice of using a combination of patch-level and larger-granularity perception, and the specific values used for supervision diversity (e.g., alpha=1), seem arbitrary without a clear theoretical justification or empirical analysis of a wider range of values. This lack of a systematic approach raises concerns about the practical applicability of the method to unseen datasets where the optimal configuration may be different.

2. While the progressive adaptation process improves segmentation performance, it may need more computational time because of the extra midstream phase, especially for large datasets. The paper claims that this extra cost is worth it for better performance, but having more exact comparisons of training time or resource usage with other PETL methods would help show the practical trade-offs, especially when computational efficiency is very important. The paper does not provide a detailed breakdown of the computational overhead introduced by the midstream adaptation phase, such as the time spent on each stage of training, or the memory usage during the intermediate task training. This makes it difficult to assess the practical cost of the proposed method compared to other parameter-efficient techniques, especially in resource-constrained environments.

### Questions
1. The paper shows that ProPETL works well with a Swin-L model pre-trained on ImageNet-21K, but how would the performance change if we use smaller or less powerful pre-trained models? Is there any guideline or expectation for using ProPETL in situations with limited resources? Would ProPETL still be helpful in transfer learning cases that use self-supervised models with lower representational capacity? It would be good to see more discussion or results about how much ProPETL depends on the quality of pre-trained models.

2. The paper says that the midstream adaptation improves segmentation performance, but how does the computational cost compare with traditional PETL methods, in terms of training time?

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
3

### Summary
This paper presents ProPETL framework, which applies progressive adaptation to Parameter-Efficient Transfer Learning (PETL) and introduces a novel midstream adaptation stage to address perception granularity differences and supervision diversity in semantic segmentation tasks.

### Strengths
This paper analyzes two candidate progressive adaptation strategies: Generalized Parametric Adaptation (GPA) and Decoupled Structured Adaptation (DSA), and employs DSA to effectively mitigate the "forgetting" issue observed in GPA. 

Extensive comparisons demonstrate that ProPETL delivers superior performance across benchmarks, underscoring its effectiveness and superiority.

### Weaknesses
1. Both Generalized Parametric Adaptation (GPA) and Decoupled Structured Adaptation (DSA) implement dimensionality reduction and expansion through bypass branches to reduce the number of parameters. However, the fixed reduction ratio $r$ may lead to the loss of critical feature information, especially in tasks with high perceptual demands (such as semantic segmentation). The fixed ratio of the reduction operation lacks adaptability to the importance of features and the complexity of input data, which may result in the bypass branch being unable to effectively retain fine-grained information, thus affecting the overall performance of the model. For instance, in scenarios where certain feature channels are highly discriminative for specific classes, a uniform reduction across all channels could inadvertently discard crucial information, leading to suboptimal segmentation boundaries and reduced accuracy, particularly for smaller or less prominent objects.

2. This paper suggests that Perception Granularity and Supervision Diversity are key factors in the design of intermediate tasks, but it lacks theoretical support for these design choices. For example, it does not explain why image-level perception granularity and multi-label supervision can enhance the fine-grained performance of downstream tasks. The paper does not provide a clear mathematical or conceptual framework that justifies why these specific choices of intermediate tasks are optimal or even beneficial. Without this theoretical grounding, the selection of intermediate tasks appears somewhat arbitrary, and it is unclear whether other combinations of granularity and supervision might yield better results or if the chosen combination is truly the most effective.

### Questions
1. DSA divides the adapter parameters into two independent parts: the parameters for the midstream adaptation stage( $\phi$) and the parameters for the downstream fine-tuning stage \($ \psi$ \). During the intermediate adaptation phase, DSA only optimizes $\phi$, while in the downstream fine-tuning phase, $\phi$ remains frozen, and only $ \psi$ is optimized. However, the strategy of freezing  $\phi$ during the downstream task, which reduces the parameter space that can be optimized and increases the burden on optimizing  $ \psi$  , leading the model to seek the best solution in a smaller space. For complex downstream tasks, this limitation may affect the model's  performance, as the optimization of  $ \psi$ cannot fully replace the tuning of  $\phi$.

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
4

### Summary
This paper proposes a framework for progressively adapting pre-trained models to downstream semantic segmentation tasks through intermediate tasks, where perception granularity and supervision diversity are interesting and novel. Although this work has some weaknesses in descriptions and experiments, its overall contribution benefits the PETL community, especially in fine-tuning VFMs from classification tasks to semantic segmentation tasks. Thus, I recommend the weak acceptance of this paper and hope the authors' responses.

### Strengths
1. The motivations of the proposed approach are clear.
2. The intermediate task designation, including perception granularity and supervision diversity, is interesting and novel.
3. The proposed approach achieves better performance on multiple benchmarks.

### Weaknesses
1. The evaluations of the generalization ability are insufficient. ProPETL demonstrates strong generalization across various pre-trained models and scenarios. However, the experimental evaluation does not show the proposed ProPETL's generalization ability under cross-scenario tasks, such as the domain generalization setting. I am interested in the proposed ProPETL's generalization ability under cross-scenario tasks.
2. The descriptions of the proposed approach are unclear. For example, the summary of the overall training and inference process and the design of the GPA's architecture in intuition or theory.
3. Do α of supervision diversity and pooling window of perception granularity correspond one to one?
4. The computational cost of the proposed approach during the training and inference stages should be introduced and compared with other fine-tuning strategies in detail, such as the total training time, inference time, FLOPs, GPU Memory, Storage, etc.
5. More backbones, such as DINOv2 and EVA02, and more segmentation heads, such as Mask2Former and SemFPN, should be included to verify the effectiveness of the proposed approach.
6. How to evaluate and compare to the Rein [1] which also introduces the PETL method for semantic segmentation tasks.
[1] Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation. CVPR 2024.
7. The fail examples, limitations, and future works should be provided and discussed.
8. Figure 1 (a) and (b) should be more elegant. Labels of the x-axis are too narrow.
9. The code should be released.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
