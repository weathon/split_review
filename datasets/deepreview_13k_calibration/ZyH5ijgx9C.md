# Efficient Stagewise Pretraining via Progressive Subnetworks

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Recent developments in large language models have sparked interest in efficient pretraining methods. Stagewise training approaches to improve efficiency, like gradual stacking and layer dropping \citep{reddi2023efficient, zhang2020accelerating}, have recently garnered attention. 
The prevailing view suggests that stagewise \emph{dropping} strategies, such as layer dropping, are ineffective, especially when compared to stacking-based approaches. This paper challenges this notion by demonstrating that, with proper design, dropping strategies can be competitive, if not better, than stacking methods. 
Specifically, we develop a principled stagewise training framework, \emph{progressive {\layerdrop} training}, which only trains subnetworks within the model and progressively increases the size of subnetworks during training, until it trains the full network. We propose an instantiation of this framework --- \textbf{Ra}ndom \textbf{P}art \textbf{Tr}aining ({\method}) --- that selects and trains only a random subnetwork (e.g. depth-wise, width-wise) of the network at each step, progressively {\em increasing} the size in stages. We show that this approach not only generalizes prior works like layer dropping but also fixes their key issues. Furthermore, we establish a theoretical basis for such approaches and provide justification for (a) {\em increasing} complexity of subnetworks in stages, conceptually diverging from prior works on layer dropping, and (b) {\em stability} in loss across stage transitions in presence of key modern architecture components like residual connections and layer norms. Through comprehensive experiments, we demonstrate that {\method} can significantly speed up training of standard benchmarks like BERT and UL2, up to 33\% compared to standard training and, surprisingly, also shows better downstream performance on UL2, improving QA tasks and SuperGLUE by 1.5\%; thereby, providing evidence of better inductive bias.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a framework to train an increasingly larger subset of layers of an LLM with a manual schedule of layer dropout with the motivation of using less compute to obtain the same pretraining performance. This work shows computational saving and a slight boost in downstream performance of BERT and UL2 pretraining.

### Strengths
RAPTR is a simple and effective method for training progressively larger networks and saving compute. It's also interesting that layer dropout as a form of regularization can improve stability and even downstream performance.

### Weaknesses
BERT baselines seem strong but it's unclear how competitive the UL2 baselines are. The soundness of baseline might be important to show as weak baselines can make any results possible. A reference on these hyperparameters would be helpful.

One unsatisfying aspect of this work is that it does not analyze how the compute-efficient frontier changes with this pretraining procedure. Model sweep would also help quantify the amount of improvement in downstream performance as we can see an overall trend more clearly.

### Questions
.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new stagewise training approach called "progressive subnetwork training" for efficiently pretraining large language models. It introduces an instantiation called Random Path Training (RAPTR) which trains random subsets/paths of layers in the network, progressively increasing the path length over stages. Experiments on BERT and UL2 models show RAPTR can match or improve baseline pretraining loss with 20-33% fewer FLOPs. RAPTR shows improved downstream task performance on UL2, gaining 1-5% on QA/GLUE over baseline and stacking methods.

### Strengths
- The paper is well-written and clearly presented; 
- The paper proposes a novel and intuitive stagewise training paradigm with theoretical motivation and it achieves strong empirical gains over baseline and stacking methods, especially for short training regimes.
- The paper provides theoretical analysis on stability of subnetwork training in residual networks and the algorithm is simple to implement on top of standard training. Detailed ablations regarding the fixed layer and scale have also been presented;

### Weaknesses
 - Theoretical results are good while limited to simplified linear residual network settings.
- The gains in pretraining flops diminish in the asymptotic long training setting. 
- Downstream task improvements lack sufficient analysis on why RAPTR has implicit biases on different tasks, for example, it seems to hurt the multilingual QA performance when adding the 30k. 
- Besides the flops, the real wall-clock time might also be good to provide, given in some cases, flops disagree with wall-clock time for efficiency measurements [1]; 
- Besides different architecture and objectives (BERT/UL2), whether the proposed method scales with model sizes and fit to LM is unknown; 

### Questions
- Could the author elaborate on the real wall-clock time gain with the pretraining experiments; 
- Could the authors explain more on the varied performance gain in Table 3;  
- Besides the ppl comparison for the ablation studies regarding the fixed layer and scale, could the author also provide the detailed downstream performance to show if the design choice affects both pretraning and downstream;

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to pre-train transformers efficiently and proposes a pre-training framework Random Path Training (RAPTR). The main idea of RAPTR is to train random sub-layers of the transformer and progressively increase the number of layers in stages. To further stabilize the training, the authors propose several techniques e.g. scaling the intermediate outputs and fixing the first and last layers. The authors also show the theoretical support for the training stability of RAPTR. Experiments on BERT and UL2 language model pre-training demonstrated the effectiveness of the proposed method. Compared with baselines like progressive stacking and layer-drop, RAPTR achieves lower perplexity under the same computation costs.

### Strengths
- The theoretical analysis and experimental results provide useful insights for pre-training large models.
- The proposed method is simple and effective and can be adapted to many deep neural networks.
- The paper is clearly written and easy to follow.

### Weaknesses
 - The idea of training sub-layers progressively is not novel, which is similar to [1][2].
- RAPTR introduces many hyper-parameters and it would be difficult to tune these hyper-parameters in the pre-training setup, which would hinder the application of this type of work.

### Questions
- How to determine the hyper-parameters of RAPTR, e.g. the number of stages and the training steps in each stage? Does it affect the learning rate schedule? Is it affected by the model scale?
- What is the training setup of baselines and the proposed method in Table 2?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article proposes a new form of stagewise training, called Random Path Training (RAPTR). Rather than increasing the number of layers trained by stacking them like in Progressive or Gradual Stacking, the authors propose to sample a subnetwork of the full network during training randomly and progressively increase the subnetwork size (while scaling outputs appropriately), which allows evaluation during training.
They show empirical improvement for the same FLOPS over other stagewise training techniques, as well as a theoretical study of the change of the losses when changing stages.

[Edit: following my comment, I am increasing my note from a 3 to a 5 for the various improvements and clarifications provided by the authors, and may increase further to a 6 following discussions with the other reviewers.]

### Strengths
The article presents a simple and effective stagewise training paradigm, by using layer dropping in the start of training. 
The experiments are clear and show the effectiveness of the method for a given FLOPs budget. 
The new proposed rescaling of the outputs seems sound and improves the results.
The theoretical analysis of the stability of the network seems interesting.

### Weaknesses
**Improvement** The experimental results do not show a consistent improvement of the method over the other stacking methods. Table 1 and 2 show very limited improvement in some cases, for the same value of FLOPs; for schedules that have been chosen by unclear means. Specifically, while RaPTr demonstrates some gains in Table 3 on Tydi QA and SQuADv2, the improvements on other metrics like TriviaQA and SuperGLUE are marginal or non-existent. This inconsistency raises concerns about the general applicability of RaPTr across different tasks and metrics. Furthermore, the alternative schedule used in Table 3, which reportedly shows a small variance, is not detailed, making it difficult to assess its impact and compare it with the standard RaPTr schedule.

The results in Table 3 are also surprising. RaPTr does show an improvement on Tydi QA and SQuADv2 other Stacking, but not for the other metrics. The alternative schedule is not detailed and merits more introduction. It is impossible to compare Stacking with RaPTras as long as Stacking has not been trained with this alternative schedule, or a similar one. (This could be done by training the entire model with 30K steps, then training only the first layers, and restacking the previously trained layers to extend the model, rather than stacking the same layer). Otherwise, the improvement due to RaPTr seems relatively small without this schedule. The small variance claimed by the authors is only proven with the alternative schedule and not RaPTr in general. 

**Notations** All along the article, the notations of the schedule of RaPTr are very inconsistent and unclear.
The schedule $T^{1:k} × (p^{1:k}, I^{1:k})$ is never used after its definition if I'm not mistaken. This is logical as it is often useless: $I$ is denoted to be the entire set during all of the experiments, and the stage times are always equal. Only $p$ ever changes during the experiments. Similarly,  The sense of $I$ reverses during the paper. At first, it defines the set of fixed layers before seemingly being reversed during the experiments as $I$ is the entire set $(1,24)$ (which is also not consistent with the claim that the first and last layers are always fixed). $I_s$ in Algorithm 1. is not defined and just seems to be $I$. 

**Schedule** The way schedules are chosen is never clear. In the experiments, the whole set of layers is used for $I$ with equal the same number of steps in every stage. Why is only $p$ varying? In Table 2, the stages are defined as 6-8-10-12 for RaPTr and 6-9-12 for stacking for BERT-base, and then once again equal for BERT-Large. Why were they different at first?

**Section 4.2** is extremely unclear. The normalization is very dependent on the initialization, however, the choice of initialization is never discussed. Similarly, the experimental values during training compared to initialization are not discussed. What we are supposed to conclude from Lemma 4.3. is not clear at all. In particular, the link between Section 4.2. and the experimental results in Table 2. are unclear. The goodness of fit of Fig 2.b seems pretty low. The sentence "$\Psi^l$ increases slowly with $l$" is surprising considering that the value decreases until $l=21$. Many claims do not seem to make sense or are never explained: "suggesting a worse-case bound of $O(L^{−0.88})$" ? What does "A simple calculation shows that the gap between a $L−1$ random subnetwork and the full model scales as $O(L^−c)$ for some c ≥ 0.5" mean?

**Novelty** The technique proposed is very close to other layer-dropping techniques, in particular of Zhang et al. 2019, which also aims at reducing the FLOPs needed for the training. The main difference is that the dropping is done at the start of training rather than the end, and the different rescaling.

**Figures** The Figures either bring very limited information or are very hard to read. Figure 1 could have been substituted by a simple Table. Figure 2 is never referred to anywhere. Figure 3 is extremely hard to read and never really explained well.

### Questions
"The intuition is that since the first and last layers play different roles": This seems logical. This does ask the question of whether not only the first and last but $k$ first or/and $k$ lasts layers may need to be fixed. Are the early or later layers more important to be fixed?

I don't really understand why the experiments on BERT are qualified as "short horizon settings".

*Errors or remarks:*

* Introduction: "Gradual stacking (Gong et al., 2019) and Progressive stacking (Reddi et al., 2023)", the order is reversed, it should be Progressive for Gong et al. and Gradual for Reddi et al.

* Sec 2: "the computed based"

* Figure 1.b. "for fixed set" -> "for the fixed set" 

* Table 2 is quite unclear. The values displayed are not defined clearly (losses?). "lower better loss" means nothing. "Layerdrop" is not defined anywhere in the article. If it is meant to represent the paper method, it is concerning that it uses a name that is already of another method.

* Table 3: Equiflop is not defined.

* Sec 4. "L-RaPTr" was not defined until now.

* "table" and "appendix" should be in upper case. Replace "fig" by "Figure".

* Sec 4.2 The norm is not defined. Vector/Matrix norm?

* Why is Section 4.2 referred several times inside Section 4.2??

* "O(L≥0.88)" means nothing.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
