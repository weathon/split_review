# A Second-Order Perspective on Model Compositionality and Incremental Learning

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
The fine-tuning of deep pre-trained models has revealed compositional properties, with multiple specialized modules that can be arbitrarily composed into a single, multi-task model. However, identifying the conditions that promote compositionality remains an open issue, with recent efforts concentrating mainly on linearized networks. We conduct a theoretical study that attempts to demystify compositionality in standard non-linear networks through the second-order Taylor approximation of the loss function. The proposed formulation highlights the importance of staying within the pre-training basin to achieve composable modules. Moreover, it provides the basis for two dual incremental training algorithms: the one from the perspective of multiple models trained individually, while the other aims to optimize the composed model as a whole. We probe their application in incremental classification tasks and highlight some valuable skills. In fact, the pool of incrementally learned modules not only supports the creation of an effective multi-task model but also enables unlearning and specialization in certain tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper conducts a theoretical analysis of model fusion in parameter space through the analysis of the second-order Taylor approximation of the multitask loss function. 

The authors begin by showing that the 2nd order approximation of the multitask (MT) loss, when evaluated on the $w$-weighted averaged of individual models ($\theta_P = w_1\theta_1 + ... + w_t\theta_t$), is upper bounded by $w$-weighted sum of individual models evaluated on the same multitask data. From this observation, the authors argue that, if each individual model could perform well on all tasks, this would drive the MT loss on $\theta_P$ down. 

Given that individual models cannot be optimized on data outside their training distribution, the authors instead propose to regularize individual models towards the base pretrained model $\theta_0$, for such samples. This leads the authors to propose a EWC-like regularizer between $\theta_0$ and $\theta_t$ (when optimizing $\theta_t$) where the Empirical Fisher Information Matrix can be computed iteratively, accumulating gradients from $\theta_0$ on data from task $t$. 

Furthermore, the authors proceed to quantify the exact gap between the previous inequality, showing that term is a function of the weighted alignment across task vectors. The authors then proceed to propose a new learning algorithm, which extends the previous EWC regularizer to also penalize not only differences between $\theta_0$ and $\theta_t$, but also difference between $\theta_t$ and subsequent  learned task vectors $\theta_{<t}$. 

The authors proceed to analyze their methods on class-incremental learning benchmarks, showing favorable results. An ablation showing the importance of the EWC regularizer is also provided. Finally, akin to Task Arithmetic manipulations, the authors show that task vectors can be used to enhance or unlearn specific task knowledge.

### Strengths
1. The paper proposes a novel theoretical analysis of the multitask loss through a second-order Taylor expansion, leading to interesting insights (namely equation 5 & 14)
2. The authors leverage this insight to propose new methods for incremental learning with weight-space merging, showing favorable results. 
3. The paper is well-structured, and the experimental section contains relevant ablations showing the effectiveness of the proposed components

### Weaknesses
I have some reservations as to the motivation of the proposed methods.

1. Regarding equation 5, I agree that should all individual models perform well on all tasks, then  $\theta_P$ would likely perform quite well. That being said, I find that approximating this condition by regularizing the task vectors to stay close to the base model somewhat of a big conceptual leap. By construction, the base model performs sub-optimally on the tasks for which we optimize a task vector, otherwise the task-specific optimization does not serve much purpose. Therefore, in Eq. 5, wouldn't replacing $\theta_t$ with $\theta_0$ for any $x \sim p_{t'}, t' \neq t$, still make the upper bound loose, and therefore not useful ? Specifically, the core idea relies on the premise that the base model, despite being suboptimal for individual tasks, possesses a broad set of features that are beneficial across all tasks. However, the paper does not provide any theoretical justification or empirical evidence to support this claim. It is not clear why the base model's feature space should be considered a good prior for all downstream tasks, especially when those tasks are significantly different from the pre-training data.

2. The authors motivate ITA vs IEL as an approach that can be executed in a decentralized fashion. However, I am not sure this is the case; given that the FIM is updated sequentially, how would one train several tasks in a decentralized manner without communicating FIM statistics? The sequential update of the FIM, even if computed with respect to the base model, still implies a dependency between tasks, which contradicts the idea of decentralized training. The paper does not clarify how the FIM can be computed and merged across different clients without introducing a sequential bottleneck or requiring a central server to accumulate and redistribute the FIM statistics. This lack of clarity undermines the claim of decentralized learning.

### Questions
1. How different are the task vectors learned with ITA vs IEL ? Do you find them to be well-aligned ?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper explores how incremental learning can be addressed through incremental model merging. The theoretical framework is based on the following intuition(s):
- if the base model is already well suited for the downstream asks (\theta_0 is a local min.), fine-tuned versions of this base model will merge better. This connects well to the recent work [5], which shows that stronger base models (instruction tuned, or more params.) lead to better merging.
This intuition serves as a starting point for their theoretical analysis and the derivation of the **ITA** method, which is similar in spirit to ColD Fusion (which does not include the EWC term) [1]. ITA ensures that each new fine-tuned model lies in the viscidity of the base model (as measured by Riemannian distance), which intuitively results in better merging.

It has to be noted, that because this work addressed image classification setting where each task has a different output space, in order to make sure that the base model is a local minimum of the downstream tasks, authors propose the so-called "task pre-consolidation" step, which involves training a task-specific on a fixed backbone before the backbone's params. are learned. The importance of this type of alignment has been recently explored in [2].

**ITA method**: in essence, this method is similar to EWC, with the difference that for each new task we start from the base model (\theta_0) and not from the model learned for the previous task (I have some questions regarding the motivation of this approach, see questions part)

While ITA enables completely independent model training in the spirit of "MoErging" methods [3], one problem with ITA is the fact that each new task's model only transfers knowledge from the base model and not from other tasks. Motivated by this, the paper proposes **IEL** method. IEL optimizes each new task vector assuming access to the merged model on tasks seen so far (somewhat standard in CL literature). This amounts to using both EWC regularization w.r.t to the base model and task alignment term ensuring the new task vector is similar to the previous ones. Importantly, the gradients of the regularization term in IEL can be computed efficiently. 

This paper presents a solid empirical section with several interesting insights. All the theoretical insights are substantiated with empirical validations.


[1] Don-Yehiya, Shachar, et al. "Cold fusion: Collaborative descent for distributed multitask finetuning." _arXiv preprint arXiv:2212.01378_ (2022).

[2] Schmidt, Fabian David, Ivan Vulić, and Goran Glavaš. "Free lunch: Robust cross-lingual transfer via model checkpoint averaging." _arXiv preprint arXiv:2305.16834_ (2023).

[3] Yadav, Prateek, et al. "A survey on model moerging: Recycling and routing among specialized experts for collaborative learning." _arXiv preprint arXiv:2408.07057_ (2024).

[4] Ostapenko, Oleksiy, et al. "Continual learning with foundation models: An empirical study of latent replay." _Conference on lifelong learning agents_. PMLR, 2022.

[5] Yadav, Prateek, et al. "What Matters for Model Merging at Scale?." _arXiv preprint arXiv:2410.03617_ (2024).

### Strengths
Overall, while the idea of using model merging for continual learning has been explored in previous works, see e.g. [1], this paper does a good job of first formalizing intuitive ideas into an appealing theoretical framework, and subsequently validating these intuitions (and theoretical insights) empirically.  While I have several questions regarding several formulations made in the paper, the overall quality of the work is commendable. 

Another strength of this work is its empirical section. Even though experiments are performed only on the image classification domain, a broad range of datasets is covered including also datasets which are OOD w.r.t the backbone.

### Weaknesses
 - This works connects to several existing works in the realm of model merging, see the "summary" section of my review. These works are not cited in the current version, maybe because these connections were not obvious to the authors. I suggest the authors revisit this potential connection and cite the related works.

 - ll. 028: "Recent AI technologies are predominantly being viewed as monoliths": while I understand the point authors are making here, it must be acknowledged that modular architectures, such as MoE have become increasingly widely used in recent years (maybe as wide as monolithic models)
- ll. 152-157: the paragraph seems to argue that the right-hand side of equation 5 will increase as new tasks are learned. But in equation 5's right-hand side, each individual loss starts from the base model and does not depend on any form of continual learning. So I am not sure I understand the argument being made here.
- would the pre-consolidation step be necessary in language modelling, where the output space is usually shared across tasks? 
Empirical section:
- are the different classification heads of the task-specific models also merged together? if so, does it mean that all tasks must have the same number of classes (i.e. share the output space)? 
- since IN-R, C-100 and CUB are very much id-distribution w.r.t pre-training on imagenet, I wonder whether simple fine-tuning of the final classification layer, which can be a metric-based classifier with no forgetting, can be sufficient to achieve good performance? (e.g. see [4])
- Did the authors investigate the effect of pre-consolidation on the CL performance?

### Questions
- ll. 028: "Recent AI technologies are predominantly being viewed as monoliths": while I understand the point authors are making here, it must be acknowledged that modular architectures, such as MoE have become increasingly widely used in recent years (maybe as wide as monolithic models)
- ll. 152-157: the paragraph seems to argue that the right-hand side of equation 5 will increase as new tasks are learned. But in equation 5's right-hand side, each individual loss starts from the base model and does not depend on any form of continual learning. So I am not sure I understand the argument being made here.
- would the pre-consolidation step be necessary in language modelling, where the output space is usually shared across tasks? 
Empirical section:
- are the different classification heads of the task-specific models also merged together? if so, does it mean that all tasks must have the same number of classes (i.e. share the output space)? 
- since IN-R, C-100 and CUB are very much id-distribution w.r.t pre-training on imagenet, I wonder whether simple fine-tuning of the final classification layer, which can be a metric-based classifier with no forgetting, can be sufficient to achieve good performance? (e.g. see [4])
- Did the authors investigate the effect of pre-consolidation on the CL performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this work, the author(s) examines the compositional properties of fine-tuning deep pre-trained models, focusing on how specialized modules within these models can be combined to create a single, multi-task model. To be specific, the author leverage a second-order Taylor approximation to understand what promotes compositionality in non-linear networks.

### Strengths
This approach reveals the importance of staying within the pre-training 'basin' to create composable modules. To achieve this, the authors introduce two incremental training algorithms: 1) training multiple models individually, and 2) optimizing the entire composed model.

The theoretical analysis section is well-developed, and the experiments are clearly presented.

Tested on incremental classification tasks, this approach enables the creation of an effective multi-task model, with capabilities for unlearning and specialization in specific tasks.

### Weaknesses
Major:

The motivation for using the second-order linear approximation is unclear. To my understanding, this work employs a similar approach to neural tangent kernel (NTK) analyses. However, in the linear approximation, NTK typically uses the first-order Taylor expansion, here the author employs the second order. Why not use the first-order Taylor expansion, which is standard in NTK analysis, or explore the potential benefits of a third-order expansion? A more detailed justification for choosing the second-order approximation is needed, especially given that the computational cost increases with higher-order terms. It would be beneficial for the authors to add a section comparing their work with [1,2], specifically addressing how their approach differs from the first-order approximation used in NTK and discussing the implications of using a second-order expansion, particularly in relation to Eq.3-4 and Lemma 3.1 in [2].

Also, there are NTK-based class incremental learning works [3-5]. The authors could include a section in the introduction or discussion to clearly point out the differences and benefits of using their approach compared to these works. Specifically, a comparison should be made regarding the computational complexity, performance, and theoretical guarantees of their method versus existing NTK-based continual learning techniques.

Minor issue: 

Some notation is hard to follow and not clearly defined, such as $ L_{\text{cur}}$. The definition of in incremental learning $t,T,\tau$ might also be confusing. The dataset $D_t$ contains $n_t$ training samples $x, y) \sim p_t(x, y)$, drawn from a distribution that varies across tasks. The authors use $\tau$ for $ T $ from $1 \ldots t $, so it is likely that $D_T$ would be more appropriate.

### Questions
see weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies model compositionality applied under class-incremental continual learning settings, where individual models fine-tuned on disjoint tasks are composed via weight averaging. By studying the second-order Taylor expansion of deep networks about a strong initial condition, the paper motivates two modifications to existing training objectives. The first encourages local linearity in model weights by minimizing the change in weights (from the pre-trained point) resulting from fine-tuning, which is shown to penalize deviations between the pre-trained and fine-tuned model outputs. The second operates in the regime where individual model weight perturbations are fine-tuned using the loss computed from the _composed_ model. The paper proposes adding a regularizer to minimize the deviation between the loss resulting from weight composition, and the loss resulting from output composition (ensembling).

### Strengths
- The paper explores the model composition approach for continual learning, which has strong advantages in more general settings, for instance in federated setups where individual models can be trained in parallel on disjoint datasets and then composed at the end.
- I appreciate the idea of enforcing local convexity or linearity via regularization, since this circumvents the need to do so explicitly via model linearization techniques like in TMC, and it appears to work very well in practice (Table 1).
- The composed model training objective proposed in IEL is also intuitive, essentially "learning to compose" since each new task perturbation is conditioned on all previously seen ones.
- Experiments are comprehensive and a variety of datasets are explored at least in the class-incremental setting. Method performs well across all datasets.

### Weaknesses
 - The regularization condition proposed in Sec 2.2 does not seem to necessitate the second-order analysis, since it simply aims to enforce a local (first-order) linear structure by making perturbation smaller.
- The wording on "incrementally train(ing) the whole composed model rather than its individual components" used throughout the paper is misleading. I only understood what this statement is trying to convey after seeing equation (15) on Page 5. It appears to me that what is being trained is still individual perturbation components ($\tau_1, \ldots, \tau_T$) , but only that the _loss_ is computed based on the composed model. I would suggest modifying the terminology for better clarity.
- L120 assumes that the pre-trained initialization $\theta_0$ is globally optimal for a quadratic model trained on the union of all tasks. This seems to be a very strong assumption that likely would never hold in practice (why train/compose when the initialization is already optimal?), contrary to what is claimed in footnote 1. This weakens the theoretical analysis.
- Lacks wall-clock time comparison ($\mathcal{O}(1)$ does not shed any light on the actual cost incurred), for instance that used to update the FIM, which is important to faithfully evaluate the method w.r.t. to other works.
- The need for the task pre-consolidation (linear probing, etc.) stage requires additional training steps, so comparisons to most existing methods that do not require this would not be completely fair. If the paper did not implement control steps to make fairer comparisons, then this should be mentioned explicitly in the limitations.

### Questions
- I see some replay-based methods like DER++ are included in Table 1, but I don't see any mention of the experimental setup used for these comparisons (e.g. assumptions on buffer size)
- Equation (13) suggests that by minimizing $\Omega$, IEL also seeks to encourage linearity in the loss, as done in ITA.  Can you provide some intuition (formal or informal) regarding under what regimes IEL fairs better than ITA, and vice-versa?

### Soundness
3

### Presentation
3

### Contribution
3
