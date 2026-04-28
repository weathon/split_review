# JOOCI: A FRAMEWORK FOR LEARNING COMPREHENSIVE SPEECH REPRESENTATIONS

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
Information in speech can be divided into two categories: \enquote{what is being said} (content) and \enquote{how it is expressed} (other). Current state-of-the-art (SOTA) techniques model speech at fixed segments, usually 10-25 ms, using a single embedding. Given the orthogonal nature of other and content information, attempting to optimize both within a single embedding results in suboptimal solutions. This approach divides the model's capacity, limiting its ability to build complex hierarchical features effectively. In this work, we present an end-to-end speech representation learning framework designed to jointly optimize the \enquote{other} and \enquote{content} information (JOOCI) in speech. By using separate learnable parameters, JOOCI addresses this optimization challenge by modeling other and content information independently. Our results show that JOOCI consistently outperforms other SOTA models of similar size (100 million parameters) and pre-training data used (960 hours) by a significant margin when evaluated on a range of speech downstream tasks in the SUPERB benchmark, as shown in Table \ref{table:superb}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a method for speech representation learning, particularly, for disentangle content information from non-content information. The paper reported strong experimental results on SUPERB benchmark.

### Strengths
The proposed method is sound. The experimental results on a subset of SUPERB benchmark are strong.

### Weaknesses
 - The novelty is limited. The proposed method is very close to a number of existing works, e.g.:
  - Chan et al., Content-Context Factorized Representations for Automated Speech Recognition, InterSpeech 2022.
  - Zhao et al., CCSRD: Content-Centric Speech Representation Disentanglement Learning for End-to-End Speech Translation, EMNLP 2023.
- The main claim is flawed. The paper claims SOTA on SUPERB. However, it only reports experimental results on a subset of the tasks from SUPERB (7 out of 10).
- The writing needs improvements:
  - Importantly, the name "other encoder" is a poor choice, which causes a lot of confusion for reading. Some simple choices such as "non-content encoder" would do a much better job.
   - Secondly, many small claims are questionable throughout the paper. A few examples:
     - Abstract: content and non-content information are orthogonal -- in the words from the paper, “how it is expressed” depends on “what is being said”
     - Sec 2.2: "Since JOOCI uses separate learnable parameters, the losses are summed directly without requiring
additional hyperparameter tuning." -- The previous paragraph said the opposite: " The GRL scale the gradients during backpropagation by a factor of 1/10, preventing interference with the other loss."
  - Lacks details of the model. While references to prior works is great, for completeness of the paper, you should describe the details of you model clearly, so that the readers understand your approach without having to jumping to many other papers.

### Questions
See Weaknesses section.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a self-supervised speech representation model that combines two encoders, one intended to encode linguistic content and the other intended for "other" content like speaker and emotion information, trained with different losses.  The idea is that, by training a single encoder with a single loss, previous approaches have trouble encoding these two types of information equally well.  The various elements of the model are largely borrowed from previous work, but combined in a new way.  The model is compared in terms of performance on 8 common tasks (from the SUPERB benchmark) to other commonly used models (HuBERT, WavLM), finding improved performance on 4 of the tasks.  The paper also includes some ablation studies and analyses of several model components.

### Strengths
+ Addresses an important need to account for both linguistic and non-linguistic content in speech representation learning.

+ Obtains impressive results on several tasks, including speech recognition and speaker identification.

### Weaknesses
 - Presentation of many details is unclear.  For example, the definition of "content" and "other" is never clearly stated.  Also, the model description is very brief, leaving many details to cited papers or the imagination (for example, is prosody ever/always/sometimes considered "content"?).  Either the writing should be much more precise or the paper should include equations specifying all of the model components.  See some other specific questions below.

- The key claimed contribution is that the model encodes both linguistic and non-linguistic information and that these are disentangled into the two encoders' representations.  However, the results don't quite show this, since the results on tasks are mixed and the analyses don't really demonstrate disentanglement (again see questions below).  Overall, I don't see the community starting to use this model as a replacement for other currently popular models.

- Some of the experiments do not, as far as I can tell, show the claimed findings (see details in "Questions" below).

- The writing is in general hard to follow at times, in part due to many grammatical errors.

### Questions
- The paper states that WavLM the "previous SOTA method".  By what measure is WavLM SOTA?  On what task(s)?

- I don't follow the sentences "As a result, the model cannot fully leverage all layers ... within a single embedding." nor the following sentence "The strategy of dividing the layers..."  Can you clarify what is meant there?

- The description of the split and append layer is a bit hard to follow.

- In Eq. 1, the index d is never used in the summand.  Also, should "MPL" be "L_MPL"?

- In Eq. 3, what exactly are Student^PN and Teacher^RDINO?

- In Table 1, where are the results for FBANK and other competitor methods obtained from?  Citations should be provided.  I also suggest including MS-HuBERT since JOOCI is based on it, and ideally also data2vec which has good results on many SUPERB tasks (but please let me know if you think these would not be relevant for some reason).

- I don't quite follow the sentence "We augment the data very lightly, so not to interfere with the content encoder a lot and divide its capacity."

- The description of the main results in Section 3.2 seems a bit misleading.  The paper states that the "results clearly indicate that JOOCI outperforms the current state-of-the-art (SOTA) models on the majority of tasks, except few ...".  However, in Table 1 JOOCI appears to outperform other models on exactly half the tasks, and it is never explained in what sense those models are SOTA (though they are clearly commonly used models).

- I do not understand the purpose of the comparison in Table 2, since JOOCI is not an alternative to adapters.  Also, "Houlsby" and "CHAPTER" need to be defined.  

- How does Figure 2 show the effect of data augmentation?  Is there a pair of curves that differs only in the use of data augmentation?

- For Figure 2, more information is needed about the y-axis.  How is CCA similarity defined?  How are the word labels encoded and how many words are there?  There has been prior work using CCA similarity for layer-wise analyses, e.g. Pasad et al., "Comparative layer-wise analysis of self-supervised speech models," ICASSP 2023.  Figure 2 seems similar to some of this prior work, and so it would also be helpful to state how your CCA-based analysis is the same or different, and whether your HuBERT results are similar to Pasad et al.'s.

- The ablation study in Sec. 4.1 is a bit confusing to me.  It claims to separately show the effect of DGRL and data augmentation, but as far as I can tell these two variables are changed simultaneously in the experiments.

- In Table 3, why are the "-" results not included?  If those could be included, they could help to show to what extent JOOCI-C and JOOCI-O specialize for linguistic vs. non-linguistic information.

- In Section 4.2, I have trouble following the first paragraph.  What kind of information is considered "higher-level" in the "other" branch, and what is the "same trend" that is referred to here?

- Section 4.3 claims to "prove that JOOCI is able to disentangle content and other information", but I don't follow how the results show this.  (Also, the word "prove" is too strong here, as in most descriptions of empirical findings.)

- In Table 5, what is the difference between the experiments in the last two lines (both labeled "JOOCI (6-11)"?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This submission introduces a framework for distinct representation learning of "content" and "other" properties in speech. The authors report improved performance on certain SUPERB tasks compared to other systems. Additionally, the submission includes comparisons with adapters, ablation studies on encoders, data augmentation, and learned representations.

### Strengths
* The research community is highly interested in the topic of speech representation learning.
* The proposed method's evaluation on certain SUPERB tasks yielded better results compared to the cited systems.
* The discussions and comparisons presented are technically sound.

### Weaknesses
Major issues:

* The model's effectiveness is unconvincing. The baselines cited are outdated and not state-of-the-art, and the model's performances on the semantic tasks are not better. Specifically, while the authors claim improvements on some SUPERB tasks, the gains are not substantial enough to demonstrate a significant advancement over existing methods. The choice of baselines, which appear to be lagging behind current state-of-the-art models, makes it difficult to assess the true potential of the proposed approach. The lack of clear improvements on semantic tasks further weakens the argument for the model's effectiveness in capturing meaningful speech representations.
* The paper's discussion of different model architectures is shallow, limiting its contribution and making it difficult to draw general conclusions. The analysis lacks depth, failing to explore the nuances of how different architectural choices impact the learned representations and downstream task performance. The paper does not provide sufficient detail on the specific architectural variations considered, nor does it offer a rigorous analysis of why certain architectures might be better suited for this task than others.

Minor:

* Figure 1 could be simplified by removing the hyperparameters.
* The discussion of "Data augmentation" in Line 52 seems out of place, as the initial focus was on model architecture for speech representation learning.

### Questions
* Can you offer insights into the relationship between SUPERB downstream task performance and model architecture designs?
* How do your results compare to recent speech representation work that has also been evaluated on SUPERB?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes to disentangle the content "what is being said" and other “how it is expressed” information present in the speech data. The paper proposes the JOCCI framework, which uses two submodules, focused on maximizing the content and the other information. The content module is trained with a self-supervised objective whereas, the other module is optimized with a teacher-student objective. A regularization loss is added to minimize the information overlap in the two submodules.

### Strengths
1) The paper is well-written and addresses an important challenge of disentangling content and other information in the speech representation.

2) The model performs well on the SUPERB benchmark and outperforms HuBERT and wavLM.

### Weaknesses
1) The baseline comparisons are limited. There have been other attempts to remove other information such as speaker information from the self-supervised representations such as contentvec[1] and SPIN[2]. Even the MS-HuBERT model used for initializing JOCCI is missing from Table 1.

2) JOCCI relies on a pretrained method RDINO for training the other encoder whereas baseline methods such as HuBERT do not. The use of RDINO, which is trained on an additional 2.5k hours of data, gives JOCCI an unfair advantage in terms of data seen during pretraining, making claims of data efficiency questionable. The paper also claims that the GRL module is used to prevent the other encoder from specializing in speaker information, but the RDINO teacher is trained to generate speaker embeddings, creating a contradiction in the training process.

[1] “Contentvec: An improved self-supervised speech representation by disentangling speakers

[2] Self-supervised Fine-tuning for Improved Content Representations by Speaker-invariant Clustering

### Questions
1) How does the JOCCI compare to the contentvec, SPIN, and Data2vec models?

2) What is the impact of initialization on the model performance e.g. random vs Ms-HuBERT initialization 

3) Can the model be trained with just the GRL loss and without the RDINO teacher?

### Soundness
3

### Presentation
3

### Contribution
2
