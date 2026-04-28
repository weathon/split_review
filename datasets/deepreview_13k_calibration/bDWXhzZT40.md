# Learning model uncertainty as variance-minimizing instance weights

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Predictive uncertainty--a model’s self-awareness regarding its accuracy on an input--is key for both building robust models via training interventions and for test-time applications such as selective classification. We propose a novel instance-conditional reweighting approach that captures predictive uncertainty using an auxiliary network, and unifies these train- and test-time applications. The auxiliary network is trained using a meta-objective in a bilevel optimization framework. A key contribution of our proposal is the meta-objective of minimizing dropout variance, an approximation of Bayesian predictive uncertainty, We show in controlled experiments that we effectively capture diverse specific notions of uncertainty through this meta-objective, while previous approaches only capture certain aspects. These results translate to significant gains in real-world settings–selective classification, label noise, domain adaptation, calibration–and across datasets–Imagenet, Cifar100, diabetic retinopathy, Camelyon, WILDs, Imagenet-C,-A,-R, Clothing-1.6M, etc. For Diabetic Retinopathy, we see upto 3.4\%/3.3\% accuracy & AUC gains over SOTA in selective classification. We also improve upon large-scale pretrained models such as PLEX.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose an instance weighting methodology based on an auxiliary network that quantifies the uncertainty of the predictor subject to learning. More precisely, a bilevel optimization formulation enables one to simultaneously learn the predictor and the auxiliary uncertainty quantifier, whereas a meta-level loss enforces to reduce the predictor’s uncertainty by minimizing a variational approximation of Bayesian Neural Networks by means of multiple inference passes employing Dropout regularizations. As the authors show, the method proves to be an effective means to achieve a more uncertainty-aware, and consequently better generalizing predictors.

### Strengths
- Strong empirical evidence of the reasonability of the method. Also, the experiments are at an impressive scale, supporting the claims of the work.
- Rich set of recent baselines considered in the experiments, fair comparisons.
- I really like that this method allows for augmenting previous robust approaches, e.g., PLEX, with the proposed solution. That significantly boosts its applicability.
- Computational efficiency concerns are thoroughly addressed in the appendix.

### Weaknesses
Major:

- The contribution and distinctions to previous works (which e.g. also use a bilevel optimization formulation for reweighting) should be made more clear in the thread of Section 3. Often, it does not become clear when something is new in the course of the ReVaR proposal, and when previous works are revisited. Specifically, the novelty of instance-conditioning and the meta-regularizer for variance minimization should be explicitly highlighted and contrasted with existing bilevel optimization techniques for reweighting. The current presentation blurs the lines between what is novel and what is adopted from prior work, making it difficult to assess the true contribution.
- Many grammatical and orthographic issues, e.g., missing articles (“*the* dataset” → motivational questions in Section 1), misplaced words (“captures captures” → beginning of Section 5), …
- Section 4 is very hard to read, some design choices also appear arbitrary. For instance, intuitively, what is the role of $X_c$, $X_e$, $W_c$ and $W_e$, and why are the dimensionalities chosen as described in the paper? The motivation behind partitioning the input space into $X_c$ and $X_e$ is unclear, and the connection to the different noise scenarios is not well-established. Furthermore, the specific dimensionalities of these variables and the weight matrices $W_c$ and $W_e$ seem arbitrary without a clear justification. Elaborating more on the setup would help to better understand the settings and allow for estimating the significance of these results.

Minor:

- Sometimes unclear / inconsistent notation, e.g., “p=w=g(x)” in  Section 1.1, also see my previous comment on $X_c$, $X_e$, $W_c$ and $W_e$.
- As far as I can see, there is no code served along with the paper, which does not support the reproducibility of this work.
- Section 4, Scenario 1: „?“ Broken reference
- Details about the U-score model architecture appear in the appendix only – as this is not as trivial as “normal” predictors, this should be already hinted at in the main paper.

### Questions
1. While Section 4 gives a comprehensive overview of different forms of captured uncertainties in $g_\theta$, I would be also interested in seeing concrete learning behaviors of $g$ in the real-world experiments. Perhaps the authors could augment the results by showing patterns of $g$ in this regime, e.g., by plotting the distributions of the learned weights, and how these evolve over the training. Right now, it is hard to get an impression about the learning dynamics, raising the following questions: Does the novel meta loss slow down the training by making it more cautious, or does it even accelerate the training? Note that I am not referring here to what has been discussed in E.3, but with the focus on learning curves. For instance, setting the maximum number of epochs / data points to control training costs is often a critical consideration in real-world application at larger scales.
2. Could the U-SCORE and predictor weights be shared? How would this affect the training?

### Soundness
4 excellent

### Presentation
2 fair

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
The paper proposes a method which learns a weighting function for the cross entropy loss, enabling re-weighting of the terms depending on how difficult (in an uncertainty sense) they are to classify. The method is learnt through a bi-level optimisation process, which is not dissimilar from a 'meta' training objective. The authors demonstrate their results on several datasets using ResNet-50 architectures.

### Strengths
The strengths of this paper are it's:
* Simplicity, the method seems very easy to implement and is intuitive to understand.
* The experiments are reasonably conclusive and operate on a significant number of datasets.

### Weaknesses
In terms of weaknesses:
* The paper seems quite rough, there are many undefined terms and functions ($R^2$, $g(x)$, $G$), missing citations (MMCE), lack of error bars in Table 4 - 7, etc.
* With a paper being set up the way it has, I would expect some proof, especially with the synthetic setup in Section 4
* Moreover, I'm not entirely convinced on why this method works, my understanding is that you are simply training the network to produce low variance in its predictions, which is manifested by the network essential learning dirac distributions over the parameters in dropout. It would be nice to see some investigation into this, or at least an explanation.
* Only performed on ResNet, there are many models available now which can be trained just as easily with similar compute.

### Questions
* What is the definition of $g(x)$? And how does this relate to $\theta$. I couldn't find this information when it was introduced, which made this paper very hard to grasp what was happening.
* How do $w_i$ and $\Theta$ relate?
* What is the theory in Scenario 1?
* What are the associated issues with this approach? I understand the objective of minimising uncertainty, but minimising the metric which provides the uncertainty is not the same thing. I'm concerned that all this is doing is simply collapsing the dropout distribution to all become the same parameters, i.e. it makes no difference on the prediction which parameters are selected. 


Whilst I think there is some contribution in this paper, I just don't think in it's current form it's ready for publication. I would suggest that the authors improve:
* The quality of the paper to make it easier to understand what the method is, i.e. define $g(x)$ properly
* A proof would strengthen the paper significantly. If you can prove why minimising the variance provides improved uncertainty you're onto a winner.
* Add more architectures, using only ResNet-50 is not enough.
* I would also suggest removing the empirical evaluation on the top set up. If you have a toy set up like this, it should turn into a proof.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose ReVar technique for predicting model uncertainty at train and test time. In particular, ReVar is notable for aiming to capture various different sources of uncertainty, including covariance shift and high label noise. ReVar uses bi-level optimization to learn both a primary model f(x) and auxiliary uncertainty model g(x), which serves as an instance-dependent weight function for training data and an uncertainty score. The technique is evaluated favorably against prior works, both on synthetic data and on real datasets for many tasks including calibration, data with label noise and selective classification.

### Strengths
- The general premise of an all-purpose uncertainty evaluation tool, useful for both train and test time and adaptive to various sources of uncertainty, is a significant and original contribution that would be very useful
- The evaluation against prior works on a variety of uncertainty-related tasks is very comprehensive
- In section 4, the classifications into types 1-3 uncertainty and discussion of how instance weights should respond to these types was a useful step towards putting these different uncertainty problems under one theoretical framework

### Weaknesses
 - Section 4's work with synthetic data has good potential to be interesting and illustrative of how ReVaR works differently in desired ways for different uncertainty types. However, I found it unclear how the "theoretical ideal for the instance dependent weights" listed in table 1 were determined. Some more information on their derivation might be helpful.
- Occasional minor notational things: Equation 3, definition of $\theta^*$, should $g_\Theta$ might instead be $g_{\Theta^*}$. The text following/explaining equation 6 introduces variables not used in equation 6; some minor rewriting could be useful here. Missing reference to a theory in section 4, scenario 1.

### Questions
- How were the targets in table 1 derived; why are these targets desirable?
- In distribution shift settings where we assume access to a validation set from the test distribution, is it not better sometimes to just fine-tune on the validation set (or a portion of it)? It could potentially be a good baseline comparison.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
