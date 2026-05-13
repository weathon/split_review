# Unbounded Activations for Constrained Monotonic Neural Networks

- Decision: Reject
- Scores: 3, 6, 6, 8

## Abstract
Monotonic multi-layer perceptrons (MLPs) are crucial in applications requiring interpretable and trustworthy machine learning models, particularly in domains where decisions must adhere to specific input-output relationships. Traditional approaches that build monotonic MLPs with universal approximation guarantees often rely on constrained weights and bounded activation functions, which suffer from optimization issues. 
In this work, we prove that non-negative constrained weights MLPs with activations that saturate on alternating sides are universal approximators for the class of monotonic functions. Thanks to this new result, we show that non-positive constrained weights MLPs with convex monotone activations, contrary to their non-negative constrained counterpart, are universal approximators. 
Despite such guarantees, we also show that such classes of MLPs are hard to optimize. Therefore, we propose a novel parametrization that eliminates the need for weight constraints, allowing the network to dynamically adjust activations based on weight signs, thus enhancing optimization stability and performance. 
Experiments demonstrate that our approach maintains theoretical guarantees and significantly outperforms existing monotonic architectures in approximation accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper is about constructing monotonic MLPs with unbounded activation functions, to ease the optimization and mitigate the issue of saturation when bounded activation functions are used in prior works. The proposed construction involves an activation function whose direction is dynamically determined depending on the sign of the weight in the linear layer.

### Strengths
* The paper proposes a novel construction for monotonic MLPs with unbounded activation functions by introducing an activation function whose direction is dynamically determined depending on the sign of the weight in the linear layer. 
* The paper theoretically proves that the constructed MLPs are universal approximators for monotonic functions.

### Weaknesses
 *  The goal of the paper is on addressing optimization issues, but empirical gains are very limited. There is no gain on three out of the five experimented datasets. On the other two datasets, although the mean of the results is improved, the variance is also much larger. Overall, the empirical improvement is quite marginal, which makes the paper not convincing enough. 
* The experiment section is also very short and the authors have not investigated the results further. For example, there is no result showing whether the optimization has been eased (with loss curves, scaling behavior, etc.) 

Thus, on the empirical side, I think the paper is still quite preliminary and not yet ready for publication.

Since I can no longer post additional messages, I am posting my final response to the authors here. My position regarding this paper remains the same, [as explained in my last response](https://openreview.net/forum?id=N1DKrLIKhT&noteId=ncbNUcaRZ4).

Now I will respond to the authors' [latest response](https://openreview.net/forum?id=N1DKrLIKhT&noteId=L5d3OYv6mS).

First of all, the authors inappropriately blamed that “the reviewer decided to wait until literally the last few hours to post his response”. The authors inappropriately assumed the pronouns of the reviewer. It makes no sense to say that I “decided to wait”. Note that I have responded to the initial rebuttal two weeks ago. My recommendation on this paper has been consistent, from my initial review, to my initial response to the rebuttal, and then my follow-up responses, and the concerns from my initial review have not been addressed by the rebuttal or follow-up responses which have been making misleading claims. 

**I want to emphasize again that I don’t think the theory in this paper is a more general one and the authors are making misleading claims.** Under the same constraint with non-negative weights, the authors removed a restriction (the activation function must saturate on both sides and now an activation which only saturates on one side can be used), but the authors also introduced a new restriction (alternating saturation sides are required, which means that we have to use alternate activation functions every two layers, instead of the same activation function for all the layers). This is thus not a generalization. It has been reflected [by the authors themselves](https://openreview.net/forum?id=N1DKrLIKhT&noteId=RYasdvC09j):

>Until now, constrained monotonic MLPs were shown to be universal approximators only using the threshold activation (sigmoid-like), thus with both sides saturating. Instead, we show that **you only need activations that alternate sides of saturation**.

The authors then said:

>it is indeed possible to use the same activation function by ensuring all weights are negative

Note that this has changed the settings (from non-negative weights to non-positive weights). Although you can use the same activation function now, another new thing has been introduced (non-positive weights). The authors again remove a restriction but add another new restriction. This is again not a generalization. 

On the empirical side, the paper only has very preliminary results. E.g., Figure 4 in the appendix showed some training loss curves on a toy setting, without further investigation on real datasets. It is also unclear if the difference in the training curves can be caused by the need of different hyperparameters when the models are different (e.g., possibly one setting requires a larger learning rate and then the loss may descend faster).

The paper requires much additional work to significantly improve the experiments which are still very preliminary for now. The experiments are necessary in order to justify that the theoretical analysis on model settings newly introduced by the authors (either alternating saturation sides or changing the sign of weights) are useful.

Both the authors and Reviewer tpMq are using an argument that the limited experiments with limited empirical improvement in this paper is not important because this work is “mostly theoretical”. I don’t find this argument reasonable here. 

In fact, this paper just reads like a regular ML paper proposing a new method, with a theoretical motivation and analysis, followed by empirical results. I don’t think it can be considered as mostly theoretical, as the paper is actually proposing a new model (just like other regular ML papers) instead of theoretically analyzing an existing technique. In this case, I believe a consistency between theoretical results and empirical results is necessary, and the empirical results should be able to demonstrate the advantage of the new model proposed. 

The paper is claiming that the proposed construction can be used for “enhancing optimization stability and performance” and “making the optimization more stable and less sensitive to initialization”, yet the experiments have not been able to sufficiently demonstrate the benefits. The paper also claims to achieve SOTA as “we show that we can achieve state-of-the-art performances”, which is not true.

I don’t think it convincing to say that this “generalizes” previous results. **I believe the theoretical contributions have been overclaimed (and overestimated by some other reviewers).** In previous results, you can use the same activation function in every layer. However, in the new results here, you have to “alternate sides of saturation” and thus essentially use alternate activation functions for every two layers. **This seems to remove the restriction on the activation being “bounded”, but it adds a new restriction -- you can’t use the same activation function for all the layers any more.** This is not a generalization and not a “structural simplification”. The new change also makes the architecture different compared to regular NNs, yet such a change is not justified (given that there is no empirical improvement). 

Therefore, the paper is actually proposing some new architecture (with activations that alternate sides of saturation every two layers) and proving that this construction is a universal approximator. However, the paper has not been able to demonstrate that the new construction is empirically useful as I mentioned earlier, and thus it has not demonstrated that a theoretical analysis alone on this particular architecture (which is not more general than existing ones) is a significant contribution. 

As I said earlier, the claim that the focus of this paper is on a theoretical analysis is quite unconvincing and misleading. The theoretical analysis is not done for existing models which have been demonstrated to work well by previous works. If a theoretical paper analyzes some existing model (which previous works have demonstrated that the model is meaningful) and provides significant theoretical insights, it would be a significant theoretical contribution. However, here the theoretical analysis is done for something newly proposed in this paper, yet the paper has not been able to demonstrate that the new thing (which eliminates a restriction but adds a new restriction) is meaningful through experiments. Therefore, I believe a theoretical analysis alone is not enough to claim a major contribution. 

For experiments, I didn't mean that you must achieve SOTA. Instead, empirical results should justify claims made in the paper regarding the newly proposed architecture (“enhancing optimization stability and performance” and “making the optimization more stable and less sensitive to initialization”). This doesn't have to be SOTA, but experiments have to justify that the new method at least has sufficient benefits.

### Questions
Why is the empirical improvement so marginal, despite the theoretical insights shown in the paper?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a new neural network structure to reflect monotonic relationships between a specific features and the output in neural networks.  Traditional monotonic MLPs rely on non-negative constrained weights and saturating activation functions (e.g. Sigmoid, Tanh) to maintain monotonic relationships, which can cause optimization difficulties and limit expressiveness. The paper proves that by using alternating left-saturating and right-saturating monotonic activation functions, an MLP with either non-negative or non-positive constrained weights can serve as a universal approximator for monotonic functions. Additionally, the authors propose a new parameterization method (activation switch) that eliminates the need for weight constraints, thereby enhancing optimization stability and performance. Experimental results demonstrate that the proposed method achieves better approximation accuracy than existing monotonic neural network structures while preserving monotonicity and universal approximation properties.

### Strengths
$\bullet$ The proof is constructed with solid mathematical rigor.

$\bullet$ The proposed method (activation switch) is explained clearly and in an easy-to-understand manner.

$\bullet$ The experiments on real-world datasets for the proposed method were conducted appropriately.

### Weaknesses
Weakness 1. The categorization of related literature is unclear, and explanations are insufficient. 
-  The explanations of related work in Section 1 (Introduction) and Section 2 (Related Work) are incomplete and would benefit from integration. (soft vs hard / CONSTRAINED MONOTONIC ARCHITECTURES vs HEURISTIC AND REGULARIZED APPROACHES)
-  There is an unclear expression on page 1, line 49-50. ("Such guarantees usually come at the cost of effectiveness.") Please explain the following sentence more clearly.

Weakness 2. Additionally, many relevant references are missing([1], [2]). 

-   Both papers [1] and [2] are recent works in the field and should be included as comparison targets as related works. These studies should be cited in the paper.


Weakness 3. There are doubts about the contributions claimed by the authors, and most aspects raise concerns regarding novelty.

-  Despite the authors' efforts in their proof, it seems that the essential point is that a monotonic neural network requires positive weights (or an even repetition(e.g. $2$-layers, $4$-layers ... $2n$-layers) of negative weights) and a structure with activation functions that support monotonic increasing properties (including both convex and concave functions). I believe the proposed structure $activation switch$ in this paper does not deviate from this approach in the broader sense. If I missed anything, please explain more clearly how the proposed method differs from existing methods.

Weakness 4. The practical issue of gradient vanishing problem.
-  Concerns about gradient vanishing should be critically considered, especially given that monotonic neural networks can generally serve as universal approximators for arbitrary monotonic functions even with a shallow depth of 4. In fact, papers [2] and [3] report better performance than the proposed method and appear to have much simpler architectures, using lower depth network. 

- As I understand it, using batch normalization along with existing methods seems to significantly alleviate the gradient vanishing problem. Is my understanding correct?



Weakness 4. The experimental results in this paper exclude several recent works in the field from comparative analysis. Although I do not believe that solely achieving SOTA performance defines the contribution of this study, there are concerns about cherry-picking in the reported results, or revisions may be necessary to better reflect the authors' claims in the experimental section.

- Paper [3] is mentioned in the main text but was excluded from the experiments. Paper [3] uses exactly the same datasets as the authors, and even shows better performance on some of them. To address concerns about cherry-picking, paper [3] should be added to the experiment.
- Paper [2] also constrains weights to be non-negative through re-parameterization (exponential transformation) and uses a saturated activation function. However, it achieves very good performance (SOTA) on several datasets. So, paper [2] also should be added to the experiment.

Weakness 5. (minor) There are multiple comma-separated phrases within single sentences, or sometimes incomplete sentences, making it difficult to understand.

- page1, line 71-74
- page3, line144-146
- page7, line 326-328
- page7, line 332-334
- page9, line 473 (incomplete sentence)

Weakness 6. It would be beneficial to include a discussion on the ethical considerations associated with using the COMPAS dataset. Given that this dataset involves sensitive information and has been widely discussed in terms of fairness and bias, it would strengthen the paper to address potential ethical concerns and how these were considered in your analysis.

### Questions
1) If I understand correctly, since they use "point-symmetric activation functions" simultaneously, wouldn’t the authors' claim in "We prove that contrary ...  even convex ones like ReLU, is a universal approx"(at contribution section in Introduction) that it is "even convex once" be incorrect? 

2) In the text, does "Constrained MLP" actually refer to "Constrained MNN"?

3) Is there any other reason why the experimental results from paper [3] were excluded?

4) It would be better to cite the officially published versions of papers, including paper [3], rather than the arXiv versions where possible.

5) Based on my understanding of the paper, it seems that having both "convex" and "concave" types of activation functions within the network is a more important key point than simply having "left-saturating" and "right-saturating" activations. Could you explain the difference between these two concepts in more detail?

(minor)
1) page9 line 473 "The only requirement for this method to work, is to have the input features to be", Isn't it an incomplete sentence?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new method for building monotonic neural networks using unbounded activations like ReLU, avoiding traditional weight constraints. The proposed architecture dynamically adjusts activations to ensure monotonicity, simplifying optimization. Theoretical results show it can approximate any monotonic function, and experiments demonstrate improved accuracy on several datasets. This approach enhances the usability of monotonic networks in interpretable AI applications.

### Strengths
1. The paper introduces a new parametrization technique for monotonic MLPs, which removes the need for weight constraints and allows the network to adjust activations dynamically. This could improve flexibility and ease of optimization.

2. The authors provide a new theoretical result showing that MLPs with alternating unbounded activations are universal approximators for monotonic functions. This strengthens the theoretical foundation of monotonic neural networks.

3. By focusing on monotonic architectures, the paper addresses a key need in applications where interpretability is critical (e.g., fairness and transparency), making this work relevant for real-world deployment.

### Weaknesses
1. The experiments cover only a small number of datasets. Extending the evaluation to more diverse datasets and tasks would provide stronger evidence of the model’s generalizability and practical utility. Specifically, the current selection does not adequately explore the model's behavior across varying data distributions or feature dimensionalities, limiting the assessment of its robustness in real-world scenarios. The lack of datasets with high dimensionality or complex feature interactions is a notable gap.

2. Although the authors propose a solution to avoid weight constraints, they do not fully address potential optimization challenges, such as sensitivity to initialization or convergence rates, which may impact the method’s robustness. The paper lacks a thorough analysis of how different initialization schemes affect the training process, and it does not provide any empirical evidence regarding the stability of the optimization process. Furthermore, the convergence behavior of the proposed method, especially in comparison to other monotonic network training methods, is not discussed.

3. The paper’s theoretical section relies heavily on specific activation behaviors without enough real-world validation, which may limit the practical applicability of the theoretical claims. While the theoretical results are interesting, the paper does not sufficiently demonstrate how these theoretical properties translate into practical advantages in real-world applications. The analysis lacks a discussion of how the assumptions made in the theoretical analysis might affect the model's performance when applied to noisy or non-ideal data.

### Questions
1. Could the authors clarify why ReLU and similar unbounded activations were chosen over traditional bounded activations in monotonic settings? What specific advantages do these activations bring in practical applications, beyond the theoretical universal approximation guarantee?

2. How does the proposed parameterization handle sensitivity to weight initialization? Did the authors test different initialization schemes, and if so, which were most effective? Further details here would be valuable for readers aiming to replicate the setup.

3. The experiments focus on a limited set of datasets. How does the model perform in other domains requiring monotonicity, such as environmental modeling or medical risk assessment? Expanding the range of tested applications could reinforce the paper's claims of generalizability.

4. The paper mentions that the new parameterization requires double matrix multiplications for weight splitting. Did the authors measure the computational overhead introduced by this approach? Reporting training times or memory usage compared to other methods would give insights into the scalability of this model.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper studies learning monotone functions with networks. The authors show a powerful expressivity result: non-negative weight networks with left- and right-saturated activation functions can approximate all monotonically increasing functions (thus all monotone functions via sign flip). They further show that non-positive weights lead to universal approximation of monotone functions even with convex activations such as ReLU, while these activations combined with non-negative weights can only approximate convex monotone functions. Overall, the authors present novel and impressive theoretical results.

This work further proposes an algorithm to utilize their theorems, achieving sufficient improvements on the tasks they studied.

### Strengths
The theoretical results are sufficiently impressive, and the proof techniques are clear and well-motivated. I found the proof easily understood. The authors also support their theorems with adequate numerical experiments.

### Weaknesses
The paper is barely written and not sufficiently revised. For example, numerous typos exist: Line 267, I suppose a $\gamma$ is missing before $1_A(x)$; Fig 2, caption looks messy; Line 473, a sentence is incomplete. I suggest all authors, especially those senior, to carefully revise the paper end to end since the current writing is a bit in fragments.

Improvements achieved in Table 1 looks marginal except for the heart disease dataset. However, I would not indicate negative opinions due to this as this is acceptable for this mostly theoretical paper. In contrast, I find this quite interesting because they were able to design a trick other than constraining the weights to enforce the monotonicity constraint.

### Questions
I have an additional question regarding the algorithm. The authors convert the constraint on networks weights to constraints on the prediction, i.e., design different forward pass for positive and negative weights. They simply claim this would mitigate the optimization difficulty because seemingly this will not lead to gradient vanishing. However, I did not find sufficient theoretical/experimental results supporting this other than the main results presented in Table 1. It would be better if the authors could clarify this.

### Soundness
4

### Presentation
2

### Contribution
4
