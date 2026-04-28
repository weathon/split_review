# Low Compute Unlearning via Sparse Representations

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 8, 6, 6

## Abstract
Machine \emph{unlearning}, which involves erasing knowledge about a \emph{forget set} from a trained model, can prove to be 
costly and infeasible using existing techniques. We propose a 
low compute unlearning technique based on a
discrete representational bottleneck. We show that the proposed
technique efficiently unlearns the forget set and incurs negligible damage to the model's performance on the rest of the data set. We evaluate the proposed technique on the problem of \textit{class unlearning} using four datasets: CIFAR-10, CIFAR-100, LACUNA-100 and ImageNet-1k. We compare the proposed technique to SCRUB, a state-of-the-art approach which uses knowledge distillation for unlearning. Across all three datasets, the  proposed technique performs as well as, if not better than SCRUB while incurring almost no computational cost.\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies machine unlearning in the setting of models with discrete key value bottlenecks, specifically in the setting where compute is limited. Specifically, this work focuses on models possessing discrete key value bottlenecks, an information bottleneck proposed recently. The use of this bottleneck facilitates the use of the proposed methods, which identify which keys are necessary for predictions of a) groups of samples, and b) certain classes. The methods are zero-shot, and their effectiveness at unlearning in this situation is demonstrated empirically.

### Strengths
The paper has several strengths:

- The proposed methods appear to be highly effective at the tasks of model unlearning (based on the empirical results proposed in Section 5). 
- The proposed methods are significantly more compute-efficient than existing methods (SCRUB), while attaining similar levels of accuracy.

### Weaknesses
The paper has several weaknesses:

**Clarity of Exposition**

- The paper is tricky to parse since no equations representing any of the operations (either describing the mechanics of the DKVB or the unlearning strategy) are provided. This adds ambiguity that should be avoided. Other mathematical details that are important for readers are the exponential moving average used for key initialization. I recommend the authors provide these formal details, at the very least in the appendix. Furthermore, the algorithmic descriptions are imprecise. For example, the inputs and outputs of the algorithms are not clearly defined, and functions such as 'argsort' are used without prior definition. The notation used to describe the range of indices is also imprecise.
- There are some issues with imprecise language as well, which I recommend the authors address in subsequent revisions, as they affect the readability of the paper. Two examples that stood out to me were:
    - For instance,  on lines 223-224, the phrase  "This ensures that the representations are distributed sparsely enough." This is an unclear statement. It would help significantly if the authors elaborated upon this in a precise fashion.
    - Similarly, in lines 238-239, the authors write "Technically, this approach requires access to the original training data corresponding to the forget class. However, it is also possible to carry out this procedure with a proxy dataset that has been sampled from a distribution close enough to that of the forget set." This is somewhat contradictory, and should be clarified.
- Typos: there are a few typos in this work. For instance: "sufficient" -> sufficient, "ther specific subset" -> the specific subset.

**Experimental Results**

There are some points in the experimental section that could be made more clear.
-  The experimental results in Section 5.2 (for different numbers of samples) should be tabulated neatly and legibly. As is, it is slightly confusing and tricky to parse.
- In Appendix A.7, it's stated that for the ResNet50 model, either the third last or fourth last layers are used in the encoder backbone. It's unclear why these particular layers were chosen for this task. Furthermore, the experimental slate may be limited. In the experiments, unlearning is performed on the best performing class, where the effectiveness is high. However, the reduction in forget class accuracy may not be the only metric of interest. For other classes, particularly those upon which the model predicts poorly, may also be commensurately high (as forgetting, say, class 3 in CIFAR10 may also cause forgetting in class 2). A better experimental comparison would be to compare the *average* drop in forget/remain class accuracies over all classes, as is the case in other works.

### Questions
I have a few questions about this work.

1. On lines 179-182, it's stated that "Although one could argue that our methods lean towards a weak unlearning strategy–given the pre-trained backbone might retain some information about the forget set–our approach deviate from the strict definition of weak unlearning as outlined by Xu et al. (2023)." This is a major concern, particularly if you take an encoder and a DKVB trained on Imagenet. Moreover, this contradicts later points in the paper where the authors consistently refer to "complete unlearning" (i.e. lines 427-429, 460-463).  If the goal is to unlearn a class (for instance) totally, isn't removing that class' information from the encoder as well crucial to the success of the method?

2.  On lines 253-255, the authors state "However, using one approach over the other may be more practical or even necessary, depending on the task at hand." Could the authors elaborate more upon this point? For what tasks would one use UvA over UvE (and vice-versa)?

3. On lines 257-259, the authors state "Moreover, the requirement of access to original training data of the forget class can also be circumvented under appropriate assumptions". Could the authors elaborate upon those assumptions? Moreover, since this is a strong claim made by the authors, is there any theoretical or empirical justification for this claim

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper propose a mechanism, based on prior work on the discrete key-value bottleneck (DKVB), for tacking the unlearning problem—how to adjust a model such that it no longer performs well on particular training examples.

The DKVB is an approach for learning data from non-stationary distributions (e.g. for continual learning). A fixed, pre-trained encoder is used to generate input-dependent queries for a set of key-value lookup tables. The keys are initialized to cover the full representational space of the encoder and thereafter fixed. The values are used to feed a decoder (which is non-parametric averaging pooling in this work), and the values can be learned. Since each query maps to $k$ keys and only the values associated with those keys are used for decoding, masking key-values belonging to particular samples allows DKVB to be a useful approach for unlearning.

### Strengths
Overall, this is a well-written and motivated paper. The prior work is discussed and the authors successfully position their work as original and significant for tackling the problem in a compute-efficient manner. The ideas presented are intuitive and well-positioned to address the unlearning problem. The results appear promising and the evaluation is correct.

### Weaknesses
 - The authors focus on image classification tasks where the decoder has only one primary output, but for many large-scale pre-trained models such as LLMs, the backbone serves many downstream tasks. Presumably, the decoder will need to produce outputs that apply equally well to all tasks. Whether this is a limitation or an issue of scaling is not discussed.

- The input representation of the encoder seems crucial for separating forget keys from retain keys, but this work has limited discussion and evaluation on how to choose a backbone.

- The current DKVB design appears to be fundamentally limited in its ability to perform instance-specific unlearning. The method relies on masking keys associated with a class, but if individual samples within a class have similar input representations, masking the keys of one sample will likely have minimal effect, as other nearby keys will still activate the same class. This limitation is not sufficiently addressed.

### Questions
1. The bottleneck design necessarily limits the DKVB output to a smaller subset of downstream tasks than the backbone. Do you envision separate DKVBs for different tasks. How does this compare to an approach that directly modifies the backbone for unlearning?
2. While the evaluation includes two different backbones, there is limited discussion of how a backbone's representations affect the DKVB. Do you have recommendations for which layer in the original model should be used as the encoder? Should it always be the full backbone?
3. Related to Question 2, what if you need to forget specific samples (instead of whole classes)? Or have samples in the retain and forget sets with very similar input representations? How does DKVB fair in these settings (there appears to be a little discussion about these limitations, but it might be more helpful to contextualize w.r.t. the DKVB operation)?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a low-compute machine unlearning technique using a discrete representational bottleneck to efficiently erase knowledge of a forget set from trained models with minimal impact on overall performance. Evaluated on datasets like CIFAR-10, CIFAR-100, LACUNA-100, and ImageNet-1k, the method matches or outperforms SCRUB—a state-of-the-art unlearning approach—while incurring negligible computational cost.

### Strengths
- The paper is well-structured, presenting with thorough results and analysis.
- The proposed technique demonstrates effective unlearning performance with minimal computational cost, validated across multiple datasets.

### Weaknesses
 - The work appears to be primarily built upon the DKVB model but applied in a reverse manner. The authors should more explicitly highlight their unique contributions and clarify how their approach differs from DKVB.

- The study focuses only on ViT-B/32 and ResNet-50 models. It's unclear why these particular models were chosen and whether the findings generalize to other architectures.



### Questions
- The paper states that the key initialization is done on the training dataset. Is it sufficient to use only a few batches for initialization, or does it require processing the entire training dataset? If it's the latter, wouldn't this be computationally expensive?

- In the experiments with ImageNet-pretrained ResNet-50 backbones, the retain set test accuracy decreases when the forget set test accuracy approaches zero (Figure 2), whereas in other settings, the retain set accuracy remains almost constant. Could the authors provide an explanation?

- Unclear Symbol on Page 14: There are two "¿" symbol on page 14 whose meaning is not clear. Could the authors clarify its significance?

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
3

### Summary
- This paper presenting unlearning with DKVB (Discrete Key-Value Bottleneck), and studies the class unlearning problem
- It uses the DKVB architecture which uses a pre-trained encoder, followed by discrete key quantization, then maps these keys to values, then trained a linear encoder on these values
- In order to unlearn a class, it records the most commonly used key/values pairs recorded by that class, then removes them from the codebook to unlearn them. (Note there is a difference between two methods of Unlearning with DKVB, examples vs. activations, but this is the broad summary)
- The method is able to unlearn a class with very little effect on the classification accuracy of the remaining classes
- There is a particular emphasis on the low compute cost compared to existing unlearning approaches, as this method does not require access to the original data (in the case of unlearning via activations), in comparison to other methods which do require the original data

### Strengths
- Not requiring access to the original data I believe is very important and this strength should perhaps be stressed more in the paper
- The method requires very little compute compared to existing methods
- Presentation is straightforward an easy to follow

### Weaknesses
 - I think that the presentation of table 1, particularly the bolding is misleading. While it is true that the DKVB unlearning results in the smallest change in the accuracy of the retain set, wouldn't one prefer a performance *increase* on the retain set, as it no longer needs to predict that last class?

 - I think more discussion on multi-class unlearning would be useful. For example the figures in appendix A.3. (figure 5) maybe could be moved into the main text, and comparisons to one of the baseline methods would give a better characteristics of the limits of the approach. At least based on my intuition, this approach could fail if there are many classes being unlearned and "too many" keys/values are removed from the codebook. Can the authors provide any insight on this?

### Questions
- Is the class logit for the forget class removed entirely for the experiments in Table 1?
- Is it possible product similar plots to figure 2 and figure 3 for one of the baseline unlearning methods? For just the smaller datasets such as CIFAR-10/100 would be sufficient
- I think more discussion on multi-class unlearning would be useful. For example the figures in appendix A.3. (figure 5) maybe could be moved into the main text, and comparisons to one of the baseline methods would give a better characteristics of the limits of the approach. At least based on my intuition, this approach could fail if there are many classes being unlearned and "too many" keys/values are removed from the codebook. Can the authors provide any insight on this?

### Soundness
3

### Presentation
3

### Contribution
2
