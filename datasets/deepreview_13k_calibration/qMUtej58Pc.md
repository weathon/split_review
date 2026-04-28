# From Overconnectivity to Sparsity: Emulating Synaptic Pruning with Long Connections

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
During brain development, an excess number of synapses are initially created, which are progressively eliminated through a process known as synaptic pruning. This procedure is activity-dependent, shaped by the brain's experiences. While creating an overabundance of synaptic connections only to later remove many might appear inefficient, research suggests that pruned networks demonstrate significant efficiency and robustness. Inspired by this biological process, we propose a neural network architecture utilizing long connections instead of traditional short residual connections. When long connections neural networks (LCNs) are trained with gradient descent, information is naturally "pushed" down to the first few layers, leading to a sparse network. Even more surprising is that this simple architectural modification leads to networks that exhibit behaviors similar to biological brain networks, namely: early overconnectivity to later sparsity,
enhanced robustness to noise, efficiency in low-data settings and longer training times. Specifically, starting with a traditional neural network architecture with initial depth $d$ and $k$ connections, long connections are added from all layers to the last layer and summed up. During LCN training, 30-80% of the top layers become effective identity mappings as all relevant information is concentrated in the bottom layers. Pruning the top layers results in a refined network with a reduced depth $d'$ and final connections $k'$, achieving significant efficiencies without any loss in performance compared to residual baselines. We apply this architecture to various classification tasks and show that, in all experiments, the network converges to utilizing only a subset of the initially defined pre-training connections, and the amount of compression is dependent on the task complexity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Inspired by brain synaptic pruning, they proposed long connection neural networks that eliminate top layers without sacrificing performance, resulting in a significant reduction in inference time.

### Strengths
1. This work accelerates inference and reduces memory usage without sacrificing performance.
2. This architecture can be used complementarily with pruning or dynamic inference techniques.

### Weaknesses
1. The validity of the structure is verified only on the base ViT, but there is a lack of experimental and theoretical validation for larger model structures.
2. If the author claims that this is a fine-tuning method, the time spent during model training is typically included in the overall time assessment. Fine-tuning often involves adjusting a pre-trained model on a specific dataset, and this process can require significant computational resources and time. However, if the focus is on inference speed or deployment efficiency, the discussion (time, GPU memory and other computation cost) might be reported during the fine-tune process .
3. It sounds like you' re noting that the determination of the final model layer relies heavily on experimental validation, which can indeed be resource-intensive and time-consuming. This approach can lead to significant computational costs, especially when iterating through different configurations to find the optimal structure.
4. While verifying the effectiveness of a structural design on a classification task provides important insights, it doesn't necessarily guarantee that the same design will perform well across different tasks, such as object detection, segmentation, or generative modeling. To better justify the generalization to other tasks, the authors could provide theoretical justifications or include empirical evidence.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors add long-range connections to standard transformers and show that this enables effective pruning, perhaps like that in the real brain.

### Strengths
This is an interesting and creative idea.  It is also true that it is supported by the neuroscience literature is a reasonable possibility.

### Weaknesses
The evaluations are too simple.  Like many things in machine learning, something that works for simple versions of tasks might break down for larger tasks.   I am most knowledgeable about vision.  I would like to see similar results for imagenet rather than just CIFAR-10 to be really sure that these results are actually going to be impactful.  (Apologies if I missed it if this was included.) I am not competent to juge the meaningfulness of the language results.

### Questions
Can you illustrate results on a stronger task like imagenet? Or perhaps CIFAR-100?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a method for encouraging more task-informative representations in the lower layers of ANNs and thereby improving efficiency.

### Strengths
- the text is generally well written

### Weaknesses
 - I did not feel that the comparison to similar models was adequately made. There is a related work section which many relevant models are correctly brought up, but 1. there is no explicit description of how LCNs are different from these models and 2. apart from residual connections, none of these models are quantitatively compared to this previous work. One is left to ponder whether LCNs makes conceptual/quantitative *advances* in the field.

- the link to biology and the brain is interesting, but after the initial abstract it is hardly addressed. The authors report longer training times as more akin to 'biological brain networks', but I'm not sure which result even supports this (in Fig 8 it trains faster?). That LCNs handle noise better is interesting, but an intuitive explanation/link to previous literature as to why this occurs would be very helpful in its interpretation.

- It appears from the figures that all results are derived using a single random initilisation seed? If so, I would strongly recommend re-running these analyses over several seeds, otherwise it is very difficult to draw any strong conclusions. 

- Some of the segways between sections could be smoother. For example short introductions to sections 3.1/7 would help. Some figures could also be clearer. For example a few instances where the axis labels were confusing. E.g. what are the axis labels in Fig 2? I presume w and the error gradient with respect to w? in fig 3 is weight of hidden1 = w1, and wouldn't it be interesting to look at w2/w3 as well to check if they are sparser for LCN, and maybe absolute values instead of raw values to better show sparsity? In Fig 7 I would prefer an explicit mathematical term relating to an equation than 'std' and 'noise_level'. In section 3.1 a schematic (even if for the appendix) would be helpful to the reader

- What fundementally concerns me is that this 'lossless' reduction depends on highly redundant original model with a significant number of (as you identify unnecessary) layers. I do not agree with the concept that ML researchers 'aim for overparameterization', I believe in ML the number of parameters if purely based on emperical performance.

- What would impress me is if you were able to demonstrate such performance gains starting with an original model with the same number of layers/parameters as, e.g. the baseline models in Table 4 in https://arxiv.org/pdf/2403.17921. That would make it much easier for me to directly compare your method to 'lossy' methods. I.e. can LCN be succesfully applied to realistic network architectures, or only those with a tremendous amount of original layers?  

- I am also rather cynical that LCN can be branded as 'lossless' versus alternative 'lossy' pruning methods. This must surely depend on the original network architecture/redundancy as per above and the type of task.

- I am still concerned however by the different numbers reported versus other studies. For example, if the ViT-Base has the same network architecture, why does it achieve ~5% less accuracy on the ImageNet task versus that reported in https://arxiv.org/pdf/2403.17921?

- Also, in Table 1 I notice the accuracy for LCN is slightly less on the Amazon task versus vanilla. This is not by itself concerning and is indeed within the margin of error, but still reinforces my belief it's dangerous to call LCN 'lossless'.

- typos:
line 210: brackets around citation
line 326: -> architectures
line 411: -> directly
paragraph 460: brackets around (multiple) citations
line 492: -> effectively

### Questions
- line 54: 'Contemporary deep learning architectures aim for overparameterization' - what does this mean?
- is the residual network given by equation (3) a specific type of residual network? It is introduced there rather abruptly for a non-expert reader
- for the toy example the models are trained for 500 epochs (1000 examples per epoch). This seems like a lot for such a simple problem?
- line 259: 'possible indication of overfitting' - is Fig 5 showing the training or validation accuracy?

- typos:
line 210: brackets around citation
line 326: -> architectures
line 411: -> directly
paragraph 460: brackets around (multiple) citations
line 492: -> effectively

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores a new neural network architecture inspired by biological brain processes, specifically synaptic pruning. The paper proposes Long-Connected Neural Networks (LCNs) as an alternative to traditional deep learning architectures that primarily use short residual connections. 
This simple architectural modification leads to networks that exhibit behaviors similar to biological brain networks, namely: early overconnectivity to later sparsity, enhanced robustness to noise, efficiency in low-data settings and longer training times.

### Strengths
- Good Writing. The paper clearly explains the motivation for the proposed work, drawing a strong connection between biological processes and deep learning archutectures.
- The paper proposes a novel architecture. By pushing information to the lower layers and pruning upper layers, the architecture addresses the common issue of overparameterization in deep learning models. It is interesting.
- The paper demonstrates that LCNs lead to sparser networks and improved efficiency. This can be particularly valuable in real-world applications where computational resources and memory are limited.

### Weaknesses
 - The paper provides some mathematical intuition, but a deeper theoretical analysis of why this architecture works so well (e.g., in terms of information bottleneck theory or gradient dynamics) could strengthen its claims.
- Across the experiments, I cannot find the comparative experiments with state-of-the-art pruning techniques.

### Questions
- Please explain why your method can have effect.
- Please compare with some state-of-the-art pruning techniques.

### Soundness
3

### Presentation
3

### Contribution
3
