# Approaching Deep Learning through the Spectral Dynamics of Weights

- Decision: Reject
- Scores: 5, 6, 6, 8

## Abstract
We propose an empirical approach centered on the spectral dynamics of weights---the behavior of singular values and vectors during optimization---to unify and clarify several phenomena in deep learning. We identify a consistent bias in optimization across various experiments, from small-scale ``grokking'' to large-scale tasks like image classification with ConvNets, image generation with UNets, speech recognition with LSTMs, and language modeling with Transformers. We also demonstrate that weight decay enhances this bias beyond its role as a norm regularizer, even in practical systems. Moreover, we show that these spectral dynamics distinguish memorizing networks from generalizing ones, offering a novel perspective on this longstanding conundrum. Additionally, we leverage spectral dynamics to explore the emergence of well-performing sparse subnetworks (lottery tickets) and the structure of the loss surface through linear mode connectivity. Our findings suggest that spectral dynamics provide a coherent framework to better understand the behavior of neural networks across diverse settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose an empirical approach centered on the spectral dynamics of the behavior of weights during optimization and they find that 1) Grokking is intimately linked to rank minimization; 2) Rank minimization is a general phenomenon in more complex tasks; 3) Weight decay acts implicitly as a low-rank regularizer; 4) Generalizing solutions have a lower rank than memorizing ones; and 5) Top singular vectors are preserved when performing magnitude pruning and while linearly interpolating between connected modes. 

Those phenomena provides a coherent framework to understand the behavior of networks across different settings.

### Strengths
1) This paper is clearly written and the idea is easy to follow.
2) The authors connect simple settings (grokking) to complex ones (LSTMs, transformers), and explore tasks from different domains including image, speech and language processing tasks. This shows that the rank minimization is a common property for people to understand deep neural networks.

### Weaknesses
As this paper is mainly empirical, it would be better to see more results of different tasks in each domain to give more evidence for the observed properties, as one task in each domain might not be enough to say they are general phenomena.

### Questions
This paper is clearly written and I do not have other questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper surveys the spectral dynamics of the weights of deep neural networks in several settings, attempting to draw some general conclusions from the commonalities in the observed dynamics. In particular, the authors examine the singular values of weight matrices in the network, the alignment between singular vectors of consecutive layers, and the effect of weight decay on the dynamics of these quantities. They find that neural network training is biased towards low-rank solutions with only a few singular modes dominating information processing after training, in line with previous theoretical and empirical findings. This effect is shown to be more pronounced with higher weight decay. They also find that the alignment between layers is not quite as strong as prior theoretical work has suggested, and requires further study. The paper also reports interesting connections between spectral dynamics and deep learning phenomena such as grokking, generalization, memorization, lottery tickets, and linear mode connectivity.

### Strengths
- Spectral analysis of the weights is an informative approach that has yielded several theoretical insights in linear networks and informed empirical algorithms, particularly in recent approaches for low-rank adaptation. In the past, such analyses have been done in isolation on simple setups. So this paper's attempt to extend the scope of the insights into something more general is novel.
- The comprehensive experiments touch upon a wide array of observed phenomena in deep learning and generally support the idea that the top singular subspace is more important for task performance.
- Some of the findings were surprising, and call for further study. For instance, panel d in Figure 2 shows an increasing alignment that moves up the ranks over training, suggesting the evolution of the relevant functional low-rank subspace.
- I also found the differences between random label learning and true label learning to be interesting. This nicely highlights how the task structure implicitly shapes the network over learning.

### Weaknesses
I have some critiques concerning the writing, particularly the lack of any solid insights. I elaborate below.
- The paper seems to be largely an exercise in plotting the singular value dynamics of several neural networks. While this is interesting in itself, I found that the paper did not extract any conclusive or striking insights from the empirical study, making it difficult to judge the significance of the work. For example, Figure 2 points out that grokking seems to be correlated with drops in the effective rank. This is interesting, but no concrete mechanistic explanation for this effect is attempted. A similar tone pervades the paper, with several disparate empirical reports but no substantive specific hypothesis or overarching message about the phenomena being observed. I understand that the paper is primarily empirical, but the paper would be much more compelling if the reader is given more details as to the significance of each finding or its implications for practitioners.
- A few concrete insights are indeed pointed out, such as weight decay implicitly promoting a low-rank bias. I appreciated the arguments provided for developing an intuition for this effect (lines 410-420). While interesting, this was not investigated in sufficient depth to clear the bar for acceptance of the paper. Furthermore, the reasoning for looking into this effect (lines 193-197) seems somewhat vague. 
- The lack of a core message is also reflected in the writing. For instance, the abstract mentions a "consistent bias in optimization" (line 13) but doesn't specify what this bias is at all. Similarly, I found the introduction perhaps too long but unspecific. It briefly describes several prior works that could be better placed in the related work section. More importantly, I found it difficult to appreciate what is the main question that is being asked. The closest was the "aim to provide a common language for probing and understanding neural networks" (lines 144-145), but still, such a language had not been specified in detail by the end of the paper. I think the paper could be much improved by addressing just these few aspects and being more specific about the core message of the paper.
- In general, I also found the treatment of prior work a little lacking in details. While I appreciate the comprehensive literature that was cited, I think the paper could benefit from closer tailoring of the references to a more specific core message.

### Questions
- What could be the reason for not observing a strong alignment between layers as proposed in the existing theory? Why does the alignment appear and then go away? I found this surprising and would like to hear what the authors think.
- The spectral dynamics are different between training with random vs true labels. But how could this insight be leveraged to distinguish memorization vs generalization between different networks trained on the same task? Would the idea be that the higher rank network is more memorizing?

### Soundness
3

### Presentation
2

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
This paper presents a framework based on spectral dynamics—the evolution of weight singular values and vectors during training—to unify key deep learning behaviors. The authors reveal a consistent optimization bias across diverse tasks, from image classification to language modeling, and demonstrate that weight decay strengthens this bias beyond norm regularization. Spectral dynamics also distinguish between networks that memorize versus generalize, offering insights into effective sparse subnetworks (lottery tickets) and the structure of loss landscapes through linear mode connectivity.

### Strengths
The paper introduce some situations in deep learning and explain them by the spectral dynamics of weights. The advantages are

 1) The paper establishes a link between ''grokkking'' and rank minimization.

 2) The paper provides different examples of deep learning, including CNN, UNet, LSTM, and transformer.

### Weaknesses
1) There is no clear description of the influences of spectral dynamics on deep learning. For example, in the line 421, weight decay can produces a low-rank behavior, but how much weight decay is needed or is weight decay related with some performance metrics? Figure 6 shows a phenomenon of adding weight decay. However, there lacks a metrics to show the level of weight decay. "The exact choice of “too much” varies across architectures and tasks." could not explain everything. Specifically, the paper lacks a quantitative analysis of how the magnitude of weight decay affects the spectral properties and, subsequently, the generalization performance. It is unclear how to choose the optimal weight decay value for a given task based on the presented spectral analysis. The paper should provide a more concrete guideline or metric to determine the appropriate level of weight decay, rather than stating it varies across architectures and tasks. For example, a study of the relationship between the weight decay coefficient and the effective rank of the weight matrices, along with the corresponding performance on validation set, would be beneficial.

2) The theoretical foundation is weak, providing limited intuition and isolated examples rather than a cohesive theory. In section 4.1 and 4.2, the authors provide the visual processing of trainings, but there is no explanation and theoretical analysis. The authors should provide more accurate analysis rather than only visualization. The paper presents visual observations of spectral dynamics during training but fails to provide a rigorous theoretical framework to explain these observations. For example, while the visualizations in Sections 4.1 and 4.2 are interesting, they lack a formal analysis of why certain spectral patterns emerge during training. The paper should include a theoretical analysis that explains the observed spectral dynamics, such as relating the spectral changes to the optimization landscape or the learning dynamics. Without such a theoretical foundation, the results remain descriptive rather than explanatory.

3) The conclusion of the paper seems to be too simple and not rigorous. It provides some right but not useful insights. In section 6, the authors provide additional connections between spectral dynamics and other phenomena. However, the connections seems to be verfied by previous works, the paper only provides some examples and visualizations of these connections. The paper's conclusions lack a strong theoretical basis and do not offer concrete, actionable insights. The connections made in Section 6, while interesting, are not sufficiently novel or rigorously demonstrated. The paper should provide a more in-depth analysis of these connections, going beyond simply showing examples and visualizations, and should provide a more rigorous analysis of the implications of these connections.

### Questions
Please see the weakness.

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
3

### Summary
This paper proposes to inspect the evolution of singular values & vectors of weights in training to gain mechanistic interpretability in deep learning. Experiments are conducted on various tasks with various models. Results shed light on grokking, low-rank weights, weight decay, and alignment between adjacent layers.

### Strengths
- This paper is well-written. The phrasing is polished. The literature review is mostly comprehensive. The problem is motivated well with an insightful introduction. I enjoyed reading it.
- The authors use the tool of spectral dynamics to examine a wide variety of tasks and analyze many recent outstanding questions in deep learning.
- Extensive experiments are carried out to provide information for the analysis.

### Weaknesses
 - The authors reviewed some prior theoretical papers and mentioned that they often cannot explain seemingly relevant phenomena in practice, which I appreciate. But in the same spirit, there are probably cases where this paper's tools cannot explain either. Could the authors give a few such instances or some relevant insights? For instance, in line 118, the authors write that any arguments about generalization cannot be capacity-based alone. Then I wonder whether arguments about generalization can be spectral-dynamics-based alone. Are there cases where the generalizing solution has a higher rank than the memorizing solution? If yes, perhaps the conclusion in line 140 should be revised or stated with more caveats.
- For the architectures studied in this paper, except for MLPs, there is not a very standard definition of alignment off the shelf. As mentioned in the Appendix, the authors tried a few different definitions before settling on the current version. So I am wondering if the results vary much with different ways of evaluating alignment.



### Questions
- In top row of Figure 2(a), why is there a large blue shaded region? The caption doesn't introduce what the shade represents. My first guess is the standard deviation but the shade reaches negative values.
- In top row of Figure 2, is the model a one-layer transformer? If so, why are there 6 layers in Figure 2(c) and 50 layers for a 12-layer transformer in Figure 3(d)?
- In line 359, why can't the last layer be pruned?
- In line 395, the authors state that the absence of alignment is reminiscent of Mulayoff & Michaeli. Mulayoff & Michaeli found that the alignment appears with GD and SGD with reasonable stepsizes and may break for GD with a large stepsize. So I'm wondering if absence of alignment in Figure 5 is due to large stepsizes and can be recovered if a smaller stepsize is used. Also, if I'm not mistaken, the assumption of whitened input is not necessary for alignment in linear networks.

### Soundness
3

### Presentation
3

### Contribution
3
