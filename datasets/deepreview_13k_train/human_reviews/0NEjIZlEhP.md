# Verified Relative Output Margins for Neural Network Twins

- Decision: Reject
- Scores: 5, 3, 6, 3, 3

## Abstract
Given two \gls{DNN} classifiers with the same input and output domains, our goal is to quantify the robustness of the two networks in relation to each other. Towards this, we introduce the notion of \glspl{RPR}. Intuitively, given two classes and a common input, \gls{RPR} of one classifier with respect to another reflects the relative {\em margins} with which decisions are made. The proposed notion is relevant in the context of several applications domains, including to compare a trained network and its corresponding {\em compact} network (e.g., pruned, quantized, distilled network). Not only can \glspl{RPR} establish whether decisions are preserved, but they can also quantify their qualities. We also propose a framework to establish safe bounds on \gls{RPR} gains or losses given an input and a family of perturbations. We evaluate our approach using the MNIST, CIFAR10, and two real-world medical datasets, to show the relevance of our results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
I am pretty new to this field so I will try to summarize what I understand to be the key contributions of this paper. If I am wrong, please do let me know in the comments:

1. The authors introduce a new way to compare two neural networks (e.g. an original and a compressed version of the same net) by looking at their "relative output margins" = essentially comparing how confidently they make the same decisions.

2. They provide a formal verification framework that can prove, within a small neighborhood of a given input (like a small perturbation of an image), that one network will always make decisions at least as confidently as another network when they're both correct.

They demonstrate this is practically useful when:

a. Comparing original networks with their pruned/quantized/distilled versions
b. Analyzing medical AI systems where reliability is crucial
c. Understanding the relationship between regular and adversarially-trained models

The key innovation is that instead of trying to verify properties across all possible inputs (which would be intractable), they focus on small, local neighborhoods around specific inputs and use linear programming techniques to efficiently compute provable bounds on the networks' relative behavior in these regions.

### Strengths
The problem the authors are addressing is import and relevant:
How to formally compare two neural networks' decision confidence across many examples and not only at the given evaluation datapoints. This is especially relevant when we modify networks via e.g. quantization and pruning but need guarantees (in high stakes settings such as medicine).

The linear programming formulation makes the solution practical, which is good -- imho a method that can be practically applied is a key to wide adoption and impact.

I also appreciate the comparison to adversarially trained models.

### Weaknesses
I have a few concerns:

1. Scalability

1.1. linear programming can be expensive -- how well does this scale to larger networks?
1.2. small networks and small regions are shown in the paper. How well would this do on e.g. a ~100M parameter ViT and with larger regions?

2. How tight are the bounds? Do you have any experiments to demonstrate that? I would also be great to discuss worst-case scenarios with examples and develop some kind of a rudimentary case study of that.

3. Small regions
The small perturbation sizes used (0.001, 0.01) may not reflect real-world distortions. If I add a bit of a Gaussian noise to the whole image, I can easily get much higher delta. 

4. Comparison to other linear programming based methods
I think there are other methods that use local approximations to calculate the difference between networks (I might be wrong on this), yet you don't compare to them?

5. Medical Application Claims
It would be good to compare your estimates to some sources of ground truth. Is that feasible?

### Questions
Included in weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper is interested in certifying the output of a given network w.r.t another one, targeting use-cases like pruning/distillation/quantization, in the goal of demonstrating that the pruned/distilled/quantized network exhibits not only similar accuracy over the train set, but even consistent decisions around the same local regions around each training example.

To do so, they introduce a novel measure called Relative Output Margin (ROM), with is the ratio between the Output Margin (OM) of two networks at a given input point. Finally, by taking the minimum of the ROM over a whole infinity-norm ball centered around a given point, they define the Local ROM (LROM).

Computing the exact LROM is a hard problem, but its linear relaxation for feed-forward ReLU networks is tractable and yields a lower bound, which is sufficient for the purpose of certification. 

The algorithm is tested in the context of pruning, quantization, and distilled networks, on two images datasets (MNIST, CIFAR-10), and two tabular/signal datasets (CHB-MIT and MIT-BIH).

### Strengths
### Originality

It think the main originality of the paper lies in considering the joint optimization of the margins of two networks. Intuitively, one can understand why this is a superior approach compared to optimizing separately the bounds and trying to aggregate them (although the optimization problem is now double the dimension), as shown in Figure 2.

Focusing on the context of pruned/distilled/quantized networks is also relevant, re-targeting the (sometimes too ambitious) conventional goal of certifying a given network into just showing that some networks is not much worse than an other.

### Clarity and soundness

The paper is clear overall, proofs look correct.

### Weaknesses
### Novelty

My main source of concern is the novelty. Computing certificates for ReLU-based networks is a well established methodology that relies on various linear relaxation (as used in this paper), or interval propagation.

This paper utilizes these tools, and the only novelty is to consider a joint optimization of the difference of logits for two networks, instead of a single one, which I consider a straightforward extension departing from existing methods.

Therefore the main contribution of the paper is introducing the OM, ROM and LROM measures, and using the whole Section 2 to deal with rather trivial considerations.

All the proofs of appendix A.1 are a trivial consequence of manipulating the log of probability ratios, to end-up with a simple difference of logits. This is colloquially called the *margin*, not to be confused with the Output Margin (OM) measure that authors introduce, without clear motivation.

In most papers for NN certification, this margin is analyzed, reported  or even optimized (using Hinge loss) in a straightforward manner, without bothering highlighting the link with output probabilities. In this regard, the theoretical contribution appears rather shallow IMHO.  

Dropping this narrative would even allow to use the method of the paper outside the context of classification. Even the concept of “twin networks” looks overkill to simply describe networks operating over the same input/output spaces.

### Questions
1) LROM is assymmetric, i.e inverting DNN N1 and N2 yields a different bound. Can you comment on this property? Is this something desirable? What if LROM(N1, N2) equals some value, and LROM(N2, N1) equals another, is there something to interpret here (qualitatively)?

2) When LROM is very negative (i.e logits difference is huge) which implies that probabilities are near-zero, not too far away from machine precision zero, do you expect this value to carry meaningful information?

3) Can you clarify use-cases in which LROM is useful for practioner?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a framework for comparing two neural network classifiers with shared input and output domains. The goal is to analyze these "neural network twins" through the concept of Relative Output Margin (ROM), a metric indicating the confidence with which one network outperforms the other within a defined input region. Specifically, the framework formalizes and verifies "Local Relative Output Margins" (LROMs), allowing for the computation of provable bounds that indicate which network consistently makes correct decisions across input variations. This is crucial in applications where compact, optimized versions of networks are used, such as in medical device deployment, where safety-critical tasks like seizure and arrhythmia detection require guaranteed performance reliability. 

The experiments in the paper evaluate the proposed Relative Output Margin (ROM) and Local Relative Output Margin (LROM) framework by testing it on four datasets: MNIST, CIFAR-10, CHB-MIT (EEG data for epilepsy detection), and MIT-BIH (ECG data for arrhythmia detection). The experiments focus on verifying LROM across different pairs of neural networks: original, pruned, quantized, and distilled versions. Across datasets, the experiments demonstrate that the LROM framework effectively captures the comparative performance and robustness of different network types under a defined perturbation range.

### Strengths
- The paper’s primary contribution lies in defining and formalizing ROM and LROM. This enables a provable, quantitative comparison between neural networks for applications requiring high reliability and safety.

- The study evaluates the proposed framework across multiple datasets, including standard and specialized medical data, supporting the generalizability and robustness of LROM as a comparative measure.

### Weaknesses
 - The LROM optimization framework requires handling complex linear programming tasks, which may limit scalability for larger networks, particularly those with a high number of parameters and layers. It would be beneficial to test the framework further on larger neural networks, such as language models, to assess its practical applicability in more complex scenarios. The computational cost associated with solving these linear programs could become prohibitive, hindering the framework's use in real-time or resource-constrained environments.

- It may be challenging to interpret the evaluated measures due to the technical intricacies involved in LROM computation. The paper could benefit from more intuitive explanations and visualizations of the LROM metric, making it more accessible to a broader audience. The current presentation assumes a strong background in formal verification, which might not be the case for all readers interested in the practical implications of the work.

### Questions
- It would be better to conduct a comparison with existing adversarial robustness metrics and methods. How do the proposed measures differ from the existing adversarial robustness measures? 

- What would be the applications of the framework beyond network twins (similar architectures with compact versions), such as varied neural architectures?

### Soundness
3

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
4

### Summary
This manuscirpt define the notion of Relative Output Margin (ROM) and Local ROM (LROM) to compare network twins. Specifially, LROM > 0 means one network can consistently outperform another one in the vicinity of a given points. a theorem is provided the bound the LROM. Experiments on for datasets with 7-layer MLP are conducted to show the effectiveness of proposed LROM.

### Strengths
- A novel notion of Relative Output Margin is proposed.

- The organization (not writing) is very well.

- Experiments on multiple experiments are presented to show the interesting property of ROM.

### Weaknesses
## Major

- The conclution is unclear.
     - In my opinion, the main theorem (Theorem 3.1) solely establish that there indeed exists upper and lower bounds for any LROM. If it is, the significance of this theorem is limited and LROM cannot be linked to the generalizability of DNNs. The theorem, as presented, does not provide a mechanism to directly relate the bounds to generalization performance. It only shows the existence of such bounds, which is not sufficient to establish a practical link to generalization.
     - There is no clear conclusion for experiments. What do the experiments show? The experiments lack a clear narrative. It's not clear what specific insights the experiments provide about the practical utility of LROM. The results are presented without a clear connection to the broader goals of the paper, such as demonstrating the practical value of LROM in comparing network twins.

- In the experiments, only a small 7-layer MLP is used, which hardly give a good predition for CIFAR-10, which makes a limited contribution. Can the authors provides the results at least on CNNs like VGG or ResNet? The use of a shallow MLP on CIFAR-10 is not convincing. The results obtained on such a simple architecture might not generalize to more complex and practically relevant architectures like VGG or ResNet. This limits the impact of the empirical evaluation.

- In the experiments, "We exclusively focus on **correctly** classified samples" (Line 299). For me, a big application for ROM is to measure the uncertainty of predictions. If we have already know that the predictions is correct, there is no point to use this technique. The focus on correctly classified samples limits the applicability of the proposed method. A key use case for margin-based analysis is to understand the uncertainty of predictions, especially for misclassified samples or samples near decision boundaries. By focusing solely on correctly classified samples, the authors miss an opportunity to demonstrate the full potential of their method.

## Minor

- The writing can be improved.
    - In Introduction, more words are needed to breifly introduce the theoretical and empirical work ( now only 6 lines from Line 61-66), which will make this paper more clear. The introduction lacks sufficient context and background on existing theoretical and empirical work related to network comparison and robustness. This makes it difficult for the reader to understand the novelty and significance of the proposed approach.
    - The notation are too complicated and can be simplified. The notation used throughout the paper is overly complex and could be simplified to improve readability and accessibility.

- It is better to number equations.

- use $\max$ and $\min$ to replace $max$ and $min$ in the equations.

- Line 215: "$-\mathcal{R}\geq \mathcal{M}$" -> "$-\mathcal{R} \geq -\mathcal{M}$"

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a methodology for verifying agreement in neural network that try to approximate the same target function.
The proposed method focuses on the predicted likelihood-ratio between two classes (denoted as OM). In particular, it gives local bounds on the difference in log OM between the two networks (log LROM). The bounds are given for local neighborhoods, assuming that the correct label is known and constant in the region. The bounds on log LROM are obtained relaxing the exact optimization objective to an approximate one, solvable with linear programming. 
The paper evaluates the proposed approach on a variety of scenarios, comparing distillation and quantization techniques, as well as evaluating the robustness of adversarial trained networks.

### Strengths
The paper is well structured, clear and straight to the point. The contribution is well laid out, and the examples for the empirical evaluation are rich, relevant and diverse.

### Weaknesses
The proposed metric of ROM represents the difference in prediction confidence, and does not necessarily relate to the agreement of the predictions. The LROM metric is only informative when the bounds do not contain zero. Moreover, even assuming a point has verifiable LROM, it might not be verifiable in the desired direction.

Moreover, the correctness of the LROM metric depends on the assumption that the correct label remains constant in the considered region. Therefore it is only sound for small enough neighborhoods. Looking at the empirical results, in many scenarios, the percentage of verifiable points rapidly drops to zero as the neighborhood size increases. 
It is unclear if the proposed approach provides a qualitatively different result than a direct pointwise comparison of model predictions.

### Questions
The authors point out that having a strictly positive/negative LROM between two networks is a sufficient condition to ensure that one makes better predictions than the other. I understand that ROM as formulated has the advantage of being invariant to the choice of threshold, but I find it paints an incomplete picture, and can be misleading. In particular, two networks can have 100% compatible predictions, yet the ROM value could vary significantly. Similarly, the same ROM can represent drastically different situations. In fact, if the two networks have log OM of +0 and +10, we are comparing a coin toss to an extremely accurate predictor. This is not the same as having two extremely confident networks with log OM of +1000 and +1010, but both situations have log ROM of +10.

The discussion on the effectiveness of adversarial training is interesting, however I can't seem to find any plot/table of the results described in the main text.

I also would be interested in a more in depth discussion of the effects of the $\delta$ parameter on the metric. Clearly for small enough values, the approach reduces to a pointwise comparison of model predictions. To justify the approach, it should be shown (at least empirically) that evaluating LROM gives significantly different results.

The choice of the correct $\delta$ seems critical. If it is too large, the metric becomes meaningless and the number of verifiable points is likely to drop. Can you provide (at least) some heuristic to quantify a good value for $\delta$?
Also, have you considered making it a function of $x$, trying to estimate the largest local region where the correct label remains constant?

### Soundness
1

### Presentation
3

### Contribution
2
