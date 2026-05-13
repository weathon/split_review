# Implicit Neural Representation Inference for Low-Dimensional Bayesian Deep Learning

- Decision: Accept
- Scores: 5, 5, 5, 8

## Abstract
Bayesian inference is the standard for providing full predictive distributions with well calibrated uncertainty estimates.
	However, scaling to a modern, overparameterized deep learning setting 
	typically comes at the cost of severe and restrictive approximations, sacrificing model predictive strength.
	With our approach, we factor model parameters as a function of deterministic and probabilistic components;
	the model is solved by combining maximum a posteriori estimation of the former,
	with inference over a low-dimensional, Implicit Neural Representation of the latter.
	This results in a solution that combines both predictive accuracy and good calibration,
	as it entails inducing stochasticity over the full set of model weights while being comparatively cheap to compute.
	Experimentally, our approach compares favorably to the state of the art,
	including much more expensive methods as well as less expressive posterior approximations over full network parameters.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a hypernetwork-based inference mechanism for BNNs, focusing on two key aspects: first, they want the hypernetwork to be compact and reusable across the main network; second, they perform approximate Bayesian inference over the compact hypernetwork. A key part of this work is the fact that the authors also keep around deterministic weights which are modulated by the stochastic nuisances sampled from the hypernetwork, allowing them to maintain good performance.

The method appears to be competitive in experiments.

### Strengths
The authors propose a relatively narrow idea: making a small hypernetwork probabilistic and sharing it across the network.

What I like about this paper is the good exploration over ways to do this: the authors both try Laplace approximations, and stochastic weight averaging as pragmatic means to parametrize an approximate posterior over the hypernet. They also propose to use normalizing flows to shape the outputs of this hypernetwork to squeeze a bit more performance out of it.

Empirically, the work shows good performance.

The paper is overall well written and easy to follow and understand.

I also want to call out that the authors are good scholars, the breadth of relevant work cited here is comprehensive and commendable.

### Weaknesses
The elephant in the room with this paper is that it is very narrow in its contribution.

Tiny shared hypernernetworks parametrizing individual implicit weight outputs via coordinate systems go as far back as the cited paper Karaletsos et al 2018. Bayesian inference over such hypernetworks has likewise been performed before, in the shape of GPs and BNNs which the authors both cite in their related work.
Blending deterministic and stochastic weights coming from hypernetworks also has been done, again cited absolutely correctly by the authors in numerous papers.

The contribution I see here is not the novelty of any of the ideas then, but the specific engineering combinations tweaked to obtain good performance. For example, executing on practical pieces like Laplace for the hypernetwork or SWA and pairing that object with normalizing flows is good execution that probably helps with performance compared to previously mentioned works.

The core weakness remains that the paper presents a combination of existing techniques without a clear, substantial novelty in the underlying methodology. The empirical results, while promising, do not sufficiently elevate the work beyond an engineering exercise. The specific choices, such as the use of Laplace approximation or SWA, are not inherently novel and are applied in a fairly standard manner. The use of normalizing flows, while a good practical choice, does not represent a significant conceptual leap. The paper lacks a theoretical contribution that would justify the specific combination of techniques, and it does not provide a deep analysis of why this particular combination works better than other plausible alternatives. The performance gains, while present, are not so substantial as to overcome the lack of methodological novelty.

### Questions
Given the relative dearth of new ideas in this work, I would like to identify its strengths in execution and overall quality of the work.

Could the authors argue that their specific combination of techniques could be applied to a larger neural network, i.e. an imagenet model?

Could the authors share a bit more about scalability and performance/memory constraints/ number of forward passes needed to obtain good performance?

I would enjoy seeing more evidence that highlights the merits of the execution here, given the relatively modest technical contributions.

As the paper stands, I would find the contributions somewhat thin, but I would enjoy seeing this line of work with hypernetworks for BNNs be paired with a very strong empirical result in the style I ask for above to enrich the community and hope the authors can find something more to show that differentiates this work more from e.g. Dusenberry et al. empirically, which can also be interpreted as a specific hierarchical weight model (with layer-specific structure).

Again, I commend the authors for their quality scholarship and would enjoy more sound arguments to place this work into the trajectory of papers they have mentioned as a primarily empirical contribution.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a new framework for approximate Bayesian inference in neural networks based on low-dimensional hypernetwork representations of weight perturbations. In this framework, hypernetworks take in weight coordinates as input and output perturbation factors for each weight. An approximate posterior is fitted for the hypernetwork and perturbations are repeatedly sampled and multiplied with the main network weights to perform Bayesian model averaging. Three alternative Bayesian hypernetworks are considered: sinusoidal representation networks (SIRENs) with Laplace and SWA-Gaussian approximate posteriors, and normalizing flows with Real Non-Volume Preserving (RealNVP) transformations. The posteriors are benchmarked on UCI regression and gap datasets, and out-of-distribution (OOD) detection is tested on CIFAR-10 image recognition.

### Strengths
- The proposed framework introduces a novel combination of approximate Bayesian inference and implicit neural representations as hypernetworks which, to the best of my knowledge, has not been explored in prior research.
- The paper offers valuable insights, e.g. in considering the benefit of multiplicative over additive perturbances, and in finding that CNN models benefit from shared representations.
- The evaluation of out-of-distribution (OOD) detection on the CIFAR-10 dataset is thorough and detailed. This plays a large role in showing the practical utility of the proposed approach.

### Weaknesses
Regarding the method:
- The derivation of the Laplace approximation is confusing: In Equations (4) and (5) a Laplace approximation with full Hessian is derived. While a full Hessian for the hypernetwork weights may be tractable for small enough networks, this approximation does not correspond to the closed form posterior of Equation (7). This closed form corresponds to linearized Laplace inference with generalized Gauss-Newton (GGN) approximation to the Hessian. It is unclear if the model evaluated in the experiments uses a full Hessian or the GGN approximation with closed form. Furthermore, the text does not explicitly state whether any additional approximations, such as Kronecker factorization, are employed in the computation of the GGN.
- The use of SIREN activation suggests that the hypernetworks need to model high frequency representations of the weight perturbations. The SIREN models presented in [Sitzmann et al., 2020] benefit from consistency and repeating patterns in the signals they are fitting, making interpolation easier. There might be some form of structural consistency in neighboring weight perturbations for CNN kernels, but it seems unlikely for the weights of linear layers. I also expect that RealNVP hypernetworks have a harder time fitting high frequency representations when comparing to SIREN. This matter is only very briefly brought up in the discussion of Figures 9 and 10.

Regarding experiments:
- The methods are benchmarked against a last-layer Laplace approximation, however a block-diagonal Kronecker-factorized (KFAC) Laplace approximation should also be considered since this corresponds better to a full network variant in the linearized Laplace family of approximations. The current baseline does not provide a strong comparison against a full network approximation.
- Both theoretical and experimental runtimes and memory requirements are not discussed. It is unclear if the proposed models take significantly more time for training or inference, since in theory a forward pass of the hypernetwork is required for every "main" network weight. The paper should include a more detailed analysis of the computational cost, including the time taken for both training and inference, as well as the memory footprint of the proposed method. Specifically, it should be clarified how the weight coordinates are batched during the hypernetwork forward pass and if a single pass with all coordinates is feasible or overly expensive.

### Questions
- Does the INR-Laplace model in the experiments employ a full Hessian or a GGN approximation? Do you make any additional approximations (e.g. Kronecker-factorization) ?
- Can you further evaluate the effect of INR network size on model performance and quality of the uncertainty estimates? Figure 1 already does this for CIFAR-10 but it would be interesting to see for MLPs on UCI and UCI-gap datasets, with INR-Laplace and INR-RealNVP, and perhaps on wider sets of network sizes. Would also be helpful to include error bars for these figures.
- Have you tried using ReLU hypernetworks? Do these fail to recover high frequency representations of the perturbations compared to SIREN?
- Do you have an intuition for why multiplicative perturbations are so successful compared to additive perturbations of the weights? Perhaps uncertainty is improved when perturbations are scaled up by the magnitude of the weight?
- Is there a reason for INR-SWAG appearing in some experiments and INR-Laplace in others?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes so-called implicit neural representation inference for Bayesian Neural Networks. In the past, several "subspace" inference frameworks have been devised, where the aim is to only model smaller part of the weight space in a Bayesian manner. This type of approaches promise to better scale the approximate Bayesian inference for deep learning, while making the inference procedure more accurate. Building upon, this paper proposes to obtain the "subspace" of weights using implicit neural representation. The paper shows how the proposed method can enhance popular frameworks such as Laplace Approximation, SWAG and normalizing flows. Experiments are conducted on UCI, cifar10 and cifar100 and the approach is compared against the baselines with performs inference over all the parameters of neural networks, as oppose to the subspace.

### Strengths
In my view, the paper has the following strengths:

- the idea of using implicit neural representation for improving Bayesian Neural Network is interesting and novel.

- Implicit neural representations are currently a popular topic, and may be therefore relevant to many researchers.

### Weaknesses
On the other-hand, I think the paper has several rooms to improve for a publication.

- The paper could improve in terms of its clarity.

Specifically, I find it difficult to parse section 3.1. I get the problem statement, but the parts on implicit neural representation with the SIREN model was difficult to understand. It would help to have a figure on this since there are many notations introduced. The text contains many mathematical symbols, which would have been explained differently. 

SIREN should be explained more in depth since I think it is an important technical detail. Also, some technical details on how implicit neural representation is obtained, and the general working principles, like an algorithm behind, would be helpful for the reader.

- Experiments may become more solid with other choices of baselines and datasets.

First, there has been many subspace approaches and also many approaches that attempts to sparsely represent model uncertainty. Some examples are references in the paper: Kristiadi, Dusenberry, Daxberger, etc. I think the experiments should compare to these baselines as well, which can really show the advantages of implicit neural representation over existing methods within the same class of approaches. Comparisons to full weight space seem not natural.

Moreover, the paper uses UCI and CIFAR as main datasets. I would have liked the paper more if "uncertainty baselines" from google was used, as such works represent the more upto date standard in experimental protocol. Speaking of the protocol, the included baselines seem not very consistent, e.g., Figure 1 misses laplace approximation, figure 2 again selectively reports INR Laplace and contains no SWAG, figure 3 misses swag, INR swag, etc.  

Overall, I recommend a weak rejection. Improving the technical quality and clarity of the presentation would be meaningful here.

### Questions
1.In line with section 3.1, is it possible to explain why INR is advantages to learn the subspace?  I could not get why it might be a good idea.

2. Another question is on expressiveness Vs accuracy of the Bayesian inference. Basically, the weight space is very large. Having a simple distribution in such a complex high dimensional space can be already advantageous in terms of expressiveness of the probability distribution. Of course, a natural direction has been also improving the expressiveness through structured distribution, correlations amongst layers, etc. On the other hand, what these subspace approaches do is to model with smaller part of the network, which can actually reduce the overall expressiveness of the distribution, though overall inference might be easier and accurate. Then the question is, when should we look into the approaches for expressiveness, and when should we look into the subspace approaches?

3. Why not only take last few layers of the network and make them probabilistic? What are advantageous of using INR against very simple baselines as taking last one or three layers? I think it might be interesting to include them as a baselines in the experiments.

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
The authors propose an approximate inference method for Bayesian neural networks. The idea is to introduce a second (auxiliary) network which computes an approximate posterior over the multiplicative noise applied to the deterministic weights of the main network. Such a multiplicative noise then induces an approximate predictive posterior distribution of the main network, they key object of interest in BNNs. The auxiliary network can be of much smaller size than the main one, and an approximate posterior over its weights can be approximated using one of the existing methods (e.g. Laplace, SWAG, Normalising Flows). The proposed method is shown to be competitive in comparison to a number of baselines.

### Strengths
+ An interesting approach to approximate BNN inference showing competitive performance
+ Clear presentation, the paper is easy to follow

### Weaknesses
The baselines used for comparison (Dropout, BbH, Ensembles) are relatively old methods (by Deep Learning standards of course). I'd be very interested to see how the proposed method compares to more modern approaches, e.g. those applying Laplace approximation directly on to weights of the main network.

A couple of minor points:
- Typo in the second to last line on page 3 (wf).
- Typo in Eq. (5) (w_{INR} should be in the subscript I guess?)

### Questions
- I wonder about the integer inputs (i.e. the tensor coordinates) to the INR network. Do you normalise these coordinates somehow or directly input the integers into the INR network? Did such an integer input space cause any problems during training?
- Why do you think that sinusoidal activations are particularly suitable for the INR network? Do you expect the result to deteriorate if you used other activations (e.g. sigmoid)? 
- Why do you think the INR with 350 outperformed 4k and 10k versions on CIFAR in Fig. 1?
- I was very interested to see that the predictive uncertainty in Fig. 2 has a stationary structure (i.e. dependent on the distance from the observations) similar to a GP with a stationary kernel. The Dropout and Deep Ensembles baselines clearly don't have such a property, but I wonder how such a figure would look like if we used a Laplace approximation directly on some layers of the main network (without INR), e.g. similar to Kristiadi et al. (2020)? In other words, I wonder how specific this stationary uncertainty structure is to the inference using an auxiliary network?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
