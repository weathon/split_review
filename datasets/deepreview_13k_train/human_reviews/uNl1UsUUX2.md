# Improving Generalization for Small Datasets with Data-Aware Dynamic Reinitialization

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
The efficacy of deep learning techniques is contingent upon copious volumes of data (labeled or unlabeled). Nevertheless, access to such data is frequently restricted in practical domains such as medical applications. This presents a formidable obstacle: How can we effectively train a deep neural network on a relatively small dataset while improving generalization? Recent works explored evolutionary or iterative training paradigms, which reinitialize a subset of the parameters to improve generalization performance for small datasets. While effective, these methods randomly select the subset of parameters and maintain a fixed mask throughout iterative training, which can be suboptimal. Motivated by the process of neurogenesis in the brain, we propose a novel iterative training framework, Selective Knowledge Evolution (SKE), that employs a data-aware dynamic masking scheme to eliminate redundant connections by estimating their significance, thereby increasing the model's capacity for further learning via random weight reinitialization. The experimental results demonstrate that our approach outperforms existing methods in accuracy and robustness, highlighting its potential for real-world applications where collecting data is challenging.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies training deep neural networks on datasets with a small number of training examples. This paper proposes a new training algorithm that selects subsets of parameters to reinitialize during the training process. For the selection of the parameters, this paper designs a method to generate parameter masks by measuring the influence of masking out one parameter on the loss function and then choosing the top-k parameters with the highest influence values. Experiments are conducted on image classification datasets, including Flower, CUB-200-2011, Stanford Dogs, and FGVC-Aircraft, with ResNet models. The proposed algorithm shows 4% average improvement over previous iterative training and reinitialization algorithms. The baselines include Dense-Sparse-Dense Networks, Born Again Networks, and Knowledge Evolution.  Furthermore, the proposed algorithms are applied to one dataset with corrupted images, CIFAR-10-C, showing consistent improvement over previous approaches. Ablation studies of masking percentages and importance metrics are conducted to confirm the benefits of the algorithm.

### Strengths
- Based on the previous knowledge evolution algorithm, this paper proposes to dynamically update the parameter masks through estimating the parameter importance on the downstream datasets. 
- This paper provides empirical studies that show the advantage of the proposed algorithm over previous iterative retraining and reinitialization algorithms.

### Weaknesses
 - Further discussion of the proposed algorithm is needed. For example, how are scores within the SNIP method computed? What is the computation complexity of estimating such scores during the training process? Would it lead to additional overhead?
- More recent baselines need to be compared. This paper conducts a comparison with previous retraining and reinitialization algorithms. However, for training on small datasets, many regularization and training algorithms are proposed, such as sharpness-aware minimization and distance-based regularization. How would the proposed method compare to such methods? Moreover, how does the method perform on transformer-based architectures?
- Further experiments can be conducted to analyze the algorithm. For example, how can one set the number of generations and the masking ratios in the algorithm? How would these parameters affect the model performance? With such a retraining algorithm, would the model converge faster than vanilla fine-tuning?

### Questions
See the weaknesses section for the questions.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a new method to improve training of neural networks. The method involves reinitializing a subset of the weights, selected based on saliency, a number of times during training. The authors compare their method to similar knowledge evolution experiments through evaluation on performance, corruptions, adversarial attacks and imbalanced datasets.

### Strengths
- The method presented is an interesting research direction that ties together many recent research directions, e.g. pruning, reinitialization and evolution. This gives it a reasonable motivation.
- The paper itself is well-structured and mostly well written (but see exceptions listed below)
- Experiments suggest the method is promising although more investigation are needed. They will be of interest to the research community.

### Weaknesses
 - The main issue with the paper is its presentation of the results on imbalanced data. The authors use accuracy as a metric, which can be highly misleading on imbalanced data. I cannot infer anything from figure 4 on the robustness to imbalanced data. There are many ways to show performance on imbalanced data, including confusion matrices or per-class accuracy. I suggest the authors either improve this presentation or remove entirely the class imbalance experiments (or correct the figure and text description if they do not mean overall accuracy). In its current form the results are not supporting the conclusions. 
- The adversarial perturbation experiments are also lacking in presentation. Is the figure a single run or multiple runs? What are the errors?
- Sensitivity analysis would have been a nice addition, the authors leave this for future work. However, the paper would have been notably stronger with these included and should be relatively inexpensive to run.

### Questions
Questions:
- In the abstract and introduction, the authors state that the KE approach is limited due to its predetermined mask. I can see that this as a valid hypothesis, but the authors state this as if it is well-established. Are there any references to support this? With the posterior knowledge of the results of SKE this statement is supported, but the hypothesis which sparked the investigation cannot be based on the results. 
- How is the size of subset used to evaluate connection sensitivity selected? Is there any estimate for what is sufficient?
- Sensitivity analysis is not part of this paper but how do the authors interpret the sparsity constraint k? Is there anything in the literature or insight they have as to how sensitive the model is to it? 

Other comments:
- There are instances where the word "significant" is used to describe the difference between two methods. I highly recommend that the authors save this term to describe statistical significance (it seems a significance test was not performed). There are better words to describe a great difference that are not as ambiguous. 
- It should be made much clearer that section 3.1 is standard KE and not the version being presented in the paper. On first reading it seems like it is the method being introduced and the fixed mask creates confusion. 
- When the binary mask is defined in 3.1, make it clear it is binary when it is first mentioned, not in a later paragraph.
- Grammatical error: "We define a deep neural network f with L layers and is characterized by"
- The acronym DNN is defined multiple times. The authors should define it once at the start and then only use it and not spell it out or redefine it multiple times.
- Figure 4 is never referenced in the main text

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper builds upon previous studies that examined the effects of reinitialization on the generalization capabilities of neural networks. The authors focus specifically on ResNets and small datasets (e.g. of size < 100K examples). Earlier research highlighted that by selectively reinitializing certain network parameters and then retraining the whole network, one could enhance generalization. The current paper presents a new approach for choosing which parameters to reset that is data-dependent, and show that it outperforms several baseline methods. Additionally, the authors provide additional useful analysis, such as the consistency in parameter selection across iterations, comparisons with other importance estimation techniques, and robustness-related evaluations.

### Strengths
- The authors explore an interesting direction: to reinitialize the network during training to improve its generalization capability. This has been studied in several recent works, and an additional investigation can be useful to the community.
- The paper shows notable improvements in performance compared to *some* baselines (namely, KE, DSD, long training). As mentioned in the paper, this approach has the potential of improving generalization in data-scarce domains, such as in healthcare.

### Weaknesses
 - It is not clear how statistically reliable the main conclusions of the paper are. This is because the number of datasets used is small (e.g. the authors evaluate ResNet18 on only four small datasets). Since the datasets are small and there are tens of vision-related datasets available, I'm curious to know why the authors used only four datasets. I don't think including more datasets should be an issue since (again) they are small and ResNet18 is also small. The same applies to the other sections. For example, the authors evaluate robustness to adversarial attacks in one dataset only!

- The authors only compare with old reinitialization baselines (KE, DSD, and BAN). There have been more recent layerwise methods, but the authors only compare against those in the appendix (see Table 5). There, the improvement is marginal. Is there a reason the authors chose to not include those other methods in the main paper? Also, why aren't they included in the ResNet50 evaluation? They are also not discussed in the Related Works section, and there are a few recent related works missing as well; e.g. (Sheheryar, et al. 2023) and (Jaehoon, et al. 2022). They should all be discussed in the related works section.

- The reported results for CIFAR10-C seem too low to me. I would expect ResNet18 trained on CIFAR10 to have an accuracy larger than 60% when evaluated on CIFAR10-C. 

- The authors argue in the appendix that transfer learning is not useful for medical applications. But that's not true. Many SotA models are pretrained on datasets, like ImageNet. See for example: https://www.nature.com/articles/s41591-020-0842-3.

- There are a few places containing typos, incomplete sentences, or undefined symbols:
   * Page 2: "Finally, Our work ... " --> "Finally, our work ..."
   * Equation 4: $\pi$ is undefined. 
   * Page 4: "Due to the difficulty in deciding ..." is not a complete sentence.
   * Page 4: "retained learned" should be either "retained" or "learned".

### Questions
- When the authors compare against long-baseline (LB), do they also remove 20% of the examples in LB? I'm asking this because LB does not need to have 20% of the examples removed, unlike SKE which uses those for importance estimation. 
- Please explain precisely how the Mean Corruption Accuracy metric is calculated?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studied how to train a neural network on small datasets while improving generalization. Motivated by neurogenesis in the brain, this paper proposed a novel iterative training framework, Selective Knowledge Evolution (SKE), that employs a stage-wise mask to reinitialize the masked weights per training stage. The stage-wise mask is obtained by estimating the data-dependent sensitivity via SNIP. The proposed SKE shows impressive empirical improvements in various experiments.

### Strengths
-	This work made two simple but effective modifications to the original Knowledge Evolution (KE) method. Both the neuroscience-inspired dynamic mask and the selective mask via SNIP are interesting.
-	I appreciate the part which introduces the inspiration from neurogenesis in the brain. 
-	The empirical improvements seem significant and general in various experiments.
-	The experiments are comprehensive and beyond simple accuracy comparison on small datasets.

### Weaknesses
 - The work did not study the computational cost comparable with KE. Moreover, I believe the empirical improvement will more convinceable if the authors may also compare the generalization under similar computational costs. Because it is known that DNNs sometimes improve generalization with longer training. Specifically, the paper does not provide a detailed breakdown of the computational overhead introduced by the dynamic masking and SNIP calculations. While the authors mention that SNIP is used to estimate data-dependent sensitivity, the frequency and intensity of these computations throughout the training process are not clearly quantified. A table comparing the wall-clock time and FLOPs for SKE, KE, and the long baseline would be beneficial.

- There is theoretical analysis at all. Theoretical understanding under some assumptions will be appreciated. For instance, while the neurogenesis inspiration is intriguing, the paper lacks a formal theoretical connection between the proposed method and the biological process. A more rigorous analysis of how the dynamic masking affects the optimization landscape and convergence properties would strengthen the paper. Furthermore, exploring the conditions under which SKE is expected to outperform standard training or KE, perhaps in terms of dataset size, model complexity, or noise levels, would provide valuable insights.

### Questions
Please see the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
