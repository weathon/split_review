# Modeling Focal Synaptic Degeneration and Neural Plasticity in Ventral Visual Cortex

- Decision: Reject
- Scores: 3, 5, 5, 6

## Abstract
Strokes affect a significant portion of the population and often result in secondary damage in the form of focal synaptic degeneration. When this occurs in the ventral visual cortex (VVC), it can lead to neurological deficits, including visual function loss. In this paper, we use the VVC as a framework in which to model focal synaptic degeneration and post-injury plasticity. We do so by progressively "injuring" synaptic connections in primate visual areas V1, V2, V4, and the inferior temporal cortex (IT), followed by continual retraining of the spared connections on real-world visual stimuli. We demonstrate that the functional signatures of carefully designed differential tasks can localize synaptic decay in the VVC. Initially, categorization performance deteriorates gradually, up to a critical threshold, beyond which there is a sharp drop. This slow decline in performance is marked by a reorganization in nearby neurons, where both visual function and the structure of receptive fields adapt to compensate for the damage. Spared recurrent connections significantly contribute to recovery. Furthermore, we find that the presence of teaching signals in the form of category labels during rehabilitation leads to improved categorization performance recovery.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper investigates the impacts of synaptic degeneration and post-stroke plasticity in the ventral visual cortex (VVC) via deep neural networks. The authors simulate focal degeneration in visual regions (V1, V2, V4, IT), in different layers of a neural network and examine recovery mechanisms. The study claims that  A) such mechanisms can be simulated from deep neural networks and B) the model’s recovery behavior under degeneration mirrors some biological observations. Additionally, the paper suggests that certain retraining protocols (e.g., contrastive learning) yield better recovery performance than supervised approaches.

### Strengths
1. Strokes and lesions are debilitating human conditions. Modeling these processes in neural networks might be a promising strategy.
2. Generating new recovery protocols is a potentially interesting use case of models

### Weaknesses
1. The study has major logical flaws with respect to the motivation. Specifically, the choice of using current neural network models as models of ischemic stroke and recovery is not clear. The study assumes a direct correspondence between individual model units and brain regions, which is problematic given that DNNs are most predictive when responses are represented as a linear combination of multiple model units, not single units. Lesioning individual units or model weights may not accurately reflect biological structures or processes. Furthermore, the study does not adequately address the fact that DNNs are primarily models of inference, lacking the biophysical mechanisms like spike-timing-dependent plasticity (STDP) crucial for experience-dependent learning and plasticity observed in the brain following injury. The simulated lesions, therefore, may not translate accurately to biological systems.
2. There are several unsubstantiated claims on biological relevance. The study intends to draw parallels between biological systems (brains) and models, and in the process overstates the degree to which this match is meaningful. The connection between model behavior under degeneration and observed behavioral phenomena (on which there is a lot in the rehabilitation and stroke literature) is speculative and not validated. For example, the study attempts to link layer-specific lesions with task performance, concluding that simpler tasks are processed by lower-level visual regions, while more complex tasks are handled by higher-level regions. However, this significantly oversimplifies the complexity of actual biological phenomena. Color processing, for instance, involves higher-level visual cortex areas, and face-selective patches are not limited to cortical regions but also observed subcortically. The model's analyses do not capture these complexities, and the claims of mimicking specific cortical impairments require stronger alignment with empirical data.
3. The clinical relevance of the findings are unclear. The paper’s findings and discussion on therapeutic interventions in its current form is superficial and lacks specific recommendations for clinicians. The study suggests that their modeling strategy could aid in diagnosing micro-stroke events and quantifying their effects. However, the data presented, relying on a broad 1000-way ImageNet classification task, lacks the specificity required for detecting subtle, localized effects. The implementation of “focal” degeneration via “non-selective” pruning of filter weights differs significantly from focal degeneration in the brain, creating a disconnect between the claim and the results. Modeling broad accuracy changes does not directly address the detection of subtle, specific effects from transient events like micro-strokes.
4. The paper also relies heavily on prior existing models (like CORnets etc) without providing clear suggestions for improvements. The analyses repurpose existing methods and there is conspicuous lack of new contributions/innovations in the modeling approach (the models or the lesioning methods). The interpretation of recurrent dynamics, implemented through backpropagation through time (BPTT), raises concerns about the validity of the method. BPTT limits the possibility of a true negative control for recurrence, as removing recurrent connections transforms the model into a feedforward network, making it difficult to isolate the specific role of recurrence in facilitating recovery. The study also mischaracterizes self-supervised model training as a “retraining protocol” which is highly misleading and confusing with the rehabilitation protocols. The discussion of this section is not well aligned with the actual manipulation.

### Questions
1. Existing literature demonstrates that deep neural networks (DNNs) serve as reasonable predictive models of the visual cortex across species, including humans, primates, and rodents. DNNs tend to be most predictive when responses are represented as a linear combination of multiple model units, as single units alone do not capture brain responses as effectively. This study’s reasoning, however, seems to hinge on an assumed direct correspondence between individual model units and brain regions, as it involves lesioning units and model weights, which may not accurately reflect biological structures or processes.
2. Even beyond the assumption of a direct correspondence between model units and neurons, it’s important to recognize that deep neural networks (DNNs) are primarily viewed as models of inference rather than mechanisms for experience-dependent learning and plasticity. Current neural networks lack essential biophysical mechanisms, such as spike-timing-dependent plasticity (STDP), that underpin the complex processes of adaptation and reorganization observed in the brain following injury. Consequently, the model's findings may not translate accurately to biological systems. Simulating lesions in a model is one thing; however, claiming that these simulated lesions are analogous to or predictive of actual brain lesions requires strong empirical validation (even with existing data in the literature, something that is notably absent in this study).
3. Lets consider Section 4.1, which attempts to link layer-specific lesions with task performance across three tasks: color discrimination, noise discrimination, and face recognition. The authors’ main conclusion is that simpler tasks are processed by lower-level visual regions, while more complex tasks are handled by higher-level regions. However, this finding significantly oversimplifies the complexity of the actual biological phenomena observed in humans. For example, color processing in the human brain is not as low-level; rather, color-biased regions are found in the high-level visual cortex, “IT-like” areas. Studies by Conway et al., Pennock et al., and Lafer-Sousa et al. have shown that these higher-level areas are implicated in conditions like achromatopsia, where color perception is lost, which is not what the model’s analyses would predict. Turning to face processing, the paper similarly misses key complexities. In primates, including humans, face-selective patches are not limited to cortical regions but have also been observed subcortically, as shown in studies by Johnson et al., Gabay et al., and Kosakowski et al. This highlights that the neural architecture for face processing is more distributed and intricate. For examples lesions even to the subcortical amygdala network or early visual regions (like OFA) can result in highly specific face recognition deficits (like prosopagnosia). To accurately claim that the model lesions mimic specific cortical impairments in biology, needs stronger alignment with empirical data and a more sophisticated treatment of the neural networks. The true strength of in silico models lies in their ability to uncover complex, nuanced phenomena that might be challenging to observe directly in biological systems. However, rather than leveraging this potential, this paper settles for making simplified claims that do not fully capture the depth of these biological processes (and may not even require neural networks).
4. In Section 4.2, the authors suggest that their modeling strategy could aid in diagnosing micro-stroke events and quantifying their effects. However, the data presented in this section does not convincingly support this claim. The results rely on a broad 1000-way ImageNet classification task, which lacks the specificity required for detecting subtle, localized effects. Furthermore, the “focal” degeneration is implemented via “non-selective” pruning of filter weights within an area, which differs significantly from focal degeneration as it occurs in the brain. This creates a clear disconnect between the claim and the results: modeling broad accuracy changes does not directly address the detection of subtle, specific effects arising from transient events like micro-strokes.
5. The interpretation of recurrent dynamics in Section 4.4 raises a critical question about the validity of the method used, specifically whether an effective negative control is even possible. In this study, recurrence is implemented through backpropagation through time (BPTT), which is a standard approach for training recurrent neural networks but differs significantly from how recurrence operates in biological systems. The issue with using BPTT is that it limits the possibility of a true negative control for recurrence. In BPTT, once the recurrent connections are removed, the model effectively becomes a feedforward network without any capacity for dynamic feedback during task performance. Thus, any observed decline in performance may stem from this static structure rather than a specific role of recurrence in facilitating recovery. In order to really show that recurrence helps, the authors need to demonstrate that the opposite result is even viable with these current neural networks.  
6. I found Section 4.5 of the paper particularly confusing. The authors motivate this section by describing some common visual rehabilitation tasks. The manipulation however however is the specific model cost function (self-supervised versus supervised model training). They show that self-supervised model recover somewhat faster (though unclear how much training data, including augmentation needed etc, which are critical for efficiency). The whole thing is mischaracterized as a self-supervised “retraining protocol” which is highly misleading and confusing with the rehabilitation protocols. Note that the discussion talks about this section with respect to rehabilitation which this section does not really engage with.  
7. Overclaims and confusing terminology: The authors should clearly distinguish between models and brains (for example V1-layer for models and V1 for brains). This makes the paper very difficult to real and distinguish between experiments on models and the brain. The paper also overclaims the results in several places. The effects of strokes in the human brain are highly complex and depend on several factors. Especially strokes to the visual cortex in adulthood (fully trained networks) are often remarkably resilient and do not recover (unlike the picture presented in this study from simulations on neural networks). 
Overall, while the paper presents a promising idea, the current implementation and the interpretation of modeling results do not align closely enough with actual observed behavioral effects to show the validity of the modeling strategy.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper describes a computational approach to understand the effects of localized synaptic damage in the ventral visual cortex caused by ischemic strokes. The researchers use deep artificial neural networks to mimic primate visual areas (V1, V2, V4, IT) and investigate how gradually losing synaptic connections influences visual processing. They also explore how the brain's ability to rewire itself, known as neural plasticity, helps in recovering from this damage. The study examines how degeneration impacts various visual tasks, identifies critical points for recovery, looks at the role of remaining connections, and evaluates the use of contrastive learning for rehabilitation. The findings offer insights into how the brain adapts after injury and propose strategies to improve recovery following cortical damage.

### Strengths
The paper presents a new computational framework for simulating focal synaptic degeneration in the VVC, a relatively underexplored area compared to global degeneration models. The innovative approach involves progressively damaging synaptic connections in biologically realistic DANNs and incorporating neural plasticity. The methodology is robust, utilizing various model architectures (feedforward, recurrent, self-supervised) to enhance the generality of the findings. The experiments are thorough, assessing the effects on different tasks and underlying mechanisms. The paper is well-written, with clear explanations and well-designed figures that aid understanding. Custom-designed datasets tailored to test specific functions add to the clarity. The study offers insights into how focal damage in visual areas affects function and recovery, potentially informing future therapeutic strategies, and bridges computational modeling with biological observations to enhance our understanding of neural plasticity.

### Weaknesses
While the models in the study are inspired by biological systems, they have limitations in fully capturing the complexities of real neural networks. The differences between simulated synaptic degeneration and actual stroke progression in patients may limit direct applicability. The modeling process assumes random synapse pruning, which oversimplifies the actual patterns of synaptic loss, and does not fully account for the complex time dynamics and spread of damage seen in real ischemic strokes. Specifically, the model does not consider the heterogeneous vulnerability of different neuron types or the spatial gradients of damage that are often observed in vivo. The retraining protocols used in the study involve large numbers of images between lesion iterations, which may not reflect the visual exposure patients experience in reality, potentially leading to an overestimation of recovery potential. Although the study shows contrastive learning to be effective over supervised learning, its practical use in clinical contexts could be challenging. Additionally, the paper notes that its hypotheses and predictions need validation through neurophysiological experiments, as the findings are currently limited to computational models.

### Questions
How would results change if the model used more realistic synaptic loss patterns from ischemic strokes, such as targeting specific neurons or connections? Can the model simulate more detailed temporal dynamics to better match clinical stroke timelines? If retraining data were greatly reduced to reflect patients' limited visual exposure, how would recovery be affected? Since contrastive learning aids recovery in the model, how can this be applied to practical rehab protocols? Could specific training tasks mimic these principles? Can this framework be adapted to other sensory systems or cognitive functions affected by strokes?

### Soundness
3

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
This paper aims to study the process of focal synaptic degeneration in order to better understand the breakdown and possible recovery of biological neural network function in stroke. The authors use systematic weight pruning and network retraining experiments to examine how the deterioration of different components of multiple deep artificial neural networks leads to decrements in function on multiple behavioral tasks, as well as in similarity to neural data. The authors conclude the following:
- retraining allows networks to better maintain function in the presence of gradual degeneration of connections
- degeneration of different hierarchical levels leads to differences in the network's performance
- degeneration with retraining can lead to functional reorganization, whereby preserved part of the network can help to compensate for lost functions in degenerating parts of the network
- recurrent connections are critical for successful preservation of function
- self-supervised retraining is more effective than supervised retraining

### Strengths
- The paper is well written and tackles an important topic of both fundamental and applied interest
- The paper connects with neurology to a degree that is rare for visual cognitive computational neuroscience 
- The authors use multiple datasets to test recovery
- The authors test multiple models
- The authors do not just test recovery performance, but also compare the match of unit properties to neural data in an areally mappable way, which is a huge strength that leads to discoveries of functional compensation
- The results on functional compensation are extremely interesting

### Weaknesses
 - Figure 5 has some very interesting results regarding compensatory changes -- probably the most interesting results of the paper -- but the presentation of the results is very chaotic. It's unclear to me what the difference in analysis approach is in Figure 5B is vs. Figure 5A. Is it just the same approach for area V2? There are randomly some results from AlexNet, some from CorNet-S, some from CORNet-R, etc. It all feels a bit chaotic. More importantly, it seems the results may be cherry picked, and it is unclear how general the trend of compensatory changes is. Can the authors do a more systematic analysis of compensatory changes to present in supplementary, and use this figure to highlight a few representative results? For example, it would be useful to quantify the RF size changes for all pairs of areas, given the first of the pair being the one lesioned. Rather than plotting over the full range, a summary statistic could be constructed for a more concise presentation capable of showing the pattern across the full span of possible effects.
- There is no supervised control for Figure 6B. Without this control, it is inappropriate to claim that self-supervised vs. supervised learning in the retraining task matters for recovery performance, since the match between initial pretraining and recovery task could be equally if not more important. It is critical to isolate the effect of the retraining method from the potential confound of task similarity by including a supervised control that is trained on the same task as the self-supervised network.
- Perhaps the authors are just following the approach of Hinton, but I find the idea of plotting performance against lesion iteration rather than total fraction of lesioned synapses a bit odd. This makes Figure 4D very hard to interpret, since it is mentioned that 95% of connections have been lesioned for that analysis, but one cannot easily connect that number with the other plots. Additionally, I do not understand how the magnitude of performance is reaching nearly 80% in Figure 4D, when the network's unlesioned performance is less than 65% in Figure 4B.
- The degeneration here is completely random within an area, in contrast to the topographic specificity of lesions in biology. This seems likely to influence the pattern of results a lot, where large deficits in narrower domains could be observed with much less damage in a topographically organized network, with more preservation of other domains, due to the greater precision in mapping between damage and local function. It could be interesting for the authors to conceptually match this sort of damage by damaging units in a way that preserves correlation: e.g. after selecting some initial set of units, units with greatest activity correlation to these units are lesioned next, etc. 
- Similarly, given the advancements in topographic neural networks in recent years, it is a bit disappointing that these authors do not discuss them at all. Indeed, these analyses would be very well suited for topographic models, since focal damage can be modeled much more accurately. 
- The choice to preserve recurrent connections seems odd - why would these be particularly spared after a stroke? It is interesting to explore the effect of this computationally at the end, but it is a bit concerning that all of the preceding main results rely on this questionable choice.

### Questions
- Biologically, why is it more sensible to prune connections (as done here) rather than entire units? If there is a clear answer, it would be great for the authors to state it clearly in the text.
- See weaknesses for other questions

### Soundness
2

### Presentation
2

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
This study explores how synaptic degradation caused by stroke affects the ventral visual cortex (VVC) and assesses the role of neural plasticity in the recovery of visual functions post-injury. Using a primate visual cortex model, the study simulates synaptic degradation by progressively weakening synaptic connections in V1, V2, V4, and the inferior temporal cortex (IT), followed by retraining with real-world visual stimuli. The results indicate that synaptic degradation leads to a gradual decline in visual function within the VVC, followed by a sharp deterioration once a critical threshold is reached. Post-injury retraining reveals reorganization of surrounding neurons and enhanced recovery through preserved recurrent connections. Differentiated visual tasks also help pinpoint specific areas of damage within the VVC. Additionally, the study finds that retraining with contrastive learning protocols aids in the recovery of classification performance. Model simulations demonstrate that, in cases of localized synaptic degradation in the VVC, recurrent connections, types of visual stimuli, and the nature of training tasks significantly influence recovery outcomes.

### Strengths
This study presents significant innovations in understanding the impact of neural injury and synaptic degradation on ventral visual cortex (VVC) function. By simulating progressive weakening of synaptic connections, the research explores the effects of synaptic degradation on visual function, demonstrating the reorganization process of VVC neurons following synaptic injury and its contribution to functional recovery. This progressive synaptic degradation model offers a novel perspective, bringing originality to the field of neural plasticity research. Moreover, using a primate visual cortex model and real-world visual stimuli for experimental simulations, the study enables accurate tracking of visual function recovery. The retraining protocols and gradual degradation simulations are highly precise, uncovering the redistribution of neural load through recurrent connections in specific brain areas post-injury and demonstrating the feasibility of enhancing visual recovery through varied training tasks. Overall, this research holds considerable importance for neurorehabilitation and visual function recovery. The findings on the role of recurrent connections in network reorganization deepen our understanding of synaptic remodeling mechanisms after neural injury and provide a scientific basis for developing rehabilitation interventions centered on recurrent connections.

### Weaknesses
Although this paper presents a progressive synaptic degradation model and demonstrates its potential in visual cortex remodeling, the scope of experimental validation remains limited. Current experiments focus on specific visual tasks, without covering a broader range of visual functions or diverse damage models. Specifically, the model is primarily evaluated using ImageNet classification, which, while a common benchmark, does not fully capture the breadth of visual processing performed by the ventral visual cortex (VVC). Consequently, while the model performs well on the tasks tested, its generalizability and adaptability to other visual tasks remain uncertain. It is recommended to incorporate a wider variety of visual tasks, such as tasks involving object recognition under varying illumination, viewpoint changes, or partial occlusions, to comprehensively assess the model's practical effectiveness. These tasks would better evaluate the model's robustness and ability to generalize beyond the specific conditions of the ImageNet dataset.

The model and experimental design also simplify biological complexity to some extent. For example, synaptic degradation is modeled as a gradual, linear process, but in actual neural injury, synaptic degradation is often nonlinear and accompanied by various physiological changes, such as inflammation and excitotoxicity. This linear simplification, particularly the use of an exponential decay function, may not accurately reflect the complex temporal dynamics of real synaptic injury, potentially affecting the model's accuracy in practical applications. It is suggested to incorporate a more complex synaptic degradation mechanism, perhaps by introducing stochastic elements or modeling different types of synaptic damage, or add a discussion explaining how these biological factors could be addressed in future research.

Additionally, while the paper demonstrates the role of recurrent connections in visual function recovery, the exploration of recurrent network reorganization mechanisms remains relatively superficial. The study does not delve into how specific network modules share or redistribute tasks post-injury, especially failing to clarify the roles of different network nodes in the functional reorganization process. For example, the paper does not analyze how the weights of recurrent connections change during retraining, nor does it investigate the specific contribution of different recurrent pathways to the recovery of visual function. A more detailed analysis of these aspects would provide a deeper understanding of the underlying mechanisms of neural plasticity.

### Questions
In your model, you assume synaptic degradation as a gradual, linear process. However, in real neural injury, this process is typically more complex and nonlinear. Could you elaborate on how you address these simplified biological assumptions?

While the re-establishment of recurrent connections has shown effectiveness in visual recovery, we still lack a detailed understanding of the specific roles of individual modules within the network. Could you further explain or share insights on the roles of each module in the model, particularly in the processes of functional reorganization and recovery from injury?

Your study lacks comparisons with other baseline methods, such as non-recurrent network models or alternative multi-task learning approaches. Such comparisons would more clearly demonstrate the unique contributions of your model. Do you plan to conduct such comparative experiments, or could you clarify the reasons for not including these comparisons?

You mentioned the role of recurrent connections in the recovery process, but the paper does not delve deeply into the interaction between recurrence and neural plasticity mechanisms. Could you further elaborate on how these two aspects interact within the model?

### Soundness
2

### Presentation
3

### Contribution
3
