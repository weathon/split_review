# Wide Neural Networks Trained with Weight Decay Provably Exhibit Neural Collapse

- Decision: Accept
- Scores: 6, 8, 8, 8, 8

## Abstract
Deep neural networks (DNNs) at convergence consistently represent the training data in the last layer via a highly symmetric geometric structure referred to as neural collapse. This empirical evidence has spurred a line of theoretical research aimed at proving the emergence of neural collapse, mostly focusing on the unconstrained features model. Here, the features of the penultimate layer are 
free variables, which makes the model data-agnostic and, hence, puts into question its ability to capture DNN training. Our work addresses the issue, moving away from unconstrained features and studying DNNs that end with at least two linear layers. We first prove generic guarantees on neural collapse that assume \emph{(i)} low training error and balancedness of the linear layers (for within-class variability collapse), and \emph{(ii)} bounded conditioning of the features before the linear part (for orthogonality of class-means, as well as their alignment with weight matrices). We then show that such assumptions hold 
for gradient descent training with weight decay: \emph{(i)} for networks with a wide first layer, we prove low training error and balancedness, and \emph{(ii)} for solutions that are either nearly optimal or stable under large learning rates, we additionally prove the bounded conditioning. Taken together, our results are the first to show neural collapse in the end-to-end training of DNNs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Dear authors, thank you for submitting your work to ICLR 2025. The paper considers the phenomenon of 'neural collapse' and attempt to extend current rather special case results to brader class of networks, specifically, a deep neural (non-linear) networks with a wide first layer, funnel architecture and several, i.e. 2+, linear layers (head) before the output. After taking several assumptions, paper shows in series of Theorems (3.1, 4.4,5.2) and Propositions (4.5, 5.1,5.3) that GD training with weight decay (under further assumptions) leads to within class variability collapse (NC1). Results are supported by experiments on MNIST and CIFAR and MLP and ResNet + MLP head.

### Strengths
S1: Novelty, pushing for (more) general results on timely and attractive topic of 'neural collapse' in DNN training
S2: Striving for a theoretically solid argumentation stating necessary assumptions (in Theorems and Propositions) and as Assumtions 4.1, 4.2, 4.3 ...
S3: Well done Introduction positioning paper within existing works (UFM, NTK and other specific results)

### Weaknesses
W1: Accessibility of the paper for a '15 mins' reader. The main results are formulated using (Abstract, l19) 'balancedness', (Abstract, l20) 'bounded conditioning' and other only later defined phrases and makes it hard to asses the attractivity/usefullness of paper unless reading it whole. It is recommended to rework (the Abstract at least, if no Conclusions are present) to make it clear and self-sustained.

W2: Quite a few assumptions are required in general. More over thay are added along the way, e.g., Assumption 4.2, $|\sigma(x)| \leq |x|$, etc., (which is ok, but also narrows the applicability of the final result). Some of those are very technical (especialy those in Theorems, such as in Theorem 3.1, (2),(3), (4)) but as well Assumption 4.3, Theorem 4.4. (10) and more) and with paper specific notation to learn, e.g., $\lambda_{3 \rightarrow L}$. It would help paper to have an thorough discussion on applicability/limitations of these assumptions. Perhaps at expense of shortening some 'proof sketches' refering them to SM?

W3: 'Discussion and Conclusion' sections are not presented. This is most likely due to space constrained and will be added in case of acceptance (?). Yet, I find it impacts the paper quality negatively. Especially in a light of the previous (W2) comments, the discussion and conclusions could have brought a critical 'back to reality' summary. Idealy it would bring more intuition for results and their application. Yet, I find it very important to have such Discussion reviewed before publishing ...

W4: Some references are rather inaccurately interpreted/generalized too much perhaps. For instance the lines 399-400 "...Thankfully, instead of simply diverging, for large η (but not too large) the parameters naturally end up at the ‘edge of stability’: the top eigenvalue of the Hessian is close to $2/\eta$ , i.e., the threshold below which GD is stable..." from (Cohen et all. 2021). Referenced work provides only experimental evidence for a phonomenon and only approximately, i.e., for certain settings operator norm of Hessian exceeds 'stability threshold' $2/\eta$, etc. Than approximation used on l410, especially $O(\epsilon_1)$ is only valid if $\nabla^2_{\theta} Z_L$ norm is bounded, which is ok for NTK regime, but not necessarily for large learning rate regime. Or is it?

W5: Following up on W4, Proposition 5.3, and other Theorem combine NTK with large learning rate regime, which sounds dangerous. Also requirement on wide first layer, suggest a NTK limit case is required. Could authors clarify a bit more on this relation?

Overall, I find it to be a solid attractive paper with technically legit reasoning, taking few shortcuts (some noted above) and with missing discussion and conclusions. I suggest authors to work on alleviating weaknesses and discussing limitations to improve contributions of this interesting work significantly.

### Questions
See Weaknesses for the most concerning questions. 
Additionaly:

Q1: Line 188: "... aproaches 1 ..." Shouldn't it be "... aproaches 2" based on (3)? Is it still sufficient for orthogonality claims (can the proof be adjusted to account for it)?

Q2: Proof sketch of Theorem 4.4., lines "306". Why and how is are "two phases" guaranteed to happen during GD training?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper presents an interesting theoretical advancement in understanding neural collapse in practical, end-to-end training scenarios, moving beyond the unconstrained features model. The authors provide a rigorous demonstration that neural collapse arises in networks with linear layers appended to a nonlinear backbone, given conditions of interpolation and balancedness. They show that these conditions hold for sufficiently wide networks trained with gradient descent and L2 regularization. The empirical results further support the theoretical findings, showcasing the robustness of neural collapse across various architectures and datasets.

### Strengths
This work provides an interesting theoretical insight on the role of training algorithm in the emergence of neural collapse, which I found especially exciting, and I think it opens up new directions for understanding the generalization properties of deep learning models.

### Weaknesses
In my opinion, this is a solid paper and I can not think of a weakness.

### Questions
In Figure 3 the authors' numerical results show that non-linear layers are increasingly linear, as the depth of the non-linear part increases. Could the authors provide more insights into how this observation relates to their theoretical results and the mechanisms driving this increased linearity?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides theoretical evidence for end-to-end training of true deep neural networks. This is contrary to previous works which primarily rely on the unconstrained features model. The paper provides explicit bounds on NC1, NC2 and NC3 for both globally optimal ($\ell_2$) regularized deep neural networks as well as neural networks trained with gradient descent. The results provide new insights on the role of additional linear layers, weight decay regularization and large learning rates with respect to neural collapse.

### Strengths
- The authors provide the first theoretical analysis of neural collapse that does not rely on the unconstrained features model.
- The use of additional linear layers is novel and interesting technique. To the best of my knowledge such an architecture has not been studied.
- The results apply to deep neural networks trained with gradient descent (under a particular architecture/nonstandard activation function) as well as networks which are globally optimal for the weight decay regularized objective.

### Weaknesses
- My main concern with the paper is the writing. The theoretical statements are very difficult to parse this is especially the case for eqs 2-5 in Theorem 3.1. Can the authors provide a more interpretable version of this theorem (hide constants, big-O etc.) and delay the details to the appendix?
- I have the same concern about Theorem 4.4.

### Minor
- The proof of Theorem 3.1 in the Appendix could also be more clear. For example mentioning Weyl's inequality in the first inequality of (21)
- In the proof of Theorem 5.2 at the Appendix (line 1264) shouldn't it be
$$\kappa(W_L) = \kappa(W_{L:L_1+1})^{\frac{1}{L_2}}$$
not 
$$\kappa(W_L) = \kappa(W_{L:L_1+1})^{\frac{1}{L_1}}$$
- Same concern about $L_1$ vs $L_2$ in the statement of Theorem 5.2.

### Questions
- What exactly is the role of these additional linear layers?  Are they only required for proving NC2 and NC3?
- Do these results suggest that neural networks with 1  non-layer and many linear layers can also exhibit neural collapse?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors identify a set of conditions under which various neural collapse phenomena provably occur in deep neural nets.  They consider neural nets which have a sequence of nonlinear layers and then a sequence of linear layers.  They find that approximate interpolation, weight balanced-ness, and boundedness suffice for deriving various neural collapse phenomena.  They then show that GD on networks with a "pyramidal" overparameterized topology (i.e., first width is >= number samples, remaining widths are decreasing), under suitable initialization and regularization, allow for one of the neural collapse phenomena to hold.  They then identify conditions (near-interpolation and small-norm) which ensure that global minimizers of the loss can satisfy all of the neural collapse phenomena.   Finally, they look at the neural collapse phenomena  from the perspective of the edge of stability via an analysis of the properties of the hessian under EoS assumptions.

### Strengths
The authors provide a novel characterization of conditions under which neural collapse can provably occur.  I am not an expert on the NC theory literature, but to my knowledge, no prior work identified balancedness and interpolation as being key factors which can allow for this to occur, and this is a pretty strong finding.   Since the balancedness of post-fixed linear layers is the strongest condition (as most common neural nets do not have multiple linear layers at the end, only a single one), the findings in Section 5 about how boundedness and interpolation can suffice for NC2+NC3 are also a nice addition.  The numerical findings nicely complement their theoretical ones.

### Weaknesses
There aren't any serious weaknesses to me.  The strongest assumptions--namely the need for multiple linear layers in order for the NC phenomenon to occur via the main theorem--seem necessary per experiments in Figure 1.  So it seems that these assumptions are strong for a fundamental reason.

The pyramidal structure assumption is a bit odd/strong, but only seems needed for the optimization result, which I don't think is the central point of the paper.  

The authors don't provide a conclusion or discussion section, and it would have been useful to have comments from the authors about what they think are the weakest parts of their work and what work should be prioritized in the future.  I think they could get some additional space by removing some of the details about optimization from Sec 4 since I don't think they're super important.

### Questions
1. Are there no assumptions on the activation function $\sigma$ needed for Theorem 3.1?  None are stated in Section 3, although assumptino 4.2 appears later.  It seems odd that a potentially discontinuous and horribly behaved activation function would be permitted (I imagine Lipschitz is required?)

2. Assumption 4.2 seems more like a smooth leaky relu, which has appeared in prior work [Chatterjee arXiv:2203.16462, Frei et al COLT 2022]

3. The authors talk about (NC1)-(NC3), what about (NC4) from the original Papyan paper?

4. Are there any important differences between the proof of Theorem 4.4 and the proofs/results in Nguyen and Mondelli?   I'm not familiar with that work, but it seems like it's not super necessary to have details about optimization (e.g. the PL inequality) in the main section of the paper, it distracts from what I think are the more interesting and stronger results elswhere in it (it would also give additional space to have a proper conclusion and outline what the authors think are future directions).   I am assuming balancedness didn't appear in the prior analysis but does here.  A few sentences describing high-level differences between proofs and ideas would be helpful.  

5. Also, to be clear, the optimization analysis in Sec 4 is in the NTK regime right?  I didn't see this explicitly mentioned but it should be if it is known.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies neural collapse phenomenon in training wide neural networks. The first result in this work establishes some general conditions (interpolation, balancedness between layers, well-conditioned-ness of weight matrices) such that NC1, NC2, and NC3 can hold. The second result considers training a wide neural network with gradient descent such that the aforementioned conditions hold after training, which implies neural collapse can happen after training.

### Strengths
This work goes beyond the conventional unconstrained feature model (which many previous works have worked on) and proves that neural collapse can happen after training for full-connected neural networks satisfying some architectural conditions such as pyramidal topology and smooth activation. The conditions established in Theorem 3.1 of this work under which neural collapse can happen seem very reasonable. Indeed, later, the authors proved that those conditions can be satisfied by training a neural network via gradient descent which automatically implies that neural collapse can happen after training. 

I am not very familiar with the prior works along this line of research such as (Kothapalli & Tirer, 2024), (Hong & Ling, 2024) and many others mentioned in the introduction and related work. Based on my knowledge on neural collapse, I think this work made some interesting contributions towards understanding this phenomenon.

### Weaknesses
1. The analysis critically relies on the fact that the last two layers of the neural network are linear. I can definitely see this condition makes the problem a lot easier to analyze. I am wondering how hard it is to remove such restrictions. 
2. It seems the analysis of Theorem 4.4 relies on the neural network in the NTK regime, as the pyramidal topology assumption has appeared in previous works such as (Nguyen & Mondelli, 2020). I don't regard this as a major weakness even if it turned out to be true that the networks are in the NTK regime given the contribution of this work, however, I do appreciate clarification on this.

### Questions
I am wondering whether the layer balanced-ness property after training can be proved as a direct consequence of [1] in the author's setting.

[1] Du, Simon S., Wei Hu, and Jason D. Lee. "Algorithmic regularization in learning deep homogeneous models: Layers are automatically balanced." Advances in neural information processing systems 31 (2018).

### Soundness
3

### Presentation
3

### Contribution
3
