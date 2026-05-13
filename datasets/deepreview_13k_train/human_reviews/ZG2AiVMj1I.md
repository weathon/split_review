# IBCL: Zero-shot Model Generation for Task Trade-offs in Continual Learning

- Decision: Reject
- Scores: 3, 6, 3, 8

## Abstract
Like generic multi-task learning, continual learning has the nature of multi-objective optimization, and therefore faces a trade-off between the performance of different tasks. That is, to optimize for the current task distribution, it may need to compromise performance on some previous tasks. This means that there exist multiple models that are Pareto-optimal at different times, each addressing a distinct task performance trade-off. Researchers have discussed how to train particular models to address specific trade-off preferences. However, existing algorithms require training overheads proportional to the number of preferences---a large burden when there are multiple, possibly infinitely many, preferences. As a response, we propose Imprecise Bayesian Continual Learning (IBCL). Upon a new task, IBCL (1) updates a knowledge base in the form of a convex hull of model parameter distributions and (2) obtains particular models to address task trade-off preferences with zero-shot. That is, IBCL does not require any additional training overhead to generate preference-addressing models from its knowledge base. We show that models obtained by IBCL have guarantees in identifying the Pareto optimal parameters. Moreover, experiments on standard image classification and NLP tasks support this guarantee. Statistically, IBCL improves average per-task accuracy by at most 23\% and peak per-task accuracy by at most 15\% with respect to the baseline methods, with steadily near-zero or positive backward transfer. Most importantly, IBCL significantly reduces the training overhead from training 1 model per preference to at most 3 models for all preferences.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a continual learning model, Imprecise Bayesian Continual Learning (IBCL), which accepts the user preference and generates the user-specific model without any training. The IBCL updates a knowledge base in the form of a convex hull of model parameter distributions. The proposed approach also ensures that the buffer growth is sublinear with the increase of tasks. The paper proposes FGCS knowledge base update and HDR computations, which, in certain constraints, help to obtain Probabilistic Pareto-optimality. The results and ablation are shown on the 20NewsGroup datasets. Also, the model requires fewer batch updates at the last task in comparison to its competitor.

### Strengths
1. The idea to generate the model without training on the fly, given the user preference, is interesting; it may have wide use for the various problems.
2. The paper provides the theoretical guarantee, but it is not clear how Pareto-optimality helps to improve the model performance. 
3. The ablations are convincing.

### Weaknesses
1. In Algorithm-1 paper shows the FGCS Knowledge Base Update, which is based on some distance, mostly selecting the samples that have maximum diversity. There are many similar works based on entropy, loss, and other metrics (please refer to [a]). The paper's use of a distance metric for distribution selection, while functional, lacks a strong justification compared to established methods utilizing entropy or loss-based criteria. The advantage of the chosen 2-Wasserstein distance, particularly in the context of continual learning, is not sufficiently highlighted, especially given its computational overhead. Furthermore, the claim of sublinear buffer growth, while a stated goal, is not convincingly superior to the fixed buffer sizes employed in many existing replay-based methods.

2. The paper is motivated as we have a large number of users, and the model is scalable for the larger number, but the results are shown only for the 5/10 task, which is small and does not align with the motivation. The experimental validation is limited in scope. The use of only 5 or 10 tasks on the 20NewsGroup dataset is insufficient to demonstrate scalability, particularly given the motivation of handling a large number of users. This discrepancy between the stated motivation and experimental setup significantly weakens the paper's claims of practical applicability. The lack of experiments with a larger number of tasks or users makes it difficult to evaluate the true potential of the proposed method.

3. The baseline papers are outdated; the recent work shows much better results even without replay samples. The selection of baselines is inadequate, with many recent and high-performing continual learning methods absent from the comparison. The inclusion of a single recent method (L2P) is insufficient to address this concern. The absence of comparisons to state-of-the-art replay-based methods, which have demonstrated superior performance, makes it difficult to assess the true effectiveness of the proposed approach. Moreover, the comparison to L2P, a replay-free method, is not a fair comparison given that IBCL uses a replay buffer.

4. The ablations are convincing, but the results are insufficient to evaluate the model. The used datasets are limited, and the training procedure is not clear. The experimental results are not comprehensive enough to fully evaluate the model's performance. The use of a single dataset (20NewsGroup) limits the generalizability of the findings. Furthermore, the training procedure is not clearly defined, lacking crucial details necessary for reproducibility. The impact of hyperparameters, beyond those explored in the ablation, is not addressed, raising concerns about the robustness of the results.

### Questions
1. In Algorithm-1 paper shows the FGCS Knowledge Base Update, which is based on some distance, mostly selecting the samples that have maximum diversity. There are many similar works based on entropy, loss, and other metrics (please refer to [b]). What advantages do they have over the other? Most of the earlier work used fixed/constant size buffers, which is better than sublinear growth. When the results are evaluated, IBCL has sublinear growth; however, the compared method GEM/A-GEM uses a fixed-size buffer. In this scenario, how do the authors ensure a fair comparison? Also, the L2P is a replay-free model, which is not a fair comparison since the model used the replay buffer. What is the buffer growth rate, and how does the performance change with the sublinear growth? 
2. The baseline papers are outdated; the recent work shows much better results even without replay samples. Please include the recent replay-based model in the baseline. Also, the L2P (is only a recent model) is a replay-free prompting-based model and there are many updated prompting-based approaches [a, c], etc. which should be included in the baseline. 
3. The motivation behind the probabilistic Pareto-optimality is not clear. Why is it important for continual learning? 
4. There are no clear descriptions about the HDR computation, i.e., how Algo-2, line-5 computes the HDR? It looks like Preference HDR Computation is expensive, and as the task grows, the complexity increases. Please discuss its computation method and complexity. 
5. The ablations are convincing, but the results are insufficient to evaluate the model. The used datasets are limited, and the training procedure is not clear. 

Reference: \
[a] CODA-Prompt: Continual Decomposed Attention-based Prompting for Rehearsal-Free Continual Learning, CVPR-2023 \
[b] Streaming LifeLong Learning With Any-Time Inference, ICRA-2023 \
[c] DualPrompt: Complementary Prompting for Rehearsal-free Continual Learning, ECCV-2022

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
This paper successfully achieves the goal of developing classification models for domain-incremental learning, considering user preferences for task trade-offs. Moreover, the learned model is efficient and guarantees Pareto-optimality. The results substantiate the claim that IBCL not only attains high performance through probabilistic Pareto optimality but also excels in the efficient, zero-shot generation of models.

### Strengths
For the current revision:

- The paper is well-written and easy to follow, with clear logic throughout. The authors have effectively used bullet points to delineate their settings and motivations, providing a lucid understanding of their objectives.
- The proposed new setting of training Pareto-optimal models under user trade-off preferences between tasks is both significant and well addressed in this context.
- The theoretical framework is self-contained, and the experimental comparisons are comprehensive.

### Weaknesses
 - The HDR concept (highlighted in purple in Fig.1) is not immediately clear. It would be more helpful to use its full name, 'high density region'. The term 'finitely generated credal set'  presents a similar issue, needing a more explicit definition.
- While the paper mentions several preference-conditioned Pareto models [1, 2] in the appendix, a more detailed explanation of how IBCL differs from these models would be beneficial.

### Questions
In the experiments, it appears that a smaller $\alpha$ value is preferable. Why not choose an even smaller $\alpha$ (e.g., 0.001)?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
They propose Imprecise Bayesian Continual Learning, and the proposed method has the two pros: (1) update the knowledge in the form of a convex of model parameters (2) it does not require additional training cost. Also, they show that models from IBCL obtain pareto optimal parameters.

### Strengths
**1 [Motivation].** I agree with the authors' claim and the philosophy of the method seems make sense for me. Especially, reducing the training overhead is very important topic in continual learning area. 

**2 [Guarantee pareto optimal].** While I'm not familiar with the mathematical analysis, the authors guarantee that model generation from IBCL has pareto optimal parameters for each task. This work seems impressive for me.

### Weaknesses
 **1 [Lack of Baselines]. ** In my opinion, the experiment evidence needs to be improved. Especially the baselines are too old and not enough to prove that the proposed method is state-of-the-art. I will propose some recent baselines as below:

**Zero-shot.** Since the proposed method argues the benefit of zeroshot, it needs to compare with the models that have zero-shot capabilities. I recommend CLIP[1] as a baseline, but if the authors think that CLIP is unfair for comparison, it is also fine to compare with traditional zero-shot learning techniques. 

** Efficient training method.** There are several continual learning papers with a few training cost. In recent, there are lots of those kinds of papers[2, 3, 4], so it would be good baselines to validate the effectiveness of proposed method. 

**Advanced Research after GEM.** In fact, there are advanced work after publishing GEM. I will share the paper[5]. Since the authors select the GEM as a baseline, it would be better to compare the method with A-GEM too. 

Lastly, I will upgrade my rating if you enhance the experiment part.

### Questions
I already wrote my concerns in weakness parts.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Imprecise Bayesian Continual Learning (ICBL) for continual learning under large number of preferences. Unlike other approaches which have to learn a model for each preference, ICBL can handle arbitrary number of preferences under limited compute by updating a knowledge base (aggregated over tasks) as a convex hull over model parameters. As only extreme point of the hull have to be stored, this can be done with lower memory requirements. Leveraging this knowledge base, preference-addressing models can be generated without training, and have guarantees w.r.t. Pareto optimal parameters.
Results on four image classification and NLP benchmarks show convincing results with effectively no negative backward transfer.

### Strengths
* To the best of my knowledge, the proposed method - ICBL - is the first to tackle the task of continual learning with a large number of preferences. 
* Its derivation and motivation appears sensible, and can account for an arbitrary number of preferences without costly retraining.

### Weaknesses
In this section, I include both issues I have with the paper, and general questions regarding my understanding of the proposed approach.

__Weaknesses__

* The paper itself is too dense - a lot of the crucial intuition and motivation is moved to the appendix, which makes the main paper very difficult to parse, for example
	* Separation and placement in literature of the proposed method IBCL and MAML/BMAML (App. A).
	* The reason for working in a bayesian CL setting (App. B)
	* The importance of the particular task similarity assumption (App. E)
	* Limited discussion on how preferences are formalized (App. G)
	* Very basic experimental details on the CL experiments (App. J)
Without continuously looking at the supplementary, understanding both key elements of the method and its motivation become in parts near impossible. This specifically refers to the reason behind bayesian CL, and details regarding the made assumptions. It would be great to see that changed.

* The proposed setup seems contrived - in particular the continual aspect, with both examples provided in the introduction primarily highlighting the multi-task nature of the problem. The continual aspect seems to be mostly a sidenote (e.g. "preference may even change over time"). Similarly, the authors only provide limited references for the relevance of the described problem scenario where a large number of preferences has to be accounted for continually over time. It would be great if the authors could offer some more clarity here.

* I may be missing something here, but the authors list poorly performing models to also be sampled from the HDRs, and require separate evaluation on a withheld validation set. This seems like a rather crucial point to elaborate on - what exactly is the rate of poorly performing models, and how dependent is ICBL on selection using validation metrics?

* The experimental studies are limited, and only compares to a single continual learning method, while not providing any context as to why GEM was selected in particular. Are other methods not suitable for this scenario? Similarly, can ICBL not be deployed on standard, single-preference continual learning benchmarks? This would be great to understand, and if not, why. 


__Questions__


* What drives the definition of the Assumption 1 for Task Similarity? In particular, how close it is to a realistic assumption (in particular F being a convex subset of \Delta_{xy})? Conceptual motivation for such a key assumption would make it easier to grasp the proposed approach quicker.

* Intuitively, it seems like the diameter of the convex subsets F (r) could connect to the expected continuous distribution shifts that can be handled. Is that right? And generally, how does the choice of r drive/change the behaviour/applicability of ICBL?

### Questions
I am currently having some trouble correctly placing the relevance of the tackled problem, alongside issues with the experiments and questions regarding the proposed approach - as listed in the above section.
I am happy to raise my score if these can be adequately addressed!

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
