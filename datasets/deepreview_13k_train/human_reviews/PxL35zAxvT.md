# Test Time Adaptation with Auxiliary Tasks

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
This work work tackles a key challenge in Test Time Adaptation~(TTA): adapting on limited data. This challenge arises naturally from two scenarios. (i) Current TTA methods are limited by the bandwidth with which the stream reveals data, since conducting several adaptation steps on each revealed batch from the stream will lead to overfitting. (ii) In many realistic scenarios, the stream reveals insufficient data for the model to fully adapt to a given distribution shift. We tackle the first scenario problem with auxiliary tasks where we leverage unlabeled data from the training distribution. In particular, we propose distilling the predictions of an originally pretrained model on clean data during adaptation. We found that our proposed auxiliary task significantly accelerates the adaptation to distribution shifts. We report a performance improvement over the state of the art by 1.5% and 6% on average across all corruptions on ImageNet-C under episodic and continual evaluation, respectively. To combat the second scenario of limited data, we analyze the effectiveness of combining federated adaptation with our proposed auxiliary task across different models even when different clients observe different distribution shifts. We find that not only federated averaging enhances adaptation, but combining it with our auxiliary task provides a notable 6% performance improvement over previous TTA methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose to leverage source data to improve the performance of EATA, a state of the art test-time adaptation algorithm. They present results on ImageNet-C, and -3DCC for small sized models (Resnet18, 50, ViT). The proposed method outperforms the state of the art, EATA on most of these tasks.

### Strengths
- Clarity: Execution of experiments and write-up of the paper story is clear.

- Quality: Results are well evaluated, yet limited in the choice of models and datasets.

- Significance: Paper shows that combination of EATA and UDA setup improves over TTA methods, see concerns below.

General comment: The motivation for the paper is clear, and results are interesting and thorough (but see the weaknesses). Limited analyis on hyperparameter effects was done, but some is included. While the objective function is a combination of UDA and EATA, the adapting weighting of the source and target losses, Eq. 4, sounds like a novel contribution.

### Weaknesses
The authors essentially re-invented domain adaptation, and try to re-sell this as a SOTA TTA approach.

In the classical domain adaptation setting, entropy minimization or pseudo labeling methods are combined with a cross-entropy on the source dataset, see e.g. [French et al. (2017)](https://arxiv.org/abs/1706.05208). This is a very well-studied method, and established to work well.

In this regard, I find the paper story a bit problematic: The authors position themselves in the space of test-time adaptation, which is exactly the setting in which source data is *not available*. The fact that the state-of-the-art TTA model, EATA*, when evaluated in an unsupervised domain adaptation setting instead of a TTA setting becomes better might be obvious.

That being said, a well-made evaluation on applying domain adaptation techniques to TTA might be interesting to increase cross-talk between the two fields/evaluation settings, but this is completely dismissed by how this paper is written. There is not even a single instance (besides a few titles in the bibliography) mentioning the word "domain adaptation", or better, "unsupervised domain adaptation", in the whole paper.

I am not sure about the best way to rectify this, and would be happy to engage in a discussion with the authors. I would be especially keen to know:

Additional main weaknesses:

- I find it confusing that at first, entropy minimization on the source data is introduced, and then switched to cross-entropy. As I noted above, this is a very standard and established thing in the literature, and I would re-write this part of the methods section with that in mind.
- "auxiliary task": I would change the naming here, again, and note that this is unsupervised domain adaptation. The paper title is also very misleading, as it suggests that multiple "auxiliary task*ss*" are considered when it is in fact only one.
- Given my comments about unsupervised DA vs. TTA, an extensive review on SOTA UDA methods is lacking, and fair experimental evaluation towards these SOTA methods. If the authors are interested in rectifying this issue, I would be happy to discuss a set of methods to benchmark against before running experiments.
- There is no discussion on the additional memory burden introduced by storing the source data in the paper. In Figure 2, EATA and DISTA are compared in terms of additional computation, but not in terms of additional memory. The memory requirement is quite drastic: [ResNet50](https://pytorch.org/vision/main/models/generated/torchvision.models.resnet50.html) weights are quoted at about 97.8 MB per model. Storing the source model is easy (as batch norm params are light), but storing the *source dataset*, which is required for this method, is of course very memory heavy. Can the authors comments if the results were conducted with using the full imagenet dataset, or subsampling it somehow? If the full imagenet dataset is used, this adds 160GB of additional storage. At this storage requirement, it would have been possible to run much bigger models, e.g. an EffNet-L2 ([Xie et al., 2020](https://arxiv.org/abs/1911.04252)) which cuts the reported error rates much more drasticially than DISTA (under higher compute requirements, of course). The memory requirement is a big limitation, and (in my opinion) one of the main reason why TTA is hard.
- Why not consider datasets for natural corruptions, like ImageNet-R, -D, ObjectNet, etc., on top of ImageNet-C?

Additional weaknesses and comments:

- "signficiantly" is used throughout the paper, and not a single error bar is provided. Please either compute error bars and proper stats, or replace this by a different term.
- There is a confusion of "improvement by X%" when "improvement by X percentage points"/"X% points" is meant. I think the confusion is used consistently, though, so might be fine.
- "large scale": I find it questionable if nowadays, ImageNet-C still constitutes a large scale dataset, but this is a minor point/comment. I would suggest to simply drop the term.
- Methodology: The start is loaded with (in my opinion) unnecessary notation for very simple concepts like how the classifier is setup. I would suggest to make this more crisp, as it does not really add much to the paper, the setup is very standard.
- The table headings should outlined which model is used for the results
- How stochastic is the method? Errorbars should be provided.
- The empirical results are somewhat limited in the breadth of explored methods. It would improve/broaden the scope if additional models, e.g. larger resnets etc. were used.


___
* note that also EATA slightly deviates from the pure TTA setup, as they leveraged clean source images for the computation of their regularizer, cf. the original paper for details.

### Questions
1. Why is there no discussion of domain adaptation, given that Eq. (4) is pretty much exactly the commonly used formulation of unsupervised domain adaptation?
2. If access to source data is allowed, then a wealth of non-TTA, unsupervised domain adaptation methods exist to perform the adaptation task. However, the paper only benchmarks against TTA approaches. Which 
3. Did you re-ran the results of other methods and yours within a single codebase (i.e., did you re-eval prev methods), or did you copy numbers from papers?
4. How were $\epsilon$ and $E_0$, which influence the weighting of both losses, tuned? An analyis table for varying these two parameters on a hold-out set (or however they were validated) is missing and should be added to the next paper version.


**Additional questions:**

- Abstract, "key challenge in TTA: adapting on limited data": Can you give references that identify this as a key challenge? Quite to the contrary, when adapting a model at test-time, especially in continual settings, I would argue that a wealth of data exists.
- Abstract, "conducting several adaptation steps ... will lead to overfitting": I am not aware of work suffering from this. Can you give a reference? Is there an experiment in the paper where you specifically show that DISTA resolves this?
- Abstract, in many realistic scenarios, the stream revals insufficent data to fully adapt": What are examples of such settings, and where was this shown?

### Soundness
2 fair

### Presentation
1 poor

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
The paper focuses on improving test time adaptation of ImageNet pretrained models on distribution shifts of ImageNet-C and ImageNet-3DCC. In addition to the test time entropy minimization objective, the paper propose to distill the predictions of unlabeled source samples from the original pretrained model during adaptation. Authors show that this additional auxiliary task improves model adaptation on target distribution data in both episodic and continual test time adaptation settings.

### Strengths
-	Proposed a novel auxiliary task for test-time adaptation problem setting.

-	Proposed method is simple and shown to be effective.

-	Method explanation is easy to understand and follow.

-	Results show good improvement over prior work on both ImageNet-C and ImageNet-3DCC.

### Weaknesses
 - Intuition behind eq, (3) is not straightforward. In particular, $\theta_{t+1}$ is obtained by updating ${\theta_t}^c$ using the gradients w.r.t  $\theta$. Discussing the intuition behind it would be helpful. Specifically, the two-step update process involving $\theta_t^c$ and then $\theta_{t+1}$ is unclear, and the motivation for using the gradient with respect to $\theta$ at $\theta_t^c$ to update $\theta_t^c$ is not well-explained. It's unclear why this intermediate step is necessary and how it contributes to the overall adaptation process.

- It is mentioned in the 2nd line of Page 4, $\mathcal{D}_s$ is sampled from the training dataset. The pretrained network has seen the $\mathcal{D}_s$ samples during its pretraining and potentially have lower entropy on those samples. Following the motivation of this work that targets to use unlabeled data, it is important to use unseen unlabeled data from source distribution for the auxiliary tasks, not the samples from the seen training set. The use of training data for the auxiliary task might introduce a bias towards the original training distribution, hindering the adaptation to new, unseen distributions. The auxiliary task's effectiveness could be compromised if it relies on data the model has already memorized.

- No ablation study on the size of unlabeled source dataset $\mathcal{D}_s$ is provided. This ablation study is important as this dataset shown to guide the adaptation process. Without exploring different sizes of $\mathcal{D}_s$, it is difficult to determine the optimal amount of source data needed for effective adaptation. The sensitivity of the method to the size of $\mathcal{D}_s$ is also unknown, which is crucial for practical implementation.

- category-wise federated TTA, where all clients are assumed to know beforehand that adaptation carries out on similar category of domain shifts. It is a controlled setting, and not a realistic one. Federated TTA with diverse distribution shifts across clients would be an interesting scenario. This setting limits the generalizability of the findings to real-world scenarios where clients might experience significantly different types of domain shifts. The current evaluation does not fully demonstrate the robustness of the method under more realistic and challenging federated settings.

### Questions
-	Consider sampling $\mathcal{D}_s$ from unseen unlabeled data from source distribution.
-	What should be the size of $\mathcal{D}_s$? How the results vary with the $\mathcal{D}_s$ size? Do the samples in $\mathcal{D}_s$ need to be class-balanced? 
-	Is $f_\theta$ in eq. (3) defaults to $f_{\theta}$ at time t?
-	What is the intuition behind updating ${\theta_t}^c$ using the gradients w.r.t  $\theta$ in eq. (3)?
-	Since $\mathcal{D}_s$ are sampled from training set, how the results would change if ground-truth labels are used in eq. (5)?
-	I understood the lookahead concept. However, what makes entropy minimization on clean data accelerate adaptation. Data distribution between clean data and targeted adapted data is different, so no additional distribution knowledge is provided to the network.
-	Please mention the network architecture used in respective figure and table captions.

I will reconsider my rating based on the authors feedback on my concerns.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Post rebuttal: Some of the original concerns remain. The new experiments on labeled vs unlabelled source data further show that the narrative of the paper needs further work. 

-------------------------------------------
The paper proposes a method for test-time adaptation that deals with limited data. This is done by adding a distillation loss on the source trained and frozen model on source data to the traditional entropy penalty on the target data. With experiments on ImageNet-C and ImageNet-3DCC, the paper shows that the method outperforms some of the recent techniques on TTA on online, continual and federated evaluations. The paper also proposes an analysis tool that is called _lookahead analysis_ which compares the entropy of predictions on a batch before and after doing the adaptation with the source distillation loss.

### Strengths
The proposed method is a simple extension to the existing methods, and is intuitive to understand. The experiments are sufficient to show the performance benefits. The work is placed well among existing works.

### Weaknesses
The method proposed in the paper is interesting, but the overall paper read like ad-hoc arguments stitched together. For example, the arguments for availability of _unlabled_ source data at inference, as opposed to storing some training data in a replay buffer is very unconvincing. It is also very unclear if the two problems that the paper set out to solve are tackled, as there doesn't seem to be any quantification of either one. The justification for federated evaluation are not convincing. Additionally, the lookahead analysis tool only measures the correlation between entropy of aux task and test data, but doesn't inform us of the test accuracy. While prior works have shows the correlation between test data entropy and accuracy, this cannot be taken for granted, as the paper doesn't show when the proposed method _doesn't_ work i.e., when is having source distillation not useful or harmless.

In addition to the weaknesses mentioned, I have the following questions about the experimentation:
* The ablation only shows the batch size more than 8. How does the method behave when the batch size is 1. MEMO shows this is possible with special handling of batchnorm params. 
* What are the effects of the source data batch size, and size of the unlabeled source data stored on performance? 
* What are the trainable parameters? Is it only normalization or the whole network? What are the effects? 
* What is the importance of the $E_0$ parameter on the data filtration process? While this is  proposed in prior works, an study of this in the current work could be illuminating.

### Questions
In addition to the weaknesses mentioned, I have the following questions about the experimentation:
* The ablation only shows the batch size more than 8. How does the method behave when the batch size is 1. MEMO shows this is possible with special handling of batchnorm params. 
* What are the effects of the source data batch size, and size of the unlabeled source data stored on performance? 
* What are the trainable parameters? Is it only normalization or the whole network? What are the effects? 
* What is the importance of the $E_0$ parameter on the data filtration process? While this is  proposed in prior works, an study of this in the current work could be illuminating. 

If the authors can provide convincing arguments, I would be happy to raise my scores.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
