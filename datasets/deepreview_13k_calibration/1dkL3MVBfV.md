# Dynamic Model Editing to Rectify Unreliable Behavior in Neural Networks

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 5, 6

## Abstract
The performance of neural network models deteriorates due to their unreliable behavior on corrupted input samples and spurious data features. Owing to their opaque nature, rectifying models to address this problem often necessitates arduous data cleaning and model retraining, resulting in huge computational and manual overhead. This motivates the development of efficient methods for rectifying models. In this work, we propose leveraging rank-one model editing to correct model's unreliable behavior on corrupt or spurious inputs and align it with that on clean samples. We introduce an attribution-based method for locating the primary layer responsible for the model's misbehavior and integrate this layer localization technique into a dynamic model editing approach, enabling dynamic adjustment of the model behavior during the editing process. Through extensive experiments, the proposed method is demonstrated to be effective in correcting model's misbehavior observed for neural Trojans and spurious correlations. Our approach demonstrates remarkable performance by achieving its editing objective with as few as a single cleansed sample, which makes it appealing for practice.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Neural network models often underperform when faced with data shifts. Due to their opaque nature, addressing this issue typically involves extensive data cleaning and retraining, resulting in significant computational and manual demands. This drives the need for more efficient model correction methods. This paper introduces a rank-one model editing approach to correct unreliable model behavior on corrupted inputs, aligning it with performance on clean data. The proposed method uses an attribution-based technique to identify the primary layer contributing to the model's misbehavior, incorporating this layer localization into a dynamic model editing process. This enables adaptive adjustments during editing. The authors performed extensive experiments which show that that their method effectively corrects issues related to neural Trojans and spurious correlations with as little as a single cleansed sample.

### Strengths
The paper is quite well written. The problem that is addressed is clearly defined and seems quite relevant for this venue. The proposed method has shown compelling results against all the baselines. Overall, this is an enjoyable paper to read.

### Weaknesses
The key limitations of this method include its reliance on identifying unreliable behaviors and the requirement that both corrupted and cleansed samples are available for effective correction. While the method has shown compelling results on almost all the benchmarks, this heavy reliance on the identification of unreliabilities makes the method less practical. Specifically, the method requires a clear signal of misbehavior to initiate the correction process, which might not always be available in real-world scenarios where the model's failure modes are subtle or unknown. Furthermore, the need for paired corrupted and cleansed samples, even if only a single pair, is a significant constraint. Obtaining a perfectly cleansed sample that precisely counteracts the corruption can be challenging, especially for complex data modalities or sophisticated attacks. Also, it seems to me that this method is mostly applicable to models with simpler computational graphs. For instance, models that involve lots of skip connections, group norm, layer norm, etc. might be quite difficult to correct. The attribution method might struggle to pinpoint the exact layers responsible for the misbehavior in such complex architectures, leading to ineffective or unstable corrections. It is also not clear to me how effective the proposed method is when dealing with stronger more  "aggressive" poisonous attacks. Mentioning how severe the attacks that are considered are and how they compare with other types of attacks might convince the reader more about the efficacy of the method. The paper does not adequately address the potential for the method to be circumvented by adversarial attacks specifically designed to exploit the correction mechanism itself.

### Questions
1. What are the possible research avenues to mitigate some of the limitations highlighted above?
2. How practical is your method for highly complex networks with very intricate computational graphs?
3. How severe are the poisonous attacks that are considered? Are there newer and more severe attacks that could evade your method?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Summary: This paper proposes a novel method for editing unreliable models, drawing inspiration from rank-one editing techniques. The authors demonstrate the effectiveness of their approach through experiments focused on backdoor attacks and spurious correlations.

### Strengths
Strengths:
1. The method's approach of retaining original samples alongside corresponding corrupted samples effectively addresses issues related to performance degradation and data volume constraints.
2. Algorithm 1 employs a clever strategy for dynamically editing the model using attribution methods by appropriately setting thresholds for $\delta$ and $\epsilon$.
3. The experimental section considers critical issues such as backdoor attacks and spurious correlations, providing an analysis of the method on the real-world ISIC dataset, which showcases the method's extensive effectiveness.

### Weaknesses
The definition of "UNRELIABLE BEHAVIOR" remains unclear. While the authors use this term to describe model predictions influenced by backdoors or spurious correlations, a more precise definition is needed, particularly in the context of the proposed rank-one editing approach. It is not immediately obvious why a rank-one update would specifically target and correct these types of issues. The paper lacks a clear explanation of how the rank-one update mechanism is tailored to address the underlying causes of unreliable behavior, such as the specific features or patterns that lead to incorrect predictions. There is no concrete evidence provided to support the claim that this method can effectively "correct the model’s unreliable behavior on corrupt or spurious inputs." The connection between the rank-one update and the mitigation of these issues is not well-established, and the paper would benefit from a more detailed theoretical justification.

The core of the method relies on the key-value optimization in Eq. (1), which is not novel. The authors' primary contribution should therefore be focused on Eq. (2). This equation necessitates a gradient disagreement for estimating the function disagreement, and it also requires a closed-form representation of the function f, which is not typically available for deep neural networks. The paper does not adequately address how this is handled in practice. Furthermore, it is unclear how a feature mapping function is defined for each layer in a neural network. Relying solely on the loss function in the final iteration may not be sufficient and could lead to issues. For Eq. (2), updating $\hat x$ requires a trustworthy direction and appropriate step sizes, yet the paper does not provide a clear justification for using $x$ as a teacher for updating $\hat x$. This approach could be problematic if the update is low-confidence, potentially leading to instability or incorrect adjustments.

Overall, the presentation is confusing and raises significant concerns. The paper would greatly benefit from a reorganization to improve clarity and make the method more self-explanatory. The current presentation feels more like a promotional piece than a rigorous scientific contribution, despite the potential for useful ideas.

### Questions
Question: The model editing process, as illustrated in Figure 3, involves clean samples and their corresponding corrupted samples. How would one edit a model trained on a dataset containing poison and Trojan horses when the original training dataset or clean samples are unavailable?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors apply model editing (very similar to ROME) for the task of removing neural trojans and mitigating reliance on spurious correlations (which in the paper, closely resemble neural trojans) for image classifiers. About half the paper is dedicated to i. explaining ROME, ii. describing some challenges in applying editing to the desired settings, and iii. detailing their modified approach. Their method consists of identifying the best layer to edit by comparing attributions (i.e. via Integrated-Gradients) for clean and poisoned samples, and then "dynamically" applying model editing, which I believe (but am unsure) means making repeated edits until the edited model's overall performance does not deviate much from the original model's overall performance. 

Experiments are conducted using a simple neural trojan and spurious feature for CIFAR10 and ImageNet classification. The proposed method successfully reduces to the attack success rate of the neural trojan to nearly zero without compromising overall accuracy. It also removes any bias to the spurious feature (measured as the increase in performance when the spurious feature is present). Baselines include fine-tuning and methods called P(or A)-ClArC, and are surpassed. Similar results are attained on a more realistic setting of skin lesion classification.

### Strengths
The method seems to work well! ASR is dropped to nearly zero without compromising accuracy, and bias toward spurious features are removed without affecting accuracy. 

The result could be an important result for the mechanistic interpretability community (which is currently garnering lots of attention) as it shows editing techniques can be applied to a second modality and to alleviate existing concerns.

I really liked that a realistic setting was also considered, and that the method seemed to work well in this case too.

### Weaknesses
 **Clarity**: I personally found this paper hard to read. I did not find Sec 4 to be well integrated to the paper. Paragraph 207-215 feels like it should be very important, but it was not clear to me how your method changed to sidestep concerns and if there was empirical evidence showing that this methodological change was truly responsible for improved performance. Specifically, the paper introduces a training process that integrates both clean and corrupted samples, but it's unclear how this addresses the challenges of rank-one editing in domain adaptation, as described in Section 4.1. The theoretical justification for how this integration sidesteps the need for extensive data preparation or mitigates performance degradation is not sufficiently detailed. A more rigorous explanation is needed to connect the theoretical claims to the empirical results. The paper would have benefitted more from taking more time to clearly explain the experiments, imo.

**Novelty over ROME**: Perhaps this relates to the above point, but it is unclear to me exactly how this differs from ROME, which as I understand it, also involves localizing and editing. The iterative nature (which authors term 'dynamic') is perhaps new, but it seems to only marginally improve performance over static editing. Similarly, the comparison to Santurkar's editing work was a bit lackluster (is the main difference that they choose the penultimate layer by default?) It is not clear if the layer localization technique is a significant improvement over existing methods, and the paper does not provide a thorough comparison with other layer selection strategies. The 'dynamic' editing approach, while presented as a key contribution, does not demonstrate a substantial performance gain over a single edit, raising questions about its practical significance.

I am **unsure if this method would work for more realistic spurious correlations**, which would not have a single fixed appearance, as is the case for the spurious features studied (even for the skin lesions, the spurious patches are quite consistent in their appearance). Even a simple benchmark like Waterbirds is not studied (I personally think even Waterbirds is too simple, but it is very established and having a result on it would greatly improve the paper's claim about spurious features). The paper's focus on fixed spurious patterns limits its applicability to real-world scenarios where spurious correlations are often more complex and variable. The lack of evaluation on established benchmarks like Waterbirds further weakens the claim about the method's ability to handle diverse spurious correlations. The experiments on skin lesions, while more realistic, still involve relatively consistent spurious patches, which may not fully represent the challenges of real-world spurious correlations.

### Questions
What is the difference between your method and ROME, aside from (i) applying it to image classifiers (ii) editing iteratively (or 'dynamically'), and (iii) the inclusion of corrupted samples in training (pls correct me if I am interpreting this wrong -- see next question)?

Does this mean you train on the corrupted samples? What if your model has already been trained? Also, don't the corrupted samples need to be included in training to begin with, so that the attack is successful? This part is unclear to me. 
> L207: "Our proposed process of model editing to correct unreliable behaviors involves integrating both original samples x and their corrupted counterpart x˜ into the training procedure"

More minor:
Don't these sentences contradict each other? Maybe you need a name for your method to distinguish it from the standard ROME (which you say doesn't work out of the box).
> L43: "we formally pinpoint two key challenges when applying rank-one editing to domain adaptation, which inevitably lead to diminished model performance and necessitate labor-intensive data preparation (details in § 4.1). Next, we establish that rank-one model editing is
well-suited for correcting model’s unreliable behavior as it intrinsically sidesteps these challenges" 

Some questions for figure 3:
- Should it be key k*? Instead of key v*? (step 3 panel)
- Yellow arrow is pointing wrong way and should be under 'attribution flow'?

What patterns? I think this is important -- it is a lot easier to edit out a reliance on a spurious pattern that does not vary much in its appearance (like in the Trojan case) than it is to edit real spurious features (e.g. to backgrounds). 
Update: I see in the appendix the patterns added are the same as the Trojans -- the only difference in the settings are that the added patterns flip the label in the Trojan case, while they do not in the spurious case. I think this makes your spurious correlations setting unrealistic.  
> L410: "we pollute a proportion of samples of class y by attaching patterns to create spurious samples"

Suggestion for table 4: highlight the accuracy on the samples without the spurious correlation (is this what you mean by clean?) or performance drop for these samples instead of showing the performance for samples with the correlation. It reads a little cleaner to see your method improves accuracy, and better highlights the cost of relying on spurious features (i.e. performance is worse when the feature is absent + correlation is broken).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work considers the problem of spurious correlations learned by a model during training. It proposes the use of rank-1 editing as an approach to correct such model errors while preserving the model’s overall performance. This method is motivated by two challenges in the use of rank-1 editing. One is technical and involves finding rank-1 updates that do not interfere with other facets of model performance. The second is more specific to domain adaptation and involves the need for sufficient quantities of labeled data. The method first utilizes a feature attribution-based approach to locate the layer of the model where editing will yield the biggest improvement. Then it applies rank-1 editing to this layer to correct the spurious correlation in the model. The paper evaluates the approach on models to which a trojan has been injected and models that have learned spurious features related to patches (for both toy and real datasets). Experiments suggest that the approach strikes a good balance between correcting model behavior in specific instances without degrading overall accuracy too much.

### Strengths
**Promising research direction:** Domain adaptation is a serious issue in the application of machine learning to many domains. While the use of rank-1 editing has been proposed before in this setting, the reviewer believes that the suite of tools that editing offers have still not been fully exploited.

**Methodical experiments and results are strong:** Overall, the experimental section is well-written. While the reviewer has some issues with the overall scope of the experiments (see Weaknesses), those that were run seem to be fairly comprehensive and the results are well-described. In the settings where the method is deployed, it performs well relative to the other baselines that are explored.

### Weaknesses
The problem that is addressed is narrow: This work claims to explore domain adaptation, but it only looks at mitigating the presence of very obvious spurious correlations in the data (e.g., trigger patches). The challenges associated with real-world domain adaptation are far more subtle than this. It would have made the work stronger if it had investigated instances of domain adaptation where the differences between domains were more subtle, such as changes in background or lighting conditions, or variations in object pose or viewpoint. If the proposed method worked in such situations, it would be very notable. Alternatively, the paper could shift its language to focus more exclusively on spurious correlations, and perhaps even more specifically on the removal of adversarial triggers, which is closer to the experimental setup.

The challenges that motivate the method are not very clearly described and are never shown empirically to be issues: The work describes two challenges that are meant to motivate the proposed approach. Overall, these are not very clearly described. Indeed, Challenge 2, which involves lack of data in domain adaptation settings, could be easily described outside of the mathematical formalism, but this is not done. Challenge 1 relates to the specific approach to rank-1 editing, specifically the failure of $k^*$ to be included in the statistics matrix $C$. This is stated as one of the fundamental challenges of using rank-1 editing for domain adaptation, but it is never explained why this is specifically a problem for domain adaptation and not a general issue. For instance, it is not clear why the feature $k^*$ would be excluded from the statistics matrix $C$ in a domain adaptation setting but not in other settings where rank-1 editing is applied. Finally, it would help make these challenges more meaningful if some empirical evidence was given to support their centrality. For example, the paper could show that without addressing these challenges, rank-1 editing fails to correct the spurious correlations, or that the performance degrades significantly.

Repeated editing has been explored in the past: To this reviewer’s understanding, the main contribution of the work is the use of feature attribution to locate a layer to edit, the modification of the existing rank-1 editing technique to mitigate an issue with the statistical matrix $C$, and the introduction of dynamic editing. The first and second are new to this reviewer’s knowledge (though the reviewer is not an expert in the breadth of what has been done in the editing space). The impact of repeated editing has been explored in detail in past works (e.g., [1]). It would be good to consider how the present paper fits into such studies. Specifically, the paper should discuss how its approach to dynamic layer selection compares to existing methods of repeated editing, and whether the observed benefits are due to the dynamic selection or simply to the fact that multiple edits are being applied.

### Questions
- Equation (1): What is $f(k^*;W)?
- Lemma 2: What does $x^* \rightarrow k^*$ mean? What is $\mathcal{X}$?

### Soundness
2

### Presentation
2

### Contribution
2
