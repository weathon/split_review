# Early Period of Training Impacts Adaptation for Out-of-Distribution Generalization: An Empirical Study

- Decision: Reject
- Scores: 6, 5, 3, 5, 6

## Abstract
Prior research shows that differences in the early period of neural network training significantly impact the performance of in-distribution (ID) data of tasks. Yet, the implications of early learning dynamics on out-of-distribution (OOD) generalization remain poorly understood, primarily due to the complexities and limitations of existing analytical techniques. In this work, we investigate the relationship between learning dynamics, OOD generalization under covariate shift and the early period of neural network training. We utilize the trace of Fisher Information and sharpness, focusing on gradual unfreezing (i.e., progressively unfreezing parameters during training) as our methodology for investigation. Through a series of empirical experiments, we show that 1) changing the number of trainable parameters during the early period of training via gradual unfreezing can significantly improve OOD results; 2) the trace of Fisher Information and sharpness can be used as indicators for the removal of gradual unfreezing during the early period of training for better OOD generalization. Our experiments on both image and text data show that the early period of training is a general phenomenon that can provide Pareto improvements in ID and OOD performance with minimal complexity. Our work represents a first step towards understanding how early learning dynamics affect neural network OOD generalization under covariate shift and suggests a new avenue to improve and study this problem.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work investigates the impact of interventions by weight freezing during early stage of training on out of distribution generalization and reports empirical evidence on 3 different OOD tasks based on covariate shift using image and language data.
They further hypothesize that using Fisher information and sharpness measures one can detect learning dynamic phase changes to leverage this phenomenon as an effective learning algorithm.
Their analysis and results provides some evidence of the. usefulness of the proposed algorithm.

### Strengths
- The Discovery of the early learning dynamics and its impact on OOD generalization is an interesting finding, and the empirical evaluations seem to show that they indeed exist.
- The evaluations are done across various tasks from images and language, and via different datasets which provides generality to the observed results.
- Both FI and sharpness are well-studied topics which have been connected to generalization from both theoretical and empirical standpoints, hence, well suited for the development of the proposed method to improve OOD generalization.

### Weaknesses
The proposed algorithm to improve OOD generalization is --as it is also mentioned by the authors-- heuristic and does not provide deeper understanding of how these changes in learning dynamics occur or is connected to generalization, beyond what has been discovered already in the literature. The gains from the algorithm that are presented in tables 1 and 2 also seem to be marginal, and it is unclear how well they perform compared to SoTA OOD, as no real baseline has been used in this work to demonstrate how the proposed algorithm compares to latest advances in OOD generalization. Furthermore, results are provided only partially, and it is unclear how the proposed algorithm performs on domain adaptation tasks. Specifically, while the paper mentions using sharpness and Fisher Information, it does not fully articulate the precise mechanism by which freezing weights during early training stages influences these metrics and subsequently impacts OOD generalization. A more rigorous analysis connecting the observed changes in sharpness and Fisher Information to specific theoretical aspects of OOD generalization would strengthen the paper's core arguments. Additionally, the reported improvements in Tables 1 and 2 are relatively small. Without a comparison to established OOD generalization methods, it is difficult to assess the practical significance of these gains. The lack of a comprehensive evaluation on a wider range of domain adaptation tasks further limits the ability to fully evaluate the proposed algorithm's effectiveness and generalizability.

### Questions
see the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates how gradual unfreezing the parameters during the early training stage affects OOD performances, and empirically unveils that gradual unfreezing leads to a time-sensitive trade-off between OOD and ID performance. The authors provide an explanation of the role of gradual unfreezing on OOD generalization: gradual unfreezing could help better to align early mini-batch gradients to the full-batch gradient, thus preventing potential overfitting to the mini-batches and eliminating spurious features. Moreover, they find that gradual unfreezing increases the sharpness and Fisher Information of the model parameters. The authors also propose a heuristic algorithm to find the best training step to start gradual unfreezing, gaining some empirical improvements on OOD tasks.

### Strengths
1. The finding of the significant impact of the early stage training on OOD performances is novel.
2. The experimental results include comprehensive OOD tasks for both vision and language domains.
3. The empirical finding that low sharpness doesn't necessarily improve OOD generalization in Figure 5 is meaningful, challenging the common belief that flat loss landscapes could benefit generalization.

### Weaknesses
1. The rationale for using sharpness as an indicator of the timing to start GU is not entirely clear. While the paper demonstrates that sharpness changes during training, it does not fully establish why starting GU at the end of a dramatic change in sharpness would necessarily lead to improved OOD performance. Specifically, the connection between sharpness, a local property of the loss landscape, and OOD generalization, a global property, needs further elaboration. The hypothesis that sharpness can reflect OOD performance is not adequately justified, and using it as a sole indicator for initiating GU seems premature without a more robust theoretical or empirical basis.

2. Section 6.2, which attempts to validate claim 2) of the hypothesis, is insufficient. The current analysis lacks a clear correlation between changes in sharpness and OOD performance across different training steps. To strengthen this claim, it would be beneficial to visualize both the "sharpness-training step" curve and the "OOD acc-GU start step" curve on the same graph for all tasks and models. This would allow for a more direct comparison and a clearer demonstration of the relationship between sharpness changes and the optimal interval to start GU. The reliance on the simple MNIST experiment in line 440, while illustrative, does not provide sufficient evidence to support the general claim that starting GU at the end of a sharp change in sharpness is always optimal.

3. The presentation of results in Tables 1 and 2 could be improved. Reporting only the winning rate, without providing the concrete numerical improvements, diminishes the persuasiveness of the findings. Including the absolute performance gains would offer a more comprehensive and convincing picture of the benefits of the proposed method.

### Questions
Is the proposed heuristic method computationally expensive? (Because you need to train an extra time and calculate the relevant metric)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors investigate whether gradual increase of the parameters in a neural network during early training helps with boosting OOD performance. To this end, the authors propose simple strategy of gradually training more parameters in a network, starting with the earlier layers and blocks until the full model is trained. This introduces a parameter, $k$, which determines the #steps until the next block in unfrozen. ID and OOD performance is tracked with this strategy on a variety of language and vision datasets under different distribution shifts. With an optimal $k$, the authors show boost in OOD performance. In the second half of the paper, the authors discuss how $k$ can be optimally chosen based on Fisher Information or sharpness, and results are presented under this heuristic.

### Strengths
The paper is generally easy to follow. The problem setup is clear, the proposed method conceptually simple to implement. A variety of datasets are included in the study. The results show possibilities to increased OOD performance on these datasets with the right gradual unfreezing schedule.

### Weaknesses
### Summary

The paper has two big issues:

First, the flow of writing: The first half of the paper addresses a possibility to increase the OOD performance depending on optimal selection of the unfreezing schedule, with little control experiments. These results appear strong. The second half of the paper then discusses how to select the unfreezing schedule, which sets the results much more in perspective. A better way, in my opinions, would be to upfront show the final method and its empirical performance: what is the proposed selection scheme for $k$, and what is the resulting performance on ID and OOD test cases across dataset and models?

Second, missing controls and baselines. The paper claims to contribute to the “understanding” of early training dynamics, but really only shows one special case of addressing this problem. The authors claim previous methods focus on ID performance and failed to address OOD improvements, but none of the methods were implemented and ran as baselines. The unfreezing schedule is also not well motivated and arbitrarily presented. What about randomly unfreezing? What about doing this not per block, but truly randomly across network parameters? What about unfreezing top to bottom? How do the methods stack up against established strategies of 

I feel like addressing any subset of these questions would greatly enhance readability, quality of investigation, and impact of the paper. Please find an additional list of weaknesses to address below (if possible, please ref their labels W1,... etc) during the rebuttal:

### Major Weaknesses

**W1.** The results presented in Figure 2 and 3 are interesting, but not sufficient to back up the authors’ claims about improvement of OOD performance. Namely, all metrics are reported directly on the test sets, which in practice are not observable, and this is not appropriately discussed in the paper. It is unclear how the optimal k in Fig. 2 and 3 would be chosen. In a typical experiments, it would be selected based on ID validation performance, and for quite a few of the presented settings, this would result in much smaller gains (or even decrease in performance).

**W2.** it is good that experiments were run across multiple seeds, but the authors should reflect these in the plots and update all plots with appropriate error bars (e.g. SEM or 95% CIs), e.g. in Fig. 2-4, and also in Fig. 5. In the tables, the WR should also be equipped with error bars.

**W3.** Is it actually required to unfreeze the model step by step? There are little controls against this proposal. What happens if blocks are unfrozen randomly? Or from last to first layer, instead vice-versa? More control experiments here would strengthen the claims made.

**W4.** The authors cite other strategies for adapting early changes to network training for improved ID performance. How do these strategies stack up against the proposed method for OOD improvements? Adding some of these comparisons would strengthen the proposed method.

**W5.** Section 3.1 is not well written. Not all variables and symbols are defined (e.g. P_w in Eq. (1)), and some of the sentences are broken. There are also multiple statements about the Fisher matrix, like “A larger Fisher information…”, “tr(F) correlates well with the full Fisher information…” which are all imprecise given that F is a matrix. I would suggest to rewrite 3.1 to improve clarity.

**W6.** The study is limited in the number of models that are investigated. It would corroborate the paper story if the findings could be demonstrated for a larger set of model architectures.

**W7.** Significance: The performance improvements in Table 1 are really slim, except for MNIST. On CIFAR, we get 72.36 vs. 73.56 and 45.10 vs. 45.82%. It would really help to contextualise this against other ways of making model training more robust. What happens when models are trained with robust pre-training techniques? Here, improvements are typically much bigger than 1-2% points.

### Questions
**Q1** In the conclusion, you claim that the paper contributes to a deeper understanding of the early period of training. Could you clarify what this understanding entails? It is unclear from how I read the paper. What does the empirical performance tells us about what happens during the early training phase within the network?

**Q2** After designing the final method, it would be interesting to apply it to larger scale, real-world applications cases (without much tuning). For instance, how does the method perform for increasing robustness on a dataset like ImageNet-C or ImageNet-R?

**Q3** The title references “adaptation”, but this is not part of the investigation. Could you clarify?

### Soundness
2

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
This paper studies the early learning dynamics of OOD generalization under covariate shift. The authors leveraged gradual unfreezing (i.e. gradually unfreeze blocks of parameters during training) as a tool and observed that OOD generalization can be improved if gradual unfreezing is applied at the beginning of training. In addition, they also observe a general trade-off between ID and OOD performance when varying the time interval of unfreezing. They further use Fisher information and loss sharpness as proxies to design heuristics that allow for capturing the optimal time interval of gradual unfreezing.

### Strengths
1. The paper is clear and easy to follow.
2. The experiments span various datasets and training setups.
3. The study of covariate shift early training dynamics, to the reviewer's knowledge, is new.

### Weaknesses
1. Lack of explanation on why the approach should work: while the reviewer acknowledges that (from its title) this paper is an empirical study, they found it hard to evaluate the value of findings in the paper without more explanation or intuition, especially the author proposes a heuristics-driven approach to improve OOD.
    1. explanation of gradual unfreezing: while the author provided intuition on page 6 about why gradual unfreezing would work, the reviewer found it not convincing: most of the experiments in Kumar et al. [1], if the reviewer remembers correctly, train linear probe then fine-tuning till convergence, but this paper considers early-training with small amount of training steps. In addition, Kumar et al. [1] consider transferring from a pre-trained model (that’s why the feature can be distorted). In contrast, in this paper, the authors train from scratch for part of the experiments. It is hard to imagine the benefits of first aligning the classification head (or top layers) while keeping the bottom layers (feature extractor) randomly fixed. 
    2. On phases of the change of the metrics: Besides, the dynamics of metrics in Figure 5 are very different, where in some cases they are decreasing but in other cases they are increasing. 
2. Related works: the reviewer found it slightly over-claimed to say that ‘the impact of the early learning period on OOD generalization remains unexplored’ throughout the paper. How the (early) learning dynamics influence the OOD generalization has been widely explored in spurious correlation, which is another major OOD generalization problem. It would be better if the authors could discuss the connection to these related works and rephrase their claims in the paper. Some examples are [2][3].
3. Robustness of the proposed heuristics: how the proposed heuristics would be able to transfer to real-world dataset is unknown. While the authors conduct experiments on multiple datasets, it is still hard to evaluate because of the lack of explanations of some components in this work (see 1.)
4. Ablation study: while we see that in Figures 2 and 3 there exists a sweet spot where ID performance remains stable while OOD performance improves, all the runs use gradual unfreezing at the beginning. A helpful ablation study shows that gradual unfreezing at the middle period or ending period of training does not exhibit this observation. That is, starting training the whole network for some epochs and then freeze all parameters and gradually unfreeze.

### Questions
Please see the above ‘weakness’ section and provide clarification if needed.

Other questions are: 

1. In Figure 5, why the k used in different subfigures different?
2. Figure 5 again, it seems that the pattern of ‘rapid change followed by stablization phase’ does not hold on the first plot of subfigure (b)(c).

Minor:

1. For a first-time reader, it is not clear what is the ‘removal of interventions’ at row 24 of the abstract, maybe consider just using ‘gradual unfreezing’ instead.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the connection between early training dynamics and out-of-distribution (OOD) generalization. By using the trace of Fisher information and sharpness as indicators to examine the effects of interventions, the authors propose a gradual unfreezing strategy that enhances OOD generalization during the early training phase without impacting in-distribution (ID) performance.

### Strengths
1. This work is the first to highlight the impact of the early training period on OOD generalization, offering a novel perspective.

2. The use of relative values of Fisher information and sharpness as metrics for OOD generalization is interesting.

3. The gradual unfreezing method is tested across a wide range of transfer learning tasks and backbone networks, demonstrating its general applicability.

### Weaknesses
1. The paper lacks comparisons to relevant baselines in some transfer learning tasks, such as Office-Home and DomainNet. Many studies in domain generalization (DG) or OOD research focus on these datasets, but the absolute improvements in OOD accuracy presented here seem modest compared to existing methods. Specifically, the paper does not compare against methods that explicitly target domain generalization, such as those using adversarial training or meta-learning techniques, which are standard in the field. The absence of these comparisons makes it difficult to assess the true effectiveness of the proposed method relative to the state-of-the-art.

2. Previous work, such as [1], has shown that freezing parameters improves OOD performance. It is unclear whether the gradual unfreezing method can be considered a variation or a weaker form of such approaches. The discussion in Section 5.2 touches on this but remains somewhat unclear. The paper should more clearly delineate the differences between gradual unfreezing and simply freezing parameters, particularly in terms of the specific layers that are frozen and the timing of unfreezing. It is not clear if the gradual aspect provides a significant advantage over a more basic freezing strategy.

3. From a causal standpoint, it is difficult to establish a causal relationship between sharpness and OOD performance rather than mere correlation. It is possible that gradual unfreezing simultaneously affects both sharpness and OOD performance. Causal intervention strategies might be needed to investigate this in more detail, for example, by ensuring sharpness remains constant during optimization after freezing and observing the potential drop in OOD performance. The paper does not explore methods to isolate the effect of sharpness, such as by using techniques that directly manipulate the loss landscape or by using regularization methods that target sharpness without altering other training dynamics.

### Questions
1. Could additional baselines from existing OOD algorithms be included to better evaluate the impact of the proposed method?

2. How does the gradual unfreezing strategy compare to other parameter-freezing approaches during early training? Could the similarities and differences be further clarified?

3. Have similar changes in Fisher information or sharpness been observed in other OOD algorithms, and if so, how do they relate to the findings in this paper?

### Soundness
2

### Presentation
3

### Contribution
3
