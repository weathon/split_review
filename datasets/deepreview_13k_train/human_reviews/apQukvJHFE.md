# Lightweight uncertainty modelling using function space particle optimization

- Decision: Reject
- Scores: 3, 5, 3, 6, 3

## Abstract
Deep ensembles have shown remarkable empirical success in quantifying uncertainty, albeit at considerable computational cost and memory footprint. Meanwhile, deterministic single-network uncertainty methods have proven as computationally effective alternatives, providing uncertainty estimates based on distributions of latent representations. While those methods are successful at out-of-domain detection, they exhibit poor calibration under distribution shifts. In this work, we propose a method that provides calibrated uncertainty by utilizing particle-based variational inference in function space. Rather than using full deep ensembles to represent particles in function space, we propose a single multi-headed neural network that is regularized to preserve bi-Lipschitz conditions. Sharing a joint latent representation enables a reduction in computational requirements, while prediction diversity is maintained by the multiple heads. We achieve competitive results in disentangling aleatoric and epistemic uncertainty for active learning, detecting out-of-domain data, and providing calibrated uncertainty estimates under distribution shifts while significantly reducing compute and memory requirements.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a functional uncertainty quantification technique for neural networks based on particle representations which has the following core innovation: it attempts to share a backbone architecture and replace heads per particle.

Taking things from the top, the authors embrace the particle-based VI literature in a functional view and combine it with spectral normalization to obtain smooth "head" representations and capture densities better.

They largely follow the path forged by D'Angelo and Fortuin, with minor modifications int he shared backbone and addition of spectral normalization which was explored heavily in DDU and other works that they attribute correctly.

In practice, the functional view trades off parameters for memory and data-constraints and becomes quasi-semi-parametric, so the authors also consider ways to generate useful "context points" to evaluate their functions so that the function-space kernel works correctly.

The performance of the technique seems fine evaluated over a variety of tasks where authors capture accuracy, in-distribution, and out-of-distribution metrics combined with parameter count.

### Strengths
The paper proposes a combination of known techniques and architecture changes that ultimately works.

The idea of sharing backbones is sound and has been applied to ensembles before, and combining their heads with spectral normalization to create better density models is also a reasonable step aligned with many successful papers.

Finally, the experiments indicate that their setup works well quantitatively with less parameters than other techniques that are as performant, and while not quite matching ensembles is oftentimes stronger than single-network uncertainty techniques.

### Weaknesses
I have a few concerns with this paper.

First:
The proposed model is extremely close to D'Angelo and Fortuin . Pairing this with shared backbones and spectral normalization is sound, but also not particularly impressive as an addition to the exploration space here.

Second:
The authors do not show enough ablations of the role of each part of their model.
How would they compare against combinations of their individual variations with baselines?
More importantly: what does spectral normalization really buy here?
How much is the backbone the key thing?

Third:
The authors evaluate a few different choices for their context dataset, but to my liking this is insufficient.
In their particle-based representation, parametric complexity is exchanged with evaluating context data, I will just call this a semi-parametric representation. As such, how much data is used for that semi-parametric representation and how that interacts with fidelity would be an important gradient to show here.
How stable is the model to varying that?
Which types of perturbations not heir images buy how much performance?
More importantly: the authors are proud of having reduced parameter count, but now require a battery of context data for each gradient step of their models. As such, evaluating how this interacts with memory requirements here is key.

In short: given that this paper jumps on the idea of representing BNNs functionally in a semi-parametric way, talking about the memory requirements for each type of computation and how that Pareto front varies seems as important as reporting the final parameter counts.

This might also help the authors justify their shared backbone more throughly: possibly the functional representation necessitates techniques to reduce memory footprint like shared backbones to more efficiently use GPU memory since the representation of f_backbone(context) is shared and as such does not incur memory overhead.

### Questions
I mentioned a lot of questions in the weaknesses tab.

Ablations of the pieces here.

A rigorous study of the context points and their properties and effects on this representation.

A study of the memory trade-offs when doing this.

In what scenarios is this type of inference beneficial compared to full ensembles?

I imagine there will be a regime of a certain dimensionality of networks or data complexity where the ensemble representation more efficiently captures uncertainty compared to the functional view.

I would enjoy seeing these talked about a lot more, they feel core to the paper's thesis.

Subject to seeing a significant change in the paper along these axes that offers more empirical learnings and insights for the reader given that the technical ideas are limited I would consider changing my score.

### Soundness
3 good

### Presentation
3 good

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
In this work, the authors proposed a hybrid approach using a multi-head network to achieve lightweight uncertainty modeling. The method provides calibrated uncertainty and also preserves bi-Lipschitz conditions by leveraging particle-based variational inference in function space. They also claim that the method achieves competitive results in disentangling aleatoric and epistemic uncertainty for multiple UQ tasks, including active learning, OOD detection, and distribution shifts with reduced compute and memory requirements.

### Strengths
1. The paper is well-written and easy to follow with strong related work and background.
2. The topic is very interesting and aims to address the current bottleneck of deep ensemble and DUQ studies. 
3. The experiments demonstrate the effectiveness of the proposed method clearly and provide a comprehensive assessment of multiple tasks in the uncertainty estimation area.

### Weaknesses
1. The novelty contribution seems not very strong. Most of the core components in this framework all exist while the development of the framework is a nontrivial task. 
2. Beyond the multi-head architectures, we did not directly capture the core contribution of the new method compared with the existing deep ensembles or DUQ methods. Specifically, the paper lacks a clear explanation of how the proposed method's specific mechanisms lead to improved uncertainty quantification compared to simply using multiple heads or other existing methods. The connection between the particle-based variational inference in function space and the observed empirical improvements is not sufficiently clear.
3. The method section lacks enough details and discussions such that it might not be easier to reproduce the method. For example, the specific initialization of the particle-based variational inference, the choice of context points, and the training procedure for the multi-head network are not described in sufficient detail. The paper should include more details on the practical implementation of the method. 
4. Some key claims, like disentangling uncertainties and preserving bi-Lipschitz conditions are not well supported from the theoretical perspective.  We only observed improved empirical results but may not fully understand why the proposed methods bring such advantages. The paper does not provide a theoretical analysis of how the proposed method achieves these properties, and the empirical results, while promising, do not fully explain the underlying mechanisms.

### Questions
1. How to preserve the bi-Lipschitz conditions and how to avoid feature collapse?  What's the key component to deal with these challenges? Can you show some ablation studies to verify the effectiveness? 

2. How to disentangle aleatoric and epistemic uncertainty?  Which features mainly handle these capabilities？ What's the theoretical foundation of the proposed method or by leveraging existing works? 

3. How about the computational cost and memory cost comparison with the baseline methods on multiple tasks?  I think it is important to show these since the paper mainly claims the high efficiency and low memory requirements.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Summary:
This article presents a lightweight approach to uncertainty modeling that provides calibrated 
uncertainty estimates by utilizing particle-based variational inference in function spaces. Unlike 
methods that use deep ensemble representations of particles, this approach presents a multi-headed 
neural network that achieves a reduction in computational requirements. By sharing a joint latent 
representation, the computational requirements are reduced, while the multi-head network maintains 
the diversity of predictions.

### Strengths
Strengths:
1) This article presents a method for uncertainty estimation based on particle inference in function 
space, along with a hybrid method using multi-head networks.
2) Using multi-headed networks instead of full deep integration methods for lightweight purposes.
3) The article examines out-of-distribution data, provides uncertainty estimates for calibration 
under distributional shifts, and obtains certain experimental results.

### Weaknesses
1)Given the emphasis on 'LIGHTWEIGHT' in the article's title, I expect to see more in-depth 
analysis and explanation of this theme in the main text to help readers better understand its 
role in the research. Specifically, the paper lacks a clear definition of what constitutes 'lightweight' in the context of uncertainty estimation. The authors should provide a quantitative measure (e.g., parameter count, FLOPs, memory footprint) to substantiate their claim of lightweight design and compare it against existing methods. Furthermore, the analysis should not only focus on the computational cost but also on the trade-off between computational efficiency and predictive performance.
2)The authors evaluated the proposed multi-headed architecture on several benchmark tasks. 
However, the reasons for the selection of these benchmark tasks were not discussed. The paper should justify the choice of these specific tasks and explain how they are relevant to the problem of uncertainty estimation under distributional shifts. It is unclear whether these tasks are representative of real-world scenarios where uncertainty quantification is critical. A more detailed discussion on the characteristics of the chosen datasets and their relevance to the proposed method is needed.
3) The topic of the article is uncertainty estimation under lightweight, the author's description of 
lightweight is not sufficient, and the analysis of lightweight is lacking in the experimental part. The experimental section lacks a thorough analysis of the computational overhead introduced by the multi-headed network. The authors should provide a detailed breakdown of the computational cost associated with each component of the proposed method, including the base network, the multi-headed network, and the particle-based variational inference. It is also important to analyze how the computational cost scales with the number of particles and the size of the input data.
 4) The author's contribution is not enough, the multi-head network and particle variational 
optimization methods used are directly from other places, and the article lacks a certain degree 
of innovation. The paper does not adequately highlight the novelty of the proposed approach. While the authors combine existing techniques, the paper should clearly articulate the specific modifications or adaptations made to these methods and how they contribute to the lightweight uncertainty estimation. The paper should also discuss the limitations of the proposed approach and compare it with other related methods in terms of both performance and computational cost.

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper is about uncertainty estimation with function space particle optimization. Its basically an ensemble, where each ensemble member represents one particle, and a special loss function repels particles away from each other, to ensure diversity in the ensemble. The authors propose to use a lightweight network architecture that uses a shared representation network and multiple prediction heads that each represent a particle.

Contributions are
- A method for uncertainty estimation using a single network architecture with multiple heads and function-space particle optimization, which is more computation and parameter efficient than a full ensemble.
- Results that show that the particle optimization in ensemble heads provides high quality uncertainty estimation in various settings including out of distribution detection and calibration, assuming the right regularization.
- Results that show successful disentangling of aleatoric and epistemic uncertainty on MNIST for active learning, and near and far out of distribution detection on CIFAR10, and provide good uncertainties under distribution shift (corruptions).

### Strengths
- The paper is mostly well written and kind of easy to understand. I have reservations below about some details of the model.
- The idea makes sense, to increase diversity of ensemble heads by treating the like particles that repel to each other and explore different parts of the parameter/function space, this seems to be applied to ensembles and now the authors propose to use a ensemble with a shared representation network, which lowers the computation costs for inference time. This is important due to researchers and practitioners not using uncertainty estimation methods because of increased computational costs.
- The selection of baselines seems to be appropriate, even as I make suggestions for better baselines in the minor comments. The paper compares against DDU and ensembles, DDU is a good and recent baseline for lightweight uncertainty estimation (using a single model), while ensembles is the state of the art for simple ways to obtain high quality uncertainty estimation.
- The evaluation seems to be correct, the paper uses Dirty MNIST and CIFAR10/100 vs several out of distribution datasets, including out of distribution classification of incorrect predictions, and evaluates appropriate metrics: accuracy, expected calibration error, and AUROC for OOD detection.
- Results indicate that the propsed method MH-POVI and MH-f-POVI performs closely to a ensemble and sometimes it outperforms DDU (also a single model) in terms of accuracy, calibration error, and out of distribution performance, often coming in 2nd place behind ensembles. I believe these results show that particle optimization for shared network ensembling is a viable strategy.
- There is a good set of ablation results, varying the selection of context points (three) for the functional variant of MH-POVI, showing the effect of this parameter on performance, and also OOD detection on corrupted versions of CIFAR10 and 100, showing that MH-POVI and functional variant are closer to ensembles in performance loss than it is to DDU (which performs worse).

### Weaknesses
 - I have doubts about the fairness of the comparisons, as 20-30 particles are used for MH-POVI and variations, but only an ensemble of five networks. I believe a fairer comparison is to equalize the number of ensemble networks and particles, or to evaluate both methods with a variable number of particles and ensemble members, which also would provide information about how both methods scale with the number of particles.

- In Figure 3, I believe the paper has to say how to interpret these plots, that in the OOD setting ideally aleatoric uncertainty should be low and epistemic uncertainty should be high, while the in-distribution setting it is the opposite (epistemic low and aleatoric variable depending on samples).
- In Section 3, please explain what is negative data augmentation, this term is not clear from the context of the paper and no citation for further information is provided.

### Questions
- Could you clarify how the network heads are trained using function space particle optimization? In particular how Eq 2 is evaluated.
- Is the model trained end-to-end? Please clarify the training process.
- Can you motivate the selection of context points? For example using Gaussian noise as a context point, how do you know that these points are supported by the data distribution?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a simple and efficient method for uncertainty estimation, namely to use a single deterministic network backbone with a small multi-head classifcation/regression head that is trained via a particle optimization objective that ensures diversity. This allows for a parametrically and computationally efficient alternative to ensembles. The experiments report improved performance over single deterministic networks and DDU on a range of in- and out-of-distribution uncertainty estimation tasks on various vision classification datasets.

Overall, while the work achieves its aim of introducing a computationally efficient method, the paper does not compare to any competitive baselines despite a range of comparable methods having been introduced in recent years. In conjunction with no new technical material being introduced, I think the paper should be rejected.

### Strengths
- the approach is described and motivated clearly
- the method is efficient and pragmatic
- paper is well-referenced, prior work that the paper builds upon is credit and the paper is properly contextualized in the literature

### Weaknesses
 - most importantly, the paper sorely lacks a competitive baseline for efficient uncertainty estimation. DDU underperforms even the single net baseline on all non-MNIST benchmarks, on some of them by a large margin (CIFAR100 in Table 2, bottom panel of Fig 4). I don't know if DDU hasn't been tuned properly or simply isn't suited to tasks with a large number of classes, but in either case there are plenty of alternatives available in the literature that have reported good results in this setting, e.g. (Liu et al., Simple and Principled Uncertainty Estimation with Deterministic Deep Learning via Distance Awareness, Neurips 2020) or (Kristiadi et al., Posterior Refinement Improves Sample Efficiency in Bayesian Neural Networks, 2022).
- the paper is a bit light on ablations. In particular the use of the spectral normalization is not justified empirically. From a theoretical standpoint, as far as I am aware, prior work has justified its need based on the network being distance preserving being necessary for the use of a distance aware output head, however I do not see the proposed method relying on this property, so I would like to see a baseline without spectral normalization. Similarly, the structure of the ensemble heads appears as a magic hyperparameter without justification. I realize that a linear head without hidden layers will probably underperform due to the categorical log likelihood being a convex/unimodal objective w.r.t. the weights of the linear output layer, but this should be justified explicitly and sensitivity of the method w.r.t. this hyperparameter evaluated.
- the paper does not introduce any new technical material. This is in itself of course not grounds for rejection, combining prior work can be valuable, however I don't see any technical or theoretical contributions that would make up for the lacking empirical evaluation.

### Questions
To summarize the weaknesses, I would suggest to:
- add a couple of competitive(!) baselines from the literature on efficient uncertainty estimation and evidential deep learning
- justify the use of spectral normalization via an ablation study
- evaluate the sensitivity of the method w.r.t. depth/width of the ensemble head and discuss the trade-off vs. computational efficiency

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
