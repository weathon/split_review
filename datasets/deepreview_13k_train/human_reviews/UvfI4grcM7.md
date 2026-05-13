# Efficient Training Framework for Realistic Sensory-Motor Integration in a Biologically Constrained Barrel Cortex Model

- Decision: Accept
- Scores: 8, 8, 3, 8

## Abstract
The brain's ability to transform sensory inputs into motor functions is central to neuroscience and crucial for the development of embodied intelligence. Sensory-motor integration involves complex neural circuits, diverse neuronal types, and intricate intercellular connections. Bridging the gap between biological realism and behavioral functionality presents a formidable challenge. In this study, we focus on the columnar structure of the superficial layers of mouse barrel cortex as a model system. We constructed a model comprising 4,218 neurons across 13 neuronal subtypes, with neural distribution and connection strengths constrained by anatomical experimental findings. A key innovation of our work is the development of an effective construction and training pipeline tailored for this biologically constrained model. Additionally, we converted an existing simulated whisker sweep dataset into a spiking-based format, enabling our network to be trained and tested on neural signals that more closely mimic those observed in biological systems. The results of object discrimination utilizing whisker signals demonstrate that our barrel cortex model, grounded in biological constraints, achieves a classification accuracy exceeds classical convolutional neural networks (CNNs), recurrent neural networks (RNNs), and long short-term memory networks (LSTMs), by an average of 8.6%, and is on par with recent spiking neural networks (SNNs) in performance. Interestingly, a whisker deprivation experiment, designed in accordance with neuroscience practices, further validates the perceptual capabilities of our model in behavioral tasks.
Critically, it offers significant biological interpretability: post-training analysis reveals that neurons within our model exhibit firing characteristics and distribution patterns similar to those observed in the actual neuronal systems of the barrel cortex. This study advances our understanding of neural processing in the barrel cortex and exemplifies how integrating detailed biological structures into neural network models can enhance both scientific inquiry and artificial intelligence applications. Code will be made publicly available upon manuscript acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors presents a biologically constrained model of the mouse barrel cortex, comprising 4,218 neurons across 13 neuronal subtypes, with neural distribution and connection strengths constrained by anatomical experimental findings. 

The authors claim to develop an efficient training algorithm tailored for this model and convert an existing simulated whisker sweep dataset into a spiking-based format. 

Their model achieves a classification accuracy exceeding classical ANN architectures by an average of 8.6%, and is on par with recent spiking neural networks (SNNs) in performance, and outperforms SNNs in whisker deprivation experiments.

Post-training analysis reveals that neurons within the model exhibit firing characteristics and distribution patterns similar to those observed in the actual neuronal systems of the barrel cortex.

### Strengths
-The authors develop an efficient training framework specifically designed for a biologically constrained model of the barrel cortex, aimed at achieving realistic sensory-motor integration.   
-The authors meticulously construct a biologically realistic network comprising 4,218 neurons across 13 neuronal subtypes, ensuring an authentic replication of the biological structure of the barrel cortex.   
-The classification accuracy of their model surpasses that of mainstream models like CNNs, RNNs, and LSTMs, and is competitive with recent SNNs, particularly in neuroscience-inspired whisker deprivation experiments.

### Weaknesses
 - Reliability of the biological model: There are always free parameters difficult to be constrained, such as noise shape and exact synaptic efficacy. Small changes in these parameters can lead to completely different dynamical states and computational properties, and I am not sure the the CV is enough to asses the plausibility of the models activity. Can the author comment on how does this affect the generalizability of the findings? 

- Generality of the comparison with standard ANNs: Why is this model so much better than ANN? Is the improvement due to spikes or to the architecture? How would an ANN perform if it had a similar topology inspired by the barrel cortex? Fig.6B makes me think that most of the improvement is due to the architecture. Can the author discuss on why?

### Questions
- Why can't the authors feed continuous signals into the spiking network and let it convert to spiking?
- In the comparison with convolutional networks, are they tested on the original dataset or on the spiking one?
- Occlusion results are interesting. A panel with performance decay across the different models would be very useful. What is the comparison with the mentioned biological experiments?
- Did the authors investigate the importance of the heterogeneity due to different neuron types? E.g. the comparison between homogeneous and uniform models classification performances. Also, I would ask the authors improve the introduction of dynamic gradients.

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
The following paper investigates the gap between biological realism and behavioural functionality of embodied intelligence to develop an efficient training algorithm. The paper introduces a framework for bridging the gap between realism and functionality based on the barrel cortex, where it covers over three contributions: biologically realistic network construction, efficient training framework and establishing a novel spiking whisker sweep dataset.

### Strengths
The paper clearly indicates the gap that exists between the training and biological plausibility of models and current progress in closing this gap.
I really like the idea on how the original weights are constrained to simulate the connections to represent the 13 neuronal subtypes.
Mapping from real to discrete space using a sigmoid function for the dataset is interesting.
Training for synchronisation of neuronal activity is a novel and effective approach, enhancing both stability and biological realism in sensory-motor integration models.

### Weaknesses
The paper mentions that it has a better classification accuracy compared to models of CNNs, RNNs, LSTMs and SNN. CNNs, for e.g. work on the spatial structure of the dataset, and thus this should be interesting to see in both the original and currently introduced spiking dataset since spikes deal more on the temporality of the data.
The structure of the paper is lacking (it seems to be going back and forth spontaneously between different sections in my opinion) although the information provided is sufficient. An example is that some of the information mentioned in Figure 2 are better mentioned after an explanation on the methodology. These took quite some time to understand until reaching section 3. Moreover, the task mentioned in contributions on the spiking dataset (page 3) would benefit better if it also uses figure 3 as a supplementary material to explain.

### Questions
Figure 1A: The figure description seems to need some clarity onto the labels (1,2,3). It is unclear whether the number defines the region or the pathway.
Figure 2A: From my perspective, the connection probability and indication of excitatory and inhibitory connections of the subtypes are not clear. These two appear to be mixed in the diagram and thus require more clarification in the diagram.
Equation 3: Please elaborate more on what beta defines.
More clarity on the dataset used for table 1 and 2: It is mentioned that it uses a spiking whisker sweep dataset in page 3 but it would be better if it is mentioned in the table descriptions as well for better clarity.
The use of the barrel cortex as a foundation to bridge the gap between efficient training and biological plausibility is well-motivated. The introduction of a biologically constrained model, trained by synchronising neuronal electrical activity, is an interesting approach as well. Given the paper’s focus on an efficient training

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper developed a trainable Barrel circuit, whose connection backbone is constrained by biological data of Barrel cortex, to classify object based on (simulated) whisker input. The network is composed of identical adaptative LIF neurons, with tranable timescale parameters. The parameter distribution and response property are analyzed after the training, which is argued to have qualitative similiarity with biological data. The model is compared with several baseline ANN and SNN models based on spiking-based dataset.

### Strengths
This paper build up a trainable bioplausible model for touch, combining the function with bio-interpretation. This is an important and interesting direction in general. On the techinical side, the paper applies the coefficient of variation to determine the desirable initial configuration of a dynamical network model. It also convert a touch dataset into spiking version by Bernoulli sampling based on firing rate. On the discovery side, the author find bio-related feature in the network after the training, including neural selectivity, shift in timescale parameters, similiar response activity as biological data, long-tailed degree distribution, etc. These make it a promissing machine learning approach to study touch.

### Weaknesses
While the overall picture is promissing, the novelty and significance of the paper may not meet the standard of ICLR.
- The training of aLIF network has been realized in a list of previous works, e.g. Chen2022 cited in the paper. And using connection probability to constrain the network topology is also not new
- The proposed CV measure is only showcased in Fig2 based on three selected configurations. It is not clear whether the CV is a significant/convincing measure of the initialization for training and whether it is generalizable to other dynamical bio-plausible models. For example, it is not clear how three configuration is selected and the results is not averged by different random seeds. Also, in FigC, the different initialization do not affact the initial traning process(0-10 epoch), which does not make sense to me if three initialization actually results in bifurcation of the dynamics regions. And the Fig.2 D all shows global synchrony dynamics (even for high CV), which still lack of variability and is not a realistic working regime in the brain .
-  The conversion of real-valued dataset to spiking-based dataset is not a significant contribution, and it is not clear whether the converted spiking data actually mimic the input in biological circuit.
- As a result, while the overall picture is interesting, the specific technical contribution of this paper beyond the related work is limited.

On the experiment side, the significance of result is also my concern:
- Compare with ANN: the ANN is compared based on spiking dataset. So it is not clear whether the poor performance of ANN is due to the data type of input. Since it is not necessary to use spiking data as input to spiking network, the author should also compare the model with ANN on original non-spiking dataset, to disentangle the whether it is the network dynamic or just the data type that acturally make the difference.
- Firing selectivity: it is not a suprise to see the symmetry breaking after the training. The author should compare the selectivity property with other SNN models (after training on this task) to stress the significance of the result.
- The shift of parameter is also not a suprise. It would be a suprise if the shifted distribution mimic that in real circuit. Without such direct comparison, it is not clear whether the shift is a specific property of this model, that have a meaning or just a general phenomenon due to training, given heterogeneous connection backbone.
- The firing rate profile, it is not clear how the this profile is computed: is identical curent applied to each subpopulation seperately or applied to the entire network? Besides, the profiles of different neuron type differ not only in firing rate but also specific spike patterns, like tonic, bursting,...and their responsive property to stimulus ('on','off','on-off'). Can author show more detailed comparison with biological response profile as support.
- For the long-tail degree distribution, it is also not clear whether it is a specific property of this model or a general property of training. I suggest the author to compare the result with other SNN / ANN, to clarify this.

Lastly, the code of the model is not provided, so it is hard to evaluate the solidness of the results.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a novel biologically constrained spiking network model of the mouse barrel cortex, introduces an initialization technique for it based on the coefficient of variation of the network activity, and evaluates both in conjunction on a newly spike converted whisker sweep dataset. The proposed method shows favorable performance compared to other even non-constrained network models, and fully trained versions of it more closely reproduce biologically observed network characteristics such as increased neuron selectivity, neuron type dependent firing rate and timescale distribution, and neuron weighted degree distribution.

### Strengths
- The paper is really well written with predominently precise use of terminology.
- It tackles an interesting and really challenging problem; effective training of biologically constrained networks, and computationally characterizing them.
- Achieving competitive performance on benchmarks given this many biological constraints, even if potentially computationally more expensive, is no easy feat.
- Also impressive is the sheer number of directions in which training the networks increased the similarity to biological network statistics.
- The dimensions along which the network was characterized are well motivated, and the used quantitative measures are really creative and nicely connected back to neuroscience literature.

### Weaknesses
 That the training methodology is really more efficient was not convincingly shown, and to call it a training framework might be a stretch:
   * 1.1) An effective initialization technique was shown (the coefficient of variation approach), yet no qualitative assessment of efficiency, such as Performance/FLOPs or Performance/Samples is provided to warrant the statement of “efficient” from my understanding. 
   * 1.2) Also consider, that figure 2C doesnt even show the efficacy convincingly, as initially all three visualized initializations perform similarly well (until around epoch 20), and subsequently run into training stability issues (examplified by the sudden drop/rise in performance). In fact even the supposed best initialization (according to the coefficient of variation) displays two mayor drops in performance during training. This could be more indicative of exploding gradient issues or extreme parameter regimes, which would rather be fixed by gradient clipping or appropriate regularization and normalization techniques: no mention of such things in the methods?
   * 1.3) Furthermore in panel 2D the network displays pathological firing synchronization in both cases, unless I’m missing something (how does a biological recording from that brain region typically look like?). This could be indicative of a lack of decorrelating mechanisms or insufficient inhibition, which to my knowledge the brain typically has.
   * 1.4) Lastly, no comparison to other initialization techniques typical in the spiking literature was conducted, such as simply scaling synapse weights by in-degree, or more sophisticated ones (e.g. see Rossbroich et. al 2022).
* However, somewhat reformulating the claims and contributions probably is sufficient to make the paper consistent.

The computational characterizations consistently lacks a control / comparison to interpret the results, and are possibly merely side effects of simple gradient descent training in networks?
   * 2.1) For neuron specific firing selectivity: it would be interesting to see how the CNNs or LSTMs neuron specificity (or similar measure) behaves? If this doesnt happen for them it’s more convincing that this is because of the biological constraint and not simply due to generic gradient optimization.
   * 2.2) For the differentiated neuronal dynamics: when initializing to a single value and training with backprop naturally the distribution become smudged, and when margenalizing over neuron type there will naturally be differences. Whether these differences here are statistically significant from random drift, or whether they reflect more closely the biological ground truth, remains unclear from the paper? The firing rate example is more convincing, yet the effect might be primarily driven by only three subtypes (6,7 and 9) and the impact of normalizing the firing rates is unclear to me. Some sort of additional control would further substantiate the point.
   * 2.3) For the weight degree distribution: one-sided metrics evaluated on variables with low variance will typically also display a longer tailed distribution in networks after training, as the variable gets smudged and the interval is only open to one side. Without a control of sorts it’s hard to understand whether in this case this is an effect of the cortical constrains or simply due to backpropagation and this being a directed graph. Evaluating this or a similar metric for e.g. the LSTM could possibly serve as a control / comparison here too.
   * 2.4) Regarding the connectivity probability: this is more convincing, yet only IFF the network was properly re-initialized for the changed connectivity, e.g. using the proposed coefficient of variation technique.
* However, it probably cannot be expected to also get explanations as to “why” we see these effects in a single paper, and therefore an extension of the future work section and making ther readers aware of these possible limitation should be enough to address most of these issues.

### Questions
1) The firing activity in figure 2D seem very synchronized and periodic, does this reflect real work data, and do you have example visualization of such data?
2) Any explanation as to why the anatomic connection probability is best? Were the initialization adjusted individually for each of the connection probabilities?
3) For each of the network characteristics findings; do you believe you find this effect due to the biological constrains or simply gradient based training in networks? 
4) Where any normalization or regularization techniques used for training, or gradient clipping?

### Soundness
3

### Presentation
4

### Contribution
3
