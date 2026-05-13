# Exploiting Open-World Data for Adaptive Continual Learning

- Decision: Reject
- Scores: 5, 3, 6, 3

## Abstract
Continual learning (CL), which involves learning from sequential tasks without forgetting, is mainly explored in supervised learning settings where all data are labeled. However, high-quality labeled data may not be readily available at a large scale due to high labeling costs, making the application of existing CL methods in real-world scenarios challenging. In this paper, we study a more practical facet of CL: open-world continual learning, where the training data comes from the open-world dataset and is partially labeled and non-i.i.d. Building on the insight that task shifts in CL can be viewed as distribution transitions from known classes to novel classes, we propose OpenACL, a method that explicitly leverages novel classes in unlabeled data to enhance continual learning.  Specifically, OpenACL considers novel classes within open-world data as potential classes for upcoming tasks and mines the underlying pattern from them to empower the model's adaptability to upcoming tasks. Furthermore, learning from extensive unlabeled data also helps to tackle the issue of catastrophic forgetting. Extensive experiments validate the effectiveness of OpenACL and show the benefit of learning from open-world data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work addresses the problem of open semi-supervised continual learning (CL). The authors propose a new method, OpenACL, which can handle both labeled and unlabeled data in a stream of tasks in an online manner, using proxy-based representation learning. The proxies represent both seen and novel classes in the latent space. When switching to a new task, OpenACL introduces an additional proxy adaptation step, where proxies are assigned for labeled data and novel classes. Experiments are conducted on split CIFAR-10, CIFAR-100, and TinyImageNet datasets, using 20% and 50% labeled data.

### Strengths
1. This work address the practical limitation of label scarcity in online continual learning (OCL).
2. Paper is easy to follow for the reader.

### Weaknesses
1. In this work, the authors present the problem of semi-supervised continual learning as a practical one and as well interesting from the research perspective. But in a way, that many already done work in semi-supervised CL [1] and very close areas, i.e., generalized-category discovery (GCD), are not presented. Even related work section is done in a way that skips existing work like [1], and GCD - especially method that use very similar approach based on proxy learning, e.g., [2]. This lack of proper discussion of what is already there in CL is weakness. 

2. Selection of the method for the comparison - why not using [1] even in the online setting. Additionally, presenting the results of an existing online representation learning method, e.g., LUMP[4] with a simple kNN classifier for labeled data would be interesting.   

2. From the abstract, l.22-23 "learning from extensive unlabeled data also helps to tackle the issue of catastrophic forgetting" - this claim raise some expectation from the work and new SSL method in OCL. Then, the reader is given only with 20% and 50% of labeled data for the main experiments. No extensive analysis of how the OpenACL methods perform with different ratio of labeled data. After the intro, especially with small ratio (e.g., 0.5, 1, 5). See for example ratio in works: [3], [4]. In the appendix, only 10% is additionally provided. However, would be nice to see where is the limit of the OpenACL method.

3. The experiments conducted only on the small size datasets and single network architecture. The results for Stanford Cars (Tab. 12) are very low and hard to compare with other works. 

4. Notation can be improved, e.g., in eq.4 x_j <> x_i, just checking indexes is enough, additonaly in eq. 5 the notation is different A(i) is introduced. This could be more consistent between equations.

5. OpenACL has limitation of alignment of number of proxy to number of classes for the task. 

[1] Kang, Zhiqi, et al. "A Soft Nearest-Neighbor Framework for Continual Semi-Supervised Learning." Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2023, pp. 11868-11877.
[2] Kim, H., Suh, S., Kim, D., Jeong, D., Cho, H., Kim, J.: Proxy anchor-based unsupervised learning for continuous generalized category discovery. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 16688–16697 (2023)
[3] Fini, Enrico, et al. "Self-Supervised Models Are Continual Learners." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2022, pp. 9621-9630.
[4] Madaan, Divyam, et al. "Representational Continuity for Unsupervised Continual Learning." Proceedings of the 10th International Conference on Learning Representations (ICLR), 2022.

### Questions
1. What is the k in k-means initialization? 
1. What is the method sensitivity towards $\lambda$?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a task set up of semi supervised continual learning and a method proposing a learned proxy 'class prototype' (usually referred to as average of class embeddings of a certain class) for the samples without label memberships. The method modifies contrastive learning objective to learn the proxies in semi-supervised learning setup. The method includes a method to facilitate the adaptability of a model to balance between forgetting and adaptability. Empirical evaluations are on CIFAR-10/100 and Tiny-ImageNet. The proposed method outperforms prior arts.

### Strengths
* Claiming a contribution of proposing a new CL setup with semi-supervised learning.
* Simplicity of a method that outperforms prior arts.

### Weaknesses
* Technical novelty of the proposed method. The proposed method is a relatively straightforward application of the well-known contrastive objective to the semi-supervised learning.
  * Although the reviewer appreciate the novelty of notion of a learned proxy for the unseen data, the objective function formulation to learn such proxies is quite limited.
* Similar task setup has been proposed before. Check out: Boschini et al., **Contrinual Semi-Supervised Learning through Contrastive Interpolation Consistency**, *Pattern Recognition Letters, 2022* (https://arxiv.org/pdf/2108.06552)
* Empirical gain seems marginal (also considering the standard deviation) compared to prior arts. (Table 1)
  * Also proposed components seems not bringing much of gain (Table 7)
* Empirical validation is limited due to the size of the dataset. Although CIFAR-10/100 and Tiny-ImageNet are widely used datasets in CL literature, they are quite small sized. ImageNet-1K would be the minimum large scale dataset to validate the value of the proposed method.
* Lack of sensitivity study of the hyperparameter $\lambda$
* Presentation can be improved
  * Although the CL should address combined challenge of forgetting of old knowledge and adaptability to new knowledge, in the introduction, the paper only mentions about forgetting. At L201-202, the paper finally mention about the combined challenge. This argument should be in the introduction.
  * L323, overwriting $\to$ overriding

### Questions
Please refer to my comments in the weakness section.

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
Unlike existing continual learning approaches, this paper considers the problem of continual learning in an open world. In this setting, when learning each task, the model not only receives a labeled dataset for that task but also an unlabeled dataset. The proposed method employs proxies and contrastive learning techniques to overcome the issue of unlabeled partial classes, and experiments demonstrates the effectiveness of this approach.

### Strengths
1. This paper addresses the problem of continual learning in an open world environment, which is more realistic and challenging compared to previous continual learning settings.

2. The proposed method is innovative, employing contrastive learning and proxies to effectively utilize unlabeled datasets to assist in continual learning.

### Weaknesses
1. Using partial data from the same dataset as open world data is a rather strong assumption. Since data within the same dataset belongs to a single domain and can be transferred between each other [1], this does not fully capture the complexities of a true open world environment. In reality, unlabeled data could differ significantly from labeled data, potentially coming from entirely different datasets.

2. Does your method utilizes all unlabeled datasets to update the model when learning a new task? If so, this still deviates from the real-world setting. In the real environment, the amount of unlabeled data could be enormous, making it impractical for the model to process all of it when learning each task. Instead, the model would likely only be able to select a portion of the unlabeled data to learn alongside the labeled task data.

[1] Galanti T, György A, Hutter M. On the Role of Neural Collapse in Transfer Learning. International Conference on Learning Representations. 2021.

### Questions
1. Is the "open-world continual learning" problem you aim to solve one that you propose first, or has it been proposed by other works previously?

2. I notice that there are several works addressing the "Continual Category Discovery" problem [1, 2]. Since both "Continual Category Discovery" problem and the problem you address involve the combination of open-world scenarios and continual learning, what are the differences between these two problems? Which one is more challenging, and what are the respective practical scenarios they face?

[1].  Cendra F J, Zhao B, Han K. Promptccd: Learning gaussian mixture prompt pool for continual category discovery. European Conference on Computer Vision. Springer, Cham, 2024: 188-205.

[2]. Ma S, Zhu F, Zhong Z, et al. Happy: A Debiased Learning Framework for Continual Generalized Category Discovery[J]. arXiv preprint arXiv:2410.06535, 2024.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper explores open-world continual learning, addressing the challenge of learning from partially labeled and non-i.i.d data, unlike traditional CL which relies on fully labeled datasets. The authors propose OpenACL, a method that leverages novel classes within unlabeled data to improve adaptability and mitigate catastrophic forgetting, demonstrating its effectiveness through extensive experiments.

### Strengths
**[Realistic setup]** I totally agree with the author's claim that is hard to gather the a large amount of high-quality annotated dataset in real scenario. It means that the proposed method can be applicable to application services in real world. 

**[Various Scenarios]** They conducted various experiments on continuous learning: task incremental learning, class incremental learning. In other words, this method is not limited to a specific scenario and can be applied to various scenarios.

### Weaknesses
**[Correlation between CL and SSL]** Although I agree with that it is hard to gather the high-quality labeled dataset, I am suspicious that combination of SSL and CL can easily solve this setup. Specifically, as shown in Tab. 1, combination of SimCLR and CL methods almost reach to the SOTA results. In this context, I have a inquiry: *What is the obstacles when combining SSL with CL in open-world data?*. 

**[Table 2]** Overall, the results in Tab. 2 are very poor. To the best of my knowledge, some methods showed high performance in CIL setup, specifically transformer-based CL such as L2P [1] and DualPrompt [2] which are trendy methods in CL research stream. 

[1] Learning to prompt for continual learning, CVPR 2022

[2] Dualprompt: Complementary prompting for rehearsal-free continual learning, ECCV 2022 

**[Further Analysis]** To the best of my understanding, the proposed method matches the proxy to the classes in the current task. However, I'm wondering the value of similarity between labeled data for specific class and proxy cluster. Also, Does the proxy cluster consist of the examples of same class? I suggest the authors to analyze the representation space of the model.

### Questions
Below ones are the minor comments, and it is not directly related to the contents of this work. 

**[autoref]** There is missing autoref in the equations. L271, equation 2 should be autoref. Also, when referring appendix section, please add autoref. 

**[Equation Font]** In Eq.5 and 6, you should "\mathrm{sim}" instead of "sim".

### Soundness
2

### Presentation
2

### Contribution
2
