# Privacy at Interpolation: Precise Analysis for Random and NTK Features

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Deep learning models often memorize the training set. This makes them vulnerable to recovery attacks, raising privacy concerns to users, and many widespread algorithms such as empirical risk minimization (ERM) do not directly enforce safety guarantees. In this paper, we study the safety of ERM models when the training samples are interpolated (i.e., *at interpolation*) against a family of powerful black-box information retrieval attacks. Our analysis quantifies this safety via two separate terms: *(i)* the model *stability* with respect to individual training samples, and *(ii)* the *feature alignment* between attacker query and original data. While the first term is well established in learning theory and it 
is connected to the generalization error in classical work, the second one is, to the best of our knowledge, novel.
Our key technical result characterizes precisely the feature alignment for the two prototypical settings of random features (RF) and neural tangent kernel (NTK) regression. 
This proves that privacy strengthens with an increase in generalization capability, unveiling the role of the model and of its activation function. 
Numerical experiments show an agreement with our theory not only for RF/NTK models, but also for deep neural networks trained on standard datasets (MNIST, CIFAR-10).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper analyzes the stability of generalized linear regression, and derives bounds on it, for two classes of models: random features, and two-layer networks in the NTK regime.
The paper also attempts to make a connection between these bounds and the success rates of a certain type of attacks, in which the attacker has partial access to the training example (e.g. background of an image), and seeks to recover the label.
Numerical experiments are provided, and focus on measuring the attack's accuracy and the model's generalization, showing the two are anti-correlated.

### Strengths
The main strength in the paper are the bounds it provides on stability of generalized linear models in the two settings of interest (random features and NTK). These bounds appear to be new. Lemma 4.1 decomposes stability into a term that involves the hat matrix (that the paper calls "feature alignment") and a term related to the model's generalization.

The paper is clearly written and the assumptions clearly stated and explained (although it would have been nice to be more upfront about certain assumptions early on, e.g. invertibility of the kernel, which requires $p \geq N$, a restrictive assumption).

The experiments give a nice illustration of the intuitive claim that attacker's success decreases with generalization.
I also commend the authors for including their code with clear instructions for reproducing the results. They clearly put effort into this.

### Weaknesses
The main weakness of the paper is its attempt to characterize "privacy". This is discussed in the paragraph "Generalization and privacy", and the only argument made there is that the attacker's recovery loss can be bounded below (eq. 12) by a quantity that depends on $\gamma_\phi \sqrt{R_{Z_{-1}}}$ (where $R$ is a generalization term, and $\gamma_\phi$ is the feature alignment term that the paper proceeds to bound).
The issue is that this lower bound ignores several terms, some of which are important (in particular the variance of $f(z_1^m, \theta^*)$. The lower bound of eq (12) is inadequate to really characterize the attacker's power. Specifically, the bound does not account for the inherent variability in the model's predictions, which could significantly impact the attacker's success. A more comprehensive analysis should consider the full distribution of $f(z_1^m, \theta^*)$ rather than just its mean.

Furthermore, there is *not a single formal result on privacy* stated in the paper. This was very surprising to me, given the many claims made about privacy guarantees. To cite a few:
- "Our analysis provides the first theoretical privacy guarantees for ERM algorithms interpolating the data."
- "The combination of Theorem 5.4 and Lemma 4.1 shows the proportionality between stability and privacy."
- "We provide a quantitative characterization of the accuracy of a family of powerful information recovery attacks"

I disagree with all of these claims. The paper only gives an informal, qualitative argument about attack success, together with nice experiments. There are no formal guarantees about privacy. In summary, I think this is a good paper on stability analysis. I don't think it's a good paper on privacy.

Another area that should be improved is connecting the results with prior work. There is a brief mention of related work on stability in Section 2, but no further attempt is made to compare/contrast the results in this paper (in particular Lemma 4.1). Beside, stability in linear regression is a classic topic, it goes back much further, see for example [1]. The projector matrix defined in the paper is known as the hat matrix, and its role in stability is well studied. For example [1] gives a similar expression of stability involving the hat matrix. Though not identical to Lemma 4.1, they are closely related, and it's important to make that connection and discuss differences. I invite the authors to do a more careful review of the topic. The paper should also discuss the limitations of the analysis, especially the assumption that $p \geq N$ which is needed for the kernel invertibility, and how this assumption impacts the applicability of the results.

### Questions
- Would the authors be willing to recast the paper as a study of stability rather than privacy? I'd be more inclined to accept the paper in that case. (in particular, removing all claims about quantitative or formal privacy guarantees, removing privacy from the title, etc. It's fine to keep the empirical results.)
- Can the authors carefully review work on stability in linear regression? In particular connections to [1] and related work.

===== post rebuttal =====
I thank the reviewer for their detailed response, for exploring the connection with [1], and for their willingness to rework the presentation.
I have raised my score to 6.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the safety of ERM model under interpolation. Specifically, the authors consider the settings where the adversary has access to the masked sample of the actual data used by the deep learning model. They characterize the effectiveness of this attack via two quantities: model stability with respect to the training sample and the alignment between the masked sample used by the attacker and the actual data.

### Strengths
- The paper provides quite an interesting insight into the privacy of deep learning models. While most previous works focus on stability under the lens of differential privacy, this work focuses more on how strong some certain attacks are depending on the resources available to the adversary. While its main conclusions are pretty much in line with previous work (a model that generalizes well is less affected by attackers), the paper still has a significant enough contribution by quantifying the level of impact of feature alignments and stability in specific settings such as Random Features and NTK.

- The paper shows that ERM model that generalizes well has some intrinsic privacy protection.

- The paper is pretty well-written overall and the proof sketch is appreciated since the detailed analysis is fairly dense and not easy to follow.

### Weaknesses
 - The paper would probably benefit from having a section that describes and discusses the results of the experiments. Though the results in sections 5 and 6 are pretty interesting, they are also quite similar. Maybe the authors can consider cutting the proof sketch of section 6 and adding some discussion on the results of the experiment. 

- I also think some discussion on the results of Theorem 5.4 and Theorem 6.3 are needed. At first glance, the main conclusion that we can get from the results is the feature alignment value would converge to some constant that depends on the norm of the background $d_y$ (which is easily interpretable) and the $l-$th Hermite coefficient of the activation function (which is not that intuitive).

- I'm probably missing something but if the feature alignment $F_{RF}$ is in $[-1,1]$ and $0 < \gamma_{RF} <1$, the results in 5.4 doesn't seem to convey too much information? The result basically says these 2 values are a constant away from each other.

### Questions
- In the experiments, the activation function that is composed of the Hermite polynomial is only used for experiments with synthetic data, is it possible to run that activation on real datasets? Also, how did the author create the synthetic data?

- I think the experiments right now mainly support that generalization improves privacy but it's quite hard to see where the feature alignments part comes into play here. Maybe the authors can try varying the level of alignment or $\alpha = d_y/d$ to see how it affects the attack's efficiency.

- I'm probably missing something but if the feature alignment $F_{RF}$ is in $[-1,1]$ and $0 < \gamma_{RF} <1$, the results in 5.4 doesn't seem to convey too much information? The result basically says these 2 values are a constant away from each other.

### Soundness
4 excellent

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper discusses a specific form of reconstruction attack in which part of the input is masked (substituted with other data from the same distribution) and the model predicts the label. The model is a generalized linear model trained to minimize quadratic loss. With a lot of additional restrictive assumptions they derive a relationship between the model stability (sensitivity to removal of one point) and privacy (difficulty in reconstructing the true label of the masked input).

### Strengths
Aside from some typos and slight conceptual inclarities, the mathematical exposition is crystal clear. The setup and results are to my knowledge original (although I don't have an encyclopedic understanding of this kind of theory). The insight from the theorems is mildly interesting (but as I understand applies in a very narrow setting, and also is not really surprising, see weaknesses).

### Weaknesses
My main problem with the paper is that it seems to be an extremely limited scenario: linear model with squared error and invertible kernel. Why is this kind of model of use in the current era? The attack also seems quite specific. A narrow example is given (a person in a compromising environment) but do the conclusions of your method apply to more general forms of realistic attacks? How? Specifically, the reliance on an invertible kernel seems particularly restrictive, as many practical kernels are not invertible, and the analysis appears to hinge on this property. It is unclear how the results would translate to scenarios with non-invertible kernels or more complex non-linear models.

Second, I feel that differential privacy has been generally accepted as the gold standard for privacy, and there are carefully reasoned arguments for this choice. You use the word "privacy guarantee". Why should we be interested in this new notion of privacy? Could you relate your ideas more to DP? It would be beneficial to explicitly discuss the relationship between the proposed notion of privacy and differential privacy, highlighting the differences and potential connections. The paper should also clarify the specific advantages of this new notion of privacy, especially when compared to the well-established framework of DP.

The intro says "the accuracy of the attack grows with generalization error". If this is the main point of the paper, it seems, if not trivial, not especially surprising. A model that can perfectly fit the data and has high generalization error clearly can easily memorize arbitrary points, which means privacy is low and the attack should be easy. The paper should provide a more nuanced discussion of this relationship, perhaps by exploring specific scenarios where the connection between generalization error and attack success is not straightforward. It would also be helpful to provide a more precise definition of what constitutes a 'successful' attack in this context.

Minor comments:
* I wouldn't say most popular applications achieve "0 training loss"; *maybe* "0 training error"
* typo "explicitely"
* Typo in citation "Milad et al." (should be "Nasr. et al")
* "$g_z$ denotes the ground-truth label of the test sample" Before you just said that $g_i$ is a function of sample $z_i$, maybe clearer to just define a label function $g(z)$.

### Questions
Questions already mentioned in Weaknesses section.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair
