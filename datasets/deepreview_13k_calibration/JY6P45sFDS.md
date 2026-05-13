# The Directionality of Optimization Trajectories in Neural Networks

- Decision: Accept
- Avg Score: 6.75
- Scores: 10, 6, 8, 3

## Abstract
The regularity or implicit bias in neural network optimization has been typically studied via the parameter norms or the landscape curvature, often overlooking the trajectory leading to these parameters. However, properties of the trajectory --- particularly its directionality --- capture critical aspects of how gradient descent navigates the landscape to converge to a solution. In this work, we introduce the notion of a Trajectory Map and derive natural complexity measures that highlight the directional characteristics of optimization trajectories. Our comprehensive analysis across vision and language modeling tasks reveals that (a) the trajectory's directionality at the macro-level saturates by the initial phase of training, wherein weight decay and momentum play a crucial but understated role; and (b) in subsequent training, trajectory directionality manifests in micro-level behaviors, such as oscillations, for which we also provide a theoretical analysis. This implies that neural optimization trajectories have, overall, a more linear form than zig-zaggy, as evident by high directional similarity, especially towards the end. To further hone this point, we show that when the trajectory direction gathers such an inertia, optimization proceeds largely unaltered even if the network is severely decapacitated (by freezing >99% of the parameters), --- thereby demonstrating the potential for significant computational and resource savings without compromising performance.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
2

### Summary
The paper presents several tools for visualizing, quantifying, and comparing neural network training trajectories. The optimization paths of neural networks are represented by a Trajectory Map (TM), which consists of the cosine similarities between parameters in checkpoint pairs of a neural network over training time. The angle between adjacent samples of the trajectory is also evaluated. Theoretically, this angle is found to be bounded by the Hessian eigenvalues so that in most training settings it is either obtuse (negative cosine) or orthogonal (0 cosine). Unlike parameter distances, the angular similarity of parameters with their initializations are also found to reduce as models get larger - a result which is used to predict relative performance between models. Finally, the "decapitation hypothesis" is introduced with supporting empirical evidence, which hypothesizes that the majority of parameters can be frozen without impacting performance, once a network's training trajectory becomes fixed in cosine similarity relative to the initialization.

### Strengths
Originality: the paper neatly ties together several previous works related to phases and trajectories of optimization. Although some of the findings confirm results from other work (e.g. larger networks are closer to initialization), other findings are novel and surprising (e.g. momentum and weight decay increasing rather than decreasing variability in the optimization paths).

Quality: the paper is overall very thorough and addresses almost all of the pertinent concerns that a reader may raise (see Weaknesses for issues). Although the decapitation hypothesis is not very well elaborated on, this is fine since the paper already covers a large amount of ground.

Clarity: the paper is very clearly laid out and neatly presented, with helpful color choices to enhance the figures and accompanying text. The writing has a succinct, engaging style, and is enjoyable to read. Having said that, there is some excess complexity in some sentence structures (e.g. contribution 1) and vocabulary choices (e.g. "epochly") which are difficult to understand.

Significance: the paper gives a nice disambiguation between distance travelled in parameter space during training, versus the straightness of the trajectory. The proposed measure of directionality in section 5 seems to be a useful metric for model capacity and training progress. Finally, the decapitation hypothesis does open up a lot of possible methodological work in the future, and potentially a new perspective on existing empirical methods for reducing training costs (e.g. LoRA).

### Weaknesses
Appendix C is important in that it looks at the baseline where the trajectory is a random walk, since naturally one would expect trajectories to become more similar over time due to learning rate decay and having travelled further from the origin. In general, it would be more informative if *all similarity values, including in the main text* were reported as increases/decreases over the random walk baseline (with decaying step size), and plots showed such relative differences instead of absolute similarities. Specifically:
- It is not obvious from figures 9-10 how much added similarity/dissimilarity is in training trajectories versus random walks - for instance, is the random walk with decay more dissimilar than training trajectories at all points in time, or do they invert in order of similarity at some point?
- What is the non-relative TM for random walks (to compare with figure 2)?
- Similiarly, what are the expected MDSs of random walks for a given step size schedule?
- Are real (empirically determined) step sizes used to derive/simulate the random walk TMs in figure 9? This seems to be the fairest method, and thus it would also be necessary to consider all combinations of momentum/weight decay and their effect on step size.

The per-epoch sampling has an unclear interaction with the analyses of adjacent steps (i.e. figure 4), because the choice of how often to sample the network could change the measured results. For example, it could be that no momentum/no weight decay actually has larger angles when measured between successive iterations, but the sum of such steps over the epochs results in smaller angles. For the sake of thoroughness, it would be nice to know how results such as figure 4a depend on the sampling rate.

### Questions
On a related note to the aforementioned weakness, neural networks are known to be much less stable during the early training period. What does the TM and angles between adjacent samples look like when sampled at a higher frequency in the first few epochs (e.g. every iteration of epoch 1)?

How much of the observations related to phases of training (figure 2 left, figure 4) are due to discontinuities in the learning rate schedule? For instance, what if a linear decay or cosine annealing schedule is used instead?

There is a similarity between the TM and notions of representational similarity which also consider distances and angles among the cosine similarities of activations (e.g. [1] Lange et al. 2023) . Could the authors discuss if either the methods of representational similarity could be applied to TM, or if there is an empirical or theoretical connection between a network's trajectory in parameter space vs representation space?

[1] Lange, R. D., Kwok, D., Matelsky, J. K., Wang, X., Rolnick, D., & Kording, K. (2023, September). Deep Networks as Paths on the Manifold of Neural Representations. In Topological, Algebraic and Geometric Learning Workshops 2023 (pp. 102-133). PMLR.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel approach to understanding neural network training trajectories by examining their directionality, particularly through the concept of a "TM: Trajectory Map." This approach sheds light on the consistency and detailed behaviors of optimization paths throughout training. The authors propose that once directional movement saturates, the model’s capacity can be effectively reduced ("decapacitation"), potentially improving computational efficiency. The study presents evidence of directional redundancy within optimization trajectories across both image classification tasks and large language models.

### Strengths
- Novelty: The Trajectory Map provides a fresh perspective on neural network training by visualizing and quantifying directional movement, potentially contributing to the development of more efficient training techniques.
- Empirical Validation: Experiments span multiple architectures and hyperparameter configurations, supporting the proposed approach.
Applicability to Efficiency: The concept of "decapacitation," where computation resources can be reduced once directionality saturates, is promising for the design of more resource-efficient training strategies.

### Weaknesses
 - Dependency on Specific Configurations: The initial results for ResNet50 appear heavily dependent on a specific learning rate decay schedule. It remains unclear whether author's findings can be replicated across different learning rate schedules (e.g., constant, cosine decay), suggesting additional experiments would be valuable to verify generalizability. Specifically, the observed saturation of directional movement might be an artifact of the step-wise decay, where sudden drops in learning rate could artificially constrain the optimization path. The study should investigate whether smoother learning rate schedules, such as cosine annealing, exhibit similar directional saturation or if the trajectory maps show fundamentally different patterns.
- Correlation Between MDS and Performance: The proposed Mean Directional Similarity (MDS) metric lacks clear quantitative correlation with test accuracy or loss, which weakens the evidence of its effectiveness. While the authors claim that MDS captures directional redundancy, it is not clear how this redundancy directly translates to improved or degraded performance. A more rigorous analysis, perhaps involving statistical correlation tests and visualization of MDS against performance metrics, is needed to establish a convincing link. The current analysis does not provide sufficient evidence that MDS is a reliable predictor of model performance.
- See questions section.

- Missing Figure References: Figures referenced on lines L1090, L1120, and L1126 are absent.

### Questions
- Details on Accuracy and Loss: Could specific values for train loss, test loss, and accuracy be provided for each experiment?
- Correlation Between Mean Directional Similarity (MDS) and Performance: What is the observed correlation between MDS and test accuracy or loss? Detailing this would clarify the effectiveness of MDS as a performance predictor.
- Learning Rate Schedule Diversity: In the appendix, including a comparison of Trajectory Maps under different learning rate schedules (e.g., constant, cosine decay, step decay) would be beneficial, as the results suggest that Trajectory Maps may vary depending on the schedule used.

#### Comments
- Missing Figure References: Figures referenced on lines L1090, L1120, and L1126 are absent.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper flattens the neural network parameters into a vector, then analyzes the evolution of that vector over the course of training. They show across a few architectures and domains that there is large directional stability, affected by hyperparameter choices. They also note that such stability can be leveraged to finetune fewer parameters, in keeping with prior literature.

### Strengths
- The choice of quantity to analyze is quite simple, and it's nice to have a fleshed out analysis of such a quantity
- It was a good idea to include the analysis of an additional domain (Pythia) so as to make the arguments firmer beyond the overparametrized setting (can get training accuracy to 0) that happens in image classification

### Weaknesses
## Overall

1. I think the motivation for why to study this quantity in the introduction is a bit sparse. As someone who works in the field I think this is an interesting quantity to look at, but I think a reader from elsewhere may not feel similarly and the paper does not make that easier. For a work on a similar topic that I think makes a better case, see https://arxiv.org/abs/2106.16004
2. We as a field obviously don't have a complete understanding of NN optimization, so I think it's a bit unfair to judge this work by saying "it's not clear why this analysis connects to things we care about" as it might be useful in the future, or for correlating with other observations, still I think the paper could make a better attempt to connect to many existing works on the topic to further the scientific dialogue. I'll try to detail this below.
3. I think the experiments could use a few more hyperparameter settings, it's a bit difficult to make claims about the importance or role of hyperparameters like momentum or weight decay with only two settings (and no sense of how they connect to performance, see next point).
4. In a paper ostensibly introducing itself about the loss landscape, it was a bit frustrating not to find a single loss curve. If the network fails to fit the loss, then that discussion should occur in concert with increased directional stability. I think it's difficult to understand these things in isolation and I wish the paper made it easier to do so.

## Specific

### Section 1
1. Implicit bias should be defined in the introduction, at least in a short sentence.
2. The introduction to the motivating question feels very fragmented.
3. "Benefits of the Trajectory View..." - I think it would be helpful to explicitly contrast this with prior metrics others have considered to make the case stronger.
4. "Decapacitation Hypothesis" - I think this is an odd name, it would imply to me that networks lose capacity, but the actual results later in the paper suggest that networks have sufficiently learned the important features such that you don't need every parameter any more, not that you never needed every parameter. Also I believe that without a discussion of prior work on this topic, giving this a new name is not good hygiene. See https://arxiv.org/abs/2312.11420

### Section 2
1. I think the motivation for why to flatten the parameters is not very clear. Especially as prior work like muP has explicitly noticed different evolution for different parameters (e.g. bias vs. matrix) given the structure of the network, it would be nice to make an explicit argument contrasting with existing work why this is a good idea. It would also be useful to discuss linear interpolation works like https://arxiv.org/abs/2106.16004 and many works cited in that paper to bolster the case.

### Section 3
1. "epochly" -> intermediate?
2. I feel that convergence in direction should probably be considered as convergence given that CE loss can never be minimized because of the exponential.
3. Training loss curves for Fig 2 + 3 are missing: is directional similarity mostly a result of the model failing to learn well at all?
4. Directional movement saturates exactly when learning rate is decayed, so it'd be nice to have a hyperparameter setting without this additional confounding factor...
5. It might be nice to rescale the trajectory maps to be on separate color scales. For example in the case with no weight decay, the increased similarity could be due to the fact that WD removes superfluous weights, but without a lot of the initialization sticks around that isn't used much for the actual prediction task. This effect could drown out any signal in the trajectory map.

### Section 4
1. The "Initial Thoughts" are confounded by the lack of training loss to correlate with the plots. It could be that the model is stuck at a local minimum.
2. Certainly in Fig. 4 the updates are oscillating, but this might be expected for (relatively) small batch sizes as the examples are likely very different. It would be interesting to know how the overall gradient oscillates.
3. In 4.2 it's very unclear to me why this is the right model to consider for NN as so much is simplified here. Certainly the stable Hessian assumption seems unfounded in the early stage of training given the trajectory differences shown in this work, without a measurement that it's stable... It's fine to try to simplify to basics but I think the presentation should be amended.
4. Also as far as I understand, EoS is for gradient descent, while here we look at practical SGD, this seems like a huge difference no?
5. Would be good to discuss related work in this section on linear interpolation, see previous links.

### Section 5
1. "Directional measures predict..." feels really too strong a claim for the existing evidence. I would want to see performance for many different hyperparameter choices vs. the apex angle. Besides there is already work on practical generalization measures (https://arxiv.org/abs/1912.02178) and it would be nice to talk about how the stronger ones there connect.

### Section 6
1. There is already work on tuning just normalization layers in the finetuning setting (https://arxiv.org/abs/2312.11420) that should be referenced and discussed here. I also don't love the naming of this phenomenon as I feel it could be stated simply as what you did.
2. It would be nice to have experiments on Pythia here as well.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper introduces the concept of the trajectory map to study the dynamics of neural network training. Specifically, the trajectory map is a matrix where each element in $i$-th row and $j$-th column represents the cosine similarity between the model parameters at $i$-th iteration and the model parameters at $j$-th iteration.
Through visualization and quantitative analysis, the study uncovers patterns such as directional redundancy as reflected in the trajectory map. Additionally, the empirical influence of momentum and weight decay on the trajectory map is verified. Finally, the paper suggests utilizing directional redundancy to enhance the efficiency of neural network training.

### Strengths
(1) This work provides a relatively thorough validation of the proposed trajectory map concept, specifically for analyzing the training trajectory. The concept of the trajectory map is new and transforms extremely high-dimensional information into a more manageable and trackable form, making it suitable for visualization and enabling the meaningful application of statistical tools for further insights.

(2) The identified observations and corresponding patterns may offer valuable insights into the dynamics of neural network training, potentially revealing useful information about the optimization process and the network’s behavior during different phases of training.

### Weaknesses
 (1) The introduction of customized properties in this work leads to findings relevant within those tailored domains. This work introduces new aspects of neural network training but does not build strong connections with the existing understanding of the optimization of neural networks. Thus, the new definitions and results in this work are less useful in motivating the development of new optimization methods or helping understand current optimization methods.

(2) The primary finding of directional redundancy is questionable. First, projecting high-dimensional information into lower-dimensional space may result in significant information loss, meaning that redundancy observed in low-dimensional representations may not necessarily imply that iterations during the later stages of training are redundant or unnecessary. Thus, the leveraging of directional redundancy (in section 6) lacks concrete theoretical support and sufficient assessment.

(3) Section 6 offers a relatively weak argument for the practical application of directional redundancy, specifically the claim that "once directional saturation is achieved, the full capacity of a network might no longer be required for further training." While the image on the right side of Figure 8 presents straightforward patterns, these patterns do not clearly align with the left side of the figure, and they seem more contingent on the percentage of iterations

### Questions
(1) What are the shared and outlined observations between Figure 2 and Figure 6? Despite the influence introduced by the learning rate schedule in Figure 6, for points along the diagonal, the cosine similarity exhibits a monotonically decreasing trend in both the horizontal and vertical directions, generally declining from 1 to 0 as observed from the upper-left point of the diagonal. While this observation is straightforward but introduces nothing new.

(2) Line383 to line388 and corresponding Figure 7. 

(2.A) I believe that the observed trends are linked to variations in model size rather than performance across different metrics.
(2.B) However, I am unclear on the significance of this comparison beyond the linear relationship between the apex angle and model size. Could you elaborate further on the insights provided by Figure 7.a in this regard?
Furthermore, Figures 7.b and 7.c "fail to capture the expected monotonic trend," but the implications of this "failure" are unclear, other than that these metrics cannot be used as reliable predictors for model size.

(3) The experiments with large language models (LLMs) in Section 5 utilize Adam as the optimizer instead of SGD. Could you provide further insights on how the choice of different optimizers, such as Adam versus SGD, influences the training process and outcomes, particularly in relation to the dynamics of adaptive learning?

(4) Section 5 key takeaways (line398 - line402). 

(4.A) What does the complexity measure refer to in this context? Is it related to the complexity of the neural loss landscapes, the architecture of the model, or something else? Could you clarify how this measure is utilized to assess the optimization process?
(4.B) While I agree that the complexity metric reveals a correlation with model size, claims regarding other correlations seem unsupported or underexplored in the current analysis.

### Soundness
2

### Presentation
3

### Contribution
2
