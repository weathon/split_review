# A qualitative theory of dynamical systems for assessing stability in ResNets

- Decision: Reject
- Scores: 8, 3, 3

## Abstract
We present an experimental method for evaluating the stability of ResNets, inspired by the qualitative theory of dynamical systems. To apply qualitative and quantitative properties from the literature on dynamical systems, we have proposed ResNets designed to maintain dimensionality throughout the residual blocks. As a result, we can not only introduce a well-suited concept of expansivity and shadowing properties for ResNets but also analyze their numerical degrees based on Dynamical Systems theory. This work aims to contribute to the understanding of ResNets' stability and bridge the gap between theory and practical applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel characterization of the stability of ResNets in terms of the expansiveness property of dynamical systems and compares to the topological stability already used in assessing stability of neural networks. This provide a novel tool to analyze neural networks providing an interesting insight in their behavior. the paper is mostly theoretical, but i does provide an analysis of what the sadowing and expansive parameter can highlight from a ResNet trained to various standard datasets.

### Strengths
- Novel approach to characterize stability, founded on a well established body of work in the field of dynamical systems analysis.
- Relatively easy to read ans self-sufficient, even though it has to introduce concepts from a foreign field.
- Interesting result comparing the shadowing property to topological stability.

### Weaknesses
 - A terse theoretical paper on the stability of ResNets might not be everyone's cup of tea (limited audience)
- The content is very dense, and some parts require to be gone over more than once.
- The experimntal results are merely illustrative, and it is hard to understand whether one might prefer this model of stability to the other in existence

### Questions
The main question would be about why this model of stability. There are many others proposed inthe literature, and while yourexperiments illustrates some interesting information about the dataset obtained by this model, it is not clear weather similar information cannot easily  be obtained from other models.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a dynamical systems interpretation of ResNets. The novelty here appears to be in the use of Lipschitz coefficients to understand stability of solutions in the context of chaotic behaviour. This is interpreted in metrics of stability and "shadowing".

### Strengths
The goal of quantifying the performance of ResNets using metrics is potentially useful for understanding the behaviour and performance of these algorithms.

### Weaknesses
The paper proposed a dynamical systems interpretation of ResNets. The novelty here appears to be in the use of Lipschitz coefficients to understand stability of solutions in the context of chaotic behaviour. This is interpreted in metrics of stability and "shadowing".

 2 fair

 1 poor

 2 fair

The goal of quantifying the performance of ResNets using metrics is potentially useful for understanding the behaviour and performance of these algorithms.

The explanation of the given metrics and how to determine them is unclear. The mathematical explanations are also unclear. There is no interpretation of the main Theorem 1 or how it relates to the numerical experiments. In addition, there has been substantial work on dynamical systems interpretations of ResNets and the work does not position itself in this literature. See questions for support for this assessment.

Specific concerns and questions are listed as follows.

1) I have seen many dynamical systems interpretations of Resnets before. However, very little of this literature is mentioned. The authors should be clearer when differentiating with previous work. A random selection of google scholar entries: "Forward Stability of ResNet and Its Variants","Understanding ResNet from a Discrete Dynamical System Perspective", "Towards Robust ResNet: A Small Step but a Giant Leap"

2) Distance $d$ has been used in Definition 1 as a distance between vectors and the same distance $d$ has been used in Definition 3 as a distance between functions. What distances do authors use?

3) ``In this context, we attempted to explore compositions of functions within the domain of H, gaining some
insights into their behavior at each processing block, even if it diverges from the conventional ResNet
structure.'' -- in what way is this diverging from the ResNet structure?

4) For $g$-expansive constant in Defn 1, the definition says that there exists $n\geq 0$ such that $d(g(\phi^n(x)), g(\phi^n(x'))) \geq \varepsilon$. How do authors find this $n$ to calculate $\varepsilon$ in Table 2?

5) Not sure I understand the definition $Sh_g(\phi,\epsilon)=\sup (\delta : \delta \in Sh_g(\phi,\epsilon))$. Same with $Top_g$.

6) In definition 3, Identity map $Id_X:X\rightarrow X$, but $H:X\rightarrow 2^X$. How do authors compute distance $d(H, Id_X)?$

7) What are the required properties of $X$ in Definitions 1 and 3? Metric space? Banach space?

8) Statement of Theorem 1. Theorem statements should not include a "we".  Also, what is $Y$ in ``g is bounded to bounded''? Also, what does it mean for a hypothesis space to have a Lipschitz constant?

9) I think that $g$-constants and Lipschitz constants do not depend on the dataset, since it is a property of function $g$ and $\phi$. Why do authors separate these constants for different datasets in Table 2?

10) There are no labels in Figure 2 and 3. If $y$-label can be assumed to be a $g$-expansive constant, there is no information about $x$-labels. Also  description and discussion about these figures (and some tables) are missing in the paper. This made it difficult to  interpret Section 4. 

11) The authors make constant use of the first person plural in a way which does not encompass the reader. This makes it seem as if the paper were about the authors and not about the result -- e.g. "we tried to look at the dynamics of ResNets," ``In the manuscript, we assumed''

12) The font of labels, legends and titles of all figures should be increased. 

Also, there are some typos and minor mistakes. 
1) Not sure why ``Dynamical Systems'' is capitalized everywhere
2) Page 3. I don't think that "Note that if $\delta \in Sh_g(\phi, \varepsilon)$ and $\delta < \delta'$, then $\delta' \in Sh_g(\phi, \varepsilon)$." is quite right. It should be $\delta'\leq \delta$.     
3) Page 6. typo "Figure 3and Table 3" $->$ "s in Figure 3 and Table 3"     
4) Page 9. Typo "initia l condition" $->$ initial condition
5) ``a directly research linked between''    
6) Formatting errors in bibliography

### Questions
Specific concerns and questions are listed as follows.

1) I have seen many dynamical systems interpretations of Resnets before. However, very little of this literature is mentioned. The authors should be clearer when differentiating with previous work. A random selection of google scholar entries: "Forward Stability of ResNet and Its Variants","Understanding ResNet from a Discrete Dynamical System Perspective", "Towards Robust ResNet: A Small Step but a Giant Leap"

2) Distance $d$ has been used in Definition 1 as a distance between vectors and the same distance $d$ has been used in Definition 3 as a distance between functions. What distances do authors use?

3) ``In this context, we attempted to explore compositions of functions within the domain of H, gaining some
insights into their behavior at each processing block, even if it diverges from the conventional ResNet
structure.'' -- in what way is this diverging from the ResNet structure?

4) For $g$-expansive constant in Defn 1, the definition says that there exists $n\geq 0$ such that $d(g(\phi^n(x)), g(\phi^n(x'))) \geq \varepsilon$. How do authors find this $n$ to calculate $\varepsilon$ in Table 2?

5) Not sure I understand the definition $Sh_g(\phi,\epsilon)=\sup (\delta : \delta \in Sh_g(\phi,\epsilon))$. Same with $Top_g$.

6) In definition 3, Identity map $Id_X:X\rightarrow X$, but $H:X\rightarrow 2^X$. How do authors compute distance $d(H, Id_X)?$

7) What are the required properties of $X$ in Definitions 1 and 3? Metric space? Banach space?

8) Statement of Theorem 1. Theorem statements should not include a "we".  Also, what is $Y$ in ``g is bounded to bounded''? Also, what does it mean for a hypothesis space to have a Lipschitz constant?

9) I think that $g$-constants and Lipschitz constants do not depend on the dataset, since it is a property of function $g$ and $\phi$. Why do authors separate these constants for different datasets in Table 2?

10) There are no labels in Figure 2 and 3. If $y$-label can be assumed to be a $g$-expansive constant, there is no information about $x$-labels. Also  description and discussion about these figures (and some tables) are missing in the paper. This made it difficult to  interpret Section 4. 
 
11) The authors make constant use of the first person plural in a way which does not encompass the reader. This makes it seem as if the paper were about the authors and not about the result -- e.g. "we tried to look at the dynamics of ResNets," ``In the manuscript, we assumed''
 
12) The font of labels, legends and titles of all figures should be increased. 

Also, there are some typos and minor mistakes. 
1) Not sure why ``Dynamical Systems'' is capitalized everywhere
2) Page 3. I don't think that "Note that if $\delta \in Sh_g(\phi, \varepsilon)$ and $\delta < \delta'$, then $\delta' \in Sh_g(\phi, \varepsilon)$." is quite right. It should be $\delta'\leq \delta$.     
3) Page 6. typo "Figure 3and Table 3" $->$ "s in Figure 3 and Table 3"     
4) Page 9. Typo "initia l condition" $->$ initial condition
5) ``a directly research linked between''    
6) Formatting errors in bibliography

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors aim to provide a theory of dynamical systems as applied to ResNets, in order to better understand their stability and robustness properties. They provide experiments using modified versions of the ResNet-18 and ResNet-50 architectures on the MNIST and CIFAR-10 datasets, and they compute constants for different dynamical systems properties applied to these architectures.

### Strengths
- The mathematical formulations in the paper seem correct. 
- The introduction covers a decent number of recent papers on the intersection between ResNet architecture and dynamical systems theory.

### Weaknesses
 - The presentation in this paper is poor. There are way too many typos, grammatical errors, and poorly written sentences; often making it difficult to understand what the authors are trying to convey. The poor writing often leads to sentences that come off as grandiose (whether intended or not), such as: _"What sets this study apart from previous research is the solid theoretical framework bridging deep learning and dynamical systems."_
- The related work is incomplete---it is limited to only closely related papers. For example, there's a lot of work connecting the training of deep nets to potential (algorithmic) stability/robustness properties, e.g. https://arxiv.org/pdf/1509.01240.pdf, http://proceedings.mlr.press/v97/du19c/du19c.pdf.
- The Experiments section is weak. The impact of experiments based MNIST and CIFAR-10 needs to be higher every year to justify using such overused datasets, and I don't think the authors demonstrated that impact here. The analysis is limited to trend analysis, and the examples are exclusively from CIFAR-10. The connection between the experimental results and the theoretical framework is not clearly established.
- The figures in the Applications section (specifically 2 and 3) are poorly constructed and hard to parse, undermining what should be the proof of the ideas laid out in the theory section. These figures do not do a good job of establishing why any of the preceding mathematical formalism is needed and/or what value it brings. The axes are not clearly labeled, and the meaning of the plotted points is not immediately obvious. The figures lack a clear explanation of how the $g$-expansive constant is calculated and how it relates to the observed trends.
- No code was provided.

### Questions
As far as I can tell, the formalism in section 2 applies to a _very_ general class of dynamical systems (essentially $\dot x(t)=\varphi(x,t), y(t) = g(x(t))$); though you keep referencing deep neural networks, images, etc., none of the stability properties are specific to those concepts. 

My question is: how sure are you that these are new concepts? For example, take your proposed new concept of "$g$-expansivity": if there is an $\epsilon$ such that
$$
g(x) \neq g(x') \implies d(g(\varphi^n(x)), g(\varphi^n(x')))\geq \epsilon \text{ for some } n\.
$$
I'm a bit skeptical that the above definition is new to dynamical systems.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
