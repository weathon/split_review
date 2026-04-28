# Mitigating backdoor attacks with generative modelling and dataset relabelling

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
Data-poisoning attacks 
change a small portion 
of the training dataset
by introducing hand-crafted triggers 
and rewiring the corresponding labels 
towards a desired target class.
Training on such data injects 
a backdoor into the model,  
that causes incorrect inference 
in selected test examples.
Existing defenses mitigate 
the risks of such attacks 
through various modifications
of the standard discriminative learning procedure.
This paper explores a different approach
that promises clean models 
by means of per-class generative modelling. 
We start by mapping the input data
into a suitable latent space
by leveraging a pre-trained 
self-supervised feature extractor.
Interestingly, these representations
get either preserved or heavily disturbed
under recent backdoor attacks.
In both cases, we find that 
per-class generative models
give rise to probabilistic densities
that allow both to detect the poisoned data
and to find their original classes.
This allows to patch the poisoned dataset
by reverting the original labels
and considering the triggers 
as a kind of augmentation.
Our experiments show that
training on patched datasets
greatly reduces attack success rate
and retains the clean accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to model the per-class distribution with a generative model and uses it to sanitise the data against backdoors. The approach operates in a latent dimension as opposed to the input space. Under the assumption and empirical observation (Figure 3, Figure 4) that the poisoned samples will exhibit different density scores for their target classes, they use a threshold to identify the poisoned samples in two scenarios

### Strengths
- This paper builds on an empirical observation that comparing per-class densities over extracted features can reveal poisoning behaviour. 

- The ablation study shows that choice of feature representation doesn’t significantly vary the performance with two models resulting in marginal differences in attack success rate and accuracy

### Weaknesses
 - I think the paper can improve with investigation of what makes a generative model stand out? Perhaps an investigation of how adaptive attacks can circumvent the threshold based detector?

- Similarly, the paper can also benefit from investigation of the choice of threshold \beta_ND and \beta_D. 

- Figure 1 and its legend are a bit small to read

### Questions
- How sensitive is this method with respect to choice of thresholds?

- It is unclear what the limits of this approach are? Are there scenarios where this detector will fail to detect?

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
This paper proposes a new method for robust training of neural network classifiers against backdoor data poisonings. In short, backdoor attacks aim to create hidden associations between a trigger and a target class by poisoning a small portion of the training data. This can be done via attaching small triggers to the image and optionally changing the labels associated with each image. If the label is changed, the attack is called poisoned-label attacks, while attacks that do not change the labels are called clean label attacks.

In this paper, the authors proposes a three stage process for purifying the poisoned dataset and training a robust model that is free of backdoors. In the first step, they use a self-supervised method such as SimCLR to train a feature extractor on the poisoned dataset. Using this feature extractor, they then get the feature representations of all the training samples. In the second step, they train a generative model (here normalizing flows) for each class representation. Using these normalizing flows, they then defined a likelihood-based score function to identify poisonous samples from clean ones. This step is motivated by earlier observations on the feature space representation of backdoor attacks using self-supervised models. In particular, for samples that are likely to be poisoned-label attacks, the proposed method can identify the target class and correctify their labels. Some samples are also removed from the training dataset if they do not belong to any of the previous categories. Once this step is done, a neural network is finally trained over the purified dataset.

Experimental results over CIFAR-10, ImageNet-30, and VGGFace indicate the effectiveness of the proposed method against poisoned-label and clean-label backdoor attacks.

### Strengths
- The proposed method is novel and interesting. It is based on an empirical observation around the feature space representation of poisoned data in the feature space of models trained with self-supervised learning. The use of normalizing flows to model the per-class latent space distribution is also novel.

- Empirical results indicate that this three stage method can mitigate the effect of backdoor attacks. Even more interestingly, it can revive the poisoned-label samples and re-use them in the training process.

### Weaknesses
 - Even though the proposed method is working well, it is highly inefficient and requires lots of compute. In particular, the proposed method starts with self-supervised pre-training of a feature extractor using SimCLR. Then, it trains _one_ normalizing flow _per each class_ to finally be able to get rid of poisonous samples and start training a robust model. Such extensive use of resources is quite intensive, and frankly speaking, might be redundant. The field of backdoor defense has came up with alternative solutions such as [1-4] that are far more efficient than the proposed solution where some of them just take one training round to give robust models. Apart from the expensive self-supervised training at the beginning, the proposed solution requires one flow-based model per class which means that its resources grows linearly with the number of classes. 

- In lieu of the previous issue, first the paper needs to include more recent baselines [1-3], and second, it is important to include the total training time (from start to delivering a robust model) for all of the methods. This way, the readers can have a better understanding of the computational efficiency of current methods. The current evaluation lacks a direct comparison of wall-clock time, making it difficult to assess the practical feasibility of the proposed approach compared to more efficient alternatives. For example, methods like [1] and [2] are designed to be computationally lightweight, and a comparison of total training time would highlight the trade-offs between defense effectiveness and computational cost.

- There are certain parts in the paper that might cause confusion. For instance, the explanations given in Sections 4.5-4.6 are seem contrasting. On the one hand, the paper says that for clean samples the score $s_{y}(\boldsymbol{z})$ is higher. On the other hand, the same score is also higher for disruptive poisoning. Figure 4 also shows the same trend for both the clean samples as well as disruptive attacks. I think that these two sections should be re-written (see below for questions), because currently it seems that some of the clean samples can also initially be removed by this method. If this is the case, it should be explained. Optionally, adding a diagram of step-by-step poisoned sample removal might also be helpful. The paper's explanation of the filtration process is unclear, particularly regarding how the score $s_{y}(\boldsymbol{z})$ is used to differentiate between clean and poisoned samples. The contradictory statements in Sections 4.5 and 4.6, along with the trends shown in Figure 4, suggest that the method might inadvertently remove clean samples, which could explain the lower benign accuracy observed in some experiments. A clearer explanation, perhaps with a step-by-step diagram, would be beneficial.

### Questions
- Claiming that this work is "the first backdoor defense based on generative modelling" is inaccurate. For one, MESA [5] has also used generative modelling as a solution to neural backdoors.

- Why do we need to identify/remove poisonous samples using class conditional normalizing flows and then train another neural network of our task? In other words, can't we just use the per-class normalizing flow for classification as well? Running experiments on this scenario is highly encouraged.

- Can you repeat the same process for generating Figure 1 for other attacks?

- Based on the Figure 1 (left), the proposed method heavily relies on the fact that the poisoned samples in the target class are scarce. What happens if the number of poisoned samples (those with triggers) that use the same trigger are abundant? Experiments on this scenario is highly encouraged.

- Section 4.5 and 4.6 are rather confusing. Can you please elaborate on the filtration procedure? The paper currently says that "We include the samples with $\alpha$ highest poisoning scores in $\hat{\mathcal{D}}\_{\mathrm{P}}$, and include the samples with the $\alpha$ lowest poisoning scores together with samples from identified clean classes in $\hat{\mathcal{D}}\_{\mathrm{C}}$." Do these two steps done on the same score graph? Does this mean that some of the clean samples are also removed? Potentially, is this the reason for the under-performance of the proposed method in the case of high poison rate (Table 4)?

- What experimental settings (number of epochs, etc.) are used for SimCLR? What is the architecture of normalizing flows?

- As mentioned above, add the mentioned baselines and report the total training time for all of the methods to see the computational efficiency.

- Why so many number of epochs (200) is used for training models? Usually, 120 epochs is enough to train ResNet models with SGD on CIFAR-10.
 
[5] Qiao, Ximing, Yukun Yang, and Hai Li. "Defending neural backdoors via generative distribution modeling." _NeurIPS_, 2019.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel method to detect and mitigate data poisoning attacks by means of per-class generative modeling. Instead of training the generative models on image space, which is claimed ineffective, the paper proposes to model the latent embeddings extracted by a self-supervised-learning feature extractor, using per-class normalizing flows. Then, it detects backdoor classes based on the average log-density over all foreign examples. Next, it computes a poisoning score to split samples of the identified target classes into clean, poisoned, and uncertain sets. Finally, the samples in the poisoned set are relabeled and combined with the clean set to produce a cleansed dataset for training. The method effectively mitigates common dirty-label attacks and one clean-label method on CIFAR-10, ImageNet, and VGGFace2.

### Strengths
- The paper explores a new approach for poisoning attack mitigation using generative modeling. While training the generative models on image space is ineffective, the paper proposes to use model the latent embeddings extracted by a self-supervised-learning feature extractor.
- The method effectively mitigates common dirty-label attacks and one clean-label method on CIFAR-10, ImageNet, and VGGFace2.

### Weaknesses
 - The last two sentences in Section 4.5 are confusing. Although the numerator is extremely low, why is the score significantly higher? Also, if the poisoned samples score significantly higher than clean samples, aren't those poisoned samples mislabeled into the clean set? Finally, the arguments may be invalid by ignoring the change of the denominator.

- The paper experiments with only one clean-label attack, which injects adversarial noises into the poisoned data. Hence, it assumes that with clean-label attacks, the poisoned samples are completely distinct from the rest of the dataset in the self-supervised feature
space. That assumption may be incorrect with other clean-label attacks such as SIG [1] and Refool [2].

- The paper should discuss some adaptive attacks. For instance, the attacker can tune the backdoor trigger to fool a surrogate SimCLR model trained on clean data.

- The proposed method depends on too many hyper-parameters (\alpha, \lambda, \beta_{ND}, \beta_D). I cannot see how the selected values of these hyper-parameters are general and can work for all scenarios. The authors should ablate the choice of these hyper-parameters, particularly under different poisoning rates.

- \alpha is set as 0.15. 
  - First, it means 70% of samples of the identified target class are uncertain and will be removed, which is a lot. It will weaken the cleansed dataset significantly, particularly when multiple (or all) classes are poisoned.
  - Also, all samples in the D_p are relabeled to a different class (Eq. 7), which is problematic if the percentage of the poisoned examples is less than 15% of the number of samples in the target class. For instance, in the case of CIFAR-10 with a 1% poisoning rate, the poisoned examples cover less than 9% of the samples in the target class, meaning more than 6% of the clean images in the target class are relabeled wrongly.
  - 15% of the samples in the target class are set as clean. It becomes problematic if the poisoned examples cover more than 85% of the samples of the target class. That situation can happen when the number of classes is high, e.g., a classification task with 100 classes and a poisoning rate of 10%.

- How does the algorithm behave in case the dataset is clean? And how does it behave under all2all attacks?

### Questions
- The last two sentences in Section 4.5 are confusing. Although the numerator is extremely low, why is the score significantly higher? Also, if the poisoned samples score significantly higher than clean samples, aren't those poisoned samples mislabeled into the clean set? Finally, the arguments may be invalid by ignoring the change of the denominator.
- The authors should run the analysis in Fig. 1 and the experiments in Table 1 using SIG and Refool attacks?
- The authors should define and examine some potential adaptive attacks?
- The authors should ablate the choice of the hyper-parameters (\alpha, \lambda, \beta_{ND}, \beta_D), particularly under different poisoning rates.
- A more in-depth discussion on the impact of the value choice for \alpha.
- How does the algorithm behave in case the dataset is clean? And how does it behave under all2all attacks?

-

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a sanitization-based defense against backdoor attacks.  Specifically, the authors learn generative models over class conditional feature space representations.  These learned distributions are then used to filter suspect training data, with the final model trained over the sanitized dataset.

### Strengths
Machine learning models are brittle, and as models are deployed in settings critical to human well-being, model failures can lead to real-world harm. This paper proposes a simple, intuitive method to improve model robustness. The paper follows the classic paradigm of using generative models to improve discriminative models' performance (i.e., robustness).

### Weaknesses
Like all other empirical defenses, the authors' method comes with no guarantees on its effectiveness.  In my view, empirical defense papers must meet two necessary conditions to be fit for publication.  Unfortunately, this paper does not meet either.
1. The paper should explicitly note that their method comes with no guarantees and contrast this weakness against the plethora of papers (e.g., [1]) that provide methods certifiably robust to training data attacks.
2. The paper should ideally evaluate against an adaptive attacker who is aware of their defense and actively tries to avoid it.  At the very minimum, the paper should include a convincing discussion of why an adaptive attacker is not feasible or reasonable.

The authors define $D^y_{F}=\{f_{\theta_F}(x_i) \vert y_i = y \}$. As I understand it, $D^y_F$ contains the set of features for all training instances whose **true label** is $y$.  (Note at the bottom of page 3, I believe $y_i$ is defined as the true labels).  Of course, $y_i$ for the poisoned data is unknown (otherwise, the problem is trivial).  I cannot determine whether there is a problem with the notation or method, but it seems ${D}_F^y$ is not known as defined.  Perhaps the authors are assuming a clean validation set to learn these generative models (as in other work), but I do not see a discussion of that.  This is a major concern and one reason I rate the soundness as 1.

In the "Questions" section below, I detail a concern about overstating the paper's novel contributions.  I will wait for the authors' response before categorically defining it as a weakness.

I **strongly** recommend either removing or redesigning Figure 2. The flow of the figure is very non-linear and non-intuitive. Best I can determine, the figure could have a linear progression starting at the initial poisoned dataset and terminating with the final trained model. Perhaps the authors chose this non-linear progression to save space, but I would view this as an especially poor choice.
* One potential way to solve this problem entirely is to change Figure 2 to an algorithm.

Several typographical issues exist in the paper.  I provide a non-exhaustive list below. These did not affect my overall score.
* Page 1: "...stealthines..."
* The authors repeatedly use `\citet{...}` in place of `\citep{...}`. See for example the two citations on page 1 in the paragraph that begins "In this work, ...".
* Page 7: "...fllowing...:"
* Page 7: ", Sample specific" ("S" should not be capitalized here)
* Page 7: "sample0specific"
* Page 13: In multiple places, the letter "x" is used in math mode when specifying dimensions resulting in the "x" being italics.  Either do not place the x in math mode or better use `\times` instead of "x".

Table 4 should show the minimum poisoning rate where either the attacks or the defenses start to fail.  For example, does your defense still work at 0.1% poisoning rate.
* Poisoning rate is also only one dimension of an attack's strength. Perturbation strength is an orthogonal dimension of attack strength against which the authors' defense is surely highly susceptible but is not explored in the empirical evaluation.

The empirical evaluation's main results use either a 10% or 25% poisoning rate.  In my view, those attack rates are wholly unrealistic for any marginally plausible real-world scenario.  I would go so far as to consider those poisoning rates not meaningful to study since I cannot see a case where an attacker is inserting 25% poisoned data.

The proposed method is studied only in the vision context. Other modalities are not explored or discussed.

### Questions
On page 2, you summarize the paper's second contribution writing, "*We propose the first backdoor defense based on generative modeling*."  This is a very broad claim that I suspect is not true. For example, [1] uses backdoor modeling for a backdoor defense back at NeurIPS 2019.   Please speak more to the basis of this claim.

At the beginning of Section 3.1, the authors write, "*We consider backdoor defenses that avoid standard supervised learning due to its sensitivity to poisoned labels and susceptibility to overfitting*." When I encountered this sentence when reading through the paper the first time, I did not understand what the authors meant, and after completing the paper, I am not sure I understood it.

### References

[1] Qiao et al. "Defending Neural Backdoors via Generative Distribution Modeling" NeurIPS'2019.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
