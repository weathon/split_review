# ARTIFICIAL KURAMOTO OSCILLATORY NEURONS

- Decision: Accept
- Avg Score: 9.00
- Scores: 8, 8, 10, 10

## Abstract
It has long been known in both neuroscience and AI that ``binding'' between neurons leads to a form of competitive learning where representations are compressed in order to represent more abstract concepts in deeper layers of the network. More recently, it was also hypothesized that dynamic (spatiotemporal) representations play an important role in both neuroscience and AI. Building on these ideas, we introduce Artificial Kuramoto Oscillatory Neurons (\method) as a dynamical alternative to threshold units, which can be combined with arbitrary connectivity designs such as fully connected, convolutional, or attentive mechanisms. Our generalized Kuramoto updates bind neurons together through their synchronization dynamics. We show that this idea provides performance improvements across a wide spectrum of tasks such as unsupervised object discovery, adversarial robustness, calibrated uncertainty quantification, and reasoning. }.
\fi

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work, the authors proposed to use Kuramoto oscillatory neurons (AKOrN) to replace the usual thresholding units in deep neural networks. The basic neuron architecture can be applied to layers with different connectivity patterns, including convolutional and self-attention layers. Models with Kuramoto oscillatory neurons show promising performance in visual discovery and reasoning tasks, they are also more robust to adversarial attacks and input corruptions.

### Strengths
1. The neuronal architecture draws inspiration from physics and neuroscience and is very novel in deep learning.
2. Model performance is impressive across a range of tasks.
3. Extensive experiments show that the method applies to mainstream architectures including convolutional neural networks and transformers.

### Weaknesses
1. While AKOrN shows promising performance on the selected tasks, the model might not work as well on more "classical tasks" such as image classification. Specifically, the current evaluation lacks a direct comparison with standard convolutional networks on benchmark datasets like CIFAR or ImageNet. This makes it difficult to assess the general applicability of the proposed method. The focus on visual discovery and reasoning, while interesting, leaves a gap in understanding its performance in more established areas of computer vision.
2. Although the motivation of AKOrN is clear from a neuroscience perspective, how, and why the model shows superior performance in the tested task is not well understood. The paper lacks a detailed analysis of the internal dynamics of the Kuramoto oscillators. For instance, it's unclear how the synchronization patterns of the oscillators relate to the learned features and ultimately contribute to the model's performance. Without this analysis, it's hard to pinpoint the exact mechanisms that lead to the observed results.

### Questions
1. Judging from the method, AKOrN seems to be much more computationally costly than the usual thresholding units. I noticed that the authors controlled the number of channels in AKOrN models, but showing the training/inference time would be helpful.
2. It would be helpful to include some explicit discussion on the weakness of the method. i.e., what tasks are probably more suitable for this method and why?
3. As mentioned above, more analysis might help establish the advantage of AKOrN. For example, the paper shows that the AKOrN models show better robustness, but it is not clear from the design that they are more robust. Thus analysis of the network dynamics on some toy tasks might be helpful (e.g., synthesized classification tasks on low-dim vectors).

### Soundness
3

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
the authors propose a neural ntwork architecture in which units are high-dimensional Kuramoto oscillatory neurons. This architecture leads synchronization or 'binding' between neurons which enables competitive performance in object discovery, reasoning and robustness.

### Strengths
- the model is interesting and well defined
- the quantitative results appear impressive, though I am have some issues with their presentation (see below)
- the many numerical results presented, and comparisons to other models, suggests that overall a good deal of thought/time has been put in the manuscript

### Weaknesses
 - there are numerous minor issues with the text/presentation (see question below) which impacts the clarity of the paper 
- This not a field I have experience in, but I am not entirley convinced a fair comparison was made to other models for object discovery. Is the idea that AKOrN is a highly competitive model for models 'trained from scratch', and that comparing it to models with some pretrained parameters (e.g. Lowe et al. 2024) is unfair? I think this could be better clarified if so
- there is a notion from the abstract and sections 1/2 that this work is relevant to neuroscience, but the link feels quite tenuous to me. Is it reasonable to think of neurons as high-d points on a sphere?

- The format of figure references could be improved. I would recommend references as 'Fig. X'. Currently there is either the period missing or there's no space (e.g. 'Fig1' on line 96). Same with Tab X -> Table X. Should also be Figs for multiple figures (not Fig as in line 368)
- line 36: 'we follow a more modern dynamical view of neurons as oscillatory units'. Is this correct? Oscilliations have been studied in the brain for a long time; moreover, I would say that the majority of computational neuroscientists currently model neurons as scalar values.
- For table 3 results are presented with error bars over 5 seeds (which I favour), why is this not the case for any of the other results presented?
- line 121: 'we introduce a multi-dimensional vector version of the model' - this line is confusing as this was already employed by Chandra et al. and Lipton et al. (as cited). Perhaps replace with 'incorporate a mutli-dimensional model...'. On this subject could you clarify to me the exact novelty of the model? Is it that it's not been introduced in deep neural nets before? Or is it about the fact connections between oscillators J is not symetric in AKOrN? Relatedly, line 308 'our..models differ from these approaches in various aspects such as...' should really provide all fundemental differences beyond some examples. In fact, in any case what's the difference between 'asymmetric connections' and 'their symmetry breaking term'? 
- line 123 (and other places): what's C? the size of the neural population? this should be clarified
- line 245: what is 'proper' energy?
- line 323: I don't understand how these convolution/self-attention layers are iterated upon. What are the shared parameters?
- I didn't understand the implementation for the sudoku task. 1. is the entire 9x9 soduku grid fed all at once, or one digit at a time? and 2. how come x_i takes the value c_i when a digit is given, does the model no longer follow equation 2? Or is this just the initial value taken before the Kuramoto steps?
- line 425: 'the energy is a good indication of the solution's correctness'. Why? I can believe that stability is often a desirable thing in tasks but think this line deserves some elaboration
- line 464: would it be possible to give a brief description/overview of what 'common corruptions' are?
- line 506: why is it surprising that confidence and accuracy are linearly correlated? 
- line 527: 'the oscillator...'. I didn't understand the logic of this sentence, could you explain it to me please?

Other comments:

- the notation x_{chw} is confusing, I think x_{c,h,w} is better
- on line 201 the terms should be switched around (the initial state of the next block is the thing being defined). But also, how does this fit in with line 189 where X^(l,0) = X^l?
- the metrics in all of the tables should be clarified. I presume the unit is %, but e.g. in the case of Table 1 I'm not entirely sure what the metric is. % objects correctly identified?
- in the results section the language can be overly strong. For example 'far better' (line 377) and 'vastly better' (line 416) do not appear to me as very scientific language. 
- in the discussion there is talk of small N resulting in a strongly regularized model. Given that the size of N nor regularization was mentioned in the prior text, this comes rather abruptly as is confusing to the reader

typos: 
- line 150: 'set C a silhouette' -> 'set C as a silhouette'

### Questions
- The format of figure references could be improved. I would recommend references as 'Fig. X'. Currently there is either the period missing or there's no space (e.g. 'Fig1' on line 96). Same with Tab X -> Table X. Should also be Figs for multiple figures (not Fig as in line 368)
- line 36: 'we follow a more modern dynamical view of neurons as oscillatory units'. Is this correct? Oscilliations have been studied in the brain for a long time; moreover, I would say that the majority of computational neuroscientists currently model neurons as scalar values.
- For table 3 results are presented with error bars over 5 seeds (which I favour), why is this not the case for any of the other results presented?
- line 121: 'we introduce a multi-dimensional vector version of the model' - this line is confusing as this was already employed by Chandra et al. and Lipton et al. (as cited). Perhaps replace with 'incorporate a mutli-dimensional model...'. On this subject could you clarify to me the exact novelty of the model? Is it that it's not been introduced in deep neural nets before? Or is it about the fact connections between oscillators J is not symetric in AKOrN? Relatedly, line 308 'our..models differ from these approaches in various aspects such as...' should really provide all fundemental differences beyond some examples. In fact, in any case what's the difference between 'asymmetric connections' and 'their symmetry breaking term'? 
- line 123 (and other places): what's C? the size of the neural population? this should be clarified
- line 245: what is 'proper' energy?
- line 323: I don't understand how these convolution/self-attention layers are iterated upon. What are the shared parameters?
- I didn't understand the implementation for the sudoku task. 1. is the entire 9x9 soduku grid fed all at once, or one digit at a time? and 2. how come x_i takes the value c_i when a digit is given, does the model no longer follow equation 2? Or is this just the initial value taken before the Kuramoto steps?
- line 425: 'the energy is a good indication of the solution's correctness'. Why? I can believe that stability is often a desirable thing in tasks but think this line deserves some elaboration
- line 464: would it be possible to give a brief description/overview of what 'common corruptions' are?
- line 506: why is it surprising that confidence and accuracy are linearly correlated? 
- line 527: 'the oscillator...'. I didn't understand the logic of this sentence, could you explain it to me please?

Other comments:

- the notation x_{chw} is confusing, I think x_{c,h,w} is better
- on line 201 the terms should be switched around (the initial state of the next block is the thing being defined). But also, how does this fit in with line 189 where X^(l,0) = X^l?
- the metrics in all of the tables should be clarified. I presume the unit is %, but e.g. in the case of Table 1 I'm not entirely sure what the metric is. % objects correctly identified?
- in the results section the language can be overly strong. For example 'far better' (line 377) and 'vastly better' (line 416) do not appear to me as very scientific language. 
- in the discussion there is talk of small N resulting in a strongly regularized model. Given that the size of N nor regularization was mentioned in the prior text, this comes rather abruptly as is confusing to the reader

typos: 
- line 150: 'set C a silhouette' -> 'set C as a silhouette'

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
- This paper developed a feature-rotation-like neuron models (high-dim feature rotation encodes synchrony binding), a promissingly neuron-level building block that can be combined with diverse network architectures, like CNN and transformer. 
- The capability of the new architecture is validated on three independent tasks: object discovery (synthetic & natural image), reasoning on Sudoku task, robustness w.r.t adversarial attack in CI
FAR10. 
- On each task, the proposed model shows SOTA performance and interesting shining points: (1) For object discovery, the model scales to natural image without pretrained DINO model; (2) for reasoning, the model's correctness is naturally implied by the "internal coherence", indicated by the task-independent energy measure; (3) for adversarial attack, robustness seems a built-in property of the dynamics and again, the energy could imply the accuracy.

### Strengths
I enjoyed reading this paper, impressed by the achievements on diverse tasks and also the authors's thoughts dispersed over the paper.  In brief, the strength of the paper includes:
- Soft grouping/clustering in neural network is an important question and often missing in main-stream ANNs.
- The proposed neuron model is neuroscientific motivated yet has concise fomula. The physical origin of the model makes it plausible to construct an "energy function", which turns out to be quite informative on the performance.
- While previous work on binding by synchrony mainly focuses on object discovery, the author extends these insights into reasoning tasks, and adversarial attack. And the performance on these new tasks is very successful.
- Lastly, the author provides a different conceptual angle for the binding by synchronization: the synchronization enables competitive learning, and therefore compresses representation to construct a bottle neck, which facilitate abstraction. As far as I know, it is a novel argument not presented in previous works and it also makes sense to me.

### Weaknesses
For the weakness:
- It is not clear what is the actual conceptual contribution / nolvelty of the Kura model proposed in this paper compared with Lowe's Rotating Feature (and recent updates). For example, equation (6) is very similiar to the "binding mechanism activation" in  [1] and I have the intuition that this is the essential mechanism for the binding ability of model, similiar to [1]. If I am wrong, please correct me.
- When generalizing the original Kura model to high-dim, it is not clear whether the Proj in eq(2) is an 'equivalent' generalization of $sin(\theta_j-\theta_i)$. So it is not clear how much this term actually contribute to the computation of the network. Note that $sin(\theta_j-\theta_i)$ is a essential mechanism in original Kura model to guarentee the synchrony as a stable state and sin acts among each pair of neurons before the $\sum$, but Proj only acts after the $\sum$. (The first two concerns are mainly about how "Kura" the model is ?)
- Since the activity is constraints on the sphere, it loses the representational ability for encoding feature presence, which is an important conceptual diaviation from synchrony binding idea and is likely to limit its ability to infer in certain cases, e.g. when the feature is uncertain or weakly related to the task.
- On the experimental side, it mostly ignored the Lowe's model for comparison (Fig.3, Fig.4,Fig.5,Tab.1,Tab2, Tab3...) and other synchrony based model, e.g. [2].
- The code is not provided, so it is hard to evaluate the the reproducibility of the results.
- The author misses several essential recent works: e.g. [2] shows how oscillation emerges in spike-based model to bind features; [3] combine Kura model with ANNs and also achieved synchrony binding.
- The first two sentences in Abstract is quite confusing and the first paragraph in Introduction is not very informative.

### Questions
(1) For the claim in the paper: 
> “binding” between neurons leads to a form of competitive learning where representations are compressed  in order to represent more abstract concepts in deeper layers of the network. 

> In fact, neighboring neurons tend to cluster their activities, and clusters tend to compete to explain the input. This “competitive learning” has the advantage that information is compressed as we move through the layers, facilitating the process of abstraction by creating an information bottleneck. Additionally, the competition encourages different higher-level neurons to focus on different aspects of the input (i.e., they specialize). This process is made possible by synchronization: like fireflies in the night, neurons tend to synchronize their activities with their neighbors’, which leads to the compression of their representations.

Can author clarify the reference if such claim is well-documented? If it is the novel claim of the author, the author should modify the tone to avoid overclaim or provide rationale or experiments to make sense of such claims.

(2) (Weakness section). What is the contribution of the "Proj", and will there be synchronization, e.g. given input image, if we replace Proj into general linear sum (ablation of Proj)? And what is the difference between eq(6) and binding mechanism in Lowe's work? Since the binding mechanism itself can generate synchronization, how to disentangle the contribution from (6) to contribution from the "Kura idea".

(3) Can author shows the segmentation results on binary datasets, like Zheng2024. The different color of object may make it eaiser to break symmetry compared with binary images. e.g. in Fig.4 the segmentation is more likely based on color instead of object-instance (the highlight is treated as an object). Besides, what is the actual input dimmension of the image to the model? To what extent it is downscaled?
(4) Why the energy function still make sense even if the J and $\Omega$ is not constraint by symmetry?
(5) What is the rationale of robustness? Is it the general outcome of dynamical models or is it the outcome of this Kura model? I suggest compare with related non-synchrony dynamical ANN models to disentagle the causal-effect.
(6) Why energy function, or the synchrony level in the network, can indicate the task performance? Can the author explain that more solidly?
(7) For the Sudoku task, can the author compare with those Ising-based models? e.g. Hopfield network or modern hopfield network. So as to disentagle the contribution for the "Kura idea" from that generally comes from attractor dynamics.

In general, I would like to vote for the accept of the paper, but I will also revisit the evaluation based on the author's response and other reviewer's comments.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper proposes a novel type of neural network where neurons’ activities are defined on the unit sphere (in N-dimensional space, where N is typically 2 or 4), and are updated based on Kuramoto equations. This can model oscillatory dynamics that can be leveraged for binding activations across neurons. The model is applied to various settings (unsupervised object discovery, image classification adversarial or natural noise robustness, Sudoku problem solving) and compared against relevant baselines (e.g. slot-based models, Transformers), each time demonstrating competitive performance. The model has clear potential to improve the state-of-the-art across domains.

### Strengths
* A biologically inspired architecture, well described and motivated by neuroscientific findings
* A thorough set of experiments across diverse machine learning domains
* Meaningful comparisons with baselines revealing competitive performance

### Weaknesses
 * The dependence of the model on the choice of dimensionality N, although it is explicitly acknowledged in the paper, warrants further investigations (which can be the goal of future studies)
* Although baselines are roughly matched for memory/parameter size and flops, it is possible that GPU optimizations will make them more efficient than the AKOrN versions. There is unfortunately no discussion of this issue nor any report of absolute time required for training or inference. This could be added to the Appendix.

### Questions
* on Lines 140-141, you argue that “we found that the use of C is necessary for stable trainings […] as a symmetry-breaking field”. But isn’t C also –and more simply—required for the network to receive inputs, and thus to perform any useful function?

### Soundness
4

### Presentation
4

### Contribution
4
