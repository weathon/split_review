# Task adaptation by biologically inspired stochastic comodulation

- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 5, 3, 5

## Abstract
Brain representations must strike a balance between generalizability and adaptability. Neural codes capture general statistical regularities in the world, while dynamically adjusting to reflect current goals. One aspect of this adaptation is stochastically co-modulating neurons' gains based on their task relevance. These fluctuations then propagate downstream to guide decision making. Here, we test the computational viability of such a scheme in the context of multi-task learning. We show that fine-tuning convolutional networks by stochastic gain modulation improves on deterministic gain modulation, achieving state-of-the-art results on the CelebA dataset. To better understand the mechanisms supporting this improvement, we explore how fine-tuning performance is affected by architecture using Cifar-100. Overall, our results suggest that stochastic comodulation can enhance learning efficiency and performance in multi-task learning, without additional learnable parameters. This offers a promising new direction for developing more flexible and robust intelligent systems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates stochastic modulation as a mechanism for adapting neural circuitry to task in large vision models. Motivation comes from biological neural networks' ability to modulate neural responses in a task-dependent manner, suggesting that this may be effective in artificial NNs and that trying it may shed light on biological NNs.

The method is centered on fine-tuning by comodulation. Extending on prior work, the method begins with a pretrained model (here, image models) and a pretrained controller that maps from task indication to task-dependent comodulation as context weights, which ideally magnify task-informative neurons while inhibiting task-irrelevant neurons. Furthermore, a stochastic modulator generates noise to apply to decoder activations. Models are trained on a primary task then tuned on a different but related task; at this point, only coupling weights change. 

Experiments are performed on CelebA (40 binary tasks, some as primary and some as secondary, each with the same input image distribution) and CIFAR-100 (one classification task into 20 superclasses, then a fine-tuning classification task into 100 classes). 

The paper finds that comodulation enables convergence in far less training than in other multi-task learning-related fine-tuning methods, though with more tuning, deterministic attention (another mechanism inspired by enhancing certain neurons and suppressing others) performs similarly. Furthermore, the paper discusses that CIFAR-100, residual connections improve comodulation, comodulation shrinks decoder noise, and comodulation improves the model's confidence calibration.

The paper concludes that comodulation can help achieve SOTA results, faster training, and better calibration than deterministic gain modulation in some conditions. It is an open question which specific conditions this applies to. The paper argues that the results also demonstrate stochastic modulation to be a computationally viable candidate for contextual fine-tuning in an animal brain.

### Strengths
#### Quality
- Paper is well-motivated by biological systems and a natural problem for ML
- Experimental setup is thorough. 
  - Particularly clever: training/fine-tuning division on CelebA vs. CIFAR-100 requiring two different types of shifts of distribution
- Results are laid out and analyzed well. While the main claims are a bit disorganized, they are all backe dup and convincing, even if at a small scale. 

#### Clarity
Paper is very well written. 


#### Originality
No originality concerns - paper is well-grounded within prior literature. 


#### Significance
The paper is contextualized well in both biology and ML literature, which can be difficult. The improvements on various datasets are nontrivial, and compete with similar types of work in ML. Experiments with the fine-tuning done on larger and more complex datasets would be good for sending a solid ML message, but this is already an interesting contribution.

### Weaknesses
#### Quality
- Final results might need more grounding to actual neural data to claim that this paper has made stochastic modulation seem more like it might be used in the brain. "Might be a computationally viable candidate" is technically accurate, but the language still feels overall overstated with respect to how much these results mean for the actual brain. 
- While this may be a matter of my not knowing prior work, the mechanism isn't clearly anchored in prior work - even after the experiments section, there's only a vague sense of it. There is one exception, where in the methods section it's made clear what the methods are built off of - more of that might be helpful.

#### Clarity
- It really is hard to see in many of the figures why we should be excited about the differences in the curves. Annotating or zooming in to ground them quantitatively would help.
- "Deterministic gain increases" and "calibration of confidence" are brought up in the intro but not defined until the methods/results, which is confusing. 
- Figure 1 should be connected to text earlier than Equation 1 - it's hard to understand what on the figure is referring to what in the paper. 
- Figure 1: unclear how the stochastic modulator originates and interacts with the decoder. The controller has task info embedded, but Fig 1 + text makes the stochastic modulator look both like it comes from the controller and like it's purely randomly sampled. Which is it? 
- Table 1 would benefit from far more annotation - it's a lot to take in right now, and the text only refers to it as a whole (or it refers to specifics that are hard to find and hold in memory). 
- Minor: the paper says the task is given as a one-hot, but the figure makes it seem like a binary representation of some kind.

#### Significance
To some degree it's unclear which audience this paper is for - for neuroscientists, there's almost no quantitative grounding in neural data. That said, the paper seems primarily geared toward the ML community - here, more/larger-scale experimentation would help but the results do show clear and consistent improvement. I think this is a smaller but well-scoped paper that points to interesting further research along with making a contribution. 


#### Minor
In the "network embeddings" paragraph in page 5, the paper refers to fig 2D; I think it should refer to fig 2C.

### Questions
- How exactly is the stochastic modulator signal integrated into the decoder, and how is it generated? Does it come from the controller or a totally random sample? How does that reflect on Fig 1?
- "Maps individual tasks into the context weights" - did you mean "to"?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a novel task adaptation technique for multi-task learning based on task-specific stochastic comodulation of neurons. The proposed approach modulates a pretrained backbone's (ResNet-18) response using iid gaussian noise ($m_t$) for stochasticity, combined with a learned representation of context information ($c_k$) and forwarded to an MLP decoder. For each downstream context $k$, the readout is obtained by scaling the decoder's activations using a context-dependent gain ($g_k$). The above described comodulation process repurposes the outputs from a strong pretrained backbone to be used for a variety of downstream tasks by identifying (and scaling) task-relevant neurons from the backbone. Results on Celeb-A and CIFAR-100 show the merits of comodulation in producing improved performance (as measured by F-score) and prediction confidence calibration. The authors also include analysis of comodulated network's internal representations to show that they learn semantically rich decoder and context representations.

### Strengths
+ This submission explores repurposing a pretrained backbone's representation with minimal finetuning and extra parameters to improve performance in diverse downstream contexts. This work is highly relevant in this era of strong pretrained visual backbones, and using their representations to perform multiple downstream tasks.
+ The evaluations are quite rigorous with multiple random intializations of all models used to report variance in performance.
+ Analysis of networks trained with comodulation using CIFAR-100 was really interesting, and it was impressive (although not clear why) that comodulation improves calibration of prediction confidence.

### Weaknesses
 - The improvements produced by comodulation over attention seem quite marginal and tend to diminish as the number of pretraining epochs increases. It is true that as backbone size increases, pretraining becomes less of a viable option, but the small gains over attention regardless (with few pretraining epochs) makes the work less exciting.
- I found the writing to be clear overall, but felt that the Methods section could be further revised for improving readability. E.g. (1) the reader isn't aware of what $h^{J}_t$ is the first time it appears at the bottom of page 3; (2) is $h^{J-1}_k$ in Eqn. 3 the output of the second encoder layer (i.e. $h^{l+1}_k$? (3) citations appear to be in the wrong format in a few places and needs to be corrected
- Although the attention baseline is repeatedly evaluated in many parts of the paper, I couldn't find a mathematical description of this approach, adding which would improve the clarity of this work.

### Questions
Please refer to my weaknesses section above. Clarifying my questions and improving the readability of this work will help improve my rating of this submission.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces biologically inspired stochastic co-modulation as a way to modulate the context of a multi-task learning framework and improve performance. Neural networks are fine-tuned with stochastic modulation gains. The authors show an increase in performance compared to non-stochastic gains, and claim that the networks train more efficiently when stochastic co-modulation is present.

### Strengths
This paper connects recent work investigating context-dependent stochastic co-modulation in biology to the multi-task learning setting, showing that it can be beneficial as a way to fine-tune the network performance. This is generally of interest to both neuroscience audiences and machine learning practitioners. I also found the experiment on CIFAR-100 (training on the 20 superclasses and fine-tuning on the 100 classes) to be an interesting way to connect perceptual learning experiments in neuroscience. The authors also demonstrated a notable improvement using stochastic co-modulation compared to the other tested models, particularly in terms of the recall score.

### Weaknesses
1. **Clarity of writing** Overall, I found the writing of the paper quite hard to follow. A lot of ground is covered by their experiments, and the motivation is often unclear (for instance, explaining the two versions of the experiment described on page (6) for the “Image Classification” experiment). Additionally, in many places of the paper, there are ad-hoc observations that are not fully explained, for instance, in the footnote on page (5) or the explanation about “network weights overfitting too much on the training set” on page (5). There are also terms that are not well defined, for instance when referring to the “reliability diagrams” on page 7, where “reliability” is not explained. These are just a few examples, and I encourage the authors to revise the text to make it more clear for the reader.
2. **Experimental details seem ad-hoc** The training setup seems a little odd. As far as I can tell, for the CelebA experiment, the authors (1) took a pre-trained ImageNet backbone (2) trained the whole network on the full task (3) fine-tuned just the controller parameters. This makes it difficult to compare the “efficiency” of training because there are many stages involved. Can the controller not be trained at the same time as the encoder/decoder (and if so, is this due to training problems or due to some experimental design choices)?  
3. **Evaluation Metrics** The sharp drop in Precision for the proposed stochastic comodulation is somewhat troubling, and the resulting explanation seems insufficient. Even if it is unintentional, it makes the metrics used for comparison seem somewhat designed to ensure that the comodulation model is listed as “best.”

### Questions
a. Is it typical to first train the entire network on all tasks and then fine-tune it on the same dataset? I am most familiar with work that fine-tunes for new tasks, so just clarifying whether this is a standard choice would be helpful. 

b. I’m a bit confused by the sentence “In other words, when a network predicts class C with a probability of 0.4, the probability that the network is correct is 0.4.” in the “Comodulation improves confidence calibration” section on Page 7). Is there a typo? If not, could you explain this in more detail, as I don’t understand how this could be correct as written. For instance, if Class C is only ever encountered <0.01% of the time then the network will be correct with a probability significantly less than 0.4, right? 

c. In Table 1, are the comparison “state of the art” methods computed on models that were trained in the same environment that is used in this paper, or are these taken directly from the cited papers? This detail seems important to clarify, as there might be other underlying differences. 

d. Could the authors provide further explanation of the deterministic “attention” model? I could not find details of this in the paper. This seems particularly important to explain, given that it is one of the critical comparisons and does best on the “Precision” metric. Is this attention just the controller without a stochastic element, and if not, why is something along those lines not a direct comparison? 

e. As a followup to (d), did the tuning of hyperparameters for training etc. for this “attention” model receive as much tweaking as the co-modulation comparison? It is a little puzzling to me that there is very little change in the representations after fine-tuning here, and so I wonder if it is the stochastic co-modulation that is actually helping, or if the “attention” case had hyperparameters that did not behave well with the training setup.  

f. On page 4 there is the sentence “...we only use stochasticity to compute the gain, but we use unperturbed representations for decision making.” This doesn’t make sense to me – isn’t the gain perturbing the representations? Or is stochasticity somehow turned off during the testing (and only on during training?) 

e. Minor: there should be a comma in “recall, precision and F1-score” on page 5.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a neuroscience-inspired method to enhance multi-task adapation in deep learning. In particular, it proposes stochastically co-modulating neurons' gains based on their task relevance in multi-task adaptation problem. The methodology involves mechanisms of stochastic comodulation and neural architectures design. Numerical experiments have been conducted in CelebA and CIFAR-100 datasets, where the experimental settings were slightly different. The experimental results demonstrate the effectiveness of the proposed method. The paper also investigates the mechanisms supporting this improvement by a range of visualizable analysis. Overall, the paper is an interesting attemptation in the adaptation in multi-task learning, while there remains some space to improve.

# Post-rebuttal 
While I appreciate the authors for the responses and clarifications, they do not solve my concerns (e.g., no addtional experiments on ImageNet or CoCo). Therefore, I will keep my original recommendation.

### Strengths
1. The proposed stochastic comodulation method is simple and effective, as well as faster in convergence.

2. The paper provides comprehensive and interesting analysis about the learned model properties (Figure 3-6).

3. This work shed light on understanding stochasticity nature of neural representations in the brain.

### Weaknesses
1. While it is interesting to see a bio-inspired algorithm, I found the motivation is a bit hard to follow without the background knowledge about "co-modulation" in the brain. There is somehow a gap between the neuroscientific findings and the proposed deep learning methodology in this paper (I have not read the preset papers (Haimerl et al. 2019; 2022)). Specifically, the paper does not clearly articulate how the biological concept of stochastic co-modulation directly translates into the proposed gain modulation of neural activations within the deep learning model. The connection between task-relevance tags and the stochastic modulation of neuronal gains needs further clarification, particularly regarding how these tags are generated and how they influence the modulation process. The paper would benefit from a more detailed explanation of the biological plausibility of the proposed mechanisms, bridging the gap between neuroscience and deep learning.

2. The novelty of this paper is unclear in presence of (Haimerl et al. 2022). The paper states that it extends the model of stochastic comodulation, but the exact differences in methodology and task settings are not clearly defined. It is difficult to assess the contribution of this work without a detailed comparison to the previous work. A more precise explanation of the novel aspects, such as the controller for dynamic neuron selection and the specific multi-task learning context, is needed to establish the paper's unique contribution. The paper should clearly delineate what aspects of the method are novel and what is built upon prior work, providing a clear understanding of the advancement made.

3. The testbeds could be more extensive. The evaluation is limited to CelebA and CIFAR-100 datasets, which are relatively small and may not fully demonstrate the scalability and robustness of the proposed method. The paper lacks experiments on more challenging datasets such as ImageNet or COCO, which are standard benchmarks in the field. The absence of these experiments makes it difficult to assess the generalizability of the proposed method to more complex and realistic scenarios. The paper should include experiments on more diverse and challenging datasets to provide a more comprehensive evaluation of the method's performance.

Minor:
- Colors in Figure 1, 2, 3,5 is not friendly to color-blind readers (especially red-green), consider using different marker/line styles instead.
- Plot labels in Figure 5 are too small and hard to recognize on printed paper.
- REPRODUCIBILITY STATEMENT: Pytorch -> PyTorch
- Is there any reason that Haimerl et al. 2022 used the term "co-modulation" but this paper use "comodulation"?

### Questions
1. The paper wrote "We extend the model of stochastic comodulation presented in Haimerl et al. (2019; 2022) ...". Could the authors explain in more details about the relationship between the current paper and (Haimerl et al. 2022), including methodology, task setting etc. ?

2. I also wonder how the presented stochastic comodulation method perform on more challenging dataset such as ImageNet and COCO. Is there any reason that ImageNet was not tested? 

3. It might be interesting to investigate whether stochastic comodulation could mitigate the notorious catastropic forgetting problem in continual/lifelong learning, since deep learning AIs are known to be suffering much more from catastropic forgetting than biological agents. Do the authors have any prelimiary results or thoughts about this?

4. What are the relation between the proposed methods and LoRA / control net, as these methods freeze the pretrained-model and conducts adaptation with additional network of fewer parameters?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
