# Credit-based self organizing maps: training deep topographic networks with minimal performance degradation

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 8, 5

## Abstract
In the primate neocortex, neurons with similar function are often found to be spatially close. Kohonen's self-organizing map (SOM) has been one of the most influential approaches for simulating brain-like topographical organization in artificial neural network models. However, integrating these maps into deep neural networks with multitude of layers has been challenging, with self-organized deep neural networks suffering from substantially diminished capacity to perform visual recognition. We identified a key factor leading to the performance degradation in self-organized topographical neural network models: the discord between predominantly bottom-up learning updates in the self-organizing maps, and those derived from top-down, credit-based learning approaches. To address this, we propose an alternative self organization algorithm, tailored to align with the top-down learning processes in deep neural networks. This model not only emulates critical aspects of cortical topography but also significantly narrows the performance gap between non-topographical and topographical models. This advancement underscores the substantial importance of top-down assigned credits in shaping topographical organization. Our findings are a step in reconciling topographical modeling with the functional efficacy of neural network models, paving the way for more brain-like neural architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Credit-Based Self-Organizing Maps (CB-SOM), a novel algorithm designed to integrate topographical organization into deep neural networks by aligning with top-down learning processes in DNNs. This new method modifies the traditional Kohonen’s Self-Organizing Map (SOM) to assign credit based on each unit's contribution to minimizing task loss. CB-SOM significantly improves object recognition performance compared to prior topographical models while maintaining alignment with the ventral visual cortex of macaques and humans. The model enhances representational alignment with neural activity in both early and high-level visual cortices, displaying substantial improvements over previous approaches.

### Strengths
1. The paper addresses the intriguing challenge of integrating topographical organization into deep neural networks, a problem with significant implications for both artificial intelligence and neuroscience.

2. The authors clearly articulate the motivation behind their work, highlighting the need to reconcile the performance of self-organized neural networks with the functional efficacy observed in biological systems.

3.  A comprehensive literature review provides context and demonstrates the paper's grounding in existing research.

4. The paper offers a thorough explanation of the proposed CB-SOM algorithm, including a detailed summary of the parameters for the experiments.

5. The authors effectively link their findings to supporting papers, relating the observed behaviors of their model to biological phenomena, thereby strengthening their claims.

6. The results showcase the superior quality of learned representations in CB-SOM and its enhanced alignment with neural responses in both human and non-human primate brains, demonstrating significant improvements over previous models.

### Weaknesses
1. The paper does not adequately assess / estimate the efficiency and computational time required for the CB-SOM learning algorithm, which could be a critical factor for its practical application. Specifically, the paper lacks a detailed analysis of the time complexity of the algorithm, particularly the best-matching unit (BMU) selection process and the weight update mechanism. It is unclear how these operations scale with the size of the feature maps and the number of units in the SOM, making it difficult to evaluate the algorithm's suitability for large-scale datasets or real-time applications.

2. The 'main contributions' statement in the introduction claims substantial improvements in object recognition performance vs prior topographical NNs, but does not comment on performance degradation compared to non-topographical models like ResNet. Including a comment on this trade-off would clarify the performance implications. The absence of a direct comparison with state-of-the-art non-topographical models in the introduction leaves the reader with an incomplete picture of the method's overall performance relative to the broader landscape of deep learning models.

3. The trade-off in performance (as seen in Figure 2A) may affect the algorithm's appeal for studies outside neuroscience. Additional commentary from the authors on this would be beneficial. The observed performance gap raises concerns about the practical utility of the algorithm in applications where high accuracy is paramount, and the authors should explicitly address this limitation and discuss potential mitigation strategies.

4. The "Deep topographical neural network" section would benefit from a high-level summary of how the previous approaches in the literature impact overall performance, providing clearer context for readers. A quantitative comparison of the performance of previous topographical models, including the specific accuracy drops they incur compared to non-topographical counterparts, would be beneficial for the reader to understand the context of the present work.

5. It would be essential to provide a link to the code to ensure reproducibility

6. Figure 2A should include comparison with the other baselines shown in Figure 2B,for completeness

### Questions
Minor: 

1. It would be interesting to discuss implications of this claim ‘resulting CB-SOM model displays substantial improvements in representational alignment with recordings from macaque visual cortex and imaging data from human visual cortex’

2. I am curious if you can provide some concrete examples for this claim ‘we believe our results are not limited to this task and could potentially be generalized to other tasks and contexts that may include multiple sensory modalities.’

3. A few typos e.g. ‘of of’ in line 510 and ‘th’ in line 205

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study proposes an intriguing way to force topography in ResNet18. Earlier topographical models had exhibited significant drops in accuracy, but this study provides an effective way to alleviate the accuracy drop.

### Strengths
The authors extensively compared the model’s responses and neural responses recorded from Nonhuman primates and humans, which will greatly interest readers of brain science research. Their study may also be of interest to the deep learning research community because it proposes a way to impose local structure to deep learning models, which may aid us build domain-specific models with specific local structure. The authors evaluated a single architecture only. It would be more compelling if they tested more architectures.

### Weaknesses
The authors evaluated a single architecture only. It would be more compelling if they tested more architectures.

### Questions
I do have two questions. 

When the authors mention “units” of ResNet18, are they referring to ResNet18’s channels? If so, some clarification is needed. If not, a detailed explanation is needed. 

In general, lateral connections in the brain have been believed to play a role in shaping topography. My second question is, could the authors provide insights into how their proposed mechanisms are related to lateral connections in the brain?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposed a method for seamlessly incorporating topographical learning with top-down supervised learning.
This paper's primary contribution is the proposal of an Action-Based Self-Organizing Map (CB-SOM) that utilizes the gradient of a loss function as the criterion for selecting the Best Matching Unit (BMU) for topographical learning.

The paper is generally very well written and supported with interesting and valid experiments.

The clarity of the paper was significantly improved after the revision.

### Strengths
The proposed method makes sense, mainly when a top-down loss function can be defined, in that the neural network should select a BMU based on the contribution of the topographical hidden neurons to the loss function. The reviewer agrees with the authors that the integration of the conventional SOM (AB-SOM) suffers from over-representations of some hidden neurons that do not necessarily contribute to the learning performance of the whole network. The proposal clearly alleviates this discrepancy.

This paper also offers interesting arguments that compare the resulting CB-based SOM with primates, which is essential to argue about the biological validity of the proposed model.

The paper is also very clearly written and easy to understand.

### Weaknesses
There are no essential weaknesses in this paper. But there are some unclarities, listed in the Questions parts of this review, that should be clarified before this paper is ready for publication.

1. As the selection of a BMU always depends on the gradient of a loss function, it is unclear how the network chooses a BMU without a loss function, for example, in the neural network's running stage. It is outside the scope of the paper, but biological neural networks also deal with reinforcement learning. Hence, the authors need to give at least their comments on how to deal with this matter.

2. It is unclear whether a reconciliation between AB-SOM and CB-SOM occurs, at least in the latter stage of the learning rule. In short, does the CB competition converge into the AB competition in the latter stage of the learning process? It would be insightful if the authors could prove or disprove that CB competition is the transient state of AB competition.

3. There is a model that seamlessly combines topographical learning and top-down reinforcement learning as follows:
a) P. Hartono, P. Hollensen and T. Trappenberg, "Learning-Regulated Context Relevant Topographical Map," in IEEE Transactions on Neural Networks and Learning Systems, vol. 26, no. 10, pp. 2323-2335, Oct. 2015, doi: 10.1109/TNNLS.2014.2379275.
b) P. Hartono, "Mixing Autoencoder With Classifier: Conceptual Data Visualization," in IEEE Access, vol. 8, pp. 105301-105310, 2020, doi: 10.1109/ACCESS.2020.2999155.

These two papers share many similarities with the proposed paper. They also derive a new modification rule for the reference vectors associated with the topographical neurons. They demonstrate that the conventional SOM may be a particular case for general topographical representations in supervised models.

The authors must argue their proposal's novelties and advantages compared with these past works.

4. There is no neighborhood function during the operation stage. All of the filters generate their outputs without any topological constraints. Is my understanding correct?

5. Regarding the difference between your model and the rRBF in [Hartono 2015, 2020]: while their model did not explicitly select the BMU based on the loss gradient, the loss gradient is included in the filters' modification. Hence, the filters with large gradient losses are the ones that are modified the most. In contrast, filters with low gradient values (credits) will be less modified. Doesn't this make your model practically equivalent to theirs?

6. Line 634 exceeds the frame of the paper.

7. [Hartono 2015, 2020] are journal papers, not conference papers, so please fix line 596 and line 602.

### Questions
1. As the selection of a BMU always depends on the gradient of a loss function, it is unclear how the network chooses a BMU without a loss function, for example, in the neural network's running stage. It is outside the scope of the paper, but biological neural networks also deal with reinforcement learning. Hence, the authors need to give at least their comments on how to deal with this matter.

2. It is unclear whether a reconciliation between AB-SOM and CB-SOM occurs, at least in the latter stage of the learning rule. In short, does the CB competition converge into the AB competition in the latter stage of the learning process? It would be insightful if the authors could prove or disprove that CB competition is the transient state of AB competition.

3. There is a model that seamlessly combines topographical learning and top-down reinforcement learning as follows:
a) P. Hartono, P. Hollensen and T. Trappenberg, "Learning-Regulated Context Relevant Topographical Map," in IEEE Transactions on Neural Networks and Learning Systems, vol. 26, no. 10, pp. 2323-2335, Oct. 2015, doi: 10.1109/TNNLS.2014.2379275.
b) P. Hartono, "Mixing Autoencoder With Classifier: Conceptual Data Visualization," in IEEE Access, vol. 8, pp. 105301-105310, 2020, doi: 10.1109/ACCESS.2020.2999155.

These two papers share many similarities with the proposed paper. They also derive a new modification rule for the reference vectors associated with the topographical neurons. They demonstrate that the conventional SOM may be a particular case for general topographical representations in supervised models.

The authors must argue their proposal's novelties and advantages compared with these past works.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper contributes an original idea for training supervised deep neural networks models whose layers show topographical organization due to self-organization. It is shown that object recognition performance is reduced less by this than by a naive approach of introducing self-organization. It is further shown that DNNs trained by this CB-SOM algorithm exhibit orientation selectivity in lower layers and category selectivity in higher ones. Comparisons to human FMRI studies are performed, indicating as good match.

### Strengths
The paper presents an original idea to tackle the long-standing problem of generative classification. It is well-organized and easy to read, with some minor glitches here and there. The technical quality of conducted experiments is good. It shows that self-organization can be shown when training CNNs on complex benchmarks like ImageNet while degrading classification performance significantly less than other models.

### Weaknesses
The main weak point is that the advantage of topographical organization is somehow assumed to be self-evident. Is there a functional advantage to having this property? As long as this is unclear, it is hard to accept that performance degradations as you show them are acceptable

Another issue is that the CB-SOM update rule is derived ad hoc, without reference to minimizing a loss. So there are no convergence guarantees or anything, which is bad from a conceptual perspective. It would be strongly desirable to derive this update rule from a loss function that is added to the supervised loss. A possibility is the energy-based SOM model of Heskes [1]

Furthermore, some technical aspects of the model are not clearly described, see comments below

Lastly, orientation/category-selectivity must be compared to a purely supervised model to assess whether the effect would not have occurred without CB-SOM. It is well-known that filters in lower CNN layers develop orientation selectivity as well.

Related work could include works on topologically organized GMMs [2,3] as well as energy-based SOM [1].
3.1 can be more concise, the formula is well known
3.2 is unclear. What are "the errors between each layer’s winning unit’s weight and other units’ weights within that layer ..." ? Just the same as $w_c(t)-w_{ij}(t)$ for AB-SOM? A formula would help here!
3.2 should be derived from minimizing a loss, e.g., Heskes? Otherwise, what is justification for post-hoc weight adjustment?
3.3 How does a 3D structure (neurons are organized in width/height/channel dimensions) like a convLayer fit with the 2D organization assumed in CB-SOM? This must be explained as it is critical to the understanding of the approach
4.1 It should be better described how training AB-SOM works in this setting
4.1 from line 243: CTA is unclear. Either explain fully, here, or not at all and leave to appendix
Fig.3a: what are we seeing in the orientation-selectivity plots? All filters arranged on a 2x2 grid? Not terribly clear to me...
All of Sec.4: this analogy to human brains is interesting, but does it serve a purpose? Why would we want this, given that object recognition is impaired by it? This question needs to be answered, imho, to assess the value of these contributions
All of section 4: The observation of category/orientation selectivity would more compelling if you compared these to plots for a ResNet that was trained in supervised fashion only, without the CB-SOM "add-on".

### Questions
The observation of category/orientation selectivity would more compelling if you compared these to plots for a ResNet that was trained in supervised fashion only, without the CB-SOM "add-on". Because it is not clear that the selectivity you observe does not come from the supervised part already. Do you have any insights on this?

### Soundness
3

### Presentation
3

### Contribution
1
