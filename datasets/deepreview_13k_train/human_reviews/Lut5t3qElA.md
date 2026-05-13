# Unsupervised Disentanglement of Content and Style via Variance-Invariance Constraints

- Decision: Accept
- Scores: 6, 6, 6, 6, 8

## Abstract
We contribute an unsupervised method that effectively learns disentangled content and style representations from sequences of observations. Unlike most disentanglement algorithms that rely on domain-specific labels or knowledge, our method is based on the insight of domain-general statistical differences between content and style --- content varies more among different fragments within a sample but maintains an invariant vocabulary across data samples, whereas style remains relatively invariant within a sample but exhibits more significant variation across different samples. We integrate such inductive bias into an encoder-decoder architecture and name our method after V3 (variance-versus-invariance). Experimental results show that V3 generalizes across multiple domains and modalities, successfully learning disentangled content and style representations, such as pitch and timbre from music audio, digit and color from images of hand-written digits, and action and character appearance from simple animations. V3 demonstrates strong disentanglement performance compared to existing unsupervised methods, along with superior out-of-distribution generalization and few-shot learning capabilities compared to supervised counterparts. Lastly, symbolic-level interpretability emerges in the learned content codebook, forging a near one-to-one alignment between machine representation and human knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
They propose an unsupervised method to disentangle content and style representations.  They use vector-quantized autoencoder architecture and incorporate variance-versus-invariance constraints. Their method benefits from meta-level inductive bias, and shows out-of-distribution generalization. They demonstrate their method’s effectiveness across diverse applications such audio, images and video clips. Moreover, the learned codebook enables interpretable features.

### Strengths
++ Unsupervised approach for separating style and content, which is a plus for domains where labeled data is unavailable or scarce

++ Generalizes across audio, image and video data. 

++ Content representations show interpretable properties. 

++ Performs well for out of distribution styles

### Weaknesses
-- They assume content elements are distinct, which can limit its application in domains with overlapping content. This assumption is particularly restrictive when dealing with complex data where content components are not easily separable. For example, in polyphonic music, multiple instruments or notes often overlap, making it difficult to define distinct content elements. Similarly, in natural scenes, objects frequently occlude each other, leading to ambiguity in content representation.

-- The method is optimized for data with predefined fragments, which may not generalize well to continuous or unsegmented data types. This reliance on pre-segmented data limits the method's applicability in scenarios where such segmentation is not readily available or is inherently ambiguous. For instance, in continuous speech, the boundaries between phonemes or words are not always clear-cut, and relying on predefined segments might introduce artifacts or inconsistencies. The method's performance on continuous video data, where actions and scenes blend seamlessly, is also questionable.

-- The experiments are done on relatively small datasets. This raises concerns about the method's ability to scale to real-world scenarios involving large and diverse datasets. The limited scale of the datasets used in the experiments might not fully capture the complexities and variations present in real-world data, potentially leading to an overestimation of the method's performance and generalization capabilities.

### Questions
- How does the choice of codebook size (K) affect interpretability and disentanglement performance?  

- The method uses specific values for the relativity parameter r and the V3 loss weight beta  depending on the dataset. Could you clarify the intuition behind selecting these values? How sensitive the performance is to different values of these hyperparameters?

- The paper mainly utilizes small datasets with specific content-style boundaries. How does it scale with larger datasets?

Minor issues: 
Line 463: The term "contennt" should be corrected to "content."

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
4

### Summary
This paper introduces an unsupervised method named V3 (variance-versus-invariance) for disentangling content and style representations from a sequence of observations. The method is based on the assumption that content varies significantly within a sample but maintains a consistent vocabulary across samples, while style remains relatively invariant within a sample but varies significantly across samples. V3 integrates this inductive bias into an encoder-decoder architecture and demonstrates its effectiveness across multiple domains and modalities, including music audio, handwritten digit images, and simple animations. The paper reports that V3 outperforms existing unsupervised methods and even surpasses supervised methods in out-of-distribution generalization and few-shot learning. Additionally, V3 exhibits symbolic-level interpretability, aligning machine representations closely with human knowledge.

### Strengths
1. The V3 method offers a novel unsupervised disentanglement approach that leverages the universal statistical differences between content and style. This is a creative application of variance-invariance constraints within an encoder-decoder framework, distinct from traditional methods that rely on supervision or paired data.
2. The loss calculation method proposed by V3, based on content and style, is concise and clear, aligning with human cognitive characteristics. Humans also tend to keep the style of the same sample similar while focusing on the content differences across different samples.
3. The model proposed in the paper is applicable to the learning of multiple modalities of style and content, including images, music, and animations, demonstrating strong generalizability. Moreover, the loss calculation pattern presented is not limited to the paper model but can also be applied to other related models for style and content learning.
4. The paper is well-structured, with a clear problem statement, methodology, and experimental evaluation. The use of datasets from multiple domains enhances the robustness of the research findings. The logic is strong, and the hierarchy is clear. The visualization of learned representations also helps readers better understand the results.

### Weaknesses
1. The paper's approach to learning sample content and style is reliant on datasets with a specific structure, which may limit its effectiveness when applied to images with varied or complex styles. For example, the Written Phone Numbers dataset contains only one digit in a specific position on each image, but the style of the digit can vary; in SPRITES, the character's position is fixed, and the form is also relatively uniform. If an image contains more content or more complex content, such as multiple objects with varying styles and positions, the model may have difficulties learning content and style. The assumption that content varies significantly within a sample while style remains invariant may not hold true in these more complex scenarios, potentially leading to the model misinterpreting style as content or vice versa.
2. The Ablation study reveals that certain components of the loss function may adversely affect performance metrics, suggesting a need for a deeper investigation into the roles and interactions of these components within V3. Specifically, the study should explore why removing certain loss terms leads to performance degradation in some cases but not others. This requires a more granular analysis of how each loss component contributes to the disentanglement process and whether the weighting of these components is optimal for different datasets.
3. It appears that V3 may have difficulty distinguishing between some similar contents during recognition. Similarly, although the paper may not mention it, V3 may also have similar problems with distinguishing styles, thus limiting the style discrimination between different samples. This limitation could stem from the model's reliance on variance and invariance assumptions, which may not be sufficient to capture subtle differences in either content or style. The model might collapse similar styles into a single representation, hindering its ability to perform fine-grained style transfer or recognition tasks.
4. Some important related works[a,b] are missing, which also rely on some assumption to disentangle content and style.   The detailed comparison should be included, especially on the basic assumptions and the scope of suitable cases.
a. Retriever: Learning Content-Style Representation as a Token-Level Bipartite Graph
b. Rethinking Content and Style: Exploring Bias for Unsupervised Disentanglement.

### Questions
1. It is better to evaluate V3 on  more complex or challenging datasets, such as face datasets FFHQ? And It is better to add discussion on 
 potential limitations of V3 when dealing with more complex data containing multiple contents or styles within a single sample.
2. Since V3 uses different losses to control content and style representations through self-supervised means, is there a risk that the representations intended to learn style might inadvertently capture content instead? How can it be ensured that there is not too much coupling between content and style representations? I suggest to conduct an analysis showing how much content information can be recovered from the style representations and vice versa.
3. Why is it necessary to apply VQ to content representations to form a codebook? What would be the impact on the learning results if VQ were not used? Seeing corresponding results in the Ablation study could be more convincing. 
4. Are the numbers of content and style representations in V3 the same? Considering that the actual samples may have varying quantities suitable for representing content and style, would setting different numbers for content and style representations in the same training round make a significant difference in the results?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes an unsupervised method that learns from raw observation and disentangles its latent space into content and style representations based on the meta-level insight of domain-general statistical differences between content and style.

### Strengths
1. The proposed method does not rely on external supervision such as labels.
2. The proposed method can generalize to unseen data.
3. The disentangled content representations align with human perceptions in some cases.

### Weaknesses
1. The paper does not explicitly discuss how the codebook size and codebook dimension are determined. This could limit the application of the proposed method to different datasets. Specifically, the lack of a principled method for setting these hyperparameters makes the method difficult to reproduce and adapt. The paper should provide guidelines or a sensitivity analysis to show how performance varies with different codebook sizes and dimensions.
2. The experiments are all conducted on toy datasets. This weakens the method's practical use in real-world scenarios. For example, for audio disentanglement, the musical note disentanglement is too simple. It is recommended to perform real-world disentanglement experiments such as voice conversion using VCTK. Furthermore, the paper should demonstrate the method's robustness to more complex and noisy data, which is common in real-world applications. The current experiments do not adequately address the challenges of real-world data.

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
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an unsupervised disentanglement algorithm between styles and content, based on the assumption that style information remains consistent within samples, but varies across samples; whereas content information varies within samples, but the aggregated content is stable across samples due to the fixed vocabulary.

### Strengths
1. This paper proposes an innovative disentanglement algorithm that does not rely on external labels of the style or content, making a novel contribution over the existing work, most of which requires external labels.

2. There is a clear rationale behind the proposed algorithm, and the rationale is interesting

3. The presentation in the paper is very clear.

### Weaknesses
1. Although the proposed method does not rely on any external labels, it seems to be built upon rather strong assumptions. In particular, the method assumes that the aggregated content of a sample should stay constant across different samples, at least more stable than the style. This assumption is very strong, and there are many scenarios where this may not hold. First, if the content information in each example is too small to exhaust all the possible combinations, then the content would still vary greatly across samples. For example, in the written digit case, if each example only contains one digit, the method would fail because it relies on observing variations within a sequence of observations to disentangle content and style. This limitation may also hold for many other scenarios, such as Chinese calligraphy, which typically only contains very few characters, paintings containing only one object, etc. Second, if the content information exhibits too much variability, then the content across different statements may still have more variability than style. For example, consider short passages of different languages, where the content is the meaning of the passage and the style is language. The content in this case still varies greatly across different passages. Meanwhile, the authors also acknowledge that the method cannot deal with large content vocabularies. This limitation, together with the limitation discussed above, significantly limits the applicability of the proposed method.

2. Related to the first limitation, the experiment section seems to focus on very simple, carefully crafted toy scenarios that happen to satisfy the assumptions of the proposed method. There is no experiment on real-world scenarios, such as disentangling real human speech, photos, paintings, music, passages, etc. The lack of real-world experiments adds to the concern that the assumptions made by the proposed method may deviate too much from real-world cases to render the method useful. Specifically, the method's reliance on observing variations within a sequence of observations is not tested in scenarios where such sequences are not naturally present or are difficult to define.

3. (Minor) On page 5, the authors state that 'Theoretically, we aim to measure the consistency of codebook usage distribution along the sample axis, which is not differentiable'. This is not necessarily true. We can derive a soft, differentiable distribution of codebook usage via a softmax codebook selection. That is, for each codebook selection, rather than have a one-hot vector indicating which code is selected, we can derive a softmax selection, which is very common in deep-learning-based vector quantization methods, such as VQ-VAE. As a result, I believe that using the mean content vector to represent the distribution information may be improved.

4. (Minor) In line 242, the authors state that 'Content should be more variable within samples than across samples'. This is an overly simple statement. A more precise version should be 'Content should be more variable within samples than the sample-wise aggregated content across samples'.

### Questions
Can the author elaborate a bit more on the experiment setting of Section 4.2?
'we evaluate the models’ content-style disentanglement ability by conducting a retrieval experiment to examine the nearest neighbors of every input zc and zs using ground truth content and style labels, evaluated by the area under the precision-recall curve (PR-AUC) and the best F1 score'

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose a method to learn representations from an adapted VQ-VAE that disentangle content and style based on their different statistical characteristics: style is more constant over patches of a sample, whereas content can vary.

### Strengths
The paper is well written and easy to follow. The method is well motivated and described and results are nicely presented.

### Weaknesses
I have few comments on the main body of the paper, so please do not see this as a "few line review", I just do not have much to say.

**Experiments**: 
* 3 of 4 are on synthetic data with only SVHN being a "natural" data set and even that is cropped to the task. 
* It is of course right to demonstrate that the model performs well on data that follows its assumptions. 
* However, it would be informative (a) to see results on more natural datasets, and (b) to see how the model performs where assumptions do not hold so well, if only as a benchmark for future improvement.

### Questions
none

### Soundness
3

### Presentation
4

### Contribution
3
