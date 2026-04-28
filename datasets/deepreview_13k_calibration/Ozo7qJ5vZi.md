# KAN: Kolmogorov–Arnold Networks

- Decision: Accept
- Avg Score: 7.20
- Scores: 8, 8, 6, 6, 8

## Abstract
small
Inspired by the Kolmogorov-Arnold representation theorem, we propose Kolmogorov-Arnold Networks (KANs) as promising alternatives to Multi-Layer Perceptrons (MLPs). While MLPs have \textit{fixed} activation functions on \textit{nodes} (``neurons''), KANs have \textit{learnable} activation functions on \textit{edges} (``weights''). KANs have no linear weights at all -- every weight parameter is replaced by a univariate function parametrized as a spline. We show that this seemingly simple change makes KANs outperform MLPs in terms of accuracy and interpretability, on small-scale AI + Science tasks. For accuracy, smaller KANs can achieve comparable or better accuracy than larger MLPs in function fitting tasks. Theoretically and empirically, KANs possess faster neural scaling laws than MLPs. For interpretability, KANs can be intuitively visualized and can easily interact with human users. Through two examples in mathematics and physics, KANs are shown to be useful ``collaborators'' helping scientists (re)discover mathematical and physical laws. %Despite being intrinsically different from MLPs, the extrinsically fully-connected structure of KANs makes them easy and 
In summary, KANs are promising alternatives for MLPs, opening opportunities for further improving today's deep learning models which rely heavily on MLPs.
\begin{figure}[hb]
    \centering
    \includegraphics[width=0.9\linewidth]{./figs/kan_mlp.pdf}
    \caption{Multi-Layer Perceptrons (MLPs) vs. Kolmogorov-Arnold Networks (KANs)}
    \label{fig:kan_mlp}
\end{figure}

\begin{comment}
\tableofcontents
\end{comment}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a replacement for multilayer perceptrons based on the Arnold-Kolmogorov theorem which gives a two layer network for function approximation as a sum of univariate functions of individual features followed by a function of the sum. The Arnold-Kolmogorov theorem has previously been declared irrelevant for building learning machines since the involved functions can be nonsmooth [cite].
The paper reconsiders the Arnold-Kolmogorov theorem for building learning models and proposes that deep versions of networks using the Arnold-Kolmogorov theorem might not be limited by the non-smoothness that appears in shallow networks. The paper proposes Kolmogorov Arnold networks which are stacked layers of the univariate function+sum layers that appear in the 2-layer network.
The paper further gives an approximation theorem which bounds the error in the derivatives up to some order for a function approximated by a KAN network with B-splines.
The advantages of KANs over MLPs are said to be that KANs can be more interpretable than MLPs which makes them useful for symbolic regression tasks and are useful in data-driven scientific discovery.

### Strengths
The main contribution of the paper is a practical instantiation of the Arnold-Kolmogorov theorem as a deep network which can avoid the difficulties plaguing shallow versions of the theorem. There are a number of experiments validating the method ranging from replicating discovery results from knot theory, automatic and interactive symbolic regression and solution of partial differential equations. The paper is generally well-written and clear.

### Weaknesses
I have a few concerns, listed in the following.

1. In light of previous concerns in the literature with the Kolmogorov-Arnold theorem as a basis for learning machines, I think the paper should focus more on establishing whether the problem of non-smoothness is in fact avoided in deeper versions. Since this would establish whether the proposed model is general enough and can scale to high dimensions.

2. The paper presents Theorem 2.1 which gives a bound on the supremum of the error in the derivative. However, it is not clear whether the bound is actually useful since it depends on f and the network in an unknown way through the constant C.
If a general theoretical argument demonstrating smoothness is too difficult, perhaps the paper could investigate the smoothness of the learned functions (or the gradients during training) to provide empirical evidence that the model learns smooth functions. 

3. Regarding the proof of Theorem 2.1 in Appendix B. It is not clear to me how the bound on the residual is obtained in line 894.
If I understand correctly, the bound on B-spline approximation in line 887 is for a single univariate function, phi_{l,i,j}, whose inputs are exact. However when the inputs from the layer below are also approximated and then summed, one would expect the bound of sup of error in the derivatives to also be summed? Whereas the error in line 887 for exact inputs and that in line 894 for approximate inputs is exactly the same. Could you clarify how the error for the residual is obtained?

4. I don’t quite understand how in the symbolic regression tasks the units are automatically converted into symbolic functions. I also couldn’t find the metric used for accuracy in the SR experiments.

5. I think the motivation described in lines 62-64 should be rephrased. Regardless of the aim of interpretability, smoothness is still quite essential for learning which is the point of Giros & Poggio [1989].

Minor corrections.

Line 16. Interpretabe -> interpretable

205. KAT -> KAN

473. pareton -> pareto

### Questions
Are the constants C in the proof in appendix B and the statement of Theorem 2.1 the same? If not, different notation would be better.  

Did you compare the symbolic regression results with other methods? Some baselines would be useful.

As asked above, could you please clarify how the residual error bound in the proof of Theorem 2.1 is obtained?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel network architecture named KAN based on the Kolmogorov-Arnold representation theorem. Unlike MLPs, the KAN architecture is composed of univariate but learnable activation functions and the summation operation. It extends the Kolmogorov-Arnold representation of a function to deeper layers, which partially addresses the issue of non-smooth functions in the original two-layer Kolmogorov-Arnold representation. KAN shows good interpretability and performance in tasks that deal with symbolic formulae (e.g., applications in scientific discovery).

### Strengths
1.	The design of KAN is well motivated and rooted in previous literature, i.e., the Kolmogorov-Arnold representation theorem. Why this theorem was not widely applied for machine learning previously is also discussed.

2.	The presentation of the paper is clear and easy to follow.

3.	The paper covers comprehensive aspects of the proposed architecture, including its theoretical foundation, detailed architectural design, guarantee on approximation ability, implementation details and tricks, etc. 

4.	The paper clearly states the “comfort zone” and limitations of KAN, and points out potential future directions.

5.	The view of external and internal degrees of freedom is interesting.

### Weaknesses
One major concern is that the selection of architectural hyperparameters of KAN (e.g., the number of layers, the number of nodes in each layer) is not discussed in detail, and it seems that we need some prior knowledge of the target function when selecting these hyperparameters. More detailed concerns and questions are listed below.

**1. About the theoretical guarantee of the approximation ability in Theorem 2.1.** Theorem 2.1 states that if the target function admits a structure of the composition of $L$ KAN layers with smooth activation functions, then we can use an $L$-layer KAN (with B-splines) to approximate it well. However, it does not discuss the scenario where the structure (in particular, the number of layers $L$) of the target function is unknown, which is common in real applications. I wonder if we use a shallower KAN (less than $L$ layers) or a deeper KAN (more than $L$ layers) to approximate the target function (which is assumed to have $L$ layers), how will the result in Theorem 2.1 change? It seems that a deeper KAN can still approximate the target function by setting higher layers as identity mappings, but things become more nuanced for a shallower KAN. Specifically, if the target function has a complex structure requiring L layers, a shallower KAN may fail to capture the intricate relationships between variables. This raises questions about the practical applicability of Theorem 2.1 when the target function's structure is unknown a priori.

**2. About how to select the number of layers in experiments.** Do we start from training a deep and wide KAN, and then use the sparsification trick in Appendix E to prune redundant nodes or even layers? Or do we simply apply a grid search over different number of layers and then select the best performing combination? It is encouraged to provide a step-by-step description of the process for determining KAN architectures in the experiments. A clear methodology for selecting the optimal number of layers would enhance the reproducibility and practical value of the proposed architecture.

There are also some subquestions in this part:

(a) If we are to first train a deep KAN whose number of layers is probably more than the number of layers of the target function, what will this KAN look like after being trained to convergence? Let us assume the target function $f$ is a composition of $L$ symbolic formulae, and the KAN we use has $M>L$ layers. Would the last $M-L$ layers behave as identity mappings, and the first $L$ layers capture exactly $f$’s structure? This is an important question for understanding the behavior of over-parameterized KANs.

(b) (As a continuation of question (a)) Although a deeper KAN may have better performance, would the increasing depth degrade its interpretability? Specifically, if the superfluous layers do not perfectly converge to identity mappings, they might introduce spurious relationships that hinder the extraction of meaningful insights from the trained model.

(c) If we use a KAN that is too deep, would there be difficulties in optimization? If so, how many layers would you recommend starting with? Deep networks are often harder to train due to issues like vanishing or exploding gradients. It would be helpful to have some guidelines on the maximum depth that can be practically used for KANs.

(d) Are there advanced and task-dependent strategies (maybe heuristics) to select these hyperparameters, especially for cases where prior knowledge of the target function is limited? Providing some practical heuristics or strategies for hyperparameter selection would greatly improve the usability of KANs.

**3. About how to select the number of nodes per layer in experiments.** I find it surprising that in Line 300, a KAN with only one internal node can perform very well in the task of knot theory. That being said, it is unclear how to determine that we only need one node in the intermediate layer. Is it achieved by some prior knowledge of the task or by training a wide KAN and then pruning out redundant nodes? A more systematic approach for determining the optimal number of nodes per layer is needed.

---

Another concern is about the necessity of the sparsity loss introduced in Appendix E. Is there any ablation study of this sparsity loss? By ablation study, I refer not only to the analysis of performance changes with and without the sparsity loss but also to how the structure of the learned KAN changes. For example, if there is no sparsity loss, is it possible for a layer to learn multiple identical functions “distributed” over different nodes, such as $ x^{2}/3, x^{2}/3, x^{2}/3$, instead of a single $ x^{2}$? This is crucial for understanding the role of sparsity in promoting interpretability and preventing redundancy in the learned representations.

### Questions
1.	About the experiment in Figure 5. It is known that standard MLPs (e.g., with ReLU activations) perform poorly in fitting periodic functions such as sine. Is it possible to also try MLPs with other activation functions (e.g., the sine function) to see if it can get better or even comparable performance with KAN?

2.	About Table 1. Does the line labeled by “Theory” refer to the ground-truth formula and the other lines the formulae predicted by KAN? If so, why does the ground-truth formula also have an “accuracy”?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Kolmogorov-Arnold Networks (KANs) as an alternative to Multi-Layer Perceptrons (MLPs), particularly when interpretability is desired, such as for extracting symbolic formulas from datasets in scientific applications. The authors contextualize the Kolmogorov-Arnold representation theorem within modern machine learning, relating it to MLPs and generalizing the representation from two layers to multiple layers via introduced KAN layers, thereby enhancing expressive power while addressing some pathological behavior of Kolmogorov-Arnold representations. 

The paper aims to demonstrate the interpretability of KANs and their potential to serve as a useful tool for scientific discoveries, presenting examples from mathematics (knot theory) and physics (Anderson localization) where KANs can assist scientists in (re)discovering mathematical and physical laws. Furthermore, the authors show through theory and experiments that KANs are accurate and have favorable scaling laws, while MLPs scale more slowly and plateau quickly.

The focus of the paper is on relatively small-scale numerical examples from various scientific domains, with the scalability and extensibility of KANs to large-scale machine learning tasks left as future work. Overall, the paper introduces KANs as a promising alternative to MLPs, especially for interpretable and accurate learning in scientific applications, and lays the groundwork for further exploration of their potential.

### Strengths
The paper presents a novel neural network architecture inspired by the Kolmogorov-Arnold representation theorem (KST). The authors creatively combine the insights from the KST with modern deep learning techniques, generalizing the original two-layer representation to multiple layers through the introduction of KAN layers. This novel approach to network design demonstrates originality and has the potential to open new avenues for research at the intersection of deep learning and approximation theory.


The authors provide extensive numerical evaluations across a diverse collection of experiments. There they aim to showcase the effectiveness of KANs in various domains, including synthetic toy datasets, special functions, physics equations (Feynman datasets), and partial differential equations. These experiments aim to provide a comprehensive assessment of KANs' performance, interpretability, and scaling laws compared to traditional MLPs. 


The paper is well-structured and clearly written, making it accessible to a broad audience. The authors provide sufficient background information on the KST and its relation to neural networks, ensuring that readers can understand the motivation behind KANs. The mathematical formulation of KANs and the approximation theory are presented in a rigorous and understandable manner.


The significance of this work lies in its potential to bridge the gap between deep learning and approximation theory, as well as its implications for interpretable and accurate learning in scientific applications. The authors demonstrate that KANs can be effective in discovering mathematical and physical laws, showcasing some early promise as a tool for scientific discovery. Moreover, the scaling laws exhibited by KANs suggest that they may be a promising alternative to MLPs in certain domains.


I would also like to acknowledge that this research has already generated considerable interest in the recent literature, with several studies exploring the possibilities brought by combining deep learning with the KST. The paper has opened new avenues for research, as the community seeks to assess and enhance the capabilities of KANs and related architectures.

### Weaknesses
While I believe that this paper puts forth a creative idea that is worthwhile publishing, the current presentation makes it very difficult to assess whether KANs are indeed a good and competitive method to employ for all the different tasks presented in this work: symbolic regression, function regression, PDE solving, etc. The main reason is that the vast majority of numerical evaluations are poorly designed, either by disadvantaging competing methods, or by comparing against very weak baselines, or by providing no comparison to competing methods (for example, in the symbolic regression benchmarks).

1.  **Comparison to state-of-the-art methods:** While the paper presents promising results for KANs in various application settings, such as symbolic regression and solving PDEs, the effectiveness of KANs compared to state-of-the-art methods in each domain remains unclear. The authors primarily compare KANs against basic MLP architectures, which may not represent the best-performing approaches in these specific areas. To provide a more comprehensive assessment of KANs' capabilities, it would be beneficial to compare them against well-established and state-of-the-art methods that are commonly used in practice for each application. This would help to better understand the relative strengths and weaknesses of KANs and their potential to advance the state of the art in these domains.

2.  **Overstated claims and conclusions:** Due to the lack of comparisons against state-of-the-art methods in each application area, the current claims and conclusions in the paper may be somewhat overstated. While the results demonstrate the potential of KANs, it is difficult to assess their true effectiveness and superiority without a more comprehensive evaluation against well-established benchmarks and leading approaches. The authors should consider tempering their claims and conclusions to reflect the limitations of their current experimental setup and the need for further validation against state-of-the-art methods.

3.  **Interpretability claims and symbolic regression protocol:** The authors emphasize the interpretability of KANs as one of their key strengths. However, the symbolic regression protocol presented in Section E.2 and Figure 10 appears to be largely heuristic and sensitive to various hyperparameter choices. The effectiveness of this protocol in recovering interpretable models from real-world data remains questionable, as the current results focus on rediscovering known scientific formulas. Moreover, the authors do not provide a comparison against state-of-the-art symbolic regression alternatives, making it difficult to assess the relative interpretability of KANs. The arguments against symbolic regression methods in the appendix are not entirely convincing, given the reported success of such methods in challenging settings [1]. To strengthen the interpretability claims, the authors should consider evaluating KANs against leading symbolic regression approaches and demonstrating their effectiveness in recovering interpretable models from real-world data.

4.  **Unconventional protocols for training MLPs:** The authors employ unconventional protocols for training MLPs, such as using networks with small widths and full-batch L-BFGS optimization for a limited number of training steps. While these choices may be made to match the parameter complexity and training cost of KANs, they could potentially disadvantage the effectiveness of MLPs and render the comparisons and conclusions questionable. Recent results [3,4] suggest that a fair comparison between KANs and MLPs may lead to different conclusions than those reported in this paper. To address this concern, the authors should consider using more standard and well-established training protocols for MLPs, ensuring a fair and unbiased comparison between the two architectures.

5.  **Comparison against plain MLPs in PINNs:** In the context of Physics-Informed Neural Networks (PINNs), the authors compare KANs against plain MLP networks initialized using the Glorot scheme. However, this setup is known to yield a poor baseline in the current PINNs literature, as the derivatives of such networks have limited expressive power to adequately minimize PDE residuals. To provide a more meaningful comparison, the authors should consider evaluating KANs against state-of-the-art PINN frameworks such as PirateNets [5] that have been specifically designed to address the challenges of PDE solving. This would help to better understand the potential advantages of KANs in the context of PINNs and their ability to advance the state of the art in this domain.

### Questions
Here are some questions and suggestions for the authors to consider during the rebuttal and discussion phase:

1. **Baselines for symbolic regression:** In the symbolic regression experiments, the authors do not include comparisons to state-of-the-art approaches like PySR (Cranmer, 2023). Such approaches have demonstrated reliable performance on a wide range of symbolic regression tasks and have been successfully applied to real-world scientific discovery problems. To better assess the effectiveness of KANs for symbolic regression, it is important to compare them against the best-performing methods in this domain. Can the authors include experiments comparing KANs to PySR and other leading symbolic regression techniques, and discuss how KANs perform relative to these state-of-the-art baselines in terms of accuracy, efficiency, and interpretability?

2. **Baselines for function regression:** In the function regression experiments, to ensure a fair and meaningful comparison, the authors should consider employing best practices for MLP training, such as using appropriate network sizes, optimization algorithms (e.g., Adam or SGD with learning rate scheduling), and regularization techniques (e.g., dropout or weight decay). Can the authors update their function regression experiments to include MLP baselines trained using best practices and discuss how KANs compare to these more robustly trained MLP models?

3. **Baselines for PDE solving:** In the PDE solving experiments, the authors compare KANs against vanilla MLPs with Glorot initialization, which is known to be a weak baseline in the current literature on Physics-Informed Neural Networks (PINNs). To better demonstrate the effectiveness of KANs in this context, the authors should consider comparing against more advanced and well-established PINN architectures and initialization schemes. Can the authors include experiments comparing KANs to state-of-the-art PINN methods like PirateNets and discuss how KANs perform relative to these stronger baselines?

4. **Continual learning comparison:** The continual learning results presented in the paper are not entirely surprising, given that the spline activations used in KANs are compactly supported, and their local behavior can be modulated by neighboring knots without altering their global structure. For a more fair and informative comparison, the authors should consider evaluating KANs against MLPs with compactly supported activations, such as Radial Basis Functions (RBF), as networks with activations like ReLU or Tanh are inherently prone to catastrophic forgetting. Can the authors provide additional experiments comparing KANs to MLPs with compactly supported activations in the continual learning setting and discuss the implications of these results?

5. **Appendix content and organization:** The Appendix contains a substantial amount of supplementary results that may not significantly contribute to the main messages of the paper and could easily be overlooked by readers. For example, the LAN approach and results presented in Appendix P are interesting but could potentially be the topic of a separate paper (although LANs appear to only introduce a small tweak to the SIREN architecture). This also raises the question of how KANs would perform for an image regression task and why such an evaluation was not provided. In general, to enhance the overall clarity and focus of the manuscript, the authors should carefully evaluate which key results from the Appendix are essential to strengthen the main messages of the paper and consider removing or reorganizing the remaining content. Can the authors provide a rationale for the current organization of the Appendix and discuss how they plan to refine it to better support the core ideas of the paper?

6. **Training details and data normalization:** Some important training details, such as data normalization protocols, are omitted from the text. It appears that KANs require inputs to be in the range [0, 1]. Are the inputs to the MLP networks normalized in the same way? Inconsistencies in data normalization can lead to unfair comparisons and affect the interpretation of the results. Can the authors clarify their data normalization procedures for both KANs and MLPs and discuss any potential impact on the reported findings? 

7. **Computational complexity of grid extension and refinement:** The paper introduces the concepts of grid extension and grid refinement for KANs but does not provide a detailed discussion on their computational complexity. Understanding the computational overhead associated with these operations is crucial for assessing the practical applicability of KANs in various settings. Can the authors provide a more in-depth analysis of the computational complexity of grid extension and refinement, including theoretical bounds and empirical measurements, and discuss the implications for the scalability and efficiency of KANs? Moreover, the update of spline grids mentioned in p. 16 seems to be a very important step of the algorithm but it is not adequately explained.

8. **Code availability:**  The authors did not provide any code with this submission and I was unable to assess their implementation. This may have helped with resolving some of the above questions.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a novel neural network architecture based on the Kolmogorov-Arnold Representation Theorem (KAT), called Kolmogorov-Arnold Networks (KANs). Although the KAT has been studied in the context of neural networks, KANs differ from most other works by allowing for wider/deeper representations, in addition to implementing functions implied by the theorem via B-splines. The authors formally describe the main component of their new architecture, the KAN-layer, which draws inspiration from the representation formula implied by the KAT. In essence, a KAN-layer works by approximating the functions implied by KAT via B-splines, as well as adding a 'residual' connection using a silu activation. These KAN-layers can then be composed together to create a deeper KAN architecture. The authors also state a theorem regarding the approximation capabilities of KANs, assuming a specific smooth representation of the target function.

The authors then go on to detail experiments using their new architecture on two main goals: a) providing interpretable results from scientific data; and b) creating accurate predictions for regression tasks and learning the solution of a PDE. On their first goal, they evaluate KANs on tasks from mathematics (knot theory) and physics (Anderson localization), as well as some toy problems on symbolic regression. For their second goal, they compare KANs against certain MLPs on regression for several smooth functions with closed form solutions, as well as a physics-informed problem where they learn the solution of a 2D Poisson equation. 

Finally, the authors summarize their results and argue that KANs offer significant advantages over traditional MLPs for scientific tasks that are "small-scale", leaving more thorough experimentation on larger-scale problems for future work.

### Strengths
### Originality/Significance: 
The paper presents several interesting original thoughts, and helps bring attention to new forms of computation to scientific deep learning. Although the connections between KAT and neural networks are quite old, dating back to the 1960s and 1970s, their work helps renew attention to this field, and applies modern knowledge about neural networks to improve on previous failed attempts of using KAT for applied problems. The authors also present interesting ideas about interpretability for deep neural networks, by using KANs to guide the discovery of closed form expressions for unknown functions.

### Quality:
The main idea (exploiting deeper/wider forms of KAT) is well-motivated and appears theoretically promising. The authors provide valuable arguments on section 2 about why such an idea could work. The paper also comes with many experiments being conducted in the main text, as well as in the appendix. Overall, I believe this paper contains very interesting ideas, and helps spark discussion about an old topic using modern lenses.


### Clarity:
The ideas are presented in a mostly clear manner, with helpful figures to illustrate the main arguments. Their main theorem (Theorem 2.1) is clearly stated in the main text, including all of its assumptions.

### Weaknesses
## Summary of weaknesses:
In summary, although the main idea of the paper seems very interesting, my main criticism of this submission is regarding their experiments, which are not conclusive to me as a reviewer. Despite presenting a very large number of different experiments, they are all very simple, and comparisons against MLPs appear to be using very weak baselines. The authors do recognize that they mainly consider small-scale experiments [line 485], but even for scientific tasks there are more realistic and interesting problems to be considered, as will be detailed later. In addition to this, their main theorem regarding approximation power of KANs (theorem 2.1), which implies very strong scaling laws, use an assumption which is known to be wrong for KAT functions (ie: inner functions being $(k+1)$-times continuously differentiable). I further detail these criticisms below, and how the authors might address them.

## Experimental Setup:
I will mainly focus on the results reported in section 4 here, which is an area I am more familiar with. My main criticisms regarding experiments is that a) all functions considered are very well-behaved and not something for which deep learning would be used in practice, with other regression tools generally being better suited; b) I am not confident that their comparisons against MLPs are done in a consistent and fair way; c) there is not enough information to fully reproduce experiments. I expand on each of these points below.

a) For regression tasks (Toy datasets + Special Functions + Feynman Datasets), all the target functions are very simple, beyond what is typical for scientific machine learning. The functions from the "Special Functions" dataset are slightly more complicated than from the other two, but still a very simple task given enough training data. A better testbed for examining approximation properties and accuracy would be for example: 1) regression against complicated PDE solutions from publicly available dataset such as PDEBench and/or PDEArena, which are more relevant to scientific computing; 2) regression against images, which was in fact considered in the appendix for their "LAN" architecture, but not KANs; 3) weather modeling, using public datasets such as ERA5 (very challenging) or NOAA's SST-V2, for example. Regarding the experiment on PINNs, it would also be more comprehensive to study more than just the Poisson equation, which is again very simple for tasks of this nature. Suggestions for other PDEs to consider, which are not unrealistic for the first iteration of a new architecture include the Allen-Cahn equation and the Darcy problem. In short, although it is true that some problems in scientific computing are simpler or lower dimensional than ones in computer vision and NLP, which are big topics in deep learning, there is still no shortage of more realistic problems in science, which would provide a better testbed for their architecture.

b) Many aspects of the experiments provided are not likely to yield a fair comparison against MLP architectures. In some cases, only MLPs of very small width (such as 5 or 20) are considered, which is not realistic of what someone would use in practice, even if the number of parameters is similar to that of KANs used. For some of the regression tasks, the grid definition of KAN's B-splines can go as high as 1000, which means that a KAN of comparable width/depth still presents far more parameters (and likely flops) than an MLP. To address this issue, I would recommend keeping a fixed number of trainable parameters (or flops/training time), comparing different hyperparameter combinations, both for KANs and MLPs. Ideally, MLPs should have widths of at least 32 or 64 for any real scenario. In addition to this, MLPs are more efficiently trained using the Adam optimizer, whereas all experiments used the L-BFGS algorithm, which is not as common and can often lead to MLPs being stuck on local minima.

c) There are many missing details for reproducing the experiments in the paper, and no code was provided as supplementary material. For example, on many of the regression tasks, the target functions are reported, but not the total number of points in the training/testing set, nor what the domain for these functions is. Other missing information for reproducibility include: 1) the batch size used during training for different benchmarks; 2) the learning rate of the optimizer; 3) the architectures used in the continual learning example. The best way of solving all this missing information issue would be to **provide the code used for each experiment as a supplementary material**, organized neatly for each benchmark.


## Theoretical Assumptions:
A main assumption of theorem 2.1 of the paper is that the functions $\phi_{l,i,j}$ are $(k+1)$-times continuously differentiable. However, the KAT only guarantees that these functions are continuous, as and the authors themselves mention, it has been shown in the literature that these functions can provably be very chaotic, with infinite set of non-differentiability. The authors argue that by using wider/deeper representations, these irregularities may disappear, but this would require further theoretical evidence. I believe there are more reasonable ways of proving universal approximation guarantees for KANs, albeit without the strong scaling laws implied by the $k$-order spline functions. This main theorem therefore can likely be stated differently, in order to obtain a weaker but more theoretically reasonable statement.



## Other minor considerations that did not affect my score:
- [line 15 + many other mentions] The analogy of referring to computations on 'edges' vs 'nodes' is not very clear or compelling to me. Depending on how you chose to represent any given architecture as a graph, it could be argued either way whether an operation happens at an 'edge' or at a 'node'.
- [line 54] Although it is true that "In science, symbolic functions are prevalent," that is not generally the case in scientific computing, where solutions are often defined on complicated domains without reasonable closed-form expressions. In fact, for tasks where numerical solutions are needed (such as solutions to ODEs, PDEs, etc), it is almost always the case that the solutions are not symbolic.
- [line 260] There are only three examples in Figure 2, not six.
- [Figure 7] It is more common for the y-axis of the plots to show the error itself, not the error squared, as is done in the figure.
- [line 875] It would also be nice to see a comparison on the computational complexity of KANs vs MLPs, in addition to parameter count.
- [line 1819] In the case of PINNs, it is almost always better to sample points randomly and independently at each iteration, as opposed to maintaining a fixed grid. I would be interested to see how KANs perform in this setting.

### Questions
I detail below some questions/suggestions to the authors, in order of how important they would be toward increasing the review score of their submission.

- **[More Challenging Problems For Testing Accuracy]** As mentioned above, I think the paper would greatly benefit from more challenging benchmarks, as the ones reported are too simple and largely not relevant to scientific computing. Seeing KANs outperform realistic MLPs (using higher widths and Fourier features, for example) on more challenging tasks could highly increase my score for the submission, depending on the results. Some potential tasks are detailed above in the previous section.

- **[Comparison Against Symbolic Regression Baselines]** The authors highlight discovery of close-form expressions from data as a key feature of KANs, but experiments lack comparison against other symbolic regression baselines, as the ones detailed in lines 2115-2121. Seeing KANs outperform these baselines could make for a much stronger paper.

- **[Spline Grid Boundary]** Using B-splines require all inputs to fall within a specified interval, which may not be the case for intermediate layers of a deep KAN. On line 852, the authors mention they "update each grid on the fly according to its input activations," but no further information is given as to how this is done, to the best of my knowledge. I feel like this is an important aspect to detail in the paper, maybe even in the main text. Related to this, how would the authors deal with problems where the inputs are defined in an unbounded (or very large) domain, such as when inputs follow a distribution with a 'fat' tail?

- **[Skip Connections]** What is the effect of removing the silu 'basis function' used in the KAN layer? Are there other suitable functions to choose instead of silu? This would be a good ablation to consider reporting.

- **[Grid Extension]** The authors propose progressively extending the grid used for computing B-splines, which improves the predictive accuracy of a given model. Is there an advantage to progressively increasing this grid as opposed to starting with a large one? That would be an interesting ablation to include in the paper.

- **[Continual Learning]** For the continual learning experiment, what happens if a deeper KAN is used? It makes sense that the local nature of B-spline computations yields this nice feature, but it seems to me that once more compositions are at play this property would be lost.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes Kolmogorov-Arnold networks (KANs) as a more interpretable alternative to multi-layer perceptrons (MLPs), particularly for scientific applications. KANs replace the fixed activation functions on nodes in MLPs with learnable activation functions on edges, represented by B-splines. The paper explores the theoretical approximation capabilities of KANs, proposes training techniques for interpretability and accuracy (pruning, symbolifying, grid extension), and demonstrates their application in mathematics (knot theory), physics (Anderson localization), and other (toy) examples.

### Strengths
+ The paper presents an interesting and original neural network architecture inspired by the Kolmogorov-Arnold representation theorem, which has very appealing properties for some applications (e.g. interpetability).

+ The paper is generally well-written and easy to follow. The architecture of KANs is clearly explained, and the figures effectively illustrate the differences between KANs and MLPs.

+ The emphasis on interpretability (and the ability to extract symbolic formulas) is relevant for scientific applications, where understanding the underlying mechanisms learned by the model is crucial.

### Weaknesses
 - Technically, the paper could be considered to be over the page limit. While the main text does keep to 9 pages, this is only the case because extremely important sections, e.g., related works and the discussion, are moved to the appendix. I feel important sections like these have to be included in the main text, even if this means other parts of the text need to be shortened to make space for them. I am sure many authors of other submissions have faced similar "space issues" and consequently had to cut parts from their main text. This paper is the only submission I am reviewing that "misuses" the appendix to circumvent the page limit restrictions (I think the appendix should be reserved for things like detailed proofs or additional, but non-essential, information). Sorry for bringing up a technicality like this, but I feel it is necessary in the interest of fairness.

- The paper contains very strong claims, e.g. that KANs with finite grid size beat the curse of dimensionality. At the same time, the authors admit that the constant $C$ in Eq.11 (Theorem 2.1) implicitly depends on the dimension (but details are left to future work). As the saying goes, extraordinary claims require extraordinary evidence, which unfortunately is missing here. The authors should either weaken their claims or provide strong empirical evidence.

- While reading the paper, I couldn't help but feel that the name "Kolmogorov-Arnold network", at least to some degree, overstates the difference to MLPs: KANs and MLPs have more in common than a superficial reading of the paper would suggest. Comparing the Kolmogorov-Arnold Theorem (KAT) with the Universal Approximation Theorem (UAT), a very important aspect is that KAT requires a width of only $2n+1$, whereas the UAT only holds in the limit of infinite width. I understand that relaxing the width-restriction from KAT may be practically useful (and the authors motivate this choice well), but it also blurs the lines between KAT and UAT. To me, KANs seem more like a KAT-inspired re-interpretation of MLPs (rather than something entirely new), which is useful for tasks where a symbolic interpretation of the learned function is desirable. For example, one distinguishing feature of KANs pointed out in the abstract are the learnable activation functions, wheareas MLPs have a fixed activation function. But if I re-write an MLP $W_2\sigma(W_1\mathbf{x})$ as $W_2\phi(\mathbf{x})$ with $phi(\mathbf{x}) = W_1\mathbf{x}$, I can also consider $phi$ to be a "learnable activation function". Similarly, the basis functions of the B-splines in KANs could be equivalently considered simply as additional input features, similar to Fourier features (https://arxiv.org/abs/2006.10739), or other tricks that were sometimes used in older works (e.g. feeding the square of an input to a layer, see e.g., "Neural Networks: Tricks of the Trade"). I think the authors should try to "de-mistify" KANs by pointing out and discussing these similarities between MLPs and KANs more transparently.

- While the examples in mathematics and physics are interesting, the scale of these problems is relatively small. The paper lacks evaluation on larger, more complex datasets. This makes it difficult to assess the true scalability and practical utility of KANs for many real-world applications. For example, a very simple test could be to compare KANs vs. MLPs on something like MNIST. Even if KANs perform worse than MLPs here, this does not mean at all that they are not useful. However, it would certainly help readers to assess whether KANs (in their current form) are likely to be directly relevant for their work or not. I encourage the authors to include at least one example like this.

- The example in Appendix J on continual learning is practically not relevant and too trivial. Of course, the B-splines in KANs are "local" and thus the corresponding weights/coefficients are not affected by catastrophic forgetting in this setting, but the toy example is also clearly constructed to take advantage of this fact. The authors should either demonstrate that KANs are less affected by catastrophic forgetting than MLPs in a more realistic/"less constructed" setting, or remove this claim from the paper.

- The paper mentions that KANs are slower to train than MLPs by roughly a factor of 10, and that KANs cannot leverage batch computation in the same way as MLPs. However, these discussion are hidden in the appendix. I think this is a highly important and practically relevant aspect, which should be discussed more prominently and in greater detail in the main text. An analysis of the computational cost, including training time and memory usage, is needed to fully understand the trade-off between interpretability and efficiency.

- The appendix is very long with >25 additional pages, not all of which feel strictly necessary to me. I think the authors should consider cutting some parts of the appendix in the interest of brevity. For example, the secion on LANs, while interesting, feels better suited as a separate submission (after doing more experiments/refining the idea).

### Questions
* How do KANs compare to other interpretable models, like Neural Additive Models or symbolic regression methods, in terms of accuracy, interpretability, and computational cost, especially on larger datasets?

* Can you provide a more detailed analysis of the computational complexity of KANs, both for training and inference? Have you explored any optimizations beyond the "multi-head" approach?

* Can you elaborate on the dependence of the constant C in Theorem 2.1 on the dimension? How does this impact the scalability of KANs to higher-dimensional problems?

* Can you provide empirical evidence supporting the claim that KANs can naturally work in continual learning without catastrophic forgetting, beyond the toy example in Appendix J?

* How sensitive are KANs to the choice of hyperparameters, such as the grid size $G$ and the spline order $k$? Have you explored techniques for automatically selecting these hyperparameters?

**Additional Feedback** (this does not affect my score)

* In my opinion, some formulations, e.g. "the Kolmogorov-Arnold representation theorem was basically sentenced to death" (l.119), or "the fastest scaling exponent ever" (l.1888) appear overly "dramatic" for a scientific paper. I suggest the authors scan their paper for cases like these and try to use more neutral/grounded language.

* There are several typos, e.g. "altnertives" (abstract), "On" (l.084), "staricase-like" (l.965), "theLANs" (l.1705), "maximu" (l.1885). I suggest the authors use an automated spell-checker to find problems like these and correct them (I likely didn't find all typos).

* Some terms are spelled inconsistently in different places of the text, for example "Deepmind" vs. "deepmind" (I actually would recommend to use "DeepMind" instead), or "ReLU" vs. "ReLu". The authors should decide on one spelling and keep it throughout the paper.

**In summary**
I believe this is a very interesting paper that should be published, but I feel major revisions are necessary (see above). If the authors implement these revisions (or at least most of them), I will gladly raise my score.

### Soundness
3

### Presentation
3

### Contribution
3
