# Narrowing the Focus: Learned Optimizers for Pretrained Models

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
In modern deep learning, the models are learned by applying gradient updates using an optimizer, which transforms the updates based on various statistics. Optimizers are often hand-designed and tuning their hyperparameters is a big part of the training process. Learned optimizers have shown some initial promise, but are generally unsuccessful as a general optimization mechanism applicable to every problem. In this work we explore a different direction: instead of learning general optimizers, we instead specialize them to a specific training environment. We propose a novel optimizer technique that learns a layer-specific linear combination of update directions provided by a set of base optimizers, effectively adapting its strategy to the specific model and dataset. When evaluated on image classification tasks, this specialized optimizer significantly outperforms both traditional off-the-shelf methods such as Adam, as well as existing general learned optimizers. Moreover, it demonstrates robust generalization with respect to model initialization, evaluating on unseen datasets, and training durations beyond its meta-training horizon.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces L3RS, a learned learning rate scheduler that ensembles updates from base optimizers like Adam and SGD. 

L3RS is parameterized as a shared MLP and layer-wise trainable embeddings. For each layer, L3RS takes its embedding and training status statistics (training time, exponential moving average of loss/gradient norm/weight norm) as input, and predicts coefficients of base optimizer updates. L3RS is trained with natural evolution strategies. In various settings with ImageNet and PLACES dataset, L3RS shows higher classification accuracy and training efficiency on ResNet34 finetuning.

### Strengths
1. The presentation is clear and easy to understand; The experiments are comprehensive and well-explained.
2. The proposed method is novel and useful: it eliminates the need for learning rate schedule tuning.
3. The proposed method demonstrates faster convergence and improved performance.

### Weaknesses
1. L3RS is not generalized and needs to be trained independently for each model architecture, which limits its application. From ImageNet <-> PLACES experiments it seems a trained L3RS can generalize to other data distributions, and it would be more beneficial to include more benchmarks to showcase that.
2. Experiments are only conducted on ResNet34, while including evaluation on other architectures and more diverse benchmarks (e.g. [VeLO](https://arxiv.org/abs/2211.09760)) would make the results more convincing. 
3. Finetuning for only 1000 steps may not well represent the practical finetuning setting.
4. Lack of a deeper analysis on how SGD/Adam update directions are favored by different layers/learning stages.
5. For practical use of L3RS, there needs to be a L3RS training recipe generalized across different model architectures, or pretrained L3RS checkpoints tuned for popular architectures.

### Questions
See weaknesses

### Soundness
3

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
This paper explores learned optimizers to refine pretrained models. The proposed method, L3RS, dynamically adjusts the weighting scaler for gradient directions derived from different optimizers like SGD and Adam in a layer-specific manner and tunes hyperparameters such as the learning rate during the meta-learning process. The results demonstrate that L3RS surpasses both traditional and other learned optimizers in terms of performance during the initial fine-tuning steps.

### Strengths
1) The paper studies the important challenge of automating hyperparameter tuning for optimizers, which is a critical aspect of training neural networks efficiently.  
2) By integrating the update directions from multiple optimizers and learning the optimal combination, the proposed method introduces a promising and potentially more adaptable approach to optimizer design.  
3) L3RS shows enhanced performance in the early stages of fine-tuning compared to baseline methods.

### Weaknesses
1) My main concern is the applicability of this approach. According to Figure 3, the proposed learned optimizer only outperforms Adam in the early stages with smaller training steps. For larger training steps, Adam achieves comparable performance to the learned optimizer. Given that the learned optimizer requires extra time and memory to learn additional parameters, using it may not be necessary. Furthermore, the total convergence time, including the meta-learning process, may be slower than Adam.  
2) The evaluation is limited to training a ResNet-34 model on image classification tasks. Expanding the experiments to include diverse tasks such as language understanding or generation and different architectures like transformers would provide a more comprehensive evaluation.  
3) The study does not consider several recent and more effective variants of adaptive learning rate methods, such as Adabelief [1]. Including these in the comparative analysis or integrating their strategies could enhance the performance of learned optimizers and better justify their adoption.

### Questions
1)	Given that the final performance of L3RS is comparable to Adam and considering the extra computational costs, what are the specific scenarios or benefits that justify the use of learned optimizers?  
2)	Experiments on additional tasks and models are necessary.  
3)	A more in-depth discussion of advanced adaptive learning methods, such as Adabelief, is helpful.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a learning to learn method where learned optimizers are used to finetune pretrained models. The work focuses mainly on downstream tasks with the goal of focusing the meta learning process on narrower tasks. Experiments revolve around showing that the learned optimizer can use off-the-shelf optimizers to surpass both off-the-shelf and SotA learned optimizers.

### Strengths
The experiments on task distribution are comprehensive.
The section on preliminaries is comprehensive.
The ablation studies show the effectiveness of each design choice.

### Weaknesses
 - The abstract is poorly written with wording that replaces necessary definitions. What is meant by “transforms the updates” (missing context), “various statistics” (can be replaced with an actual example) or “hand-designed” (didn’t understand what this could be in relation to)? In general, in terms of writing, the paper seems rushed and incomplete with inconsistencies in writing quality.

- L154: There is a mention of "a lot of parameters". A casual writing style isn't appropriate. Either the number of parameters should be mentioned or a relative figure should be given justifying the issues that the authors take with VELO. Especially since this paper quantitatively addresses this issue in Table 1 and a simple referral to that section would be enough.

- L153: "2-hidden layer, 4-hidden MLP" this part doesn't make sense. 4-hidden MLP?

- L155: The usage of the word "lean" is vague and uncommon as far as I'm aware. Did you mean flexible?

- L189: “is probably the closest”. Again, casual writing style is not appropriate.

- The structuring of paragraphs is odd. As an example, in the preliminaries section, some paragraphs are only a single sentence.

- One of the problems mentioned in the intro is about the short horizon and how far we need to move from the pretrained model to train it. But then in the next few paragraphs, the authors mention that they want to focus on finetuning pretrained models. Wouldn’t that make the problem of short horizons moot not only for this work but also for the previous works that supposedly had problems with long horizons?

- I didn’t find a comparison to ATMO Landro et al. (2021) in the paper especially since it is mentioned in the paper that ATMO is the closest to this work. Is the ablation at L476 a representation of ATMO?

- The experiments seem to focus on one structure and one variant of that structure. More structures are needed to show that the approach isn't limited to resnet only especially since more complicated mechanisms like attention don't exist in ResNet-34 making them unsuitable for a considerable number of current day problems.

- Section 5, meta-evaluation and baselines: why are those baselines chosen? there is no description of the reasoning as to what the point of comparison to those baselines is. This is referring to the case of cosine, cosine head, const and const head. If the point is to vary the learning rate scheduler, there are many other schedulers. What makes cosine scheduling so special to act as a baseline? Is it the popularity of cosine schedulers? To note, I'm asking for a description for the reasoning of choosing those baselines. The VELO models have descriptions giving reasoning as to why they were chosen for comparison but the other baselines don't.

- Since the work is focused on narrow datasets and finetuning scenarios, I’d expected to see more datasets with varying granularity to showcase the effectiveness of this method.

Nitpicks:
Tables should be changed to booktabs format for readability if the venue rules allow.
Figure 3 caption is hard to read.
L200, comma missing at the start of paragraph.

### Questions
Please refer to the weaknesses section.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Typical model training requires an optimizer such as SGD, or ADAM and tune the hyper parameters such as learning rate. One alternative direction is to have meta-learning, where a general-purpose optimizer is trained from multiple tasks and then apply to the specific problem. This meta-learning approach such as VELO is computational expensive. This paper tries a different direction which is to learn a specialized learned optimizer namely L3RS to focus on improving the pre-trained model fine-tuning. Different from the VELO approach, the proposed L3RS uses smaller MLP networks for per-layer operations and relies on base optimizers. This design choice leads to two to three orders magnitude fewer parameters compared to the VELO. The proposed L3RS shows 50% speed up over VELO and 100% speedup over the best hand-designed optimizer on ImageNet benchmark.

### Strengths
1. L3RS is a unique learning-to-learn optimizer approach that focuses on the fine-tuning cases. This is different from the standard fine-tuning optimizer such as SGD or ADAM, and it is also very different from the general learning-to-learn optimizer such as VELO.
2. The proposed approach is evaluated on various experimental settings such as ImageNet and PLACES datasets. The proposed experimental setting seems to be typical for learning-to-learn related papers.
3. L3RS shows a significantly speed up than the VELO and baseline in the benchmarks.

### Weaknesses
1. Experiments are not comprehensive and convincing. The actual baseline used in the experiments is VELO. However, the field has many other famous approaches, such as Shampoo optimizers. Can the proposed approach show better results than Shampoo as well? I am also not sure about the generalization of the proposed approach. Specifically, how would one know that the layers trained with the proposed approach are not stuck in the local optimal? Can you provide any theoretical or experimental analysis? It seems to be odd to focus only on achieving accuracy. It would be better to see if the model is converged.
2. Resources. The proposed approach is still considerably expensive, and it might not be that attractive to the practitioner if it only helps to optimize the optimizer to adapt to the specific dataset with specific model fine-tuning. It would be great to justify the resources.

### Questions
1. How is the proposed approach perform against the other alternative such as Shampoo optimizer?

2. How is the proposed approach determine if the learned optimizer is useful to help the model to be trained to converged rather than reaching certain accuracy?

3. Can you give more back envelop estimation on the computational cost versus the benefits of the proposed approach bringing in in the actual useful applications?

### Soundness
3

### Presentation
2

### Contribution
3
