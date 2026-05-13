# Data Distillation Can Be Like Vodka: Distilling More Times For Better Quality

- Decision: Accept
- Scores: 6, 5, 8

## Abstract
Dataset distillation aims to minimize the time and memory needed for training deep networks on large datasets, by creating a small set of synthetic images 
that has a similar generalization performance to that of the full dataset. However, current dataset distillation techniques fall short, showing a notable performance gap when compared to training on the original data. 
In this work, we are the first to argue that using just one synthetic subset for distillation will not yield optimal generalization performance. This is because the training dynamics of deep networks drastically change during the training. Hence, multiple synthetic subsets are required to capture the training dynamics at different phases of training. To address this issue, we propose Progressive Dataset Distillation (\alg). \alg synthesizes multiple small sets of synthetic images, each conditioned on the previous sets, and trains the model on the cumulative union of these subsets without requiring additional training time.
Our extensive experiments show that \alg can effectively improve the performance of existing dataset distillation methods by up to $4.3\%$. In addition, our method for the first time enable generating considerably larger synthetic datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a dataset distillation algorithm that generates synthetic data in a progressive manner: the next batch of synthetic data would be dependent on previous batches. The training using the distilled datasets also contains several stages. The training data for each stage come from the corresponding batch of the distilled dataset and its previous batches in a cumulative way. Experiments demonstrate that the proposed strategy improves the baseline method.

### Strengths
The idea of progressive dataset distillation is interesting. This can 1) capture the training dynamic of neural networks better as demonstrated by authors, 2) reduce the complexity of training the whole synthetic dataset together, and 3) serve as a strong method for slimmable dataset condensation [a].

[a] Slimmable Dataset Condensation, CVPR 2023.

### Weaknesses
1. Many places are unclear.
    * Fig. 1 needs some explanations. How do the results come in detail, like what's the IPC of each stage, and how to conduct multi-stage training? Although some of these questions are answered in the following parts, the writing is not coherent. Specifically, the figure does not clearly indicate the IPC used at each stage, nor does it show the cumulative effect of the progressive distillation. It's unclear how the accuracy is measured across different stages with varying amounts of synthetic data. The figure should explicitly show the performance at each stage, and how the IPC accumulates over the stages.
    * The networks for the next stage come from the training results with previous batches of synthetic data. In IDC, the networks are periodically re-initialized randomly. In MTT, the networks come from checkpoints of training with original datasets. We have to conduct some modifications to these baselines before using PDD. These operations are unclear. It is not clear how the re-initialization in IDC is handled in the progressive setting. Specifically, how the weights are transferred or if they are completely re-initialized at each stage. For MTT, it's unclear how the checkpoints from the original dataset are used to initialize the network at each stage of PDD. The paper needs to provide a more precise description of these modifications.
2. A comment: this method makes an assumption on downstream training using synthetic datasets: models must be trained in a multi-stage way using the provided multi-stage synthetic data, which would introduce a lot of hyperparameters, especially in the cross-architecture setting and make the dataset distillation less elegant. Given that the performance gain is not significant in most cases, the practical value of the proposed method is somewhat limited. The requirement for multi-stage training introduces a dependency on the specific training regime used for distillation. This limits the flexibility of the distilled dataset, as it cannot be used directly with other training strategies. The paper should discuss the implications of this dependency and how it affects the generalizability of the distilled datasets. Furthermore, the performance gains, while present, are not substantial enough to justify the added complexity of multi-stage training, particularly when considering the potential for increased hyperparameter tuning.
3. Through the results in Tab. 6, the effect of discarding easy-to-learn examples at later stages is not significant. More evidence is necessary to demonstrate the effectiveness. The paper claims that discarding easy-to-learn examples improves efficiency, but the results in Table 6 do not strongly support this claim. The performance differences between using all examples and discarding easy examples are marginal, especially in later stages. The paper needs to provide more compelling evidence or a more detailed analysis to justify this design choice.

### Questions
Please refer to the Weaknesses part. I would also like the authors to discuss more benefits of PDD as mentioned in the 1st point of Strengths in the camera-ready version or in the next revision cycle.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a dataset distillation method. The core idea is to freeze the previously distilled subset and then only optimize the new subset. This method can be applied to several dataset distillation methods and show marginal improvement over the original method.

### Strengths
1. The overall writing is clear.
2. The comparison with a few previous is clear to validate the effectiveness of the method.
3. The explanation looks sufficient.

### Weaknesses
1. Some important reference is missing such as DEARM [a]. Since this is the SOTA method in dataset distillation, the authors should cite and compare the paper.
2. After Eq.4, the authors claim PDD can be used to **any** dataset distillation method. Therefore, it is necessary to do experiment if the PDD can augment DREAM.
3. The accuracy is not as good as DREAM. For example, on CIFAR-10 IPC-10, DREAM can achieve 69.4% accuracy. But the proposed PDD can just achieve 67.9%. On CIFAR-100 IPC-10, DREAM can achieve 46.8% accuracy. But the proposed PDD can just achieve 45.8%.
4. Based on question 3, why does the proposed method have bad performance on IPC-10?
5. The idea is too straightforward. Is it possible to update the previous frozen subset with small learning rate?

### Questions
see weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The significant contribution of this work lies in the introduction of Progressive Dataset Distillation (PDD). It is a novel methodology in the field of dataset distillation. PDD effectively addresses the limitations inherent in existing DD works by recognizing that relying solely on a single synthetic subset for distillation does not lead to optimal generalization. 

Specifically, PDD innovatively synthesizes multiple small sets of synthetic images, with each set being conditioned on the knowledge acquired from the preceding sets. The alteranated updated model is then trained on the cumulative union of these subsets. This sophisticated approach results in a noteworthy performance improvement.

### Strengths
1. The idea presented in this work is both intriguing and groundbreaking. As far as my knowledge extends, this is the first instance where the synthesis of multiple small sets of distilled images has been proposed. The authors have adeptly addressed the challenge of minimizing bias and ensuring training stability by introducing a conditioning mechanism for each distilled set, based on the knowledge accumulated from the preceding sets.

2. The clarity and coherence of the writing are commendable. The motivation behind the research is robust, and the overall structure of the paper is meticulously organized.

3. The experimental results provided in the paper are highly promising and effectively illustrate the efficacy of the proposed solution.

### Weaknesses
N.A.

### Questions
Is it possible to provide additional experimental results about "DM+PDD"?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
