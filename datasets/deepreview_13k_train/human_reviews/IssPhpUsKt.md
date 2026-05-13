# Improving Reasoning Performance in Large Language Models via Representation Engineering

- Decision: Accept
- Scores: 6, 6, 8, 8, 6

## Abstract
Recent advancements in large language models (LLMs) have resulted in increasingly anthropomorphic language concerning the ability of LLMs to reason. Whether reasoning in LLMs should be understood to be inherently special is, however, widely debated. We propose utilizing a representation engineering approach wherein model activations are read from the residual stream of an LLM when processing a reasoning task. The activations are used to derive a control vector that is applied to the model as an inference-time intervention, modulating the representational space of the model, to improve performance on the specified task. We additionally open-source the code for deriving control vectors and analyzing model representations. The method allows us to improve performance on reasoning benchmarks and assess how control vectors influence the final logit distribution of a model via metrics such as KL divergence and entropy. We apply control vectors to Mistral-7B-Instruct and a range of Pythia models on an inductive, a deductive and mathematical reasoning task. We show that an LLM can, to a certain degree, be controlled to improve its perceived reasoning ability by modulating activations. The intervention is dependent upon the ability to reliably extract the model's typical state when correctly solving a task. Our results suggest that reasoning performance can be modulated in the same manner as other information-processing tasks performed by LLMs and demonstrate that we are capable of improving performance on specific tasks via a simple intervention on the residual stream with no additional training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes improving reasoning performance of LLMs through representation engineering. The authors introduce the "control vector" derived from the residual stream of the model as an inference-time intervention, which modulates the representational space to enhance reasoning capabilities without additional training. The approach is evaluated on inductive (indirect-object identification) and deductive (bAbI) reasoning tasks with models from the Pythia suite and Mistral-7B-Instruct. The authors suggest that the intervention improves task performance and reasoning may not fundamentally differ from other token generation tasks implied by the results.

### Strengths
**Originality:** The representation engineering approach utilizing the residual stream for reasoning task offers a novel view. 

**Quality:** The study is methodologically clear. The use of models at varying scales and the combination of several metrics (accuracy, KL divergence, entropy) offers a comprehensive evaluation.

**Clarity:** The paper clearly explains the steps for deriving control vectors.

**Significance:** The problem of whether reasoning requires distinct treatment than other tasks is important.

### Weaknesses
1. **Task complexity**: The reasoning tasks (IOI and bAbI) used are relatively simple, potentially limiting the conclusions drawn about "reasoning" in general. Results might differ on more challenging tasks. Specifically, mathematical reasoning has received great attention as a difficult type of reasoning and has been widely adopted as benchmarks for LLMs. Could you add addtional experiments on the GSM8K or MATH dataset to explore how this approach applies to more complex reasoning tasks?
2. **Model scope**: Testing is limited to smaller models (up to 7B parameters), which could restrict applicability of the conclusions. Larger models might capture reasoning dynamics differently and yield varied results under similar interventions. Could you include experiments for Pythia-12B to investigate how the method scales with model size?
3. **Hyperparameter choice:** As indicated by the experimental results, the choice of $\alpha$ actually dominates the final outcome. However the paper does not provide a systematic procedure to choose $\alpha$ beforehand. To make the framework applicable to a wide range of tasks and models, could you provide a general routine to determine the value of $\alpha$ and its interpretation?
4. **Contrastive pair selection and control vector derivation:** The paper uses random character strings as "negative" samples and PCA-based control vectors according to empirical performance. I wonder if we can gain more insights for these choices. Could this empirical advantage be due to the nature of IOI task, where answers could be semantically correct but not expected? This is also why I suggest to include math reasoning in point 1, where ambiguity of answers is minimized. Could you report the results for different types of contrastive prompts (e.g., partially correct responses) on the GSM8K / MATH dataset to investigate how they impact control vector efficacy?
5. **Experiment settings:** The Pythia models are only reported for the IOI task, which seems insufficient to me. Could you provide results of Pythia-1.4B & Pythia-2.8B on the bAbI task also?
6. **Result interpretation:** If I understand the figures correctly, there is an apparent decrease for B & BL condition and almost no improvement for A & AL condition with the Pythia-2.8B model in logit-based accuracy. This raises my doubts about the effectiveness of the approach and is probably my biggest concern. The performance gap between A condition and B condition may imply the statistical learning bias in disguise rather than genuine reasoning. Therefore the conclusion that "there is no intrinsic difference between the process of reasoning and other information-processing tasks performed by LLMs" does not seem valid to me. Could you make further explanation regarding this experiment result?

### Questions
See Weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper uses control vectors with a residual stream added to transformers, trained using contrastive prompt pairs, to improve reasoning ability in a couple of tasks. Some improvement is achieved with some ranges of a controlling parameter alpha.

### Strengths
- This is an insightful technique that can shed light on the behaviour of LLM and reasoning.
- Well written.

### Weaknesses
 - Novelty. They apply an existing technique, adapting it to a couple of architectures and deriving prompts pairs for 

- The results are only slightly better for some ranges of alpha. 

- Very few models, very small models, and just two datasets.

- The insights about reasoning are somewhat limited. They say that "reasoning is not neccesarily different from any other form of processing done by LLMs". This is either a tautology if we are assuming that LLMs do reasoning or needs to be compared to some other kinds of specific processing that are not reasoning, such as perhaps retrieval, etc. If the meaning is that the patterns are no different, then the paper should compare with the other patterns. In any case, for two tasks, it's limited how much we can extrapolate for the understanding of what reasoning is.

- The second task (IOI) is too simple, and in some cases, as the authors say, the answer is not fully specified.

Minor
- "illustrated in 1" -> "illustrated in Figure 1"

### Questions
- How can we find the best alpha in a new deployment situation?

- How does it compare to chain-of-thought or a fine-tuning that highlights the prompts that are associated with good reasoning and bad reasoning? Can a similar information be provided contextually?

- Why do the contrastive pairs have to be associated with good and bad prompts instead of good and bad reasoning instance?

- What do you mean by: "We furthermore cannot expect to be able to improve a model on a task it
cannot correctly solve when the method of improving a model is derived directly from it’s [sic] own
hidden states."? The whole purpose is to improve the model on instance it wouldn't solve without the residual stream?

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
3

### Summary
The paper proposes a new way to improve reasoning in LLMs via representatoin engineering. It basically reads activations from the residual streams of LLMs during reasoning, derives a control vector from this, and applies this vector during inference time to modulate the representation space. The results are evaulated on inductive and deductive reasoning tasks using Pythia and Mistral Instruct 7B. This intervention seems to improve reasoning without further training, which suggests that reasoning is not too different from other information processing done by LLMs.

### Strengths
Originality - As far as I am aware, such control vector intervention is a new idea, and the proposed framework for deriving control vectors and their impact (KL div, entropy) is a useful contribution.

Clarity - The paper explains its methods and findings in a structured and thoughtful way. The transformer architecture for conceptually reframing this problem is helpful.

Significance - I think the result that reasoning is an emergent general information processing ability is useful and important.

### Weaknesses
1. The paper only tests the approach on two models. Larger models will need to be used to validate these findings.
2. I think the IOI task is too simple, even though the bABI task is representative. The authors should explore a wider range of reasoning tasks to strengthen the conclusions.
3. The contrastive approach using random strings seems a bit arbitrary. Probably a more principled method would be more fruitful.
4. The probability mass results seem to disagree a little with the entropy KL divergence results.

### Questions
1. How does performance intervention compare to finetuning? I believe that would be a fair baseline.
2. Are there any hypotheses as to why there is disagreement between the KL divergence and entropy results?
3. Is performance intervention sensitive to layer choice? How so?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a method to elicit improved reasoning from LLMs at inference time. Similar to inducing writing style or emotional valence, the researchers suggest that reasoning ability is a controllable characteristic which can be suppressed or enhanced. 

Using representation engineering, they read residual stream activations from a training set containing positive and negative reasoning trajectories, and these are used to derive a control vector which, colloquially speaking, points in the “better reasoning” direction. In order to improve results, the paper uses contrastive pairs, and further takes only the strongest PCA component of the pairs in order to only select for the “better reasoning dimension”. At inference time, it is applied to the residual stream to improve the model’s reasoning capabilities. 

The paper carries out experiments on a bAbI simple deductive reasoning dataset task and the indirect-object-identification (IOI) task. These are applied to two Pythia models and a larger Mistral-7B-Instruct which demonstrate that applying this method yields improved results compared to the baseline (average probability of correct vs. incorrect). It also shows that the model’s entropy and KL divergence are modified due to this intervention as one would expect.

### Strengths
Strong points:
The paper provides a clear overview of the motivation and methodology. It is well-structured and self contained.  
The paper performs a simple and novel training-free application of an existing method to improve basic capability of LLMs, where it was previously only used for eliciting style modifications. While other papers have shown that, e.g. truthfulness exists as a direction (or control vector) in representation space, it may still be counterintuitive that a capability such as reasoning is also a “direction” in representation space. 
The paper uses auxiliary methods (Entropy & KL divergence) to analyze the results of applying this method. 
The paper’s most validating result, as mentioned in the results section: an 8% improvement in the bAbi task over baseline.

### Weaknesses
Method:
The paper reports a successful application of the method to two datasets. Due to the need for contrastive pairs in order to generate the control vector, it requires positive (good reasoning) and  negative ones (bad reasoning).
The paper discusses 3 schemes for generating the “negative” pairs:
- Asking the model to produce an incorrect answer. This, as the paper notes, is not really a negative example since the model uses correct reasoning when generating an incorrect answer.
- Selecting cases in which model response is not the expected one (which, as the paper notes may still be “not actually wrong” just not the expected answer)
- Selecting a random string of 75 letters as the model’s output reasoning trajectory, which is surely “wrong”. This is pointed out correctly as being ‘unnatural’.

There are a couple of points that are not clarified:
- The paper mentioned testing the latter two schemes, but it is unclear from the results how these are tested. This should be explained in detail (e.g. are they equally mixed as negatives. This requires clarification (or perhaps an ablation study to understand the effects).
  Please provide details on how the different negative example schemes were combined or compared in their experiments. 
- Furthermore, without analyzing the errors made by the model, it is not entirely obvious that either of these schemes actually push the model towards correct reasoning. For example, if most errors are “out of distribution” as in the example in the paper: ”Mary[A] and John[B] went to the store. John[B] gave the groceries to Carl[C], merely forcing the model to remain “within” distribution of tokens it’s already seen will already improve its results even if the modified reasoning paths only choose names at random from A and B. Similarly, making sure the model is pushed away from random strings of letters will do the same, and it is hard to say if reasoning has indeed been improved, as in each case (bABi and IOI) there appears to be a natural incorrect token (the “other name”) measuring its probability as an additional measure (as opposed to just the correct token) may help understand these issues better. It is also unclear how the different negative examples are weighted, or if they are treated equally, and how this impacts the results.

Results and analysis:
It is stated that the entropy is expected to decrease as the model veers towards the correct token, concentrating its mass to it. This would mean that it would be negatively correlated with accuracy. However, this does not appear to be the case for Figure 4, the bAbi on Mistral, unless I missed something. In fact the opposite appears to be true. In this plot the entropy also appears to be positively correlated with the probability mass, which requires explanation. If this is indeed the case, please provide a more detailed analysis of the result, and possibly the discuss the correlation between these results.

### Questions
The main questions the paper would benefit from answering (following the above discussion) to strengthen the claim:
1. Is the “reasoning” task specific? Does it benefit other tasks? 
2. Which types of incorrect reasoning are reduced when using the method? 
Either analyzing the errors or showing improved reasoning on a held-out reasoning task (i.e. using an OOD reasoning task) would strengthen the claims appearing in the paper, which can be argued to be at least somewhat related to non-reasoining improvements. 

Following the points from above:
- Please explain how the negative sample for the contrastive pairs were constructed or show an ablation study
- Please explain whether the entropy behaves as expected for the Mistral result. 

A few more minor points that would improve readability and clarify confusions: 
1. Unless I missed something, the paper does not explain how the reading vector (or control vector) is constructed from the latent representation of the examples. Specifically, there are several tokens in each prompt, and it is not clear how these are treated. It is implicitly understood from the notation that this is not per-token, so perhaps the last one is taken. It would be useful if explained explicitly (perhaps even discuss different design choices), possibly by providing psuedocode, formulas or a diagram.
2. The claims are that the results are improved for all tasks but in different directions. This is taken to mean “different sign of alpha” but it is not clear. There appears to be no natural direction, possibly(?) due to the PCA process. 
3. The evaluation as scoring from logits makes sense, but it is not explained how these are chosen, and so possibly may be a source of confusion. 
3. It is stated that the KL divergence is expected to rise linearly with alpha, and reported that this is indeed the case. Looking at the plots (Figures 3,4) this seems to be quadratic in nature for the larger models, so it rises linearly with the magnitude of alpha, not with alpha.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work uses the control vector method to promote task-performant representations in LLMs for IOI and certain bAbI tasks, using a new (but unspecified) software framework, with moderate success. The paper's substantive claims are:

1. These tasks are reflective of LLM reasoning ability
2. The corresponding task-representation vectors in the residual stream are appropriately representative of reasoning in LLMs
3. The observed increase in task-performance after applying the method is evidence for an improvement in reasoning as a broad faculty (as opposed to only the specific task at hand.)
4. There is no intrinsic difference between reasoning and other information-processing tasks as far as an LLM is concerned.

### Strengths
It is very clearly presented what the paper wishes to achieve, and the methodology is clear.
The introduction adequately situates this work in the context of prior work in the field.
To the best of my knowledge, the control-vector method has not been tried before on this particular task.
I particularly enjoyed the meticulous introduction that covered the conceptual and mathematical bases for the remainder of the work; it read well as a mini-tutorial on the techniques used here.

### Weaknesses
It feels as if this paper wanted to be about a software tool or framework, but "reasoning" was more attractive as a topic.
Of the four substantive claims concerning reasoning, I don't think a single one is substantiated.
These 4 criticisms are the foundations of my current stance on the paper, and I would be happy to raise my score accordingly if these concerns were adequately addressed (by e.g. weakening claims or strengthening their support.)

1. The tasks are reflective of LLM reasoning ability.

That is a stretch, right? IOI is out of the question. bAbI is a sort of edge-case, but consider that Weston et al frame the suite as toy tasks, and that the success of various memorisation architectures on the taskset afterwards have prompted the development of new benchmarks that aren't hackable by exploiting statistical regularities. The claim that this is about "Reasoning" is too heavy for the experimental foundations.

2. The corresponding task-representation vectors in the residual stream are appropriately representative of reasoning in LLMs

This is essentially what the paper needs to establish the existence or nonexistence of empirically; that there exists some broad and task-general faculty in LLMs (that we would call Reasoning), and that this faculty has a manipulable representation in the residual stream. Even if I am willing to take all the literature on residual streams at face value, the onus is still on the authors to establish that the tasks they have chosen are really reflective of Reasoning --- that's claim 1.

3. The observed increase in task-performance after applying the method is evidence for an improvement in reasoning as a broad faculty (as opposed to only the specific task at hand.)

This is crucial. If applying the control vector only improves an LLMs ability to do bAbI tasks, then we're not saying anything about a capacity to Reason: we would instead call it "a capacity to do bAbI", similarly to a "capacity to play chess". If the authors insist on framing the contribution around Reasoning, then at least there ought to be some evidence of generality: if it turns out that boosting performance for bAbI also increases performance on the GSM suite or ARC or anything else, then that would be very interesting to see! Due to the "context-freeness" of Reasoning, there is no way around this particular hurdle apart from empirical demonstration of the efficacy of the technique in general performance boosts across substantially different domains. I can't see any way to get around this purely rhetorically: whatever argument X the authors would like to make that their current experimental basis is sufficient evidence for improvement at a broad capacity for Reasoning, I can take that argument X and apply it for the cited work (line 59) that residual stream modification improves chess and othello performance, undermining the authors' claims to conceptual novelty.

4. There is no intrinsic difference between reasoning and other information-processing tasks as far as an LLM is concerned.

It's unclear that the empirical observations obtained in this work are sufficient to substantiate this claim. It does not help the matter that the authors deliberately avoid taking any stance on characterising what Reasoning might be, or what properties it might or might not have (lines 38, 438), which makes it difficult to evaluate what the claim is even supposed to mean. I would like to view this refusal to take a stance on what-Reasoning-is charitably as scholarly circumspection, but when juxtaposed with unsubstantiated claims about Reasoning ability in LLMs, I'm afraid that citations like Johnson-Laird read more like a checklisting exercise than material engagement with the literature.

### Questions
- If you are framing this around "Reasoning", what kinds of philosophical commitments are you making? For example, it seems you implicitly want to frame reasoning as something that cannot be characterised purely behaviouristically, which would necessitate the kind of "going into internal representational structure" that you seem to want to frame the control-vector technique as; so maybe it's worth doubling down on Reasoning as something involving mental states and representations with causal force. However, since you also want to conclude that reasoning is not an innately distinguished ability in LLMs, are you implicitly discounting prompt-level interventions such as CoT and their efficacy at improving task performance? What conception of Reasoning makes it amenable to be improved by residual stream modification but apparently not by structured CoT?

- Why is there nothing about the software? Evidently it was a useful suite of tools to have gotten you through all of the experiments, why say nothing about it?

### Soundness
2

### Presentation
3

### Contribution
2
