# Functional segregation of inputs in artificial neural networks for vision

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
One of the main organizational principles of artificial and biological intelligence systems is their reliance on signed inputs: positive and negative weights in artificial networks, and excitatory and inhibitory synapses in the brain. However, little is known about the role of inhibitory activity in high-level visual cortex such as inferotemporal cortex, or how artificial neural networks (ANNs) trained for object recognition segregate their learned representations into positive and negative weights.
Here, we dissected high-level visual mechanisms in ANNs trained with ImageNet. We investigated how learned representations of ANN classification units depended on their positive or negative inputs using ablation experiments and feature visualization. We found that unit representations changed more when ablating positive- vs. negative inputs. Object-related features were abolished when ablating positive inputs, while still preserving background textures. This effect was more pronounced in adversarially trained robust networks. This segregation persisted in networks trained with unsupervised learning, but was not present in a ResNet18 trained with Tanh instead of ReLU.
We found a consistent functional segregation when we trained models to replicate the activity of neurons in monkey visual cortex, across the ventral stream (V1, V4, and IT). Feature visualization of the neuron models produced images containing local features preferred by actual neurons. Analogous to units trained for classification, the learned representations of units trained to simulate neurons changed more upon ablating positive than negative inputs. We conclude that ANNs for classification segregate object or foreground information into the positive weights, with background or contextual information into the negative weights, in their last layer before softmax. These results hint at the relevance of signal rectification and inhibition into shaping feature selectivity in the primate ventral stream, a hypothesis we are testing in vivo.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper employs sophisticated methods to investigate the roles of positive and negative weights in deep neural networks. Through feature visualization, the authors illustrate the effects of ablating positive and negative weights, finding that positive weights contribute significantly to object representation, whereas negative weights primarily encode background information. Furthermore, similar results are obtained with real neuron responses as objective, showing a potential similar mechanism also in biological visual processing.

### Strengths
•  The idea is novel and intriguing, addressing a fundamental problem in systems neuroscience.
•  The experiments are thorough and well-designed.
•  The results are clearly presented.

### Weaknesses
The paper requires a relatively advanced understanding from readers; the writing could be improved with more intuitive explanations.

My main concern is the rationale behind the roles of positive and negative weights. Do we have a theory explaining why positive weights contribute to object representation and negative weights to background information? Could it not be the other way around? I realize this is challenging to answer, but a direction for future research would be helpful.

In Figure 1, are the lines averaged across 10 units from the 1,000 categories? Also, what is "control" here? My understanding is that it represents no ablation, so is it expected to be a flat line?

The section on ablation has some issues. Could you clarify $\sum_{i=1}^{k} w_i$? It seems wrong as alpha is the proportion. Should it be $\frac{\sum_{i=1}^{k} w_i}{\sum w_i}  $

In the Figure 3 caption, what does “visualization score” mean?

In Section 4.2, what is meant by “robust networks”? Could you clarify what they are robust to?

The phrase “the diverseSet covers the embedding space of AlexNet” is unclear. What does "embedding" refer to here, and which layer do the embeddings belong to?

Figure 8 is confusing. What does extrapolation mean in this context? The main text does not seem to cover this—did I miss something?

I understand that the neuro features obtained in vivo were spatially localized. How were these localized features obtained?

### Questions
1.	My main concern is the rationale behind the roles of positive and negative weights. Do we have a theory explaining why positive weights contribute to object representation and negative weights to background information? Could it not be the other way around? I realize this is challenging to answer, but a direction for future research would be helpful.

Writing-related questions:

2.	In Figure 1, are the lines averaged across 10 units from the 1,000 categories? Also, what is "control" here? My understanding is that it represents no ablation, so is it expected to be a flat line?

3.	The section on ablation has some issues. Could you clarify $\sum_{i=1}^{k} w_i$? It seems wrong as alpha is the proportion. Should it be $\frac{\sum_{i=1}^{k}}{\sum w_i}  $ 
4.	In the Figure 3 caption, what does “visualization score” mean?

5.	In Section 4.2, what is meant by “robust networks”? Could you clarify what they are robust to?

6.	The phrase “the diverseSet covers the embedding space of AlexNet” is unclear. What does "embedding" refer to here, and which layer do the embeddings belong to?
7.	Figure 8 is confusing. What does extrapolation mean in this context? The main text does not seem to cover this—did I miss something?
8.	I understand that the neuro features obtained in vivo were spatially localized. How were these localized features obtained?

### Soundness
3

### Presentation
2

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
This paper uses positive and negative weight ablation experiments as well as feature visualization to show that positive weights in a CNN tend to encode object information, while negative weights tend to encode background and contextual information, respectively.  The authors show that this is not only true for CNN but also for the neurons in the macaque ventral visual system. The authors further show that this tendency is even stronger in robust neural networks.

### Strengths
The study appears to be carefully organized and systematically conducted. The basic findings appear to be consistent and valid across multiple CNN models, though less so for models of biological neurons.

### Weaknesses
First, it is debatable whether the positive and negative weights in CNN can be equated to the excitatory and inhibitory input to a neuron or the action of excitatory neurons and inhibitory neurons. Second, in the visual cortex, such as V1, inhibitions coming from the surroundings or from within the hypercolumn in the primary visual cortex are known to mediate competition from other objects in the scene (same and different locations) as a way to resolve ambiguity. From the traditional neuroscience perspective, there is no particular reason that the inhibition has to carry only  "background" or "texture" information. Third, figure 9's ablation experiment on the neuronal model fitted to the neuron's responses did not appear to contain only background texture, even with the positive weights ablated. These concerns lead me to question whether these findings are relevant to understanding the brain.

### Questions
Is there a logical or computational explanation as to why the negative weights are carrying "background" and "texture" information?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper aims to find the distinct role of excitatory and inhibitory synaptic weights in biological and artificial networks. Ablating positive vs negative weights in a layer of neural network, visualizing the affected features, showed that object related features when ablating positive weights, while the background texture remains less affected. When networks mapped to real neurons in primate brain (mostly PIT area) were ablated similarly, a consistent result was reported. Altogether, this work suggests the role of inhibitory neurons is shape feature selectivity in primate vision.

### Strengths
Role of excitatory and inhibitory neurons in natural vision remains a fundamental question in neuroscience. On the other hand, the rise of mechanistic interpretability in ML, begs the question are they related to meaningful features in the image? The study is well-motivated, and the study of both natural and artificial visual systems side-by-side is very important to illuminate both fields.

### Weaknesses
#### Insufficient experiments to support the claims

> 4.1 NETWORKS TRAINED ON IMAGENET ALLOCATED OBJECT INFORMATION INTO POSITIVE
WEIGHTS

To claim, the effect seen for positive vs. negative weights in DNNs are relevant for excitatory vs inhibitory synapses in the brain, one should look into more layers and not just the layer before softmax in AlexNet ('fc' layer). That layers contain weights which during training were encouraged to organized in 'be a large positive' for 'the correct class' and be suppressed otherwise, because of the properties of the softmax. So, it is almost trivial that ablation of positive weights in that layer hurt the object features and keeps the background intact.
This explanation is perfectly inline with the next experiment that showed

> 4.2 ROBUST NETWORKS ARE LESS ROBUST TO ABLATIONS

where the results show robustness increases the segregation. Robust training makes the model to rely on object features more, as previous work showed that robust neural networks are more shape-biased (Geirhos et al, 2018). Also, see background challenge paper (Noise or Signal: The Role of Image Backgrounds in Object Recognition, Xiao et al, 2020)

So, to address this concern, I suggest running control experiments for other layers (doesn't need to be exhaustive, and doesn't need to include black-box feature visualization which is time-consuming). Just a few other intermediate layers from simple networks using simple (but reliable) gradient-basedd feature visualization would work. Inclusion of the information regarding positive/negative weight ratio is important, too.

> 4.3 BIOLOGICAL MODELS BASED ON IMAGENET NETWORKS SEGREGATE LOCAL FEATURE
INFORMATION INTO POSITIVE WEIGHTS

The main concern that I have regarding this section is that unlike the first experiment where the proportion of positive vs. negative weights were listed (Table 1), it's not clear how to interpret the results in this section without that information.

Moreover, since the main question is about the functional role of inhibitory vs excitatory synapses, here is a good chance to restrict the mapping to excitatory vs. inhibitory **neurons** as opposed to **synapses**. Because real neurons can't have both type of synapses and since the goal in this closed-loop monkey-included experiment is to uncover the role of inhibition, I wonder why not establish a Dale's law mapping network instead of regular PLS which allows positive and negative weights for all units. I appreciate that in the limitations authors brought up Dale's law, just wondering if Dale's law in mapping as opposed to Dale's law in the trained network (which is very constraining) could bring more insights about inhibition vs excitation in the brain.

In summary, the main claim in the paper about role of excitatory vs inhibitory neurons in object feature enhancement needs support because the experiment on penultimate layer where positiveness of weights are directly linked to classes can't be generalized to positive vs negative weight's role in the whole network (or brain).

### Questions
- In figure 9, why figures were labeled as *exc*, vs *inh* rather than *pos* vs *neg* as before? The weights are still not in a biological brain so I found this labeling a bit misleading.

### Soundness
2

### Presentation
2

### Contribution
2
