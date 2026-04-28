# The Super Weight in Large Language Models

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 5, 1, 5, 6

## Abstract
Recent works have shown a surprising result: a small fraction of Large Language Model (LLM) parameter outliers are disproportionately important to the quality of the model. 
LLMs contain billions of parameters, so these small fractions, such as 0.01\%, translate to hundreds of thousands of parameters. In this work, we present an even more surprising finding: Pruning as few as \textbf{a single parameter} can destroy an LLM's ability to generate text -- increasing perplexity by 3 orders of magnitude and reducing zero-shot accuracy to guessing. 
We propose a data-free method for identifying such parameters, termed \emph{super weights}, using a single forward pass through the model.
We additionally find that these super weights induce correspondingly rare and large activation outliers, termed \emph{super activations}. When preserved with high precision, super activations can improve simple round-to-nearest quantization to become competitive with state-of-the-art methods. For weight quantization, we similarly find that by preserving the super weight and clipping other weight outliers, round-to-nearest quantization can scale to much larger block sizes than previously considered.}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the impact of outlier weights in large language models (LLMs), specifically larger weights, which the authors term superweights and superactivations. First, the authors analyze how much these weights and activations affect LLM performance. They then use this as motivation to discuss quantization methods designed to account for superweights and superactivations. Throughout the paper, the authors also discuss the impact of superweight scaling and provide experimental results showing how their quantization method improves upon standard rounding, especially when using larger block sizes within the network.

### Strengths
The paper is well-written and effectively illustrates the importance of superweights and superactivations. I appreciate the discussion on the percolation of superactivations across the network and the identification of superweights across layers (Figure 3). Additionally, I find the potential implications of superweight upscaling presented in Figure 6 quite interesting.

### Weaknesses
While I appreciate the analysis presented in this paper, I am struggling to see the novelty of this work. I may be misunderstanding, but from what I gather, superweights and superactivations have already been discussed in prior analyses of LLMs. Specifically, the observation of outlier weights and activations, and their disproportionate influence on model behavior, is not entirely new. Furthermore, it seems that methods like AWQ and SqueezeLLM inherently focus on superactivations, as they are designed to handle the most impactful outliers during quantization. The proposed method, while effective, appears to be another approach to outlier management, and compared to other weight quantization techniques, the proposed method does not appear to offer significant improvements in terms of performance or efficiency. The paper would benefit from a more detailed comparison to these existing methods, clearly delineating the unique contributions.

### Questions
1. Could the authors provide clarification on the points I raised in the weaknesses section, especially if I may have misunderstood some of the contributions?

2. In Figure 6, do the authors have any insights into the concave behavior of the scaling factor? Are there specific explanations or potential methods for identifying this optimal scaling factor?

3. Regarding the stop word shift in distribution, is it generally accepted that a higher probability of stop words negatively impacts LLM performance?

### Soundness
3

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
The paper is about the discovery of super weights in LLMs that are disproportionately important, pruning these hurts model quality quite a bit. The authors have provided a way to identify these super weights using a forward pass. Super weights are activations are sensitive to quantization effects and hence authors propose a super weight aware quantization method enabling effective quantization.

### Strengths
Novel discovery about the importance of a few handful of neurons: The identification and analysis of super weights and super activations as critical outliers and their positive influence on model's performance is noteworthy and interesting. 

Quantization proposals: Authors went one step further to propose a super weight-aware quantization method to make the best use of these super weights/activations. Data free quantization proposal with on par performance compared to SmoothQuant is also a worthy contribution.

### Weaknesses
Though the discovery is quite interesting, the improvements of proposed methods with existing baselines are quite marginal. In general, such kind of super weights might be a natural phenomenon in any machine learning model. How can one say this is relevant only to LLM's?

The work seems to be very much based on empirical observations (which is not my concern) but more discussions/intuitions/explanations around how/why these super weights are formed will be useful.

### Questions
The paper mostly focuses on post training model weight/activation analysis and identifies certain handful of importance weights/activations. The authors also say that irrespective of the input prompt the super weights are always the same and they mostly occur in the early layer's down projection with some reasoning via skip connections diagram. 

Though these insights are helpful, but it would be good if authors can follow up with what happens during the training process that such super weights are formed in the first place. Does the training methodology in terms of quantization during training/layernorm, gradient scaling, etc play any role in the forming of these super weights?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper investigates the sensitivity of a subset of outliers in LLMs, referring to them as "super weights." The authors conducted experiments to examine the impact of these super weights on model performance.

### Strengths
The authors conducted experimental explorations on the so-called "super weights."

### Weaknesses
1. The necessity of "super weights" is unclear, as outliers are already identified based on the threshold. Increasing the threshold will naturally reduce the number of outliers with very large weights. Given the known importance of outliers in LLMs, emphasizing "super weights" (outliers at a higher threshold) does not appear novel.

2. Figure 1 is misleading. According to the author's definition, "super weights" are a subset of outliers. However, the figure suggests -1.9 is a typical outlier with nearby values being quite small (.1 and .2), implying that zeroing out outliers produces nonsensical text—a widely acknowledged fact. To better demonstrate the significance of super weights, it would be beneficial to explore whether zeroing out all outliers results in poor performance, and similarly, whether zeroing out just a small subset (e.g., 20-30) leads to comparably severe degradation.

3. Table 1 raises critical concerns. First, the criterion for selecting outliers needs specification. Second, the "Prune SW, +SA" setting in Lines 146-152 is confusing, as it suggests pruning super weights while partially restoring super activations enhances quality. However, the authors did not prune activations, leading to confusion about this claim.

4. Table 2 appears redundant and fails to convey meaningful information. Replacing it with visual representations of "super weights" distributions would be more informative, as the current table occupies considerable space without offering clear insights.

5. Figure 2 is difficult to interpret. The depiction of super weights and their impact, such as generating nonsensical text, is not clear. The use of the same color block in both the network and the output is puzzling. Are the model's dynamics linear? How do the output and weights share the same significance? Clarification is needed on whether this figure is based on assumptions or empirical data.

6. In Lines 189-190, the term "super activations" is introduced but lacks clarity on whether it is threshold-based or aligns with corresponding weights, which could be time-consuming. The authors should clarify this terminology.

7. The paper contains several unprofessional notations. For example, "Yij" should be corrected to "Y_{ij}" in Line 204, and similarly, "Xik" and "Wjk" should be "X_{ik}" and "W_{jk}" in Line 205. The inconsistency in notation and dimensions between "d" and "D" in Line 204 suggests a lack of careful writing and review, raising concerns about the overall professionalism of the paper.

8. Lines 198-210, which discuss the identification of super weights, are crucial yet unclear. The selection criteria for super weights remain ambiguous and need a precise mathematical description. Readers should understand the definition of outliers and the criteria for their selection explicitly.

9. The paper lacks consistency in terminology. "Super weights" sometimes refer to both activations and weights, and at other times only to weights, adding confusion. In Line 306, the term "super outliers" is introduced, suggesting that the paper should maintain consistent terminology from the start, including in the title, if both weights and activations are discussed.

### Questions
Please refer to the weaknesses section above.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper reveals that Large Language Models (LLMs) contain a very small subset of weights
(super weights) that are extremely important, where removing them severely degrades model
performance. The researchers developed an efficient, data-free method to identify these super
weights using only a single forward pass. They further investigated how these super weights
influence network behavior by analyzing their relationship with activation outliers. Building on
these insights, they proposed a quantization approach that carefully preserves these super
weights while effectively compressing other weights, resulting in the maintenance of model
quality after compression.

### Strengths
The discovery is interesting and the proposed quantization method is easy to implement, which
can maintain better performance compared to Round to nearest quantization with the same
block size.

### Weaknesses
The authors failed to show how the proposed methods can improve the SOTA.
1. Although the method is data-free, its performance does not exceed SOTA methods like
SmoothQuant, given incorporating a small calibration dataset would not increase the
quantization complexity much.
2. The author mentions that this method is hardware-friendly, but no experiments to show
its effectiveness in improving latency, throughput, memory usage, etc.

### Questions
1. For equation 1, the median is used to replace super activation. Is getting the median
time-consuming since GPU is not good at sorting? (Although there are GPU-version
sorting algorithms)
2. The authors mentioned that SmoothQuant does not report on some models this paper
evaluates, they compare our results with naive W8A8 quantization (line 407 - line 409).
Can the authors run SmoothQuant on these methods since it is open-source? The naive
W8A8 is a too-weak baseline.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the concept of "super weights" in Large Language Models (LLMs), identifying a small number of individual weight parameters (as few as one) that have a disproportionately large impact on model performance.  Pruning these super weights drastically reduces the quality of generated text, while pruning thousands of other larger-magnitude outliers has a negligible effect.  The paper proposes a data-free method for identifying super weights based on their connection to "super activations," exceptionally large activation outliers previously observed in LLMs.  Finally, the paper demonstrates that preserving super weights and activations during quantization significantly improves compression quality, achieving competitive results methods like SmoothQuant.

### Strengths
- The identification of "super weights" and their connection to super activations represents a novel and potentially significant finding in understanding the inner workings of LLMs.
- Connection of "super weights" to quantization accuracy is quite interesting and has practical implications.
- The paper provides a clear methodology for identifying super weights and evaluating their impact, along with an index of super weight coordinates for common LLMs, facilitating further research.

### Weaknesses
# Major

- Connection to Adversarial Examples: The literature extensively documents how small changes in the input domain can drastically alter output probabilities. Consequently, significantly harming the network by removing weights, as demonstrated, is somewhat expected.  The authors should explicitly discuss the connection between super weight removal and adversarial examples, and cite relevant work exploring the impact of specific weights on adversarial vulnerability. The input space, in a way, is just another activation, and the distinction between adversarial images and activation outliers may not be as substantial as it seems. It would be beneficial to explore if there are studies analyzing the effect of individual weights on the creation of adversarial examples, especially given that some research suggests sparse networks exhibit greater robustness against such attacks.

- Magnitude Pruning Baseline: In Table 1, the comparison of super weight pruning with global magnitude pruning may not be the most informative. A stronger baseline would involve pruning only within the layer where super activations occur, and specifically, only the same number of weights as the super weights. This would better isolate the impact of the super weight itself, and demonstrate that it is not simply the case that the least magnitude weights are the most important. The current approach of pruning globally identified outliers does not provide a fair comparison, as the super weight identification process is layer-specific.

- Quantization Baseline: The "Naive W8A8" quantization baseline should incorporate clipping. The current presentation makes it unclear whether the observed improvements stem from outlier removal or clipping, especially since super weight handling affects only a single layer during quantization, while clipping is applied to every layer. Furthermore, it should be noted that the clipping threshold is determined using Wikitext-2, which is also included in the evaluation of quantized models.

# Minor

- Terminology: The term "extreme" might be more descriptive and informative than "super" when referring to these weights.

- Weight Distribution Visualization: Including a histogram visualizing the position of the super weight within the overall weight distribution would enhance understanding of its magnitude relative to other weights.

### Questions
- Section 3.2, "Prune SW+SA":  The description of the "Prune SW+SA" condition in Section 3.2 is unclear.  Specifically, how does this condition differ from the original model?  I understand that super activations typically precede super weights in the model.  Therefore, I am unsure what modification is being made in "Prune SW+SA" and how it distinguishes itself from the original, unpruned model.  Could you please elaborate on this procedure?

### Soundness
2

### Presentation
3

### Contribution
2
